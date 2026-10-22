from __future__ import annotations

import json
import os
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

    def test_extract_reads_the_flat_shape(self) -> None:
        self.assertEqual(
            eve_toolbelt.extract_active_tools({"active_tools": ["wiki_local", "junk"]}),
            ["wiki_local"],
        )

    def test_extract_reads_the_nested_shape(self) -> None:
        """The live harnesses posted `{"toolbelt": {"active_tools": [...]}}`.

        The toolbelt path only read the flat shape, so the nested one was
        silently discarded and every measurement taken against it was
        attributed to a toolbelt that was never actually applied.
        """

        self.assertEqual(
            eve_toolbelt.extract_active_tools(
                {"toolbelt": {"active_tools": ["wiki_local", "voice_presence"]}}
            ),
            ["wiki_local", "voice_presence"],
        )

    def test_flat_shape_wins_when_both_are_present(self) -> None:
        self.assertEqual(
            eve_toolbelt.extract_active_tools(
                {
                    "active_tools": ["tool_forge"],
                    "toolbelt": {"active_tools": ["wiki_local"]},
                }
            ),
            ["tool_forge"],
        )

    def test_extract_returns_none_when_no_toolbelt_is_present(self) -> None:
        """None means "carry no toolbelt" — not "an empty toolbelt".

        The difference matters: an absent toolbelt must leave the persisted
        selection alone, while an explicit empty list clears it.
        """

        self.assertIsNone(eve_toolbelt.extract_active_tools({"message": "hi"}))
        self.assertIsNone(eve_toolbelt.extract_active_tools({"toolbelt": {}}))
        self.assertIsNone(eve_toolbelt.extract_active_tools({"active_tools": "wiki_local"}))
        self.assertEqual(eve_toolbelt.extract_active_tools({"active_tools": []}), [])

    def test_apply_persists_the_nested_shape_and_strips_both_keys(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                out = eve_toolbelt.apply_active_tools(
                    {"message": "hello", "toolbelt": {"active_tools": ["wiki_local"]}}
                )
            self.assertEqual(out, {"message": "hello"})
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["active_tools"], ["wiki_local"])

    def test_temporary_active_tools_restores_the_previous_selection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                eve_toolbelt.write_active_tools(["tool_forge"])
                with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                    self.assertEqual(eve_toolbelt.load_active_tools(), ["wiki_local"])
                self.assertEqual(eve_toolbelt.load_active_tools(), ["tool_forge"])

    def test_temporary_active_tools_restores_after_a_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                eve_toolbelt.write_active_tools(["tool_forge"])
                with self.assertRaises(RuntimeError):
                    with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                        raise RuntimeError("harness failed")
                self.assertEqual(eve_toolbelt.load_active_tools(), ["tool_forge"])

    def test_temporary_active_tools_restores_the_file_byte_for_byte(self) -> None:
        """The restore must be EXACT, not merely equivalent.

        The file is the operator's; a re-serialised version would drop keys
        the operator (or a future version) put there.
        """

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            original = b'{"active_tools": ["voice_presence"], "custom": 7}\n'
            path.write_bytes(original)
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                    self.assertEqual(eve_toolbelt.load_active_tools(), ["wiki_local"])
                self.assertEqual(path.read_bytes(), original)

    def test_temporary_active_tools_removes_a_file_it_created(self) -> None:
        """A missing file and a file holding [] are different states.

        The agent (toolbelt.ts) falls back to its default Voice + Wiki
        selection only when the file is ABSENT, so restoring "[]" would
        silently turn the voice limb OFF on a fresh install.
        """

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                with eve_toolbelt.temporary_active_tools(["wiki_local"]):
                    self.assertTrue(path.exists())
                self.assertFalse(
                    path.exists(),
                    "the guard left a toolbelt file that was not there before",
                )

    def test_temporary_active_tools_merge_keeps_the_operator_selection(self) -> None:
        """merge=True ADDS limbs; the operator's own stay on for the run."""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                eve_toolbelt.write_active_tools(["tool_forge"])
                with eve_toolbelt.temporary_active_tools(
                    ["wiki_local"], merge=True
                ) as applied:
                    self.assertIn("tool_forge", applied)
                    self.assertIn("wiki_local", applied)
                self.assertEqual(eve_toolbelt.load_active_tools(), ["tool_forge"])

    def test_write_active_tools_is_atomic(self) -> None:
        """A half-written file must never be observable.

        The agent reads this file on every tool check, so a torn write would
        be read as a broken toolbelt.
        """

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                eve_toolbelt.write_active_tools(["wiki_local"])
                saved = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(saved["active_tools"], ["wiki_local"])
            leftovers = [p.name for p in Path(tmp).iterdir() if p.name != "eve-toolbelt.json"]
            self.assertEqual(leftovers, [], "the atomic write left a temp file behind")

    def test_toolbelt_path_honours_the_env_override(self) -> None:
        """The toolbelt file is the operator's; the test suite redirects it.

        A test that touched `apply_active_tools` (which persists what it is
        given) used to write the REAL file in %LOCALAPPDATA%\\EMPIRE - so
        running the unit tests turned the Architect's voice_presence limb
        off. The path is now overridable and `tests/__init__.py` points it
        at a temp file for every test run.
        """

        with tempfile.TemporaryDirectory() as tmp:
            override = Path(tmp) / "toolbelt.json"
            with patch.dict(os.environ, {"EMPIRE_TOOLBELT_PATH": str(override)}):
                self.assertEqual(eve_toolbelt._toolbelt_path(), override)

    def test_the_test_package_redirects_the_toolbelt(self) -> None:
        import tests

        self.assertTrue(
            os.environ.get("EMPIRE_TOOLBELT_PATH"),
            "the test package must point the toolbelt at a temp file",
        )
        self.assertTrue(tests.__doc__)

    def test_load_defaults_empty_when_file_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "missing.json"
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertEqual(eve_toolbelt.load_active_tools(), [])

    def test_load_migrates_v1_toolbelt_to_voice_on(self) -> None:
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

    def test_load_v2_to_v3_preserves_checklist_without_forcing_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "eve-toolbelt.json"
            path.write_text(
                json.dumps(
                    {"active_tools": ["wiki_local"], "defaults_version": 2},
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                self.assertEqual(eve_toolbelt.load_active_tools(), ["wiki_local"])
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["defaults_version"], 3)

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
        cases: list[tuple[object, list[str]]] = [
            ("1", ["tool_forge", "voice_presence", "wiki_local"]),
            ("1.0", ["tool_forge", "voice_presence", "wiki_local"]),
            ("legacy", ["tool_forge", "voice_presence", "wiki_local"]),
            ([], ["tool_forge", "voice_presence", "wiki_local"]),
            ({"v": 1}, ["tool_forge", "voice_presence", "wiki_local"]),
            (True, ["tool_forge", "voice_presence", "wiki_local"]),
            ("2", ["tool_forge"]),
            (2, ["tool_forge"]),
        ]
        for raw_version, expected in cases:
            with self.subTest(raw_version=raw_version):
                with tempfile.TemporaryDirectory() as tmp:
                    path = Path(tmp) / "eve-toolbelt.json"
                    path.write_text(
                        json.dumps({"active_tools": ["tool_forge"], "defaults_version": raw_version}),
                        encoding="utf-8",
                    )
                    with patch.object(eve_toolbelt, "_toolbelt_path", return_value=path):
                        self.assertEqual(eve_toolbelt.load_active_tools(), expected)
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
