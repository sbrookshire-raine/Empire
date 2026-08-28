from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from frontend import ollama_cli


class OllamaCliTests(unittest.TestCase):
    @patch("frontend.ollama_cli.build_inventory")
    @patch("frontend.ollama_cli.fetch_tags")
    def test_inventory_prints_json(self, fetch_tags, build_inventory) -> None:
        fetch_tags.return_value = {"models": []}
        build_inventory.return_value = {"ok": True, "models": [], "recommendations": {"suite": []}}

        with patch("sys.stdout") as stdout:
            code = ollama_cli.cmd_inventory()

        self.assertEqual(code, 0)
        payload = json.loads(stdout.write.call_args[0][0])
        self.assertTrue(payload["ok"])

    @patch("frontend.ollama_cli.set_active_model")
    @patch("frontend.ollama_cli.fetch_tags")
    def test_set_active_returns_status(self, fetch_tags, set_active_model) -> None:
        fetch_tags.return_value = {"models": []}
        set_active_model.return_value = {
            "ok": True,
            "connected": True,
            "active": "deepseek-r1:latest",
            "models": [],
            "error": "",
        }

        with patch("sys.stdout") as stdout:
            code = ollama_cli.cmd_set_active("deepseek-r1:latest")

        self.assertEqual(code, 0)
        payload = json.loads(stdout.write.call_args[0][0])
        self.assertEqual(payload["active"], "deepseek-r1:latest")


if __name__ == "__main__":
    unittest.main()
