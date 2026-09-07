"""Living ARCHITECT_NOW.md — current facts that override old journal distillations."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CORE = Path(r"C:\Empire_Workbench\00_Core_Profile")
NOW_FILE = CORE / "ARCHITECT_NOW.md"
MAX_FILE_CHARS = 8_000
MAX_FACT_CHARS = 500


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _read() -> str:
    try:
        if NOW_FILE.is_file():
            return NOW_FILE.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        pass
    return ""


def _write(text: str) -> None:
    CORE.mkdir(parents=True, exist_ok=True)
    if len(text) > MAX_FILE_CHARS:
        text = text[: MAX_FILE_CHARS - 1].rstrip() + "…\n"
    NOW_FILE.write_text(text, encoding="utf-8")


def show() -> dict[str, object]:
    body = _read().strip()
    return {
        "ok": True,
        "path": str(NOW_FILE),
        "exists": bool(body),
        "text": body,
        "chars": len(body),
    }


def update(fact: str, *, replace_all: bool = False) -> dict[str, object]:
    cleaned = re.sub(r"\s+", " ", (fact or "").strip())
    if not cleaned:
        return {"ok": False, "error": "fact required"}
    if len(cleaned) > MAX_FACT_CHARS:
        cleaned = cleaned[: MAX_FACT_CHARS - 1].rstrip() + "…"

    stamp = _utc()
    if replace_all:
        text = (
            "# Architect — current facts (living)\n\n"
            "These beat old journal distillations. Eve must treat this as **now**.\n\n"
            f"- {cleaned}\n\n"
            f"_Updated {stamp}_\n"
        )
        _write(text)
        return {"ok": True, "path": str(NOW_FILE), "mode": "replace", "fact": cleaned}

    existing = _read().strip()
    if not existing:
        existing = (
            "# Architect — current facts (living)\n\n"
            "These beat old journal distillations. Eve must treat this as **now**.\n"
        )
    # Dedupe exact bullet
    bullet = f"- {cleaned}"
    if bullet in existing:
        return {
            "ok": True,
            "path": str(NOW_FILE),
            "mode": "unchanged",
            "fact": cleaned,
        }
    # Strip trailing "Updated" line then append
    lines = [ln for ln in existing.splitlines() if not ln.startswith("_Updated")]
    body = "\n".join(lines).rstrip() + f"\n{bullet}\n\n_Updated {stamp}_\n"
    _write(body)
    return {"ok": True, "path": str(NOW_FILE), "mode": "append", "fact": cleaned}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update ARCHITECT_NOW living facts")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show", help="Print current NOW file as JSON")
    up = sub.add_parser("update", help="Append or replace a durable fact")
    up.add_argument("fact", type=str)
    up.add_argument(
        "--replace-all",
        action="store_true",
        help="Replace entire NOW file with a single fact block",
    )
    args = parser.parse_args(argv)
    if args.command == "show":
        print(json.dumps(show()))
        return 0
    if args.command == "update":
        print(json.dumps(update(args.fact, replace_all=args.replace_all)))
        return 0
    raise SystemExit(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
