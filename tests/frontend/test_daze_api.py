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

    def test_compare_phases_mocked(self) -> None:
        def fake_list(*, day=None, phase=None):  # noqa: ANN001
            if phase == "planned":
                return {
                    "ok": True,
                    "date": day or "2026-09-06",
                    "items": [
                        {
                            "id": "1",
                            "title": "Run",
                            "start_minute": 420,
                            "end_minute": 480,
                            "kind": "body",
                        }
                    ],
                    "conflicts": [],
                }
            return {
                "ok": True,
                "date": day or "2026-09-06",
                "items": [],
                "conflicts": [],
            }

        original = daze_api.list_day
        daze_api.list_day = fake_list  # type: ignore[assignment]
        try:
            result = daze_api.compare_phases(day="2026-09-06")
        finally:
            daze_api.list_day = original  # type: ignore[assignment]
        self.assertTrue(result["ok"])
        self.assertEqual(result["planned"]["count"], 1)
        self.assertTrue(result["coaching"])

    def test_normalize_day_aliases(self) -> None:
        today = daze_api._today_local()
        day, err = daze_api.normalize_day("")
        self.assertIsNone(err)
        self.assertEqual(day, today)
        day2, err2 = daze_api.normalize_day("today")
        self.assertIsNone(err2)
        self.assertEqual(day2, today)
        bad, err3 = daze_api.normalize_day("October 5, 2023")
        self.assertIsNone(bad)
        self.assertIn("YYYY-MM-DD", err3 or "")

    def test_handle_api_both_phase_route(self) -> None:
        def fake_list(*, day=None, phase=None):  # noqa: ANN001
            return {
                "ok": True,
                "date": day or "2026-09-06",
                "items": [],
                "conflicts": [],
            }

        original = daze_api.list_day
        daze_api.list_day = fake_list  # type: ignore[assignment]
        try:
            status, payload = daze_api.handle_api(
                "GET",
                "/api/daze/day?date=2026-09-06&phase=both",
            )
        finally:
            daze_api.list_day = original  # type: ignore[assignment]
        self.assertEqual(status, 200)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["phase"], "both")


if __name__ == "__main__":
    unittest.main()
