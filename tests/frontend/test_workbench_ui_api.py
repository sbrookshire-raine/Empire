"""Workbench UI context enrichment for Eve chat."""

from __future__ import annotations

import unittest

from frontend import workbench_ui_api


class WorkbenchUiApiTests(unittest.TestCase):
    def test_injects_daze_panel_context(self) -> None:
        payload = {
            "message": "What's free today?",
            "workbench_ui": {
                "tab": "chat",
                "panels": {
                    "daze_dial": True,
                    "daze_screen": "Schedule",
                    "tools_dock": False,
                    "history": False,
                },
                "active_tools": ["time_reclaim"],
            },
        }
        out = workbench_ui_api.enrich_eve_message_payload(payload)
        self.assertIn(workbench_ui_api.WORKBENCH_UI_MARKER, out["message"])
        self.assertIn("Schedule", out["message"])
        self.assertIn("What's free today?", out["message"])
        self.assertNotIn("workbench_ui", out)

    def test_skips_when_no_panels_open(self) -> None:
        payload = {
            "message": "Hello",
            "workbench_ui": {"tab": "chat", "panels": {}, "active_tools": []},
        }
        out = workbench_ui_api.enrich_eve_message_payload(payload)
        self.assertEqual(out["message"], "Hello")


if __name__ == "__main__":
    unittest.main()
