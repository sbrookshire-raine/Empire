"""Tests for GitHub scout (mocked HTTP)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from pipeline import github_scout


class GitHubScoutTests(unittest.TestCase):
    def test_search_repos_mock(self) -> None:
        payload = {
            "items": [
                {
                    "full_name": "org/demo-mcp",
                    "description": "Local MCP demo",
                    "stargazers_count": 42,
                    "forks_count": 3,
                    "language": "Python",
                    "license": {"spdx_id": "MIT"},
                    "updated_at": "2026-01-01T00:00:00Z",
                    "html_url": "https://github.com/org/demo-mcp",
                    "topics": ["mcp"],
                }
            ]
        }

        def fake_get(path: str, *, timeout: float = 25.0, **_kwargs: object) -> dict:
            self.assertIn("/search/repositories", path)
            return {"ok": True, "status": 200, "url": path, "data": payload}

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(github_scout, "_github_get", side_effect=fake_get):
                result = github_scout.search_repos(
                    "mcp local",
                    limit=5,
                    cache_dir=Path(tmp),
                    write_files=True,
                )
            self.assertTrue(result["ok"])
            self.assertEqual(result["count"], 1)
            self.assertTrue(Path(result["path"]).is_file())

    def test_repo_readme_requires_slug(self) -> None:
        result = github_scout.repo_readme("not-a-slug", write_files=False)
        self.assertFalse(result["ok"])


if __name__ == "__main__":
    unittest.main()
