from __future__ import annotations

import json
import unittest
from unittest.mock import MagicMock, patch

from pipeline import heptabase_cli


class HeptabaseCliTests(unittest.TestCase):
    def test_health_parses_version(self) -> None:
        fake_proc = MagicMock()
        fake_proc.returncode = 0
        fake_proc.stdout = "0.6.0"
        fake_proc.stderr = ""
        with patch.object(heptabase_cli.subprocess, "run", return_value=fake_proc):
            with patch.object(
                heptabase_cli,
                "run_cli",
                return_value={"ok": True, "cards": []},
            ):
                out = heptabase_cli.health_check()
        self.assertTrue(out.get("compatible_0_6_x"))

    def test_run_cli_parses_json(self) -> None:
        fake_proc = MagicMock()
        fake_proc.returncode = 0
        fake_proc.stdout = json.dumps({"cards": [{"id": "abc"}]})
        fake_proc.stderr = ""
        with patch.object(heptabase_cli.subprocess, "run", return_value=fake_proc):
            out = heptabase_cli.run_cli(["card", "list", "--limit", "1"])
        self.assertTrue(out.get("ok"))


if __name__ == "__main__":
    unittest.main()
