"""CLI for the on-demand tool documentation registry (R-03).

Eve's `tool_docs` tool calls this: `list` gives the compact index, `<tool>` gives one tool's deep
syntax. Kept tiny on purpose — it replaces prompt weight, so it must not become prompt weight.
"""

from __future__ import annotations

import argparse
import json
import sys

from pipeline.tool_registry import doc, index


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Tool documentation registry lookup.")
    parser.add_argument("name", nargs="?", default="", help="tool name; omit to list all")
    parser.add_argument("--max-chars", type=int, default=2400)
    args = parser.parse_args(argv)

    if not args.name.strip():
        entries = index()
        payload = {
            "ok": True,
            "count": len(entries),
            "tools": [
                {"name": entry["name"], "one_line": entry["one_line"], "toolbelt": entry["toolbelt"]}
                for entry in entries
            ],
        }
        print(json.dumps(payload))
        return 0

    result = doc(args.name, max_chars=args.max_chars)
    print(json.dumps(result))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())