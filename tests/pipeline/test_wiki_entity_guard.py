from __future__ import annotations

import unittest
from unittest.mock import patch

from pipeline.wiki_entity_guard import gliner_grounding_enabled, verify_entities


class WikiEntityGuardTests(unittest.TestCase):
    def test_disabled_by_default(self) -> None:
        with patch.dict("os.environ", {"EMPIRE_GLINER_GROUNDING": "0"}, clear=False):
            ok, unsupported = verify_entities(
                'Kate Bush wrote "Wow".',
                {"ok": True, "lead": 'Kate Bush "Running Up That Hill"', "title": "Running Up That Hill"},
            )
        self.assertTrue(ok)
        self.assertEqual(unsupported, [])

    def test_enabled_without_model_skips(self) -> None:
        with patch.dict("os.environ", {"EMPIRE_GLINER_GROUNDING": "1"}, clear=False):
            with patch("pipeline.wiki_entity_guard._load_model", return_value=None):
                ok, unsupported = verify_entities("test", {"ok": True, "lead": "lead"})
        self.assertTrue(ok)
        self.assertEqual(unsupported, [])

    def test_gliner_flag_parser(self) -> None:
        with patch.dict("os.environ", {"EMPIRE_GLINER_GROUNDING": "1"}, clear=False):
            self.assertTrue(gliner_grounding_enabled())


if __name__ == "__main__":
    unittest.main()
