"""Prompt-budget measurement CLI (refactor plan R-01/R-03).

Prints what the model pays for before the user speaks: always-on instructions, always-registered
tool schemas, and the default Toolbelt set (`wiki_local` is on by default) — plus the change against a
git revision, so a reduction is reproducible rather than claimed.

    .\\venv\\Scripts\\python.exe scripts\\measure-prompt-budget.py
    .\\venv\\Scripts\\python.exe scripts\\measure-prompt-budget.py --json
    .\\venv\\Scripts\\python.exe scripts\\measure-prompt-budget.py --baseline HEAD

Logic lives in `pipeline/prompt_budget.py`, shared with `tests/test_prompt_budget.py`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.prompt_budget import measure, measure_rev, tokens  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure the pre-conversation prompt budget.")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument(
        "--baseline",
        default="HEAD",
        help="git revision to compare against (default HEAD); use '' to skip the comparison",
    )
    args = parser.parse_args()

    data = measure()
    if args.json:
        print(json.dumps(data, indent=2))
        return 0

    print("Always-on instructions")
    for name, chars in data["instructions"].items():
        print(f"  {name:<28} {chars:6,} chars  ~{tokens(chars):5,} tok")
    print(f"  {'subtotal':<28} {data['instruction_chars']:6,} chars  ~{data['instruction_tokens']:5,} tok")

    print("\nTool schemas (description + parameter text)")
    print(f"  always registered ({data['always_tools']} tools)   ~{data['always_schema_tokens']:5,} tok")
    print(
        f"  wiki_local ({data['default_gated_tools']} tools, on)   "
        f"~{data['default_gated_schema_tokens']:5,} tok"
    )
    print(f"  default schema weight             ~{data['default_schema_tokens']:5,} tok")

    print(
        f"\nFLOOR before the user speaks: ~{data['floor_tokens']:,} of {data['num_ctx']:,} tokens "
        f"(~{data['headroom_tokens']:,} left for conversation + tool results)"
    )

    if args.baseline.strip():
        base = measure_rev(args.baseline.strip())
        print(f"\nChange vs {args.baseline.strip()} (same chars/3.8 basis)")
        print(
            f"  instructions      {base['instruction_tokens']:6,} -> {data['instruction_tokens']:6,} tok"
            f"   ({data['instruction_tokens'] - base['instruction_tokens']:+,})"
        )
        print(
            f"  default schemas   {base['default_schema_tokens']:6,} -> {data['default_schema_tokens']:6,} tok"
            f"   ({data['default_schema_tokens'] - base['default_schema_tokens']:+,})"
        )
        saved = base["floor_tokens"] - data["floor_tokens"]
        percent = (saved / base["floor_tokens"] * 100) if base["floor_tokens"] else 0.0
        print(
            f"  floor             {base['floor_tokens']:6,} -> {data['floor_tokens']:6,} tok"
            f"   ({-saved:+,}, {percent:.0f}% smaller)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())