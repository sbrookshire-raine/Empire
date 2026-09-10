from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline.wiki_kiwix_ladder import (
    get_content_summary,
    search_with_snippets,
)


class WikiKiwixLadderTests(unittest.TestCase):
    @patch("pipeline.wiki_kiwix_ladder.search")
    def test_search_with_snippets_truncates(self, mock_search) -> None:
        mock_search.return_value = {
            "ok": True,
            "snapshot_year": "2026",
            "cards": [
                {
                    "title": "Running Up That Hill",
                    "snippet": "x" * 400,
                    "corpus_rel_path": "batch/a.md",
                    "snapshot_year": "2026",
                }
            ],
            "hit_meta": [{"title": "Running Up That Hill", "corpus_rel_path": "batch/a.md"}],
            "titles": ["Running Up That Hill"],
        }
        result = search_with_snippets("stranger things song", year="2026")
        self.assertTrue(result.get("ok"))
        self.assertEqual(result.get("ladder_rung"), "search_with_snippets")
        snippet = result["snippets"][0]["snippet"]
        self.assertLessEqual(len(snippet), 201)

    @patch("pipeline.wiki_kiwix_ladder.wiki_read_lead")
    def test_get_content_summary_tags_rung(self, mock_lead) -> None:
        mock_lead.return_value = {"ok": True, "title": "Kate Bush", "lead": "Bio text."}
        result = get_content_summary("Kate Bush", "2026")
        self.assertTrue(result.get("ok"))
        self.assertEqual(result.get("ladder_rung"), "get_content_summary")


if __name__ == "__main__":
    unittest.main()
