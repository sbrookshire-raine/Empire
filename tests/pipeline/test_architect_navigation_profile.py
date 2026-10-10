"""Tests for architect navigation profile sentence tagging."""

from __future__ import annotations

import unittest

from pipeline import architect_navigation_profile as nav


class TestArchitectNavigationProfile(unittest.TestCase):
    def test_classify_frustration(self) -> None:
        cat = nav.classify_sentence(
            "I ended up in error hell for three hours trying to troubleshoot Docker."
        )
        self.assertIn(cat, {"frustrations", "issues"})

    def test_classify_style(self) -> None:
        cat = nav.classify_sentence(
            "I need you to explain this in basic terms without technical jargon."
        )
        self.assertEqual(cat, "response_style")

    def test_classify_like(self) -> None:
        cat = nav.classify_sentence(
            "It was a step in the right direction and I felt it should count as a win."
        )
        self.assertEqual(cat, "likes")


if __name__ == "__main__":
    unittest.main()
