#!/usr/bin/env python3
"""Generate self-contained packages from canonical root resources."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ("codex", "claude-code")


def shared_files(root):
    paths = []
    for part in ("references", "assets"):
        paths.extend(p for p in (root / part).rglob("*") if p.is_file())
    paths.extend(root / "scripts" / name for name in ("audit_sdd.py", "test_audit_sdd.py"))
    return {p.relative_to(root): p for p in paths}


def sync(root=ROOT, check=False):
    problems = []
    for agent in AGENTS:
        package = root / agent / "android-kotlin-sdd"
        expected = shared_files(root)
        if agent == "codex":
            expected[Path("SKILL.md")] = root / "SKILL.md"
            expected[Path("agents/openai.yaml")] = root / "agents/openai.yaml"
        elif not (package / "SKILL.md").is_file():
            raise ValueError("Falta la entrada propia de Claude Code")
        allowed = set(expected) | {Path("SKILL.md")}
        for path in package.rglob("*"):
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                if path.relative_to(package) not in allowed:
                    problems.append(f"Archivo extra, revisar manualmente: {path}")
        for relative, source in expected.items():
            destination = package / relative
            if source.is_symlink() or any(p.is_symlink() for p in (destination, *destination.parents)):
                raise ValueError("No se admiten symlinks en la distribución")
            if not destination.is_file() or source.read_bytes() != destination.read_bytes():
                if check:
                    problems.append(f"Recurso desincronizado: {destination}")
                else:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(source, destination)
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    problems = sync(check=args.check)
    for problem in problems:
        print(problem)
    print("Paquetes sincronizados" if not problems else "Revisar distribución")
    return bool(problems)


if __name__ == "__main__":
    raise SystemExit(main())
