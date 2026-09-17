"""Unit tests for the capability seed (governance activation).

Verifies the seed produces an approved, hash-stable registry + snapshot, and
that the fail-closed verify path rejects unseeded/unknown capabilities.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline import capability_registry as cr
from pipeline import capability_seed as cs


class CapabilitySeedTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_seed_writes_registry_and_snapshot(self) -> None:
        out = cs.seed(registry_dir=str(self.root))
        self.assertTrue(out["ok"])
        self.assertTrue(Path(out["registry"]).is_file())
        self.assertTrue(Path(out["snapshot"]).is_file())
        self.assertEqual(out["tool_count"], 13)
        self.assertIn("switchboard", out["capabilities"])

    def test_seeded_capabilities_verify_approved(self) -> None:
        cs.seed(registry_dir=str(self.root))
        for cid in cs.canonical_capabilities():
            res = cr.verify_capability(cid["capability_id"])
            self.assertTrue(res["ok"], f"{cid['capability_id']}: {res}")
            self.assertTrue(res["approved"], f"{cid['capability_id']}: {res}")

    def test_unknown_capability_fails_closed(self) -> None:
        cs.seed(registry_dir=str(self.root))
        res = cr.verify_capability("does_not_exist")
        self.assertFalse(res["ok"])
        self.assertFalse(res["approved"])

    def test_seed_is_idempotent(self) -> None:
        first = cs.seed(registry_dir=str(self.root))
        second = cs.seed(registry_dir=str(self.root))
        self.assertTrue(first["ok"])
        self.assertTrue(second["ok"])
        self.assertEqual(first["capabilities"], second["capabilities"])
        self.assertEqual(first["tool_count"], second["tool_count"])


if __name__ == "__main__":
    unittest.main()
