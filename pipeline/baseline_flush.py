"""One-shot lighten: optional tools off, session admits released, GPU/Docker hygiene."""

from __future__ import annotations

import json
import os
import subprocess
import urllib.request
from pathlib import Path
from typing import Any

from pipeline import baseline_audit

ROOT = Path(__file__).resolve().parents[1]
OLLAMA_PS = "http://127.0.0.1:11434/api/ps"


def _run(args: list[str], *, timeout: float = 60.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        encoding="utf-8",
        errors="replace",
    )


def _ollama_unload_loaded() -> list[str]:
    stopped: list[str] = []
    try:
        with urllib.request.urlopen(OLLAMA_PS, timeout=8) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (OSError, json.JSONDecodeError, urllib.error.URLError):
        return stopped
    for row in payload.get("models") or []:
        if not isinstance(row, dict):
            continue
        name = str(row.get("name") or "").strip()
        if not name:
            continue
        proc = _run(["ollama", "stop", name], timeout=120.0)
        if proc.returncode == 0:
            stopped.append(name)
    return stopped


def _docker_stop_container(name: str) -> bool:
    if _run(["docker", "info"]).returncode != 0:
        return False
    exists = (
        _run(["docker", "ps", "-aq", "--filter", f"name=^{name}$"]).stdout or ""
    ).strip()
    if not exists:
        return False
    _run(["docker", "stop", name])
    return True


def _stop_weaviate() -> dict[str, Any]:
    script = ROOT / "scripts" / "stop-weaviate.ps1"
    if not script.is_file():
        return {"ok": False, "error": "stop-weaviate.ps1 missing"}
    proc = _run(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
        ],
        timeout=90.0,
    )
    return {"ok": proc.returncode == 0, "exit_code": proc.returncode}


def flush_baseline(*, stop_docker_limbs: bool = True) -> dict[str, Any]:
    """Return actions taken + fresh resource pulse (bars should drop for RAM/VRAM/tools)."""
    from frontend import eve_toolbelt
    from pipeline import admission_controller, gpu_lease, resource_pulse

    before = resource_pulse.pulse()
    before_meter = before.get("capacity_meter") if isinstance(before.get("capacity_meter"), dict) else {}

    actions: dict[str, Any] = {}

    rel = admission_controller.release_session("dashboard_flush")
    actions["session_release"] = rel

    try:
        actions["gpu_lease"] = gpu_lease.release()
    except Exception as exc:  # noqa: BLE001
        actions["gpu_lease"] = {"ok": False, "error": str(exc)}

    previous_tools = list(eve_toolbelt.load_active_tools())
    eve_toolbelt.write_active_tools([])
    actions["toolbelt_cleared_from"] = previous_tools

    killed_pids = baseline_audit.kill_orphan_llama_servers()
    actions["orphan_llama_killed"] = killed_pids

    sbx = baseline_audit.stop_eve_sbx_docker()
    actions["eve_sbx_removed"] = sbx

    actions["ollama_stopped"] = _ollama_unload_loaded()

    if stop_docker_limbs:
        actions["weaviate_stop"] = _stop_weaviate()
        actions["speaches_stop"] = _docker_stop_container("empire-speaches")

    after = resource_pulse.pulse()
    after_meter = after.get("capacity_meter") if isinstance(after.get("capacity_meter"), dict) else {}

    return {
        "ok": True,
        "summary": (
            "Optional tools off, session admits cleared, GPU models unloaded. "
            "RAM/VRAM bars should drop; disk bar is whole-drive and usually unchanged."
        ),
        "actions": actions,
        "before": {
            "activation_on_count": before_meter.get("activation_on_count"),
            "ram_used_pct": before_meter.get("ram_used_pct"),
            "vram_used_pct": before_meter.get("vram_used_pct"),
            "disk_used_pct": before_meter.get("disk_used_pct"),
        },
        "after": {
            "activation_on_count": after_meter.get("activation_on_count"),
            "ram_used_pct": after_meter.get("ram_used_pct"),
            "vram_used_pct": after_meter.get("vram_used_pct"),
            "disk_used_pct": after_meter.get("disk_used_pct"),
        },
        "pulse": after,
    }


def main() -> int:
    report = flush_baseline()
    print(json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
