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
        self.assertIn("[AUTHORITATIVE LOCAL CATALOG CONTEXT]", block)
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

    def test_voice_guard_rejects_wholesale_failure_fiction(self) -> None:
        raw = "Action blocked: GPU VRAM is 405 MB, below the 1 GB safety threshold."
        fictional = "System update successful. New software version installed on all servers."
        self.assertFalse(serve._voice_output_is_safe(raw, fictional))

    def test_resource_guard_blocks_explicit_heavy_request(self) -> None:
        with patch("pipeline.resource_pulse.pulse", return_value={"headroom_ok": False, "headroom_reasons": ["VRAM very low"]}):
            block = serve._resource_guard_context("force-enable vision despite constrained GPU")
        self.assertIn("AUTHORITATIVE RESOURCE BLOCK", block)
        self.assertIn("VRAM very low", block)

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

    def test_catalog_directive_forbids_wiki_for_pure_catalog_ask(self) -> None:
        directive = serve._catalog_directive(
            "Eve, query your catalog for tools related to 'minimax' or 'decision making'."
        )
        self.assertIn("Do NOT call wiki_scout_search", directive)

    def test_catalog_directive_allows_wiki_when_prompt_also_targets_encyclopedia(self) -> None:
        directive = serve._catalog_directive(
            "Query the catalog for 'decision making'. Then, look up the Wikipedia "
            "article for 'Agent-based model'."
        )
        self.assertIn("catalog portion", directive)
        self.assertNotIn("Do NOT call wiki_scout_search", directive)

    def test_server_context_is_placed_adjacent_to_user_request(self) -> None:
        message = "[[EMPIRE_COMPANION]]\n\nlong preamble\n\nUser message:\nwhat tools exist?"
        out = serve._attach_server_context(
            message,
            "[AUTHORITATIVE LOCAL CATALOG CONTEXT]\nrows",
        )
        self.assertLess(
            out.index("[AUTHORITATIVE LOCAL CATALOG CONTEXT]"),
            out.index("what tools exist?"),
        )
        self.assertTrue(out.rstrip().endswith("what tools exist?"))
        self.assertEqual(out.count("User message:"), 1)

    def test_server_context_falls_back_without_user_message_anchor(self) -> None:
        out = serve._attach_server_context(
            "plain ask",
            "[AUTHORITATIVE LOCAL CATALOG CONTEXT]\nrows",
        )
        self.assertIn("[USER REQUEST]\nplain ask", out)

    def test_server_context_noop_when_context_empty(self) -> None:
        self.assertEqual(serve._attach_server_context("plain ask", ""), "plain ask")


if __name__ == "__main__":
    unittest.main()