"""Unit tests for Wiki Interpreter query/subject extraction."""

from __future__ import annotations

import unittest

from pipeline.wiki_interpreter import clean_query_for_retrieval, extract_wiki_subject


class WikiSubjectTests(unittest.TestCase):
    def test_how_does_subject_work_yields_the_subject(self) -> None:
        """Measured live 2026-09-23: this shape missed the wiki entirely before the fix, which is
        what sent the 14B into a repeated-search loop on a "no page" answer."""

        self.assertEqual(extract_wiki_subject("How does magnetism work?"), "magnetism")
        self.assertEqual(extract_wiki_subject("How do magnets work?"), "magnets")
        self.assertEqual(extract_wiki_subject("how magnets work"), "magnets")
        self.assertEqual(extract_wiki_subject("how does the stock market work?"), "stock market")
        self.assertEqual(extract_wiki_subject("how do solar panels function?"), "solar panels")

    def test_how_question_with_pronoun_is_not_a_lookup(self) -> None:
        """A how-to question about the user's own task must not become an article title."""

        for query in (
            "how do I install python?",
            "how do you make sourdough",
            "How much does a Tesla cost?",
            "how can we ship this today?",
        ):
            self.assertEqual(extract_wiki_subject(query), "", msg=query)

    def test_what_is_still_works(self) -> None:
        self.assertEqual(extract_wiki_subject("What is magnetism?"), "magnetism")

    def test_clean_query_uses_the_same_subject(self) -> None:
        self.assertEqual(clean_query_for_retrieval("How does magnetism work?"), "magnetism")
        self.assertEqual(clean_query_for_retrieval("What is magnetism?"), "magnetism")


if __name__ == "__main__":
    unittest.main()