"""Unit tests for deterministic wiki Evidence JSON extraction."""

from __future__ import annotations

import unittest

from pipeline.wiki_extract import (
    extract_from_markdown,
    format_extract_injection,
    format_extract_prose,
    is_extract_shaped_question,
)


SAMPLE = """---
title: Sample Page
---

# Sample Page

| length = 5:00
| label = EMI
| writer = Kate Bush
| paradigm = Multi-paradigm: object-oriented

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

## See also

- Related A
- Related B
"""

RATINGS = """---
title: The Following
---

# The Following

{| class="wikitable"
|+ U.S. television ratings for *The Following*
|-
! scope="col" rowspan="2"| Season
! scope="col" rowspan="2"| Timeslot (ET)
! scope="col" rowspan="2"| Number of episodes
! scope="col" colspan="2" | Premiere
! scope="col" colspan="2" | Finale
! scope="col" rowspan="2"| TV season
! scope="col" rowspan="2"| Overall rank
! scope="col" rowspan="2"| 18-49 rank
! scope="col" rowspan="2"| Overall viewership
|-
! scope="col" | Date
! scope="col" |
! scope="col" | Date
! scope="col" |
|-
! 1
| rowspan="3" style="text-align: center;" | Monday 9:00 pm
| 15
| style="text-align: center;"|
| 10.42
| style="text-align: center;"|
| 7.82
|
| style="background:#fc9;"| #22
| style="background:#fc9;"| #9
| style="background:#fc9;"| 11.87
|-
! 2
| 15
| style="text-align: center;"|
| 11.18
| style="text-align: center;"|
| 4.81
|
| style="background:#fc9;"| #45
| style="background:#fc9;"| #22
| style="background:#fc9;"| 8.21
|}
"""

TECH_KV = """---
title: Nintendo Switch
---

{| class="wikitable"
|+ Technical specifications of Nintendo Switch
! scope="rowgroup" rowspan="2" | System-on-chip
! scope="row" colspan="2" | Name
|
|-
! scope="row" colspan="2" | ISA
| ARMv8-A
|-
! scope="rowgroup" rowspan="2" | GPU
! scope="row" colspan="2" | Type
| Nvidia GM20B Maxwell-based
|}
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

    def test_field_only_need_drops_tables(self) -> None:
        result = extract_from_markdown(
            SAMPLE,
            title="Sample Page",
            year="2026",
            need_hint="What paradigm field is listed for the Sample Page?",
        )
        self.assertEqual(result["state"], "ok")
        self.assertTrue(result["fields"])
        self.assertEqual(result["tables"], [])
        self.assertEqual(result["lists"], [])
        keys = {f["key"].casefold() for f in result["fields"]}
        self.assertIn("paradigm", keys)
        prose = format_extract_prose(result)
        self.assertNotIn("Alpha", prose)

    def test_list_only_need_drops_tables(self) -> None:
        result = extract_from_markdown(
            SAMPLE,
            title="Sample Page",
            year="2026",
            need_hint="Extract the See also list from the Sample Page.",
        )
        self.assertEqual(result["state"], "ok")
        self.assertEqual(result["tables"], [])
        self.assertEqual(result["fields"], [])
        self.assertTrue(result["lists"])
        blob = " ".join(
            " ".join(lst.get("items") or []) for lst in result["lists"]
        ).casefold()
        self.assertIn("related a", blob)

    def test_multicolumn_ratings_keep_headers(self) -> None:
        result = extract_from_markdown(
            RATINGS,
            title="The Following",
            year="2026",
            need_hint="Pull the U.S. television ratings table rows from The Following page.",
        )
        self.assertEqual(result["state"], "ok")
        self.assertTrue(result["tables"])
        headers = result["tables"][0]["headers"]
        self.assertGreaterEqual(len(headers), 3)
        self.assertNotEqual(headers[:2], ["Property", "Value"])
        joined = " | ".join(headers).casefold()
        self.assertIn("season", joined)
        rows = result["tables"][0]["rows"]
        flat = " ".join(" ".join(r) for r in rows)
        self.assertIn("11.87", flat)

    def test_tech_kv_still_property_value(self) -> None:
        result = extract_from_markdown(
            TECH_KV,
            title="Nintendo Switch",
            year="2026",
            need_hint="Extract the technical specifications table from the Nintendo Switch page.",
        )
        self.assertEqual(result["state"], "ok")
        self.assertTrue(result["tables"])
        self.assertEqual(result["tables"][0]["headers"][:2], ["Property", "Value"])
        flat = " ".join(" ".join(r) for r in result["tables"][0]["rows"])
        self.assertIn("ARMv8-A", flat)
        self.assertIn("GM20B", flat)
        self.assertEqual(result["fields"], [])
        self.assertEqual(result["lists"], [])


if __name__ == "__main__":
    unittest.main()
