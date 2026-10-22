#!/usr/bin/env python3
"""Measure the prompt the LIVE model actually pays, in real tokens.

Why a second measurement
-------------------------
`scripts/measure-prompt-budget.py` estimates tokens as chars/3.8 over the
instruction files and the tool-schema prose. That is a consistent proxy, and
it is the right basis for a ceiling test (it needs no stack). But it is an
*estimate*: Ollama's own `prompt_tokens` also counts the chat template, the
JSON Schema envelope and the tool-call scaffolding, which no character count
can see.

This asks the running stack what it is really charged, and reports the delta
against the static estimate so the proxy's error is known rather than
assumed.

Usage (stack up):
    .\\venv\\Scripts\\python.exe scripts\\measure-live-prompt.py
    .\\venv\\Scripts\\python.exe scripts\\measure-live-prompt.py --json
    .\\venv\\Scripts\\python.exe scripts\\measure-live-prompt.py --max-tokens 12000

Exit code 0 = the measurement was taken and is under the ceiling.
Exit code 1 = the measurement failed, or the live prompt is over the ceiling.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline import prompt_budget


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure the live prompt budget in real tokens.")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--model", default="", help="model to measure (default: the active model)")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=0,
        help="fail when the live prompt exceeds this many tokens (default: the context window)",
    )
    args = parser.parse_args()

    live = prompt_budget.measure_live(model=args.model)
    static = prompt_budget.measure()
    if not live.get("ok"):
        print(f"FAIL: live prompt measurement unavailable: {live.get('reason')}")
        if args.json:
            print(json.dumps({"ok": False, "live": live, "static": static}, indent=2))
        return 1

    measured = int(live["prompt_tokens"])
    estimate = int(static["floor_tokens"])
    ceiling = args.max_tokens or int(live["num_ctx"])
    live["static_estimate_tokens"] = estimate
    live["delta_tokens"] = measured - estimate
    live["ceiling_tokens"] = ceiling
    live["ok"] = measured <= ceiling

    if args.json:
        print(json.dumps({"live": live, "static": static}, indent=2, ensure_ascii=False))
        return 0 if live["ok"] else 1

    print("Live prompt budget (measured, not estimated)")
    print(f"  model                {live['model']}")
    print(f"  always-on tools      {live['tool_count']}")
    print(f"  system prompt        {live['system_chars']:,} chars")
    print(f"  MEASURED prompt      {measured:,} tokens")
    print(f"  static estimate      {estimate:,} tokens (chars/3.8)")
    delta = int(live["delta_tokens"])
    sign = "+" if delta >= 0 else ""
    print(f"  delta                {sign}{delta:,} tokens ({sign}{(delta / max(estimate, 1)) * 100:.1f}%)")
    print(f"  context window       {live['num_ctx']:,} tokens")
    print(f"  headroom             {live['headroom_tokens']:,} tokens")
    print(f"  ceiling              {ceiling:,} tokens")
    if not live["ok"]:
        print(f"FAIL: the live prompt ({measured:,}) exceeds the ceiling ({ceiling:,})")
        return 1
    print(f"PASS: the live prompt fits with {live['headroom_tokens']:,} tokens to spare")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
