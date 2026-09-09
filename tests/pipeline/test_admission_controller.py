"""Tests for Research Autopilot admission controller."""

from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from pipeline import admission_controller


class AdmissionControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmpdir.cleanup)
        self.session_file = Path(self._tmpdir.name) / "eve-capability-session.json"
        self.manifest_file = Path(self._tmpdir.name) / "capability-manifest.json"
        manifest_src = Path(__file__).resolve().parents[2] / "config" / "capability-manifest.json"
        self.manifest_file.write_text(manifest_src.read_text(encoding="utf-8"), encoding="utf-8")
        admission_controller.DEFAULT_SESSION = self.session_file
        self._session_patch = mock.patch.object(
            admission_controller, "session_path", return_value=self.session_file
        )
        self._manifest_patch = mock.patch.object(
            admission_controller, "manifest_path", return_value=self.manifest_file
        )
        self._session_patch.start()
        self._manifest_patch.start()
        self.addCleanup(self._session_patch.stop)
        self.addCleanup(self._manifest_patch.stop)
        self.session_file.write_text(
            json.dumps(
                {
                    "research_partner_mode": False,
                    "session_capabilities": [],
                    "expires_at": "",
                    "started_at": "",
                    "last_reason": "",
                }
            ),
            encoding="utf-8",
        )

    def test_request_denied_when_partner_off(self) -> None:
        with mock.patch("frontend.eve_toolbelt.category_enabled", return_value=False):
            result = admission_controller.request_capability("web_scout", "test")
        self.assertFalse(result["ok"])
        self.assertIn("Research Partner", result.get("error", ""))

    def test_request_granted_when_partner_on(self) -> None:
        admission_controller.set_research_partner(True)
        with mock.patch("frontend.eve_toolbelt.category_enabled", return_value=False), mock.patch.object(
            admission_controller, "_preflight", return_value={"ok": True}
        ):
            result = admission_controller.request_capability("web_scout", "test")
        self.assertTrue(result["ok"])
        self.assertIn("web_scout", result.get("session_capabilities", []))

    def test_non_auto_category_denied(self) -> None:
        admission_controller.set_research_partner(True)
        result = admission_controller.request_capability("stem_factory", "test")
        self.assertFalse(result["ok"])

    def test_capability_active_manual_toolbelt(self) -> None:
        with mock.patch("frontend.eve_toolbelt.category_enabled", return_value=True):
            self.assertTrue(admission_controller.capability_active("wiki_local"))

    def test_release_clears_session(self) -> None:
        admission_controller.set_research_partner(True)
        with mock.patch.object(admission_controller, "_preflight", return_value={"ok": True}):
            admission_controller.request_capability("github_scout", "test")
        released = admission_controller.release_session("test")
        self.assertTrue(released["ok"])
        status = admission_controller.status()
        self.assertEqual(status.get("session_capabilities"), [])

    def test_expire_stale(self) -> None:
        past = (datetime.now(timezone.utc) - timedelta(minutes=5)).isoformat()
        self.session_file.write_text(
            json.dumps(
                {
                    "research_partner_mode": True,
                    "session_capabilities": ["web_scout"],
                    "expires_at": past,
                    "started_at": past,
                    "last_reason": "old",
                }
            ),
            encoding="utf-8",
        )
        admission_controller.expire_stale()
        status = admission_controller.status()
        self.assertEqual(status.get("session_capabilities"), [])


if __name__ == "__main__":
    unittest.main()
