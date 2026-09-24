"""List and filter the idea store (`docs/ideas/*.md`) — thin CLI over `pipeline.idea_store`.

    .\\venv\\Scripts\\python.exe scripts\\list-ideas.py
    .\\venv\\Scripts\\python.exe scripts\\list-ideas.py --status idea --area media
    .\\venv\\Scripts\\python.exe scripts\\list-ideas.py --show media-limb-yt-dlp
    .\\venv\\Scripts\\python.exe scripts\\list-ideas.py --json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pipeline.idea_store import IDEAS_DIR, STATUSES, filter_ideas, load_ideas, read_idea  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="List ideas from docs/ideas front matter.")
    parser.add_argument("--status", default="", help=f"one of {', '.join(STATUSES)}")
    parser.add_argument("--area", default="", help="filter by area, e.g. media")
    parser.add_argument("--show", default="", help="print one idea in full (slug or E-xx)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if args.show.strip():
        idea = read_idea(args.show)
        if not idea.get("ok"):
            print(json.dumps(idea))
            return 1
        print(f"# {idea['id']} · {idea['title']}\n")
        print(f"status={idea['status']} area={idea['area']} priority={idea['priority']}")
        print(f"file={idea['path']}\n")
        print(idea["body"])
        return 0

    ideas = filter_ideas(load_ideas(), status=args.status, area=args.area)
    if args.json:
        print(json.dumps({"count": len(ideas), "ideas": ideas}, indent=2))
        return 0

    if not ideas:
        print("no ideas match")
        return 0

    print(f"{'id':<6} {'status':<12} {'area':<10} {'prio':<7} title")
    for idea in ideas:
        print(
            f"{idea['id']:<6} {idea['status']:<12} {idea['area']:<10} "
            f"{idea['priority']:<7} {idea['title'][:60]}"
        )
    print(f"\n{len(ideas)} idea(s)  ·  {IDEAS_DIR.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())