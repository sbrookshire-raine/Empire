from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from frontend import eve_toolbelt


class EveToolbeltTests(unittest.TestCase):
    def test_normalize_keeps_allowed_order_and_drops_junk(self) -> None:
        self.assertEqual(
            eve_toolbelt.normalize_active_tools(
                ["tool_forge", "wiki_local", "gumloop_cloud", "memory", "tool_forge", 3]
            ),
            ["tool_forge", "wiki_local", "gumloop_cloud"],
        )

    def test_wiki_local_is_optional_limb(self) -> None:
        self.assertIn("wiki_local", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("time_reclaim", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("stem_factory", eve_toolbelt.ALLOWED_CATEGORIES)

    def test_normalize_defaults_when_missing(self) -> None:
        self.assertEqual(eve_toolbelt.normalize_active_tools(None), [])

    def test_apply_persists_and_strips_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                out = eve_toolbelt.apply_active_tools(
                    {
                        "message": "hello",
                        "active_tools": ["web_research", "tool_forge"],
                    }
                )
            self.assertEqual(out, {"message": "hello"})
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["active_tools"], ["web_research", "tool_forge"])
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertTrue(eve_toolbelt.category_enabled("web_research"))
                self.assertFalse(eve_toolbelt.category_enabled("gumloop_cloud"))

    def test_brain_categories_are_not_toolbelt_limbs(self) -> None:
        self.assertNotIn("memory", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertNotIn("work_orders", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertNotIn("local_files", eve_toolbelt.ALLOWED_CATEGORIES)

    def test_apply_leaves_payload_when_field_absent(self) -> None:
        payload = {"message": "hi"}
        self.assertEqual(eve_toolbelt.apply_active_tools(payload), payload)


if __name__ == "__main__":
    unittest.main()
