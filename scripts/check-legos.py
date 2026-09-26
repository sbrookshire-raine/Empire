"""LEGO contract validator - enforce docs/LEGO_CONTRACT.md mechanically.

Checks the invariants that can be checked against the catalogs and limb sources as
they exist right now. Exits 1 on a hard violation so it can run inside
mechanic-green; softer findings are WARN and never fail the build (recorded drift
is not a violation).

    python scripts/check-legos.py
    python scripts/check-legos.py --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRICKS = ROOT / "config" / "lego-bricks.json"
MANIFEST = ROOT / "config" / "capability-manifest.json"
LIBRARY = ROOT / "config" / "library.json"
ADAPTER_DIR = ROOT / "agents" / "empire-task-agent" / "agent" / "lib"
PLAYBOOK_DIR = ROOT / "config" / "eve-capabilities" / "playbook"
PROMPT_FILES = (
    ROOT / "eve_instructions.md",
    ROOT / "agents" / "empire-task-agent" / "agent" / "empire-routing.md",
)
PROMPT_BUDGET_KB = 20.0
REQUIRED_BRICK_FIELDS = ("id", "label", "default_on", "tools")
CLOUD_MARKERS = (
    "api.openai.com",
    "api.anthropic.com",
    "generativelanguage.googleapis.com",
    "api.mistral.ai",
    "openrouter.ai",
)

failures: list[str] = []
warnings: list[str] = []
notes: list[str] = []


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"{path.relative_to(ROOT)}: unreadable ({exc})")
        return None


def check_bricks() -> list[dict]:
    data = load_json(BRICKS)
    if not isinstance(data, dict):
        return []
    bricks = data.get("bricks", []) or []
    for brick in bricks:
        bid = brick.get("id", "<no id>")
        for field in REQUIRED_BRICK_FIELDS:
            if field not in brick:
                failures.append(f"brick '{bid}' missing field '{field}'")
        if not brick.get("tools"):
            failures.append(f"brick '{bid}' declares no tools")
        if brick.get("toolbelt") and brick.get("default_on"):
            failures.append(f"brick '{bid}' is optional (toolbelt set) but default_on=true")
        if "gpu_tenant" not in brick:
            warnings.append(f"brick '{bid}' does not declare gpu_tenant")
        if "ports" not in brick:
            warnings.append(f"brick '{bid}' does not declare ports")
    notes.append(f"bricks checked: {len(bricks)}")
    return bricks


def playbook_tool_names() -> set[str]:
    names: set[str] = set()
    if not PLAYBOOK_DIR.is_dir():
        failures.append("playbook directory missing")
        return names
    for page in sorted(PLAYBOOK_DIR.glob("*.md")):
        text = page.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"(?m)^tools:\s*(.+)$", text)
        if match:
            names.update(part.strip() for part in match.group(1).split(",") if part.strip())
    return names


def check_adapters() -> None:
    if not ADAPTER_DIR.is_dir():
        failures.append("agent/lib missing")
        return
    adapters = sorted(ADAPTER_DIR.glob("*-mcp.ts"))
    for adapter in adapters:
        text = adapter.read_text(encoding="utf-8", errors="replace")
        name = adapter.name
        if "@modelcontextprotocol" in text:
            failures.append(f"{name} imports the MCP SDK directly (must use #lib/mcp-client)")
        if "createEmpireMcpClient" not in text:
            failures.append(f"{name} does not use the shared client")
        for marker in CLOUD_MARKERS:
            if marker in text:
                failures.append(f"{name} references a cloud endpoint: {marker}")
        lines = len(text.splitlines())
        if lines > 120:
            warnings.append(f"{name} is {lines} lines - adapters should stay thin")
    notes.append(f"adapters checked: {len(adapters)}")


def check_library() -> None:
    data = load_json(LIBRARY)
    if not isinstance(data, dict):
        return
    points = data.get("access_points", []) or []
    for point in points:
        target = Path(str(point.get("path", "")))
        if not target.exists():
            failures.append(f"library '{point.get('id')}' path missing: {target}")
        if point.get("embed"):
            failures.append(
                f"library '{point.get('id')}' is embed=true - reference is never embedded"
            )
    notes.append(f"library access points checked: {len(points)}")


def check_prompt_layer() -> None:
    total_kb = 0.0
    for path in PROMPT_FILES:
        if not path.is_file():
            failures.append(f"always-on prompt file missing: {path.relative_to(ROOT)}")
            continue
        total_kb += len(path.read_bytes()) / 1024
    if total_kb > PROMPT_BUDGET_KB:
        failures.append(
            f"always-on prompt layer is {total_kb:.1f} KB, budget {PROMPT_BUDGET_KB} KB"
        )
    else:
        notes.append(f"prompt layer: {total_kb:.1f} KB of {PROMPT_BUDGET_KB} KB budget")


def check_contract_drift() -> None:
    data = load_json(MANIFEST)
    if not isinstance(data, dict):
        return
    for name, category in (data.get("categories") or {}).items():
        services = [str(item) for item in (category.get("requires_services") or [])]
        if any(item.startswith("weaviate") for item in services):
            warnings.append(
                f"admission '{name}' still requires {services} while Weaviate is retired "
                "(LEGO_CONTRACT.md section 6)"
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate EMPIRE against the LEGO contract."
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    bricks = check_bricks()
    names = playbook_tool_names()
    if names and bricks:
        covered = [b for b in bricks if any(t in names for t in (b.get("tools") or []))]
        notes.append(f"bricks with a tool named in a playbook limb: {len(covered)}/{len(bricks)}")
    check_adapters()
    check_library()
    check_prompt_layer()
    check_contract_drift()

    if args.json:
        print(json.dumps({"failures": failures, "warnings": warnings, "notes": notes}, indent=2))
        return 1 if failures else 0

    print("LEGO contract check")
    print("===================")
    for line in notes:
        print(f"  note  {line}")
    for line in warnings:
        print(f"  WARN  {line}")
    for line in failures:
        print(f"  FAIL  {line}")
    print("")
    if failures:
        print(f"  {len(failures)} violation(s) - not contract conforming")
        return 1
    print("  contract conforming")
    return 0


if __name__ == "__main__":
    sys.exit(main())
