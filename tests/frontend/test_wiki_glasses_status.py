"""Unit tests for wiki glasses readiness on /api/wiki/status."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import wiki_api


class WikiGlassesStatusTests(unittest.TestCase):
    def test_glasses_ok_when_index_and_year_root_exist(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            index = root / "title-index.sqlite"
            year_root = root / "2017"
            index.write_bytes(b"sqlite")
            year_root.mkdir()
            with (
                patch("frontend.wiki_api.load_checkpoint", return_value={}),
                patch(
                    "frontend.wiki_api.build_progress_block",
                    return_value={"done": 0},
                ),
                patch("frontend.wiki_api.overnight_pid_alive", return_value=False),
                patch("frontend.wiki_api.status_path", return_value=root / "missing.json"),
                patch("frontend.wiki_api.default_index_path", return_value=index),
                patch("frontend.wiki_api.wiki_md_root", return_value=root),
            ):
                out = wiki_api.wiki_status("2017")
            self.assertTrue(out["ok"])
            self.assertTrue(out["glasses_ok"])

    def test_glasses_not_ok_when_index_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            year_root = root / "2017"
            year_root.mkdir()
            missing = root / "title-index.sqlite"
            with (
                patch("frontend.wiki_api.load_checkpoint", return_value={}),
                patch(
                    "frontend.wiki_api.build_progress_block",
                    return_value={"done": 0},
                ),
                patch("frontend.wiki_api.overnight_pid_alive", return_value=False),
                patch("frontend.wiki_api.status_path", return_value=root / "missing.json"),
                patch("frontend.wiki_api.default_index_path", return_value=missing),
                patch("frontend.wiki_api.wiki_md_root", return_value=root),
            ):
                out = wiki_api.wiki_status("2017")
            self.assertFalse(out["glasses_ok"])
            self.assertIn("title index missing", out["glasses_reason"])

    def test_glasses_health_uses_default_year(self) -> None:
        with patch(
            "frontend.wiki_api.wiki_status",
            return_value={
                "glasses_ok": True,
                "glasses_reason": "ready",
                "title_index_path": "x",
                "wiki_md_year_root": "y",
            },
        ), patch("frontend.wiki_api.default_snapshot_year", return_value="2026"):
            out = wiki_api.wiki_glasses_health()
        self.assertTrue(out["glasses_ok"])
        self.assertEqual(out["year"], "2026")


if __name__ == "__main__":
    unittest.main()
