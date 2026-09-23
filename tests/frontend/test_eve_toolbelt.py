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

    def test_category_buckets(self) -> None:
        self.assertEqual(eve_toolbelt.category_bucket("voice_presence"), "always")
        self.assertEqual(eve_toolbelt.category_bucket("wiki_local"), "session")
        self.assertEqual(eve_toolbelt.category_bucket("stem_factory"), "products")
        self.assertEqual(eve_toolbelt.category_bucket("time_reclaim"), "products")
        meta = eve_toolbelt.toolbelt_meta()
        self.assertEqual(len(meta["buckets"]), 3)
        self.assertIn("voice_presence", meta["buckets"][0]["categories"])

    def test_wiki_local_is_optional_limb(self) -> None:
        self.assertIn("wiki_local", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("time_reclaim", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("stem_factory", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("tool_forge", eve_toolbelt.ALLOWED_CATEGORIES)
        self.assertIn("loom_intake", eve_toolbelt.ALLOWED_CATEGORIES)

    def test_normalize_defaults_when_missing(self) -> None:
        self.assertEqual(
            eve_toolbelt.normalize_active_tools(None),
            ["voice_presence", "wiki_local"],
        )

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

    def test_load_defaults_voice_and_wiki_when_file_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertEqual(
                    eve_toolbelt.load_active_tools(),
                    ["voice_presence", "wiki_local"],
                )

    def test_load_migrates_legacy_toolbelt_to_voice_on(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            path.write_text(
                json.dumps({"active_tools": ["tool_forge"]}, indent=2) + "\n",
                encoding="utf-8",
            )
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertEqual(
                    eve_toolbelt.load_active_tools(),
                    ["tool_forge", "voice_presence", "wiki_local"],
                )
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["defaults_version"], eve_toolbelt.DEFAULTS_VERSION)

    def test_load_honors_string_current_version_without_forcing_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            path.write_text(
                json.dumps(
                    {
                        "active_tools": ["tool_forge"],
                        "defaults_version": str(eve_toolbelt.DEFAULTS_VERSION),
                    }
                ),
                encoding="utf-8",
            )
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertEqual(eve_toolbelt.load_active_tools(), ["tool_forge"])

    def test_load_tolerates_legacy_version_shapes(self) -> None:
        for raw_version in ("1", "1.0", "legacy", [], {"v": 1}, True):
            with self.subTest(raw_version=raw_version):
                with tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "eve-toolbelt.json"
                    path.write_text(
                        json.dumps({"active_tools": ["tool_forge"], "defaults_version": raw_version}),
                        encoding="utf-8",
                    )
                    with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                        self.assertEqual(
                            eve_toolbelt.load_active_tools(),
                            ["tool_forge", "voice_presence", "wiki_local"],
                        )
                    saved = json.loads(path.read_text(encoding="utf-8"))
                    self.assertEqual(saved["defaults_version"], eve_toolbelt.DEFAULTS_VERSION)

    def test_version_number_coercion(self) -> None:
        self.assertEqual(eve_toolbelt._version_number(None), 0)
        self.assertEqual(eve_toolbelt._version_number("2.0"), 2)
        self.assertEqual(eve_toolbelt._version_number("  3 "), 3)
        self.assertEqual(eve_toolbelt._version_number("legacy"), 0)
        self.assertEqual(eve_toolbelt._version_number([1]), 0)
        self.assertEqual(eve_toolbelt._version_number(4), 4)


if __name__ == "__main__":
    unittest.main()
