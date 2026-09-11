from __future__ import annotations

import unittest

from pipeline.wiki_grounding_guard import apply_grounding_guard, verify_grounding


class WikiGroundingGuardTests(unittest.TestCase):
    def test_rejects_wow_for_kate_bush_revival(self) -> None:
        evidence = {
            "ok": True,
            "title": "Running Up That Hill",
            "lead": (
                'Kate Bush\'s "Running Up That Hill" surged after Stranger Things season 4.'
            ),
            "allowed_names": ["Running Up That Hill", "Kate Bush", "Stranger Things"],
        }
        bad = (
            'The song was "Wow," originally released on Lionheart in 1978.'
        )
        ok, fixed = verify_grounding(
            bad,
            evidence,
            user_question="what song from Kate Bush reinvigorated her career in 2025-2026?",
        )
        self.assertFalse(ok)
        self.assertIn("Running Up That Hill", fixed)

    def test_apply_guard_replaces_bad_reply(self) -> None:
        evidence = {
            "ok": True,
            "title": "Running Up That Hill",
            "lead": '"Running Up That Hill" by Kate Bush revived via Stranger Things.',
            "allowed_names": ["Running Up That Hill"],
            "user_question": "what song from Kate Bush reinvigorated her career?",
        }
        out = apply_grounding_guard(
            'Answer: "Wow."',
            evidence,
            user_question=evidence["user_question"],
        )
        self.assertIn("Running Up That Hill", out)
        self.assertNotIn("Wow", out)

    def test_rejects_bio_trivia_for_who_is(self) -> None:
        evidence = {
            "ok": True,
            "title": "Kate Bush",
            "lead": (
                "**Catherine Bush** (born 30 July 1958) is an English singer, "
                "songwriter, musician, dancer and record producer."
            ),
            "allowed_names": ["Kate Bush", "Catherine Bush"],
        }
        bad = (
            "Kate Bush was ranked at No. 60 in the list of 200 Best Singers of All Time "
            "by Rolling Stone. Fish People moved to state51."
        )
        ok, fixed = verify_grounding(bad, evidence, user_question="Who is Kate Bush?")
        self.assertFalse(ok)
        self.assertIn("1958", fixed)
        self.assertNotIn("Rolling Stone", fixed)


if __name__ == "__main__":
    unittest.main()
