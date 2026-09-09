"""Tests for embedding A/B eval (mocked Ollama — no live models required)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import embedding_ab


def _vec(*values: float) -> list[float]:
    return list(values)


class EmbeddingAbTests(unittest.TestCase):
    def test_cosine_similarity(self) -> None:
        self.assertAlmostEqual(embedding_ab.cosine_similarity(_vec(1, 0), _vec(1, 0)), 1.0)
        self.assertAlmostEqual(embedding_ab.cosine_similarity(_vec(1, 0), _vec(0, 1)), 0.0)

    def test_case_hit(self) -> None:
        self.assertTrue(embedding_ab._case_hit(["c1"], ["c1", "c2"], 2))
        self.assertFalse(embedding_ab._case_hit(["c1"], ["c2", "c3"], 1))

    def test_rank_candidates_mocked(self) -> None:
        def fake_embed(text: str, *, model: str, base_url: str | None = None) -> list[float]:
            lowered = text.lower()
            if "weaviate" in lowered:
                return _vec(1.0, 0.0, 0.0)
            if "pocketbase" in lowered:
                return _vec(0.0, 1.0, 0.0)
            return _vec(0.0, 0.0, 1.0)

        candidates = [
            {"id": "c1", "text": "Weaviate on-demand Docker"},
            {"id": "c2", "text": "PocketBase tasks"},
        ]
        with mock.patch.object(embedding_ab, "embed_text", side_effect=fake_embed):
            out = embedding_ab.rank_candidates(
                "local weaviate wikipedia",
                candidates,
                model="nomic-embed-text",
                top_k=2,
            )
        self.assertTrue(out["ok"])
        self.assertEqual(out["results"][0]["id"], "c1")

    def test_run_eval_mocked_writes_report(self) -> None:
        fixture = [
            {
                "id": "one",
                "query": "weaviate docker",
                "top_k": 1,
                "expected_top_ids": ["c1"],
                "candidates": [
                    {"id": "c1", "text": "Weaviate Docker wiki"},
                    {"id": "c2", "text": "PocketBase sqlite"},
                ],
            }
        ]

        def fake_embed(text: str, *, model: str, base_url: str | None = None) -> list[float]:
            if "weaviate" in text.lower():
                return _vec(1.0, 0.0)
            if "pocketbase" in text.lower():
                return _vec(0.0, 1.0)
            return _vec(0.5, 0.5)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture_path = root / "cases.json"
            fixture_path.write_text(json.dumps(fixture), encoding="utf-8")
            acceptance = root / "acceptance"
            reports = root / "reports"
            with (
                mock.patch.object(embedding_ab, "embed_text", side_effect=fake_embed),
                mock.patch.object(embedding_ab, "model_available", return_value=(True, "ok")),
                mock.patch.object(embedding_ab, "ACCEPTANCE_DIR", acceptance),
                mock.patch.object(embedding_ab, "REPORT_DIR", reports),
                mock.patch.object(embedding_ab, "production_model", return_value="nomic-embed-text"),
                mock.patch.object(embedding_ab, "candidate_model", return_value="qwen3-embedding:0.6b"),
            ):
                result = embedding_ab.run_eval(fixture_path=fixture_path)

            self.assertTrue(result["ok"])
            self.assertEqual(result["production_hits"], 1)
            self.assertEqual(result["candidate_hits"], 1)
            self.assertEqual(result["verdict"], "tie")
            self.assertTrue(Path(result["acceptance_path"]).is_file())
            self.assertTrue(Path(result["report_path"]).is_file())

    def test_model_unavailable_skips_embed(self) -> None:
        fixture = [
            {
                "id": "one",
                "query": "test",
                "top_k": 1,
                "expected_top_ids": ["c1"],
                "candidates": [{"id": "c1", "text": "doc"}],
            }
        ]
        with tempfile.TemporaryDirectory() as tmp:
            fixture_path = Path(tmp) / "cases.json"
            fixture_path.write_text(json.dumps(fixture), encoding="utf-8")
            with (
                mock.patch.object(
                    embedding_ab,
                    "model_available",
                    side_effect=lambda m, **_: (m == "nomic-embed-text", "ok" if m == "nomic-embed-text" else "missing"),
                ),
                mock.patch.object(embedding_ab, "embed_text", return_value=_vec(1.0)),
                mock.patch.object(embedding_ab, "ACCEPTANCE_DIR", Path(tmp) / "acc"),
                mock.patch.object(embedding_ab, "REPORT_DIR", Path(tmp) / "rep"),
                mock.patch.object(embedding_ab, "production_model", return_value="nomic-embed-text"),
                mock.patch.object(embedding_ab, "candidate_model", return_value="qwen3-embedding:0.6b"),
            ):
                result = embedding_ab.run_eval(fixture_path=fixture_path)
        self.assertTrue(result["ok"])
        cand = result["models"]["qwen3-embedding:0.6b"]
        self.assertFalse(cand["ok"])
        self.assertEqual(cand["hits"], 0)

    def test_empty_query_rejected(self) -> None:
        out = embedding_ab.rank_candidates("", [{"id": "c1", "text": "x"}], model="m")
        self.assertFalse(out["ok"])


if __name__ == "__main__":
    unittest.main()
