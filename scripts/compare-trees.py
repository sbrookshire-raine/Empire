r"""Compare two directory trees by relative path + size (read-only; writes nothing anywhere).

Built for the estate question this repo keeps having to ask: is a copy a *backup*, or just a folder that looks
like one? A first pass on `I:\weaviate_v2_archive` vs `D:\weaviate_v2_archive` reported "71 files short", which
turned out to be a *net* figure hiding 498 vs 427 differing paths — every one of them a Weaviate write-ahead
log. The lesson is built into the tool: name the difference, never just count it (ESTATE_INVENTORY.md, §6 item 6).

    .\venv\Scripts\python.exe scripts\compare-trees.py D:\wiki_md I:\wiki_md
    .\venv\Scripts\python.exe scripts\compare-trees.py <left> <right> --summary-only --list 0
    .\venv\Scripts\python.exe scripts\compare-trees.py <src> <dst> --exclude "data,.git,.venv" --labels "src,dst"

`--exclude` matters for copies made with `robocopy /XD`: without it every deliberately-excluded directory shows
up as "only in source" and masks whether the files that *were* meant to copy actually match.

Exits 0 when the trees match, 1 when they do not, 2 on a bad path — so it works as a check, not only a report.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def walk(root: Path, depth: int | None, exclude: frozenset[str] = frozenset()) -> dict[str, int]:
    """Relative path -> size. `--depth` bounds the walk, `--exclude` drops named dirs/files on both sides."""
    files: dict[str, int] = {}
    root_depth = len(root.parts)
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        if exclude:
            dirnames[:] = [d for d in dirnames if d not in exclude]
        if depth is not None and (len(current.parts) - root_depth) >= depth:
            dirnames[:] = []
            continue
        for name in filenames:
            if exclude and name in exclude:
                continue
            path = current / name
            relative = path.relative_to(root).as_posix()
            if exclude and any(part in exclude for part in relative.split("/")[:-1]):
                continue
            try:
                size = path.stat().st_size
            except OSError:
                size = -1
            files[relative] = size
    return files


def total_gb(files: dict[str, int]) -> float:
    return sum(size for size in files.values() if size > 0) / 1e9


def report(label: str, left: dict[str, int], right: dict[str, int], shown: int) -> int:
    only_left = sorted(set(left) - set(right))
    only_right = sorted(set(right) - set(left))
    size_diff = sorted(key for key in set(left) & set(right) if left[key] != right[key])

    print(f"\nonly in {label[0]}: {len(only_left)}   only in {label[1]}: {len(only_right)}"
          f"   in both but different size: {len(size_diff)}")

    for title, keys in (
        (f"only in {label[0]}", only_left),
        (f"only in {label[1]}", only_right),
        ("size differs", size_diff),
    ):
        if not keys:
            continue
        print(f"\n-- {title} (showing {min(shown, len(keys))} of {len(keys)}) --")
        for key in keys[:shown]:
            shown_left = left.get(key, "-")
            shown_right = right.get(key, "-")
            print(f"   {key}   left={shown_left}   right={shown_right}")

    return 1 if (only_left or only_right or size_diff) else 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Compare two trees by relative path and size.")
    parser.add_argument("left")
    parser.add_argument("right")
    parser.add_argument("--depth", type=int, default=None, help="bound the walk (useful for huge trees)")
    parser.add_argument("--list", type=int, default=20, help="how many differing paths to print")
    parser.add_argument("--summary-only", action="store_true", help="print counts and sizes only")
    parser.add_argument("--labels", default="", help="two names for the sides, e.g. D:,I:")
    parser.add_argument(
        "--exclude",
        default="",
        help="comma-separated directory or file names to skip on BOTH sides (for copies made with robocopy /XD)",
    )
    args = parser.parse_args()

    exclude = frozenset(part.strip() for part in args.exclude.split(",") if part.strip())

    left_root, right_root = Path(args.left), Path(args.right)
    for root in (left_root, right_root):
        if not root.is_dir():
            print(f"not a directory: {root}")
            return 2

    labels = tuple(args.labels.split(",")) if args.labels.count(",") == 1 else (str(left_root), str(right_root))
    left = walk(left_root, args.depth, exclude)
    right = walk(right_root, args.depth, exclude)

    scope = f" (walk bounded to depth {args.depth})" if args.depth is not None else ""
    if exclude:
        scope += f" (excluding: {', '.join(sorted(exclude))})"
    print(f"{labels[0]}: {len(left)} files, {total_gb(left):.2f} GB{scope}")
    print(f"{labels[1]}: {len(right)} files, {total_gb(right):.2f} GB{scope}")

    if args.summary_only:
        only_left = len(set(left) - set(right))
        only_right = len(set(right) - set(left))
        size_diff = sum(1 for key in set(left) & set(right) if left[key] != right[key])
        print(f"\nonly in {labels[0]}: {only_left}   only in {labels[1]}: {only_right}"
              f"   size differs: {size_diff}")
        return 1 if (only_left or only_right or size_diff) else 0

    return report(labels, left, right, args.list)


if __name__ == "__main__":
    raise SystemExit(main())
