from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import disassembly_card


class DisassemblyCardTests(unittest.TestCase):
    def test_write_and_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(disassembly_card, "cards_dir", return_value=root):
                payload = {
                    "title": "Test Electron bridge",
                    "container": "electron",
                    "target_summary": "Sample app preload",
                    "connections": [
                        {"from": "renderer", "to": "preload", "kind": "ipc"},
                        {"from": "preload", "to": "main", "kind": "bridge"},
                    ],
                    "evidence_refs": ["C:/Empire_Workbench/rea_inbox/ab/file.zip"],
                }
                result = disassembly_card.write_card(payload)
                self.assertTrue(result.get("ok"))
                card_id = result["card"]["id"]
                listed = disassembly_card.list_cards(limit=5)
                self.assertEqual(listed[0]["id"], card_id)

    def test_rejects_too_few_connections(self) -> None:
        with self.assertRaises(ValueError):
            disassembly_card.validate_payload({"title": "x", "connections": []})


if __name__ == "__main__":
    unittest.main()
