#!/usr/bin/env python3
"""Print the Title DNS index path the RUNTIME would use, for a given year.

Why this exists
---------------
`mechanic-green.ps1` used to hardcode `I:\\EMPIRE_DATA\\wiki-reports\\2026\\title-index.sqlite`
as the precondition for the wiki extract battery. The runtime does not work
that way: `pipeline.wiki_ops_paths.reports_root()` prefers the override, then
drive I:, then drive D:, and only then falls back. On a machine where the T7
is not mounted but the corpus lives on D:, the gate therefore SKIPPED the
wiki battery while the runtime happily served wiki lookups from the very
same corpus. A green gate that skipped a real check proved nothing about
the wiki limb.

This helper asks the runtime where the index is, so the gate and the runtime
can never disagree about it.

Usage:
    .\\venv\\Scripts\\python.exe scripts\\wiki-index-path.py [year]

Prints the resolved path on stdout when the index file exists, and prints
nothing (exit 1) when there is no corpus for that year.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def resolve(year: str) -> Path | None:
    """The index path the runtime would use, or None when there is no corpus."""

    from pipeline.wiki_title_dns import default_index_path

    try:
        path = default_index_path(year)
    except Exception:  # noqa: BLE001 - a missing corpus is not an error here
        return None
    try:
        return path if path.is_file() else None
    except OSError:
        return None


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    year = args[0].strip() if args and args[0].strip() else "2026"
    path = resolve(year)
    if path is None:
        return 1
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
