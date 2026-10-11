from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import disassembly_card, intake_to_lego


class IntakeToLegoTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cards_patch = patch.object(disassembly_card, "cards_dir", return_value=self.root)
        self.cards_patch.start()

    def tearDown(self) -> None:
        self.cards_patch.stop()
        self.tmp.cleanup()

    def test_intake_web_writes_card(self) -> None:
        fake = {
            "ok": True,
            "title": "Example Docs",
            "text": "Body text for the page.",
            "final_url": "https://example.com/docs",
            "path": "C:/cache/web_example.md",
        }
        with patch.object(intake_to_lego.web_scout, "scout", return_value=fake):
            out = intake_to_lego.intake_web("https://example.com/docs")
        self.assertTrue(out.get("ok"))
        self.assertTrue(str(out.get("card_id") or "").startswith("dc_"))

    def test_normalize_repo_from_url(self) -> None:
        self.assertEqual(
            intake_to_lego._normalize_repo("https://github.com/acme/foo"),
            "acme/foo",
        )


if __name__ == "__main__":
    unittest.main()
