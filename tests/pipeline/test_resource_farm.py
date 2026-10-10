from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import disassembly_card, resource_farm


class ResourceFarmTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cards_patch = patch.object(disassembly_card, "cards_dir", return_value=self.root)
        self.cards_patch.start()

    def tearDown(self) -> None:
        self.cards_patch.stop()
        self.tmp.cleanup()

    def test_catalog_status_empty(self) -> None:
        out = resource_farm.catalog_status()
        self.assertTrue(out.get("ok"))
        self.assertEqual(out.get("farmed_repo_count"), 0)

    def test_run_farm_skips_duplicate_repo(self) -> None:
        disassembly_card.write_card(
            {
                "title": "acme/foo — scout ticket",
                "target_summary": "existing",
                "source_repo": "acme/foo",
                "farm_kind": "scout",
                "connections": [
                    {"from": "a", "to": "b", "kind": "k"},
                    {"from": "b", "to": "c", "kind": "k"},
                    {"from": "c", "to": "d", "kind": "k"},
                ],
            }
        )
        fake_search = {
            "ok": True,
            "query": "test",
            "count": 1,
            "path": "C:/cache/search.md",
            "results": [
                {
                    "full_name": "acme/foo",
                    "description": "desc",
                    "html_url": "https://github.com/acme/foo",
                    "language": "Rust",
                    "topics": ["mcp"],
                }
            ],
        }
        with patch.object(resource_farm.github_scout, "search_repos", return_value=fake_search):
            with patch.object(resource_farm.github_scout, "repo_readme") as readme_mock:
                readme_mock.return_value = {
                    "ok": True,
                    "path": "C:/cache/readme.md",
                    "summary": "hello mcp",
                }
                out = resource_farm.run_farm("local agent", max_new_cards=3)

        self.assertTrue(out.get("ok"))
        self.assertEqual(len(out.get("created") or []), 0)
        self.assertEqual(len(out.get("skipped") or []), 1)

    def test_heptabase_plan_requires_confirm(self) -> None:
        ok, reason = resource_farm._heptabase_publish_plan(
            architect_confirm=False,
            publish_heptabase=None,
        )
        self.assertFalse(ok)
        self.assertIn("architect_confirm", reason)


if __name__ == "__main__":
    unittest.main()
