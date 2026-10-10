"""Disassembly Card v1 — local catalog of RE play sessions (scratch, not Cognee)."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, TypedDict

from pipeline.artifact_lineage import lineage_envelope, sha256_text
from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_DIR = Path(
    os.environ.get(
        "EMPIRE_DISASSEMBLY_CARD_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\disassembly_cards",
    )
)
SCHEMA_ID = "DisassemblyCard.v1"
CONTAINERS = frozenset(
    {"electron", "native_pe", "web", "game_logic", "audio_pipeline", "unknown"}
)
STAGES = frozenset({"draft", "published", "linked", "mature", "evolved"})
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")
CARD_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{7,63}$")


class ConnectionRow(TypedDict, total=False):
    from_: str
    to: str
    kind: str
    evidence_ref: str


def cards_dir() -> Path:
    path = DEFAULT_DIR
    path.mkdir(parents=True, exist_ok=True)
    return path


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _safe_id(prefix: str = "dc") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


def _sidecar_path(card_id: str) -> Path:
    if not CARD_ID_RE.match(card_id):
        raise ValueError("invalid card id")
    return cards_dir() / f"{card_id}.json"


def _markdown_path(card_id: str) -> Path:
    return cards_dir() / f"{card_id}.md"


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp = tempfile.mkstemp(prefix="dc-", suffix=path.suffix, dir=str(path.parent))
    tmp_path = Path(tmp)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def _normalize_connections(raw: Any) -> list[dict[str, str]]:
    if not isinstance(raw, list):
        return []
    out: list[dict[str, str]] = []
    for row in raw:
        if not isinstance(row, dict):
            continue
        src = str(row.get("from") or row.get("from_") or "").strip()
        dst = str(row.get("to") or "").strip()
        if not src or not dst:
            continue
        out.append(
            {
                "from": src,
                "to": dst,
                "kind": str(row.get("kind") or "flow").strip(),
                "evidence_ref": str(row.get("evidence_ref") or "").strip(),
            }
        )
    return out


def validate_payload(data: dict[str, Any]) -> dict[str, Any]:
    title = str(data.get("title") or "").strip()
    if not title:
        raise ValueError("title is required")
    container = str(data.get("container") or "unknown").strip().lower()
    if container not in CONTAINERS:
        container = "unknown"
    connections = _normalize_connections(data.get("connections"))
    if len(connections) < 1:
        raise ValueError("at least one connection row is required")
    if len(connections) > 7:
        raise ValueError("at most seven connection rows per card")
    stage = str(data.get("learning_stage") or "draft").strip().lower()
    if stage not in STAGES:
        stage = "draft"
    card_id = str(data.get("id") or _safe_id()).strip()
    if not CARD_ID_RE.match(card_id):
        card_id = _safe_id()
    return {
        "schema_id": SCHEMA_ID,
        "id": card_id,
        "title": title[:200],
        "container": container,
        "target_summary": str(data.get("target_summary") or "").strip()[:500],
        "connections": connections,
        "evidence_refs": [
            str(x).strip()
            for x in (data.get("evidence_refs") or [])
            if str(x).strip()
        ][:20],
        "lego_hooks": [
            str(x).strip() for x in (data.get("lego_hooks") or []) if str(x).strip()
        ][:10],
        "evolution_note": str(data.get("evolution_note") or "").strip()[:2000],
        "related_card_ids": [
            str(x).strip()
            for x in (data.get("related_card_ids") or [])
            if str(x).strip()
        ],
        "depends_on": [
            str(x).strip() for x in (data.get("depends_on") or []) if str(x).strip()
        ],
        "learning_stage": stage,
        "heptabase_card_id": str(data.get("heptabase_card_id") or "").strip(),
        "heptabase_placement_id": str(data.get("heptabase_placement_id") or "").strip(),
        "heptabase_whiteboard_id": str(data.get("heptabase_whiteboard_id") or "").strip(),
        "published_at": str(data.get("published_at") or "").strip(),
        "source_repo": str(data.get("source_repo") or "").strip().lower()[:200],
        "farm_kind": str(data.get("farm_kind") or "").strip().lower()[:32],
        "created_at": str(data.get("created_at") or _utc_now()),
        "updated_at": _utc_now(),
    }


def strip_yaml_front_matter(text: str) -> str:
    """Remove leading --- YAML --- block so Heptabase sees # title first."""
    lines = text.splitlines()
    if len(lines) < 2 or lines[0].strip() != "---":
        return text
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            rest = lines[idx + 1 :]
            while rest and not rest[0].strip():
                rest = rest[1:]
            body = "\n".join(rest)
            if text.endswith("\n"):
                body += "\n"
            return body
    return text


def markdown_for_heptabase(card: dict[str, Any]) -> str:
    """Note body for Heptabase create/append (no YAML front matter; # title first)."""
    return strip_yaml_front_matter(render_markdown(card))


def render_markdown(card: dict[str, Any]) -> str:
    envelope = lineage_envelope(
        schema_id=SCHEMA_ID,
        tool="disassembly_card_write",
        limb="rea",
        model_id="empire.disassembly_card",
        input_hash=sha256_text(json.dumps(card, sort_keys=True, default=str)),
        validation_ok=True,
        extra={"card_id": card.get("id"), "container": card.get("container")},
    )
    fm = [
        "---",
        *provenance_fields(
            source="disassembly_card",
            kind="disassembly_catalog",
            tool="disassembly_card_write",
            limb="rea",
            extra={
                "card_id": card.get("id"),
                "container": card.get("container"),
                "learning_stage": card.get("learning_stage"),
            },
        ),
        "---",
    ]
    lines = [
        *fm,
        f"# {card['title']}",
        "",
        f"**Container:** `{card['container']}`",
        f"**Stage:** `{card['learning_stage']}`",
        "",
        "## Target",
        "",
        card.get("target_summary") or "_none_",
        "",
        "## Connections (semantic)",
        "",
    ]
    for idx, row in enumerate(card.get("connections") or [], start=1):
        lines.append(
            f"{idx}. `{row.get('from')}` → `{row.get('to')}` ({row.get('kind')})"
            + (f" — _{row.get('evidence_ref')}_" if row.get("evidence_ref") else "")
        )
    lines.extend(["", "## Evidence refs", ""])
    for ref in card.get("evidence_refs") or []:
        lines.append(f"- `{ref}`")
    if not card.get("evidence_refs"):
        lines.append("- _none listed_")
    lines.extend(["", "## Depends on (catalog)", ""])
    for dep in card.get("depends_on") or []:
        lines.append(f"- `{dep}`")
    if not card.get("depends_on"):
        lines.append("- _none_")
    lines.extend(["", "## Evolution", "", card.get("evolution_note") or "_none_", ""])
    if card.get("lego_hooks"):
        lines.extend(["## LEGO hooks", ""])
        for hook in card["lego_hooks"]:
            lines.append(f"- `{hook}`")
    lines.extend(
        [
            "",
            f"```json\n{json.dumps(envelope, indent=2)}\n```",
            provenance_markdown_footer(
                source="disassembly_card",
                tool="disassembly_card_write",
                limb="rea",
            ),
        ]
    )
    return "\n".join(lines) + "\n"


def write_card(data: dict[str, Any]) -> dict[str, Any]:
    card = validate_payload(data)
    sidecar = _sidecar_path(card["id"])
    if sidecar.exists() and not data.get("allow_overwrite"):
        raise ValueError(f"card id already exists: {card['id']}")
    _atomic_write(sidecar, json.dumps(card, indent=2, ensure_ascii=False))
    _atomic_write(_markdown_path(card["id"]), render_markdown(card))
    return {"ok": True, "card": public_card(card)}


def read_card(card_id: str) -> dict[str, Any]:
    path = _sidecar_path(card_id.strip())
    if not path.is_file():
        raise KeyError(card_id)
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("corrupt card sidecar")
    return raw


def update_card(card_id: str, patch: dict[str, Any]) -> dict[str, Any]:
    existing = read_card(card_id)
    merged = {**existing, **patch, "id": card_id, "updated_at": _utc_now()}
    card = validate_payload(merged)
    _atomic_write(_sidecar_path(card_id), json.dumps(card, indent=2, ensure_ascii=False))
    _atomic_write(_markdown_path(card_id), render_markdown(card))
    return {"ok": True, "card": public_card(card)}


def public_card(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": card.get("id"),
        "title": card.get("title"),
        "container": card.get("container"),
        "target_summary": card.get("target_summary"),
        "connections": card.get("connections"),
        "learning_stage": card.get("learning_stage"),
        "depends_on": card.get("depends_on"),
        "heptabase_card_id": card.get("heptabase_card_id"),
        "heptabase_placement_id": card.get("heptabase_placement_id"),
        "published_at": card.get("published_at"),
        "source_repo": card.get("source_repo") or "",
        "farm_kind": card.get("farm_kind") or "",
        "updated_at": card.get("updated_at"),
        "markdown_path": str(_markdown_path(str(card.get("id"))).resolve()),
    }


def list_cards(*, limit: int = 50) -> list[dict[str, Any]]:
    root = cards_dir()
    paths = sorted(root.glob("dc_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out: list[dict[str, Any]] = []
    for path in paths[: max(1, min(limit, 200))]:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                out.append(public_card(raw))
        except (OSError, json.JSONDecodeError, ValueError):
            continue
    return out


def published_count() -> int:
    count = 0
    for path in cards_dir().glob("dc_*.json"):
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(raw, dict) and raw.get("heptabase_placement_id"):
                count += 1
        except (OSError, json.JSONDecodeError):
            continue
    return count


def layout_anchor(container: str, index: int) -> tuple[float, float]:
    from pipeline.heptabase_config import load_learning_map

    cfg = load_learning_map().get("layout") or {}
    origin_x = float(cfg.get("origin_x") or 120)
    origin_y = float(cfg.get("origin_y") or 280)
    step_x = float(cfg.get("step_x") or 320)
    row_gap = float(cfg.get("row_gap_y") or 180)
    rows = cfg.get("container_rows") or {}
    row = int(rows.get(container) or rows.get("unknown") or 0)
    return origin_x + index * step_x, origin_y + row * row_gap


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE disassembly cards")
    sub = parser.add_subparsers(dest="cmd", required=True)
    write = sub.add_parser("write", help="Write card from JSON file")
    write.add_argument("--file", required=True)
    sub.add_parser("list").add_argument("--limit", type=int, default=50)
    show = sub.add_parser("show")
    show.add_argument("card_id")
    args = parser.parse_args(argv)
    if args.cmd == "write":
        raw = json.loads(Path(args.file).read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise SystemExit("payload must be a JSON object")
        result = write_card(raw)
    elif args.cmd == "list":
        result = {"ok": True, "cards": list_cards(limit=args.limit)}
    elif args.cmd == "show":
        result = {"ok": True, "card": public_card(read_card(args.card_id))}
    else:
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
