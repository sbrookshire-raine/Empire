"""Skill compiler — inventory + Build1 3-Bin heuristic triage for Cursor skills.

Ported from Gumloop FVCC Skill Builder playbook. Rule-based (no cloud LLM required).
Outputs manifest JSON + markdown matrix under harvest_cache or Resource Queue.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import zipfile
from pathlib import Path
from typing import Any

DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_HARVEST_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\harvest_cache",
    )
)
DEFAULT_SKILLS_DIR = Path(os.environ.get("EMPIRE_CURSOR_SKILLS_DIR", r"C:\EMPIRE\.cursor\skills"))

BUILD1_COMPONENTS = (
    "ollama",
    "pocketbase",
    "cognee",
    "fastmcp",
    "htmx",
    "alpine",
    "sqlite",
    "mcp",
)

CLOUD_ONLY_PATTERNS = re.compile(
    r"\b("
    r"firebase|supabase|openai\.com/api|anthropic\.com/api|"
    r"vercel(?!.*local)|netlify(?!.*local)|"
    r"gumloop\.com(?!.*scrape)|"
    r"requires?\s+(a\s+)?(paid|proprietary)\s+cloud"
    r")\b",
    re.IGNORECASE,
)

COMPETING_STACK = re.compile(
    r"\b(react|next\.js|vue|svelte|firebase|supabase)\b",
    re.IGNORECASE,
)

DUPLICATE_HINTS: dict[str, str] = {
    "css-framework": "css-framework-reference",
    "css-utility": "css-utility-snippets",
    "icon-library": "icon-library-lookup",
    "web-researcher": "web-researcher",
    "code-analyst": "code-analyst",
}


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="skill-", suffix=".tmp", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def _read_skill_md(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    name = path.parent.name
    description = ""
    m = re.search(r"^description:\s*(.+)$", text, re.M)
    if m:
        description = m.group(1).strip().strip('"')
    elif re.search(r"^#\s+", text, re.M):
        description = re.search(r"^#\s+(.+)$", text, re.M).group(1).strip()  # type: ignore[union-attr]
    excerpt = text[:400].replace("\n", " ")
    return {
        "name": name,
        "path": str(path),
        "source": str(path.parent.parent),
        "description": description,
        "excerpt": excerpt,
        "content_hash": hashlib.sha256(text.encode("utf-8")).hexdigest()[:16],
    }


def _iter_skill_files(root: Path) -> list[Path]:
    if root.is_file() and root.suffix.lower() == ".zip":
        return _skills_from_zip(root)
    if root.is_dir():
        return sorted(root.rglob("SKILL.md"))
    return []


def _skills_from_zip(zip_path: Path) -> list[Path]:
    extracted: list[Path] = []
    staging = zip_path.parent / f".skill_inventory_{zip_path.stem}"
    staging.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(staging)
    extracted.extend(sorted(staging.rglob("SKILL.md")))
    return extracted


def inventory_sources(
    paths: list[str | Path] | None = None,
    *,
    include_default_skills: bool = True,
) -> dict[str, Any]:
    """Build skill inventory from paths, zips, and optionally .cursor/skills."""
    roots: list[Path] = []
    if include_default_skills and DEFAULT_SKILLS_DIR.is_dir():
        roots.append(DEFAULT_SKILLS_DIR)
    for raw in paths or []:
        p = Path(raw)
        if p.exists():
            roots.append(p)

    entries: list[dict[str, str]] = []
    seen_hashes: set[str] = set()
    for root in roots:
        for skill_md in _iter_skill_files(root):
            try:
                row = _read_skill_md(skill_md)
            except OSError as exc:
                continue
            if row["content_hash"] in seen_hashes:
                continue
            seen_hashes.add(row["content_hash"])
            row["index"] = len(entries)
            entries.append(row)

    return {"ok": True, "count": len(entries), "entries": entries}


def _components_in_text(text: str) -> list[str]:
    lower = text.lower()
    found: list[str] = []
    mapping = {
        "ollama": "Ollama",
        "pocketbase": "PocketBase",
        "sqlite": "PocketBase",
        "cognee": "Cognee",
        "fastmcp": "FastMCP",
        "htmx": "HTMX/Alpine",
        "alpine": "HTMX/Alpine",
        "mcp": "FastMCP",
    }
    for key, label in mapping.items():
        if key in lower and label not in found:
            found.append(label)
    return found


def heuristic_three_bin(entry: dict[str, str], *, batch_names: set[str]) -> dict[str, Any]:
    """Assign Bin 1/2/3 using Build1 rubric (rule-based)."""
    name = entry.get("name", "")
    blob = f"{entry.get('description', '')} {entry.get('excerpt', '')}".lower()

    for hint, canonical in DUPLICATE_HINTS.items():
        if hint in name.lower() and name != canonical and canonical in batch_names:
            return {
                "index": entry.get("index"),
                "name": name,
                "path": entry.get("path"),
                "source": entry.get("source"),
                "bin": 2,
                "reason": f"Near-duplicate of existing skill '{canonical}'.",
                "build1_components": _components_in_text(blob) or ["none"],
                "duplicate_of": canonical,
            }

    if CLOUD_ONLY_PATTERNS.search(blob) and not any(c in blob for c in BUILD1_COMPONENTS):
        return {
            "index": entry.get("index"),
            "name": name,
            "path": entry.get("path"),
            "source": entry.get("source"),
            "bin": 2,
            "reason": "Hard cloud-only SaaS dependency with no local swap evident.",
            "build1_components": ["none"],
            "duplicate_of": None,
        }

    if COMPETING_STACK.search(blob) and "htmx" not in blob:
        return {
            "index": entry.get("index"),
            "name": name,
            "path": entry.get("path"),
            "source": entry.get("source"),
            "bin": 2,
            "reason": "Competing SPA/cloud stack component conflicts with Build1 frontend rules.",
            "build1_components": ["none"],
            "duplicate_of": None,
        }

    components = _components_in_text(blob)
    if components or any(
        kw in blob
        for kw in (
            "infra-agnostic",
            "local-first",
            "offline",
            "reference",
            "lookup",
            "scrape",
            "markdown",
            "fastmcp",
        )
    ):
        return {
            "index": entry.get("index"),
            "name": name,
            "path": entry.get("path"),
            "source": entry.get("source"),
            "bin": 1,
            "reason": "Compatible with Build1 local stack or infra-agnostic reference tooling.",
            "build1_components": components or ["none"],
            "duplicate_of": None,
        }

    return {
        "index": entry.get("index"),
        "name": name,
        "path": entry.get("path"),
        "source": entry.get("source"),
        "bin": 3,
        "reason": "Ambiguous Build1 fit — Architect review recommended.",
        "build1_components": components or ["none"],
        "duplicate_of": None,
    }


def triage_inventory(
    inventory: dict[str, Any],
) -> dict[str, Any]:
    entries = inventory.get("entries") or []
    batch_names = {str(e.get("name")) for e in entries}
    verdicts = [heuristic_three_bin(e, batch_names=batch_names) for e in entries]
    bins = {1: 0, 2: 0, 3: 0}
    for v in verdicts:
        bins[int(v["bin"])] = bins.get(int(v["bin"]), 0) + 1
    return {
        "ok": True,
        "count": len(verdicts),
        "bins": bins,
        "verdicts": verdicts,
    }


def write_triage_manifest(
    triage: dict[str, Any],
    *,
    out_dir: Path | None = None,
    write_files: bool = True,
) -> dict[str, Any]:
    out = out_dir or DEFAULT_CACHE_DIR
    verdicts = triage.get("verdicts") or []
    bins = triage.get("bins") or {}

    json_path = out / "skill_triage_manifest.json"
    md_path = out / "SKILL_TRIAGE_MANIFEST.md"

    if write_files:
        _atomic_write(json_path, json.dumps(triage, indent=2))
        lines = [
            "# Skill Triage Manifest (Build1 heuristic)",
            "",
            f"Generated by EMPIRE skill_compiler | total: {triage.get('count', 0)}",
            "",
            "## Summary",
            "",
            f"- Bin 1 (keep): {bins.get(1, 0)}",
            f"- Bin 2 (reject): {bins.get(2, 0)}",
            f"- Bin 3 (review): {bins.get(3, 0)}",
            "",
            "## Verdicts",
            "",
            "| Bin | Skill | Reason | Components |",
            "|---|---|---|---|",
        ]
        for v in verdicts:
            comps = ", ".join(v.get("build1_components") or [])
            lines.append(
                f"| {v.get('bin')} | `{v.get('name')}` | {v.get('reason')} | {comps} |"
            )
        _atomic_write(md_path, "\n".join(lines) + "\n")

    return {
        "ok": True,
        "json_path": str(json_path) if write_files else None,
        "markdown_path": str(md_path) if write_files else None,
        "bins": bins,
    }


def run_inventory_and_triage(
    paths: list[str | Path] | None = None,
    *,
    out_dir: Path | None = None,
    include_default_skills: bool = True,
) -> dict[str, Any]:
    inventory = inventory_sources(paths, include_default_skills=include_default_skills)
    if not inventory.get("ok"):
        return inventory
    triage = triage_inventory(inventory)
    manifest = write_triage_manifest(triage, out_dir=out_dir)
    return {
        "ok": True,
        "inventory_count": inventory.get("count"),
        "bins": manifest.get("bins"),
        "json_path": manifest.get("json_path"),
        "markdown_path": manifest.get("markdown_path"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE skill inventory + 3-Bin triage")
    parser.add_argument(
        "paths",
        nargs="*",
        help="Zip files or directories containing SKILL.md trees",
    )
    parser.add_argument(
        "--no-default-skills",
        action="store_true",
        help="Skip scanning C:/EMPIRE/.cursor/skills",
    )
    parser.add_argument("-o", "--output-dir", type=Path, default=DEFAULT_CACHE_DIR)
    args = parser.parse_args(argv)

    result = run_inventory_and_triage(
        args.paths,
        out_dir=args.output_dir,
        include_default_skills=not args.no_default_skills,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
