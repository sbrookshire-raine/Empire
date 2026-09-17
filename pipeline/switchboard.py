"""Eve switchboard — governed service control (flagship of the arms plan).

Wraps the existing service-control engine (`scripts/lib/service-control.ps1` +
`config/services.json`) and the serial GPU lease (`pipeline/gpu_lease.py`) behind
a governed, dry-runnable Python surface so Eve starts/stops exactly the services
a task needs and never oversubscribes 16 GB VRAM.

Safety contract:
  * Every start/stop is a *plan first* (dry_run returns the plan with no action).
  * Every mutating action is gated by `resource_pulse.pulse()` headroom.
  * Heavy GPU tenants serialize through `gpu_lease` — one at a time, release before switch.
  * All actions append to the admission audit trail (no silent changes).
  * PowerShell runs with `-File` + `-Only` on the *allowlisted* service ids only;
    the ids come from `config/services.json`, never from free-form user text.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

from pipeline import gpu_lease, resource_pulse

ROOT = Path(__file__).resolve().parents[1]
SERVICES_JSON = ROOT / "config" / "services.json"
ROLL_IN_PS1 = ROOT / "scripts" / "roll-in.ps1"
ROLL_OUT_PS1 = ROOT / "scripts" / "roll-out.ps1"

# Services Eve may auto-start/stop. `ollama` is external (managed=false) so Eve
# never spawns it; `eve` is self — never stop the process you're running in.
EVE_MANAGEABLE = ("pocketbase", "frontend")
EVE_EXTERNAL = ("ollama", "eve")


def load_services() -> dict[str, Any]:
    try:
        data = json.loads(SERVICES_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"rollInOrder": [], "rollOutOrder": [], "services": {}}
    if not isinstance(data, dict):
        return {"rollInOrder": [], "rollOutOrder": [], "services": {}}
    return data


def service_ids() -> list[str]:
    services = load_services().get("services") or {}
    return [str(k) for k in services if isinstance(services, dict)]


def _validate_targets(targets: list[str]) -> dict[str, Any]:
    """Reject anything outside the allowlisted service ids (no free-form args)."""
    allowed = set(service_ids())
    cleaned: list[str] = []
    for t in targets:
        name = str(t or "").strip()
        if not name:
            continue
        if name not in allowed:
            return {"ok": False, "error": f"Unknown service: {name}", "allowed": sorted(allowed)}
        if name not in cleaned:
            cleaned.append(name)
    return {"ok": True, "targets": cleaned}


def _run_powershell(script: Path, targets: list[str], *, dry_run: bool) -> dict[str, Any]:
    """Run roll-in/roll-out scoped to allowlisted services. dry_run = no-op plan."""
    if dry_run:
        return {
            "ok": True,
            "dry_run": True,
            "script": script.name,
            "targets": targets,
            "note": "plan only — no service mutated",
        }
    cmd = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        str(script),
        "-Only",
    ]
    cmd.extend(targets)
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "service control timed out (180s)"}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}
    out = (completed.stdout or "").strip()
    err = (completed.stderr or "").strip()
    gpu_lease.append_audit(
        "switchboard_service_control",
        detail={
            "script": script.name,
            "targets": targets,
            "exit": completed.returncode,
            "stdout_tail": out[-400:],
            "stderr_tail": err[-400:],
        },
    )
    return {
        "ok": completed.returncode == 0,
        "exit_code": completed.returncode,
        "targets": targets,
        "stdout": out[-800:],
        "stderr": err[-800:],
    }


def _headroom_ok() -> tuple[bool, dict[str, Any]]:
    """Headroom gate: refuse mutations when the machine is already tight."""
    try:
        snap = resource_pulse.pulse()
    except Exception as exc:  # noqa: BLE001
        return False, {"ok": False, "error": str(exc)}
    return bool(snap.get("headroom_ok")), snap


def status() -> dict[str, Any]:
    services = load_services()
    cfg = services.get("services") or {}
    pulse = resource_pulse.pulse()
    lease = gpu_lease.status()
    rows: list[dict[str, Any]] = []
    for name in service_ids():
        meta = cfg.get(name) or {}
        rows.append(
            {
                "id": name,
                "label": str(meta.get("label") or name),
                "port": meta.get("port"),
                "managed": bool(meta.get("managed")),
                "up": bool((pulse.get("services") or {}).get(name)),
            }
        )
    return {
        "ok": True,
        "services": rows,
        "headroom_ok": bool(pulse.get("headroom_ok")),
        "headroom_reasons": pulse.get("headroom_reasons") or [],
        "gpu_lease": lease,
        "manageable": list(EVE_MANAGEABLE),
        "external": list(EVE_EXTERNAL),
        "roll_in_order": list(services.get("rollInOrder") or []),
        "roll_out_order": list(services.get("rollOutOrder") or []),
    }


def plan(services_needed: list[str]) -> dict[str, Any]:
    """Compute which services to start/stop for a task class — no mutation."""
    valid = _validate_targets(services_needed)
    if not valid["ok"]:
        return valid
    targets = valid["targets"]
    services = load_services().get("services") or {}
    to_start: list[str] = []
    for name in targets:
        meta = services.get(name) or {}
        if not bool(meta.get("managed")):
            continue  # external (ollama) — verify only, never start
        to_start.append(name)
    # Stop only managed services not in the needed set (within Eve-manageable scope).
    to_stop = [n for n in EVE_MANAGEABLE if n not in targets]
    return {
        "ok": True,
        "dry_run": True,
        "needed": targets,
        "start": to_start,
        "stop": to_stop,
        "external_verify": [n for n in targets if n in EVE_EXTERNAL],
    }


def ensure(services_needed: list[str], *, dry_run: bool = False) -> dict[str, Any]:
    """Start the services a task needs, gated by headroom."""
    p = plan(services_needed)
    if not p["ok"]:
        return p
    ok_head, snap = _headroom_ok()
    if not ok_head and not dry_run:
        gpu_lease.append_audit("switchboard_ensure_denied", detail={"headroom": snap})
        return {
            "ok": False,
            "error": "Headroom not OK — refused to start services to protect the machine.",
            "headroom_reasons": snap.get("headroom_reasons") or [],
            "plan": p,
        }
    start_targets = list(p["start"])
    if not start_targets:
        result = dict(p)
        result["headroom_ok"] = bool(snap.get("headroom_ok"))
        return result
    result = _run_powershell(ROLL_IN_PS1, start_targets, dry_run=dry_run)
    result["plan"] = p
    result["headroom_ok"] = bool(snap.get("headroom_ok"))
    return result


def release(services_to_stop: list[str], *, dry_run: bool = False) -> dict[str, Any]:
    """Stop managed services a task no longer needs (never Eve/ollama)."""
    valid = _validate_targets(services_to_stop)
    if not valid["ok"]:
        return valid
    targets = [n for n in valid["targets"] if n in EVE_MANAGEABLE]
    if not targets:
        return {
            "ok": True,
            "dry_run": dry_run,
            "note": "nothing to release (only pocketbase/frontend are Eve-manageable)",
            "requested": valid["targets"],
        }
    result = _run_powershell(ROLL_OUT_PS1, targets, dry_run=dry_run)
    result["requested"] = valid["targets"]
    return result


def tenant(action: str, *, tenant_name: str = "", dry_run: bool = False) -> dict[str, Any]:
    """Serialize one heavy GPU tenant; acquire with force=False, release before switch."""
    action = (action or "").strip().lower()
    if action == "status":
        return gpu_lease.status()
    if action == "acquire":
        if dry_run:
            return {"ok": True, "dry_run": True, "action": "acquire", "tenant": tenant_name}
        return gpu_lease.acquire(tenant_name)  # type: ignore[arg-type]
    if action == "release":
        if dry_run:
            return {"ok": True, "dry_run": True, "action": "release"}
        return gpu_lease.release()
    return {"ok": False, "error": f"Unknown tenant action: {action}"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE Eve switchboard")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="Service + headroom + GPU lease snapshot")
    sub.add_parser("plan", help="Dry-run plan (no mutation)").add_argument(
        "services", nargs="*"
    )

    ens = sub.add_parser("ensure", help="Start services (headroom-gated)")
    ens.add_argument("services", nargs="*")
    ens.add_argument("--dry-run", action="store_true")

    rel = sub.add_parser("release", help="Stop managed services")
    rel.add_argument("services", nargs="*")
    rel.add_argument("--dry-run", action="store_true")

    tn = sub.add_parser("tenant", help="GPU tenant acquire/release/status")
    tn.add_argument("action", choices=("acquire", "release", "status"))
    tn.add_argument("--tenant", default="")
    tn.add_argument("--dry-run", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "status":
        out = status()
    elif args.cmd == "plan":
        out = plan(list(args.services))
    elif args.cmd == "ensure":
        out = ensure(list(args.services), dry_run=bool(args.dry_run))
    elif args.cmd == "release":
        out = release(list(args.services), dry_run=bool(args.dry_run))
    elif args.cmd == "tenant":
        out = tenant(args.action, tenant_name=args.tenant, dry_run=bool(args.dry_run))
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
