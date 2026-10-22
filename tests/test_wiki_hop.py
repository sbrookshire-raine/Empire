"""The hop affordance: how Eve reaches the page that holds the asked-for fact.

The landing page is often not the page that holds the answer. "What 80s song
became a hit again in the series Stranger Things?" lands on the series page,
which does not name the song; the "Music of Stranger Things" page does.

Three pieces make the hop work:

- `wiki_title_dns.related_titles` - the lexical hop: titles in the index
  that CONTAIN the subject (the link web is one-directional).
- `wiki_title_dns.ensure_links` - the semantic hop: the page's own outgoing
  links, scanned on demand, because the bulk link web is a 14.5-hour build.
- `wiki_read_lead.pick_section_for_question` / `page_outline` - which section
  of the hop page holds the fact, and what each section says.
"""

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]

PAGE = """---
title: "Music of Stranger Things"
page_id: "55632157"
outgoing_links:
  - "Stranger Things"
  - "Kate Bush"
section_headings:
  - "Original music score production"
  - "Period music"
  - "\\"Running Up That Hill\\""
---
# Music of Stranger Things

The *Stranger Things* original music score soundtracks are composed by Kyle Dixon.

## Period music

In addition to original music, *Stranger Things* features period music from
artists including The Clash and Kate Bush.

### "Running Up That Hill"

"Running Up That Hill" by English musician Kate Bush features prominently in
the fourth episode of the fourth season, and is re-used in subsequent episodes.
"""


def _write_corpus(root: Path) -> Path:
    """Write the corpus under `root` and return the ROOT (wiki_md_root is a root)."""

    year = root / "2026"
    batch = year / "batch_00000"
    batch.mkdir(parents=True, exist_ok=True)
    (batch / "wiki_1.md").write_text(PAGE, encoding="utf-8")
    return root


def _write_index(root: Path, titles: list[tuple[str, str]]) -> Path:
    index = root / "title-index.sqlite"
    conn = sqlite3.connect(index)
    try:
        conn.execute(
            "CREATE TABLE pages (title_norm TEXT PRIMARY KEY, title TEXT NOT NULL, "
            "path TEXT NOT NULL, rel_path TEXT NOT NULL, page_id TEXT, year TEXT NOT NULL)"
        )
        for title, rel_path in titles:
            conn.execute(
                "INSERT INTO pages(title_norm, title, path, rel_path, page_id, year) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (title.casefold(), title, str(rel_path), rel_path, "1", "2026"),
            )
        conn.commit()
    finally:
        conn.close()
    return index


class RelatedTitlesTests(unittest.TestCase):
    """The lexical hop: a title that CONTAINS the subject is a page about it."""

    def test_finds_titles_that_contain_the_subject(self) -> None:
        from pipeline import wiki_title_dns as dns

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            index = _write_index(
                root,
                [
                    ("Stranger Things", "batch_00000/wiki_1.md"),
                    ("Music of Stranger Things", "batch_00000/wiki_2.md"),
                    ("Stranger Things (soundtrack)", "batch_00000/wiki_3.md"),
                    ("The White Stripes", "batch_00000/wiki_4.md"),
                ],
            )
            found = dns.related_titles("Stranger Things", "2026", index_path=index)
        self.assertIn("Music of Stranger Things", found)
        self.assertIn("Stranger Things (soundtrack)", found)
        self.assertNotIn("The White Stripes", found)

    def test_the_subject_itself_is_not_a_hop(self) -> None:
        from pipeline import wiki_title_dns as dns

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            index = _write_index(root, [("Stranger Things", "batch_00000/wiki_1.md")])
            found = dns.related_titles("Stranger Things", "2026", index_path=index)
        self.assertNotIn("Stranger Things", found)

    def test_wildcards_in_the_subject_are_escaped(self) -> None:
        from pipeline import wiki_title_dns as dns

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            index = _write_index(
                root,
                [
                    ("AC/DC", "batch_00000/wiki_1.md"),
                    ("AC/DC Live", "batch_00000/wiki_2.md"),
                    ("Advanced", "batch_00000/wiki_3.md"),
                ],
            )
            found = dns.related_titles("AC/DC", "2026", index_path=index)
        # An unescaped "%" or "_" would match half the corpus.
        self.assertIn("AC/DC Live", found)
        self.assertNotIn("Advanced", found)


class EnsureLinksTests(unittest.TestCase):
    """The semantic hop: one file read per page, then cached."""

    def _corpus(self, root: Path):
        year = _write_corpus(root)
        index = _write_index(
            root,
            [
                ("Music of Stranger Things", "batch_00000/wiki_1.md"),
            ],
        )
        return index, year

    def test_scans_the_page_once_and_caches_the_edges(self) -> None:
        from pipeline import wiki_title_dns as dns

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            index, year = self._corpus(root)
            with patch.object(dns, "default_index_path", return_value=index), patch.object(
                dns, "wiki_md_root", return_value=year
            ):
                first = dns.ensure_links("Music of Stranger Things", "2026")
                second = dns.ensure_links("Music of Stranger Things", "2026")
            conn = sqlite3.connect(index)
            try:
                edges = conn.execute("SELECT COUNT(*) FROM links").fetchone()[0]
            finally:
                conn.close()
        self.assertTrue(first["scanned"])
        self.assertGreaterEqual(first["edges"], 1)
        self.assertFalse(second["scanned"])
        self.assertGreaterEqual(edges, 1)

    def test_a_missing_page_is_not_scanned(self) -> None:
        from pipeline import wiki_title_dns as dns

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            index, year = self._corpus(root)
            with patch.object(dns, "default_index_path", return_value=index), patch.object(
                dns, "wiki_md_root", return_value=year
            ):
                result = dns.ensure_links("No Such Page At All", "2026")
        self.assertFalse(result["scanned"])
        self.assertEqual(result["edges"], 0)


class SectionChoiceTests(unittest.TestCase):
    def test_a_song_question_wants_the_music_section(self) -> None:
        from pipeline.wiki_read_lead import pick_section_for_question

        titles = [
            "Original music score production",
            "Period music",
            '"Running Up That Hill"',
        ]
        self.assertEqual(
            pick_section_for_question(titles, "what 80s song became a hit again?"),
            "Period music",
        )

    def test_a_cast_question_wants_the_cast_section(self) -> None:
        from pipeline.wiki_read_lead import pick_section_for_question

        titles = ["Plot", "Cast and characters", "Production"]
        self.assertEqual(
            pick_section_for_question(titles, "who played the mother?"),
            "Cast and characters",
        )

    def test_an_unrelated_question_picks_no_section(self) -> None:
        from pipeline.wiki_read_lead import pick_section_for_question

        titles = ["Plot", "Cast and characters", "Production"]
        self.assertEqual(pick_section_for_question(titles, "when was it filmed?"), "")


class PageOutlineTests(unittest.TestCase):
    def test_outline_pairs_each_heading_with_its_opening_words(self) -> None:
        from pipeline.wiki_read_lead import page_outline

        outline = page_outline(PAGE, limit=10)
        joined = " | ".join(outline)
        self.assertIn("Period music", joined)
        self.assertIn("Running Up That Hill", joined)
        self.assertIn("Kate Bush", joined)

    def test_raw_wikitable_markup_is_left_out(self) -> None:
        from pipeline.wiki_read_lead import page_outline

        body = "## Releases\n\n{| class=\"wikitable\"\n|-\n| a | b\n|}"
        outline = page_outline(body, limit=10)
        self.assertFalse(any("{|" in line for line in outline))


class EvidenceBlockTests(unittest.TestCase):
    def test_an_oversized_block_is_trimmed_instead_of_recursing(self) -> None:
        """A big hop used to recurse forever instead of being trimmed.

        The retry trimmed the landing lead but not the hop leads, so it
        produced the same oversized block and called itself again.
        """

        from frontend import wiki_drift_api as api

        evidence = {
            "ok": True,
            "title": "Stranger Things",
            "lead": "x" * 5000,
            "hop_leads": [
                {
                    "ok": True,
                    "title": "Music of Stranger Things",
                    "lead": "y" * 5000,
                    "section": "z" * 5000,
                }
            ],
        }
        block = api._format_evidence_block(evidence, user_question="a question")
        self.assertTrue(block)
        self.assertLess(len(block), 12_000)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

