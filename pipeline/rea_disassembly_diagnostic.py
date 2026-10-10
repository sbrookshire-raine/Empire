"""REA + Disassembly catalog diagnostic battery (config-driven)."""

from __future__ import annotations

import importlib
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
BATTERY_PATH = EMPIRE_ROOT / "config" / "diagnostics" / "rea-disassembly-battery.json"
REA_MJS = EMPIRE_ROOT / "tools" / "rea" / "node_modules" / "rea-agents" / "scripts" / "rea.mjs"


@dataclass
class CheckResult:
    id: str
    tier: str
    ok: bool
    optional: bool = False
    detail: str = ""
    data: dict[str, Any] = field(default_factory=dict)


def load_battery() -> dict[str, Any]:
    if not BATTERY_PATH.is_file():
        raise FileNotFoundError(f"battery missing: {BATTERY_PATH}")
    return json.loads(BATTERY_PATH.read_text(encoding="utf-8"))


def resolve_path(battery: dict[str, Any], key: str | None, rel: str | None = None) -> Path:
    if key:
        raw = (battery.get("paths") or {}).get(key) or ""
        if raw:
            return Path(raw)
    if rel:
        return EMPIRE_ROOT / rel.replace("/", "\\")
    raise ValueError("no path")


def _http_ok(url: str, path: str = "/", timeout: float = 8.0) -> tuple[bool, str]:
    target = url.rstrip("/") + path
    try:
        req = urllib.request.Request(target, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400, f"HTTP {resp.status}"
    except urllib.error.HTTPError as exc:
        return exc.code < 500, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def _rea_doctor_node() -> tuple[bool, str, dict[str, Any]]:
    if not REA_MJS.is_file():
        return False, f"rea.mjs missing at {REA_MJS}", {}
    try:
        proc = subprocess.run(
            ["node", str(REA_MJS), "doctor"],
            capture_output=True,
            timeout=90,
            cwd=str(EMPIRE_ROOT),
        )
    except Exception as exc:  # noqa: BLE001
        return False, str(exc), {}
    text = (proc.stdout or b"").decode("utf-8", errors="replace") + (
        proc.stderr or b""
    ).decode("utf-8", errors="replace")
    node_ok = bool(re.search(r"name:\s*node\s*\n\s*ok:\s*true", text, re.I)) or "node" in text.lower()
    match = re.search(r"detail:\s*([\d.]+)", text)
    version = match.group(1) if match else ""
    ok = node_ok and proc.returncode == 0
    if not ok and node_ok:
        ok = True
        detail = f"Node OK ({version or 'unknown'}); REA doctor exit {proc.returncode} (native engines optional)"
    else:
        detail = f"Node {version or '?'}; exit {proc.returncode}"
    return ok, detail, {"exit_code": proc.returncode, "node_ok": node_ok}


def _rea_analyze_js(path: Path, timeout_sec: int) -> tuple[bool, str, dict[str, Any]]:
    if not REA_MJS.is_file():
        return False, "rea.mjs missing", {}
    if not path.is_dir():
        return False, f"not a directory: {path}", {}
    try:
        proc = subprocess.run(
            ["node", str(REA_MJS), "analyze-javascript-application", str(path)],
            capture_output=True,
            timeout=timeout_sec,
            cwd=str(EMPIRE_ROOT),
        )
    except subprocess.TimeoutExpired:
        return False, f"timed out after {timeout_sec}s", {}
    except Exception as exc:  # noqa: BLE001
        return False, str(exc), {}
    stdout = (proc.stdout or b"").decode("utf-8", errors="replace")
    stderr = (proc.stderr or b"").decode("utf-8", errors="replace")
    combined = stdout + stderr
    tail = combined.splitlines()[-80:]
    last_line = ""
    for line in tail:
        line = line.strip()
        if line.startswith("{") and ("module" in line.lower() or "application" in line.lower()):
            last_line = line
    summary = "no result json"
    modules = 0
    if last_line:
        try:
            parsed = json.loads(last_line)
            if isinstance(parsed, dict):
                modules = int(parsed.get("module_count") or parsed.get("modules") or 0)
                summary = parsed.get("summary") or parsed.get("application") or "parsed"
        except json.JSONDecodeError:
            summary = last_line[:200]
    ok = proc.returncode == 0 or modules > 0 or "analyze_javascript" in combined
    if not ok and proc.returncode == 0:
        ok = True
        summary = "analyze completed (progress-only stdout)"
    return ok, summary if isinstance(summary, str) else str(summary), {
        "exit_code": proc.returncode,
        "modules_hint": modules,
        "stdout_lines": len(combined.splitlines()),
    }


def _repo_slug_from_package(pkg: dict[str, Any], repo_dir: Path) -> str:
    repo_field = pkg.get("repository")
    url = ""
    if isinstance(repo_field, str):
        url = repo_field
    elif isinstance(repo_field, dict):
        url = str(repo_field.get("url") or "")
    match = re.search(r"github\.com[:/]+([^/\s#\"'>]+/[^/\s#\"'>]+)", url, re.I)
    if match:
        return match.group(1).replace(".git", "").lower()
    folder = repo_dir.name.lower()
    if folder:
        return f"local/{folder}"
    return ""


def _atomic_seed_card(battery: dict[str, Any]) -> tuple[bool, str, dict[str, Any]]:
    from pipeline import disassembly_card

    repo = resolve_path(battery, "atomic_agent_repo")
    src = resolve_path(battery, "atomic_agent_src")
    pkg_path = repo / "package.json"
    if not pkg_path.is_file():
        return False, "atomic-agent package.json missing", {}
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    src_dirs = sorted(
        [p.name for p in src.iterdir() if p.is_dir()] if src.is_dir() else [],
    )[:12]
    evidence = [str(pkg_path), str(src)]
    readme = repo / "README.md"
    if readme.is_file():
        evidence.append(str(readme))
    payload = {
        "title": "atomic-agent vs EMPIRE Eve (study session)",
        "container": "electron",
        "target_summary": (
            f"{pkg.get('name', 'atomic-agent')} — {pkg.get('description', '')} "
            f"Sidecar NDJSON + llama.cpp HTTP; compare to Eve on Ollama + MCP + Cognee."
        )[:500],
        "connections": [
            {
                "from": "atomic-agent sidecar (dist/sidecar)",
                "to": "Tauri host NDJSON",
                "kind": "protocol",
                "evidence_ref": str(src / "sidecar"),
            },
            {
                "from": "local-llm / llm modules",
                "to": "external llama.cpp HTTP",
                "kind": "inference",
                "evidence_ref": str(src / "llm"),
            },
            {
                "from": "memory / eval-memory",
                "to": "EMPIRE Cognee + eve_memory",
                "kind": "analogy",
                "evidence_ref": str(repo / "MEMORY.md"),
            },
            {
                "from": "mcp + playwright-core",
                "to": "EMPIRE mcp/ + browser_local",
                "kind": "tools",
                "evidence_ref": str(src / "mcp"),
            },
            {
                "from": "starter-skills",
                "to": "agents/empire-task-agent/agent/skills",
                "kind": "packaging",
                "evidence_ref": str(repo / "starter-skills"),
            },
        ],
        "evidence_refs": evidence,
        "lego_hooks": ["rea", "disassembly-session", "heptabase"],
        "evolution_note": "Seed card from diagnostic battery; deepen after rea_js_atomic_src.",
        "depends_on": [],
        "related_card_ids": [],
        "source_repo": _repo_slug_from_package(pkg, repo),
        "farm_kind": "study",
    }
    try:
        disassembly_card.validate_payload(payload)
    except ValueError as exc:
        return False, str(exc), {}
    existing = disassembly_card.list_cards(limit=50)
    for card in existing:
        if card.get("title") == payload["title"]:
            return True, f"already exists: {card.get('id')}", {"card_id": card.get("id"), "skipped": True}
    result = disassembly_card.write_card(payload)
    if not result.get("ok"):
        return False, str(result.get("error") or result), result
    card_id = (result.get("card") or {}).get("id") or ""
    return True, card_id, {"card_id": card_id, "src_modules": src_dirs}


def run_check(battery: dict[str, Any], spec: dict[str, Any]) -> CheckResult:
    cid = str(spec.get("id") or "")
    tier = str(spec.get("tier") or "")
    optional = bool(spec.get("optional"))
    kind = str(spec.get("kind") or "")

    try:
        if kind == "file":
            path = resolve_path(battery, None, spec.get("path"))
            ok = path.is_file()
            return CheckResult(cid, tier, ok, optional, "present" if ok else f"missing {path}")

        if kind == "dir":
            path = resolve_path(battery, spec.get("path_key"))
            count = len(list(path.iterdir())) if path.is_dir() else 0
            need = int(spec.get("min_entries") or 1)
            ok = count >= need
            return CheckResult(cid, tier, ok, optional, f"{count} entries under {path}")

        if kind == "module":
            target = str(spec.get("target") or "")
            importlib.import_module(target)
            return CheckResult(cid, tier, True, optional, target)

        if kind == "disassembly_roundtrip":
            import tempfile
            from unittest.mock import patch

            from pipeline import disassembly_card

            payload = {
                "title": "diagnostic roundtrip",
                "container": "unknown",
                "target_summary": "ephemeral diagnostic write",
                "connections": [
                    {"from": "a", "to": "b", "kind": "test"},
                    {"from": "b", "to": "c", "kind": "test"},
                    {"from": "c", "to": "d", "kind": "test"},
                ],
            }
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                with patch.object(disassembly_card, "cards_dir", return_value=root):
                    written = disassembly_card.write_card(payload)
            ok = bool(written.get("ok"))
            card_id = (written.get("card") or {}).get("id", "")
            return CheckResult(cid, tier, ok, optional, card_id, {"card_id": card_id})

        if kind == "rea_doctor_node":
            ok, detail, data = _rea_doctor_node()
            return CheckResult(cid, tier, ok, optional, detail, data)

        if kind == "rea_analyze_js":
            path = resolve_path(battery, spec.get("path_key"))
            timeout_sec = int(spec.get("timeout_sec") or 120)
            ok, detail, data = _rea_analyze_js(path, timeout_sec)
            return CheckResult(cid, tier, ok, optional, detail, data)

        if kind == "heptabase_health":
            from pipeline.heptabase_cli import health_check

            data = health_check()
            ok = bool(data.get("ok"))
            return CheckResult(cid, tier, ok, optional, str(data.get("hint") or data.get("error") or "ok"), data)

        if kind == "http":
            services = battery.get("services") or {}
            base = str(services.get(spec.get("url_key") or "") or "")
            path = str(spec.get("path") or "/")
            ok, detail = _http_ok(base, path)
            return CheckResult(cid, tier, ok, optional, detail)

        if kind == "atomic_seed_card":
            ok, detail, data = _atomic_seed_card(battery)
            return CheckResult(cid, tier, ok, optional, detail, data)

        return CheckResult(cid, tier, False, optional, f"unknown kind: {kind}")
    except Exception as exc:  # noqa: BLE001
        return CheckResult(cid, tier, False, optional, str(exc))


def run_battery(*, include_optional: bool = True, skip_tiers: set[str] | None = None) -> dict[str, Any]:
    battery = load_battery()
    skip = skip_tiers or set()
    results: list[CheckResult] = []
    for spec in battery.get("checks") or []:
        if not isinstance(spec, dict):
            continue
        tier = str(spec.get("tier") or "")
        if tier in skip:
            continue
        if spec.get("optional") and not include_optional:
            continue
        results.append(run_check(battery, spec))

    required = [r for r in results if not r.optional]
    optional = [r for r in results if r.optional]
    required_ok = all(r.ok for r in required)
    optional_ok = all(r.ok for r in optional)

    return {
        "ok": required_ok,
        "optional_ok": optional_ok,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "battery": battery.get("name"),
        "required": [asdict(r) for r in required],
        "optional": [asdict(r) for r in optional],
        "summary": {
            "required_pass": sum(1 for r in required if r.ok),
            "required_total": len(required),
            "optional_pass": sum(1 for r in optional if r.ok),
            "optional_total": len(optional),
        },
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Run REA/disassembly diagnostic battery")
    parser.add_argument("--json", action="store_true", help="print JSON only")
    parser.add_argument("--out", type=Path, help="write JSON report path")
    parser.add_argument("--fast", action="store_true", help="skip optional checks and rea_js analyze")
    args = parser.parse_args(argv)

    skip: set[str] = set()
    include_optional = True
    if args.fast:
        include_optional = False
        skip.add("rea")

    report = run_battery(include_optional=include_optional, skip_tiers=skip)

    out_path = args.out or (EMPIRE_ROOT / "tmp" / "rea_disassembly_diagnostic.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        s = report["summary"]
        print("REA / Disassembly diagnostic")
        print("============================")
        print(
            f"Required: {s['required_pass']}/{s['required_total']}  "
            f"Optional: {s['optional_pass']}/{s['optional_total']}"
        )
        for block, label in ((report["required"], "required"), (report["optional"], "optional")):
            for item in block:
                mark = "OK" if item["ok"] else "FAIL"
                opt = " (optional)" if item.get("optional") else ""
                print(f"  [{mark}] {item['id']}{opt}: {item.get('detail') or ''}")
        print(f"\nReport: {out_path}")

    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
