from __future__ import annotations

import unittest
from unittest.mock import patch

from frontend import wiki_drift_api


class WikiDriftApiTests(unittest.TestCase):
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

    def test_plain_chat_not_wiki(self) -> None:
        text = "hows it going?"
        self.assertFalse(wiki_drift_api.is_wiki_lookup_query(text))
        self.assertFalse(wiki_drift_api.is_truth_drift_query(text))

    def test_enrich_access_does_not_default_post_truth(self) -> None:
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            payload = wiki_drift_api.enrich_eve_message_payload(
                {"message": "Can you access my Wikipedia data?"}
            )
        msg = str(payload.get("message") or "")
        self.assertIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, msg)
        self.assertNotIn("post-truth", msg.casefold())

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
            "Music of Stranger Things",
        )

    def test_stranger_things_song_question_resolves_topic(self) -> None:
        from pipeline.wiki_interpreter import resolve_lookup_topic

        q = "what song in 1980s song got popular in the series stranger things?"
        self.assertEqual(resolve_lookup_topic(q), "Music of Stranger Things")
        self.assertEqual(wiki_drift_api.extract_search_query(q), "Music of Stranger Things")

    def test_conversational_song_question_extracts_artist(self) -> None:
        from pipeline.wiki_interpreter import (
            clean_query_for_retrieval,
            extract_wiki_subject,
        )

        q = "what song from Kate Bush reinvigorated her career in 2025-2026"
        self.assertEqual(extract_wiki_subject(q), "Kate Bush")
        self.assertEqual(clean_query_for_retrieval(q), "Kate Bush")

    def test_revival_song_injection_uses_lead_evidence(self) -> None:
        lookup = {
            "ok": True,
            "snapshot_year": "2026",
            "cards": [{"title": "Running Up That Hill", "snippet": "Kate Bush song."}],
            "hit_meta": [
                {
                    "title": "Running Up That Hill",
                    "corpus_rel_path": "batch/y.md",
                }
            ],
        }
        lead = {
            "ok": True,
            "title": "Running Up That Hill",
            "snapshot": "2026",
            "lead": (
                'Kate Bush\'s "Running Up That Hill" surged after Stranger Things season 4.'
            ),
            "allowed_names": ["Running Up That Hill", "Kate Bush"],
        }
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch.object(wiki_drift_api, "run_lookup", return_value=lookup):
                with patch.object(
                    wiki_drift_api, "_build_lead_evidence", return_value=lead
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

    def test_enrich_artist_runs_lookup_not_compare(self) -> None:
        fake = {
            "ok": True,
            "snapshot_year": "2017",
            "usable": True,
            "cards": [
                {
                    "title": "Kate Bush",
                    "kind_hint": "article",
                    "snippet": "English singer-songwriter.",
                }
            ],
        }
        with patch.object(wiki_drift_api, "load_active_tools", return_value=["wiki_local"]):
            with patch.object(wiki_drift_api, "run_lookup", return_value=fake) as lookup:
                payload = wiki_drift_api.enrich_eve_message_payload(
                    {"message": "Who is Kate Bush?"}
                )
        lookup.assert_called_once_with(
            "Kate Bush",
            year=None,
            user_question="Who is Kate Bush?",
        )
        msg = str(payload.get("message") or "")
        self.assertIn(wiki_drift_api.WIKI_LOOKUP_MARKER, msg)
        self.assertIn("Kate Bush", msg)
        self.assertNotIn(wiki_drift_api.WIKI_DRIFT_MARKER, msg)


if __name__ == "__main__":
    unittest.main()
