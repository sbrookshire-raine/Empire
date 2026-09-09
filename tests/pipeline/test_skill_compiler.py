"""Tests for skill compiler heuristic triage."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline import skill_compiler


class SkillCompilerTests(unittest.TestCase):
    def test_inventory_and_triage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            keep = root / "docs-guide-scraper" / "SKILL.md"
            keep.parent.mkdir(parents=True)
            keep.write_text(
                "---\nname: docs-guide-scraper\ndescription: Local docs scrape for Cognee ingest\n---\n# Docs\n",
                encoding="utf-8",
            )
            reject = root / "firebase-app" / "SKILL.md"
            reject.parent.mkdir(parents=True)
            reject.write_text(
                "---\nname: firebase-app\ndescription: Requires Firebase cloud backend only\n---\n",
                encoding="utf-8",
            )

            inventory = skill_compiler.inventory_sources(
                [root],
                include_default_skills=False,
            )
            self.assertEqual(inventory["count"], 2)
            triage = skill_compiler.triage_inventory(inventory)
            verdicts = {v["name"]: v["bin"] for v in triage["verdicts"]}
            self.assertEqual(verdicts["docs-guide-scraper"], 1)
            self.assertEqual(verdicts["firebase-app"], 2)

            manifest = skill_compiler.write_triage_manifest(
                triage,
                out_dir=root,
            )
            self.assertTrue(Path(manifest["json_path"]).is_file())
            self.assertTrue(Path(manifest["markdown_path"]).is_file())


if __name__ == "__main__":
    unittest.main()
