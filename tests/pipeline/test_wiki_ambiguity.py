"""Unit tests for R-02 ambiguity: same-noun-family candidates from Title DNS.

Hermetic — a temp SQLite index seeded like the real one (the live 31 GB index is 7.1M pages, so
the shape matters: the bare plural is absent, the singular stem and concept pages are present).

Measured on the real index 2026-09-24: `magnets` has no page, `magnet` and `magnetism` do,
`white stripe(s)` has none, and `batteries` resolves through the alias table to
`Batteries (journal)` while `battery` is its own page.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline.wiki_title_dns import (
    _connect,
    family_candidates,
    resolve,
    singular_stem,
    upsert_pages,
)

PAGES = [
    ("The Magnets", "m/st.md", "magnetic_entity"),
    ("Magnet", "m/magnet.md", "device"),
    ("Magnetism", "m/magnetism.md", "concept"),
    ("The White Stripes", "w/tws.md", "band"),
    ("Kate Bush", "k/kb.md", "person"),
    ("Series", "s/series.md", "generic"),
    ("News", "n/news.md", "generic"),
]
ALIASES = [("batteries", "the batteries"), ("the batteries", "the batteries")]


class AmbiguityTests(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.index = Path(tmp.name) / "title-index.sqlite"
        conn = _connect(self.index)
        upsert_pages(
            conn,
            [
                (
                    title,
                    rf"D:\wiki_md\2026\batch_00001\{slug}.md",
                    f"batch_00001/{slug}.md",
                    slug,
                    "2026",
                )
                for title, slug, _kind in PAGES
            ]
            + [
                ("The Batteries", r"D:\wiki_md\2026\batch_00002\tb.md", "batch_00002/tb.md", "tb", "2026"),
                ("Battery", r"D:\wiki_md\2026\batch_00002\bt.md", "batch_00002/bt.md", "bt", "2026"),
                ("Batteries (journal)", r"D:\wiki_md\2026\batch_00002/bj.md", "batch_00002/bj.md", "bj", "2026"),
            ],
        )
        conn.execute("INSERT OR REPLACE INTO aliases(alias_norm, title_norm) VALUES (?, ?)", ALIASES[0])
        conn.commit()
        conn.close()

    def family(self, subject: str) -> dict:
        return family_candidates(subject, "2026", index_path=self.index)

    def test_bare_plural_with_singular_family_is_ambiguous(self) -> None:
        """The live acceptance case: asked 'magnets', so 'The Magnets' must not be the only reading."""

        result = self.family("magnets")
        self.assertTrue(result["ambiguous"], result)
        titles = [c["title"] for c in result["candidates"]]
        self.assertIn("Magnet", titles)
        self.assertIn("Magnetism", titles)
        self.assertNotIn("The Magnets", titles)  # the matched entity comes from the hit, not here

    def test_concrete_page_of_its_own_is_not_ambiguous(self) -> None:
        for subject in ("magnet", "magnetism", "kate bush", "series", "news"):
            self.assertFalse(self.family(subject)["ambiguous"], subject)

    def test_band_subject_is_not_flagged(self) -> None:
        """'white stripes' has no stem page, so the band resolves cleanly (no false ambiguity)."""

        self.assertFalse(self.family("white stripes")["ambiguous"])
        self.assertFalse(self.family("the white stripes")["ambiguous"])

    def test_alias_redirection_is_flagged(self) -> None:
        """'batteries' redirects to 'The Batteries' while 'Battery' is its own page."""

        result = self.family("batteries")
        self.assertTrue(result["ambiguous"], result)
        self.assertIn("Battery", [c["title"] for c in result["candidates"]])

    def test_singular_stem_guards(self) -> None:
        self.assertEqual(singular_stem("magnets"), "magnet")
        self.assertEqual(singular_stem("batteries"), "battery")
        self.assertEqual(singular_stem("glasses"), "glass")
        for guarded in ("series", "physics", "news", "species", "class"):
            self.assertEqual(singular_stem(guarded), guarded)
        self.assertEqual(singular_stem("the white stripes"), "white stripe")

    def test_resolve_still_returns_the_hit(self) -> None:
        """Ambiguity is additive: the tool still has a page to read, so nothing regresses."""

        dns = resolve("magnets", "2026", index_path=self.index)
        self.assertEqual(dns.status, "hit")
        self.assertIsNotNone(dns.hit)
        self.assertEqual(dns.hit.title, "The Magnets")

    def test_missing_index_is_not_an_error(self) -> None:
        result = family_candidates("magnets", "2026", index_path=Path("does/not/exist.sqlite"))
        self.assertFalse(result["ambiguous"])
        self.assertEqual(result["candidates"], [])


if __name__ == "__main__":
    unittest.main()