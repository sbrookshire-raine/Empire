"""Unit tests for resource pulse chat injection."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from frontend import resource_pulse_api


class ResourcePulseApiTests(unittest.TestCase):
    def test_capability_question_gets_pulse_marker(self) -> None:
        with patch(
            "pipeline.resource_pulse.pulse",
            return_value={
                "ok": True,
                "summary": "Headroom OK. GPU lease: idle.",
                "headroom_ok": True,
                "can_admit_now": ["github_scout"],
                "inventory": {"effective_tools": ["voice_presence", "wiki_local"]},
                "gpu_lease": {"tenant": "idle"},
            },
        ):
            out = resource_pulse_api.enrich_eve_message_payload(
                {
                    "message": (
                        "What capabilities do you have right now, and what's free "
                        "on the machine?"
                    )
                }
            )
        msg = str(out.get("message") or "")
        self.assertIn(resource_pulse_api.RESOURCE_PULSE_MARKER, msg)
        self.assertIn("github_scout", msg)
        self.assertIn("idle", msg)

    def test_plain_chat_untouched(self) -> None:
        payload = {"message": "hows it going?"}
        out = resource_pulse_api.enrich_eve_message_payload(payload)
        self.assertEqual(out.get("message"), "hows it going?")


if __name__ == "__main__":
    unittest.main()
