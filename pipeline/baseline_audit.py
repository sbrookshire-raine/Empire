"""Layered baseline audit: host, Docker, EMPIRE services, toolbelt alignment.

One call from Workbench / scripts answers: is the fresh-boot baseline honest and lean?
"""

from __future__ import annotations

import json
import os
import re
import socket
import subprocess
import urllib.error
import urllib.request
from typing import Any

EMPIRE_KEEP_CONTAINERS = frozenset(
    {
        "empire-cognee-postgres",
        "empire-weaviate-heist-2017",
        "empire-speaches",
        "empire-searxng",
    }
)

LEGACY_CONTAINER_PREFIXES = (
    "v2-archive-",
    "media-weaviate",
    "raine_abacus",
    "n8n",
    "agent-zero",
)

SERVICE_PORTS: dict[str, tuple[str, ...]] = {
    "workbench": ("127.0.0.1", 8080),
    "eve": ("127.0.0.1", 2000),
    "pocketbase": ("127.0.0.1", 8090),
    "ollama": ("127.0.0.1", 11434),
    "weaviate": ("127.0.0.1", 8091),
    "voice": ("127.0.0.1", 8000),
}


def _port_open(host: str, port: int, timeout: float = 1.5) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _run(args: list[str], *, timeout: float = 15.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
        encoding="utf-8",
        errors="replace",
    )


def _docker_ok() -> bool:
    return _run(["docker", "info"]).returncode == 0


def _docker_ps_all() -> list[tuple[str, str]]:
    if not _docker_ok():
        return []
    proc = _run(["docker", "ps", "-a", "--format", "{{.Names}}|{{.Status}}"])
    rows: list[tuple[str, str]] = []
    for line in (proc.stdout or "").splitlines():
        if "|" not in line:
            continue
        name, status = line.split("|", 1)
        rows.append((name.strip(), status.strip()))
    return rows


def _eve_sbx_count() -> int:
    if not _docker_ok():
        return 0
    proc = _run(["docker", "ps", "-aq", "--filter", "name=eve-sbx"])
    lines = [x for x in (proc.stdout or "").splitlines() if x.strip()]
    return len(lines)


def _orphan_llama_servers() -> list[dict[str, Any]]:
    """llama-server.exe whose parent is not ollama.exe (Windows)."""
    if os.name != "nt":
        return []
    ps = _run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            (
                "Get-CimInstance Win32_Process -Filter \"Name='llama-server.exe'\" | "
                "ForEach-Object { "
                "$p=$_; $par=Get-CimInstance Win32_Process -Filter "
                "\"ProcessId=$($p.ParentProcessId)\" -ErrorAction SilentlyContinue; "
                "[PSCustomObject]@{Id=$p.ProcessId; ParentName=$par.Name; "
                "MB=[math]::Round($p.WorkingSetSize/1MB,0)} "
                "} | ConvertTo-Json -Compress"
            ),
        ],
        timeout=30.0,
    )
    raw = (ps.stdout or "").strip()
    if not raw:
        return []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return []
    items = parsed if isinstance(parsed, list) else [parsed]
    orphans: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        parent = str(item.get("ParentName") or "").strip().lower()
        if parent != "ollama.exe":
            orphans.append(
                {
                    "pid": item.get("Id"),
                    "parent": item.get("ParentName") or "(dead)",
                    "mb": item.get("MB"),
                }
            )
    return orphans


def _load_toolbelt_active() -> list[str]:
    try:
        from frontend.eve_toolbelt import load_active_tools

        return list(load_active_tools())
    except Exception:  # noqa: BLE001
        return []


def _fetch_resource_pulse(origin: str = "http://127.0.0.1:8080") -> dict[str, Any]:
    url = f"{origin.rstrip('/')}/api/resource-pulse"
    req = urllib.request.Request(url, headers={"Origin": origin})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body if isinstance(body, dict) else {"ok": False}
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": str(exc)}


def run(*, origin: str = "http://127.0.0.1:8080") -> dict[str, Any]:
    layers: dict[str, Any] = {}
    blockers: list[str] = []
    warnings: list[str] = []

    active = _load_toolbelt_active()
    active_set = set(active)
    wiki_on = "wiki_local" in active_set
    voice_on = "voice_presence" in active_set

    # L1 Host / GPU hygiene
    orphans = _orphan_llama_servers()
    host_ok = len(orphans) == 0
    if orphans:
        blockers.append(
            f"{len(orphans)} orphan llama-server process(es) inflate RAM/VRAM meters"
        )
    layers["host"] = {
        "ok": host_ok,
        "orphan_llama_servers": orphans,
        "fix": "Stop-Process those PIDs or restart Ollama from the tray; then re-run baseline-audit.",
    }

    # L2 Docker estate
    docker_rows = _docker_ps_all()
    sbx = _eve_sbx_count()
    unexpected_running: list[str] = []
    legacy_present: list[str] = []
    keep_running: list[str] = []
    for name, status in docker_rows:
        low = name.lower()
        if any(low.startswith(p) or p in low for p in LEGACY_CONTAINER_PREFIXES):
            legacy_present.append(f"{name} ({status})")
        if status.lower().startswith("up"):
            if name in EMPIRE_KEEP_CONTAINERS:
                keep_running.append(name)
            elif "eve-sbx" in name:
                unexpected_running.append(name)
            elif name not in EMPIRE_KEEP_CONTAINERS:
                unexpected_running.append(name)

    docker_ok = sbx == 0 and not unexpected_running and not legacy_present
    if sbx:
        blockers.append(f"{sbx} eve-sbx sandbox container(s) still present")
    if unexpected_running:
        blockers.append(f"Unexpected running containers: {', '.join(unexpected_running)}")
    if legacy_present:
        warnings.append(
            f"Legacy containers still on disk (exited OK): {len(legacy_present)} — "
            "run .\\scripts\\prune-legacy-docker.ps1 -Apply"
        )
    layers["docker"] = {
        "ok": sbx == 0 and not unexpected_running,
        "eve_sbx_count": sbx,
        "running_empire": keep_running,
        "legacy_containers": legacy_present[:8],
        "unexpected_running": unexpected_running,
    }

    # L3 Core services (always expected when stack is up)
    core = {
        "workbench": _port_open(*SERVICE_PORTS["workbench"]),
        "eve": _port_open(*SERVICE_PORTS["eve"]),
        "pocketbase": _port_open(*SERVICE_PORTS["pocketbase"]),
        "ollama": _port_open(*SERVICE_PORTS["ollama"]),
    }
    optional = {
        "weaviate": _port_open(*SERVICE_PORTS["weaviate"]),
        "voice": _port_open(*SERVICE_PORTS["voice"]),
    }
    services_ok = all(core.values())
    if not core["workbench"]:
        blockers.append("Workbench :8080 not listening")
    if not core["eve"]:
        blockers.append("Eve :2000 not listening")
    if not core["pocketbase"]:
        warnings.append("PocketBase :8090 not listening")
    if not core["ollama"]:
        warnings.append("Ollama :11434 not listening")

    if wiki_on and not optional["weaviate"]:
        warnings.append("wiki_local ON but Weaviate :8091 down")
    if not wiki_on and optional["weaviate"]:
        warnings.append("Weaviate :8091 up but wiki_local OFF in toolbelt (extra RAM)")
    if voice_on and not optional["voice"]:
        warnings.append("voice_presence ON but Speaches :8000 down")
    if not voice_on and optional["voice"]:
        warnings.append("Speaches :8000 up but voice_presence OFF (optional stop via Stop-EMPIRE)")

    layers["services"] = {
        "ok": services_ok,
        "core": core,
        "optional": optional,
        "toolbelt_wiki_on": wiki_on,
        "toolbelt_voice_on": voice_on,
    }

    # L4 Truth layer (pulse vs toolbelt)
    pulse = _fetch_resource_pulse(origin)
    meter = pulse.get("capacity_meter") if isinstance(pulse.get("capacity_meter"), dict) else {}
    effective = []
    inv = pulse.get("inventory")
    if isinstance(inv, dict):
        effective = list(inv.get("effective_tools") or [])
    pulse_ok = bool(pulse.get("ok", pulse.get("headroom_ok")))
    if effective and set(effective) != active_set:
        warnings.append(f"Pulse effective_tools {effective} != toolbelt {active}")

    layers["telemetry"] = {
        "ok": pulse_ok,
        "headroom_score": meter.get("headroom_score"),
        "activation_on": meter.get("activation_on_count"),
        "activation_pool": meter.get("activation_pool_count"),
        "ram_used_pct": meter.get("ram_used_pct"),
        "disk_used_pct": meter.get("disk_used_pct"),
        "vram_used_pct": meter.get("vram_used_pct"),
        "gpu_tenant": meter.get("gpu_tenant"),
        "effective_tools": effective,
    }

    layers["toolbelt"] = {
        "ok": True,
        "active_tools": active,
        "defaults_version": 3,
    }

    ok = not blockers and host_ok and layers["docker"]["ok"] and services_ok
    return {
        "ok": ok,
        "layers": layers,
        "blockers": blockers,
        "warnings": warnings,
        "summary": (
            "Baseline clear — meters reflect machine + toolbelt."
            if ok and not warnings
            else "Baseline needs attention (see blockers/warnings)."
        ),
    }


def kill_orphan_llama_servers() -> list[int]:
    """Terminate llama-server.exe not parented by ollama.exe (Windows)."""
    if os.name != "nt":
        return []
    killed: list[int] = []
    for row in _orphan_llama_servers():
        pid = row.get("pid")
        if not isinstance(pid, int):
            continue
        proc = _run(["taskkill", "/PID", str(pid), "/F"])
        if proc.returncode == 0:
            killed.append(pid)
    return killed


def stop_eve_sbx_docker() -> int:
    if not _docker_ok():
        return 0
    running = [
        x
        for x in (_run(["docker", "ps", "-q", "--filter", "name=eve-sbx"]).stdout or "").splitlines()
        if x.strip()
    ]
    if not running:
        return 0
    proc = _run(["docker", "kill", *running])
    if proc.returncode == 0:
        _run(["docker", "rm", "-f", *running])
    return len(running)


def main() -> int:
    import sys

    origin = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080"
    report = run(origin=origin)
    print(json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
