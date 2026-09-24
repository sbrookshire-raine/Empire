"""Idea store hygiene: an idea cannot silently rot.

Guarantees the thing the Architect asked for — "the information is not lost":

- every idea doc has valid front matter (id, slug, title, status, area, priority, created, source);
- `slug` matches the filename and `status` is in the queue's legend;
- the template's required sections are present (Intent, Why it matters, acceptance, Stack plan,
  Constraints, Open questions);
- every idea doc has a row in the queue ledger pointing at it.

Run `scripts/list-ideas.py` to see the index; see docs/ideas/README.md for the convention.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from pipeline.idea_store import (
    IDEAS_DIR,
    QUEUE_PATH,
    REQUIRED_FIELDS,
    REQUIRED_SECTIONS,
    STATUSES,
    idea_files,
    load_ideas,
    parse_front_matter,
)


class IdeaStoreTests(unittest.TestCase):
    def test_template_exists_with_required_sections(self) -> None:
        template = IDEAS_DIR / "_TEMPLATE.md"
        self.assertTrue(template.is_file(), "docs/ideas/_TEMPLATE.md is the contract")
        text = template.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            self.assertIn(section, text, f"template is missing {section!r}")

    def test_every_idea_has_valid_front_matter(self) -> None:
        self.assertTrue(idea_files(), "expected at least one idea doc")
        for path in idea_files():
            fields = parse_front_matter(path.read_text(encoding="utf-8"))
            for field in REQUIRED_FIELDS:
                self.assertIn(field, fields, f"{path.name}: missing {field!r} in front matter")
            self.assertIn(
                fields["status"],
                STATUSES,
                f"{path.name}: status {fields['status']!r} not in the queue legend",
            )
            self.assertEqual(
                fields["slug"],
                path.stem,
                f"{path.name}: slug {fields['slug']!r} must match the filename",
            )

    def test_every_idea_has_the_required_sections(self) -> None:
        for path in idea_files():
            text = path.read_text(encoding="utf-8")
            for section in REQUIRED_SECTIONS:
                self.assertIn(section, text, f"{path.name}: missing section {section!r}")

    def test_every_idea_has_a_queue_row(self) -> None:
        queue = QUEUE_PATH.read_text(encoding="utf-8")
        for path in idea_files():
            fields = parse_front_matter(path.read_text(encoding="utf-8"))
            self.assertIn(
                f"| {fields['id']} |",
                queue,
                f"{path.name}: no queue row for {fields['id']} — the ledger is the front door",
            )
            self.assertIn(
                path.name,
                queue,
                f"{path.name}: the queue row should link to this file",
            )

    def test_index_reads_the_files(self) -> None:
        ideas = load_ideas()
        self.assertEqual(len(ideas), len(idea_files()))
        for idea in ideas:
            self.assertTrue(idea["id"], idea)
            self.assertTrue(idea["title"], idea)


if __name__ == "__main__":
    unittest.main()