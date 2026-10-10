"""Host-side Heptabase CLI wrapper — JSON stdout only, never log tokens."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"(\d+)\.(\d+)\.(\d+)")


def resolve_cli_command() -> list[str]:
    override = (os.environ.get("HEPTABASE_CLI_PATH") or "").strip()
    if override:
        return [override]
    local = Path(os.environ.get("LOCALAPPDATA", "")) / ".heptabase" / "bin" / "heptabase.cmd"
    if local.is_file():
        return [str(local)]
    found = shutil.which("heptabase")
    if found:
        return [found]
    return ["heptabase"]


def _redact_stderr(text: str) -> str:
    return re.sub(r"(token|secret|password)[^\s]*", "[redacted]", text, flags=re.I)


def run_cli(args: list[str], *, input_json: dict[str, Any] | None = None, timeout: int = 120) -> dict[str, Any]:
    cmd = resolve_cli_command() + args
    stdin_data: bytes | None = None
    temp_path: Path | None = None
    try:
        if input_json is not None:
            handle, tmp = tempfile.mkstemp(prefix="heptabase-", suffix=".json")
            temp_path = Path(tmp)
            os.close(handle)
            temp_path.write_text(json.dumps(input_json, ensure_ascii=False), encoding="utf-8")
            cmd.extend(["--input", str(temp_path)])
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(EMPIRE_ROOT),
            shell=False,
        )
    except FileNotFoundError:
        return {
            "ok": False,
            "error": "Heptabase CLI not found. Install from the desktop app (Local CLI) or set HEPTABASE_CLI_PATH.",
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "Heptabase CLI timed out. Is the desktop app running?"}
    finally:
        if temp_path:
            temp_path.unlink(missing_ok=True)

    stdout = (proc.stdout or "").strip()
    stderr = _redact_stderr((proc.stderr or "").strip())
    if proc.returncode != 0:
        return {
            "ok": False,
            "error": stderr or stdout or f"heptabase exited {proc.returncode}",
            "exit_code": proc.returncode,
        }
    if not stdout:
        return {"ok": True, "raw": ""}
    try:
        parsed = json.loads(stdout)
        if isinstance(parsed, dict):
            parsed.setdefault("ok", True)
            return parsed
        return {"ok": True, "data": parsed}
    except json.JSONDecodeError:
        return {"ok": False, "error": "Heptabase CLI returned non-JSON stdout.", "raw_preview": stdout[:500]}


def health_check() -> dict[str, Any]:
    cmd = resolve_cli_command()
    try:
        proc = subprocess.run(
            cmd + ["--version"],
            capture_output=True,
            text=True,
            timeout=30,
            shell=False,
        )
    except FileNotFoundError:
        return {"ok": False, "error": "Heptabase CLI not found.", "cli_path": cmd[0]}
    version_line = (proc.stdout or proc.stderr or "").strip()
    match = VERSION_RE.search(version_line)
    compatible = False
    if match:
        major, minor = int(match.group(1)), int(match.group(2))
        compatible = major == 0 and minor >= 6
    probe = run_cli(["card", "list", "--limit", "1"])
    return {
        "ok": proc.returncode == 0 and probe.get("ok") is not False,
        "version": version_line,
        "compatible_0_6_x": compatible,
        "cli_path": cmd[0],
        "probe": "card list" if probe.get("ok") is not False else probe.get("error"),
        "hint": "Start the Heptabase desktop app if probe failed.",
    }


def search_cards(query: str, *, limit: int = 20) -> dict[str, Any]:
    args = ["card", "list", "--limit", str(max(1, min(limit, 50)))]
    if query.strip():
        args.extend(["-q", query.strip()])
    return run_cli(args)


def read_note(card_id: str) -> dict[str, Any]:
    cleaned = (card_id or "").strip()
    if not cleaned:
        return {"ok": False, "error": "card_id required"}
    return run_cli(["note", "read", cleaned])


def _write_markdown_temp(body: str) -> Path:
    handle, tmp = tempfile.mkstemp(prefix="heptabase-note-", suffix=".md")
    temp_path = Path(tmp)
    os.close(handle)
    temp_path.write_text(body, encoding="utf-8")
    return temp_path


def create_note(content: str, *, human_owned: bool = False) -> dict[str, Any]:
    body = (content or "").strip()
    if not body:
        return {"ok": False, "error": "content required"}
    temp_path = _write_markdown_temp(body)
    try:
        args = ["note", "create", "--content-file", str(temp_path)]
        if human_owned:
            args.append("--no-created-by-ai")
        return run_cli(args)
    finally:
        temp_path.unlink(missing_ok=True)


def append_note(card_id: str, content: str) -> dict[str, Any]:
    cleaned_id = (card_id or "").strip()
    body = (content or "").strip()
    if not cleaned_id:
        return {"ok": False, "error": "card_id required"}
    if not body:
        return {"ok": False, "error": "content required"}
    temp_path = _write_markdown_temp(body)
    try:
        return run_cli(["note", "append", cleaned_id, "--content-file", str(temp_path)])
    finally:
        temp_path.unlink(missing_ok=True)


def whiteboard_read_structure(whiteboard_id: str) -> dict[str, Any]:
    wid = (whiteboard_id or "").strip()
    if not wid:
        return {"ok": False, "error": "whiteboard_id required"}
    return run_cli(["whiteboard", "read", wid, "--mode", "structure"])


def whiteboard_read_layout(whiteboard_id: str) -> dict[str, Any]:
    wid = (whiteboard_id or "").strip()
    if not wid:
        return {"ok": False, "error": "whiteboard_id required"}
    return run_cli(["whiteboard", "read-layout", wid])


def whiteboard_create(title: str, *, parent_id: str = "") -> dict[str, Any]:
    args = ["whiteboard", "create", "--title", title.strip() or "EMPIRE Disassembly Catalog"]
    if parent_id.strip():
        args.extend(["--parent-whiteboard-id", parent_id.strip()])
    return run_cli(args)


def place_card_on_whiteboard(whiteboard_id: str, card_id: str) -> dict[str, Any]:
    payload = {
        "whiteboardId": whiteboard_id,
        "objects": [{"id": card_id, "objectType": "card"}],
        "destination": {"type": "auto"},
    }
    return run_cli(["whiteboard", "place-objects"], input_json=payload)


def move_card_to_point(whiteboard_id: str, placement_id: str, x: float, y: float) -> dict[str, Any]:
    payload = {
        "whiteboardId": whiteboard_id,
        "moves": [
            {
                "selection": {
                    "type": "objects",
                    "objects": [{"id": placement_id, "objectType": "card"}],
                },
                "destination": {"type": "point", "x": x, "y": y},
            }
        ],
    }
    return run_cli(["whiteboard", "move-objects"], input_json=payload)


def recolor_placement(whiteboard_id: str, placement_id: str, color: str) -> dict[str, Any]:
    payload = {
        "whiteboardId": whiteboard_id,
        "updates": [{"id": placement_id, "objectType": "card", "color": color}],
    }
    return run_cli(["whiteboard", "recolor-objects"], input_json=payload)


def create_connection(
    whiteboard_id: str,
    from_placement: str,
    to_placement: str,
) -> dict[str, Any]:
    payload = {
        "whiteboardId": whiteboard_id,
        "connections": [
            {
                "from": {"id": from_placement, "objectType": "card", "position": "right"},
                "to": {"id": to_placement, "objectType": "card", "position": "left"},
                "direction": "oneWay",
                "routeType": "straight",
            }
        ],
    }
    return run_cli(["whiteboard", "create-connections"], input_json=payload)


def whiteboard_lint(whiteboard_id: str) -> dict[str, Any]:
    return run_cli(["whiteboard", "lint", whiteboard_id])


def extract_card_id_from_create(result: dict[str, Any]) -> str:
    for key in ("cardId", "card_id", "id"):
        val = result.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    data = result.get("data")
    if isinstance(data, dict):
        for key in ("cardId", "card_id", "id"):
            val = data.get(key)
            if isinstance(val, str) and val.strip():
                return val.strip()
    return ""


def extract_placement_id_from_place(result: dict[str, Any]) -> str:
    """Best-effort parse of place-objects response (whiteboard instance id, not card id)."""
    for key in ("results", "createdWhiteboardObjects", "objects", "placements"):
        items = result.get(key)
        if not isinstance(items, list) or not items:
            continue
        first = items[0]
        if not isinstance(first, dict):
            continue
        for field in ("instanceId", "whiteboardObjectId", "placementId", "placement_id"):
            val = first.get(field)
            if isinstance(val, str) and val.strip():
                pid = val.strip()
                if not pid.startswith("inst:"):
                    pid = f"inst:{pid}"
                return pid
    return ""


def remove_card_from_whiteboard(whiteboard_id: str, card_id: str) -> dict[str, Any]:
    wid = (whiteboard_id or "").strip()
    cid = (card_id or "").strip()
    if not wid or not cid:
        return {"ok": False, "error": "whiteboard_id and card_id required"}
    payload = {
        "whiteboardId": wid,
        "removals": [{"id": cid, "objectType": "card"}],
    }
    return run_cli(["whiteboard", "remove-objects"], input_json=payload)


def trash_card(card_id: str) -> dict[str, Any]:
    cleaned = (card_id or "").strip()
    if not cleaned:
        return {"ok": False, "error": "card_id required"}
    return run_cli(["card", "trash", cleaned])


def resize_card_fit(whiteboard_id: str, placement_id: str) -> dict[str, Any]:
    pid = (placement_id or "").strip()
    if pid and not pid.startswith("inst:"):
        pid = f"inst:{pid}"
    payload = {
        "whiteboardId": whiteboard_id,
        "resizes": [{"id": pid, "objectType": "card", "mode": "fitToContent"}],
    }
    return run_cli(["whiteboard", "resize-objects"], input_json=payload)


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE Heptabase CLI wrapper")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health")
    search = sub.add_parser("search")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--limit", type=int, default=20)
    read = sub.add_parser("read-note")
    read.add_argument("card_id")
    args = parser.parse_args(argv)
    if args.cmd == "health":
        out = health_check()
    elif args.cmd == "search":
        out = search_cards(args.query, limit=args.limit)
    elif args.cmd == "read-note":
        out = read_note(args.card_id)
    else:
        return 1
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") is not False else 1


if __name__ == "__main__":
    raise SystemExit(main())
