"""CLI for section-aware Wikipedia markdown reads."""

from __future__ import annotations

import argparse
import json
import sys

from pipeline.wiki_read_lead import wiki_read


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read wiki lead/section")
    parser.add_argument("cmd", choices=["read"])
    parser.add_argument("title")
    parser.add_argument("--year", default="2026")
    parser.add_argument("--section", default="")
    parser.add_argument("--question", default="")
    args = parser.parse_args(argv)
    result = wiki_read(
        args.title,
        args.year,
        section=args.section,
        user_question=args.question,
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
