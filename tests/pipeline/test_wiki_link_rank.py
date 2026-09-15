from __future__ import annotations

import unittest

from pipeline.wiki_link_rank import (
    rank_related_titles,
    select_hop_titles,
)


class WikiLinkRankTests(unittest.TestCase):
    def test_cheddar_outranks_alphabetical_noise(self) -> None:
        ranked = rank_related_titles(
            ["acid", "archeology", "black pepper", "Cheddar cheese", "Brie"],
            "tell me about cheddar in cheese",
            landing_title="Cheese",
        )
        self.assertEqual(ranked[0].casefold(), "cheddar cheese")

    def test_revival_song_beats_music_of_show_page(self) -> None:
        ranked = rank_related_titles(
            [
                "Music of Stranger Things",
                "Stranger Things season 4",
                "Running Up That Hill",
                "Kate Bush",
            ],
            "what popular 80s song got re-popularized during stranger things?",
            landing_title="Stranger Things",
        )
        self.assertEqual(ranked[0], "Running Up That Hill")
        ranked = rank_related_titles(
            [
                "1980s in music",
                "Wow (Kate Bush song)",
                "Acid",
                "Running Up That Hill",
                "Master of Puppets (song)",
            ],
            "what popular 80s song got re-popularized during stranger things?",
            landing_title="Stranger Things",
        )
        self.assertEqual(ranked[0], "Running Up That Hill")
        self.assertNotEqual(ranked[0], "Wow (Kate Bush song)")

    def test_kate_bush_revival_hops_to_ruth(self) -> None:
        ranked = rank_related_titles(
            [
                "AllMusic",
                "Babooshka (song)",
                "Wow (Kate Bush song)",
                "Music of Stranger Things",
                "Running Up That Hill",
                "Wuthering Heights (song)",
            ],
            "what song from Kate Bush reinvigorated her career in 2025-2026?",
            landing_title="Kate Bush",
        )
        hops = select_hop_titles(
            ranked,
            "what song from Kate Bush reinvigorated her career in 2025-2026?",
            landing_title="Kate Bush",
        )
        self.assertEqual(ranked[0], "Running Up That Hill")
        self.assertEqual(hops, ["Running Up That Hill"])

    def test_cast_prefers_actor_titles(self) -> None:
        ranked = rank_related_titles(
            ["1980s", "Cold War", "Caleb McLaughlin", "Anna Wood (actress)"],
            "What actors played in Stranger Things?",
            landing_title="Stranger Things",
        )
        top = {t.casefold() for t in ranked[:2]}
        self.assertIn("anna wood (actress)", top)
        hops = select_hop_titles(
            ranked,
            "What actors played in Stranger Things?",
            landing_title="Stranger Things",
            limit=2,
        )
        self.assertEqual(hops, ["Anna Wood (actress)", "Caleb McLaughlin"])

    def test_who_is_does_not_hop(self) -> None:
        ranked = rank_related_titles(
            ["Running Up That Hill", "Art pop"],
            "who is Kate Bush?",
            landing_title="Kate Bush",
        )
        hops = select_hop_titles(
            ranked,
            "who is Kate Bush?",
            landing_title="Kate Bush",
        )
        self.assertEqual(hops, [])

    def test_max_track_question_still_ranks_ruth(self) -> None:
        ranked = rank_related_titles(
            [
                "Music of Stranger Things",
                "Master of Puppets (song)",
                "Running Up That Hill",
            ],
            "what track did Max listen to in Stranger Things season 4",
            landing_title="Stranger Things",
        )
        self.assertEqual(ranked[0], "Running Up That Hill")


if __name__ == "__main__":
    unittest.main()
