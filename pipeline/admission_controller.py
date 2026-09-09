"""Session-scoped capability admission for Research Autopilot.

Merges manual Toolbelt choices with TTL session grants. Never auto-promotes
to Cognee or mutates manual eve-toolbelt.json.
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

from frontend import eve_toolbelt
from pipeline import gpu_lease

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "config" / "capability-manifest.json"
DEFAULT_SESSION = ROOT / "config" / "eve-capability-session.json"
WEAVIATE_READY_URL = "http://127.0.0.1:8091/v1/.well-known/ready"
WEAVIATE_API_KEY = os.environ.get(
    "WEAVIATE_API_KEY",
    "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih",
)
WEAVIATE_START_TIMEOUT_SEC = int(os.environ.get("EMPIRE_WEAVIATE_START_TIMEOUT", "120"))


def _utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def _utc_now_iso() -> str:
    return _utc_now().isoformat()


def _empire_dir() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder
        except OSError:
            pass
    folder = ROOT / "config"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def session_path() -> Path:
    return _empire_dir() / "eve-capability-session.json"


def manifest_path() -> Path:
    env = os.environ.get("EMPIRE_CAPABILITY_MANIFEST", "").strip()
    if env:
        return Path(env)
    return DEFAULT_MANIFEST


def _atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2) + "\n"
    handle, tmp_name = tempfile.mkstemp(prefix="cap-", suffix=".json", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def _load_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return dict(fallback)
    return data if isinstance(data, dict) else dict(fallback)


def load_manifest() -> dict[str, Any]:
    raw = _load_json(manifest_path(), {"categories": {}, "max_session_capabilities": 4})
    categories = raw.get("categories")
    if not isinstance(categories, dict):
        raw["categories"] = {}
    return raw


def category_meta(category: str) -> dict[str, Any] | None:
    manifest = load_manifest()
    categories = manifest.get("categories")
    if not isinstance(categories, dict):
        return None
    meta = categories.get(category)
    return meta if isinstance(meta, dict) else None


def load_session() -> dict[str, Any]:
    path = session_path()
    if not path.exists() and DEFAULT_SESSION.exists():
        try:
            _atomic_write(path, _load_json(DEFAULT_SESSION, _empty_session()))
        except OSError:
            pass
    return _load_json(path, _empty_session())


def _empty_session() -> dict[str, Any]:
    return {
        "research_partner_mode": False,
        "session_capabilities": [],
        "expires_at": "",
        "started_at": "",
        "last_reason": "",
    }


def _parse_iso(value: str) -> datetime | None:
    cleaned = (value or "").strip()
    if not cleaned:
        return None
    try:
        return datetime.fromisoformat(cleaned.replace("Z", "+00:00"))
    except ValueError:
        return None


def expire_stale() -> dict[str, Any]:
    session = load_session()
    expires = _parse_iso(str(session.get("expires_at") or ""))
    caps = session.get("session_capabilities")
    if not isinstance(caps, list):
        caps = []
    if expires and _utc_now() >= expires and caps:
        session["session_capabilities"] = []
        session["expires_at"] = ""
        session["last_reason"] = "ttl_expired"
        try:
            _atomic_write(session_path(), session)
        except OSError:
            pass
        gpu_lease.append_audit(
            "capability_session_expired",
            detail={"previous": caps},
        )
        return {"ok": True, "expired": True, "previous": caps}
    return {"ok": True, "expired": False}


def research_partner_enabled() -> bool:
    expire_stale()
    session = load_session()
    return bool(session.get("research_partner_mode"))


def set_research_partner(enabled: bool) -> dict[str, Any]:
    session = load_session()
    session["research_partner_mode"] = bool(enabled)
    if not enabled:
        session["session_capabilities"] = []
        session["expires_at"] = ""
        session["last_reason"] = "partner_mode_off"
    try:
        _atomic_write(session_path(), session)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    gpu_lease.append_audit(
        "research_partner_mode",
        detail={"enabled": bool(enabled)},
    )
    return {
        "ok": True,
        "research_partner_mode": bool(enabled),
        "path": str(session_path()),
    }


def _session_active(category: str) -> bool:
    expire_stale()
    session = load_session()
    if not session.get("research_partner_mode"):
        return False
    caps = session.get("session_capabilities")
    if not isinstance(caps, list) or category not in caps:
        return False
    expires = _parse_iso(str(session.get("expires_at") or ""))
    if expires and _utc_now() >= expires:
        return False
    return True


def capability_active(category: str) -> bool:
    cleaned = (category or "").strip()
    if not cleaned:
        return False
    if cleaned not in eve_toolbelt.ALLOWED_CATEGORIES:
        return False
    if eve_toolbelt.category_enabled(cleaned):
        return True
    return _session_active(cleaned)


def load_effective_tools() -> list[str]:
    manual = eve_toolbelt.load_active_tools()
    expire_stale()
    session = load_session()
    caps = session.get("session_capabilities")
    if not isinstance(caps, list) or not session.get("research_partner_mode"):
        return manual
    expires = _parse_iso(str(session.get("expires_at") or ""))
    if expires and _utc_now() >= expires:
        return manual
    merged: list[str] = []
    for item in manual + caps:
        if isinstance(item, str) and item in eve_toolbelt.ALLOWED_CATEGORIES and item not in merged:
            merged.append(item)
    return merged


def _http_ready(url: str, *, headers: dict[str, str] | None = None, timeout: float = 5.0) -> bool:
    try:
        req = Request(url, headers=headers or {})
        with urlopen(req, timeout=timeout) as resp:
            return 200 <= int(getattr(resp, "status", 200) or 200) < 400
    except (URLError, OSError, ValueError):
        return False


def _ensure_weaviate() -> dict[str, Any]:
    headers = {"Authorization": f"Bearer {WEAVIATE_API_KEY}"}
    if _http_ready(WEAVIATE_READY_URL, headers=headers):
        return {"ok": True, "already_running": True}
    script = ROOT / "scripts" / "start-weaviate.ps1"
    if not script.is_file():
        return {"ok": False, "error": f"start script missing: {script}"}
    try:
        completed = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(script),
            ],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=WEAVIATE_START_TIMEOUT_SEC,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "Weaviate start timed out"}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    if _http_ready(WEAVIATE_READY_URL, headers=headers):
        return {
            "ok": True,
            "started": True,
            "exit_code": completed.returncode,
        }
    stderr = (completed.stderr or "").strip()[:400]
    return {
        "ok": False,
        "error": "Weaviate not ready after start script",
        "exit_code": completed.returncode,
        "detail": stderr,
    }


def _preflight(category: str, meta: dict[str, Any]) -> dict[str, Any]:
    snap = gpu_lease._resource_snapshot()
    min_disk = float(meta.get("min_disk_free_gb") or 0)
    disk_free = snap.get("disk_free_gb")
    if min_disk and isinstance(disk_free, (int, float)) and disk_free < min_disk:
        return {
            "ok": False,
            "error": f"Disk free {disk_free} GB below minimum {min_disk} GB for {category}",
        }
    gpu_tenant = str(meta.get("gpu_tenant") or "none")
    if gpu_tenant not in {"", "none", "idle"}:
        lease = gpu_lease.status()
        active = str(lease.get("tenant") or "idle")
        if active not in {"idle", gpu_tenant}:
            return {
                "ok": False,
                "error": f"GPU leased to {active}; cannot admit {category} ({gpu_tenant})",
                "gpu_lease": lease,
            }
    services = meta.get("requires_services")
    if isinstance(services, list):
        for svc in services:
            if not isinstance(svc, str):
                continue
            if svc == "weaviate:8091":
                weav = _ensure_weaviate()
                if not weav.get("ok"):
                    return weav
    return {"ok": True, "resources": snap}


def request_capability(
    category: str,
    reason: str = "",
    *,
    ttl_min: int | None = None,
    bypass_partner_check: bool = False,
) -> dict[str, Any]:
    cleaned = (category or "").strip()
    if cleaned not in eve_toolbelt.ALLOWED_CATEGORIES:
        return {"ok": False, "error": f"Unknown category: {cleaned}"}
    meta = category_meta(cleaned)
    if not meta:
        return {"ok": False, "error": f"No manifest entry for {cleaned}"}
    if not bypass_partner_check and not research_partner_enabled():
        if not eve_toolbelt.category_enabled(cleaned):
            return {
                "ok": False,
                "error": "Research Partner mode is off — enable it or toggle Toolbelt manually.",
                "category": cleaned,
            }
    if eve_toolbelt.category_enabled(cleaned):
        return {
            "ok": True,
            "category": cleaned,
            "source": "manual_toolbelt",
            "already_active": True,
        }
    if not meta.get("auto_enable"):
        return {
            "ok": False,
            "error": f"{cleaned} cannot be auto-enabled — use manual Toolbelt.",
            "category": cleaned,
        }
    expire_stale()
    session = load_session()
    caps = session.get("session_capabilities")
    if not isinstance(caps, list):
        caps = []
    manifest = load_manifest()
    max_caps = int(manifest.get("max_session_capabilities") or 4)
    if cleaned not in caps and len(caps) >= max_caps:
        return {
            "ok": False,
            "error": f"Session cap {max_caps} reached — release or wait for TTL.",
            "session_capabilities": caps,
        }
    preflight = _preflight(cleaned, meta)
    if not preflight.get("ok"):
        gpu_lease.append_audit(
            "capability_request_denied",
            detail={"category": cleaned, "reason": reason, **preflight},
        )
        return {**preflight, "category": cleaned}

    default_ttl = int(meta.get("session_ttl_min") or 30)
    ttl = ttl_min if ttl_min is not None else default_ttl
    ttl = max(5, min(ttl, 120))
    now = _utc_now()
    expires = now + timedelta(minutes=ttl)
    if not caps:
        session["started_at"] = now.isoformat()
    if cleaned not in caps:
        caps.append(cleaned)
    session["session_capabilities"] = caps
    session["expires_at"] = expires.isoformat()
    session["last_reason"] = (reason or f"admit {cleaned}")[:500]
    try:
        _atomic_write(session_path(), session)
    except OSError as exc:
        return {"ok": False, "error": str(exc), "category": cleaned}

    gpu_lease.append_audit(
        "capability_request_ok",
        detail={
            "category": cleaned,
            "reason": reason,
            "ttl_min": ttl,
            "expires_at": session["expires_at"],
            "preflight": preflight,
        },
    )
    return {
        "ok": True,
        "category": cleaned,
        "source": "session",
        "session_capabilities": caps,
        "expires_at": session["expires_at"],
        "ttl_min": ttl,
        "preflight": preflight,
    }


def release_session(reason: str = "manual") -> dict[str, Any]:
    session = load_session()
    previous = list(session.get("session_capabilities") or [])
    session["session_capabilities"] = []
    session["expires_at"] = ""
    session["last_reason"] = (reason or "released")[:500]
    try:
        _atomic_write(session_path(), session)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    gpu_lease.append_audit(
        "capability_session_released",
        detail={"reason": reason, "previous": previous},
    )
    return {"ok": True, "released": previous, "reason": reason}


def status() -> dict[str, Any]:
    expire_stale()
    session = load_session()
    manifest = load_manifest()
    manual = eve_toolbelt.load_active_tools()
    effective = load_effective_tools()
    expires = str(session.get("expires_at") or "")
    expires_dt = _parse_iso(expires)
    ttl_remaining_sec = 0
    if expires_dt and expires_dt > _utc_now():
        ttl_remaining_sec = int((expires_dt - _utc_now()).total_seconds())
    return {
        "ok": True,
        "research_partner_mode": bool(session.get("research_partner_mode")),
        "session_capabilities": list(session.get("session_capabilities") or []),
        "manual_toolbelt": manual,
        "effective_tools": effective,
        "expires_at": expires,
        "ttl_remaining_sec": ttl_remaining_sec,
        "started_at": str(session.get("started_at") or ""),
        "last_reason": str(session.get("last_reason") or ""),
        "gpu_lease": gpu_lease.status(),
        "resources": gpu_lease._resource_snapshot(),
        "session_path": str(session_path()),
        "manifest_path": str(manifest_path()),
        "max_session_capabilities": int(manifest.get("max_session_capabilities") or 4),
    }


def handle_api_action(payload: dict[str, Any]) -> dict[str, Any]:
    action = str(payload.get("action") or "").strip().lower()
    if action == "request":
        ttl_raw = payload.get("ttl_min")
        ttl_min = int(ttl_raw) if isinstance(ttl_raw, (int, float)) else None
        return request_capability(
            str(payload.get("category") or ""),
            str(payload.get("reason") or ""),
            ttl_min=ttl_min,
        )
    if action == "release":
        return release_session(str(payload.get("reason") or "api"))
    if action == "set_research_partner":
        enabled = payload.get("enabled")
        if not isinstance(enabled, bool):
            return {"ok": False, "error": "enabled boolean required"}
        return set_research_partner(enabled)
    return {"ok": False, "error": f"Unknown action: {action}"}


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE capability admission")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    active = sub.add_parser("active")
    active.add_argument("category")
    req = sub.add_parser("request")
    req.add_argument("category")
    req.add_argument("--reason", default="")
    req.add_argument("--ttl-min", type=int, default=None)
    rel = sub.add_parser("release")
    rel.add_argument("--reason", default="cli")
    partner = sub.add_parser("set-research-partner")
    partner.add_argument("enabled", choices=("true", "false"))
    args = parser.parse_args(argv)

    if args.command == "status":
        result = status()
    elif args.command == "active":
        result = {"ok": True, "category": args.category, "active": capability_active(args.category)}
    elif args.command == "request":
        result = request_capability(args.category, args.reason, ttl_min=args.ttl_min)
    elif args.command == "release":
        result = release_session(args.reason)
    elif args.command == "set-research-partner":
        result = set_research_partner(args.enabled == "true")
    else:
        raise SystemExit(f"unknown command: {args.command}")

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
