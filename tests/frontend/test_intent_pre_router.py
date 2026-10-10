from __future__ import annotations

import unittest

from pipeline import intent_codex


class IntentPreRouterTests(unittest.TestCase):
    def test_scrape_injects_intent_block(self) -> None:
        block = intent_codex.context_block("please scrape https://example.com")
        self.assertIn("AUTHORITATIVE INTENT ROUTE", block)

    def test_hello_has_no_intent_block(self) -> None:
        block = intent_codex.context_block("hello there")
        self.assertEqual(block, "")


if __name__ == "__main__":
    unittest.main()
