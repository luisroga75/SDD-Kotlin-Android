"""Observable invariants of the read-only checker; isolated temporary fixtures."""

import tempfile
import unittest
from pathlib import Path

from audit_sdd import audit


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="android-sdd-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "AGENTS.md").write_text("# Proyecto de prueba\n", encoding="utf-8")
        (self.root / "docs/constitution.md").write_text("# Principios comprobables\n", encoding="utf-8")

    def feature(self, name="001-recordatorios", dependency="ninguna"):
        folder = self.root / "specs" / name
        folder.mkdir(parents=True)
        (folder / "spec.md").write_text("# Spec\n- RF-1: CUANDO se guarda, EL SISTEMA mostrará el registro.\n", encoding="utf-8")
        (folder / "plan.md").write_text("# Plan\nRepositorio y pantalla cubren RF-1; test de guardado.\n", encoding="utf-8")
        (folder / "tasks.md").write_text(
            f"# Tareas\n- [ ] T1. Guardar\n  - RF: RF-1\n  - Dependencias: {dependency}\n"
            "  - Hecho cuando: el registro se muestra tras guardarlo.\n"
            "  - Verificación: prueba del recorrido de guardado.\n"
            "  - Evidencia: no ejecutada.\n", encoding="utf-8")
        return folder

    def test_valid_readiness_and_no_writes(self):
        self.feature()
        before = {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        report = audit(self.root, ready=True)
        self.assertEqual(report["errors"], [])
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_missing_task_coverage_even_if_in_table(self):
        folder = self.feature()
        task = folder / "tasks.md"
        task.write_text(task.read_text().replace("RF: RF-1", "RF: ninguno (infraestructura)") + "\n## Cobertura\nRF-1 | T1\n")
        self.assertTrue(any("sin cobertura" in e for e in audit(self.root, True)["errors"]))

    def test_cross_spec_dependencies_and_local_ids(self):
        self.feature()
        self.feature("002-sincronizacion", "001-recordatorios/T1")
        self.assertEqual(audit(self.root, True)["errors"], [])

    def test_cycle_across_specs(self):
        self.feature(dependency="002-sincronizacion/T1")
        self.feature("002-sincronizacion", "001-recordatorios/T1")
        self.assertTrue(any("Ciclo" in e for e in audit(self.root, True)["errors"]))

    def test_duplicate_and_unknown_requirement(self):
        folder = self.feature()
        spec = folder / "spec.md"
        spec.write_text(spec.read_text() + "- RF-1: Repetición.\n")
        (folder / "plan.md").write_text("RF-1 y RF-99\n")
        errors = audit(self.root, True)["errors"]
        self.assertTrue(any("duplicada" in e for e in errors))
        self.assertTrue(any("RF-99" in e for e in errors))

    def test_checked_task_requires_evidence(self):
        folder = self.feature()
        task = folder / "tasks.md"
        task.write_text(task.read_text().replace("[ ]", "[x]"))
        self.assertTrue(any("sin evidencia" in e for e in audit(self.root, True)["errors"]))

    def test_partial_draft_is_not_ready(self):
        folder = self.feature()
        (folder / "plan.md").unlink()
        self.assertEqual(audit(self.root)["errors"], [])
        self.assertTrue(audit(self.root)["warnings"])
        self.assertTrue(audit(self.root, True)["errors"])

    def test_number_collision(self):
        self.feature()
        self.feature("001-otra")
        self.assertTrue(any("Número de spec duplicado" in e for e in audit(self.root, True)["errors"]))

    def test_marker_and_missing_dependency(self):
        folder = self.feature(dependency="T8")
        (folder / "plan.md").write_text("RF-1 {{DECISION}}\n")
        errors = audit(self.root, True)["errors"]
        self.assertTrue(any("Marcador" in e for e in errors))
        self.assertTrue(any("T8" in e for e in errors))


    def test_claude_only(self):
        self.feature()
        (self.root / "AGENTS.md").rename(self.root / "CLAUDE.md")
        self.assertEqual(audit(self.root, True, "claude")["errors"], [])
        self.assertTrue(audit(self.root, True, "codex")["errors"])

    def test_claude_import_requires_agents(self):
        self.feature()
        (self.root / "AGENTS.md").unlink()
        (self.root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
        self.assertTrue(any("AGENTS.md" in e for e in audit(self.root, True, "claude")["errors"]))

    def test_both_agents(self):
        self.feature()
        self.assertTrue(audit(self.root, True, "both")["errors"])
        (self.root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
        self.assertEqual(audit(self.root, True, "both")["errors"], [])


if __name__ == "__main__":
    unittest.main()
