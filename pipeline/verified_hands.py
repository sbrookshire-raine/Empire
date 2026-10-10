"""Persist mechanic/smoke verification so Eve's pulse can cite proven tool hands."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_PATH = Path(os.environ.get("LOCALAPPDATA", "")) / "EMPIRE" / "eve_hands_verified.json"
MAX_AGE_HOURS = 168  # one week — stale record ignored in pulse


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def record_path() -> Path:
    override = (os.environ.get("EMPIRE_VERIFIED_HANDS_PATH") or "").strip()
    return Path(override) if override else DEFAULT_PATH


def write_verification(
    *,
    checks: list[dict[str, Any]],
    source: str,
    notes: str = "",
) -> dict[str, Any]:
    """Write latest verification snapshot (smoke / playwright / manual)."""
    passed = [c for c in checks if c.get("ok")]
    payload = {
        "ok": len(passed) == len(checks) and bool(checks),
        "verified_at": _utc_now(),
        "source": source,
        "notes": notes.strip(),
        "checks": checks,
        "tools_proven": sorted(
            {
                str(c.get("tool") or "").strip()
                for c in passed
                if str(c.get("tool") or "").strip()
            }
        ),
        "summary": _summary_from_checks(checks),
    }
    path = record_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return payload


def _summary_from_checks(checks: list[dict[str, Any]]) -> str:
    ok_names = [str(c.get("name") or c.get("tool") or "?") for c in checks if c.get("ok")]
    if not ok_names:
        return "No hands verified in last run."
    return "Mechanic verified: " + ", ".join(ok_names[:12]) + ("…" if len(ok_names) > 12 else "") + "."


def load_verification(*, max_age_hours: float = MAX_AGE_HOURS) -> dict[str, Any]:
    path = record_path()
    if not path.is_file():
        return {"ok": False, "reason": "no_verification_file"}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "reason": str(exc)}
    if not isinstance(raw, dict):
        return {"ok": False, "reason": "invalid_format"}
    verified_at = str(raw.get("verified_at") or "")
    if verified_at:
        try:
            ts = datetime.fromisoformat(verified_at.replace("Z", "+00:00"))
            age_h = (datetime.now(timezone.utc) - ts).total_seconds() / 3600.0
            if age_h > max_age_hours:
                return {
                    "ok": False,
                    "reason": "stale",
                    "verified_at": verified_at,
                    "age_hours": round(age_h, 1),
                }
        except ValueError:
            pass
    raw.setdefault("ok", bool(raw.get("checks")))
    return raw


def pulse_snippet() -> str:
    """One-line authoritative note for resource_pulse injection."""
    rec = load_verification()
    if not rec.get("ok"):
        return ""
    tools = rec.get("tools_proven") or []
    summary = str(rec.get("summary") or "").strip()
    at = str(rec.get("verified_at") or "")[:19]
    if not summary:
        return ""
    tool_part = f" Proven tools: {', '.join(tools)}." if tools else ""
    return f"{summary} (as of {at} UTC).{tool_part} Trust these hands; call them when the Architect asks."
