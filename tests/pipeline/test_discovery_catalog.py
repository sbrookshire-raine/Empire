from __future__ import annotations

import unittest

from pipeline import discovery_catalog


class DiscoveryCatalogTests(unittest.TestCase):
    def test_search_finds_minimax_tool(self) -> None:
        result = discovery_catalog.search_catalog("minimax")
        self.assertTrue(result["ok"])
        ids = {row["id"] for row in result["results"]}
        self.assertIn("local/scenario-regret", ids)

    def test_search_is_bounded(self) -> None:
        result = discovery_catalog.search_catalog("tool", limit=1000)
        self.assertLessEqual(len(result["results"]), 20)


if __name__ == "__main__":
    unittest.main()
