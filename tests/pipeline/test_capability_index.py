"""Capability route index — keyword search over tools, limbs, and playbook areas."""

from __future__ import annotations

import unittest

from pipeline import capability_index


class CapabilityIndexTests(unittest.TestCase):
    def test_route_wikipedia_hits_wiki_tools(self) -> None:
        result = capability_index.route("wikipedia cast list", limit=5)
        self.assertTrue(result["ok"])
        ids = {row["id"] for row in result["results"]}
        self.assertTrue(
            ids & {"wiki_scout_search", "wiki_local", "wiki-archive"},
            f"expected wiki hits, got {ids}",
        )

    def test_route_reverse_engineering_hits_rea(self) -> None:
        result = capability_index.route("reverse engineer electron app", limit=5)
        self.assertTrue(result["ok"])
        ids = {row["id"] for row in result["results"]}
        self.assertTrue(
            ids & {"rea", "rea_doctor", "reverse-engineering"},
            f"expected REA hits, got {ids}",
        )

    def test_route_empty_query_fails_closed(self) -> None:
        result = capability_index.route("")
        self.assertFalse(result["ok"])

    def test_results_include_protocol(self) -> None:
        result = capability_index.route("create task", limit=3)
        self.assertTrue(result["ok"])
        self.assertIn("protocol", result)
        self.assertGreaterEqual(len(result["results"]), 1)


if __name__ == "__main__":
    unittest.main()
