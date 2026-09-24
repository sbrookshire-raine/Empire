from __future__ import annotations

import functools
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import wiki_drift_api


def legacy_middleware_test(fn):
    """Run the test with the legacy regex injection path enabled (escape hatch).

    Default behaviour as of the 2026-09-23 migration: Wikipedia retrieval is an
    autonomous MCP tool process and `enrich_eve_message_payload` is a passthrough.
    These tests pin the escape hatch (EMPIRE_WIKI_MIDDLEWARE=1) so the legacy path
    stays working if it is ever needed.
    """

    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        with patch.dict(
            "os.environ", {wiki_drift_api.WIKI_MIDDLEWARE_ENV: "1"}, clear=False
        ):
            return fn(self, *args, **kwargs)

    return wrapper


class WikiDriftApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self._lock_tmp = tempfile.TemporaryDirectory()
        lock = Path(self._lock_tmp.name) / "lock.json"
        self._env = patch.dict(
            "os.environ",
            {
                "EMPIRE_WIKI_LOOKUP_LOCK": str(lock),
                # Default mode: the legacy regex middleware is OFF (autonomous MCP
                # tools own Wikipedia retrieval). Legacy tests opt in via
                # @legacy_middleware_test.
                wiki_drift_api.WIKI_MIDDLEWARE_ENV: "",
            },
            clear=False,
        )
        self._env.start()
        # Reset single-user conversational state between tests.
        wiki_drift_api.clear_resolved_wiki_title()
        wiki_drift_api.clear_dns_ambiguous()

    def tearDown(self) -> None:
        self._env.stop()
        self._lock_tmp.cleanup()

    def test_middleware_disabled_by_default(self) -> None:
        """2026-09-23 migration: Eve owns Wikipedia retrieval, so the legacy regex
        injection path must be OFF unless the escape hatch is explicitly enabled."""
        previous = os.environ.pop(wiki_drift_api.WIKI_MIDDLEWARE_ENV, None)
        if previous is not None:
            self.addCleanup(
                os.environ.__setitem__, wiki_drift_api.WIKI_MIDDLEWARE_ENV, previous
            )
        self.assertIsNone(os.environ.get(wiki_drift_api.WIKI_MIDDLEWARE_ENV))
        self.assertFalse(wiki_drift_api.wiki_middleware_enabled())

    def test_middleware_env_truth_table(self) -> None:
        for raw in ("1", "true", "TRUE", "Yes", "on"):
            with patch.dict(
                "os.environ", {wiki_drift_api.WIKI_MIDDLEWARE_ENV: raw}, clear=False
            ):
                self.assertTrue(wiki_drift_api.wiki_middleware_enabled(), raw)
        for raw in ("", "0", "false", "off", "no", "maybe"):
            with patch.dict(
                "os.environ", {wiki_drift_api.WIKI_MIDDLEWARE_ENV: raw}, clear=False
            ):
                self.assertFalse(wiki_drift_api.wiki_middleware_enabled(), raw)

    def test_enrich_is_passthrough_when_middleware_off(self) -> None:
        """Default mode: no marker and no `_wiki_evidence` — Eve resolves the subject
        and pronouns herself, then calls the empire-wiki-scout MCP tools."""
        text = "What actors played in Stranger Things?"
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            payload = wiki_drift_api.enrich_eve_message_payload({"message": text}, force=True)
        self.assertEqual(payload.get("message"), text)
        self.assertNotIn("_wiki_evidence", payload)
        self.assertNotIn(wiki_drift_api.WIKI_LOOKUP_MARKER, str(payload.get("message")))
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, str(payload.get("message")))

    def test_enrich_anaphoric_followup_no_injection_by_default(self) -> None:
        """A remembered page must not trigger server-side anaphora resolution any more."""
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes", "2026")
        text = "what else is on that page"
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch.object(wiki_drift_api, "_lookup_from_title_dns") as lookup:
                payload = wiki_drift_api.enrich_eve_message_payload(
                    {"message": text, "sessionId": "s"}, force=True
                )
        lookup.assert_not_called()
        self.assertEqual(payload.get("message"), text)

    def test_enrich_writes_no_lookup_lock_when_middleware_off(self) -> None:
        """The cross-process lookup lock hides wiki tools from Eve; default mode must
        never set it, or the autonomous tools would be suppressed."""
        from pipeline.wiki_lookup_lock import wiki_lookup_lock_active

        self.assertFalse(wiki_lookup_lock_active())
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            wiki_drift_api.enrich_eve_message_payload(
                {"message": "Who is Kate Bush?", "sessionId": "s"}, force=True
            )
        self.assertFalse(wiki_lookup_lock_active())

    def test_access_question_is_lookup_not_drift(self) -> None:
        text = "Can you access my Wikipedia data?"
        self.assertFalse(wiki_drift_api.is_truth_drift_query(text))
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertEqual(wiki_drift_api.extract_search_query(text), "")

    def test_artist_question_is_lookup(self) -> None:
        text = "Who is Kate Bush?"
        self.assertFalse(wiki_drift_api.is_truth_drift_query(text))
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertEqual(wiki_drift_api.extract_search_query(text), "Kate Bush")

    def test_album_question_extracts_artist(self) -> None:
        text = "What albums did Kate Bush release?"
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertEqual(wiki_drift_api.extract_search_query(text), "Kate Bush")

    def test_band_called_phrase_extracts_proper_entity(self) -> None:
        self.assertEqual(
            wiki_drift_api.extract_search_query("name the albums from the band called The White Stripes"),
            "White Stripes",
        )

    def test_quoted_band_phrase_extracts_proper_entity(self) -> None:
        self.assertEqual(
            wiki_drift_api.extract_search_query("name the albums released by the band 'the white stripes'"),
            "white stripes",
        )

    def test_album_names_of_band_triggers_lookup(self) -> None:
        """2026-09-23: this phrasing got no injection at all, so Eve refused."""
        text = "tell me the names of the band 'the white stripes' albums"
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertEqual(wiki_drift_api.extract_search_query(text), "white stripes")

    def test_anaphoric_that_page_is_not_a_title(self) -> None:
        """Regression: "not on that page" extracted the pronoun "that" and Title DNS
        resolved the grammar article "That", which was injected as mandatory evidence
        so Eve answered from the wrong page entirely."""
        text = (
            "and are you saying the album names are not on that page, "
            "because that's what i asked you to find for me"
        )
        self.assertEqual(wiki_drift_api.extract_search_query(text), "")
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            payload = wiki_drift_api.enrich_eve_message_payload({"message": text}, force=True)
        msg = str(payload.get("message") or "")
        self.assertNotIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertEqual(msg, text)

    def test_anaphoric_pronouns_rejected_as_topics(self) -> None:
        for candidate in ("that", "this", "it", "the page", "that page", "same page"):
            self.assertTrue(
                wiki_drift_api._is_anaphoric_topic(candidate),
                f"{candidate!r} must not be treated as a page title",
            )
        for candidate in ("Kate Bush", "The White Stripes", "V", "Dune: Part Two"):
            self.assertFalse(
                wiki_drift_api._is_anaphoric_topic(candidate),
                f"{candidate!r} is a legitimate title",
            )

    def test_find_for_me_does_not_fire_lookup_gate(self) -> None:
        self.assertFalse(
            wiki_drift_api.is_wiki_lookup_query("what did you find for me earlier?")
        )
        self.assertTrue(
            wiki_drift_api.is_wiki_lookup_query("find the Wikipedia page for Kate Bush")
        )

    def test_remember_get_and_clear_resolved_title(self) -> None:
        self.assertEqual(wiki_drift_api.get_resolved_wiki_title(), "")
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes", "2026", "q")
        self.assertEqual(wiki_drift_api.get_resolved_wiki_title(), "The White Stripes")
        wiki_drift_api.clear_resolved_wiki_title()
        self.assertEqual(wiki_drift_api.get_resolved_wiki_title(), "")

    def test_anaphoric_followup_detection(self) -> None:
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes")
        for q in (
            "what else is on that page",
            "tell me more about it",
            "what about their discography",
            "who else is in it",
            "what about them",
        ):
            self.assertTrue(
                wiki_drift_api.is_anaphoric_followup(q),
                f"{q!r} should be an anaphoric follow-up",
            )
        self.assertFalse(wiki_drift_api.is_anaphoric_followup("who is Kate Bush"))

    def test_anaphoric_followup_requires_resolved_title(self) -> None:
        # No remembered title -> the anaphoric gate must stay silent.
        self.assertFalse(wiki_drift_api.is_anaphoric_followup("what else is on that page"))
        self.assertFalse(wiki_drift_api.is_wiki_lookup_query("what else is on that page"))

    def test_anaphoric_subject_is_empty(self) -> None:
        """The follow-up has no explicit subject; extraction must yield '' so the
        remembered title can be substituted downstream."""
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes")
        self.assertEqual(wiki_drift_api.extract_search_query("what else is on that page"), "")

    def test_anaphoric_gate_fires_with_title(self) -> None:
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes")
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query("what else is on that page"))

    @legacy_middleware_test
    def test_enrich_anaphoric_followup_reuses_last_title(self) -> None:
        """End-to-end: a follow-up 'that page' re-targets the previously resolved page."""
        wiki_drift_api.remember_resolved_wiki_title("The White Stripes", "2026")
        captured: dict = {}

        def fake_lookup(query, *, year, user_question, include_hops=True):
            captured["query"] = query
            captured["year"] = year
            captured["include_hops"] = include_hops
            return f"{wiki_drift_api.WIKI_LOOKUP_MARKER}\nTitle: {query}", None

        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch.object(wiki_drift_api, "_lookup_from_title_dns", side_effect=fake_lookup):
                payload = wiki_drift_api.enrich_eve_message_payload(
                    {"message": "what else is on that page", "sessionId": "s"}, force=True
                )
        self.assertEqual(captured.get("query"), "The White Stripes")
        self.assertEqual(captured.get("year"), "2026")
        self.assertFalse(captured.get("include_hops", True))
        self.assertIn("Title: The White Stripes", str(payload.get("message") or ""))

    @legacy_middleware_test
    def test_error_book_hint_suppressed_when_evidence_present(self) -> None:
        """A subject that missed yesterday must not be told 'not in archive' once it
        now resolves. The persistent Error Book hint is suppressed when this turn
        produced real evidence (regression: contradictory guidance made Eve refuse
        a page it just retrieved)."""
        from pipeline.wiki_scratchpad import error_book_append

        q = "tell me about white stripes"
        with tempfile.TemporaryDirectory() as td:
            book = Path(td) / "err.jsonl"
            with patch.dict("os.environ", {"EMPIRE_WIKI_ERROR_BOOK": str(book)}, clear=False):
                error_book_append(query=q, reason="not in title registry", title="white stripes")

                def fake_lookup(query, *, year, user_question, include_hops=True):
                    return (
                        f"{wiki_drift_api.WIKI_LOOKUP_MARKER}\nTitle: The White Stripes",
                        {"ok": True, "title": "The White Stripes"},
                    )

                with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
                    with patch.object(
                        wiki_drift_api, "_lookup_from_title_dns", side_effect=fake_lookup
                    ):
                        payload = wiki_drift_api.enrich_eve_message_payload(
                            {"message": q, "sessionId": "s"}, force=True
                        )
        msg = str(payload.get("message") or "")
        self.assertNotIn("[[EMPIRE_WIKI_ERROR_BOOK]]", msg)
        self.assertIn("[[EMPIRE_WIKI_LOOKUP]]", msg)
        self.assertIn("The White Stripes", msg)

    def test_band_tail_with_lead_singer_context_extracts_entity(self) -> None:
        self.assertEqual(
            wiki_drift_api.extract_search_query("who was a lead singer for the band Type O-Megative"),
            "Type O-Megative",
        )

    def test_explicit_wikipedia_target_wins_in_multi_part_prompt(self) -> None:
        text = (
            "Query the catalog for 'decision making'. Then, look up the Wikipedia "
            "article for 'Agent-based model'. Summarize the lead."
        )
        self.assertEqual(wiki_drift_api.extract_search_query(text), "Agent-based model")

    def test_explicit_drift_still_triggers_compare(self) -> None:
        text = "Compare post-truth across 2017, 2021, and 2026"
        self.assertTrue(wiki_drift_api.is_truth_drift_query(text))
        self.assertEqual(wiki_drift_api.pick_compare_topic(text), "post-truth")

    def test_ai_change_picks_artificial_intelligence(self) -> None:
        text = "How did AI change between 2017 and 2026?"
        self.assertTrue(wiki_drift_api.is_truth_drift_query(text))
        self.assertEqual(
            wiki_drift_api.pick_compare_topic(text),
            "artificial intelligence",
        )

    def test_how_has_ai_changed_phrasing(self) -> None:
        text = "how has artificial intelligence changed from 2017 to 2026"
        self.assertTrue(wiki_drift_api.is_truth_drift_query(text))
        self.assertEqual(
            wiki_drift_api.pick_compare_topic(text),
            "artificial intelligence",
        )

    def test_what_changed_about_ai(self) -> None:
        text = "what changed about AI across 2017 and 2026"
        self.assertEqual(
            wiki_drift_api.pick_compare_topic(text),
            "artificial intelligence",
        )

    def test_compare_artificial_intelligence_phrasing(self) -> None:
        text = "Compare artificial intelligence 2017 vs 2026"
        self.assertEqual(
            wiki_drift_api.pick_compare_topic(text),
            "artificial intelligence",
        )

    def test_actors_tv_show_is_lookup(self) -> None:
        text = "What actors played in the TV show 'The Following'?"
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertEqual(wiki_drift_api.extract_search_query(text), "The Following")

    def test_titles_match_rejects_cult_following(self) -> None:
        self.assertFalse(
            wiki_drift_api._titles_match_topic(
                ["Cult following", "Following", "Trend following"],
                "The Following",
                user_question="What actors played in the TV show 'The Following'?",
            )
        )
        self.assertTrue(
            wiki_drift_api._titles_match_topic(
                ["Stranger Things", "Music of Stranger Things"],
                "Stranger Things",
                user_question="What actors played in Stranger Things?",
            )
        )

    def test_plain_chat_not_wiki(self) -> None:
        text = "hows it going?"
        self.assertFalse(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertFalse(wiki_drift_api.is_truth_drift_query(text))

    def test_bare_tell_me_does_not_hijack_local_tool_request(self) -> None:
        text = (
            "Check the health of the Workbench using your local tools, "
            "then tell me how much free disk space is available."
        )
        self.assertFalse(wiki_drift_api.is_wiki_lookup_query(text))

    def test_tell_me_about_encyclopedia_object_still_lookup(self) -> None:
        self.assertTrue(
            wiki_drift_api.is_wiki_lookup_query("can you tell me about black holes please?")
        )
        self.assertTrue(
            wiki_drift_api.is_wiki_lookup_query("tell me about a sci-fi series in the 80s called 'V'")
        )

    def test_capability_headroom_question_not_wiki(self) -> None:
        text = (
            "What capabilities do you have right now, and what's free on the machine? "
            "Summarize briefly"
        )
        self.assertTrue(wiki_drift_api.is_resource_pulse_query(text))
        self.assertFalse(wiki_drift_api.is_wiki_lookup_query(text))
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            payload = wiki_drift_api.enrich_eve_message_payload({"message": text})
        msg = str(payload.get("message") or "")
        self.assertNotIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertEqual(msg, text)

    def test_summarize_about_topic_still_wiki(self) -> None:
        text = "summarize about Kate Bush albums"
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(text))

    @legacy_middleware_test
    def test_enrich_access_does_not_default_post_truth(self) -> None:
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            payload = wiki_drift_api.enrich_eve_message_payload(
                {"message": "Can you access my Wikipedia data?"}
            )
        msg = str(payload.get("message") or "")
        self.assertIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, msg)
        self.assertNotIn("post-truth", msg.casefold())

    def test_quoted_single_letter_title(self) -> None:
        q = "what actors played in the original 1983/1984 series called 'V'?"
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(q))
        self.assertEqual(wiki_drift_api.extract_search_query(q), "V")
        q2 = "tell me about a sci-fi series in the 80s called 'V'"
        self.assertEqual(wiki_drift_api.extract_search_query(q2), "V")

    def test_im_interested_does_not_eat_contraction(self) -> None:
        q = "I'm interested in the 1984 TV series 'V'."
        self.assertEqual(wiki_drift_api.extract_search_query(q), "V")
        self.assertNotIn("interested", wiki_drift_api.extract_search_query(q).casefold())

    def test_disambiguation_followup_picks_1984(self) -> None:
        wiki_drift_api.remember_dns_ambiguous(
            "V",
            "2026",
            ["V (1984 TV series)", "V (1983 miniseries)"],
        )
        self.assertEqual(
            wiki_drift_api.pick_disambiguation_followup(
                "I'm interested in the 1984 TV series 'V'."
            ),
            "V (1984 TV series)",
        )
        self.assertEqual(
            wiki_drift_api.pick_disambiguation_followup("the miniseries?"),
            "V (1983 miniseries)",
        )
        wiki_drift_api.clear_dns_ambiguous()

    def test_parse_year_from_message(self) -> None:
        from pipeline.wiki_scout import parse_snapshot_year_from_text

        self.assertEqual(parse_snapshot_year_from_text("Who is Kate Bush in 2017?"), "2017")
        self.assertIsNone(parse_snapshot_year_from_text("Who is Kate Bush?"))

    def test_popular_80s_song_stranger_things_triggers_lookup(self) -> None:
        q = (
            "what popular 80s song got re-popularized during the later "
            "seasons of stranger things?"
        )
        self.assertTrue(wiki_drift_api.is_wiki_lookup_query(q))
        self.assertEqual(
            wiki_drift_api.extract_search_query(q),
            "Stranger Things",
        )

    def test_stranger_things_song_question_resolves_topic(self) -> None:
        from pipeline.wiki_interpreter import resolve_lookup_topic

        q = "what song in 1980s song got popular in the series stranger things?"
        self.assertEqual(resolve_lookup_topic(q), "Stranger Things")
        self.assertEqual(wiki_drift_api.extract_search_query(q), "Stranger Things")

    def test_conversational_song_question_extracts_artist(self) -> None:
        from pipeline.wiki_interpreter import (
            clean_query_for_retrieval,
            extract_wiki_subject,
        )

        q = "what song from Kate Bush reinvigorated her career in 2025-2026"
        self.assertEqual(extract_wiki_subject(q), "Kate Bush")
        self.assertEqual(clean_query_for_retrieval(q), "Kate Bush")

    @legacy_middleware_test
    def test_revival_song_injection_uses_lead_evidence(self) -> None:
        from pipeline.wiki_title_dns import DnsHit, DnsResult

        lead = {
            "ok": True,
            "title": "Running Up That Hill",
            "snapshot": "2026",
            "lead": (
                'Kate Bush\'s "Running Up That Hill" surged after Stranger Things season 4.'
            ),
            "allowed_names": ["Running Up That Hill", "Kate Bush"],
        }
        dns = DnsResult(
            status="hit",
            query="Kate Bush",
            year="2026",
            hit=DnsHit(
                title="Kate Bush",
                path=r"D:\wiki_md\2026\kb.md",
                rel_path="kb.md",
                page_id="kb",
                year="2026",
            ),
            reason="exact",
        )
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch(
                "pipeline.wiki_title_dns.resolve",
                return_value=dns,
            ):
                with patch(
                    "pipeline.wiki_read_lead.wiki_read_lead",
                    return_value=lead,
                ):
                    payload = wiki_drift_api.enrich_eve_message_payload(
                        {
                            "message": (
                                "what song from Kate Bush reinvigorated her career "
                                "in 2025-2026?"
                            )
                        }
                    )
        msg = str(payload.get("message") or "")
        self.assertIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertIn("EVIDENCE", msg)
        self.assertIn("running up that hill", msg.casefold())
        self.assertIn("_wiki_evidence", payload)

    @legacy_middleware_test
    def test_enrich_artist_uses_dns_not_compare(self) -> None:
        from pipeline.wiki_title_dns import DnsHit, DnsResult

        lead = {
            "ok": True,
            "title": "Kate Bush",
            "snapshot": "2026",
            "lead": "English singer-songwriter.",
            "allowed_names": ["Kate Bush"],
        }
        dns = DnsResult(
            status="hit",
            query="Kate Bush",
            year="2026",
            hit=DnsHit(
                title="Kate Bush",
                path=r"D:\wiki_md\2026\kb.md",
                rel_path="kb.md",
                page_id="kb",
                year="2026",
            ),
            reason="exact",
        )
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch(
                "pipeline.wiki_title_dns.resolve",
                return_value=dns,
            ) as resolve:
                with patch(
                    "pipeline.wiki_read_lead.wiki_read_lead",
                    return_value=lead,
                ):
                    with patch.object(wiki_drift_api, "run_lookup") as lookup:
                        payload = wiki_drift_api.enrich_eve_message_payload(
                            {"message": "Who is Kate Bush?"}
                        )
        resolve.assert_called()
        lookup.assert_not_called()
        msg = str(payload.get("message") or "")
        self.assertIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertIn("Kate Bush", msg)
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, msg)

    @legacy_middleware_test
    def test_following_cast_is_dns_miss(self) -> None:
        from pipeline.wiki_title_dns import DnsResult

        miss = DnsResult(
            status="miss",
            query="The Following",
            year="2026",
            reason="not in title registry",
        )
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch("pipeline.wiki_title_dns.resolve", return_value=miss):
                with patch.object(wiki_drift_api, "run_lookup") as lookup:
                    payload = wiki_drift_api.enrich_eve_message_payload(
                        {"message": "What actors played in the TV show 'The Following'?"}
                    )
        lookup.assert_not_called()
        msg = str(payload.get("message") or "").casefold()
        self.assertIn("did not return a usable page", msg)
        self.assertIn("the following", msg)
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, str(payload.get("message") or ""))


if __name__ == "__main__":
    unittest.main()
