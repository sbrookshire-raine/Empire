"""Thought-experiment notes: capture, then the read-back half (list/read) added 2026-09-24.

Capture alone left past experiments unreachable — the folder held caches and a smoke note, so a new
experiment could not build on an old one. `read` must also refuse to leave the directory.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from pipeline import thought_experiment


class ThoughtExperimentTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = Path(self._tmp.name)

    def test_capture_writes_a_note_with_front_matter(self) -> None:
        result = thought_experiment.capture(
            "Juggling rules for drumming",
            notes="Cascade = cyclic timing constraint.",
            out_dir=self.dir,
        )
        self.assertTrue(result["ok"], result)
        path = Path(result["path"])
        self.assertTrue(path.is_file())
        self.assertTrue(path.name.startswith("TE_"))
        body = path.read_text(encoding="utf-8")
        self.assertIn("# Thought experiment: Juggling rules for drumming", body)
        self.assertIn("Cascade = cyclic timing constraint.", body)

    def test_capture_still_requires_a_topic(self) -> None:
        result = thought_experiment.capture("   ", out_dir=self.dir)
        self.assertFalse(result["ok"])

    def test_list_is_newest_first_and_reads_the_topic(self) -> None:
        thought_experiment.capture("First idea", out_dir=self.dir)
        second = thought_experiment.capture("Second idea", out_dir=self.dir)
        listing = thought_experiment.list_experiments(out_dir=self.dir)
        self.assertTrue(listing["ok"])
        self.assertEqual(listing["count"], 2)
        self.assertEqual(listing["experiments"][0]["topic"], "Second idea")
        self.assertIn(Path(second["path"]).name, [Path(e["path"]).name for e in listing["experiments"]])

    def test_read_returns_the_note_body(self) -> None:
        captured = thought_experiment.capture("Readable", notes="detail here", out_dir=self.dir)
        name = Path(captured["path"]).stem
        result = thought_experiment.read_experiment(name, out_dir=self.dir)
        self.assertTrue(result["ok"], result)
        self.assertIn("detail here", result["text"])
        self.assertEqual(result["name"], name)

    def test_read_refuses_traversal_and_missing_notes(self) -> None:
        outside = self.dir.parent / "outside.md"
        outside.write_text("secret", encoding="utf-8")
        self.addCleanup(outside.unlink, missing_ok=True)
        escaped = thought_experiment.read_experiment("../outside.md", out_dir=self.dir)
        self.assertFalse(escaped["ok"])
        self.assertIn("inside 04_Thought_Experiments", escaped["error"])
        missing = thought_experiment.read_experiment("ghost", out_dir=self.dir)
        self.assertFalse(missing["ok"])

    def test_list_reports_a_missing_directory(self) -> None:
        result = thought_experiment.list_experiments(out_dir=self.dir / "nope")
        self.assertFalse(result["ok"])


if __name__ == "__main__":
    unittest.main()
