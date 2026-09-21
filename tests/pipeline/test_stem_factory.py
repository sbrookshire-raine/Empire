"""Tests for the bounded local Stem Factory wrapper."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import stem_factory


class StemFactoryTests(unittest.TestCase):
    def test_list_inbox_reports_only_audio_in_approved_inbox(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            inbox = Path(temp_dir) / "input"
            outbox = Path(temp_dir) / "output"
            inbox.mkdir(parents=True)
            (inbox / "song.mp3").write_bytes(b"audio")
            (inbox / "notes.txt").write_text("not audio", encoding="utf-8")

            with mock.patch.object(stem_factory, "DEFAULT_INBOX", inbox), mock.patch.object(
                stem_factory, "DEFAULT_OUTBOX", outbox
            ), mock.patch.object(stem_factory, "ALLOWED_ROOTS", [inbox, outbox]):
                result = stem_factory.list_inbox()

        self.assertTrue(result["ok"])
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["files"][0]["name"], "song.mp3")

    def test_run_rejects_path_outside_approved_roots(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            approved_inbox = root / "approved-input"
            approved_outbox = root / "approved-output"
            unapproved = root / "unapproved"
            approved_inbox.mkdir()
            approved_outbox.mkdir()
            unapproved.mkdir()

            with mock.patch.object(stem_factory, "DEFAULT_INBOX", approved_inbox), mock.patch.object(
                stem_factory, "DEFAULT_OUTBOX", approved_outbox
            ), mock.patch.object(stem_factory, "ALLOWED_ROOTS", [approved_inbox, approved_outbox]):
                result = stem_factory.run_stems(input_dir=str(unapproved))

        self.assertFalse(result["ok"])
        self.assertIn("approved roots", result["error"])


if __name__ == "__main__":
    unittest.main()