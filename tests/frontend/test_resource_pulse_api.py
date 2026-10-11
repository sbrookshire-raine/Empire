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

    def test_plain_chat_still_gets_pulse(self) -> None:
        with patch(
            "pipeline.resource_pulse.pulse",
            return_value={
                "ok": True,
                "summary": "Headroom OK.",
                "headroom_ok": True,
                "can_admit_now": [],
                "inventory": {"effective_tools": ["wiki_local"]},
                "gpu_lease": {"tenant": "idle"},
            },
        ):
            out = resource_pulse_api.enrich_eve_message_payload({"message": "hows it going?"})
        msg = str(out.get("message") or "")
        self.assertIn(resource_pulse_api.RESOURCE_PULSE_MARKER, msg)
        self.assertIn("wiki_local", msg)

    def test_wiki_lookup_skips_pulse(self) -> None:
        out = resource_pulse_api.enrich_eve_message_payload(
            {
                "message": (
                    "Go to my local Wikipedia and find what are the albums "
                    "released by the Beach Boys."
                )
            }
        )
        self.assertNotIn(resource_pulse_api.RESOURCE_PULSE_MARKER, str(out.get("message") or ""))

    def test_pulse_stays_outside_user_message_anchor(self) -> None:
        with patch(
            "pipeline.resource_pulse.pulse",
            return_value={
                "ok": True,
                "summary": "Headroom OK.",
                "headroom_ok": True,
                "can_admit_now": [],
                "inventory": {"effective_tools": ["wiki_local"]},
                "gpu_lease": {"tenant": "idle"},
            },
        ):
            out = resource_pulse_api.enrich_eve_message_payload(
                {
                    "message": (
                        "[[EMPIRE_COMPANION]]\n\nROLE: partner.\n\n"
                        "User message:\nWhat did we decide about the kitchen remodel?"
                    )
                }
            )
        msg = str(out.get("message") or "")
        user_part = msg.rsplit("\n\nUser message:\n", 1)[-1].strip()
        self.assertEqual(user_part, "What did we decide about the kitchen remodel?")
        self.assertIn(resource_pulse_api.RESOURCE_PULSE_MARKER, msg.split("User message:")[0])


if __name__ == "__main__":
    unittest.main()
