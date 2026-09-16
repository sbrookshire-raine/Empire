"""Unit tests for Eve staging memory (mocked Cognee)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from pipeline import eve_staging


class EveStagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.staging = self.root / "staging"
        self.ledger = self.root / "ledger.json"
        self.staging.mkdir(parents=True, exist_ok=True)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_propose_list_confirm_drop(self) -> None:
        with (
            patch.object(eve_staging, "staging_dir", return_value=self.staging),
            patch.object(eve_staging, "ledger_path", return_value=self.ledger),
            patch(
                "pipeline.wiki_scout.allowed_promote_datasets",
                return_value=frozenset({"eve_staging", "eve_memory", "eve_core"}),
            ),
            patch("pipeline.cognee_client.remember", new_callable=AsyncMock) as mock_remember,
        ):
            proposed = eve_staging.propose_remember(
                "Useful crumb: recall worked for Switch specs.",
                reason="successful extract",
                crumb="nintendo-switch-specs",
            )
            self.assertTrue(proposed["ok"])
            eid = proposed["entry_id"]
            mock_remember.assert_awaited()

            listed = eve_staging.list_staging()
            self.assertEqual(listed["count"], 1)
            self.assertEqual(listed["entries"][0]["id"], eid)

            confirmed = eve_staging.confirm_remember(eid, target_dataset="eve_memory")
            self.assertTrue(confirmed["ok"])
            self.assertEqual(confirmed["dataset"], "eve_memory")

            proposed2 = eve_staging.propose_remember("noise", reason="test")
            self.assertTrue(proposed2["ok"])
            dropped = eve_staging.drop_staging(proposed2["entry_id"])
            self.assertTrue(dropped["ok"])

    def test_confirm_rejects_bad_target(self) -> None:
        with (
            patch.object(eve_staging, "staging_dir", return_value=self.staging),
            patch.object(eve_staging, "ledger_path", return_value=self.ledger),
            patch(
                "pipeline.wiki_scout.allowed_promote_datasets",
                return_value=frozenset({"eve_staging", "eve_memory"}),
            ),
            patch("pipeline.cognee_client.remember", new_callable=AsyncMock),
        ):
            proposed = eve_staging.propose_remember("x")
            eid = proposed["entry_id"]
            bad = eve_staging.confirm_remember(eid, target_dataset="truth_drift")
            self.assertFalse(bad["ok"])

    def test_sweep_expired(self) -> None:
        with (
            patch.object(eve_staging, "staging_dir", return_value=self.staging),
            patch.object(eve_staging, "ledger_path", return_value=self.ledger),
            patch(
                "pipeline.wiki_scout.allowed_promote_datasets",
                return_value=frozenset({"eve_staging", "eve_memory"}),
            ),
            patch("pipeline.cognee_client.remember", new_callable=AsyncMock),
            patch.object(eve_staging, "ttl_hours", return_value=0),
        ):
            proposed = eve_staging.propose_remember("stale crumb", reason="ttl test")
            eid = proposed["entry_id"]
            path = Path(proposed["path"])
            self.assertTrue(path.is_file())
            swept = eve_staging.sweep_expired()
            self.assertTrue(swept["ok"])
            self.assertIn(eid, swept["swept"])
            self.assertFalse(path.is_file())


if __name__ == "__main__":
    unittest.main()
