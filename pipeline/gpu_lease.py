"""Serial GPU lease for EMPIRE (RTX 16GB — one heavy tenant at a time).

Tenants: chat | stem | vision | voice
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

Tenant = Literal["chat", "stem", "vision", "voice", "idle"]
VALID: frozenset[str] = frozenset({"chat", "stem", "vision", "voice", "idle"})


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def lease_path() -> Path:
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder / "gpu-lease.json"
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    folder = root / "config"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "gpu-lease.json"


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
    }


def acquire(tenant: Tenant, *, holder: str = "", note: str = "", force: bool = False) -> dict[str, Any]:
    if tenant not in VALID or tenant == "idle":
        return {"ok": False, "error": f"Invalid tenant: {tenant}"}
    current = status()
    active = str(current.get("tenant") or "idle")
    if active not in {"idle", tenant} and not force:
        return {
            "ok": False,
            "error": f"GPU leased to {active} (holder={current.get('holder')}). "
            "Finish that job or release first.",
            "current": current,
        }
    payload = {
        "tenant": tenant,
        "holder": holder or tenant,
        "since": _utc_now(),
        "note": note or f"{tenant} lease",
    }
    try:
        _atomic_write(lease_path(), payload)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, **payload, "path": str(lease_path())}


def release(*, expected: str | None = None) -> dict[str, Any]:
    current = status()
    active = str(current.get("tenant") or "idle")
    if expected and active not in {"idle", expected}:
        return {
            "ok": False,
            "error": f"Lease held by {active}, expected {expected}",
            "current": current,
        }
    payload = {"tenant": "idle", "holder": "", "since": _utc_now(), "note": "released"}
    try:
        _atomic_write(lease_path(), payload)
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    return {"ok": True, **payload, "previous": active, "path": str(lease_path())}


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(description="EMPIRE GPU lease")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    acq = sub.add_parser("acquire")
    acq.add_argument("tenant", choices=["chat", "stem", "vision", "voice"])
    acq.add_argument("--holder", default="")
    acq.add_argument("--force", action="store_true")
    sub.add_parser("release")
    args = parser.parse_args(argv)

    if args.command == "status":
        result = status()
    elif args.command == "acquire":
        result = acquire(args.tenant, holder=args.holder, force=args.force)
    else:
        result = release()
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
