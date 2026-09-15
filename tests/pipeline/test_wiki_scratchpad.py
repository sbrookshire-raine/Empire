"""Tests for Wikipedia research scratchpad + Error Book."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import wiki_scratchpad


class WikiScratchpadTests(unittest.TestCase):
    def test_upsert_read_clear(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pad = Path(tmp) / "scratch.json"
            with patch.dict("os.environ", {"EMPIRE_WIKI_SCRATCHPAD": str(pad)}, clear=False):
                wiki_scratchpad.scratch_clear("s1")
                up = wiki_scratchpad.scratch_upsert(
                    "Lead actor linked to Elm Street",
                    session_id="s1",
                    title="V (1983 miniseries)",
                )
                self.assertTrue(up.get("ok"))
                data = wiki_scratchpad.scratch_read("s1")
                self.assertIn("Elm Street", data.get("summary") or "")
                wiki_scratchpad.scratch_clear("s1")
                empty = wiki_scratchpad.scratch_read("s1")
                self.assertEqual(empty.get("summary") or "", "")

    def test_error_book_append_and_mention(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            book = Path(tmp) / "errors.jsonl"
            with patch.dict("os.environ", {"EMPIRE_WIKI_ERROR_BOOK": str(book)}, clear=False):
                wiki_scratchpad.error_book_append(
                    query="Zxqwy Blorf Band discography",
                    reason="not in title registry",
                    title="Zxqwy Blorf Band",
                )
                self.assertTrue(
                    wiki_scratchpad.error_book_mentions_miss("Zxqwy Blorf Band")
                )
                self.assertFalse(wiki_scratchpad.error_book_mentions_miss("Kate Bush"))


if __name__ == "__main__":
    unittest.main()
