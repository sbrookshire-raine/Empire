"""DAZE day-block helpers — PocketBase CRUD + free-window math (Phase 5)."""

from __future__ import annotations

import json
import os
import re
from datetime import date, datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, quote, urlencode, urlparse
from urllib.request import Request, urlopen

POCKETBASE_URL = os.environ.get("POCKETBASE_URL", "http://127.0.0.1:8090").rstrip("/")
COLLECTION = "day_blocks"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
KINDS = ("focus", "body", "admin", "creative", "rest", "other")
PHASES = ("planned", "actual")
DEFAULT_COLORS = {
    "focus": "#5b8def",
    "body": "#3ecf8e",
    "admin": "#c9a227",
    "creative": "#c084fc",
    "rest": "#94a3b8",
    "other": "#f97316",
}


def _today_local() -> str:
    return date.today().isoformat()


def normalize_day(day: str | None) -> tuple[str | None, str | None]:
    """Resolve YYYY-MM-DD; empty/today/now -> local today."""
    if day is None:
        return _today_local(), None
    cleaned = str(day).strip()
    if not cleaned:
        return _today_local(), None
    lowered = cleaned.lower()
    if lowered in {"today", "now", "current"}:
        return _today_local(), None
    if DATE_RE.fullmatch(cleaned):
        return cleaned, None
    return None, "date must be YYYY-MM-DD (omit the parameter for today)"


def _pb(method: str, path: str, body: dict[str, Any] | None = None) -> Any:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(f"{POCKETBASE_URL}{path}", data=data, headers=headers, method=method)
    try:
        with urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8")
            if not raw:
                return None
            return json.loads(raw)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"PocketBase HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"PocketBase unreachable at {POCKETBASE_URL}: {exc}") from exc


def validate_block_payload(payload: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    day_raw = payload.get("date")
    day, day_err = normalize_day(str(day_raw) if day_raw is not None else None)
    if day_err or not day:
        return None, day_err or "date must be YYYY-MM-DD"
    title = str(payload.get("title") or "").strip()
    if not title:
        return None, "title is required"
    try:
        start = int(payload.get("start_minute"))
        end = int(payload.get("end_minute"))
    except (TypeError, ValueError):
        return None, "start_minute and end_minute must be integers"
    if not (0 <= start < 1440 and 0 < end <= 1440 and end > start):
        return None, "minutes must satisfy 0 <= start < end <= 1440"
    kind = str(payload.get("kind") or "focus").strip().lower()
    if kind not in KINDS:
        return None, f"kind must be one of {', '.join(KINDS)}"
    phase = str(payload.get("phase") or "planned").strip().lower()
    if phase not in PHASES:
        return None, f"phase must be one of {', '.join(PHASES)}"
    notes = str(payload.get("notes") or "").strip()
    color = str(payload.get("color") or DEFAULT_COLORS.get(kind, "#5b8def")).strip()
    return {
        "date": day,
        "title": title[:255],
        "start_minute": start,
        "end_minute": end,
        "kind": kind,
        "phase": phase,
        "notes": notes[:5000],
        "color": color[:32],
    }, None


def list_day(day: str | None = None, phase: str | None = None) -> dict[str, Any]:
    day_s, day_err = normalize_day(day)
    if day_err or not day_s:
        return {"ok": False, "error": day_err or "date must be YYYY-MM-DD", "items": []}
    filt = f'date = "{day_s}"'
    if phase:
        phase_s = phase.strip().lower()
        if phase_s not in PHASES:
            return {"ok": False, "error": f"phase must be one of {', '.join(PHASES)}", "items": []}
        filt += f' && phase = "{phase_s}"'
    params = urlencode(
        {
            "filter": filt,
            "sort": "start_minute",
            "perPage": "200",
        }
    )
    try:
        data = _pb("GET", f"/api/collections/{COLLECTION}/records?{params}")
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "items": []}
    items = data.get("items") if isinstance(data, dict) else []
    return {
        "ok": True,
        "date": day_s,
        "count": len(items or []),
        "items": items or [],
        "conflicts": find_conflicts(items or []),
    }


def upsert_block(payload: dict[str, Any], record_id: str = "") -> dict[str, Any]:
    cleaned, err = validate_block_payload(payload)
    if err or cleaned is None:
        return {"ok": False, "error": err or "invalid payload"}
    try:
        if record_id.strip():
            record = _pb(
                "PATCH",
                f"/api/collections/{COLLECTION}/records/{quote(record_id.strip())}",
                cleaned,
            )
        else:
            record = _pb("POST", f"/api/collections/{COLLECTION}/records", cleaned)
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "record": record}


def delete_block(record_id: str) -> dict[str, Any]:
    rid = record_id.strip()
    if not rid:
        return {"ok": False, "error": "record_id is required"}
    try:
        _pb("DELETE", f"/api/collections/{COLLECTION}/records/{quote(rid)}")
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}
    return {"ok": True, "deleted": rid}


def find_conflicts(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    conflicts: list[dict[str, Any]] = []
    sorted_items = sorted(
        items,
        key=lambda x: (int(x.get("start_minute") or 0), int(x.get("end_minute") or 0)),
    )
    for i, a in enumerate(sorted_items):
        a0, a1 = int(a.get("start_minute") or 0), int(a.get("end_minute") or 0)
        for b in sorted_items[i + 1 :]:
            b0, b1 = int(b.get("start_minute") or 0), int(b.get("end_minute") or 0)
            if b0 >= a1:
                break
            if a0 < b1 and b0 < a1:
                conflicts.append(
                    {
                        "a_id": a.get("id"),
                        "b_id": b.get("id"),
                        "a_title": a.get("title"),
                        "b_title": b.get("title"),
                        "overlap_start": max(a0, b0),
                        "overlap_end": min(a1, b1),
                    }
                )
    return conflicts


def free_windows(
    day: str | None = None,
    phase: str = "planned",
    min_minutes: int = 30,
) -> dict[str, Any]:
    listed = list_day(day=day, phase=phase)
    if not listed.get("ok"):
        return listed
    items = listed.get("items") or []
    occupied = sorted(
        (
            (int(x.get("start_minute") or 0), int(x.get("end_minute") or 0))
            for x in items
        ),
        key=lambda p: p[0],
    )
    merged: list[list[int]] = []
    for start, end in occupied:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    free: list[dict[str, Any]] = []
    cursor = 0
    min_m = max(1, int(min_minutes))
    for start, end in merged:
        if start - cursor >= min_m:
            free.append(
                {
                    "start_minute": cursor,
                    "end_minute": start,
                    "minutes": start - cursor,
                    "label": f"{_fmt(cursor)}–{_fmt(start)}",
                }
            )
        cursor = max(cursor, end)
    if 1440 - cursor >= min_m:
        free.append(
            {
                "start_minute": cursor,
                "end_minute": 1440,
                "minutes": 1440 - cursor,
                "label": f"{_fmt(cursor)}–{_fmt(1440)}",
            }
        )
    return {
        "ok": True,
        "date": listed.get("date"),
        "phase": phase,
        "min_minutes": min_m,
        "free": free,
        "conflicts": listed.get("conflicts") or [],
        "note": (
            "Free windows are gaps between blocks. "
            "Promote body/meditation into these arcs when coaching."
        ),
        "fetched_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }


def _fmt(minute: int) -> str:
    m = max(0, min(1440, int(minute)))
    if m == 1440:
        return "24:00"
    return f"{m // 60:02d}:{m % 60:02d}"


def compare_phases(day: str | None = None) -> dict[str, Any]:
    """Planned vs actual summary for Eve coaching (no PocketBase schema change)."""
    day_s, day_err = normalize_day(day)
    if day_err or not day_s:
        return {"ok": False, "error": day_err or "date must be YYYY-MM-DD"}
    planned = list_day(day=day_s, phase="planned")
    actual = list_day(day=day_s, phase="actual")
    if not planned.get("ok") or not actual.get("ok"):
        return {
            "ok": False,
            "error": planned.get("error") or actual.get("error") or "list failed",
        }
    planned_free = free_windows(day=day_s, phase="planned", min_minutes=30)
    actual_free = free_windows(day=day_s, phase="actual", min_minutes=30)
    planned_items = planned.get("items") or []
    actual_items = actual.get("items") or []
    body_planned = sum(
        1 for x in planned_items if str(x.get("kind") or "").lower() in {"body", "rest"}
    )
    body_actual = sum(
        1 for x in actual_items if str(x.get("kind") or "").lower() in {"body", "rest"}
    )
    coaching: list[str] = []
    if body_planned > body_actual:
        coaching.append(
            f"Planned includes {body_planned} body/rest block(s) but actual only has {body_actual} — check if exercise or meditation slipped."
        )
    if (planned.get("conflicts") or []) and not (actual.get("conflicts") or []):
        coaching.append(
            "Planned day is overbooked but actual is not — good chance to simplify the plan."
        )
    if (actual.get("conflicts") or []) and not (planned.get("conflicts") or []):
        coaching.append(
            "Actual day has overlaps that planned did not — schedule drift or ad-hoc stacking."
        )
    if planned_free.get("free") and not coaching:
        best = max(planned_free["free"], key=lambda w: int(w.get("minutes") or 0))
        coaching.append(
            f"Largest planned free window: {best.get('label')} ({best.get('minutes')} min) — candidate for body or rest."
        )
    return {
        "ok": True,
        "date": day_s,
        "planned": {
            "count": len(planned_items),
            "conflicts": planned.get("conflicts") or [],
            "free": planned_free.get("free") or [],
        },
        "actual": {
            "count": len(actual_items),
            "conflicts": actual.get("conflicts") or [],
            "free": actual_free.get("free") or [],
        },
        "coaching": coaching,
        "empire_url": "http://127.0.0.1:8080/daze.html",
        "fetched_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }


def handle_api(method: str, path: str, payload: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
    """HTTP adapter for frontend static server (/api/daze/*)."""
    parsed = urlparse(path)
    params = {key: values[0] for key, values in parse_qs(parsed.query).items()}
    route = parsed.path.rstrip("/")
    if method == "GET" and route == "/api/daze/day":
        phase = params.get("phase") or ""
        day = params.get("date") or None
        if phase == "both":
            planned = list_day(day=day, phase="planned")
            actual = list_day(day=day, phase="actual")
            if not planned.get("ok") or not actual.get("ok"):
                return 502, {
                    "ok": False,
                    "error": planned.get("error") or actual.get("error") or "list failed",
                }
            return 200, {
                "ok": True,
                "date": planned.get("date") or actual.get("date"),
                "phase": "both",
                "planned": planned.get("items") or [],
                "actual": actual.get("items") or [],
                "planned_conflicts": planned.get("conflicts") or [],
                "actual_conflicts": actual.get("conflicts") or [],
            }
        return 200, list_day(day=day, phase=phase or None)

    if method == "GET" and route == "/api/daze/free":
        return 200, free_windows(
            day=params.get("date") or None,
            phase=params.get("phase") or "planned",
            min_minutes=int(params.get("min_minutes") or 30),
        )

    if method == "GET" and route == "/api/daze/compare":
        return 200, compare_phases(day=params.get("date") or None)

    if method == "POST" and route == "/api/daze/block":
        body = payload or {}
        record_id = str(body.get("id") or body.get("record_id") or "").strip()
        return 200, upsert_block(body, record_id=record_id)

    if method == "DELETE" and route == "/api/daze/block":
        record_id = params.get("id") or str((payload or {}).get("id") or "")
        if not record_id:
            return 400, {"ok": False, "error": "id query param required"}
        return 200, delete_block(record_id)

    return 404, {"ok": False, "error": f"unknown daze route: {route}"}
