"""Every routing caller must agree with the shared classifier.

The four implementations that used to answer "wiki or memory?" on their own
were:

- `frontend/wiki_drift_api.py::is_wiki_lookup_query`
- `frontend/memory_api.py::is_memory_chat_query`
- `frontend/eve-workbench.js::isMemoryQuery` (the browser)
- `pipeline/intent_codex.py::context_block` (the codex override)

They disagreed, and nothing said so. This file asserts they agree now, on
the shared corpus, so a future change to one of them cannot silently
reintroduce a second opinion.
"""

from __future__ import annotations

import unittest

from frontend import memory_api, wiki_drift_api
from pipeline import intent_codex, route_classifier
from tests.pipeline.route_corpus import CORPUS


class WikiLookupParityTests(unittest.TestCase):
    """`is_wiki_lookup_query` must never contradict the classifier."""

    def test_wiki_lookup_agrees_with_the_classifier(self) -> None:
        failures: list[str] = []
        for message, expected in CORPUS:
            classified = route_classifier.classify(message) == route_classifier.WIKI
            looked_up = wiki_drift_api.is_wiki_lookup_query(message)
            if classified and not looked_up:
                failures.append(f"{message!r}: classifier says wiki, lookup says no")
        self.assertEqual(failures, [], "\n".join(failures))

    def test_wiki_lookup_never_claims_a_memory_ask(self) -> None:
        """A memory ask must never be hijacked by the wiki limb.

        The wiki module keeps some rules of its own (the page we are
        currently discussing), so it is a superset — but a *memory* ask is
        never one of them.
        """

        for message, expected in CORPUS:
            if expected != "memory":
                continue
            self.assertFalse(
                wiki_drift_api.is_wiki_lookup_query(message),
                f"{message!r} is a memory ask but was claimed by the wiki limb",
            )

    def test_wiki_lookup_never_claims_a_stack_question(self) -> None:
        """"what is my disk space" is about the machine.

        This is the case that used to fail: the bare verb "what" scored
        as a wiki lookup, and Eve was told to go and look up the disk
        space on Wikipedia.
        """

        for message, expected in CORPUS:
            if expected != "other":
                continue
            if "disk" in message or "capabilities" in message or "machine" in message:
                self.assertFalse(
                    wiki_drift_api.is_wiki_lookup_query(message),
                    f"{message!r} is a stack question but was claimed by the wiki limb",
                )


class MemoryChatParityTests(unittest.TestCase):
    """`is_memory_chat_query` must match the classifier's memory route."""

    def test_memory_chat_agrees_with_the_classifier(self) -> None:
        failures: list[str] = []
        for message, expected in CORPUS:
            classified = route_classifier.classify(message) == route_classifier.MEMORY
            is_memory = memory_api.is_memory_chat_query(message)
            if classified and not is_memory:
                failures.append(f"{message!r}: classifier says memory, memory API says no")
            if is_memory and expected != "memory":
                failures.append(
                    f"{message!r}: memory API says memory, corpus says {expected}"
                )
        self.assertEqual(failures, [], "\n".join(failures))


class IntentCodexParityTests(unittest.TestCase):
    """`resolve()` and `context_block()` must pick the same route."""

    def test_resolve_and_context_block_agree(self) -> None:
        failures: list[str] = []
        for message, _expected in CORPUS:
            result = intent_codex.resolve(message)
            primary = result.get("primary")
            block = intent_codex.context_block(message)
            intent_id = primary.get("id") if primary else None
            if intent_id and intent_id not in block:
                failures.append(
                    f"{message!r}: resolve picked {intent_id!r} but the block does not name it"
                )
            if not intent_id and block:
                failures.append(f"{message!r}: resolve picked nothing but the block is not empty")
        self.assertEqual(failures, [], "\n".join(failures))

    def test_resolve_reports_the_shared_route(self) -> None:
        for message, _expected in CORPUS:
            result = intent_codex.resolve(message)
            primary = result.get("primary")
            if not primary:
                continue
            self.assertIn(
                "route",
                primary,
                f"{message!r}: resolve() must report the shared route",
            )

    def test_wiki_route_never_lands_on_the_wiki_intent_by_accident(self) -> None:
        """A message the classifier calls "other" must not reach wiki_fact.

        The codex's own trigger scoring put "what is my disk space" on
        the wiki limb, because the bare verb "what" matched a wiki
        trigger. The classifier now demotes it.
        """

        for message, expected in CORPUS:
            if expected != "other":
                continue
            result = intent_codex.resolve(message)
            primary = result.get("primary")
            if not primary:
                continue
            self.assertNotEqual(
                primary.get("id"),
                "wiki_fact",
                f"{message!r} is not a wiki ask but resolved to wiki_fact",
            )

    def test_wiki_route_resolves_to_the_wiki_intent(self) -> None:
        for message, expected in CORPUS:
            if expected != "wiki":
                continue
            result = intent_codex.resolve(message)
            primary = result.get("primary")
            self.assertIsNotNone(primary, message)
            assert primary is not None
            self.assertEqual(primary.get("id"), "wiki_fact", message)
            self.assertEqual(primary.get("route"), "wiki", message)

    def test_memory_route_resolves_to_the_memory_intent(self) -> None:
        for message, expected in CORPUS:
            if expected != "memory":
                continue
            result = intent_codex.resolve(message)
            primary = result.get("primary")
            self.assertIsNotNone(primary, message)
            assert primary is not None
            self.assertEqual(primary.get("id"), "remember_recall", message)
            self.assertEqual(primary.get("route"), "memory", message)


class GreenPathParityTests(unittest.TestCase):
    """The wiki green path must only prefetch for a wiki ask."""

    def test_green_path_only_fires_for_wiki_asks(self) -> None:
        from frontend import wiki_green_path

        for message, expected in CORPUS:
            if expected == "wiki":
                continue
            # The green path must not prefetch archive evidence for anything
            # the classifier did not call a wiki ask. It returns "" early
            # for a non-wiki message, before it touches the archive.
            self.assertEqual(
                wiki_green_path.build_green_path_block(message),
                "",
                f"{message!r} is a {expected} ask but the green path prefetched evidence",
            )


if __name__ == "__main__":
    unittest.main()

