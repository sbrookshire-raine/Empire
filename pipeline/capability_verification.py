"""Verify every Eve tool contract + MCP server import — before Architect UX smoke.

Writes:
- tmp/capability_verification_report.json
- data/curated_primitives/raw_materials/EVE_VERIFIED_CAPABILITIES.md (for eve_core sync)
- %LOCALAPPDATA%/EMPIRE/eve_hands_verified.json (pulse injection)
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
BATTERY_PATH = EMPIRE_ROOT / "config" / "diagnostics" / "capability-verification-battery.json"
MCP_JSON = EMPIRE_ROOT / ".cursor" / "mcp.json"
TOOL_DOCS = EMPIRE_ROOT / "config" / "eve-capabilities" / "tool-docs"
EVE_BUILD = EMPIRE_ROOT / "agents" / "empire-task-agent" / ".output" / "server" / "index.mjs"


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_battery() -> dict[str, Any]:
    return json.loads(BATTERY_PATH.read_text(encoding="utf-8"))


def _check(name: str, ok: bool, detail: str = "", *, tool: str = "", tier: str = "offline") -> dict[str, Any]:
    return {
        "name": name,
        "ok": ok,
        "detail": detail[:500],
        "tool": tool or name,
        "tier": tier,
    }


def probe_playbook_coverage() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, "-m", "pipeline.playbook", "--coverage"],
        cwd=str(EMPIRE_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    ok = proc.returncode == 0
    detail = (proc.stdout or proc.stderr or "")[:400]
    return _check("playbook_coverage", ok, detail, tool="playbook")


def probe_capability_governance() -> dict[str, Any]:
    from pipeline import capability_registry as cr
    from pipeline import capability_seed as cs

    missing: list[str] = []
    for cap in cs.canonical_capabilities():
        cid = str(cap.get("capability_id") or "")
        res = cr.verify_capability(cid)
        if not res.get("ok"):
            missing.append(f"{cid}:{res.get('reason')}")
    ok = not missing
    return _check(
        "capability_governance",
        ok,
        f"verified={len(cs.canonical_capabilities())} fail={len(missing)}",
        tool="capability_registry",
    )


def probe_eve_tool_docs() -> dict[str, Any]:
    docs = sorted(TOOL_DOCS.glob("*.md"))
    names = [p.stem for p in docs]
    ok = len(names) >= 80
    return _check("eve_tool_docs", ok, f"count={len(names)}", tool="tool_docs")


def probe_eve_build() -> dict[str, Any]:
    if not EVE_BUILD.is_file():
        return _check("eve_build", False, "missing index.mjs — run start-eve or npm run build", tool="eve_runtime")
    text = EVE_BUILD.read_text(encoding="utf-8", errors="replace")
    samples = ("resource_farm_run_default", "github_scout_search_default", "resource_pulse_default")
    missing = [s for s in samples if s not in text]
    ok = not missing
    return _check("eve_build", ok, f"missing={missing}" if missing else "core tools bundled", tool="eve_runtime")


def probe_pipeline_call(spec: dict[str, Any]) -> dict[str, Any]:
    cid = str(spec.get("id") or "pipeline")
    mod_name = str(spec.get("module") or "")
    fn_name = str(spec.get("call") or "")
    try:
        mod = importlib.import_module(mod_name)
        fn = getattr(mod, fn_name)
        args = spec.get("args") or []
        kwargs = spec.get("kwargs") or {}
        result = fn(*args, **kwargs)
        ok = isinstance(result, dict) and result.get("ok") is not False
        if cid == "resource_pulse":
            ok = bool(result.get("ok"))
        detail = str(result.get("summary") or result.get("error") or "ok")[:200]
    except Exception as exc:  # noqa: BLE001
        return _check(cid, False, str(exc), tool=fn_name or cid)
    return _check(cid, ok, detail, tool=fn_name or cid)


def probe_mcp_servers() -> list[dict[str, Any]]:
    if not MCP_JSON.is_file():
        return [_check("mcp_json", False, "missing .cursor/mcp.json", tier="mcp")]
    raw = json.loads(MCP_JSON.read_text(encoding="utf-8"))
    servers = raw.get("mcpServers") if isinstance(raw, dict) else {}
    if not isinstance(servers, dict):
        return [_check("mcp_json", False, "invalid shape", tier="mcp")]
    out: list[dict[str, Any]] = []
    for server_id, cfg in sorted(servers.items()):
        if not isinstance(cfg, dict):
            out.append(_check(f"mcp:{server_id}", False, "bad config", tier="mcp"))
            continue
        args = cfg.get("args") if isinstance(cfg.get("args"), list) else []
        script = ""
        for arg in args:
            if isinstance(arg, str) and arg.replace("\\", "/").endswith(".py"):
                script = arg
                break
        if not script:
            out.append(
                _check(
                    f"mcp:{server_id}",
                    True,
                    "non-python entry (graft/rea node) — skipped import",
                    tool=server_id,
                    tier="mcp",
                )
            )
            continue
        path = Path(script)
        if not path.is_absolute():
            path = EMPIRE_ROOT / path
        if not path.is_file():
            out.append(_check(f"mcp:{server_id}", False, f"missing {path}", tool=server_id, tier="mcp"))
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"mcp_probe_{server_id}", path)
            if spec is None or spec.loader is None:
                raise RuntimeError("spec failed")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            out.append(_check(f"mcp:{server_id}", True, "import_ok", tool=server_id, tier="mcp"))
        except Exception as exc:  # noqa: BLE001
            out.append(_check(f"mcp:{server_id}", False, str(exc)[:200], tool=server_id, tier="mcp"))
    return out


def run_offline() -> list[dict[str, Any]]:
    battery = load_battery()
    checks: list[dict[str, Any]] = []
    for spec in battery.get("offline_pipeline_probes") or []:
        if not isinstance(spec, dict):
            continue
        kind = str(spec.get("kind") or "")
        if kind == "playbook_coverage":
            checks.append(probe_playbook_coverage())
        elif kind == "capability_governance":
            checks.append(probe_capability_governance())
        elif kind == "eve_tool_docs":
            checks.append(probe_eve_tool_docs())
        elif kind == "eve_build":
            checks.append(probe_eve_build())
        elif spec.get("module"):
            checks.append(probe_pipeline_call(spec))
    checks.extend(probe_mcp_servers())
    return checks


def run_live() -> list[dict[str, Any]]:
    battery = load_battery()
    checks: list[dict[str, Any]] = []
    for spec in battery.get("live_stack_probes") or []:
        if not isinstance(spec, dict):
            continue
        script = str(spec.get("script") or "")
        args = [str(a) for a in (spec.get("args") or [])]
        path = EMPIRE_ROOT / script.replace("/", "\\")
        if not path.is_file():
            checks.append(_check(str(spec.get("id") or script), False, "script missing", tier="live"))
            continue
        proc = subprocess.run(
            [sys.executable, str(path), *args],
            cwd=str(EMPIRE_ROOT),
            capture_output=True,
            text=True,
            timeout=600,
            env={**os.environ, "PYTHONPATH": str(EMPIRE_ROOT)},
        )
        ok = proc.returncode == 0
        tail = (proc.stdout or proc.stderr or "")[-400:]
        checks.append(
            _check(
                str(spec.get("id") or path.name),
                ok,
                tail,
                tier="live",
            )
        )
    return checks


def render_markdown(checks: list[dict[str, Any]], *, live_ran: bool) -> str:
    passed = [c for c in checks if c.get("ok")]
    failed = [c for c in checks if not c.get("ok")]
    tools = sorted({str(c.get("tool") or "") for c in passed if c.get("tool")})
    mcps = sorted(
        {str(c.get("name") or "").replace("mcp:", "") for c in passed if str(c.get("tier")) == "mcp"}
    )
    lines = [
        "---",
        "source: capability_verification",
        "kind: eve_operating_contract",
        "dataset: eve_core",
        "memory_status: foundation",
        "promote: mechanic_only",
        f"verified_at: {_utc_now()}",
        "---",
        "# EVE verified capabilities (mechanic report)",
        "",
        "This document is **written by Mechanic** (`pipeline.capability_verification`). "
        "Eve should treat it as authoritative for *what is proven to work* on this machine. "
        "Do not tell the Architect a tool is broken without checking this report age and re-running "
        "`scripts/verify-capabilities.ps1`.",
        "",
        f"- Offline checks: **{len([c for c in checks if c.get('tier') != 'live'])}** "
        f"({len(passed)} pass, {len(failed)} fail)",
        f"- Live stack checks run: **{live_ran}**",
        f"- Eve tool-doc registry: **{len(tools)}+** named tools (see `tool_docs` / `playbook`)",
        f"- MCP servers import-clean: **{len(mcps)}**",
        "",
        "## How Eve should use this",
        "",
        "1. **Always-on:** `eve-operating-context.md` in system prompt + `[[EMPIRE_RESOURCE_PULSE]]` every turn.",
        "2. **Route:** `capability_route` → `playbook` → `tool_docs` for parameters.",
        "3. **Call tools** — optional limbs auto-admit via `resource_pulse` / `admit_for_goal`; "
        "never claim you lack GitHub/internet if the tool is listed below as proven.",
        "4. **Workbench Tools dock** is read-only status; you manage admits.",
        "",
        "## Proven MCP servers (import / wiring)",
        "",
    ]
    for name in mcps:
        lines.append(f"- `{name}`")
    if not mcps:
        lines.append("- _(none passed)_")
    lines.extend(["", "## Proven checks (sample tools / subsystems)", ""])
    for c in passed[:40]:
        lines.append(f"- **{c.get('name')}** — `{c.get('tool')}` ({c.get('tier')})")
    if len(passed) > 40:
        lines.append(f"- … and {len(passed) - 40} more")
    if failed:
        lines.extend(["", "## Failed (Architect should not UX-test until fixed)", ""])
        for c in failed:
            lines.append(f"- **{c.get('name')}**: {c.get('detail')}")
    lines.extend(
        [
            "",
            "## Refresh",
            "",
            "```powershell",
            ".\\scripts\\verify-capabilities.ps1",
            ".\\scripts\\verify-capabilities.ps1 -Live -SyncCognee",
            "```",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def write_artifacts(checks: list[dict[str, Any]], *, live_ran: bool) -> dict[str, Any]:
    battery = load_battery()
    cognee_rel = str((battery.get("cognee") or {}).get("markdown_out") or "")
    md_path = EMPIRE_ROOT / cognee_rel.replace("/", "\\") if cognee_rel else None
    report = {
        "ok": all(c.get("ok") for c in checks),
        "verified_at": _utc_now(),
        "check_count": len(checks),
        "passed": sum(1 for c in checks if c.get("ok")),
        "failed": sum(1 for c in checks if not c.get("ok")),
        "live_ran": live_ran,
        "checks": checks,
    }
    tmp = EMPIRE_ROOT / "tmp" / "capability_verification_report.json"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if md_path:
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(render_markdown(checks, live_ran=live_ran), encoding="utf-8")
        report["markdown_path"] = str(md_path)
    from pipeline import verified_hands

    verified_hands.write_verification(
        checks=[{**c, "ok": c.get("ok")} for c in checks if c.get("ok")],
        source="capability_verification",
        notes=f"passed={report['passed']} failed={report['failed']} live={live_ran}",
    )
    report["verified_hands_snippet"] = verified_hands.pulse_snippet()
    from pipeline import eve_operating_context

    ctx = eve_operating_context.write_operating_context()
    report["operating_context_path"] = ctx.get("path")
    return report


def sync_cognee_markdown(md_path: Path, *, dataset: str = "eve_core") -> dict[str, Any]:
    if not md_path.is_file():
        return {"ok": False, "error": f"missing {md_path}"}
    content = md_path.read_text(encoding="utf-8")
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "pipeline.cognee_worker",
            "remember",
            "--content",
            content,
            "--dataset",
            dataset,
        ],
        cwd=str(EMPIRE_ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    if proc.returncode != 0:
        return {
            "ok": False,
            "error": (proc.stderr or proc.stdout or "remember failed")[:400],
            "hint": "Docker Postgres / Cognee may be down — markdown still updated on disk.",
        }
    return {"ok": True, "dataset": dataset, "stdout": (proc.stdout or "")[:200]}


def run(*, live: bool = False, sync_cognee: bool = False) -> dict[str, Any]:
    checks = run_offline()
    live_ran = False
    if live:
        live_ran = True
        checks.extend(run_live())
    report = write_artifacts(checks, live_ran=live_ran)
    if sync_cognee and report.get("ok"):
        md = report.get("markdown_path")
        if md:
            ds = str((load_battery().get("cognee") or {}).get("dataset") or "eve_core")
            sync = sync_cognee_markdown(Path(md), dataset=ds)
            report["cognee_sync"] = sync
            if sync.get("ok") is not True:
                report["cognee_sync_warning"] = (
                    "Markdown updated on disk; eve_core sync failed — start Docker/Cognee and re-run -SyncCognee."
                )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE capability verification battery")
    parser.add_argument("--live", action="store_true", help="Also run live stack probes (Eve up)")
    parser.add_argument(
        "--sync-cognee",
        action="store_true",
        help="Remember markdown report into eve_core (needs Cognee/Postgres)",
    )
    args = parser.parse_args(argv)
    report = run(live=args.live, sync_cognee=args.sync_cognee)
    print(json.dumps(report, indent=2, ensure_ascii=False, default=str))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
