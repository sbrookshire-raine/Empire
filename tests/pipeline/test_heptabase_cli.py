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

    def test_create_note_uses_content_file(self) -> None:
        seen: dict[str, list[str]] = {}

        def fake_run(cmd: list[str], **kwargs: object) -> MagicMock:
            seen["cmd"] = cmd
            proc = MagicMock()
            proc.returncode = 0
            proc.stdout = json.dumps({"id": "n1", "title": "T"})
            proc.stderr = ""
            return proc

        with patch.object(heptabase_cli.subprocess, "run", side_effect=fake_run):
            out = heptabase_cli.create_note("# Title\n\nHello")
        self.assertTrue(out.get("ok"))
        cmd = seen["cmd"]
        self.assertIn("--content-file", cmd)
        self.assertNotIn("--content", cmd)


if __name__ == "__main__":
    unittest.main()
