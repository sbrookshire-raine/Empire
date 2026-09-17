"""Unit tests for workspace_search, query_data, and read_document arms."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import query_data, read_document, workspace_search


def _write(root: Path, rel: str, content: str) -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


class WorkspaceSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        _write(self.root, "notes/alpha.md", "The quick brown fox\njumps over the lazy dog\n")
        _write(self.root, "notes/beta.txt", "nothing relevant here\n")
        _write(self.root, "notes/skip.bin", "fox in binary")  # not a text ext

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_search_finds_literal(self) -> None:
        res = workspace_search.search("fox", roots=[self.root])
        self.assertTrue(res["ok"])
        self.assertEqual(res["count"], 1)
        self.assertIn("alpha.md", res["results"][0]["path"])

    def test_search_binary_ext_skipped(self) -> None:
        res = workspace_search.search("fox", roots=[self.root])
        paths = [r["path"] for r in res["results"]]
        self.assertNotIn("skip.bin", "".join(paths))

    def test_redaction(self) -> None:
        _write(self.root, "secrets.env", "API_KEY=sk-supersecretvalue123\n")
        res = workspace_search.search("sk-supersecret", roots=[self.root])
        self.assertTrue(res["ok"])
        self.assertIn("REDACTED", res["results"][0]["text"])

    def test_empty_query_rejected(self) -> None:
        res = workspace_search.search("   ", roots=[self.root])
        self.assertFalse(res["ok"])


class QueryDataTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.csv = _write(
            self.root,
            "data/sample.csv",
            "name,age\nada,36\ngrace,44\nlinus,55\n",
        )

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_csv_query(self) -> None:
        with patch.dict(os.environ, {"EMPIRE_QUERY_ROOTS": str(self.root)}):
            res = query_data.query(
                "SELECT name FROM data WHERE age > 40 ORDER BY age",
                data_file=str(self.csv),
            )
        self.assertTrue(res["ok"], res.get("error"))
        self.assertEqual(res["columns"], ["name"])
        self.assertEqual(res["row_count"], 2)

    def test_blocked_network(self) -> None:
        res = query_data.query("SELECT * FROM 'https://example.com/x.csv'")
        self.assertFalse(res["ok"])

    def test_blocked_multiple_statements(self) -> None:
        res = query_data.query("SELECT 1; DROP TABLE x;")
        self.assertFalse(res["ok"])

    def test_blocked_non_read(self) -> None:
        res = query_data.query("DELETE FROM data")
        self.assertFalse(res["ok"])

    def test_path_escape_rejected(self) -> None:
        with patch.dict(os.environ, {"EMPIRE_QUERY_ROOTS": str(self.root)}):
            res = query_data.query("SELECT 1", data_file=r"C:\Windows\system32\config\SAM")
        self.assertFalse(res["ok"])


class ReadDocumentTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.md = _write(self.root, "doc.md", "# Title\n\nhello world\n")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_read_markdown_direct(self) -> None:
        with patch.dict(os.environ, {"EMPIRE_READ_DOC_ROOTS": str(self.root)}):
            res = read_document.read_document(str(self.md))
        self.assertTrue(res["ok"], res.get("error"))
        self.assertEqual(res["engine"], "direct")
        self.assertIn("hello world", res["content"])

    def test_read_missing(self) -> None:
        with patch.dict(os.environ, {"EMPIRE_READ_DOC_ROOTS": str(self.root)}):
            res = read_document.read_document(str(self.root / "nope.md"))
        self.assertFalse(res["ok"])

    def test_read_network_rejected(self) -> None:
        res = read_document.read_document("https://example.com/a.pdf")
        self.assertFalse(res["ok"])


if __name__ == "__main__":
    unittest.main()
