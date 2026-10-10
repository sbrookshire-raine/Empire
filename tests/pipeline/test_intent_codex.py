"""Intent codex — plain-language verb routing."""

from __future__ import annotations

import unittest

from pipeline import intent_codex


class IntentCodexTests(unittest.TestCase):
    def test_scrape_with_url(self) -> None:
        result = intent_codex.resolve("can you scrape https://example.com/foo and summarize")
        self.assertTrue(result["ok"])
        primary = result["primary"]
        self.assertIsNotNone(primary)
        assert primary is not None
        self.assertEqual(primary["id"], "scrape_gather_web")
        self.assertIn("web_scout", primary["online_tools"])

    def test_research_local_first(self) -> None:
        result = intent_codex.resolve("research the yt-dlp release notes")
        self.assertTrue(result["ok"])
        primary = result["primary"]
        assert primary is not None
        self.assertEqual(primary["id"], "research_deep")
        self.assertTrue(primary["local_first"])
        self.assertIn("cognee_recall", primary["local_tools"])

    def test_wiki_who_is(self) -> None:
        result = intent_codex.resolve("who is Kate Bush?")
        self.assertTrue(result["ok"])
        primary = result["primary"]
        assert primary is not None
        self.assertEqual(primary["id"], "wiki_fact")

    def test_context_block_when_confident(self) -> None:
        block = intent_codex.context_block("scrape this link https://a.test")
        self.assertIn("AUTHORITATIVE INTENT ROUTE", block)
        self.assertIn("scrape_gather_web", block)

    def test_context_block_empty_when_vague(self) -> None:
        block = intent_codex.context_block("hello")
        self.assertEqual(block, "")

    def test_architect_z_drive_backup(self) -> None:
        result = intent_codex.resolve("is anything processing to my z drive currently")
        self.assertTrue(result["ok"])
        primary = result["primary"]
        assert primary is not None
        self.assertEqual(primary["id"], "backup_estate_status")

    def test_language_barrier_intent(self) -> None:
        result = intent_codex.resolve("help the language barrier with how i talk")
        self.assertTrue(result["ok"])
        ids = {row["id"] for row in result["intents"]}
        self.assertTrue(
            ids & {"interpret_architect_voice", "remember_recall", "save_to_memory"},
            f"expected voice/memory intent, got {ids}",
        )

    def test_vault_archaeology_phrase(self) -> None:
        result = intent_codex.resolve("did we already build a version of this")
        self.assertTrue(result["ok"])
        ids = {row["id"] for row in result["intents"]}
        self.assertIn("remember_recall", ids)

    def test_close_the_loop_voice(self) -> None:
        result = intent_codex.resolve("close the loop on a small verified win")
        self.assertTrue(result["ok"])
        primary = result["primary"]
        assert primary is not None
        self.assertEqual(primary["id"], "interpret_architect_voice")


if __name__ == "__main__":
    unittest.main()
