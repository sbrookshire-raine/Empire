"""Build a verifiable project catalog from workbench harvest artifacts."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import TypedDict

WORKBENCH_ROOT = Path(r"C:\Empire_Workbench")
FLAT_DIR = WORKBENCH_ROOT / "03_Active_Tools"
MEMORY_BANK = WORKBENCH_ROOT / "01_Memory_Bank"
CORE_MANIFEST = WORKBENCH_ROOT / "00_Core_Profile" / "eve_core_manifest.json"
CATALOG_PATH = WORKBENCH_ROOT / "00_Core_Profile" / "projects_catalog.json"

FLATTEN_NAME_RE = re.compile(
    r"^(?P<prefix>(?:sbx2020|sbrookshire-raine)_)?(?P<name>.+?)_flattened(?:_\d+)?\.txt$",
    re.IGNORECASE,
)


class ProjectRecord(TypedDict, total=False):
    id: str
    name: str
    display_name: str
    github_owner: str
    github_repo: str
    flattened_file: str
    flattened_source: str
    flattened_at: str
    source_file_count: int
    flattened_bytes: int
    memory_files: list[str]
    in_eve_core: bool
    nlm_topics: list[str]
    kind: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return cleaned or "project"


def _parse_flatten_header(path: Path) -> dict[str, object]:
    meta: dict[str, object] = {
        "flattened_source": "",
        "flattened_at": "",
        "source_file_count": 0,
    }
    try:
        with path.open(encoding="utf-8", errors="ignore") as handle:
            for _ in range(5):
                line = handle.readline()
                if not line:
                    break
                if line.startswith("# Flattened codebase:"):
                    meta["flattened_source"] = line.split(":", 1)[1].strip()
                elif line.startswith("# Generated:"):
                    meta["flattened_at"] = line.split(":", 1)[1].strip()
                elif line.startswith("# Source files included:"):
                    try:
                        meta["source_file_count"] = int(line.split(":", 1)[1].strip())
                    except ValueError:
                        meta["source_file_count"] = 0
    except OSError:
        return meta
    return meta


def _flatten_projects() -> dict[str, ProjectRecord]:
    projects: dict[str, ProjectRecord] = {}
    if not FLAT_DIR.is_dir():
        return projects

    for path in sorted(FLAT_DIR.glob("*_flattened*.txt")):
        match = FLATTEN_NAME_RE.match(path.name)
        if not match:
            continue
        prefix = match.group("prefix") or ""
        repo_name = match.group("name")
        owner = ""
        if prefix.casefold().startswith("sbx2020"):
            owner = "sbx2020"
        elif prefix.casefold().startswith("sbrookshire"):
            owner = "sbrookshire-raine"
        project_id = _slug(f"{owner}-{repo_name}" if owner else repo_name)
        header = _parse_flatten_header(path)
        try:
            size = path.stat().st_size
        except OSError:
            size = 0

        existing = projects.get(project_id)
        if existing and int(existing.get("source_file_count") or 0) >= int(
            header.get("source_file_count") or 0
        ):
            continue

        projects[project_id] = {
            "id": project_id,
            "name": repo_name,
            "display_name": repo_name.replace("_", " ").replace("-", " "),
            "github_owner": owner,
            "github_repo": repo_name,
            "flattened_file": str(path),
            "flattened_source": str(header.get("flattened_source") or ""),
            "flattened_at": str(header.get("flattened_at") or ""),
            "source_file_count": int(header.get("source_file_count") or 0),
            "flattened_bytes": size,
            "memory_files": [],
            "in_eve_core": False,
            "nlm_topics": [],
            "kind": "codebase",
        }
    return projects


def _memory_projects(
    projects: dict[str, ProjectRecord],
    *,
    eve_core_paths: set[str],
) -> None:
    if not MEMORY_BANK.is_dir():
        return

    evolution = projects.setdefault(
        "empire-evolution",
        {
            "id": "empire-evolution",
            "name": "Rain to Empire",
            "display_name": "Rain to Empire (evolution notes)",
            "github_owner": "",
            "github_repo": "",
            "flattened_file": "",
            "flattened_source": "",
            "flattened_at": "",
            "source_file_count": 0,
            "flattened_bytes": 0,
            "memory_files": [],
            "in_eve_core": False,
            "nlm_topics": [],
            "kind": "evolution",
        },
    )

    for path in sorted(MEMORY_BANK.glob("*.md")):
        rel = str(path)
        name = path.name
        lower = name.casefold()
        in_core = rel in eve_core_paths or str(path) in eve_core_paths

        if lower.startswith("p_raine") or "rain to empire" in lower:
            evolution["memory_files"].append(rel)
            if in_core:
                evolution["in_eve_core"] = True
            continue

        if lower.startswith("nlm"):
            topic = re.sub(r"^nlm[\s\-_]*", "", lower, flags=re.I)
            topic = re.sub(r"\s+(cs|ncs).*$", "", topic).strip()
            project_id = _slug(f"nlm-{topic}")
            record = projects.setdefault(
                project_id,
                {
                    "id": project_id,
                    "name": topic or name,
                    "display_name": f"NLM: {topic or name}",
                    "github_owner": "",
                    "github_repo": "",
                    "flattened_file": "",
                    "flattened_source": "",
                    "flattened_at": "",
                    "source_file_count": 0,
                    "flattened_bytes": 0,
                    "memory_files": [],
                    "in_eve_core": False,
                    "nlm_topics": [topic or name],
                    "kind": "nlm",
                },
            )
            record["memory_files"].append(rel)
            if in_core:
                record["in_eve_core"] = True
            continue

        if any(token in lower for token in ("forge", "daze", "empire", "workbench")):
            project_id = _slug(path.stem)
            record = projects.setdefault(
                project_id,
                {
                    "id": project_id,
                    "name": path.stem,
                    "display_name": path.stem,
                    "github_owner": "",
                    "github_repo": "",
                    "flattened_file": "",
                    "flattened_source": "",
                    "flattened_at": "",
                    "source_file_count": 0,
                    "flattened_bytes": 0,
                    "memory_files": [],
                    "in_eve_core": False,
                    "nlm_topics": [],
                    "kind": "notes",
                },
            )
            record["memory_files"].append(rel)
            if in_core:
                record["in_eve_core"] = True


def _link_nlm_to_codebases(projects: dict[str, ProjectRecord]) -> None:
    for record in projects.values():
        if record.get("kind") != "codebase":
            continue
        repo = str(record.get("github_repo") or "").casefold()
        for other in projects.values():
            if other.get("kind") != "nlm":
                continue
            topic = " ".join(other.get("nlm_topics") or []).casefold()
            if repo and (repo in topic or topic in repo):
                other.setdefault("linked_codebases", []).append(record["id"])  # type: ignore[attr-defined]


def load_eve_core_paths() -> set[str]:
    if not CORE_MANIFEST.is_file():
        return set()
    try:
        payload = json.loads(CORE_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    paths: set[str] = set()
    for item in payload.get("files", []):
        if isinstance(item, dict) and item.get("path"):
            paths.add(str(item["path"]))
    return paths


def build_project_catalog() -> dict[str, object]:
    eve_core_paths = load_eve_core_paths()
    projects = _flatten_projects()
    _memory_projects(projects, eve_core_paths=eve_core_paths)
    _link_nlm_to_codebases(projects)

    for record in projects.values():
        if record.get("flattened_file") and record["id"] in {
            "empire",
            "sbrookshire-raine-empire",
        }:
            evolution = projects.get("empire-evolution")
            if evolution is not None:
                evolution.setdefault("linked_codebases", []).append(record["id"])  # type: ignore[attr-defined]

    ordered = sorted(
        projects.values(),
        key=lambda item: (
            0 if item.get("kind") == "evolution" else 1,
            0 if item.get("in_eve_core") else 1,
            -(int(item.get("source_file_count") or 0)),
            str(item.get("display_name") or ""),
        ),
    )
    return {
        "generated_at": _utc_now(),
        "workbench_root": str(WORKBENCH_ROOT),
        "project_count": len(ordered),
        "in_eve_core_count": sum(1 for item in ordered if item.get("in_eve_core")),
        "flattened_count": sum(1 for item in ordered if item.get("flattened_file")),
        "projects": ordered,
    }


def save_project_catalog() -> dict[str, object]:
    catalog = build_project_catalog()
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2), encoding="utf-8")
    return catalog


def load_project_catalog(*, rebuild: bool = False) -> dict[str, object]:
    if rebuild or not CATALOG_PATH.is_file():
        return save_project_catalog()
    try:
        payload = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return save_project_catalog()
    if not isinstance(payload, dict) or not payload.get("projects"):
        return save_project_catalog()
    return payload


def public_project(record: dict[str, object]) -> dict[str, object]:
    return {
        "id": record.get("id"),
        "displayName": record.get("display_name") or record.get("name"),
        "kind": record.get("kind"),
        "inEveCore": bool(record.get("in_eve_core")),
        "hasCode": bool(record.get("flattened_file")),
        "sourceFileCount": int(record.get("source_file_count") or 0),
        "memoryFileCount": len(record.get("memory_files") or []),
        "flattenedAt": record.get("flattened_at") or "",
        "flattenedSource": record.get("flattened_source") or "",
        "githubOwner": record.get("github_owner") or "",
        "githubRepo": record.get("github_repo") or "",
        "memoryFiles": [
            Path(str(path)).name for path in (record.get("memory_files") or [])[:8]
        ],
    }
