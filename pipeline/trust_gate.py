"""Prompt-injection isolation — trust gate for Eve's tool admission.

When a turn consumes untrusted content (public-web fetch, a document a user
pasted, anything carrying instructions that weren't authored by the Architect),
Eve must not auto-acquire write/shell/memory tools in that same turn.

This module is a small, explicit trust ledger: arms that ingest untrusted bytes
call `mark_untrusted()`; the admission path consults `untrusted_active()` and
refuses dangerous (write/shell/memory) admits until the turn resets.

Trust domains (matches docs/EMPIRE_CLARITY.md):
  local_evidence -> read-only (may be marked untrusted if user-supplied)
  public_web     -> always untrusted
  memory         -> write tools are the dangerous ones; never auto from untrusted
"""

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any

# How long a turn's untrusted flag stays hot (seconds). Long enough to cover a
# single multi-step turn without leaking into the next Architect turn.
DEFAULT_TTL_SEC = int(os.environ.get("EMPIRE_UNTRUSTED_TTL_SEC", "300"))

# Trust domains whose content is considered untrusted-by-default.
UNTRUSTED_DOMAINS: frozenset[str] = frozenset({"public_web"})

# Tool categories that must NOT be auto-acquired while untrusted content is hot.
DANGEROUS_CATEGORIES: frozenset[str] = frozenset(
    {
        "tool_forge",          # writes Active Tools
        "author_code",         # writes code
        "create_spreadsheet",  # writes artifacts (lower risk, but still a write)
        "structured_extract",  # writes scratch from arbitrary docs
        "loom_intake",         # promotes into ledger
    }
)

_MEMORY_TOOLS: frozenset[str] = frozenset(
    {"cognee_remember", "cognee_improve", "wiki_remember", "remember_wiki_lead", "confirm_remember"}
)


def state_path() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
    else:
        folder = Path(__file__).resolve().parents[1] / "config"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "untrusted-turn.json"


def mark_untrusted(*, domain: str = "public_web", reason: str = "") -> dict[str, Any]:
    """Flag that the current turn is consuming untrusted content."""
    payload = {
        "untrusted": True,
        "domain": domain,
        "reason": (reason or "")[:300],
        "expires_at": time.time() + DEFAULT_TTL_SEC,
    }
    try:
        import json

        state_path().write_text(json.dumps(payload), encoding="utf-8")
    except OSError:
        pass
    return {"ok": True, "untrusted": True, "expires_sec": DEFAULT_TTL_SEC}


def reset() -> dict[str, Any]:
    try:
        import json

        state_path().write_text(json.dumps({"untrusted": False, "expires_at": 0}), encoding="utf-8")
    except OSError:
        pass
    return {"ok": True, "untrusted": False}


def untrusted_active() -> bool:
    try:
        import json

        data = json.loads(state_path().read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    if not isinstance(data, dict) or not data.get("untrusted"):
        return False
    expires = data.get("expires_at") or 0
    if isinstance(expires, (int, float)) and time.time() >= float(expires):
        return False
    return True


def can_admit_dangerous(category: str) -> bool:
    """Dangerous (write/shell) categories are blocked while untrusted is hot."""
    cleaned = (category or "").strip()
    if cleaned not in DANGEROUS_CATEGORIES and cleaned not in {"author_code"}:
        return True
    return not untrusted_active()


def is_memory_tool(tool_name: str) -> bool:
    return (tool_name or "").strip() in _MEMORY_TOOLS


def gate_memory_tool(tool_name: str) -> dict[str, Any]:
    """Refuse memory writes during an untrusted turn (defense in depth)."""
    if is_memory_tool(tool_name) and untrusted_active():
        return {
            "ok": False,
            "blocked": True,
            "reason": "untrusted content active — refuse memory write this turn",
        }
    return {"ok": True, "blocked": False}


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Prompt-injection trust gate")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    mark = sub.add_parser("mark")
    mark.add_argument("--domain", default="public_web")
    mark.add_argument("--reason", default="")
    sub.add_parser("reset")
    args = parser.parse_args(argv)

    if args.cmd == "status":
        out = {"untrusted": untrusted_active()}
    elif args.cmd == "mark":
        out = mark_untrusted(domain=args.domain, reason=args.reason)
    elif args.cmd == "reset":
        out = reset()
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
