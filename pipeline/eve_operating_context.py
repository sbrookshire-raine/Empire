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
        "Each turn carries `[[EMPIRE_RESOURCE_PULSE]]` with **capacity_meter** (progress bars) and "
        "**activation** (ACTIVE / DORMANT / OFF / LOCKED limbs).",
        "",
        f"**Registered tools:** {tool_count} (schema cues in your tool list; full syntax via `tool_docs`).",
        "",
        "## As Eve: ACTIVATE / DEACTIVATE (resource-aware)",
        "",
        "1. **Read the meter** — `capacity_meter.headroom_score` and RAM/Disk/VRAM bars in the pulse block. "
        "Red/ low score → do not ACTIVATE new limbs; finish work and **DEACTIVATE**.",
        "2. **ACTIVATE** — `admit_for_goal(category)` when state is DORMANT, or call a scout tool (auto-admits when room OK).",
        "3. **Use while ACTIVE** — `playbook(area)` + `tool_docs(name)` for how; `capability_route` when unsure.",
        "4. **DEACTIVATE** — `release_capabilities` when a scout burst ends or slots should free (see `activation.session_slots`).",
        "5. **LOCKED** (GPU/heavy) — ask the Architect once; never force Toolbelt or GPU lease.",
        "6. **Never** invent inventory or deny GitHub/internet when pulse shows DORMANT scouts with room to ACTIVATE.",
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
