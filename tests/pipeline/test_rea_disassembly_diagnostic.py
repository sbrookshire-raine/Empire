from __future__ import annotations

import json
import unittest
from pathlib import Path

from pipeline import rea_disassembly_diagnostic


class ReaDisassemblyDiagnosticTests(unittest.TestCase):
    def test_battery_file_is_valid(self) -> None:
        battery = rea_disassembly_diagnostic.load_battery()
        self.assertEqual(battery.get("version"), 1)
        checks = battery.get("checks")
        self.assertIsInstance(checks, list)
        self.assertGreaterEqual(len(checks), 8)
        ids = [c["id"] for c in checks if isinstance(c, dict)]
        self.assertEqual(len(ids), len(set(ids)))

    def test_fast_battery_required_passes_without_live_services(self) -> None:
        report = rea_disassembly_diagnostic.run_battery(
            include_optional=False,
            skip_tiers={"rea"},
        )
        self.assertTrue(report.get("ok"), report)
        summary = report.get("summary") or {}
        self.assertGreater(summary.get("required_pass", 0), 0)

    def test_battery_json_roundtrip(self) -> None:
        path = Path(__file__).resolve().parents[2] / "config" / "diagnostics" / "rea-disassembly-battery.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertIn("atomic_agent_repo", data.get("paths") or {})


if __name__ == "__main__":
    unittest.main()
