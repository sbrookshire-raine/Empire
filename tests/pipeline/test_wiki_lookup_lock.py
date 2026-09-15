"""Tests for the cross-process wiki lookup lock."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import wiki_lookup_lock


class WikiLookupLockTests(unittest.TestCase):
    def test_set_active_clear(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            lock = Path(tmp) / "lock.json"
            with patch.dict(
                "os.environ",
                {"EMPIRE_WIKI_LOOKUP_LOCK": str(lock), "EMPIRE_WIKI_LOOKUP_LOCK_TTL": "60"},
                clear=False,
            ):
                wiki_lookup_lock.clear_wiki_lookup_lock()
                self.assertFalse(wiki_lookup_lock.wiki_lookup_lock_active())
                wiki_lookup_lock.set_wiki_lookup_lock(reason="lookup_injected", session_id="s1")
                self.assertTrue(wiki_lookup_lock.wiki_lookup_lock_active())
                data = wiki_lookup_lock.read_wiki_lookup_lock()
                assert data is not None
                self.assertEqual(data.get("reason"), "lookup_injected")
                wiki_lookup_lock.clear_wiki_lookup_lock()
                self.assertFalse(wiki_lookup_lock.wiki_lookup_lock_active())

    def test_expired_lock_clears(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            lock = Path(tmp) / "lock.json"
            with patch.dict(
                "os.environ",
                {"EMPIRE_WIKI_LOOKUP_LOCK": str(lock), "EMPIRE_WIKI_LOOKUP_LOCK_TTL": "60"},
                clear=False,
            ):
                wiki_lookup_lock.set_wiki_lookup_lock(ttl_sec=60)
                # Force expiry in the file
                import json
                import time

                payload = json.loads(lock.read_text(encoding="utf-8"))
                payload["expires_at"] = time.time() - 1
                lock.write_text(json.dumps(payload), encoding="utf-8")
                self.assertFalse(wiki_lookup_lock.wiki_lookup_lock_active())


if __name__ == "__main__":
    unittest.main()
