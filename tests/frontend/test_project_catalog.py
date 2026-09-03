from __future__ import annotations

import unittest

from frontend.project_catalog import build_project_catalog, public_project


class ProjectCatalogTests(unittest.TestCase):
    def test_build_catalog_has_empire_evolution(self) -> None:
        catalog = build_project_catalog()
        projects = catalog.get("projects")
        self.assertIsInstance(projects, list)
        ids = {item.get("id") for item in projects if isinstance(item, dict)}
        self.assertIn("empire-evolution", ids)

    def test_public_project_shape(self) -> None:
        public = public_project(
            {
                "id": "empire",
                "display_name": "Empire",
                "kind": "codebase",
                "in_eve_core": True,
                "flattened_file": "x",
                "source_file_count": 241,
                "memory_files": ["a.md"],
            }
        )
        self.assertEqual(public["displayName"], "Empire")
        self.assertTrue(public["inEveCore"])


if __name__ == "__main__":
    unittest.main()
