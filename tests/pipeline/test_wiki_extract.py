"""Unit tests for deterministic wiki Evidence JSON extraction."""

from __future__ import annotations

import unittest

from pipeline.wiki_extract import (
    extract_from_markdown,
    format_extract_injection,
    is_extract_shaped_question,
)


SAMPLE = """---
title: Sample Page
---

# Sample Page

| length = 5:00
| label = EMI
| writer = Kate Bush

{| class="wikitable"
|+ Demo table
|-
! Name !! Value
|-
| Alpha || 1
|-
| Beta || 2
|}

## History

- First item
- Second item
"""


class WikiExtractTests(unittest.TestCase):
    def test_extract_shaped_detector(self) -> None:
        self.assertTrue(is_extract_shaped_question("What is the population of Paris?"))
        self.assertTrue(is_extract_shaped_question("When was the PlayStation 2 released?"))
        self.assertFalse(is_extract_shaped_question("Tell me about cheese"))

    def test_fields_tables_lists(self) -> None:
        result = extract_from_markdown(SAMPLE, title="Sample Page", year="2026")
        self.assertEqual(result["state"], "ok")
        self.assertTrue(result["ok"])
        keys = {f["key"].casefold() for f in result["fields"]}
        self.assertIn("label", keys)
        self.assertIn("writer", keys)
        self.assertTrue(result["tables"])
        headers = [h.casefold() for h in result["tables"][0]["headers"]]
        self.assertTrue(any("name" in h for h in headers))
        rows = result["tables"][0]["rows"]
        self.assertTrue(any("Alpha" in row for row in rows))
        self.assertTrue(any(lst.get("section", "").casefold() == "history" for lst in result["lists"]))

    def test_no_raw_wikitable_in_injection(self) -> None:
        result = extract_from_markdown(SAMPLE, title="Sample Page", year="2026")
        block = format_extract_injection(result, user_question="table of values")
        self.assertIn("[[EMPIRE_WIKI_EXTRACT]]", block)
        self.assertNotIn("{|", block)
        self.assertIn("CONTRACT:", block)

    def test_empty_page_fail_closed(self) -> None:
        result = extract_from_markdown(
            "---\ntitle: Thin\n---\n\n# Thin\n\nOnly a sentence.\n",
            title="Thin",
            year="2026",
        )
        self.assertEqual(result["state"], "empty")
        self.assertFalse(result["ok"])
        block = format_extract_injection(result, user_question="population of Thin")
        self.assertIn("Refuse", block)


if __name__ == "__main__":
    unittest.main()
