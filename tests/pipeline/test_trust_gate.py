"""Unit tests for the prompt-injection trust gate."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import trust_gate


class TrustGateTests(unittest.TestCase):
    def setUp(self) -> None:
        # The real state path is shared with the running stack
        # (%LOCALAPPDATA%\EMPIRE\untrusted-turn.json), so a test run racing the live agent — or a
        # second pytest process — made test_memory_gate flake ("True is not false"). Pin it to a
        # temp file so the gate is exercised on its own state.
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self._state = Path(tmp.name) / "untrusted-turn.json"
        patcher = patch.object(trust_gate, "state_path", lambda: self._state)
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self) -> None:
        trust_gate.reset()

    def test_clean_turn_admits_dangerous(self) -> None:
        trust_gate.reset()
        self.assertTrue(trust_gate.can_admit_dangerous("author_code"))
        self.assertTrue(trust_gate.can_admit_dangerous("create_spreadsheet"))

    def test_untrusted_blocks_dangerous(self) -> None:
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
