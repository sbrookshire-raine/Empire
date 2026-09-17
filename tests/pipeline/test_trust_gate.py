"""Unit tests for the prompt-injection trust gate."""

from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline import trust_gate


class TrustGateTests(unittest.TestCase):
    def tearDown(self) -> None:
        trust_gate.reset()

    def test_clean_turn_admits_dangerous(self) -> None:
        trust_gate.reset()
        self.assertTrue(trust_gate.can_admit_dangerous("author_code"))
        self.assertTrue(trust_gate.can_admit_dangerous("create_spreadsheet"))

    def test_untrusted_blocks_dangerous(self) -> None:
        with patch.object(trust_gate, "state_path", return_value=trust_gate.state_path()):
            trust_gate.mark_untrusted(domain="public_web")
            self.assertTrue(trust_gate.untrusted_active())
            self.assertFalse(trust_gate.can_admit_dangerous("author_code"))
            self.assertFalse(trust_gate.can_admit_dangerous("create_spreadsheet"))

    def test_memory_gate(self) -> None:
        trust_gate.mark_untrusted(domain="public_web")
        res = trust_gate.gate_memory_tool("cognee_remember")
        self.assertFalse(res["ok"])
        self.assertTrue(res["blocked"])

    def test_memory_gate_allows_when_clean(self) -> None:
        trust_gate.reset()
        res = trust_gate.gate_memory_tool("cognee_remember")
        self.assertTrue(res["ok"])
        self.assertFalse(res["blocked"])

    def test_non_memory_tool_not_gated(self) -> None:
        trust_gate.mark_untrusted(domain="public_web")
        res = trust_gate.gate_memory_tool("workspace_search")
        self.assertTrue(res["ok"])
        self.assertFalse(res["blocked"])


if __name__ == "__main__":
    unittest.main()
