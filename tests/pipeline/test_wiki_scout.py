"""Unit tests for pipeline.wiki_scout cache writers (no live Weaviate)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import wiki_scout
from pipeline.wiki_title_dns import DnsHit


class WikiScoutCacheTests(unittest.TestCase):
    def setUp(self) -> None:
        self._lock_tmp = tempfile.TemporaryDirectory()
        self._lock_path = Path(self._lock_tmp.name) / "lock.json"
        self._env = patch.dict(
            "os.environ",
            {"EMPIRE_WIKI_LOOKUP_LOCK": str(self._lock_path)},
            clear=False,
        )
        self._env.start()

    def tearDown(self) -> None:
        self._env.stop()
        self._lock_tmp.cleanup()

    def test_resolve_collection_years(self) -> None:
        self.assertEqual(wiki_scout.resolve_collection(year=2017), ("WikiChunk", "2017"))
        self.assertEqual(
            wiki_scout.resolve_collection(year="2021"), ("WikiChunk2021", "2021")
        )
        self.assertEqual(
            wiki_scout.resolve_collection(year="2026"), ("WikiChunk2026", "2026")
        )
        with self.assertRaises(ValueError):
            wiki_scout.resolve_collection(year="1999")

    def test_resolve_collection_defaults_to_2026(self) -> None:
        with patch.dict("os.environ", {"EMPIRE_WIKI_DEFAULT_YEAR": "2026"}, clear=False):
            self.assertEqual(
                wiki_scout.resolve_collection(year=None),
                ("WikiChunk2026", "2026"),
            )

    def test_write_cache_hit_frontmatter_and_path(self) -> None:
        hit = {
            "collection": "WikiChunk",
            "snapshot_year": "2017",
            "snapshot_id": "20170301",
            "title": "Battle of Cambrai",
            "text": "A" * 100,
            "doc_id": "wikipedia:20170301:cambrai",
            "chunk_id": "chunk-1",
            "object_id": "abcdef12-3456-7890",
            "distance": 0.12,
            "query": "Cambrai",
        }
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp)
            path = wiki_scout.write_cache_hit(hit, cache_dir=cache)
            self.assertTrue(path.is_file())
            self.assertTrue(str(path).startswith(str(cache)))
            text = path.read_text(encoding="utf-8")
            self.assertIn("source: weaviate", text)
            self.assertIn("kind: wiki_chunk", text)
            self.assertIn('snapshot_year: "2017"', text)
            self.assertIn('title: "Battle of Cambrai"', text)
            self.assertIn('query: "Cambrai"', text)
            self.assertIn("distance: 0.12", text)
            self.assertIn("# Battle of Cambrai (2017)", text)

    def test_write_compare_cache_shape(self) -> None:
        hits_by_year = {
            "2017": [
                {
                    "title": "Cambrai",
                    "text": "old text",
                    "distance": 0.2,
                }
            ],
            "2021": [],
            "2026": [
                {
                    "title": "Cambrai",
                    "text": "new text",
                    "distance": 0.1,
                }
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = wiki_scout.write_compare_cache(
                "Cambrai", hits_by_year, cache_dir=Path(tmp)
            )
            text = path.read_text(encoding="utf-8")
            self.assertIn("kind: truth_drift_compare", text)
            self.assertIn('query: "Cambrai"', text)
            self.assertIn("## 2017", text)
            self.assertIn("## 2021", text)
            self.assertIn("_No hits._", text)
            self.assertIn("## 2026", text)
            self.assertIn("new text", text)

    def test_phrase_query_retries_the_bare_title(self) -> None:
        """Measured in the browser 2026-09-24: "The White Stripes studio albums" missed, and the model
        then told the Architect the *page* did not exist. The tool now retries the bare title itself."""

        dns_payload = {
            "ok": True,
            "query": "The White Stripes",
            "source": "title_dns",
            "titles": ["The White Stripes"],
            "cards": [{"title": "The White Stripes", "snippet": "American rock duo"}],
            "usable": True,
        }

        def fake_dns(query, **kwargs):
            return dict(dns_payload) if str(query).strip() == "The White Stripes" else None

        with patch.object(wiki_scout, "_search_via_title_dns", side_effect=fake_dns):
            result = wiki_scout.search("The White Stripes studio albums", write_files=False)

        self.assertTrue(result["ok"], result)
        self.assertEqual(result["retried_from"], "The White Stripes studio albums")
        self.assertEqual(result["resolved_title"], "The White Stripes")
        self.assertIn("exact titles", result["coverage_note"])

    def test_bare_title_helper_strips_only_trailing_modifiers(self) -> None:
        cases = {
            "The White Stripes studio albums": "The White Stripes",
            "The White Stripes discography": "The White Stripes",
            "Drum kit components": "Drum kit",
            "The Following cast": "The Following",
            "The Following ratings table": "The Following",
            "Magnet": "",  # already bare: never retry
            "": "",
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                self.assertEqual(wiki_scout.bare_title_from_phrase(query), expected)

    def test_retry_can_be_disabled_by_env(self) -> None:
        with (
            patch.object(wiki_scout, "_search_via_title_dns", return_value=None) as dns,
            patch.dict("os.environ", {"EMPIRE_WIKI_BARE_RETRY": "0"}, clear=False),
        ):
            result = wiki_scout.search("Drum kit components", write_files=False)
        self.assertFalse(result["ok"])
        self.assertEqual(dns.call_count, 1, "with the retry off, only the original query runs")

    def test_search_graceful_when_weaviate_down(self) -> None:
        with (
            patch.object(wiki_scout, "_search_via_title_dns", return_value=None),
            patch.object(wiki_scout, "check_weaviate", return_value=(False, "down")),
        ):
            result = wiki_scout.search("Cambrai", year=2017, write_files=False)
        self.assertFalse(result["ok"])
        self.assertIn("Title DNS found no page", result["error"])
        self.assertNotIn("8091", result["error"])
        # Instruction may say "Do NOT mention Weaviate" — that is fine.
        self.assertEqual(result["paths"], [])

    def test_search_skips_weaviate_by_default(self) -> None:
        with (
            patch.object(wiki_scout, "_search_via_title_dns", return_value=None),
            patch.object(wiki_scout, "check_weaviate") as weaviate,
            patch.dict("os.environ", {"EMPIRE_WIKI_WEAVIATE_FALLBACK": "0"}, clear=False),
        ):
            result = wiki_scout.search("Cambrai", year=2017, write_files=False)
        weaviate.assert_not_called()
        self.assertFalse(result["ok"])
        self.assertIn("Title DNS found no page", result["error"])

    def test_search_title_dns_works_when_weaviate_down(self) -> None:
        dns_payload = {
            "ok": True,
            "query": "V",
            "source": "title_dns",
            "titles": ["V (1983 miniseries)"],
            "cards": [{"title": "V (1983 miniseries)", "snippet": "Kenneth Johnson"}],
            "usable": True,
            "paths": [],
        }
        with (
            patch.object(wiki_scout, "_search_via_title_dns", return_value=dns_payload),
            patch.object(wiki_scout, "check_weaviate", return_value=(False, "down")) as weaviate,
        ):
            result = wiki_scout.search(
                "what actors played in the 1980s miniseries called 'V'",
                year=2026,
                write_files=False,
            )
        weaviate.assert_not_called()
        self.assertTrue(result["ok"])
        self.assertEqual(result["source"], "title_dns")
        self.assertEqual(result["titles"], ["V (1983 miniseries)"])

    def test_dns_ambiguity_auto_selects_primary_entity(self) -> None:
        primary = DnsHit(
            title="The White Stripes",
            path="D:\\wiki_md\\2026\\white-stripes.md",
            rel_path="white-stripes.md",
            page_id="band",
            year="2026",
        )
        album = DnsHit(
            title="The White Stripes (album)",
            path="D:\\wiki_md\\2026\\white-stripes-album.md",
            rel_path="white-stripes-album.md",
            page_id="album",
            year="2026",
        )
        dns_result = type("DnsResult", (), {"status": "ambiguous", "candidates": (album, primary)})()
        lead = {"ok": True, "title": primary.title, "lead": "An American rock band.", "path": primary.path}
        with (
            patch("pipeline.wiki_title_dns.resolve", return_value=dns_result),
            patch("pipeline.wiki_read_lead.wiki_read_lead", return_value=lead),
        ):
            result = wiki_scout._search_via_title_dns("the white stripes", year="2026", limit=3)
        self.assertIsNotNone(result)
        assert result is not None
        self.assertTrue(result["usable"])
        self.assertEqual(result["titles"], ["The White Stripes"])
        self.assertNotIn("album", result["coverage_note"].casefold())
        self.assertNotIn("album", result["chat_reply_rule"].casefold())
        self.assertIn("Answer directly", result["chat_reply_rule"])

    def test_repeat_search_call_is_flagged(self) -> None:
        """Premature-completion signature: the same landing search twice in one session."""
        wiki_scout.reset_search_calls()
        self.addCleanup(wiki_scout.reset_search_calls)
        self.assertFalse(wiki_scout.note_search_call("Who is Kate Bush?", "2026"))
        self.assertTrue(wiki_scout.note_search_call("Who is Kate Bush?", "2026"))
        # Case/whitespace differences are the same search.
        self.assertTrue(wiki_scout.note_search_call("  who is KATE bush?  ", "2026"))
        # A different snapshot year is a different search (Truth Drift).
        self.assertFalse(wiki_scout.note_search_call("Who is Kate Bush?", "2021"))

    def test_repeat_call_hint_names_the_deeper_tools(self) -> None:
        self.assertIn("wiki_read_section", wiki_scout.REPEAT_CALL_HINT)
        self.assertIn("wiki_extract", wiki_scout.REPEAT_CALL_HINT)

    def test_search_strike_escalates_then_resets_after_window(self) -> None:
        """Measured 2026-09-23: the 14B ignored the soft hint 6x (7 searches, 66 s). Strike 3
        must be distinguishable so the tool can refuse instead of paying another round-trip."""

        wiki_scout.reset_search_calls()
        self.addCleanup(wiki_scout.reset_search_calls)
        self.assertEqual(wiki_scout.search_strike("Magnets", "2026"), 1)
        self.assertEqual(wiki_scout.search_strike("magnets", "2026"), 2)
        self.assertEqual(wiki_scout.search_strike("MAGNETS ", "2026"), 3)
        self.assertEqual(wiki_scout.search_strike("Magnets", "2026"), 4)

        # A later legitimate question about the same subject must start over, not be refused.
        key = wiki_scout._search_key("Magnets", "2026")
        count, _ = wiki_scout._SEARCH_CALLS[key]
        wiki_scout._SEARCH_CALLS[key] = (count, 0.0)
        self.assertEqual(wiki_scout.search_strike("Magnets", "2026"), 1)

    def test_hard_stop_hint_forbids_more_tools(self) -> None:
        hint = wiki_scout.HARD_STOP_REPEAT_HINT
        self.assertIn("STOP", hint)
        self.assertIn("Do NOT call any more tools", hint)

    def test_should_refuse_repeat_starts_at_strike_three(self) -> None:
        """The MCP tool refuses on strike 3 so a stuck turn cannot buy another round-trip."""

        self.assertFalse(wiki_scout.should_refuse_repeat(1))
        self.assertFalse(wiki_scout.should_refuse_repeat(2))
        self.assertTrue(wiki_scout.should_refuse_repeat(3))
        self.assertTrue(wiki_scout.should_refuse_repeat(7))
        self.assertEqual(wiki_scout.HARD_STOP_REPEAT_AT, 3)

    def test_search_writes_with_mocked_backend(self) -> None:
        row = {
            "title": "Cambrai",
            "text": "Battle details here.",
            "doc_id": "wikipedia:20170301:x",
            "chunk_id": "c1",
            "snapshot_id": "20170301",
            "_additional": {"id": "deadbeef-0001", "distance": 0.05},
        }
        with tempfile.TemporaryDirectory() as tmp:
            lock = Path(tmp) / "lock.json"
            with (
                patch.object(wiki_scout, "_search_via_title_dns", return_value=None),
                patch.object(wiki_scout, "check_weaviate", return_value=(True, "ready")),
                patch.object(wiki_scout, "embed_query", return_value=[0.1, 0.2, 0.3]),
                patch.object(wiki_scout, "_graphql_hybrid_search", return_value=[row]),
                patch.dict(
                    "os.environ",
                    {
                        "EMPIRE_WIKI_WEAVIATE_FALLBACK": "1",
                        "EMPIRE_WIKI_LOOKUP_LOCK": str(lock),
                    },
                    clear=False,
                ),
            ):
                result = wiki_scout.search(
                    "Cambrai",
                    year=2017,
                    limit=1,
                    cache_dir=Path(tmp),
                )
            self.assertTrue(result["ok"])
            self.assertEqual(result["titles"], ["Cambrai"])
            self.assertEqual(len(result["paths"]), 1)
            self.assertTrue(Path(result["paths"][0]).is_file())

    def test_resolve_promote_dataset_compare(self) -> None:
        body = "---\nkind: truth_drift_compare\ncognee_dataset: truth_drift\n---\n# x\n"
        chosen, reason = wiki_scout.resolve_promote_dataset("compare_x.md", body)
        self.assertEqual(chosen, "truth_drift")
        self.assertEqual(reason, "front_matter_cognee_dataset")

    def test_resolve_promote_dataset_wiki_chunk(self) -> None:
        body = "---\nkind: wiki_chunk\ncognee_dataset: eve_memory\n---\n# x\n"
        chosen, reason = wiki_scout.resolve_promote_dataset("hit.md", body)
        self.assertEqual(chosen, "eve_memory")
        self.assertEqual(reason, "front_matter_cognee_dataset")

    def test_resolve_promote_dataset_rejects_bad_override(self) -> None:
        chosen, err = wiki_scout.resolve_promote_dataset("x.md", "", dataset="not_allowed")
        self.assertIsNone(chosen)
        self.assertIn("dataset must be one of", err or "")

    def test_write_cache_hit_includes_cognee_dataset(self) -> None:
        hit = {
            "collection": "WikiChunk",
            "snapshot_year": "2017",
            "snapshot_id": "20170301",
            "title": "Test",
            "text": "body",
            "doc_id": "d",
            "chunk_id": "c",
            "object_id": "oid12345",
            "distance": 0.1,
            "query": "q",
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = wiki_scout.write_cache_hit(hit, cache_dir=Path(tmp))
            text = path.read_text(encoding="utf-8")
            self.assertIn('cognee_dataset: "eve_memory"', text)


if __name__ == "__main__":
    unittest.main()
