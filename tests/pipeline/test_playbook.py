"""Playbook registry: every section must carry worked examples, and lookups stay bounded.

The Architect's requirement (2026-09-24): for **each** skill, 3–7 concrete examples of using it to build
or learn something, so pathways get reused instead of tools chosen at random. `thin_sections()` is the
mechanism that keeps that true as the playbook grows.
"""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import playbook

AREA = """---
area: example-area
one_line: One line about the area.
tools: alpha_tool, beta_tool
---

# Example area

## First capability
Use when: testing.

- **Ask:** "one?" -> **Do:** `alpha_tool()` -> **Get:** a thing.
- **Ask:** "two?" -> **Do:** `alpha_tool()` -> **Get:** another thing.
- **Ask:** "three?" -> **Do:** `beta_tool()` -> **Get:** a third thing.
"""

THIN = """---
area: thin-area
one_line: Only one example.
tools: alpha_tool
---

## Sparse capability
- **Ask:** "only one?" -> **Do:** `alpha_tool()` -> **Get:** a thing.
"""


class PlaybookRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = Path(self._tmp.name)
        (self.dir / "example-area.md").write_text(AREA, encoding="utf-8")
        patcher = patch.dict(os.environ, {"EMPIRE_PLAYBOOK": str(self.dir)})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_index_reports_areas_sections_and_example_counts(self) -> None:
        entries = playbook.index()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["area"], "example-area")
        self.assertEqual(entries[0]["sections"], ["First capability"])
        self.assertEqual(entries[0]["examples"], 3)

    def test_topic_by_area_id_and_by_tool_name(self) -> None:
        by_area = playbook.topic("example-area")
        self.assertTrue(by_area["ok"], by_area)
        self.assertIn("alpha_tool", by_area["playbook"])
        by_tool = playbook.topic("beta_tool")
        self.assertTrue(by_tool["ok"], by_tool)
        self.assertEqual(by_tool["matched"], "beta_tool")

    def test_lookup_is_bounded_and_paths_are_refused(self) -> None:
        bounded = playbook.topic("example-area", max_chars=40)
        self.assertTrue(bounded["truncated"])
        self.assertIn("[truncated", bounded["playbook"])
        for bad in ("../secrets", "a/b", "..", ""):
            with self.subTest(bad=bad):
                self.assertFalse(playbook.topic(bad)["ok"])

    def test_unknown_topic_lists_the_areas_instead(self) -> None:
        result = playbook.topic("nothing-like-this")
        self.assertFalse(result["ok"])
        self.assertIn("example-area", result["areas"])

    def test_thin_sections_flags_any_skill_under_three_examples(self) -> None:
        self.assertEqual(playbook.thin_sections(), [])
        (self.dir / "thin-area.md").write_text(THIN, encoding="utf-8")
        self.assertEqual(
            playbook.thin_sections(),
            [{"area": "thin-area", "section": "Sparse capability", "examples": 1}],
        )

    def test_the_shipped_playbook_has_no_thin_sections(self) -> None:
        """The Architect's rule, enforced against the real content (not the fixture)."""

        with patch.dict(os.environ, {"EMPIRE_PLAYBOOK": ""}):
            thin = playbook.thin_sections()
            areas = playbook.index()
        self.assertGreaterEqual(len(areas), 5, f"expected a real playbook, saw {len(areas)} areas")
        self.assertEqual(thin, [], f"sections below {playbook.MIN_EXAMPLES} examples: {thin}")


if __name__ == "__main__":
    unittest.main()
