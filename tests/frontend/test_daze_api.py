"""Unit tests for DAZE free-window / conflict helpers (no PocketBase required)."""

from __future__ import annotations

import unittest

from frontend import daze_api


class DazeApiHelpersTests(unittest.TestCase):
    def test_validate_rejects_bad_range(self) -> None:
        cleaned, err = daze_api.validate_block_payload(
            {
                "date": "2026-09-06",
                "title": "X",
                "start_minute": 100,
                "end_minute": 50,
                "kind": "focus",
                "phase": "planned",
            }
        )
        self.assertIsNone(cleaned)
        self.assertIn("minutes", err or "")

    def test_find_conflicts(self) -> None:
        items = [
            {"id": "a", "title": "A", "start_minute": 60, "end_minute": 120},
            {"id": "b", "title": "B", "start_minute": 90, "end_minute": 150},
            {"id": "c", "title": "C", "start_minute": 200, "end_minute": 260},
        ]
        conflicts = daze_api.find_conflicts(items)
        self.assertEqual(len(conflicts), 1)
        self.assertEqual(conflicts[0]["a_id"], "a")
        self.assertEqual(conflicts[0]["b_id"], "b")

    def test_free_windows_with_mocked_list(self) -> None:
        def fake_list(*, day=None, phase=None):  # noqa: ANN001
            return {
                "ok": True,
                "date": "2026-09-06",
                "items": [
                    {"id": "1", "start_minute": 0, "end_minute": 60, "title": "sleep"},
                    {
                        "id": "2",
                        "start_minute": 600,
                        "end_minute": 720,
                        "title": "work",
                    },
                ],
                "conflicts": [],
            }

        original = daze_api.list_day
        daze_api.list_day = fake_list  # type: ignore[assignment]
        try:
            result = daze_api.free_windows(day="2026-09-06", min_minutes=30)
        finally:
            daze_api.list_day = original  # type: ignore[assignment]
        self.assertTrue(result["ok"])
        labels = [w["label"] for w in result["free"]]
        self.assertTrue(any(w.startswith("01:00") for w in labels))
        self.assertTrue(any("12:00" in w for w in labels))


if __name__ == "__main__":
    unittest.main()
