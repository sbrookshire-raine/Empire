from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import disassembly_card, disassembly_publish, heptabase_cli


class DisassemblyPublishTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.cards_patch = patch.object(disassembly_card, "cards_dir", return_value=self.root)
        self.cards_patch.start()

    def tearDown(self) -> None:
        self.cards_patch.stop()
        self.tmp.cleanup()

    def _write_card(self, **extra: object) -> str:
        payload = {
            "title": "Publish test",
            "container": "web",
            "target_summary": "summary",
            "connections": [
                {"from": "a", "to": "b", "kind": "test"},
                {"from": "b", "to": "c", "kind": "test"},
                {"from": "c", "to": "d", "kind": "test"},
            ],
            **extra,
        }
        result = disassembly_card.write_card(payload)
        self.assertTrue(result.get("ok"))
        return str(result["card"]["id"])

    def test_publish_requires_architect_confirm(self) -> None:
        card_id = self._write_card()
        out = disassembly_publish.publish_to_heptabase(card_id, architect_confirm=False)
        self.assertFalse(out.get("ok"))
        self.assertTrue(out.get("need_architect"))

    def test_publish_applies_orange_then_blue_when_linked(self) -> None:
        dep_id = self._write_card(title="dep")
        disassembly_card.update_card(
            dep_id,
            {
                "heptabase_placement_id": "dep-placement",
                "allow_overwrite": True,
            },
        )
        card_id = self._write_card(depends_on=[dep_id], evolution_note="")

        recolors: list[tuple[str, str]] = []

        def fake_recolor(_wb: str, placement: str, color: str) -> dict:
            recolors.append((placement, color))
            return {"ok": True}

        with patch("pipeline.disassembly_publish.catalog_whiteboard_id", return_value="wb-1"):
            with patch.object(heptabase_cli, "health_check", return_value={"ok": True}):
                with patch.object(heptabase_cli, "whiteboard_read_layout", return_value={"ok": True}):
                    with patch.object(
                        heptabase_cli,
                        "create_note",
                        return_value={"ok": True, "cardId": "note-1"},
                    ):
                        with patch.object(
                            heptabase_cli,
                            "place_card_on_whiteboard",
                            return_value={"ok": True, "placementId": "inst:new-1"},
                        ):
                            with patch.object(
                                heptabase_cli,
                                "extract_card_id_from_create",
                                return_value="note-1",
                            ):
                                with patch.object(
                                    heptabase_cli,
                                    "extract_placement_id_from_place",
                                    return_value="inst:new-1",
                                ):
                                    with patch.object(
                                        heptabase_cli,
                                        "move_card_to_point",
                                        return_value={"ok": True},
                                    ):
                                        with patch.object(
                                            heptabase_cli,
                                            "recolor_placement",
                                            side_effect=fake_recolor,
                                        ):
                                            with patch.object(
                                                heptabase_cli,
                                                "create_connection",
                                                return_value={"ok": True},
                                            ):
                                                with patch.object(
                                                    heptabase_cli,
                                                    "whiteboard_lint",
                                                    return_value={"ok": True},
                                                ):
                                                    out = disassembly_publish.publish_to_heptabase(
                                                        card_id,
                                                        architect_confirm=True,
                                                    )

        self.assertTrue(out.get("ok"))
        self.assertEqual(out.get("learning_stage"), "linked")
        self.assertGreaterEqual(len(recolors), 2)
        self.assertEqual(recolors[0][1], "orange")
        self.assertEqual(recolors[-1][1], "blue")

    def test_publish_evolved_purple_when_dep_and_evolution_note(self) -> None:
        card_id = self._write_card(
            depends_on=["dc_missing"],
            evolution_note="Builds on prior session.",
        )
        colors: list[str] = []

        with patch("pipeline.disassembly_publish.catalog_whiteboard_id", return_value="wb-1"):
            with patch.object(heptabase_cli, "health_check", return_value={"ok": True}):
                with patch.object(heptabase_cli, "whiteboard_read_layout", return_value={"ok": True}):
                    with patch.object(
                        heptabase_cli,
                        "create_note",
                        return_value={"ok": True, "cardId": "n1"},
                    ):
                        with patch.object(
                            heptabase_cli,
                            "place_card_on_whiteboard",
                            return_value={"ok": True, "placementId": "inst:p1"},
                        ):
                            with patch.object(
                                heptabase_cli,
                                "extract_card_id_from_create",
                                return_value="n1",
                            ):
                                with patch.object(
                                    heptabase_cli,
                                    "extract_placement_id_from_place",
                                    return_value="inst:p1",
                                ):
                                    with patch.object(
                                        heptabase_cli,
                                        "move_card_to_point",
                                        return_value={"ok": True},
                                    ):
                                        with patch.object(
                                            heptabase_cli,
                                            "recolor_placement",
                                            side_effect=lambda _w, _p, c: colors.append(c) or {"ok": True},
                                        ):
                                            with patch.object(
                                                heptabase_cli,
                                                "whiteboard_lint",
                                                return_value={"ok": True},
                                            ):
                                                out = disassembly_publish.publish_to_heptabase(
                                                    card_id,
                                                    architect_confirm=True,
                                                )

        self.assertTrue(out.get("ok"))
        self.assertEqual(out.get("learning_stage"), "evolved")
        self.assertEqual(colors[0], "purple")

    def test_seed_legend_uses_learning_map_markdown(self) -> None:
        with patch("pipeline.disassembly_publish.catalog_whiteboard_id", return_value="wb-legend"):
            with patch(
                "pipeline.disassembly_publish.load_learning_map",
                return_value={"legend_markdown": "# Legend\n\nOrange = new"},
            ):
                captured: dict[str, str] = {}

                def fake_create(body: str, **kwargs: object) -> dict:
                    captured["body"] = body
                    return {"ok": True, "cardId": "leg-1"}

                with patch.object(heptabase_cli, "create_note", side_effect=fake_create):
                    with patch.object(
                        heptabase_cli,
                        "extract_card_id_from_create",
                        return_value="leg-1",
                    ):
                        with patch.object(
                            heptabase_cli,
                            "place_card_on_whiteboard",
                            return_value={"ok": True, "placementId": "inst:leg"},
                        ):
                            with patch.object(
                                heptabase_cli,
                                "extract_placement_id_from_place",
                                return_value="inst:leg",
                            ):
                                with patch.object(
                                    heptabase_cli,
                                    "move_card_to_point",
                                    return_value={"ok": True},
                                ):
                                    with patch.object(
                                        heptabase_cli,
                                        "recolor_placement",
                                        return_value={"ok": True},
                                    ):
                                        out = disassembly_publish.seed_legend(
                                            architect_confirm=True,
                                        )

        self.assertTrue(out.get("ok"))
        self.assertIn("Legend", captured.get("body", ""))

    def test_learning_map_has_stage_colors(self) -> None:
        path = Path(__file__).resolve().parents[2] / "config" / "heptabase-learning-map.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        colors = data.get("stage_colors") or {}
        for stage in ("published", "linked", "mature", "evolved"):
            self.assertIn(stage, colors)


if __name__ == "__main__":
    unittest.main()
