"""CLI for Wikipedia research scratchpad + Error Book."""

from __future__ import annotations

import argparse
import json
import sys

from pipeline import wiki_scratchpad


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Wiki scratchpad / error book")
    sub = parser.add_subparsers(dest="cmd", required=True)
    up = sub.add_parser("upsert")
    up.add_argument("text")
    up.add_argument("--title", default="")
    up.add_argument("--session", default="")
    rd = sub.add_parser("read")
    rd.add_argument("--session", default="")
    rd.add_argument("--errors", action="store_true")
    clr = sub.add_parser("clear")
    clr.add_argument("--session", default="")
    err = sub.add_parser("error")
    err.add_argument("--query", required=True)
    err.add_argument("--reason", default="miss")
    err.add_argument("--title", default="")
    err.add_argument("--year", default="2026")
    args = parser.parse_args(argv)

    if args.cmd == "upsert":
        result = wiki_scratchpad.scratch_upsert(
            args.text, session_id=args.session, title=args.title
        )
    elif args.cmd == "read":
        result = wiki_scratchpad.scratch_read(args.session)
        if args.errors:
            result["errors"] = wiki_scratchpad.error_book_recent(limit=20)
    elif args.cmd == "clear":
        result = wiki_scratchpad.scratch_clear(args.session)
    else:
        result = wiki_scratchpad.error_book_append(
            query=args.query,
            reason=args.reason,
            title=args.title,
            year=args.year,
        )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
