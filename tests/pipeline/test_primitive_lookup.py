"""Primitive ledger lookup: ranking, dedupe, filters, and the vocabulary hand-back on a miss."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline import primitive_lookup

LEDGER = (
    "id,date,thing,domain,mechanism,primitives,sibling,decoded_by,track\n"
    '1,2026-07-07T14:37:09+00:00,pencil (writing end),mechanical,'
    '"Forward progress happens only by shedding tiny bits of graphite",'
    "Sacrificial Attrition;Granular Deposition,"
    '"a birthday candle burning down, or a 3D printer laying filament",Keeper,corpus\n'
    "38,2026-07-07T17:54:54+00:00,goflow (1mb-dev),software,"
    '"Token-bucket counters regulate how much work passes per second",'
    "Force-to-Output Modulation;Timing & Sync,"
    '"an IV drip regulator metering fluid at a fixed rate",Keeper,corpus\n'
    "38,2026-07-07T17:54:54+00:00,goflow (1mb-dev),software,"
    '"Token-bucket counters regulate how much work passes per second",'
    "Force-to-Output Modulation;Timing & Sync,"
    '"an IV drip regulator metering fluid at a fixed rate",Keeper,corpus\n'
    "44,2026-07-07T19:45:17+00:00,Libby apprenticeship coordination,workforce,"
    '"All cross-party coordination flows through exactly two people",'
    "The Keystone Pin,"
    '"a nonprofit where only one person knows how to renew the grant",Keeper,corpus\n'
)


class PrimitiveLookupTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.ledger = Path(self._tmp.name) / "primitive_ledger.csv"
        self.ledger.write_text(LEDGER, encoding="utf-8")

    def test_text_query_ranks_and_dedupes(self) -> None:
        result = primitive_lookup.lookup(text="timing throughput", ledger=self.ledger)
        self.assertTrue(result["ok"])
        self.assertEqual(result["rows_total"], 4)
        self.assertEqual(result["rows_distinct"], 3)
        things = [match["thing"] for match in result["matches"]]
        self.assertEqual(things[0], "goflow (1mb-dev)")
        self.assertEqual(things.count("goflow (1mb-dev)"), 1, "duplicate ledger rows collapse")

    def test_primitive_filter_requires_the_name(self) -> None:
        hit = primitive_lookup.lookup(primitive="Timing & Sync", ledger=self.ledger)
        self.assertEqual([match["thing"] for match in hit["matches"]], ["goflow (1mb-dev)"])
        miss = primitive_lookup.lookup(primitive="Not A Primitive", ledger=self.ledger)
        self.assertEqual(miss["matches"], [])
        self.assertIn("not in the ledger yet", miss["note"])

    def test_domain_filter_and_limit(self) -> None:
        result = primitive_lookup.lookup(domain="workforce", ledger=self.ledger)
        self.assertEqual([match["thing"] for match in result["matches"]], ["Libby apprenticeship coordination"])
        limited = primitive_lookup.lookup(text="counters coordination", ledger=self.ledger, limit=1)
        self.assertTrue(limited["ok"])
        self.assertEqual(len(limited["matches"]), 1)

    def test_miss_hands_back_the_ledger_vocabulary(self) -> None:
        result = primitive_lookup.lookup(text="zzzznothing", ledger=self.ledger)
        self.assertEqual(result["matches"], [])
        names = [entry["primitive"] for entry in result["vocabulary"]]
        self.assertIn("Timing & Sync", names)
        self.assertIn("The Keystone Pin", names)
        self.assertIn("retry with one of those", result["note"])

    def test_empty_query_is_refused_with_vocabulary(self) -> None:
        result = primitive_lookup.lookup(text="the and of", ledger=self.ledger)
        self.assertFalse(result["ok"])
        self.assertIn("vocabulary", result)

    def test_missing_ledger_reports_the_path(self) -> None:
        result = primitive_lookup.lookup(text="pencil", ledger=Path(self._tmp.name) / "nope.csv")
        self.assertFalse(result["ok"])
        self.assertIn("not readable", result["error"])

    def test_common_words_alone_do_not_produce_matches(self) -> None:
        """Measured 2026-09-24: "one" matched "one help button"/"one uniform protocol" and handed
        a juggling question three irrelevant mechanisms. Rarity filter, not just stopwords."""

        result = primitive_lookup.lookup(text="one two three", ledger=self.ledger)
        self.assertFalse(result["ok"])
        self.assertIn("vocabulary", result)

    def test_terms_drop_stopwords_and_short_words(self) -> None:
        self.assertEqual(
            primitive_lookup._terms("How can I learn to play the drums using the rules of juggling?"),
            ["play", "drums", "juggling"],
        )


if __name__ == "__main__":
    unittest.main()
