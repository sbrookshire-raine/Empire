#!/usr/bin/env python3
"""
Empire Safe Harvester — scan a messy directory, categorize files, flatten codebases.
COPY ONLY — never moves or deletes source files.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SOURCE_ROOT = Path(r"G:\My Drive")

MEMORY_BANK = Path(r"C:\Empire_Workbench\01_Memory_Bank")
SKILLS_PROMPTS = Path(r"C:\Empire_Workbench\02_Skills_and_Prompts")
ACTIVE_TOOLS = Path(r"C:\Empire_Workbench\03_Active_Tools")
INFRASTRUCTURE = Path(r"D:\Empire_Workbench\04_Infrastructure")

MANUAL_MOVE_LOG = INFRASTRUCTURE / "needs_manual_move_log.txt"
HARVEST_SUMMARY = Path(r"C:\Empire_Workbench\harvest_summary.json")
GITHUB_STAGING = Path(r"D:\Empire_Workbench\_github_staging")

DEFAULT_EXTRA_SOURCES = [
    Path(r"G:\My Drive\nov26_lcc_laptop_docs"),
    Path(r"C:\Users\m69nr\OneDrive\Desktop"),
]
DEFAULT_GITHUB_USERS = ["sbx2020", "sbrookshire-raine"]

INFRA_EXTENSIONS = {".gguf", ".db", ".sqlite", ".bak"}
NOTE_EXTENSIONS = {".md", ".txt", ".csv"}
FLATTEN_EXTENSIONS = {".py", ".ts", ".js", ".md"}
CODEBASE_MARKERS = ("package.json", "requirements.txt", ".git")

SKIP_DIR_NAMES = {"node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".next"}
PROMPT_KEYWORDS = re.compile(r"(prompt|gem|rule|workflow)", re.IGNORECASE)

CODE_EXTENSIONS = FLATTEN_EXTENSIONS  # used when walking codebases


def ensure_directories() -> None:
    """Create all target directories if they do not exist."""
    for d in (MEMORY_BANK, SKILLS_PROMPTS, ACTIVE_TOOLS, INFRASTRUCTURE):
        d.mkdir(parents=True, exist_ok=True)


def is_hidden(path: Path) -> bool:
    """Return True if any path component is hidden (starts with '.')."""
    return any(part.startswith(".") for part in path.parts)


def should_skip_dir(name: str) -> bool:
    return name in SKIP_DIR_NAMES or name.startswith(".")


def is_codebase_dir(directory: Path) -> bool:
    """A directory is a codebase if it contains any codebase marker."""
    for marker in CODEBASE_MARKERS:
        if (directory / marker).exists():
            return True
    return False


def find_codebase_roots(source: Path) -> list[Path]:
    """
    Find outermost codebase roots so nested package.json folders
    are not flattened separately when inside a parent repo.
    """
    candidates: list[Path] = []
    if not source.is_dir():
        return candidates

    for dirpath, dirnames, _ in _walk_dirs(source):
        current = Path(dirpath)
        if is_codebase_dir(current):
            candidates.append(current.resolve())

    # Keep only shallowest roots (drop any candidate inside another candidate)
    candidates.sort(key=lambda p: (len(p.parts), str(p)))
    roots: list[Path] = []
    for candidate in candidates:
        if not any(_is_under(candidate, root) for root in roots):
            roots.append(candidate)
    return roots


def _is_under(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return child != parent
    except ValueError:
        return False


def _walk_dirs(root: Path):
    """os.walk-style generator that prunes skip/hidden directories."""
    for dirpath, dirnames, filenames in os_walk(root):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        yield dirpath, dirnames, filenames


def os_walk(root: Path):
    """Thin wrapper so we can patch in tests if needed."""
    import os

    for dirpath, dirnames, filenames in os.walk(root):
        yield dirpath, dirnames, filenames


def file_inside_codebase(file_path: Path, codebase_roots: list[Path]) -> bool:
    resolved = file_path.resolve()
    return any(_is_under(resolved, root) or resolved == root for root in codebase_roots)


def unique_dest_path(dest_dir: Path, filename: str) -> Path:
    """Avoid overwriting by appending _1, _2, ... when names collide."""
    target = dest_dir / filename
    if not target.exists():
        return target
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    counter = 1
    while True:
        candidate = dest_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def is_gumloop_json(file_path: Path) -> bool:
    if file_path.suffix.lower() != ".json":
        return False
    name_lower = file_path.name.lower()
    if "gumloop" in name_lower:
        return True
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")[:4096]
        return "gumloop" in text.lower()
    except OSError:
        return False


def is_skills_prompt_file(file_path: Path) -> bool:
    if is_gumloop_json(file_path):
        return True
    return bool(PROMPT_KEYWORDS.search(file_path.stem))


def copy_file(src: Path, dest: Path, stats: dict) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    stats["copied_files"].append({"from": str(src), "to": str(dest)})


def log_infrastructure_path(file_path: Path, log_lines: list[str], stats: dict) -> None:
    line = str(file_path.resolve())
    log_lines.append(line)
    stats["infrastructure_logged"].append(line)


def flatten_codebase(codebase_root: Path, stats: dict, name_prefix: str = "") -> None:
    """Concatenate source files from a codebase into one flattened text file."""
    folder_name = f"{name_prefix}{codebase_root.name}" if name_prefix else codebase_root.name
    safe_name = re.sub(r'[<>:"/\\|?*]', "_", folder_name) or "codebase"
    dest = unique_dest_path(ACTIVE_TOOLS, f"{safe_name}_flattened.txt")

    sections: list[str] = []
    file_count = 0

    for dirpath, dirnames, filenames in _walk_dirs(codebase_root):
        current = Path(dirpath)
        if is_hidden(current.relative_to(codebase_root)) if current != codebase_root else False:
            dirnames.clear()
            continue

        for fname in sorted(filenames):
            fpath = current / fname
            if fpath.suffix.lower() not in FLATTEN_EXTENSIONS:
                continue
            if is_hidden(fpath):
                continue
            try:
                content = fpath.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                sections.append(
                    f"\n{'=' * 72}\n"
                    f"FILE: {fpath}\n"
                    f"ERROR: could not read — {exc}\n"
                )
                continue

            rel = fpath.relative_to(codebase_root)
            sections.append(
                f"\n{'=' * 72}\n"
                f"FILE: {rel}\n"
                f"{'=' * 72}\n"
                f"{content}\n"
            )
            file_count += 1

    header = (
        f"# Flattened codebase: {codebase_root}\n"
        f"# Generated: {datetime.now(timezone.utc).isoformat()}\n"
        f"# Source files included: {file_count}\n"
    )
    dest.write_text(header + "".join(sections), encoding="utf-8")

    stats["flattened_codebases"].append(
        {
            "source": str(codebase_root),
            "destination": str(dest),
            "files_included": file_count,
        }
    )


def load_infra_log_lines() -> list[str]:
    if not MANUAL_MOVE_LOG.exists():
        return []
    return [
        line
        for line in MANUAL_MOVE_LOG.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip()
    ]


def write_infra_log(log_lines: list[str]) -> None:
    seen: set[str] = set()
    unique_log: list[str] = []
    for line in log_lines:
        if line not in seen:
            seen.add(line)
            unique_log.append(line)
    MANUAL_MOVE_LOG.write_text(
        "\n".join(unique_log) + ("\n" if unique_log else ""),
        encoding="utf-8",
    )


def github_flatten_prefix(codebase_root: Path) -> str:
    """Prefix flattened output with GitHub owner when under staging."""
    try:
        rel = codebase_root.resolve().relative_to(GITHUB_STAGING.resolve())
        if len(rel.parts) >= 2:
            return f"{rel.parts[0]}_"
    except ValueError:
        pass
    return ""


def clone_github_repos(users: list[str], staging: Path) -> list[Path]:
    """Shallow-clone GitHub repos into staging; return paths ready to harvest."""
    staging.mkdir(parents=True, exist_ok=True)
    cloned: list[Path] = []

    for user in users:
        result = subprocess.run(
            ["gh", "repo", "list", user, "--limit", "1000", "--json", "name"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            print(f"WARNING: could not list repos for {user}: {result.stderr.strip()}")
            continue

        repos = json.loads(result.stdout or "[]")
        user_dir = staging / user
        user_dir.mkdir(parents=True, exist_ok=True)

        for repo in repos:
            name = repo["name"]
            dest = user_dir / name
            if dest.exists() and (dest / ".git").exists():
                cloned.append(dest)
                continue

            print(f"Cloning {user}/{name} ...")
            clone = subprocess.run(
                ["gh", "repo", "clone", f"{user}/{name}", str(dest), "--", "--depth", "1"],
                capture_output=True,
                text=True,
                check=False,
            )
            if clone.returncode != 0:
                print(f"  WARNING: clone failed: {clone.stderr.strip()}")
                continue
            cloned.append(dest)

    return cloned


def harvest(source: Path, infra_log_lines: list[str]) -> dict:
    """Harvest one source tree. Returns per-source statistics."""
    stats: dict = defaultdict(list)
    stats["errors"] = []
    stats["skipped_source_missing"] = False
    stats["source_root"] = str(source)

    if not source.exists():
        stats["skipped_source_missing"] = True
        stats["errors"].append(f"Source path does not exist: {source}")
        return dict(stats)

    codebase_roots = find_codebase_roots(source)
    stats["codebase_roots_found"] = [str(p) for p in codebase_roots]

    for root in codebase_roots:
        try:
            flatten_codebase(root, stats, name_prefix=github_flatten_prefix(root))
        except OSError as exc:
            stats["errors"].append(f"Flatten failed for {root}: {exc}")

    for dirpath, dirnames, filenames in _walk_dirs(source):
        current = Path(dirpath)
        for fname in filenames:
            fpath = current / fname
            if is_hidden(fpath):
                continue

            ext = fpath.suffix.lower()

            if file_inside_codebase(fpath, codebase_roots):
                continue

            try:
                if ext in INFRA_EXTENSIONS:
                    log_infrastructure_path(fpath, infra_log_lines, stats)
                    continue

                if is_skills_prompt_file(fpath):
                    dest = unique_dest_path(SKILLS_PROMPTS, fpath.name)
                    copy_file(fpath, dest, stats)
                    continue

                if ext in NOTE_EXTENSIONS:
                    dest = unique_dest_path(MEMORY_BANK, fpath.name)
                    copy_file(fpath, dest, stats)
                    continue

            except OSError as exc:
                stats["errors"].append(f"Failed processing {fpath}: {exc}")

    return dict(stats)


def merge_stats(accumulator: dict, new_stats: dict) -> dict:
    """Merge per-source stats into a combined run summary."""
    for key in (
        "copied_files",
        "flattened_codebases",
        "infrastructure_logged",
        "codebase_roots_found",
        "errors",
        "sources_scanned",
    ):
        accumulator.setdefault(key, [])
        if key in new_stats and isinstance(new_stats[key], list):
            accumulator[key].extend(new_stats[key])

    if new_stats.get("skipped_source_missing"):
        accumulator.setdefault("skipped_sources", []).append(new_stats["source_root"])

    return accumulator


def harvest_all(
    sources: list[Path],
    github_users: list[str] | None = None,
) -> dict:
    """Run harvest across multiple local paths and optional GitHub accounts."""
    ensure_directories()

    infra_log_lines = load_infra_log_lines()
    combined: dict = defaultdict(list)
    combined["errors"] = []
    combined["sources_scanned"] = []

    for source in sources:
        print(f"\n--- Harvesting: {source} ---")
        result = harvest(source, infra_log_lines)
        if not result.get("skipped_source_missing"):
            combined["sources_scanned"].append(str(source))
        merge_stats(combined, result)

    if github_users:
        print(f"\n--- Cloning GitHub repos: {', '.join(github_users)} ---")
        repo_paths = clone_github_repos(github_users, GITHUB_STAGING)
        for repo_path in repo_paths:
            print(f"\n--- Harvesting repo: {repo_path} ---")
            result = harvest(repo_path, infra_log_lines)
            if not result.get("skipped_source_missing"):
                combined["sources_scanned"].append(str(repo_path))
            merge_stats(combined, result)

    write_infra_log(infra_log_lines)

    summary = dict(combined)
    summary["harvested_at"] = datetime.now(timezone.utc).isoformat()
    HARVEST_SUMMARY.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def print_summary(stats: dict) -> None:
    """Print a human-readable harvest summary."""
    print("\n" + "=" * 72)
    print("EMPIRE SAFE HARVESTER — SUMMARY")
    print("=" * 72)

    copied = stats.get("copied_files", [])
    memory = [c for c in copied if MEMORY_BANK.as_posix() in c["to"].replace("\\", "/")]
    skills = [c for c in copied if SKILLS_PROMPTS.as_posix() in c["to"].replace("\\", "/")]

    sources = stats.get("sources_scanned") or [stats.get("source_root", SOURCE_ROOT)]
    print(f"\nSources scanned ({len(sources)}):")
    for src in sources:
        print(f"  - {src}")
    print(f"Codebase roots found: {len(stats.get('codebase_roots_found', []))}")
    print(f"Codebases flattened: {len(stats.get('flattened_codebases', []))}")
    print(f"Notes copied -> 01_Memory_Bank: {len(memory)}")
    print(f"Prompts/skills copied -> 02_Skills_and_Prompts: {len(skills)}")
    print(f"Infrastructure paths logged (not copied): {len(stats.get('infrastructure_logged', []))}")

    if stats.get("flattened_codebases"):
        print("\nFlattened codebases:")
        for item in stats["flattened_codebases"]:
            print(f"  • {item['source']}")
            print(f"    -> {item['destination']} ({item['files_included']} files)")

    if stats.get("infrastructure_logged"):
        print(f"\nManual-move log: {MANUAL_MOVE_LOG}")
        print(f"  ({len(stats['infrastructure_logged'])} paths logged)")

    if stats.get("errors"):
        print(f"\nErrors ({len(stats['errors'])}):")
        for err in stats["errors"][:20]:
            print(f"  • {err}")
        if len(stats["errors"]) > 20:
            print(f"  … and {len(stats['errors']) - 20} more")

    print(f"\nFull JSON summary: {HARVEST_SUMMARY}")
    print("=" * 72 + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Empire Safe Harvester")
    parser.add_argument(
        "--source",
        action="append",
        dest="sources",
        help="Local directory to scan (repeatable)",
    )
    parser.add_argument(
        "--github-user",
        action="append",
        dest="github_users",
        help="GitHub account whose repos to shallow-clone and harvest",
    )
    parser.add_argument(
        "--include-default-drive",
        action="store_true",
        help="Also scan G:\\My Drive (full first-pass source)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    sources = [Path(s) for s in (args.sources or DEFAULT_EXTRA_SOURCES)]
    if args.include_default_drive:
        sources.insert(0, SOURCE_ROOT)

    github_users = (
        args.github_users
        if args.github_users is not None
        else ([] if args.sources else DEFAULT_GITHUB_USERS)
    )

    result = harvest_all(sources, github_users=github_users)
    print_summary(result)
