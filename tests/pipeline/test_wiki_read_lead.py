from __future__ import annotations

import unittest

from pipeline.wiki_read_lead import (
    allowed_names_from_lead,
    extract_lead,
    pick_lead_target,
)


class WikiReadLeadTests(unittest.TestCase):
    def test_extract_lead_skips_infobox_table(self) -> None:
        body = (
            "---\ntitle: Running Up That Hill\n---\n"
            "# Running Up That Hill | length = | label = EMI\n"
            "| A-side | Running Up That Hill |\n"
            "A synth-pop song by Kate Bush from 1985.\n\n"
            "## Background\n"
            "Later section."
        )
        lead = extract_lead(body, max_chars=500)
        self.assertIn("synth-pop song", lead)
        self.assertNotIn("length =", lead)
        self.assertNotIn("A-side", lead)

    def test_extract_lead_stops_at_h2(self) -> None:
        body = (
            "---\ntitle: Example\n---\n"
            "Lead paragraph one.\n\n"
            "Lead paragraph two.\n\n"
            "## History\n"
            "Later section."
        )
        lead = extract_lead(body, max_chars=500)
        self.assertIn("Lead paragraph one", lead)
        self.assertNotIn("Later section", lead)

    def test_allowed_names_from_quoted_titles(self) -> None:
        lead = 'Kate Bush\'s "Running Up That Hill" featured in Stranger Things.'
        names = allowed_names_from_lead(lead, title="Running Up That Hill")
        joined = " | ".join(names).casefold()
        self.assertIn("running up that hill", joined)
        self.assertIn("kate bush", joined)

    def test_pick_lead_target_prefers_running_up_that_hill(self) -> None:
        hit_meta = [
            {"title": "Kate Bush discography", "corpus_rel_path": "batch/x.md"},
            {"title": "Running Up That Hill", "corpus_rel_path": "batch/y.md"},
        ]
        title, path = pick_lead_target(
            "what song from Kate Bush reinvigorated her career in 2025-2026?",
            hit_meta,
        )
        self.assertEqual(title, "Running Up That Hill")
        self.assertEqual(path, "batch/y.md")


if __name__ == "__main__":
    unittest.main()
