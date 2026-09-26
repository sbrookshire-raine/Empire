"""EMPIRE operating audit - measure the running stack against its contract.

Read-only: HTTP probes, Ollama /api/ps, git census. No writes to the stack, no
restarts, no ingestion, no model calls. Exits 1 when a threshold fails, so it can
run as a gate step.

    python scripts/audit-empire.py           # human summary
    python scripts/audit-empire.py --json    # machine-readable
    python scripts/audit-empire.py --write   # also docs/audits/<date>.runtime.json

Contract: docs/OPERATING_CONTRACT.md - that document is the record, this script is
the measurement. If they disagree, fix whichever is wrong and say so in both.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CTX = 24576
# Embedding models are pinned resident on purpose (ensure-ollama-parallel.ps1 sets
# keep_alive=-1 for nomic-embed-text) and have their own small context, so the chat
# window rule must not be applied to them. They are reported, never enforced.
EMBEDDER_HINTS = ("embed", "nomic", "bge", "e5-")
SERVICES = (
    ("PocketBase", "http://127.0.0.1:8090/api/health"),
    ("Eve Workbench", "http://127.0.0.1:8080/api/memory/status"),
    ("Eve runtime", "http://127.0.0.1:2000/eve/v1/info"),
    ("Voice (Speaches)", "http://127.0.0.1:8000/health"),
)
PROMPT_LAYER = (
    ("eve_instructions.md", ROOT / "eve_instructions.md"),
    (
        "empire-routing.md",
        ROOT / "agents" / "empire-task-agent" / "agent" / "empire-routing.md",
    ),
)


def get_json(url: str, timeout: float = 6.0):
    """Return (status, parsed-or-None). Health endpoints may answer plain text."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            try:
                return resp.status, json.loads(body)
            except json.JSONDecodeError:
                return resp.status, None
    except urllib.error.HTTPError as exc:
        return exc.code, None
    except (urllib.error.URLError, TimeoutError, OSError):
        return None, None


def probe_services() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for name, url in SERVICES:
        status, _ = get_json(url)
        out.append(
            {
                "name": name,
                "url": url,
                "status": status,
                "ok": bool(status and 200 <= int(status) < 400),
            }
        )
    return out


def ollama_placement() -> dict[str, object]:
    status, payload = get_json("http://127.0.0.1:11434/api/ps")
    if status != 200 or not isinstance(payload, dict):
        return {"reachable": False, "models": []}
    models = [
        {
            "name": model.get("name"),
            "context": model.get("context_length"),
            "vram_gb": round((model.get("size_vram") or 0) / (1024**3), 1),
        }
        for model in payload.get("models", [])
    ]
    return {"reachable": True, "models": models}


def prompt_layer() -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for label, path in PROMPT_LAYER:
        if not path.is_file():
            out.append({"file": label, "exists": False})
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        out.append(
            {
                "file": label,
                "exists": True,
                "lines": len(text.splitlines()),
                "kb": round(len(text.encode("utf-8")) / 1024, 1),
            }
        )
    return out


def git(*args: str) -> str:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=90,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return completed.stdout


def doc_census() -> dict[str, int]:
    tracked = [line for line in git("ls-files", "*.md").splitlines() if line.strip()]
    skip = {".git", "venv", "node_modules", "dist", "build", ".eve", ".output"}
    on_disk = [
        path for path in ROOT.rglob("*.md") if not any(part in skip for part in path.parts)
    ]
    return {"tracked_md": len(tracked), "on_disk_md": len(on_disk)}


def attribution() -> dict[str, int]:
    out = git(
        "grep",
        "-l",
        "-E",
        "SPDX|Licensed under|Copyright \\(c\\)",
        "--",
        "*.py",
        "*.ts",
        "*.ps1",
    )
    return {"files_with_licence_header": len([l for l in out.splitlines() if l.strip()])}


def evaluate(report: dict[str, object]) -> list[str]:
    problems: list[str] = []
    for service in report["services"]:  # type: ignore[union-attr]
        if not service["ok"]:
            problems.append(f"service down: {service['name']} (status {service['status']})")
    placement = report["placement"]  # type: ignore[assignment]
    if not placement["reachable"]:
        problems.append("Ollama /api/ps unreachable")
    else:
        for model in placement["models"]:
            name = str(model["name"] or "")
            if any(hint in name.casefold() for hint in EMBEDDER_HINTS):
                continue
            if model["context"] != EXPECTED_CTX:
                problems.append(
                    f"{model['name']} loaded at ctx {model['context']}, contract says "
                    f"{EXPECTED_CTX} (apply: ensure-ollama-parallel.ps1 -KvCacheType q8_0 "
                    "-FlashAttention)"
                )
    for item in report["prompt_layer"]:  # type: ignore[union-attr]
        if not item["exists"]:
            problems.append(f"always-on prompt file missing: {item['file']}")
    return problems


def build_report() -> dict[str, object]:
    report: dict[str, object] = {
        "measured_at": dt.datetime.now().isoformat(timespec="seconds"),
        "services": probe_services(),
        "placement": ollama_placement(),
        "prompt_layer": prompt_layer(),
        "docs": doc_census(),
        "attribution": attribution(),
    }
    report["problems"] = evaluate(report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure EMPIRE against its operating contract."
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--write",
        action="store_true",
        help="also write docs/audits/<date>.runtime.json",
    )
    args = parser.parse_args()

    report = build_report()

    if args.write:
        target = ROOT / "docs" / "audits" / f"{dt.date.today().isoformat()}.runtime.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        report["written_to"] = str(target.relative_to(ROOT))

    if args.json:
        print(json.dumps(report, indent=2))
        return 1 if report["problems"] else 0

    print("EMPIRE operating audit")
    print("======================")
    for service in report["services"]:  # type: ignore[union-attr]
        flag = "OK  " if service["ok"] else "DOWN"
        print(f"  {flag} {service['name']:<18} {service['status']}")
    placement = report["placement"]  # type: ignore[assignment]
    if placement["models"]:
        for model in placement["models"]:
            print(f"  ctx {model['context']}  vram {model['vram_gb']} GB  {model['name']}")
    elif placement["reachable"]:
        print("  placement           idle (0 VRAM - correct between turns)")
    else:
        print("  placement           unreachable")
    for item in report["prompt_layer"]:  # type: ignore[union-attr]
        state = f"{item['lines']}L / {item['kb']}KB" if item["exists"] else "MISSING"
        print(f"  prompt {item['file']:<24} {state}")
    docs = report["docs"]  # type: ignore[assignment]
    attr = report["attribution"]  # type: ignore[assignment]
    print(f"  docs                tracked={docs['tracked_md']} on-disk={docs['on_disk_md']}")
    print(f"  attribution         headers={attr['files_with_licence_header']}")
    if report["problems"]:
        print("")
        print("  CONTRACT VIOLATIONS:")
        for problem in report["problems"]:  # type: ignore[union-attr]
            print(f"   - {problem}")
    else:
        print("")
        print("  contract satisfied")
    return 1 if report["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
