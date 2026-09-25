"""Research bench: the baseline proves the hole, the grader proves the fix.

`docs/RESEARCH_CLOSURE.md` requires a measured regression before any architecture change. The
Architect's ask — *"let her search the internet if I need her to"* — had no capable tool, so this
bench is the measurement: the shipped cases must show `search` as blocked while no search tool
exists, and must flip to ready once one does.
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import research_bench


class BenchFileTests(unittest.TestCase):
    def test_shipped_bench_is_valid_and_covers_the_named_needs(self) -> None:
        cases = research_bench.load_cases()
        self.assertGreaterEqual(len(cases), 8, "expected a real bench")
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)), "case ids must be unique")
        for case in cases:
            self.assertTrue(str(case.get("query") or "").strip(), case)
            self.assertIn(case.get("needs"), research_bench.NEED_TOOLS, case)
        needs = {case["needs"] for case in cases}
        self.assertLessEqual({"search", "fetch", "github", "archive", "artefact"}, needs)

    def test_cases_without_a_query_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bench.jsonl"
            path.write_text(
                json.dumps({"id": "a", "query": "  "}) + "\n"
                + json.dumps({"id": "b", "query": "real question", "needs": "none"}) + "\n",
                encoding="utf-8",
            )
            cases = research_bench.load_cases(path)
        self.assertEqual([case["id"] for case in cases], ["b"])


class CapabilityBaselineTests(unittest.TestCase):
    def _baseline_with(self, names: set[str]) -> dict:
        with patch.object(research_bench, "_registry_names", lambda: names):
            return research_bench.capability_baseline()

    def test_public_web_search_is_blocked_while_no_search_tool_exists(self) -> None:
        """The measured hole: only archive/github/url-fetch tools exist, so `search` is blocked."""

        payload = self._baseline_with(
            {
                "wiki_scout_search",
                "github_scout_search",
                "web_scout",
                "create_spreadsheet",
            }
        )
        self.assertFalse(payload["ok"])
        self.assertEqual(payload["blocked_needs"], ["search"])
        blocked = [row for row in payload["rows"] if row["verdict"] == "blocked"]
        self.assertEqual(sorted(row["id"] for row in blocked), ["rb_01", "rb_02"])

    def test_a_search_tool_flips_those_cases_to_ready(self) -> None:
        """The gate the fix must pass: add the tool, and the same bench goes green."""

        payload = self._baseline_with(
            {
                "wiki_scout_search",
                "github_scout_search",
                "web_scout",
                "create_spreadsheet",
                "searxng_search",
            }
        )
        self.assertTrue(payload["ok"], payload["rows"])
        self.assertEqual(payload["blocked_needs"], [])
        search_rows = [row for row in payload["rows"] if row["needs"] == "search"]
        self.assertTrue(all(row["verdict"] == "ready" for row in search_rows))

    def test_a_disabled_tool_does_not_count_as_capability(self) -> None:
        """`web_search` is `disableTool()` — naming it in the table must not satisfy the need."""

        payload = self._baseline_with({"wiki_scout_search"})
        self.assertIn("search", payload["blocked_needs"])
        search_row = next(row for row in payload["rows"] if row["needs"] == "search")
        self.assertEqual(search_row["available"], [])

    def test_resident_versus_admission_is_reported(self) -> None:
        with (
            patch.object(research_bench, "_registry_names", lambda: {"wiki_scout_search"}),
            patch.object(research_bench, "_resident_names", lambda: {"wiki_scout_search"}),
        ):
            payload = research_bench.capability_baseline()
        row = next(item for item in payload["rows"] if item["id"] == "rb_05")
        self.assertEqual(row["resident"], ["wiki_scout_search"])
        self.assertIn("resident", row["reason"])


class GraderTests(unittest.TestCase):
    FETCH_CASE = {
        "id": "rb_x",
        "needs": "fetch",
        "expect_tool_any": ["web_scout"],
        "must_cite_source": True,
    }

    def test_a_good_turn_passes(self) -> None:
        result = research_bench.grade(
            self.FETCH_CASE,
            answer="Per https://docs.searxng.org/dev/search_api.html you pass format=json.",
            tools=["web_scout"],
        )
        self.assertTrue(result["passed"], result["issues"])
        self.assertTrue(result["evidence"]["cited_url"])
        self.assertEqual(result["evidence"]["tools"], ["web_scout"])

    def test_a_missing_expected_tool_fails_with_the_evidence(self) -> None:
        result = research_bench.grade(
            self.FETCH_CASE,
            answer="Per https://example.com it works.",
            tools=[],
        )
        self.assertFalse(result["passed"])
        self.assertIn("no expected tool ran (saw: none)", result["issues"])

    def test_a_missing_source_url_fails(self) -> None:
        result = research_bench.grade(
            self.FETCH_CASE,
            answer="You just add format=json to the query.",
            tools=["web_scout"],
        )
        self.assertFalse(result["passed"])
        self.assertIn("no source URL in the answer", result["issues"])

    def test_forbidden_claims_are_caught(self) -> None:
        result = research_bench.grade(
            self.FETCH_CASE,
            answer="As an AI language model I cannot browse. See https://x.test",
            tools=["web_scout"],
        )
        self.assertFalse(result["passed"])
        self.assertTrue(any("forbidden" in issue for issue in result["issues"]))

    def test_the_artefact_must_come_from_a_tool_not_chat_text(self) -> None:
        """A markdown table in the reply is chat, not a document he can open."""

        case = {
            "id": "rb_t",
            "needs": "artefact",
            "expect_tool_any": ["create_spreadsheet"],
            "expect_artefact": True,
        }
        produced = research_bench.grade(
            case,
            answer="Saved it as 00_Resource_Queue/white_stripes_leads.xlsx",
            tools=["create_spreadsheet"],
        )
        self.assertTrue(produced["passed"], produced["issues"])
        chat_only = research_bench.grade(case, answer="| year | lead |\n|---|---|\n| 2017 | duo |\n")
        self.assertFalse(chat_only["passed"])
        self.assertIn("no artefact: no create_spreadsheet/author_code call ran", chat_only["issues"])

    def test_an_open_ended_case_requires_prose_not_pretend_evidence(self) -> None:
        case = {
            "id": "rb_p",
            "needs": "none",
            "expect_tool_any": [],
            "must_not_mention": ["I searched", "the archive says"],
        }
        honest = research_bench.grade(case, answer="Local models are getting better fast.")
        self.assertTrue(honest["passed"], honest["issues"])
        pretending = research_bench.grade(case, answer="I searched the web and the archive says so.")
        self.assertFalse(pretending["passed"])

    def test_empty_reply_fails(self) -> None:
        result = research_bench.grade(self.FETCH_CASE, answer="   ", tools=["web_scout"])
        self.assertFalse(result["passed"])
        self.assertIn("empty reply", result["issues"])

    def test_summarise_counts_per_need(self) -> None:
        results = [
            {"id": "a", "needs": "search", "passed": False, "issues": ["x"]},
            {"id": "b", "needs": "archive", "passed": True, "issues": []},
            {"id": "c", "needs": "archive", "passed": False, "issues": ["y"]},
        ]
        summary = research_bench.summarise(results)
        self.assertEqual(summary["cases"], 3)
        self.assertEqual(summary["passed"], 1)
        self.assertEqual(summary["failed"], 2)
        self.assertEqual(summary["per_need"]["archive"], {"pass": 1, "fail": 1})
        self.assertEqual([item["id"] for item in summary["failures"]], ["a", "c"])


if __name__ == "__main__":
    unittest.main()

