"""Serial GPU lease for EMPIRE (RTX 16GB — one heavy tenant at a time).

Tenants: chat | stem | vision | voice | extract
Admission events append to admission-audit.jsonl for Architect smoke evidence.
"""

from __future__ import annotations

import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

Tenant = Literal["chat", "stem", "vision", "voice", "extract", "idle"]
VALID: frozenset[str] = frozenset({"chat", "stem", "vision", "voice", "extract", "idle"})
ACTIVE_TENANTS: frozenset[str] = frozenset({"chat", "stem", "vision", "voice", "extract"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _empire_dir() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    folder = root / "config"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def lease_path() -> Path:
    return _empire_dir() / "gpu-lease.json"


def audit_path() -> Path:
    return _empire_dir() / "admission-audit.jsonl"


def _atomic_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, indent=2) + "\n"
    handle, tmp_name = tempfile.mkstemp(prefix="gpu-", suffix=".json", dir=str(path.parent))
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


def _resource_snapshot() -> dict[str, Any]:
    snap: dict[str, Any] = {}
    try:
        total, used, free = shutil.disk_usage(str(_empire_dir()))
        snap["disk_free_gb"] = round(free / (1024**3), 2)
        snap["disk_total_gb"] = round(total / (1024**3), 2)
    except OSError:
        pass
    try:
        import psutil  # type: ignore

        snap["ram_available_gb"] = round(psutil.virtual_memory().available / (1024**3), 2)
        snap["ram_total_gb"] = round(psutil.virtual_memory().total / (1024**3), 2)
    except Exception:
        pass
    return snap


def append_audit(event: str, *, detail: dict[str, Any] | None = None) -> None:
    path = audit_path()
    record = {
        "ts": _utc_now(),
        "event": event,
        "detail": detail or {},
        "resources": _resource_snapshot(),
    }
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, default=str) + "\n")
    except OSError:
        # Never crash the stack over audit I/O
        pass


def status() -> dict[str, Any]:
    path = lease_path()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {
            "ok": True,
            "tenant": "idle",
            "holder": "",
            "since": "",
            "note": "No lease file — GPU treated as free.",
            "path": str(path),
            "audit_path": str(audit_path()),
        }
    if not isinstance(raw, dict):
        return {"ok": False, "error": "Invalid lease file", "path": str(path)}
    tenant = str(raw.get("tenant") or "idle").strip()
    if tenant not in VALID:
        tenant = "idle"
    return {
        "ok": True,
        "tenant": tenant,
        "holder": str(raw.get("holder") or ""),
        "since": str(raw.get("since") or ""),
        "note": str(raw.get("note") or ""),
        "path": str(path),
        "audit_path": str(audit_path()),
    }


def acquire(tenant: Tenant, *, holder: str = "", note: str = "", force: bool = False) -> dict[str, Any]:
    if tenant not in ACTIVE_TENANTS:
        result = {"ok": False, "error": f"Invalid tenant: {tenant}"}
        append_audit("acquire_reject", detail=result)
        return result
    current = status()
    active = str(current.get("tenant") or "idle")
    if active not in {"idle", tenant} and not force:
        result = {
            "ok": False,
            "error": f"GPU leased to {active} (holder={current.get('holder')}). "
            "Finish that job or release first.",
            "current": current,
        }
        append_audit("acquire_deny", detail={"tenant": tenant, "holder": holder, **result})
        return result
    payload = {
        "tenant": tenant,
        "holder": holder or tenant,
        "since": _utc_now(),
        "note": note or f"{tenant} lease",
    }
    try:
        _atomic_write(lease_path(), payload)
    except OSError as exc:
        result = {"ok": False, "error": str(exc)}
        append_audit("acquire_error", detail=result)
        return result
    out = {"ok": True, **payload, "path": str(lease_path()), "audit_path": str(audit_path())}
    append_audit("acquire_ok", detail={"tenant": tenant, "holder": out["holder"], "force": force})
    return out


def release(*, expected: str | None = None) -> dict[str, Any]:
    current = status()
    active = str(current.get("tenant") or "idle")
    if expected and active not in {"idle", expected}:
        result = {
            "ok": False,
            "error": f"Lease held by {active}, expected {expected}",
            "current": current,
        }
        append_audit("release_deny", detail=result)
        return result
    payload = {"tenant": "idle", "holder": "", "since": _utc_now(), "note": "released"}
    try:
        _atomic_write(lease_path(), payload)
    except OSError as exc:
        result = {"ok": False, "error": str(exc)}
        append_audit("release_error", detail=result)
        return result
    out = {"ok": True, **payload, "previous": active, "path": str(lease_path())}
    append_audit("release_ok", detail={"previous": active})
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE GPU lease")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    acq = sub.add_parser("acquire")
    acq.add_argument("tenant", choices=sorted(ACTIVE_TENANTS))
    acq.add_argument("--holder", default="")
    acq.add_argument("--force", action="store_true")
    sub.add_parser("release")
    args = parser.parse_args(argv)

    if args.command == "status":
        result = status()
    elif args.command == "acquire":
        result = acquire(args.tenant, holder=args.holder, force=args.force)  # type: ignore[arg-type]
    elif args.command == "release":
        result = release()
    else:
        raise SystemExit(f"unknown command: {args.command}")

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
