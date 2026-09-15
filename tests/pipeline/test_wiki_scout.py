"""Unit tests for pipeline.wiki_scout cache writers (no live Weaviate)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import wiki_scout


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
