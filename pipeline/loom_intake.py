"""EMPIRE wrapper for The Keeper Loom — Knowledge Shell intake + ledger status.

Runs scripts from Empire_Workbench/04_Thought_Experiments/loom (copied from
TOOL_FACTORY_GUMLOOP). Never auto-promotes ledger rows to Cognee.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import sys
from pathlib import Path
from typing import Any

DEFAULT_LOOM_ROOT = Path(
    os.environ.get(
        "EMPIRE_LOOM_ROOT",
        r"C:\Empire_Workbench\04_Thought_Experiments\loom",
    )
)
RESOURCE_QUEUE = Path(
    os.environ.get(
        "EMPIRE_RESOURCE_QUEUE_DIR",
        r"C:\Empire_Workbench\00_Resource_Queue",
    )
)


def loom_root() -> Path:
    return DEFAULT_LOOM_ROOT


def _wire_loom_imports(root: Path) -> None:
    for segment in (
        root,
        root / "skills" / "primitive-decoder" / "scripts",
        root / "scripts",
        root / "intake",
    ):
        text = str(segment)
        if text not in sys.path:
            sys.path.insert(0, text)


def _load_process_shell_packets(root: Path):
    _wire_loom_imports(root)
    module_path = root / "intake" / "process_shell_packets.py"
    if not module_path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("loom_process_shell_packets", module_path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_csv_path(csv_input: str) -> Path:
    raw = (csv_input or "").strip().strip('"')
    if not raw:
        raise ValueError("csv_path required")
    candidate = Path(raw)
    if candidate.is_file():
        return candidate.resolve()
    from_queue = RESOURCE_QUEUE / raw
    if from_queue.is_file():
        return from_queue.resolve()
    from_intake = loom_root() / "intake" / raw
    if from_intake.is_file():
        return from_intake.resolve()
    raise FileNotFoundError(f"Shell packet CSV not found: {raw}")


def process_shell_csv(
    csv_path: str,
    *,
    domain_bucket: str = "general",
    decoded_by: str = "Keeper",
    max_per_cycle: int = 7,
) -> dict[str, Any]:
    """Run Knowledge Shell intake on a 12-column Shell Packet CSV."""
    root = loom_root()
    if not root.is_dir():
        return {
            "ok": False,
            "error": f"Loom root missing: {root}",
            "hint": "Copy loom/ from TOOL_FACTORY_GUMLOOP into 04_Thought_Experiments/loom",
        }
    try:
        resolved = resolve_csv_path(csv_path)
    except (ValueError, FileNotFoundError) as exc:
        return {"ok": False, "error": str(exc)}

    module = _load_process_shell_packets(root)
    if module is None:
        return {"ok": False, "error": "process_shell_packets.py not found under loom/intake"}

    outdir = root / "workspace_data"
    try:
        report = module.process_shell_packets(
            csv_input=str(resolved),
            domain_bucket=domain_bucket,
            decoded_by=decoded_by,
            max_per_cycle=max_per_cycle,
            outdir=str(outdir),
        )
    except Exception as exc:
        return {"ok": False, "error": f"loom intake failed: {exc}", "csv_path": str(resolved)}

    fatal = report.get("fatal_error")
    return {
        "ok": fatal is None,
        "fatal_error": fatal,
        "csv_path": str(resolved),
        "domain_bucket": domain_bucket,
        "report": report,
        "ledger_path": str(outdir / "primitive_ledger.csv"),
        "gap_report_path": str(outdir / "gap_report.csv"),
    }


def loom_status() -> dict[str, Any]:
    """Return Loom workspace paths and ledger/buffer counts."""
    root = loom_root()
    data = root / "workspace_data"
    ledger = data / "primitive_ledger.csv"
    buffer = data / "knowledge_shell_buffer.csv"
    rejects = data / "knowledge_shell_rejects.csv"
    gap = data / "gap_report.csv"

    status: dict[str, Any] = {
        "ok": root.is_dir(),
        "loom_root": str(root),
        "seeker_prompt": str(root / "intake" / "seeker_extraction_prompt_v5.md"),
        "sample_csv": str(root / "intake" / "sample_shell_packets.csv"),
        "ledger_path": str(ledger),
        "ledger_rows": 0,
        "buffer_path": str(buffer),
        "buffer_rows": 0,
        "rejects_path": str(rejects),
        "rejects_rows": 0,
        "gap_report_path": str(gap),
        "gap_report_exists": gap.is_file(),
    }
    if not root.is_dir():
        status["error"] = "Loom root directory missing"
        return status

    for key, path in (
        ("ledger_rows", ledger),
        ("buffer_rows", buffer),
        ("rejects_rows", rejects),
    ):
        if path.is_file():
            with path.open(newline="", encoding="utf-8") as stream:
                status[key] = max(0, sum(1 for _ in csv.DictReader(stream)))
    return status


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE Loom Knowledge Shell intake")
    sub = parser.add_subparsers(dest="cmd")

    status_cmd = sub.add_parser("status", help="Show loom workspace status")
    status_cmd.set_defaults(cmd="status")

    run_cmd = sub.add_parser("process", help="Process Shell Packet CSV")
    run_cmd.add_argument("csv_path")
    run_cmd.add_argument("--domain-bucket", default="general")
    run_cmd.add_argument("--max-per-cycle", type=int, default=7)
    run_cmd.set_defaults(cmd="process")

    args = parser.parse_args(argv)
    if args.cmd == "status":
        result = loom_status()
    elif args.cmd == "process":
        result = process_shell_csv(
            args.csv_path,
            domain_bucket=args.domain_bucket,
            max_per_cycle=args.max_per_cycle,
        )
    else:
        parser.print_help()
        return 1

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
