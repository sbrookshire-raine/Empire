"""Unit tests for the on-demand tool documentation registry (R-03)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import prompt_budget, tool_registry


class ToolRegistryTests(unittest.TestCase):
    """Backend behaviour against a temp docs directory."""

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.docs = Path(tmp.name)
        (self.docs / "example_tool.md").write_text(
            "---\n"
            "name: example_tool\n"
            "toolbelt: wiki_local\n"
            "one_line: Does the example thing.\n"
            "---\n\n"
            "## Description\n\nLong form prose.\n",
            encoding="utf-8",
        )
        patcher = patch.object(tool_registry, "docs_dir", lambda: self.docs)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_index_lists_front_matter(self) -> None:
        entries = tool_registry.index()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["name"], "example_tool")
        self.assertEqual(entries[0]["toolbelt"], "wiki_local")
        self.assertEqual(entries[0]["one_line"], "Does the example thing.")

    def test_doc_returns_body_without_front_matter(self) -> None:
        result = tool_registry.doc("example_tool")
        self.assertTrue(result["ok"])
        self.assertNotIn("---", result["doc"])
        self.assertIn("Long form prose.", result["doc"])
        self.assertFalse(result["truncated"])

    def test_doc_is_bounded(self) -> None:
        (self.docs / "big_tool.md").write_text(
            "---\nname: big_tool\n---\n\n" + ("x" * 5000), encoding="utf-8"
        )
        result = tool_registry.doc("big_tool", max_chars=200)
        self.assertTrue(result["ok"])
        self.assertTrue(result["truncated"])
        self.assertLessEqual(len(result["doc"]), 260)

    def test_missing_tool_reports_what_is_documented(self) -> None:
        result = tool_registry.doc("nope_tool")
        self.assertFalse(result["ok"])
        self.assertIn("example_tool", result["documented_tools"])

    def test_path_traversal_is_rejected(self) -> None:
        for bad in ("../secrets", "a/b", "a\\b", ""):
            self.assertFalse(tool_registry.doc(bad)["ok"], bad)

    def test_missing_reports_undocumented_names(self) -> None:
        self.assertEqual(tool_registry.missing(["example_tool"]), [])
        self.assertEqual(tool_registry.missing(["example_tool", "ghost"]), ["ghost"])


class RepoDocsCoverageTests(unittest.TestCase):
    """Uses the real docs directory: the R-03 trade must hold in the shipped tree."""

    def hot_set(self) -> list[str]:
        names: list[str] = []
        for path in prompt_budget.TOOLS.glob("*.ts"):
            text = path.read_text(encoding="utf-8")
            gated = "isCapabilityActive" in text or "isCategoryEnabled" in text
            if not gated or '"wiki_local"' in text:
                names.append(path.stem)
        return names

    def test_repo_docs_cover_the_hot_set(self) -> None:
        names = self.hot_set()
        self.assertGreater(len(names), 30, "expected a substantial default-enabled set")
        self.assertEqual(tool_registry.missing(names), [], "hot-set tools missing documentation")
        documented = {entry["name"] for entry in tool_registry.index()}
        self.assertGreaterEqual(len(documented), 80, "expected docs for essentially every tool")

    def test_every_tool_has_a_doc(self) -> None:
        """Coverage beyond the hot set, so moving a tool into the default set is safe."""

        all_tools = sorted(path.stem for path in prompt_budget.TOOLS.glob("*.ts"))
        self.assertEqual(tool_registry.missing(all_tools), [], "tools missing documentation")


if __name__ == "__main__":
    unittest.main()