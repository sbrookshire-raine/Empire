"""The shared route classifier — the one decision point for wiki / memory / task.

The corpus lives in `tests/pipeline/route_corpus.py` so the classifier's
own test and the caller-parity test read the *same* cases.
"""

from __future__ import annotations

import unittest

from pipeline import route_classifier
from tests.pipeline.route_corpus import CORPUS


class RouteClassifierTests(unittest.TestCase):
    def test_every_corpus_case_classifies_as_expected(self) -> None:
        failures: list[str] = []
        for message, expected in CORPUS:
            got = route_classifier.classify(message)
            if got != expected:
                detail = route_classifier.explain(message)
                failures.append(
                    f"{message!r}: expected {expected}, got {got} ({detail['reason']})"
                )
        self.assertEqual(failures, [], "\n".join(failures))

    def test_corpus_covers_all_four_routes(self) -> None:
        routes = {expected for _, expected in CORPUS}
        self.assertEqual(routes, set(route_classifier.ROUTES))

    def test_corpus_is_large_enough_to_mean_something(self) -> None:
        self.assertGreaterEqual(len(CORPUS), 40)

    def test_empty_message_is_other(self) -> None:
        self.assertEqual(route_classifier.classify(""), "other")
        self.assertEqual(route_classifier.classify("   "), "other")

    def test_helpers_agree_with_classify(self) -> None:
        for message, expected in CORPUS:
            self.assertEqual(
                route_classifier.is_wiki(message),
                expected == "wiki",
                message,
            )
            self.assertEqual(
                route_classifier.is_memory(message),
                expected == "memory",
                message,
            )
            self.assertEqual(
                route_classifier.is_task(message),
                expected == "task",
                message,
            )

    def test_explain_names_the_rule_that_fired(self) -> None:
        self.assertEqual(
            route_classifier.explain("Who is Kate Bush?")["reason"],
            "generic wiki verb + encyclopedic subject",
        )
        self.assertEqual(
            route_classifier.explain("what do you know about me")["reason"],
            "memory anchor + recall verb",
        )
        self.assertEqual(
            route_classifier.explain("list my tasks")["reason"],
            "task signal",
        )
        self.assertEqual(
            route_classifier.explain("hello")["reason"],
            "no route matched",
        )

    def test_explicit_wiki_signal_beats_a_memory_anchor(self) -> None:
        """The documented precedence: wiki signal first, memory anchor second.

        "look up the wikipedia article we discussed" is a wiki ask — the
        wiki verb names the archive, so the memory anchor does not steal it.
        """

        self.assertEqual(
            route_classifier.classify("look up the wikipedia article we discussed"),
            "wiki",
        )

    def test_memory_anchor_beats_a_generic_wiki_verb(self) -> None:
        """The other half of the precedence: memory wins over "what is"."""

        self.assertEqual(
            route_classifier.classify("what is my memory of the project"),
            "memory",
        )

    def test_wiki_followup_only_fires_with_the_context(self) -> None:
        """A follow-up is only a wiki ask when a page is actually in play.

        The context is the caller's to supply — the classifier cannot see
        the conversation.
        """

        self.assertEqual(route_classifier.classify("what else is on that page"), "other")
        self.assertEqual(
            route_classifier.classify("what else is on that page", wiki_followup=True),
            "wiki",
        )

    def test_classification_is_case_insensitive(self) -> None:
        for message, expected in CORPUS:
            self.assertEqual(
                route_classifier.classify(message.upper()),
                route_classifier.classify(message),
                f"{message!r} changed route when upper-cased",
            )

    def test_classification_ignores_surrounding_whitespace(self) -> None:
        for message, expected in CORPUS:
            self.assertEqual(
                route_classifier.classify(f"  {message}  "),
                expected,
                message,
            )


if __name__ == "__main__":
    unittest.main()
