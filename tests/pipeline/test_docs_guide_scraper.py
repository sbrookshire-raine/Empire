"""Tests for docs guide scraper (mocked fetch)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import docs_guide_scraper


class DocsGuideScraperTests(unittest.TestCase):
    def test_discover_single_page_fallback(self) -> None:
        def fake_fetch(url: str, *, timeout: float = 45.0) -> dict:
            if url.endswith("llms.txt") or url.endswith("sitemap.xml"):
                return {"ok": False, "error": "missing"}
            return {
                "ok": True,
                "url": url,
                "title": "Docs Home",
                "text": "Welcome to the documentation.",
            }

        with mock.patch.object(docs_guide_scraper, "fetch_url", side_effect=fake_fetch):
            result = docs_guide_scraper.discover_pages("https://docs.example.com/start")
        self.assertTrue(result["ok"])
        self.assertEqual(result["method"], "single-page")
        self.assertEqual(result["count"], 1)

    def test_scrape_site_writes_file(self) -> None:
        llms_body = "# Page One\n\nHello world.\n\n# Page Two\n\nSecond page.\n"

        def fake_fetch(url: str, *, timeout: float = 45.0) -> dict:
            if "llms-full.txt" in url or "llms.txt" in url:
                return {"ok": True, "url": url, "title": "llms", "text": llms_body}
            return {"ok": False, "error": "skip"}

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(docs_guide_scraper, "fetch_url", side_effect=fake_fetch):
                result = docs_guide_scraper.scrape_site(
                    "https://docs.example.com/",
                    cache_dir=Path(tmp),
                )
            self.assertTrue(result["ok"])
            self.assertGreaterEqual(result["pages_fetched"], 2)
            path = Path(result["path"])
            self.assertTrue(path.is_file())
            text = path.read_text(encoding="utf-8")
            self.assertIn("Complete Documentation Guide", text)
            self.assertIn("Page One", text)


if __name__ == "__main__":
    unittest.main()
