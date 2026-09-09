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
CORE_PROFILE = WORKBENCH_ROOT / "00_Core_Profile"
CORE_MANIFEST = CORE_PROFILE / "eve_core_manifest.json"
CATALOG_PATH = CORE_PROFILE / "projects_catalog.json"
DAZE_PROFILE = CORE_PROFILE / "DAZE_PRODUCT_PROFILE.md"

FLATTEN_NAME_RE = re.compile(
    r"^(?P<prefix>(?:sbx2020|sbrookshire-raine)_)?(?P<name>.+?)_flattened(?:_\d+)?\.txt$",
    re.IGNORECASE,
)

DAZE_MEMORY_RE = re.compile(r"^daze[\W_!]", re.IGNORECASE)

CANONICAL_PRODUCTS: dict[str, dict[str, object]] = {
    "daze": {
        "display_name": "DAZE (Daily OS)",
        "kind": "product",
        "live_url": "https://daze-murex.vercel.app/",
        "empire_url": "http://127.0.0.1:8080/daze.html",
        "product_stack": "React · Vite · Firebase · Vercel",
        "empire_stack": "Alpine · PocketBase · /api/daze (Phase 5)",
        "empire_status": "working",
        "summary": (
            "Live: full radial Daily OS with concentric overlap tracks, tabbed logs, and Firebase sync. "
            "EMPIRE: sovereign dual-ring dial (planned + actual), conflict glow, Eve Time Reclaim tools."
        ),
    },
}


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
    alternate_flattened: list[str]
    in_eve_core: bool
    nlm_topics: list[str]
    kind: str
    live_url: str
    empire_url: str
    product_stack: str
    empire_stack: str
    empire_status: str
    summary: str
    profile_file: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return cleaned or "project"


def _is_daze_memory_path(path: Path) -> bool:
    stem = path.stem.casefold()
    if stem == "daze":
        return True
    if DAZE_MEMORY_RE.match(path.name):
        return True
    if stem.startswith("daze_") or stem.startswith("daze "):
        return True
    return False


def _blank_record(project_id: str, *, name: str, display_name: str, kind: str) -> ProjectRecord:
    return {
        "id": project_id,
        "name": name,
        "display_name": display_name,
        "github_owner": "",
        "github_repo": "",
        "flattened_file": "",
        "flattened_source": "",
        "flattened_at": "",
        "source_file_count": 0,
        "flattened_bytes": 0,
        "memory_files": [],
        "alternate_flattened": [],
        "in_eve_core": False,
        "nlm_topics": [],
        "kind": kind,
    }


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
            "alternate_flattened": [],
            "in_eve_core": False,
            "nlm_topics": [],
            "kind": "codebase",
        }
    return projects


def _ensure_daze_record(projects: dict[str, ProjectRecord]) -> ProjectRecord:
    overlay = CANONICAL_PRODUCTS["daze"]
    record = projects.get("daze")
    if record is None:
        record = _blank_record(
            "daze",
            name="DAZE",
            display_name=str(overlay["display_name"]),
            kind=str(overlay["kind"]),
        )
        projects["daze"] = record
    else:
        record["display_name"] = str(overlay["display_name"])
        record["kind"] = str(overlay["kind"])
    record.setdefault("alternate_flattened", [])
    record.setdefault("memory_files", [])
    for key in (
        "live_url",
        "empire_url",
        "product_stack",
        "empire_stack",
        "empire_status",
        "summary",
    ):
        record[key] = overlay[key]  # type: ignore[literal-required]
    if DAZE_PROFILE.is_file():
        record["profile_file"] = str(DAZE_PROFILE)
    return record


def _memory_projects(
    projects: dict[str, ProjectRecord],
    *,
    eve_core_paths: set[str],
) -> None:
    if not MEMORY_BANK.is_dir():
        return

    evolution = projects.setdefault(
        "empire-evolution",
        _blank_record(
            "empire-evolution",
            name="Rain to Empire",
            display_name="Rain to Empire (evolution notes)",
            kind="evolution",
        ),
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
                _blank_record(
                    project_id,
                    name=topic or name,
                    display_name=f"NLM: {topic or name}",
                    kind="nlm",
                ),
            )
            record["nlm_topics"] = [topic or name]
            record["memory_files"].append(rel)
            if in_core:
                record["in_eve_core"] = True
            continue

        if _is_daze_memory_path(path):
            daze = _ensure_daze_record(projects)
            if rel not in daze["memory_files"]:
                daze["memory_files"].append(rel)
            if in_core:
                daze["in_eve_core"] = True
            continue

        if any(token in lower for token in ("forge", "empire", "workbench")):
            project_id = _slug(path.stem)
            record = projects.setdefault(
                project_id,
                _blank_record(
                    project_id,
                    name=path.stem,
                    display_name=path.stem,
                    kind="notes",
                ),
            )
            record["memory_files"].append(rel)
            if in_core:
                record["in_eve_core"] = True


def _consolidate_daze_projects(projects: dict[str, ProjectRecord], *, eve_core_paths: set[str]) -> None:
    daze = _ensure_daze_record(projects)
    profile_path = str(DAZE_PROFILE)
    if DAZE_PROFILE.is_file() and profile_path in eve_core_paths:
        daze["in_eve_core"] = True

    remove_ids: list[str] = []
    for project_id, record in projects.items():
        if project_id == "daze":
            continue
        repo = str(record.get("github_repo") or "").casefold()
        name = str(record.get("name") or "").casefold()
        if repo == "daze" or name == "daze" or project_id.startswith("daze"):
            flat = str(record.get("flattened_file") or "")
            if flat and flat != daze.get("flattened_file"):
                alternates = daze.setdefault("alternate_flattened", [])
                if flat not in alternates:
                    alternates.append(flat)
            if not daze.get("flattened_file") and flat:
                daze["flattened_file"] = flat
                daze["flattened_source"] = str(record.get("flattened_source") or "")
                daze["flattened_at"] = str(record.get("flattened_at") or "")
                daze["source_file_count"] = int(record.get("source_file_count") or 0)
                daze["flattened_bytes"] = int(record.get("flattened_bytes") or 0)
            for mf in record.get("memory_files") or []:
                if mf not in daze["memory_files"]:
                    daze["memory_files"].append(mf)
            if record.get("in_eve_core"):
                daze["in_eve_core"] = True
            remove_ids.append(project_id)
            continue
        # Memory-only fragments that slipped through with daze slug stems
        if project_id.startswith("daze-") and record.get("kind") == "notes":
            for mf in record.get("memory_files") or []:
                if mf not in daze["memory_files"]:
                    daze["memory_files"].append(mf)
            if record.get("in_eve_core"):
                daze["in_eve_core"] = True
            remove_ids.append(project_id)

    for project_id in remove_ids:
        projects.pop(project_id, None)


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
    if DAZE_PROFILE.is_file():
        paths.add(str(DAZE_PROFILE))
    return paths


def build_project_catalog() -> dict[str, object]:
    eve_core_paths = load_eve_core_paths()
    projects = _flatten_projects()
    _memory_projects(projects, eve_core_paths=eve_core_paths)
    _consolidate_daze_projects(projects, eve_core_paths=eve_core_paths)
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
            0 if item.get("kind") == "product" else 1,
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
    memory_files = record.get("memory_files") or []
    alternate_flat = record.get("alternate_flattened") or []
    payload: dict[str, object] = {
        "id": record.get("id"),
        "displayName": record.get("display_name") or record.get("name"),
        "kind": record.get("kind"),
        "inEveCore": bool(record.get("in_eve_core")),
        "hasCode": bool(record.get("flattened_file")),
        "sourceFileCount": int(record.get("source_file_count") or 0),
        "memoryFileCount": len(memory_files),
        "flattenedAt": record.get("flattened_at") or "",
        "flattenedSource": record.get("flattened_source") or "",
        "githubOwner": record.get("github_owner") or "",
        "githubRepo": record.get("github_repo") or "",
        "memoryFiles": [Path(str(path)).name for path in memory_files[:8]],
        "alternateFlattenedCount": len(alternate_flat),
    }
    if record.get("live_url"):
        payload["liveUrl"] = record.get("live_url")
    if record.get("empire_url"):
        payload["empireUrl"] = record.get("empire_url")
    if record.get("product_stack"):
        payload["productStack"] = record.get("product_stack")
    if record.get("empire_stack"):
        payload["empireStack"] = record.get("empire_stack")
    if record.get("empire_status"):
        payload["empireStatus"] = record.get("empire_status")
    if record.get("summary"):
        payload["summary"] = record.get("summary")
    return payload
