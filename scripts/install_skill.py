#!/usr/bin/env python3
"""Install one local package without network or overwriting existing skills."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
NAME = "android-kotlin-sdd"


def install(agent, scope="user", project=None, home=None, dry_run=False):
    if agent not in ("codex", "claude-code"):
        raise ValueError("Agente no válido")
    if scope not in ("user", "project"):
        raise ValueError("Ámbito no válido")
    source = ROOT / agent / NAME
    if not (source / "SKILL.md").is_file():
        raise ValueError("Falta la carpeta completa de la skill")
    if source.is_symlink() or any(p.is_symlink() for p in source.rglob("*")):
        raise ValueError("No se instalan paquetes con symlinks")
    if scope == "project":
        if project is None or not Path(project).is_dir():
            raise ValueError("Indica con --project una raíz de proyecto existente")
        base = Path(project).resolve()
    else:
        if project is not None:
            raise ValueError("--project solo se utiliza con --scope project")
        base = Path(home) if home is not None else Path.home()
        if agent == "codex" and (base / ".codex/skills" / NAME).exists():
            raise FileExistsError("Ya existe la instalación compatible en .codex/skills; revísala para evitar duplicados")
    destination = base / (".agents" if agent == "codex" else ".claude") / "skills" / NAME
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Ya existe {destination}; no se sobrescribe. Revisa y respalda antes de actualizar.")
    if not dry_run:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=("codex", "claude-code"))
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--project", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        destination = install(args.agent, args.scope, args.project, dry_run=args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"No instalado: {exc}\n")
    print(("Destino previsto: " if args.dry_run else "Instalado en: ") + str(destination))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
