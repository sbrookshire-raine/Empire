"""Unit tests for LEGO whiteboard API."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from frontend import lego_api


class LegoApiTests(unittest.TestCase):
    def test_instantiate_research_recipe(self) -> None:
        result = lego_api.instantiate_recipe("research-partner")
        self.assertTrue(result["ok"])
        board = result["board"]
        self.assertEqual(len(board["nodes"]), 5)
        self.assertGreaterEqual(len(board["edges"]), 4)
        bricks = {node["brick"] for node in board["nodes"]}
        self.assertIn("github", bricks)
        self.assertIn("wiki", bricks)

    def test_validate_unknown_brick(self) -> None:
        result = lego_api.validate_board(
            {
                "nodes": [{"id": "n1", "brick": "not-a-brick", "enabled": True}],
                "edges": [],
            }
        )
        self.assertFalse(result["ok"])
        self.assertTrue(result["issues"])

    def test_apply_merge_keeps_existing_toolbelt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            toolbelt = Path(tmp) / "eve-toolbelt.json"
            toolbelt.write_text(
                json.dumps({"active_tools": ["voice_presence"]}),
                encoding="utf-8",
            )
            with mock.patch.object(lego_api.eve_toolbelt, "_toolbelt_path", return_value=toolbelt):
                with mock.patch.object(
                    lego_api.eve_toolbelt,
                    "load_active_tools",
                    return_value=["voice_presence"],
                ):
                    result = lego_api.apply_toolbelt_from_board(
                        {
                            "nodes": [
                                {
                                    "id": "n1",
                                    "brick": "wiki",
                                    "enabled": True,
                                }
                            ],
                            "edges": [],
                            "merge": True,
                        }
                    )
            self.assertTrue(result["ok"])
            self.assertIn("wiki_local", result["active_tools"])
            self.assertIn("voice_presence", result["active_tools"])

    def test_load_recipes_catalog(self) -> None:
        result = lego_api.load_recipes()
        self.assertTrue(result["ok"])
        ids = [item["id"] for item in result["recipes"]]
        self.assertIn("morning-coach", ids)


if __name__ == "__main__":
    unittest.main()
