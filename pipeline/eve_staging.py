"""Eve staging memory — propose → confirm/drop with TTL.

Eve may write to eve_staging freely. Permanence into eve_memory / eve_core
requires Architect confirm. See docs/EMPIRE_CLARITY.md.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

STAGING_DATASET = "eve_staging"
DEFAULT_TARGET = "eve_memory"
ALLOWED_CONFIRM_TARGETS = frozenset({"eve_memory", "eve_core"})
TTL_HOURS_DEFAULT = 72
SCHEMA_VERSION = 1


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_iso(raw: str) -> datetime | None:
    text = (raw or "").strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def staging_dir() -> Path:
    override = os.environ.get("EMPIRE_EVE_STAGING_DIR", "").strip()
    if override:
        path = Path(override)
    else:
        path = Path(
            r"C:\Empire_Workbench\04_Thought_Experiments\eve_staging"
        )
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        logger.warning("eve_staging dir create failed: %s", exc)
    return path


def ledger_path() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder / "eve_staging_ledger.json"
        except OSError:
            pass
    return staging_dir() / "ledger.json"


def ttl_hours() -> int:
    raw = os.environ.get("EMPIRE_EVE_STAGING_TTL_HOURS", str(TTL_HOURS_DEFAULT)).strip()
    try:
        return max(1, min(24 * 30, int(raw)))
    except ValueError:
        return TTL_HOURS_DEFAULT


def _load_ledger() -> dict[str, Any]:
    path = ledger_path()
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema_version": SCHEMA_VERSION, "entries": []}
    if not isinstance(parsed, dict):
        return {"schema_version": SCHEMA_VERSION, "entries": []}
    entries = parsed.get("entries")
    if not isinstance(entries, list):
        entries = []
    return {"schema_version": SCHEMA_VERSION, "entries": entries}


def _save_ledger(ledger: dict[str, Any]) -> None:
    path = ledger_path()
    try:
        path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except OSError as exc:
        logger.warning("eve_staging ledger write failed: %s", exc)


def _entry_path(entry_id: str) -> Path:
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", entry_id).strip("_")[:64] or "entry"
    return staging_dir() / f"{safe}.md"


def _find_entry(ledger: dict[str, Any], entry_id: str) -> dict[str, Any] | None:
    for item in ledger.get("entries") or []:
        if isinstance(item, dict) and str(item.get("id") or "") == entry_id:
            return item
    return None


def propose_remember(
    content: str,
    *,
    reason: str = "",
    crumb: str = "",
    source: str = "eve",
) -> dict[str, Any]:
    """Stage content into eve_staging (file + Cognee). Does not touch eve_memory."""
    from pipeline.cognee_client import remember
    from pipeline.wiki_scout import allowed_promote_datasets

    text = (content or "").strip()
    if not text:
        return {"ok": False, "error": "empty content"}
    if len(text) > 8000:
        text = text[:7997].rstrip() + "…"

    if STAGING_DATASET not in allowed_promote_datasets():
        return {
            "ok": False,
            "error": f"{STAGING_DATASET} not in allowed promote datasets — update config/wiki-promote.json",
        }

    entry_id = f"stg_{uuid.uuid4().hex[:16]}"
    now = _utc_now()
    expires = now + timedelta(hours=ttl_hours())
    reason_clean = (reason or "").strip()[:400]
    crumb_clean = (crumb or "").strip()[:200]

    body = (
        f"# Eve staging proposal\n\n"
        f"id: {entry_id}\n"
        f"dataset: {STAGING_DATASET}\n"
        f"proposed_at: {_iso(now)}\n"
        f"expires_at: {_iso(expires)}\n"
        f"source: {(source or 'eve').strip()[:80]}\n"
        f"reason: {reason_clean or '(none)'}\n"
        f"crumb: {crumb_clean or '(none)'}\n\n"
        f"{text}\n"
    )
    path = _entry_path(entry_id)
    try:
        path.write_text(body, encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": f"staging write failed: {exc}"}

    try:
        import asyncio

        asyncio.run(remember(body, dataset=STAGING_DATASET))
    except Exception as exc:  # noqa: BLE001
        logger.warning("eve_staging cognee remember failed: %s", exc)
        # Keep file ledger even if Cognee is cold — confirm can re-remember.
        cognee_ok = False
        cognee_error = str(exc)[:240]
    else:
        cognee_ok = True
        cognee_error = None

    entry = {
        "id": entry_id,
        "path": str(path),
        "proposed_at": _iso(now),
        "expires_at": _iso(expires),
        "reason": reason_clean,
        "crumb": crumb_clean,
        "source": (source or "eve").strip()[:80],
        "status": "proposed",
        "chars": len(text),
        "cognee_ok": cognee_ok,
    }
    ledger = _load_ledger()
    entries = [e for e in (ledger.get("entries") or []) if isinstance(e, dict)]
    entries.insert(0, entry)
    ledger["entries"] = entries[:200]
    _save_ledger(ledger)

    out: dict[str, Any] = {
        "ok": True,
        "state": "proposed",
        "entry_id": entry_id,
        "dataset": STAGING_DATASET,
        "expires_at": entry["expires_at"],
        "path": str(path),
        "message": "Staged. Ask the Architect to confirm (keep) or drop before it expires.",
    }
    if cognee_error:
        out["cognee_warning"] = cognee_error
    return out


def list_staging(*, include_expired: bool = False) -> dict[str, Any]:
    ledger = _load_ledger()
    now = _utc_now()
    items: list[dict[str, Any]] = []
    for entry in ledger.get("entries") or []:
        if not isinstance(entry, dict):
            continue
        status = str(entry.get("status") or "proposed")
        if status not in {"proposed", "expired"} and not include_expired:
            if status in {"confirmed", "dropped"}:
                continue
        exp = _parse_iso(str(entry.get("expires_at") or ""))
        expired = bool(exp and exp <= now and status == "proposed")
        if expired:
            entry = {**entry, "status": "expired"}
        if not include_expired and entry.get("status") in {"confirmed", "dropped"}:
            continue
        if not include_expired and entry.get("status") == "expired" and not include_expired:
            # still show expired so Architect can drop
            pass
        items.append(
            {
                "id": entry.get("id"),
                "status": entry.get("status"),
                "proposed_at": entry.get("proposed_at"),
                "expires_at": entry.get("expires_at"),
                "reason": entry.get("reason"),
                "crumb": entry.get("crumb"),
                "chars": entry.get("chars"),
                "path": entry.get("path"),
            }
        )
    return {"ok": True, "count": len(items), "entries": items, "dataset": STAGING_DATASET}


def confirm_remember(
    entry_id: str,
    *,
    target_dataset: str = DEFAULT_TARGET,
) -> dict[str, Any]:
    """Promote a staging entry into eve_memory or eve_core."""
    from pipeline.cognee_client import remember
    from pipeline.wiki_scout import allowed_promote_datasets

    eid = (entry_id or "").strip()
    if not eid:
        return {"ok": False, "error": "entry_id required"}
    target = (target_dataset or DEFAULT_TARGET).strip() or DEFAULT_TARGET
    if target not in ALLOWED_CONFIRM_TARGETS:
        return {
            "ok": False,
            "error": f"target_dataset must be one of: {', '.join(sorted(ALLOWED_CONFIRM_TARGETS))}",
        }
    if target not in allowed_promote_datasets():
        return {"ok": False, "error": f"dataset not allowed: {target}"}

    ledger = _load_ledger()
    entry = _find_entry(ledger, eid)
    if entry is None:
        return {"ok": False, "error": f"unknown entry_id: {eid}"}
    if str(entry.get("status") or "") not in {"proposed", "expired"}:
        return {"ok": False, "error": f"entry status is {entry.get('status')}, not proposed"}

    path = Path(str(entry.get("path") or _entry_path(eid)))
    try:
        body = path.read_text(encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": f"cannot read staging file: {exc}"}

    try:
        import asyncio

        asyncio.run(remember(body, dataset=target))
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": f"cognee remember failed: {exc}"}

    now = _utc_now()
    for item in ledger.get("entries") or []:
        if isinstance(item, dict) and item.get("id") == eid:
            item["status"] = "confirmed"
            item["confirmed_at"] = _iso(now)
            item["target_dataset"] = target
            break
    _save_ledger(ledger)

    return {
        "ok": True,
        "state": "confirmed",
        "entry_id": eid,
        "dataset": target,
        "message": f"Kept in {target}. Staging entry marked confirmed.",
    }


def drop_staging(entry_id: str) -> dict[str, Any]:
    eid = (entry_id or "").strip()
    if not eid:
        return {"ok": False, "error": "entry_id required"}
    ledger = _load_ledger()
    entry = _find_entry(ledger, eid)
    if entry is None:
        return {"ok": False, "error": f"unknown entry_id: {eid}"}

    path = Path(str(entry.get("path") or _entry_path(eid)))
    try:
        if path.is_file():
            path.unlink()
    except OSError as exc:
        logger.warning("drop_staging unlink failed: %s", exc)

    now = _utc_now()
    for item in ledger.get("entries") or []:
        if isinstance(item, dict) and item.get("id") == eid:
            item["status"] = "dropped"
            item["dropped_at"] = _iso(now)
            break
    _save_ledger(ledger)
    return {"ok": True, "state": "dropped", "entry_id": eid}


def sweep_expired() -> dict[str, Any]:
    """Mark/drop expired proposed entries (file delete + ledger)."""
    ledger = _load_ledger()
    now = _utc_now()
    swept: list[str] = []
    for item in ledger.get("entries") or []:
        if not isinstance(item, dict):
            continue
        if str(item.get("status") or "") != "proposed":
            continue
        exp = _parse_iso(str(item.get("expires_at") or ""))
        if not exp or exp > now:
            continue
        eid = str(item.get("id") or "")
        path = Path(str(item.get("path") or ""))
        try:
            if path.is_file():
                path.unlink()
        except OSError:
            pass
        item["status"] = "expired"
        item["swept_at"] = _iso(now)
        if eid:
            swept.append(eid)
    _save_ledger(ledger)
    return {"ok": True, "swept": swept, "count": len(swept)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Eve staging memory CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_prop = sub.add_parser("propose", help="Stage content for Architect confirm")
    p_prop.add_argument("--content", required=True)
    p_prop.add_argument("--reason", default="")
    p_prop.add_argument("--crumb", default="")
    p_prop.add_argument("--source", default="eve")

    sub.add_parser("list", help="List open staging entries")

    p_conf = sub.add_parser("confirm", help="Promote staging entry to core memory")
    p_conf.add_argument("entry_id")
    p_conf.add_argument("--dataset", default=DEFAULT_TARGET)

    p_drop = sub.add_parser("drop", help="Drop a staging entry")
    p_drop.add_argument("entry_id")

    sub.add_parser("sweep", help="Expire and remove stale proposals")

    args = parser.parse_args(argv)
    if args.cmd == "propose":
        out = propose_remember(
            args.content, reason=args.reason, crumb=args.crumb, source=args.source
        )
    elif args.cmd == "list":
        out = list_staging()
    elif args.cmd == "confirm":
        out = confirm_remember(args.entry_id, target_dataset=args.dataset)
    elif args.cmd == "drop":
        out = drop_staging(args.entry_id)
    elif args.cmd == "sweep":
        out = sweep_expired()
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
