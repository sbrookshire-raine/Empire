"""Dependency-free smoke tests for the EMPIRE upgrade foundation."""

from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPABILITY_DIR = ROOT / "config" / "eve-capabilities"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class UpgradeFoundationTests(unittest.TestCase):
    def test_all_installed_manifests_and_entrypoints_exist(self) -> None:
        for name in ("thought-map", "scenario-regret", "forecast-baseline", "topology-audit", "bayes-update"):
            skill_root = ROOT / "eve-skills" / name
            self.assertTrue((skill_root / "SKILL.md").is_file())
            self.assertTrue((skill_root / "src").is_dir())
            self.assertTrue(any(skill_root.glob("src/*/__main__.py")))

    def test_catalog_seed_is_repeatable(self) -> None:
        seed = load_module("upgrade_seed", CAPABILITY_DIR / "seed_catalog.py")
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "catalog.db"
            first = seed.seed(seed.DEFAULT_SOURCE, database)
            second = seed.seed(seed.DEFAULT_SOURCE, database)
            self.assertEqual(first["inserted"], 860)
            self.assertEqual(second["inserted"], 0)
            connection = sqlite3.connect(database)
            try:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM local_skills").fetchone()[0], 5)
            finally:
                connection.close()

    def test_router_rejects_skill_traversal(self) -> None:
        router = load_module("upgrade_router", CAPABILITY_DIR / "discovery-router.py")
        with self.assertRaises(ValueError):
            router.load_skill_manifest("../UPGRADE")

    def test_event_triggers_use_boundaries(self) -> None:
        events = load_module("ambient_events", CAPABILITY_DIR / "ambient_events.py")
        self.assertTrue(events.memory_triggered({"role": "user", "status": "completed", "text": "Perfect, that worked."}))
        self.assertFalse(events.memory_triggered({"role": "user", "status": "completed", "text": "This is an imperfection."}))
        self.assertFalse(events.memory_triggered({"role": "assistant", "status": "completed", "text": "Perfect."}))


if __name__ == "__main__":
    unittest.main()