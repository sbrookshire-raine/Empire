from __future__ import annotations

import asyncio
import unittest
from unittest.mock import patch

from frontend import serve


class CatalogPreRouterTests(unittest.TestCase):
    def test_explicit_catalog_intent_injects_results(self) -> None:
        with patch(
            "pipeline.discovery_catalog.search_catalog",
            side_effect=lambda query, limit=5: {"ok": True, "query": query, "results": [{"id": "local/scenario-regret"}]},
        ) as search:
            block = serve._catalog_context(
                "Query your catalog for tools related to 'decision making' or 'minimax'."
            )
        self.assertIn("SYSTEM NOTE: Catalog search returned", block)
        self.assertIn("local/scenario-regret", block)
        self.assertEqual([call.args[0] for call in search.call_args_list], ["decision making", "minimax"])

    def test_catalog_router_ignores_later_wikipedia_clause(self) -> None:
        with patch("pipeline.discovery_catalog.search_catalog", return_value={"ok": True, "results": []}) as search:
            serve._catalog_context(
                "Query your catalog for 'minimax'. Then, look up the Wikipedia article for 'Agent-based model'."
            )
        self.assertEqual([call.args[0] for call in search.call_args_list], ["minimax"])

    def test_ordinary_prompt_has_no_catalog_context(self) -> None:
        self.assertEqual(serve._catalog_context("Summarize this local evidence."), "")

    def test_async_router_ignores_wikipedia_title(self) -> None:
        async def fake_intent(*args, **kwargs):
            return "minimax"

        async def run():
            with patch.object(serve, "_extract_catalog_intent", fake_intent), patch(
                "pipeline.discovery_catalog.search_catalog",
                return_value={"ok": True, "results": [{"id": "local/scenario-regret"}]},
            ):
                return await serve._catalog_context_async(
                    "Find minimax tools, then read Wikipedia article 'Agent-based model'."
                )

        block = asyncio.run(run())
        self.assertIn("local/scenario-regret", block)
        self.assertNotIn("Agent-based model", block)


if __name__ == "__main__":
    unittest.main()