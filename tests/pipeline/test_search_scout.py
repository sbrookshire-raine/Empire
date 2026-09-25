"""SearXNG search: a query tool that is honest when the instance is missing (E-35)."""

from __future__ import annotations

import io
import json
import os
import unittest
import urllib.error
from unittest.mock import patch

from pipeline import search_scout

SAMPLE = {
    "query": "local first llm",
    "number_of_results": 1234,
    "results": [
        {
            "title": "SearXNG — a privacy-respecting metasearch engine",
            "url": "https://docs.searxng.org/",
            "content": "  aggregates   dozens of engines  ",
            "engine": "duckduckgo",
        },
        {"title": "No url here", "content": "ignored without a link"},
        {"title": "Second", "url": "https://example.org/two", "content": "second result", "engine": "brave"},
        {"title": "Third", "url": "https://example.org/three", "engine": "google"},
    ],
}


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        return False


def opener_returning(payload: dict):
    def _open(request, timeout=None):
        return FakeResponse(json.dumps(payload).encode("utf-8"))

    return _open


def opener_raising(error: Exception):
    def _open(request, timeout=None):
        raise error

    return _open


class SearchScoutTests(unittest.TestCase):
    def test_results_are_parsed_and_cleaned(self) -> None:
        found = search_scout.search("local first llm", limit=5, opener=opener_returning(SAMPLE))
        self.assertTrue(found["ok"], found)
        self.assertEqual(len(found["results"]), 3, "entries without a URL are dropped")
        first = found["results"][0]
        self.assertEqual(first["title"], "SearXNG — a privacy-respecting metasearch engine")
        self.assertEqual(first["snippet"], "aggregates dozens of engines", "whitespace collapsed")
        self.assertEqual(found["engine_reported_count"], 1234)
        self.assertIn("not a source", found["note"])

    def test_the_limit_is_capped_not_trusted(self) -> None:
        found = search_scout.search("q", limit=999, opener=opener_returning(SAMPLE))
        self.assertLessEqual(len(found["results"]), search_scout.MAX_LIMIT)

    def test_a_query_is_required(self) -> None:
        payload = search_scout.search("   ", opener=opener_returning(SAMPLE))
        self.assertFalse(payload["ok"])
        self.assertIn("query is required", payload["error"])

    def test_a_down_instance_is_stated_with_the_fix(self) -> None:
        """The measured hole must not turn into a fabricated answer."""

        payload = search_scout.search(
            "anything", opener=opener_raising(urllib.error.URLError("connection refused"))
        )
        self.assertFalse(payload["ok"])
        self.assertIn("not reachable", payload["error"])
        self.assertIn("start-searxng.ps1", payload["hint"])

    def test_json_disabled_explains_the_403(self) -> None:
        error = urllib.error.HTTPError("http://x/search", 403, "Forbidden", {}, None)
        payload = search_scout.search("anything", opener=opener_raising(error))
        self.assertFalse(payload["ok"])
        self.assertIn("refused the JSON format", payload["error"])
        self.assertIn("settings.yml", payload["hint"])

    def test_non_json_body_is_reported(self) -> None:
        def _open(request, timeout=None):
            return FakeResponse(b"<html>not json</html>")

        payload = search_scout.search("anything", opener=_open)
        self.assertFalse(payload["ok"])
        self.assertIn("did not return JSON", payload["error"])

    def test_urls_for_hands_the_desk_a_fetch_list(self) -> None:
        payload = search_scout.urls_for("local first llm", limit=2, opener=opener_returning(SAMPLE))
        self.assertTrue(payload["ok"], payload)
        self.assertEqual(
            payload["urls"], ["https://docs.searxng.org/", "https://example.org/two"]
        )

    def test_urls_for_propagates_the_failure(self) -> None:
        payload = search_scout.urls_for("x", opener=opener_raising(urllib.error.URLError("nope")))
        self.assertFalse(payload["ok"])

    def test_results_carry_a_citation_rule(self) -> None:
        """rb_02's failure mode: the tool ran and the answer cited nothing."""

        found = search_scout.search("local first llm", opener=opener_returning(SAMPLE))
        rule = str(found.get("chat_reply_rule") or "")
        self.assertIn("URL", rule)
        self.assertIn("web_scout", rule)
        self.assertIn("lead", str(found.get("note") or ""))

    def test_base_url_env_override_is_honoured(self) -> None:
        with patch.dict(os.environ, {"EMPIRE_SEARXNG_URL": "http://127.0.0.1:9999/"}):
            self.assertEqual(search_scout.base_url(), "http://127.0.0.1:9999")


if __name__ == "__main__":
    unittest.main()
