"""Generate always-on Eve operating context (playbook index + how to use tools).

Written by Mechanic on verify-capabilities; loaded with eve_instructions + empire-routing
on every session.started — no special Architect phrases required.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = (
    EMPIRE_ROOT / "agents" / "empire-task-agent" / "agent" / "eve-operating-context.md"
)


def render_operating_context_md() -> str:
    from pipeline import playbook, verified_hands

    cov = playbook.coverage()
    tool_count = int(cov.get("tool_docs") or cov.get("claimed_tools") or 0)
    areas = playbook.index()
    verified = verified_hands.load_verification()
    verified_line = verified_hands.pulse_snippet()

    lines = [
        "# Eve operating context (Mechanic-generated)",
        "",
        "You **always** have this map. The Architect does not need magic phrases. "
        "Each user turn also carries a live `[[EMPIRE_RESOURCE_PULSE]]` block — "
        "**effective_tools**, **can_admit_now**, and headroom are authoritative there.",
        "",
        f"**Registered tools:** {tool_count} (short schema cues are already in your tool list).",
        "",
        "## How to use limbs (default workflow)",
        "",
        "1. **Live inventory** — read the pulse block on this turn; do not invent GPU/RAM or deny GitHub/internet if scouts are listed.",
        "2. **Pick the limb** — `capability_route(question)` when intent is unclear.",
        "3. **Worked paths** — `playbook(area)` for Ask → Do → Get examples (areas below).",
        "4. **Parameters** — `tool_docs(tool_name)` before calling an unfamiliar tool.",
        "5. **Admit session tools** — `admit_for_goal(category)` when pulse says headroom OK and the limb is off.",
        "6. **Never** tell the Architect a tool is broken without checking pulse + this file's verified section.",
        "",
        "## Playbook areas (`playbook(\"area\")`)",
        "",
    ]
    for entry in areas:
        area = str(entry.get("area") or "").strip()
        one = str(entry.get("one_line") or "").strip()
        if not area:
            continue
        lines.append(f"- **{area}** — {one}")
    lines.extend(
        [
            "",
            "## Mechanic verified on this machine",
            "",
        ]
    )
    if verified.get("ok") and verified_line:
        lines.append(verified_line)
        tools = verified.get("tools_proven") or []
        if isinstance(tools, list) and tools:
            sample = ", ".join(str(t) for t in tools[:24])
            if len(tools) > 24:
                sample += f", … (+{len(tools) - 24} more)"
            lines.append(f"Proven names (sample): {sample}.")
    else:
        lines.append(
            "_No fresh verification file — run `scripts/verify-capabilities.ps1` before claiming what is proven._"
        )
    lines.extend(
        [
            "",
            "## Refresh",
            "",
            "Mechanic: `python -m pipeline.eve_operating_context` or `verify-capabilities.ps1`.",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def write_operating_context(path: Path | None = None) -> dict[str, Any]:
    out = path or DEFAULT_OUT
    text = render_operating_context_md()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return {"ok": True, "path": str(out), "chars": len(text)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Write eve-operating-context.md for Eve session prompt")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    result = write_operating_context(args.out)
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
