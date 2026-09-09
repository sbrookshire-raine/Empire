"""Tests for Loom intake wrapper."""

from __future__ import annotations

import os
import unittest
from pathlib import Path

from pipeline import loom_intake

LOOM_ROOT = Path(
    os.environ.get(
        "EMPIRE_LOOM_ROOT",
        r"C:\Empire_Workbench\04_Thought_Experiments\loom",
    )
)


@unittest.skipUnless(LOOM_ROOT.is_dir(), "loom tree not copied to workbench")
class LoomIntakeTests(unittest.TestCase):
    def test_status_reports_ledger(self) -> None:
        status = loom_intake.loom_status()
        self.assertTrue(status["ok"])
        self.assertGreater(status["ledger_rows"], 0)
        self.assertTrue(Path(status["ledger_path"]).is_file())

    def test_process_sample_csv(self) -> None:
        sample = LOOM_ROOT / "intake" / "sample_shell_packets.csv"
        if not sample.is_file():
            self.skipTest("sample_shell_packets.csv missing")
        result = loom_intake.process_shell_csv(
            str(sample),
            domain_bucket="education",
            max_per_cycle=7,
        )
        self.assertTrue(result["ok"], result.get("error"))
        report = result.get("report") or {}
        self.assertIsNone(report.get("fatal_error"))


if __name__ == "__main__":
    unittest.main()
