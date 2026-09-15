"""Tests for MediaWiki meta import helpers."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline.wiki_mediawiki_meta import (
    import_disambiguation_tsv,
    mark_disambiguation_titles,
    seed_disambig_from_titles,
)
from pipeline.wiki_title_dns import upsert_pages, _connect


class WikiMediawikiMetaTests(unittest.TestCase):
    def test_seed_disambig_from_titles(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "idx.sqlite"
            conn = _connect(index)
            upsert_pages(
                conn,
                [
                    ("Mercury", str(Path(tmp) / "a.md"), "a.md", "1", "2026"),
                    (
                        "Mercury (disambiguation)",
                        str(Path(tmp) / "b.md"),
                        "b.md",
                        "2",
                        "2026",
                    ),
                ],
            )
            n = seed_disambig_from_titles(conn)
            conn.commit()
            row = conn.execute(
                "SELECT is_disambiguation FROM pages WHERE title_norm = ?",
                ("mercury (disambiguation)",),
            ).fetchone()
            conn.close()
            self.assertGreaterEqual(n, 1)
            self.assertEqual(int(row[0]), 1)

    def test_import_disambiguation_tsv(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "idx.sqlite"
            tsv = Path(tmp) / "disambig.tsv"
            tsv.write_text("Mercury\n# comment\n", encoding="utf-8")
            conn = _connect(index)
            upsert_pages(
                conn,
                [("Mercury", str(Path(tmp) / "a.md"), "a.md", "1", "2026")],
            )
            conn.commit()
            conn.close()
            n = import_disambiguation_tsv(index, tsv)
            self.assertGreaterEqual(n, 1)


if __name__ == "__main__":
    unittest.main()
