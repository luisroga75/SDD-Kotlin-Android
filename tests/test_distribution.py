"""Distribution smoke tests; never touch the user's actual skills."""
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_skill import install
from sync_packages import sync


class DistributionTests(unittest.TestCase):
    def test_synced(self):
        self.assertEqual(sync(check=True), [])

    def test_independent_packages(self):
        with tempfile.TemporaryDirectory() as folder:
            for agent in ("codex", "claude-code"):
                package = install(agent, home=folder)
                for name in ("SKILL.md", "references/entrevista.md", "assets/templates/spec.md", "scripts/audit_sdd.py"):
                    self.assertTrue((package / name).is_file(), name)
                result = subprocess.run([sys.executable, "-B", str(package / "scripts/test_audit_sdd.py")], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual((package / "agents/openai.yaml").exists(), agent == "codex")

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            package = install("codex", home=folder)
            original = (package / "SKILL.md").read_bytes()
            with self.assertRaises(FileExistsError):
                install("codex", home=folder)
            self.assertEqual((package / "SKILL.md").read_bytes(), original)

    def test_legacy_codex_not_duplicated(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / ".codex/skills/android-kotlin-sdd").mkdir(parents=True)
            with self.assertRaises(FileExistsError):
                install("codex", home=folder)

    def test_dry_run(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = install("claude-code", home=folder, dry_run=True)
            self.assertFalse(destination.exists())
            self.assertEqual(list(Path(folder).iterdir()), [])

    def test_project_install(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = install("claude-code", "project", folder)
            self.assertEqual(destination, Path(folder) / ".claude/skills/android-kotlin-sdd")

    def test_invalid_arguments(self):
        for kwargs in ({"agent": "other"}, {"agent": "codex", "scope": "other"}, {"agent": "codex", "scope": "project"}, {"agent": "codex", "project": ROOT}):
            with self.assertRaises(ValueError):
                install(**kwargs)

    def test_local_markdown_links(self):
        for agent in ("codex", "claude-code"):
            package = ROOT / agent / "android-kotlin-sdd"
            for file in package.rglob("*.md"):
                if "assets" in file.relative_to(package).parts:
                    continue  # Template links target the future app, not this package.
                for link in re.findall(r"\]\(([^)]+)\)", file.read_text()):
                    if "://" in link or link.startswith("#"):
                        continue
                    self.assertTrue((file.parent / link.split("#")[0]).exists(), f"{file}: {link}")


if __name__ == "__main__":
    unittest.main()
