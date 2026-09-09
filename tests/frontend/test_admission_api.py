"""Smoke tests for /api/admission handlers."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import admission_controller


class AdmissionApiLogicTests(unittest.TestCase):
    def test_handle_set_research_partner(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            session_file = Path(tmp) / "eve-capability-session.json"
            session_file.write_text(
                json.dumps({"research_partner_mode": False, "session_capabilities": []}),
                encoding="utf-8",
            )
            manifest = Path(__file__).resolve().parents[2] / "config" / "capability-manifest.json"
            with mock.patch.object(admission_controller, "session_path", return_value=session_file), mock.patch.object(
                admission_controller, "manifest_path", return_value=manifest
            ):
                result = admission_controller.handle_api_action(
                    {"action": "set_research_partner", "enabled": True}
                )
            self.assertTrue(result["ok"])
            self.assertTrue(result.get("research_partner_mode"))


if __name__ == "__main__":
    unittest.main()
