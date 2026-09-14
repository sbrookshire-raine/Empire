from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from unittest.mock import patch

from pipeline.wiki_title_dns import (
    build_links,
    import_redirects,
    neighbors,
    remember_wiki_lead,
    resolve,
    seed_parenthetical_aliases,
    upsert_pages,
    _connect,
)


def _seed(index: Path) -> None:
    conn = _connect(index)
    upsert_pages(
        conn,
        [
            (
                "Stranger Things",
                r"D:\wiki_md\2026\batch_00001\st.md",
                "batch_00001/st.md",
                "st",
                "2026",
            ),
            (
                "Kate Bush",
                r"D:\wiki_md\2026\batch_00002\kb.md",
                "batch_00002/kb.md",
                "kb",
                "2026",
            ),
            (
                "Cult following",
                r"D:\wiki_md\2026\batch_00003\cf.md",
                "batch_00003/cf.md",
                "cf",
                "2026",
            ),
            (
                "Following",
                r"D:\wiki_md\2026\batch_00003\f.md",
                "batch_00003/f.md",
                "f",
                "2026",
            ),
            (
                "Mercury (planet)",
                r"D:\wiki_md\2026\batch_00004\mp.md",
                "batch_00004/mp.md",
                "mp",
                "2026",
            ),
            (
                "Mercury (element)",
                r"D:\wiki_md\2026\batch_00004\me.md",
                "batch_00004/me.md",
                "me",
                "2026",
            ),
            (
                "V",
                r"D:\wiki_md\2026\batch_00005\v.md",
                "batch_00005/v.md",
                "v",
                "2026",
            ),
            (
                "V (1983 miniseries)",
                r"D:\wiki_md\2026\batch_00005\v1983.md",
                "batch_00005/v1983.md",
                "v1983",
                "2026",
            ),
            (
                "V (1984 TV series)",
                r"D:\wiki_md\2026\batch_00005\v1984.md",
                "batch_00005/v1984.md",
                "v1984",
                "2026",
            ),
            (
                "V (2009 TV series)",
                r"D:\wiki_md\2026\batch_00005\v2009.md",
                "batch_00005/v2009.md",
                "v2009",
                "2026",
            ),
            (
                "V (TV series)",
                r"D:\wiki_md\2026\batch_00005\vtv.md",
                "batch_00005/vtv.md",
                "vtv",
                "2026",
            ),
        ],
    )
    seed_parenthetical_aliases(conn)
    conn.commit()
    conn.close()


class WikiTitleDnsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.index = Path(self.tmp.name) / "title-index.sqlite"
        _seed(self.index)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_stranger_things_hit(self) -> None:
        result = resolve("Stranger Things", "2026", index_path=self.index)
        self.assertEqual(result.status, "hit")
        assert result.hit is not None
        self.assertEqual(result.hit.title, "Stranger Things")
        self.assertEqual(result.hit.rel_path, "batch_00001/st.md")

    def test_following_tv_is_miss(self) -> None:
        result = resolve(
            "The Following",
            "2026",
            user_question="What actors played in the TV show 'The Following'?",
            index_path=self.index,
        )
        self.assertEqual(result.status, "miss")
        self.assertIsNone(result.hit)

    def test_cult_following_not_used_for_tv(self) -> None:
        result = resolve(
            "Following",
            "2026",
            user_question="cast of the TV series Following",
            index_path=self.index,
        )
        self.assertEqual(result.status, "miss")

    def test_mercury_ambiguous(self) -> None:
        result = resolve("Mercury", "2026", index_path=self.index)
        self.assertEqual(result.status, "ambiguous")
        titles = {c.title for c in result.candidates}
        self.assertIn("Mercury (planet)", titles)
        self.assertIn("Mercury (element)", titles)

    def test_v_1983_tv_hits_miniseries(self) -> None:
        result = resolve(
            "V",
            "2026",
            user_question="what actors played in the original 1983/1984 series called 'V'?",
            index_path=self.index,
        )
        self.assertEqual(result.status, "hit")
        assert result.hit is not None
        self.assertEqual(result.hit.title, "V (1983 miniseries)")

    def test_v_80s_miniseries_word_picks_1983(self) -> None:
        result = resolve(
            "V",
            "2026",
            user_question='what actors were in the 80s miniseries called "V"',
            index_path=self.index,
        )
        self.assertEqual(result.status, "hit")
        assert result.hit is not None
        self.assertEqual(result.hit.title, "V (1983 miniseries)")

    def test_1980s_does_not_mean_year_1980(self) -> None:
        from pipeline.wiki_title_dns import _years_from_question

        self.assertEqual(
            _years_from_question("what actors played in the 1980s miniseries called 'V'"),
            (),
        )
        self.assertEqual(
            _years_from_question("actors in the 1983 miniseries V"),
            ("1983",),
        )

    def test_v_1984_tv_series_word_picks_weekly(self) -> None:
        result = resolve(
            "V",
            "2026",
            user_question="I'm interested in the 1984 TV series 'V'.",
            index_path=self.index,
        )
        self.assertEqual(result.status, "hit")
        assert result.hit is not None
        self.assertEqual(result.hit.title, "V (1984 TV series)")

    def test_v_80s_does_not_pick_2009_reboot(self) -> None:
        result = resolve(
            "V",
            "2026",
            user_question="tell me about a sci-fi series in the 80s called 'V'",
            index_path=self.index,
        )
        titles = {c.title for c in result.candidates}
        if result.status == "hit":
            assert result.hit is not None
            titles.add(result.hit.title)
        self.assertTrue(titles & {"V (1983 miniseries)", "V (1984 TV series)"})
        self.assertNotIn("V (2009 TV series)", titles)
        self.assertNotEqual(getattr(result.hit, "title", None), "V")

    def test_import_redirects(self) -> None:
        tsv = Path(self.tmp.name) / "redirects.tsv"
        tsv.write_text("RUTH\tKate Bush\n", encoding="utf-8")
        n = import_redirects(self.index, tsv)
        self.assertGreaterEqual(n, 1)
        result = resolve("RUTH", "2026", index_path=self.index)
        self.assertEqual(result.status, "hit")
        assert result.hit is not None
        self.assertEqual(result.hit.title, "Kate Bush")

    def test_missing_index_is_miss(self) -> None:
        missing = Path(self.tmp.name) / "nope.sqlite"
        result = resolve("Stranger Things", "2026", index_path=missing)
        self.assertEqual(result.status, "miss")
        self.assertIn("missing", result.reason)

    def test_remember_lead_writes_cache_and_dedupes(self) -> None:
        cache = Path(self.tmp.name) / "wiki_cache"
        reports = Path(self.tmp.name) / "reports"
        lead = {
            "ok": True,
            "title": "Stranger Things",
            "lead": "An American science fiction series.",
        }
        with patch.dict(
            "os.environ",
            {
                "EMPIRE_WIKI_REPORTS_ROOT": str(reports),
                "EMPIRE_WIKI_CACHE_DIR": str(cache),
            },
        ):
            with patch(
                "pipeline.wiki_read_lead.wiki_read_lead",
                return_value=lead,
            ):
                first = remember_wiki_lead(
                    "Stranger Things",
                    "2026",
                    index_path=self.index,
                    promote=False,
                )
                second = remember_wiki_lead(
                    "Stranger Things",
                    "2026",
                    index_path=self.index,
                    promote=False,
                )
        self.assertTrue(first.get("ok"))
        self.assertFalse(first.get("skipped"))
        self.assertTrue(Path(str(first.get("path"))).is_file())
        self.assertTrue(second.get("skipped"))
        body = Path(str(first.get("path"))).read_text(encoding="utf-8")
        self.assertIn("An American science fiction series", body)
        self.assertNotIn("full article", body.casefold())

    def test_build_links_and_neighbors(self) -> None:
        wiki = Path(self.tmp.name) / "wiki_md" / "2026"
        rel = "batch_00001/st.md"
        page = wiki / rel
        page.parent.mkdir(parents=True)
        page.write_text(
            "---\ntitle: Stranger Things\noutgoing_links:\n"
            "  - Kate Bush\n"
            "  - Running Up That Hill\n"
            "  - Wikipedia:Ignore\n"
            "---\n# Stranger Things\nA show.\n",
            encoding="utf-8",
        )
        conn = _connect(self.index)
        upsert_pages(
            conn,
            [
                (
                    "Stranger Things",
                    str(page),
                    rel.replace("\\", "/"),
                    "st",
                    "2026",
                )
            ],
        )
        conn.commit()
        conn.close()
        built = build_links(
            "2026",
            index_path=self.index,
            wiki_root=Path(self.tmp.name) / "wiki_md",
            resume=False,
        )
        self.assertTrue(built.get("ok"))
        self.assertGreaterEqual(int(built.get("edges") or 0), 2)
        web = neighbors("Stranger Things", "2026", index_path=self.index)
        self.assertTrue(web.get("ok"))
        outbound = [t.casefold() for t in web.get("outbound") or []]
        self.assertIn("kate bush", outbound)
        self.assertIn("running up that hill", outbound)
        self.assertNotIn("wikipedia:ignore", outbound)

    def test_neighbors_rank_inbound_song(self) -> None:
        from pipeline.wiki_title_matcher import normalize_text

        conn = _connect(self.index)
        upsert_pages(
            conn,
            [
                (
                    "Running Up That Hill",
                    r"D:\wiki_md\2026\batch_00009\ruth.md",
                    "batch_00009/ruth.md",
                    "ruth",
                    "2026",
                ),
                (
                    "Acid",
                    r"D:\wiki_md\2026\batch_00009\acid.md",
                    "batch_00009/acid.md",
                    "acid",
                    "2026",
                ),
                (
                    "Music of Stranger Things",
                    r"D:\wiki_md\2026\batch_00009\most.md",
                    "batch_00009/most.md",
                    "most",
                    "2026",
                ),
            ],
        )
        show = normalize_text("Stranger Things")
        conn.executemany(
            "INSERT OR IGNORE INTO links(from_norm, to_norm, to_title) VALUES (?, ?, ?)",
            [
                (normalize_text("Acid"), show, "Stranger Things"),
                (normalize_text("Running Up That Hill"), show, "Stranger Things"),
                (normalize_text("Music of Stranger Things"), show, "Stranger Things"),
            ],
        )
        conn.commit()
        conn.close()
        web = neighbors(
            "Stranger Things",
            "2026",
            index_path=self.index,
            user_question=(
                "what popular 80s song got re-popularized during stranger things?"
            ),
        )
        ranked = web.get("ranked") or []
        self.assertTrue(ranked)
        self.assertEqual(ranked[0], "Running Up That Hill")
        self.assertEqual(web.get("hops"), ["Running Up That Hill"])


if __name__ == "__main__":
    unittest.main()
