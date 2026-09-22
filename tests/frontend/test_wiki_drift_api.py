from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import wiki_drift_api


class WikiDriftApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self._lock_tmp = tempfile.TemporaryDirectory()
        lock = Path(self._lock_tmp.name) / "lock.json"
        self._env = patch.dict(
            "os.environ",
            {"EMPIRE_WIKI_LOOKUP_LOCK": str(lock)},
            clear=False,
        )
        self._env.start()

    def tearDown(self) -> None:
        self._env.stop()
        self._lock_tmp.cleanup()

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
