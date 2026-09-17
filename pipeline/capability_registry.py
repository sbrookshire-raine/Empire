"""Capability registry — versioned, hash-verified tool/schema catalog for Eve's arms.

Fail-closed: if a registered arm's declared tool schema or description drifts
from the approved snapshot, it is reported as unapproved so callers refuse it.
This is the governance foundation the arms build on (no code execution here —
read-only registry with sha256 digests).

Trust-domain split (matches docs/EMPIRE_CLARITY.md and the arms plan):
  local_evidence  -> read-only files / documents / read-only SQL (network DENY)
  artifact        -> writable staging/output only (network DENY)
  public_web      -> network allowlist; no private files/shell/memory
  code            -> disposable worktree; no credentials; reviewable diff only
  memory          -> existing Cognee; explicit + provenance only
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
DEFAULT_REGISTRY_DIR = Path(r"C:\EMPIRE\config\eve-capabilities")
REGISTRY_FILENAME = "capability-registry.json"
SNAPSHOT_FILENAME = "tool-schema-snapshot.json"

# Canonical input/output roots used by the arms (real paths, never invented).
DEFAULT_INPUT_DIR = Path(r"C:\Empire_Workbench\00_Resource_Queue")
DEFAULT_OUTPUT_DIR = Path(r"C:\EMPIRE\eve-output")
DEFAULT_STAGING_DIR = Path(r"C:\Empire_Workbench\04_Thought_Experiments\eve_staging")
DEFAULT_WORKTREE_DIR = Path(r"C:\EMPIRE\eve-worktrees")

TRUST_DOMAINS = ("local_evidence", "artifact", "public_web", "code", "memory", "ops")


def registry_dir() -> Path:
    override = os.environ.get("EMPIRE_CAPABILITY_DIR", "").strip()
    if override:
        return Path(override)
    return DEFAULT_REGISTRY_DIR


def registry_path() -> Path:
    return registry_dir() / REGISTRY_FILENAME


def snapshot_path() -> Path:
    return registry_dir() / SNAPSHOT_FILENAME


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_tool_signature(tool: dict[str, Any]) -> str:
    """Deterministic string over the fields that must not silently change."""
    name = str(tool.get("name") or "").strip()
    description = str(tool.get("description") or "").strip()
    schema = json.dumps(tool.get("input_schema") or {}, sort_keys=True)
    return f"{name}\n{description}\n{schema}"


def empty_registry() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "trust_domains": list(TRUST_DOMAINS),
        "capabilities": [],
    }


def load_registry(path: Path | None = None) -> dict[str, Any]:
    p = path or registry_path()
    try:
        parsed = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return empty_registry()
    if not isinstance(parsed, dict):
        return empty_registry()
    parsed.setdefault("capabilities", [])
    parsed.setdefault("schema_version", SCHEMA_VERSION)
    return parsed


def save_registry(registry: dict[str, Any], path: Path | None = None) -> Path:
    p = path or registry_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return p


def register_capability(
    registry: dict[str, Any],
    *,
    capability_id: str,
    label: str,
    domain: str,
    tools: list[dict[str, Any]],
    entrypoint: str = "",
    note: str = "",
) -> dict[str, Any]:
    """Add (or replace) a capability. Each tool gets an approved schema hash."""
    cid = (capability_id or "").strip()
    if not cid:
        raise ValueError("capability_id is required")
    if domain not in TRUST_DOMAINS:
        raise ValueError(f"domain must be one of {TRUST_DOMAINS}")

    caps = registry.get("capabilities")
    if not isinstance(caps, list):
        caps = []
        registry["capabilities"] = caps

    normalized_tools: list[dict[str, Any]] = []
    for tool in tools:
        if not isinstance(tool, dict) or not str(tool.get("name") or "").strip():
            raise ValueError("each tool needs a non-empty name")
        normalized_tools.append(
            {
                "name": str(tool["name"]).strip(),
                "description": str(tool.get("description") or "").strip(),
                "input_schema": tool.get("input_schema") or {},
                "signature_hash": _sha256_text(canonical_tool_signature(tool)),
            }
        )

    entry = {
        "id": cid,
        "label": (label or cid).strip(),
        "domain": domain,
        "entrypoint": entrypoint.strip(),
        "note": note.strip(),
        "tools": normalized_tools,
    }

    for idx, existing in enumerate(caps):
        if isinstance(existing, dict) and existing.get("id") == cid:
            caps[idx] = entry
            break
    else:
        caps.append(entry)
    return registry


def build_snapshot(registry: dict[str, Any]) -> dict[str, Any]:
    """Flat {tool_name: signature_hash} across all capabilities."""
    snapshot: dict[str, str] = {}
    for cap in registry.get("capabilities") or []:
        if not isinstance(cap, dict):
            continue
        for tool in cap.get("tools") or []:
            if isinstance(tool, dict) and tool.get("name"):
                snapshot[str(tool["name"])] = str(tool.get("signature_hash") or "")
    return {"schema_version": SCHEMA_VERSION, "tools": snapshot}


def write_snapshot(registry: dict[str, Any], path: Path | None = None) -> Path:
    p = path or snapshot_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(build_snapshot(registry), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return p


def load_snapshot(path: Path | None = None) -> dict[str, Any]:
    p = path or snapshot_path()
    try:
        parsed = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"schema_version": SCHEMA_VERSION, "tools": {}}
    if not isinstance(parsed, dict):
        return {"schema_version": SCHEMA_VERSION, "tools": {}}
    tools = parsed.get("tools")
    if not isinstance(tools, dict):
        tools = {}
    return {"schema_version": SCHEMA_VERSION, "tools": tools}


def verify_capability(
    capability_id: str,
    *,
    registry: dict[str, Any] | None = None,
    snapshot: dict[str, Any] | None = None,
    path: Path | None = None,
    snapshot_path_: Path | None = None,
) -> dict[str, Any]:
    """Fail-closed check: a capability is approved only if present and hash-stable."""
    reg = registry if registry is not None else load_registry(path)
    snap = snapshot if snapshot is not None else load_snapshot(snapshot_path_)
    tools = snap.get("tools") or {}

    cap = None
    for entry in reg.get("capabilities") or []:
        if isinstance(entry, dict) and entry.get("id") == capability_id:
            cap = entry
            break
    if cap is None:
        return {"ok": False, "approved": False, "reason": "capability not registered"}

    mismatches: list[str] = []
    for tool in cap.get("tools") or []:
        name = str(tool.get("name") or "")
        approved = tools.get(name)
        current = str(tool.get("signature_hash") or "")
        if approved is None:
            mismatches.append(f"{name}: missing from snapshot")
        elif approved != current:
            mismatches.append(f"{name}: schema drifted")

    if mismatches:
        return {
            "ok": False,
            "approved": False,
            "reason": "schema drift",
            "mismatches": mismatches,
        }
    return {"ok": True, "approved": True, "capability": cap.get("id"), "tools": len(cap.get("tools") or [])}


def capability_ids(registry: dict[str, Any] | None = None) -> list[str]:
    reg = registry if registry is not None else load_registry()
    return [
        str(c.get("id"))
        for c in (reg.get("capabilities") or [])
        if isinstance(c, dict) and c.get("id")
    ]


def list_capabilities(registry: dict[str, Any] | None = None) -> dict[str, Any]:
    reg = registry if registry is not None else load_registry()
    rows: list[dict[str, Any]] = []
    for c in reg.get("capabilities") or []:
        if not isinstance(c, dict):
            continue
        rows.append(
            {
                "id": c.get("id"),
                "label": c.get("label"),
                "domain": c.get("domain"),
                "entrypoint": c.get("entrypoint"),
                "tool_count": len(c.get("tools") or []),
            }
        )
    return {"ok": True, "schema_version": reg.get("schema_version"), "capabilities": rows}


def ensure_layout() -> dict[str, Any]:
    """Create the on-disk capability + data roots (idempotent, non-destructive)."""
    dirs = [
        registry_dir(),
        DEFAULT_OUTPUT_DIR,
        DEFAULT_STAGING_DIR,
        DEFAULT_WORKTREE_DIR,
    ]
    created: list[str] = []
    for d in dirs:
        try:
            d.mkdir(parents=True, exist_ok=True)
            created.append(str(d))
        except OSError as exc:
            return {"ok": False, "error": f"{d}: {exc}"}
    return {"ok": True, "created": created}


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE capability registry")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("ensure-layout", help="Create registry + data roots")
    sub.add_parser("list", help="List registered capabilities")
    sub.add_parser("write-snapshot", help="Recompute and write the schema snapshot")

    pv = sub.add_parser("verify", help="Fail-closed verify one capability")
    pv.add_argument("capability_id")

    args = parser.parse_args(argv)
    if args.cmd == "ensure-layout":
        out = ensure_layout()
    elif args.cmd == "list":
        out = list_capabilities()
    elif args.cmd == "write-snapshot":
        write_snapshot(load_registry())
        out = {"ok": True, "snapshot": str(snapshot_path())}
    elif args.cmd == "verify":
        out = verify_capability(args.capability_id)
    else:
        raise SystemExit(f"unknown cmd {args.cmd}")
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
