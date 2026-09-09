"""Tests for research orchestrator."""

from __future__ import annotations

import unittest
from unittest import mock

from pipeline import research_orchestrator


class ResearchOrchestratorTests(unittest.TestCase):
    def test_requires_partner_mode(self) -> None:
        with mock.patch(
            "pipeline.admission_controller.research_partner_enabled",
            return_value=False,
        ):
            result = research_orchestrator.orchestrate("duckdb mcp")
        self.assertFalse(result["ok"])
        self.assertIn("Research Partner", result.get("error", ""))

    def test_orchestrate_mocks_sources(self) -> None:
        with mock.patch(
            "pipeline.admission_controller.research_partner_enabled",
            return_value=True,
        ), mock.patch(
            "pipeline.admission_controller.request_capability",
            return_value={"ok": True, "category": "github_scout"},
        ), mock.patch(
            "pipeline.admission_controller.release_session",
            return_value={"ok": True, "released": ["github_scout"]},
        ), mock.patch(
            "pipeline.github_scout.search_repos",
            return_value={"ok": True, "results": [], "path": ""},
        ):
            result = research_orchestrator.orchestrate(
                "duckdb",
                sources=["github"],
                write_brief=False,
            )
        self.assertTrue(result["ok"])
        self.assertIn("github", result.get("results", {}))


if __name__ == "__main__":
    unittest.main()
