"""Resource pulse — headroom + inventory so Eve can manage capabilities safely.

Policy B: light (manifest auto_enable) skills may be admitted when headroom is OK
without requiring the Architect to toggle Research Partner. GPU / heavy skills
return need_architect=true — Eve must ask before enabling.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

from frontend import eve_toolbelt
from pipeline import admission_controller, gpu_lease

# Conservative floors when pulse cannot read hardware (fail closed for auto-admit).
MIN_RAM_AVAILABLE_GB = 2.0
MIN_DISK_FREE_GB = 5.0


def _http_ok(url: str, *, timeout: float = 2.0) -> bool:
    try:
        with urlopen(Request(url), timeout=timeout) as resp:
            return int(getattr(resp, "status", 200) or 200) < 500
    except (URLError, OSError, TimeoutError, ValueError):
        return False


def _nvidia_snapshot() -> dict[str, Any]:
    try:
        completed = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=memory.used,memory.total,utilization.gpu",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {"ok": False, "error": "nvidia-smi unavailable"}
    if completed.returncode != 0:
        return {
            "ok": False,
            "error": (completed.stderr or completed.stdout or "nvidia-smi failed")[:200],
        }
    line = (completed.stdout or "").strip().splitlines()
    if not line:
        return {"ok": False, "error": "nvidia-smi empty"}
    parts = [p.strip() for p in line[0].split(",")]
    if len(parts) < 3:
        return {"ok": False, "error": f"unexpected nvidia-smi: {line[0][:120]}"}
    try:
        used = float(parts[0])
        total = float(parts[1])
        util = float(parts[2])
    except ValueError:
        return {"ok": False, "error": f"parse failed: {line[0][:120]}"}
    free = max(0.0, total - used)
    return {
        "ok": True,
        "vram_used_mb": used,
        "vram_total_mb": total,
        "vram_free_mb": free,
        "gpu_util_pct": util,
    }


def _service_probes() -> dict[str, Any]:
    probes = {
        "ollama": _http_ok("http://127.0.0.1:11434/api/tags"),
        "speaches": _http_ok("http://127.0.0.1:8000/health")
        or _http_ok("http://127.0.0.1:8000/v1/models")
        or _http_ok("http://127.0.0.1:8000/"),
        "pocketbase": _http_ok("http://127.0.0.1:8090/api/health"),
        "eve": _http_ok("http://127.0.0.1:2000/"),
    }
    glasses: dict[str, Any] = {"ok": False}
    try:
        from frontend import wiki_api

        glasses = wiki_api.wiki_glasses_health()
    except Exception as exc:  # noqa: BLE001
        glasses = {"ok": False, "glasses_ok": False, "error": str(exc)}
    probes["wiki_glasses"] = bool(glasses.get("glasses_ok"))
    return {"services": probes, "wiki_glasses_detail": glasses}


def _headroom_ok(resources: dict[str, Any], nvidia: dict[str, Any]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    ram = resources.get("ram_available_gb")
    if isinstance(ram, (int, float)):
        if ram < MIN_RAM_AVAILABLE_GB:
            reasons.append(f"RAM available {ram} GB below {MIN_RAM_AVAILABLE_GB} GB")
    else:
        reasons.append("RAM unavailable — fail closed")
    disk = resources.get("disk_free_gb")
    if isinstance(disk, (int, float)):
        if disk < MIN_DISK_FREE_GB:
            reasons.append(f"Disk free {disk} GB below {MIN_DISK_FREE_GB} GB")
    else:
        reasons.append("Disk free unavailable — fail closed")
    # VRAM is advisory unless lease is busy; do not block light admits on missing nvidia-smi
    if nvidia.get("ok") and isinstance(nvidia.get("vram_free_mb"), (int, float)):
        if float(nvidia["vram_free_mb"]) < 512:
            reasons.append(f"VRAM free {nvidia['vram_free_mb']} MB very low")
    return (len(reasons) == 0, reasons)


def _classify_manifest() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    light: list[dict[str, Any]] = []
    heavy: list[dict[str, Any]] = []
    manifest = admission_controller.load_manifest()
    cats = manifest.get("categories") if isinstance(manifest, dict) else {}
    if not isinstance(cats, dict):
        return light, heavy
    for cat_id, meta in cats.items():
        if not isinstance(meta, dict):
            continue
        entry = {
            "id": cat_id,
            "label": str(meta.get("label") or cat_id),
            "gpu_tenant": str(meta.get("gpu_tenant") or "none"),
            "auto_enable": bool(meta.get("auto_enable")),
        }
        gpu = entry["gpu_tenant"]
        if entry["auto_enable"] and gpu in {"", "none", "idle"}:
            light.append(entry)
        else:
            heavy.append(entry)
    return light, heavy


def pulse() -> dict[str, Any]:
    """Full resource + inventory snapshot for Eve."""
    resources = gpu_lease._resource_snapshot()
    nvidia = _nvidia_snapshot()
    lease = gpu_lease.status()
    admit_status = admission_controller.status()
    services_block = _service_probes()
    headroom_ok, headroom_reasons = _headroom_ok(resources, nvidia)
    light, heavy = _classify_manifest()
    effective = set(admit_status.get("effective_tools") or [])
    lease_tenant = str(lease.get("tenant") or "idle")
    gpu_busy = lease_tenant not in {"", "idle"}

    can_admit_now: list[str] = []
    if headroom_ok and not gpu_busy:
        for item in light:
            cid = item["id"]
            if cid not in effective:
                can_admit_now.append(cid)
    elif headroom_ok and gpu_busy:
        # Light network skills still OK when GPU busy (scouts don't take lease)
        for item in light:
            cid = item["id"]
            if cid not in effective:
                can_admit_now.append(cid)

    ask_first: list[dict[str, Any]] = []
    for item in heavy:
        ask_first.append(
            {
                **item,
                "why": "GPU or non-auto skill — ask Architect before enabling",
            }
        )

    summary_parts = [
        f"Effective tools: {', '.join(sorted(effective)) or 'core only'}.",
        f"GPU lease: {lease_tenant}"
        + (f" ({lease.get('holder')})" if lease.get("holder") else "")
        + ".",
    ]
    if headroom_ok:
        summary_parts.append("Headroom OK for light session admits.")
    else:
        summary_parts.append("Headroom blocked: " + "; ".join(headroom_reasons) + ".")
    if can_admit_now:
        summary_parts.append("Can admit now: " + ", ".join(can_admit_now) + ".")
    else:
        summary_parts.append("No light admits needed or headroom blocked.")
    summary_parts.append(
        "Ask Architect before: "
        + ", ".join(i["id"] for i in ask_first[:8])
        + ("…" if len(ask_first) > 8 else "")
        + "."
    )

    return {
        "ok": True,
        "policy": "B",
        "resources": resources,
        "nvidia": nvidia,
        "gpu_lease": lease,
        "services": services_block["services"],
        "wiki_glasses": services_block.get("wiki_glasses_detail"),
        "inventory": {
            "manual_toolbelt": admit_status.get("manual_toolbelt") or [],
            "session_capabilities": admit_status.get("session_capabilities") or [],
            "effective_tools": admit_status.get("effective_tools") or [],
            "research_partner_mode": admit_status.get("research_partner_mode"),
            "ttl_remaining_sec": admit_status.get("ttl_remaining_sec"),
        },
        "headroom_ok": headroom_ok,
        "headroom_reasons": headroom_reasons,
        "light_skills": light,
        "heavy_skills": heavy,
        "can_admit_now": can_admit_now,
        "ask_architect_first": ask_first,
        "summary": " ".join(summary_parts),
    }


def admit_for_goal(
    category: str,
    reason: str = "",
    *,
    ttl_min: int | None = None,
) -> dict[str, Any]:
    """Admit a light skill for a goal when safe; otherwise tell Eve to ask."""
    cleaned = (category or "").strip()
    if cleaned not in eve_toolbelt.ALLOWED_CATEGORIES:
        return {"ok": False, "error": f"Unknown category: {cleaned}"}
    meta = admission_controller.category_meta(cleaned)
    if not meta:
        return {"ok": False, "error": f"No manifest entry for {cleaned}"}

    gpu_tenant = str(meta.get("gpu_tenant") or "none")
    is_light = bool(meta.get("auto_enable")) and gpu_tenant in {"", "none", "idle"}

    snap = pulse()
    if not is_light:
        return {
            "ok": False,
            "need_architect": True,
            "category": cleaned,
            "error": (
                f"{cleaned} is a GPU/heavy or non-auto skill — ask the Architect "
                "before enabling. Do not force the Toolbelt."
            ),
            "pulse_summary": snap.get("summary"),
            "gpu_lease": snap.get("gpu_lease"),
        }

    if not snap.get("headroom_ok"):
        return {
            "ok": False,
            "need_architect": False,
            "category": cleaned,
            "error": "Headroom not OK — refuse admit to protect the machine.",
            "headroom_reasons": snap.get("headroom_reasons"),
            "pulse_summary": snap.get("summary"),
        }

    # Resource-gated path: bypass Research Partner so Architect is not the button.
    result = admission_controller.request_capability(
        cleaned,
        reason or f"eve admit_for_goal {cleaned}",
        ttl_min=ttl_min,
        bypass_partner_check=True,
    )
    result = dict(result)
    result["pulse_summary"] = snap.get("summary")
    result["policy"] = "B"
    result["resource_gated"] = True
    if result.get("ok"):
        result["need_architect"] = False
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE resource pulse + safe admit")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pulse", help="Diagnostics snapshot for Eve")
    admit = sub.add_parser("admit", help="Admit light skill when headroom OK")
    admit.add_argument("category")
    admit.add_argument("--reason", default="")
    admit.add_argument("--ttl-min", type=int, default=None)
    args = parser.parse_args(argv)

    if args.cmd == "pulse":
        out = pulse()
    elif args.cmd == "admit":
        out = admit_for_goal(args.category, args.reason, ttl_min=args.ttl_min)
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
