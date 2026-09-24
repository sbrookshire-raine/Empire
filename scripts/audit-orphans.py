"""Reference-graph audit: which files in this repo are actually referenced anywhere?

Answers "is this file connected to something, or is it leftover junk?" for scripts, modules and
tests, by counting references to each file's stem across the repo and splitting them by referrer:
code (pipeline/frontend/mcp), tests, scripts, docs, and other (`.bat`, configs, HTML, env files).

Reading the result:

- `code` / `script` / `test` / `other` > 0 → wired. Keep.
- `doc` only → documented but unwired: document its purpose or retire it.
- all zero (`<-- ORPHAN`) → verify by hand before removing: some files are wired *outside* the repo
  (Windows Task Scheduler, `.cursor/` hooks, batch entry points), and test files are wired by pytest
  discovery, so a test file with zero refs is normal.

Run from the repo root (venv python):

    .\\venv\\Scripts\\python.exe scripts\\audit-orphans.py
    .\\venv\\Scripts\\python.exe scripts\\audit-orphans.py --area scripts

The 2026-09-24 pass (see docs/REFACTOR_EVAL.md) found zero orphan modules in pipeline/frontend/mcp
and a handful of scripts wired only outside the repo.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", ".eve", ".output", "dev-runtime",
    "eve-audit", "tmp", "__pycache__", ".mypy_cache", ".pytest_cache", "pb_data",
    "site-packages",
}
TEXT_EXT = {".py", ".ts", ".js", ".ps1", ".md", ".json", ".html", ".bat", ".cmd", ".env", ".example"}
CANDIDATE_EXT = {".py", ".ps1", ".js", ".ts"}


def iter_files(exts: set[str] | None = None):
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if exts and path.suffix.lower() not in exts:
            continue
        yield path


def load_corpus() -> dict[Path, str]:
    corpus: dict[Path, str] = {}
    for path in iter_files(TEXT_EXT):
        try:
            if path.stat().st_size > 1_500_000:
                continue
            corpus[path] = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
    return corpus


def classify(source: Path) -> str:
    rel = source.relative_to(ROOT)
    if "tests" in rel.parts:
        return "test"
    if rel.parts[0] in {"pipeline", "frontend", "mcp"}:
        return "module"
    if rel.parts[0] == "scripts":
        return "script"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="Find orphaned (unreferenced) files.")
    parser.add_argument("--area", default="", help="limit to a top-level folder, e.g. scripts")
    args = parser.parse_args()

    corpus = load_corpus()
    candidates = [p for p in corpus if p.suffix.lower() in CANDIDATE_EXT]
    if args.area:
        candidates = [p for p in candidates if p.relative_to(ROOT).parts[0] == args.area]

    rows = []
    for source in sorted(candidates):
        stem = source.stem
        if len(stem) < 4 or stem in {"main", "test", "run", "index", "setup", "__init__"}:
            continue
        pattern = re.compile(rf"\b{re.escape(stem)}\b")
        hits = {"code": 0, "test": 0, "script": 0, "doc": 0, "other": 0}
        for other, text in corpus.items():
            if other == source or not pattern.search(text):
                continue
            kind = classify(other)
            hits["code" if kind == "module" else kind] += 1
        outside = sum(v for k, v in hits.items() if k != "test")
        rows.append((outside, hits, source))

    rows.sort(key=lambda r: (r[0], r[1]["doc"], r[1]["test"]))
    print(f"{'out':>4} {'test':>5} {'code':>5} {'scr':>4} {'doc':>4} {'oth':>4}  file")
    for outside, hits, source in rows:
        rel = source.relative_to(ROOT).as_posix()
        wired = hits["code"] + hits["script"] + hits["other"]
        if outside == 0:
            flag = "  <-- ORPHAN (verify: scheduler/hooks/batch?)"
        elif wired == 0 and hits["test"] == 0:
            flag = "  <-- docs only"
        else:
            flag = ""
        print(
            f"{outside:>4} {hits['test']:>5} {hits['code']:>5} {hits['script']:>4} "
            f"{hits['doc']:>4} {hits['other']:>4}  {rel}{flag}"
        )
    print(f"\n{len(rows)} candidates scanned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())