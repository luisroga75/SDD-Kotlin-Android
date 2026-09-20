#!/usr/bin/env python3
"""Read-only structural audit of the bundled SDD document convention.

No dependencies, Gradle execution, network access or project writes.
Textual references are not proof that requirements are implemented or tested.
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


FEATURE = re.compile(r"^([0-9]{3,})-[a-z0-9]+(?:-[a-z0-9]+)*$")
DEFINITION = re.compile(r"^\s*-\s+((?:RF|RNF)-[1-9][0-9]*):\s*(.+)$", re.M)
REQ_REF = re.compile(r"(?<![\w/-])(?:([0-9]{3,}-[a-z0-9-]+)/)?((?:RF|RNF)-[1-9][0-9]*)\b")
TASK = re.compile(r"^\s*- \[([ xX])\] (T[1-9][0-9]*)[.:]\s+(.+)$", re.M)
TASK_REF = re.compile(r"(?<![\w/-])(?:([0-9]{3,}-[a-z0-9-]+)/)?(T[1-9][0-9]*)\b")
UNRESOLVED = re.compile(r"\{\{[^}]+\}\}|\[NECESITA ACLARACI[ÓO]N[^\]]*\]", re.I)


def audit(root, ready=False, agent="codex"):
    root = Path(root).resolve()
    errors, warnings = [], []
    result = {"project": str(root), "mode": "ready" if ready else "draft",
              "features": [], "errors": errors, "warnings": warnings}

    def gap(message):
        (errors if ready else warnings).append(message)

    def read(path):
        if not path.resolve().is_relative_to(root):
            errors.append(f"Ruta fuera del proyecto: {path}")
            return ""
        if not path.is_file():
            gap(f"Falta {path.relative_to(root)}")
            return ""
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"No se puede leer {path}: {exc}")
            return ""
        if not text.strip():
            gap(f"Archivo vacío: {path.relative_to(root)}")
        if UNRESOLVED.search(text):
            gap(f"Marcador o aclaración pendiente: {path.relative_to(root)}")
        return text.replace("**", "").replace("`", "")

    if not root.is_dir():
        errors.append("La raíz indicada no existe o no es un directorio.")
        return result
    if agent not in ("codex", "claude", "both"):
        errors.append("Agente desconocido.")
        return result
    if agent in ("codex", "both"):
        read(root / "AGENTS.md")
    if agent in ("claude", "both"):
        instructions = read(root / "CLAUDE.md")
        if agent == "claude" and re.search(r"^@(?:\./)?AGENTS\.md\s*$", instructions, re.M):
            read(root / "AGENTS.md")
    read(root / "docs" / "constitution.md")
    specs = root / "specs"
    if not specs.resolve().is_relative_to(root):
        errors.append("El directorio specs apunta fuera del proyecto.")
        return result
    folders = sorted(p for p in specs.iterdir() if p.is_dir() and FEATURE.fullmatch(p.name)) if specs.is_dir() else []
    if not folders:
        gap("No hay carpetas specs/NNN-nombre; otros formatos requieren revisión manual.")
        return result
    for number, count in Counter(int(FEATURE.fullmatch(p.name)[1]) for p in folders).items():
        if count > 1:
            errors.append(f"Número de spec duplicado: {number:03d}")

    documents, requirements, active, tasks = {}, {}, {}, {}
    for folder in folders:
        name = folder.name
        result["features"].append(name)
        documents[name] = {file: read(folder / file) for file in ("spec.md", "plan.md", "tasks.md")}
        definitions = DEFINITION.findall(documents[name]["spec.md"])
        ids = [identifier for identifier, _ in definitions]
        requirements[name] = set(ids)
        active[name] = {identifier for identifier, body in definitions if not body.startswith("[RETIRADO]")}
        if not any(identifier.startswith("RF-") for identifier in active[name]):
            gap(f"{name}: no hay RF activos con formato '- RF-1: ...'.")
        for identifier, count in Counter(ids).items():
            if count > 1:
                errors.append(f"{name}: definición duplicada de {identifier}.")
        matches = list(TASK.finditer(documents[name]["tasks.md"]))
        tasks[name] = {}
        for index, match in enumerate(matches):
            done, identifier, title = match.groups()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(documents[name]["tasks.md"])
            body = documents[name]["tasks.md"][match.end():end]
            # A section heading ends the final task before coverage tables.
            body = re.split(r"^#{1,6}\s", body, maxsplit=1, flags=re.M)[0]
            if identifier in tasks[name]:
                errors.append(f"{name}: tarea duplicada {identifier}.")
            tasks[name][identifier] = (done.lower() == "x", title, body)
        if not matches:
            gap(f"{name}: no hay tareas con formato '- [ ] T1. ...'.")

    graph = {}
    for name, files in documents.items():
        for file, text in files.items():
            for target, identifier in REQ_REF.findall(text):
                target = target or name
                if identifier not in requirements.get(target, set()):
                    errors.append(f"{name}/{file}: referencia inexistente {target}/{identifier}.")
        in_plan = {identifier for target, identifier in REQ_REF.findall(files["plan.md"]) if not target or target == name}
        in_tasks = set()
        for identifier, (done, title, body) in tasks[name].items():
            node = f"{name}/{identifier}"
            graph[node] = []
            rf_line = re.search(r"^\s*-?\s*RF:\s*(.+)$", body, re.M)
            if not rf_line:
                gap(f"{node}: falta campo RF (o justificación de infraestructura).")
            else:
                in_tasks.update(ref for target, ref in REQ_REF.findall(rf_line[1]) if not target or target == name)
            for field in ("Hecho cuando", "Verificación", "Dependencias"):
                if not re.search(rf"^\s*-?\s*{field}:\s*\S", body, re.M):
                    gap(f"{node}: falta {field}.")
            dependency = re.search(r"^\s*-?\s*Dependencias:\s*(.+)$", body, re.M)
            if dependency:
                for target, ref in TASK_REF.findall(dependency[1]):
                    target = target or name
                    graph[node].append(f"{target}/{ref}")
                    if ref not in tasks.get(target, {}):
                        errors.append(f"{node}: dependencia inexistente {target}/{ref}.")
            if done:
                evidence = re.search(r"^\s*-?\s*Evidencia:\s*(.+)$", body, re.M)
                if not evidence or re.search(r"no ejecutad[ao]|pendiente|sin evidencia|\{\{", evidence[1], re.I):
                    errors.append(f"{node}: marcada completa sin evidencia registrada.")
        for identifier in sorted(active[name]):
            if identifier not in in_plan:
                gap(f"{name}/{identifier}: sin referencia en plan.md.")
            if identifier not in in_tasks:
                gap(f"{name}/{identifier}: sin cobertura en campos RF de tareas.")

    visiting, visited = set(), set()

    def visit(node, trail):
        if node in visiting:
            errors.append("Ciclo de tareas: " + " -> ".join(trail + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency, trail + [node])
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node, [])
    result["errors"] = list(dict.fromkeys(errors))
    result["warnings"] = list(dict.fromkeys(warnings))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--ready", action="store_true", help="Exige documentos listos para implementar.")
    parser.add_argument("--json", action="store_true", help="Resultado estructurado.")
    parser.add_argument("--agent", choices=("codex", "claude", "both"), default="codex")
    args = parser.parse_args()
    report = audit(args.project, args.ready, args.agent)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Specs revisadas: {len(report['features'])}; modo: {report['mode']}")
        for item in report["errors"]:
            print(f"ERROR: {item}")
        for item in report["warnings"]:
            print(f"AVISO: {item}")
        print("Auditoría estructural: " + ("con errores" if report["errors"] else "sin errores"))
        print("No acredita implementación, cobertura semántica ni resultados de pruebas Android.")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
