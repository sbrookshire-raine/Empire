"""Publish Disassembly Cards to Heptabase catalog whiteboard."""

from __future__ import annotations

import json
from typing import Any

from pipeline import disassembly_card, heptabase_cli
from pipeline.heptabase_config import catalog_whiteboard_id, load_learning_map


def _stage_color(stage: str) -> str:
    colors = load_learning_map().get("stage_colors") or {}
    return str(colors.get(stage) or colors.get("published") or "orange")


def _resolve_dep_placement(dep_id: str) -> str:
    """dep_id may be local dc_* id or inst: placement."""
    if dep_id.startswith("inst:"):
        return dep_id
    try:
        card = disassembly_card.read_card(dep_id)
    except (KeyError, ValueError):
        return ""
    pid = str(card.get("heptabase_placement_id") or "").strip()
    if pid and not pid.startswith("inst:"):
        pid = f"inst:{pid}"
    return pid


def publish_to_heptabase(
    card_id: str,
    *,
    architect_confirm: bool = False,
    human_owned_note: bool = False,
) -> dict[str, Any]:
    if not architect_confirm:
        return {
            "ok": False,
            "error": "architect_confirm must be true to publish to Heptabase.",
            "need_architect": True,
        }
    whiteboard_id = catalog_whiteboard_id()
    if not whiteboard_id:
        return {
            "ok": False,
            "error": "HEPTABASE_DISASSEMBLY_WHITEBOARD_ID not set. Run scripts/ensure-heptabase-disassembly-board.ps1.",
        }
    health = heptabase_cli.health_check()
    if not health.get("ok"):
        return {"ok": False, "error": health.get("error") or "Heptabase not ready.", "health": health}

    try:
        card = disassembly_card.read_card(card_id)
    except KeyError:
        return {"ok": False, "error": f"unknown disassembly card: {card_id}"}

    md_path = disassembly_card._markdown_path(card_id)  # noqa: SLF001
    try:
        note_body = md_path.read_text(encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc)}

    heptabase_cli.whiteboard_read_layout(whiteboard_id)

    created = heptabase_cli.create_note(note_body, human_owned=human_owned_note)
    if created.get("ok") is False:
        return {"ok": False, "error": created.get("error"), "step": "note_create", "detail": created}
    hb_card_id = heptabase_cli.extract_card_id_from_create(created)
    if not hb_card_id:
        return {"ok": False, "error": "could not parse Heptabase card id from create response", "detail": created}

    placed = heptabase_cli.place_card_on_whiteboard(whiteboard_id, hb_card_id)
    if placed.get("ok") is False:
        return {"ok": False, "error": placed.get("error"), "step": "place", "detail": placed}
    placement_id = heptabase_cli.extract_placement_id_from_place(placed)

    index = disassembly_card.published_count()
    x, y = disassembly_card.layout_anchor(str(card.get("container") or "unknown"), index)
    if placement_id:
        moved = heptabase_cli.move_card_to_point(whiteboard_id, placement_id, x, y)
        if moved.get("ok") is False:
            # Non-fatal — auto placement may still be usable
            moved = {"ok": False, "warning": moved.get("error")}

    depends = list(card.get("depends_on") or [])
    stage = "evolved" if depends and card.get("evolution_note") else "published"
    color = _stage_color(stage)
    if placement_id:
        heptabase_cli.recolor_placement(whiteboard_id, placement_id, color)

    links_created = 0
    link_errors: list[str] = []
    if placement_id:
        for dep in depends:
            from_pid = _resolve_dep_placement(dep)
            if not from_pid:
                link_errors.append(f"no placement for dependency {dep}")
                continue
            conn = heptabase_cli.create_connection(whiteboard_id, from_pid, placement_id)
            if conn.get("ok") is False:
                link_errors.append(str(conn.get("error") or dep))
            else:
                links_created += 1
    if links_created > 0 and stage == "published":
        stage = "linked"
        if placement_id:
            heptabase_cli.recolor_placement(whiteboard_id, placement_id, _stage_color("linked"))

    patch = {
        "heptabase_card_id": hb_card_id,
        "heptabase_placement_id": placement_id.replace("inst:", "") if placement_id else "",
        "heptabase_whiteboard_id": whiteboard_id,
        "learning_stage": stage,
        "published_at": disassembly_card._utc_now(),  # noqa: SLF001
        "allow_overwrite": True,
    }
    updated = disassembly_card.update_card(card_id, patch)
    lint = heptabase_cli.whiteboard_lint(whiteboard_id)

    return {
        "ok": True,
        "card_id": card_id,
        "heptabase_card_id": hb_card_id,
        "heptabase_placement_id": placement_id,
        "learning_stage": stage,
        "color": color,
        "links_created": links_created,
        "link_errors": link_errors,
        "lint": lint,
        "updated": updated.get("card"),
    }


def mark_mature(
    card_id: str,
    *,
    architect_confirm: bool = False,
) -> dict[str, Any]:
    if not architect_confirm:
        return {
            "ok": False,
            "error": "architect_confirm must be true to mark mature.",
            "need_architect": True,
        }
    whiteboard_id = catalog_whiteboard_id()
    if not whiteboard_id:
        return {"ok": False, "error": "HEPTABASE_DISASSEMBLY_WHITEBOARD_ID not set."}
    try:
        card = disassembly_card.read_card(card_id)
    except KeyError:
        return {"ok": False, "error": f"unknown card: {card_id}"}
    pid = str(card.get("heptabase_placement_id") or "").strip()
    if not pid:
        return {"ok": False, "error": "card not published to Heptabase yet."}
    placement = pid if pid.startswith("inst:") else f"inst:{pid}"
    color = _stage_color("mature")
    recolor = heptabase_cli.recolor_placement(whiteboard_id, placement, color)
    if recolor.get("ok") is False:
        return {"ok": False, "error": recolor.get("error"), "detail": recolor}
    updated = disassembly_card.update_card(
        card_id,
        {"learning_stage": "mature", "allow_overwrite": True},
    )
    return {"ok": True, "card_id": card_id, "color": color, "card": updated.get("card")}


def seed_legend(*, architect_confirm: bool = False) -> dict[str, Any]:
    if not architect_confirm:
        return {"ok": False, "error": "architect_confirm required", "need_architect": True}
    whiteboard_id = catalog_whiteboard_id()
    if not whiteboard_id:
        return {"ok": False, "error": "whiteboard id not configured"}
    legend = str(load_learning_map().get("legend_markdown") or "").strip()
    if not legend:
        return {"ok": False, "error": "legend markdown missing in learning map"}
    created = heptabase_cli.create_note(legend, human_owned=True)
    if created.get("ok") is False:
        return {"ok": False, "error": created.get("error"), "detail": created}
    card_id = heptabase_cli.extract_card_id_from_create(created)
    if not card_id:
        return {"ok": False, "error": "no card id from legend note"}
    placed = heptabase_cli.place_card_on_whiteboard(whiteboard_id, card_id)
    placement_id = heptabase_cli.extract_placement_id_from_place(placed)
    if placement_id:
        heptabase_cli.move_card_to_point(whiteboard_id, placement_id, 40, 40)
        heptabase_cli.recolor_placement(whiteboard_id, placement_id, "yellow")
    return {
        "ok": placed.get("ok") is not False,
        "legend_card_id": card_id,
        "placement_id": placement_id,
        "detail": placed,
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Publish disassembly cards to Heptabase")
    sub = parser.add_subparsers(dest="cmd", required=True)
    pub = sub.add_parser("publish")
    pub.add_argument("card_id")
    pub.add_argument("--architect-confirm", action="store_true")
    mat = sub.add_parser("mark-mature")
    mat.add_argument("card_id")
    mat.add_argument("--architect-confirm", action="store_true")
    leg = sub.add_parser("seed-legend")
    leg.add_argument("--architect-confirm", action="store_true")
    args = parser.parse_args(argv)
    if args.cmd == "publish":
        result = publish_to_heptabase(args.card_id, architect_confirm=args.architect_confirm)
    elif args.cmd == "mark-mature":
        result = mark_mature(args.card_id, architect_confirm=args.architect_confirm)
    else:
        result = seed_legend(architect_confirm=args.architect_confirm)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
