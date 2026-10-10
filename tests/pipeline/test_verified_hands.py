from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import verified_hands


class VerifiedHandsTests(unittest.TestCase):
    def test_write_and_load(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "verified.json"
            with patch.object(verified_hands, "record_path", return_value=path):
                verified_hands.write_verification(
                    checks=[
                        {"name": "a", "tool": "resource_farm_run", "ok": True},
                        {"name": "b", "tool": "github_scout_search", "ok": True},
                    ],
                    source="test",
                )
                loaded = verified_hands.load_verification(max_age_hours=1)
                self.assertTrue(loaded.get("ok"))
                self.assertIn("resource_farm_run", loaded.get("tools_proven") or [])
                snippet = verified_hands.pulse_snippet()
                self.assertIn("Mechanic verified", snippet)


if __name__ == "__main__":
    unittest.main()
