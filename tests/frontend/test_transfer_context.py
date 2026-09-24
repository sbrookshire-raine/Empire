"""Transfer-context injection: the Architect's ledger reaches the ask without a model choice.

Measured 2026-09-24: a cross-domain question ("can i learn to play the drums by using the rules of
juggling?") produced six phrase-shaped wiki searches and zero `primitive_lookup` calls, so a prompt
hint alone never fired the ledger route. The frontend now runs the lookup and attaches the decoded
mechanisms next to the ask, exactly like the catalog block.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import serve
from pipeline import primitive_lookup

LEDGER = """id,date,thing,domain,mechanism,primitives,sibling,decoded_by,track
253,2026-07-08T22:05:45-06:00,TokenBucket,mechanical,Modulate machine command throughput to match actuator timing constraints.,Timing & Sync,Like a conveyor belt speed limiter.,jurisdiction-router,corpus
300,2026-07-09T10:00:00+00:00,juggling cascade,general,A cyclic timing constraint keeps three objects airborne by shedding each one at a fixed duty cycle,Timing & Sync;Sensory Feedback,"a drummer's ostinato across four limbs",Keeper,corpus
1,2026-07-07T14:37:09+00:00,pencil (writing end),mechanical,"Forward progress happens only by shedding graphite",Sacrificial Attrition;Granular Deposition,"a birthday candle burning down",Keeper,corpus
"""


class TransferContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.ledger = Path(self._tmp.name) / "ledger.csv"
        self.ledger.write_text(LEDGER, encoding="utf-8")
        patcher = patch.object(primitive_lookup, "DEFAULT_LEDGER", self.ledger)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_question_phrasing_variants_are_recognised(self) -> None:
        """Measured 2026-09-24: "which primitives does juggling share with drumming" was NOT matched
        by the first pattern set, so no ledger block reached the prompt and she echoed the card."""

        for message in (
            "which primitives does juggling share with drumming, and what would falsify the analogy?",
            "Use my primitive ledger: what overlaps with drumming?",
            "are there parallels between juggling and drumming?",
        ):
            with self.subTest(message=message):
                self.assertNotEqual(serve._transfer_context(message), "")

    def test_plain_question_gets_no_block(self) -> None:
        self.assertEqual(serve._transfer_context("what is the capital of peru?"), "")

    def test_transfer_question_gets_the_decoded_mechanisms(self) -> None:
        block = serve._transfer_context("can i learn to play the drums by using the rules of juggling?")
        self.assertIn("AUTHORITATIVE PRIMITIVE LEDGER CONTEXT", block)
        self.assertIn("Timing & Sync", block)
        self.assertIn("sibling", block)
        self.assertIn("Do not answer this from general knowledge alone", block)

    def test_no_match_returns_the_vocabulary_instead(self) -> None:
        block = serve._transfer_context("can i apply the rules of quantum chromodynamics to my taxes?")
        self.assertIn("AUTHORITATIVE PRIMITIVE LEDGER", block)
        self.assertIn("no decoded row matches this ask", block)
        self.assertIn("never invent a mechanism", block)

    def test_an_unreadable_ledger_never_breaks_the_turn(self) -> None:
        with patch.object(primitive_lookup, "DEFAULT_LEDGER", Path(self._tmp.name) / "missing.csv"):
            block = serve._transfer_context("can i apply the rules of juggling to drumming?")
        self.assertIn("could not be read", block)
        self.assertIn("Do not answer this from general knowledge", block)


if __name__ == "__main__":
    unittest.main()
