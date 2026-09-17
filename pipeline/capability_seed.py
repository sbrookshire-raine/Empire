"""Seed the capability registry with Eve's canonical governed arms.

This is the activation step for the fail-closed governance foundation
(`capability_registry.py`). The registry + tool-schema snapshot are written to
`config/eve-capabilities/` so that `verify_capability()` has an approved
baseline to compare against. Run via `scripts/seed-capabilities.ps1` (idempotent:
re-running recomputes the same hashes and rewrites the snapshot).

The canonical arm list mirrors `config/lego-bricks.json` and
`config/capability-manifest.json`. If a tool's schema/description changes, the
snapshot hash drifts and `mechanic-green` reports it fail-closed until the seed
is re-run deliberately (never silently in CI).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pipeline import capability_registry as cr

# Trust domains: local_evidence / artifact / public_web / code / memory / ops.
# The `ops` domain carries the switchboard (governed service control).


def _tool(name: str, description: str, schema: dict[str, Any]) -> dict[str, Any]:
    return {"name": name, "description": description, "input_schema": schema}


def _obj(props: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": props,
        "required": required or [],
        "additionalProperties": False,
    }


def _str(description: str) -> dict[str, Any]:
    return {"type": "string", "description": description}


def _int(description: str) -> dict[str, Any]:
    return {"type": "integer", "description": description}


def _bool(description: str) -> dict[str, Any]:
    return {"type": "boolean", "description": description}


def canonical_capabilities() -> list[dict[str, Any]]:
    """Return the authoritative list of capabilities + tool schemas to seed."""
    return [
        {
            "capability_id": "workspace_search",
            "label": "Workspace Search",
            "domain": "local_evidence",
            "entrypoint": "pipeline.workspace_search",
            "note": "Read-only ripgrep/builtin text search over allowlisted roots.",
            "tools": [
                _tool(
                    "workspace_search",
                    "Search allowlisted local roots for text (offline, no network).",
                    _obj(
                        {
                            "query": _str("Search query."),
                            "max_results": _int("Max results (default 100)."),
                            "note": _str("Optional Architect note."),
                        },
                        required=["query"],
                    ),
                ),
            ],
        },
        {
            "capability_id": "query_data",
            "label": "Query Data",
            "domain": "local_evidence",
            "entrypoint": "pipeline.query_data",
            "note": "Read-only DuckDB query over local CSV/JSON/Parquet/SQLite.",
            "tools": [
                _tool(
                    "query_data",
                    "Run a read-only DuckDB query over a local data file.",
                    _obj(
                        {
                            "sql": _str("Read-only SELECT SQL."),
                            "data_file": _str("Allowlisted data file path."),
                            "max_rows": _int("Max rows returned (default 1000)."),
                        },
                        required=["sql"],
                    ),
                ),
            ],
        },
        {
            "capability_id": "read_document",
            "label": "Read Document",
            "domain": "local_evidence",
            "entrypoint": "pipeline.read_document",
            "note": "MarkItDown -> Docling fallback extraction from local files.",
            "tools": [
                _tool(
                    "read_document",
                    "Extract text/markdown from a local document.",
                    _obj(
                        {
                            "input_path": _str("Allowlisted document path."),
                            "max_chars": _int("Max characters returned (default 200000)."),
                        },
                        required=["input_path"],
                    ),
                ),
            ],
        },
        {
            "capability_id": "create_spreadsheet",
            "label": "Spreadsheet",
            "domain": "artifact",
            "entrypoint": "pipeline.create_spreadsheet",
            "note": "openpyxl .xlsx into eve-output; formula-injection blocked.",
            "tools": [
                _tool(
                    "create_spreadsheet",
                    "Write an .xlsx into eve-output (formula injection blocked).",
                    _obj(
                        {
                            "filename": _str("Output .xlsx filename."),
                            "headers": {"type": "array", "items": {"type": "string"}},
                            "rows": {
                                "type": "array",
                                "items": {"type": "array", "items": {}},
                            },
                            "sheet_name": _str("Sheet name (default Sheet1)."),
                            "note": _str("Optional Architect note."),
                        },
                        required=["filename", "headers", "rows"],
                    ),
                ),
            ],
        },
        {
            "capability_id": "author_code",
            "label": "Code Author",
            "domain": "code",
            "entrypoint": "pipeline.author_code",
            "note": "Disposable Git worktree authoring; reviewable diffs, never merges.",
            "tools": [
                _tool(
                    "author_code_create_worktree",
                    "Create a disposable Git worktree for code authoring.",
                    _obj({"note": _str("Optional Architect note.")}),
                ),
                _tool(
                    "author_code_apply_patch",
                    "Write a file in a disposable worktree and return its diff.",
                    _obj(
                        {
                            "worktree": _str("Worktree id."),
                            "relative_path": _str("Repo-relative file path."),
                            "content": _str("Full file content."),
                        },
                        required=["worktree", "relative_path", "content"],
                    ),
                ),
                _tool(
                    "author_code_remove_worktree",
                    "Remove a disposable worktree.",
                    _obj({"worktree": _str("Worktree id.")}, required=["worktree"]),
                ),
            ],
        },
        {
            "capability_id": "python_verify",
            "label": "Python Verify",
            "domain": "code",
            "entrypoint": "pipeline.python_verify",
            "note": "Syntax + optional lint/test in a disposable worktree.",
            "tools": [
                _tool(
                    "python_verify",
                    "Syntax-check + (optional) lint/test a disposable worktree.",
                    _obj(
                        {
                            "worktree": _str("Worktree id."),
                            "run_tests": _bool("Run tests (default true)."),
                        },
                        required=["worktree"],
                    ),
                ),
            ],
        },
        {
            "capability_id": "switchboard",
            "label": "Switchboard",
            "domain": "ops",
            "entrypoint": "pipeline.switchboard",
            "note": "Governed service control + GPU tenant serialization (dry-run first).",
            "tools": [
                _tool(
                    "switchboard_status",
                    "Snapshot of services, headroom, and GPU lease (read-only).",
                    _obj({}),
                ),
                _tool(
                    "switchboard_plan",
                    "Dry-run plan for which services a task needs (no mutation).",
                    _obj(
                        {"services": {"type": "array", "items": {"type": "string"}}},
                        required=["services"],
                    ),
                ),
                _tool(
                    "switchboard_ensure",
                    "Start services a task needs (headroom-gated; dry_run default true).",
                    _obj(
                        {
                            "services": {"type": "array", "items": {"type": "string"}},
                            "dry_run": _bool("Plan only (default true)."),
                        },
                        required=["services"],
                    ),
                ),
                _tool(
                    "switchboard_release",
                    "Stop managed services a task no longer needs (dry_run default true).",
                    _obj(
                        {
                            "services": {"type": "array", "items": {"type": "string"}},
                            "dry_run": _bool("Plan only (default true)."),
                        },
                        required=["services"],
                    ),
                ),
                _tool(
                    "switchboard_tenant",
                    "GPU tenant lease: acquire/release/status (dry_run default true).",
                    _obj(
                        {
                            "action": _str("acquire | release | status."),
                            "tenant": _str("Tenant name (for acquire)."),
                            "dry_run": _bool("Plan only (default true)."),
                        },
                        required=["action"],
                    ),
                ),
            ],
        },
    ]


def seed(registry_dir: str | None = None) -> dict[str, Any]:
    """Register every canonical arm and write registry + snapshot. Idempotent.

    When `registry_dir` is given (tests), writes into that directory with no
    global-state side effects. Otherwise writes to the canonical registry dir
    and ensures the production data roots exist.
    """
    reg = cr.empty_registry()
    for cap in canonical_capabilities():
        cr.register_capability(
            reg,
            capability_id=cap["capability_id"],
            label=cap["label"],
            domain=cap["domain"],
            entrypoint=cap["entrypoint"],
            note=cap["note"],
            tools=cap["tools"],
        )

    if registry_dir:
        base = Path(registry_dir)
        base.mkdir(parents=True, exist_ok=True)
        reg_path = base / cr.REGISTRY_FILENAME
        snap_path = base / cr.SNAPSHOT_FILENAME
    else:
        reg_path = cr.registry_path()
        snap_path = cr.snapshot_path()
        cr.ensure_layout()

    cr.save_registry(reg, path=reg_path)
    cr.write_snapshot(reg, path=snap_path)

    return {
        "ok": True,
        "registry": str(reg_path),
        "snapshot": str(snap_path),
        "capabilities": cr.capability_ids(reg),
        "tool_count": sum(
            len(cap.get("tools") or []) for cap in reg.get("capabilities") or []
        ),
    }


def main(argv: list[str] | None = None) -> int:
    import argparse
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Seed EMPIRE capability registry")
    parser.add_argument("--dir", default="", help="Override registry dir (tests only).")
    args = parser.parse_args(argv)
    out = seed(args.dir or None)
    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
