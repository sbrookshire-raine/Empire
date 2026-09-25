"""Error Book (autonomous path): a miss logs itself and comes back as an authoritative hint.

Measured 2026-09-24: the book was inert outside the legacy middleware — 52 `wiki_scout_search` calls
in a day, zero entries — so "the local archive doesn't have a page on X" survived as a conclusion
while `Drum kit` and `Juggling` sat in the index. `wiki_scout_search` now appends the miss
server-side (deduped) and attaches `known_miss` + the hint, so no model compliance is needed.
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import wiki_scratchpad

MCP_PATH = Path(__file__).resolve().parents[2] / "mcp" / "wiki_scout_mcp.py"


def _load_mcp():
    """Import the MCP module by path; `mcp` as a package name collides with the FastMCP library."""

    spec = importlib.util.spec_from_file_location("wiki_scout_mcp_under_test", MCP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tool(module, name: str):
    candidate = getattr(module, name)
    for attribute in ("fn", "func", "__wrapped__"):
        if hasattr(candidate, attribute):
            candidate = getattr(candidate, attribute)
    return candidate


MISS = {
    "ok": False,
    "error": "Title DNS found no page for this query in the local Wikipedia archive.",
    "paths": [],
    "titles": [],
    "source": "title_dns",
}


class AutonmousMissLoggingTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.book = Path(self._tmp.name) / "wiki-error-book.jsonl"
        patcher = patch.dict(os.environ, {"EMPIRE_WIKI_ERROR_BOOK": str(self.book)})
        patcher.start()
        self.addCleanup(patcher.stop)
        self.module = _load_mcp()
        self.search = _tool(self.module, "wiki_scout_search")

    def _entries(self) -> list[dict]:
        if not self.book.is_file():
            return []
        return [
            json.loads(line)
            for line in self.book.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_a_miss_is_logged_once_and_flagged_in_the_payload(self) -> None:
        with patch("pipeline.wiki_scout.search", return_value=dict(MISS)):
            first = json.loads(asyncio.run(self.search("learning to play the drums")))
            second = json.loads(asyncio.run(self.search("learning to play the drums")))

        self.assertTrue(first["known_miss"], first)
        self.assertIn("error_book_hint", first)
        self.assertEqual(len(self._entries()), 1, self._entries())
        self.assertEqual(self._entries()[0]["query"], "learning to play the drums")
        self.assertTrue(second["known_miss"])

    def test_the_third_identical_section_read_is_refused(self) -> None:
        """Measured in the browser 2026-09-24: 14 identical `wiki_read_section("albums")` calls in one
        turn; the payload already listed `available_sections` and the model ignored it. The guard is in
        the tool, not the prompt (E-27)."""

        read = _tool(self.module, "wiki_read_section")
        missing = {"ok": True, "title": "The White Stripes", "section_missing": True, "available_sections": ["Discography"]}
        with patch("pipeline.wiki_read_lead.wiki_read", return_value=dict(missing)) as reader:
            first = json.loads(asyncio.run(read("The White Stripes", section="albums")))
            second = json.loads(asyncio.run(read("The White Stripes", section="albums")))
            third = json.loads(asyncio.run(read("The White Stripes", section="albums")))

        self.assertTrue(first.get("ok"))
        self.assertTrue(second.get("ok"))
        self.assertEqual(third.get("refused"), "repeat_section")
        self.assertIn("do not repeat a section name", third["chat_reply_rule"])
        self.assertEqual(reader.call_count, 2, "the refused call never reaches the reader")

    def test_a_hit_is_not_logged(self) -> None:
        hit = {"ok": True, "query": "Drum kit", "cards": [{"title": "Drum kit"}], "usable": True}
        with patch("pipeline.wiki_scout.search", return_value=hit):
            payload = json.loads(asyncio.run(self.search("Drum kit")))
        self.assertTrue(payload["ok"])
        self.assertEqual(self._entries(), [])

    def test_the_book_is_bounded(self) -> None:
        for index in range(wiki_scratchpad._MAX_ERROR_BOOK_ENTRIES + 5):
            wiki_scratchpad.error_book_append(query=f"miss {index}", reason="test")
        self.assertEqual(len(self._entries()), wiki_scratchpad._MAX_ERROR_BOOK_ENTRIES)
        # Newest survive.
        self.assertEqual(self._entries()[-1]["query"], f"miss {wiki_scratchpad._MAX_ERROR_BOOK_ENTRIES + 4}")


if __name__ == "__main__":
    unittest.main()
