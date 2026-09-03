#!/usr/bin/env python3
"""Build a small high-signal eve_core dataset from the workbench bulk harvest.

Bulk eve_memory (12k+ files) is an archive. Chat recall should target eve_core:
scored project docs + a generated profile summary. Optional memify pass on the
small dataset only.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path

EMPIRE_ROOT = Path(__file__).resolve().parent.parent
WORKBENCH_ROOT = Path(r"C:\Empire_Workbench")
DEFAULT_SCAN_FOLDERS = (
    WORKBENCH_ROOT / "01_Memory_Bank",
    WORKBENCH_ROOT / "02_Skills_and_Prompts",
)
CORE_OUTPUT = WORKBENCH_ROOT / "00_Core_Profile"
PROFILE_FILE = CORE_OUTPUT / "USER_CORE_PROFILE.md"
MANIFEST_FILE = CORE_OUTPUT / "eve_core_manifest.json"
DATASET = "eve_core"
ALLOWED_SUFFIXES = {".md", ".txt"}
MAX_FILE_BYTES = 120_000
PROFILE_EXCERPT_CHARS = 1_800
INGEST_TIMEOUT_SECONDS = 600


def worker_env() -> dict[str, str]:
    env = dict(**{key: value for key, value in __import__("os").environ.items()})
    env["PYTHONPATH"] = str(EMPIRE_ROOT)
    env["PYTHONUNBUFFERED"] = "1"
    env["CACHING"] = "false"
    env["COGNEE_SKIP_CONNECTION_TEST"] = "true"
    return env

POSITIVE_PATH_RE = re.compile(
    r"(empire|forge|rain|reign|daze|workbench|P_Raine|project)",
    re.IGNORECASE,
)
POSITIVE_BODY_RE = re.compile(
    r"\b(empire|forge|rain|reign|daze|cognee|eve|pocketbase|ollama|workbench|jarvis)\b",
    re.IGNORECASE,
)
NEGATIVE_PATH_RE = re.compile(
    r"(self[-_ ]?help|learning[-_ ]techniques|youtube|transcript|webinar|course)",
    re.IGNORECASE,
)
NEGATIVE_BODY_RE = re.compile(
    r"(youtube\.com|youtu\.be|\(00:\d{2}:\d{2}\)|Nobel Prize|Set Measurable Goals|"
    r"heat-seeking missile|Heptabase Gallery)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ScoredFile:
    path: Path
    score: int


def score_file(path: Path) -> int | None:
    rel = str(path)
    name = path.name
    try:
        size = path.stat().st_size
        if size == 0 or size > MAX_FILE_BYTES:
            return None
        body = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None
    stripped = body.strip()
    if len(stripped) < 160:
        return None

    score = 0
    if NEGATIVE_PATH_RE.search(rel):
        score -= 60
    if NEGATIVE_BODY_RE.search(body):
        score -= 50
    if POSITIVE_PATH_RE.search(rel) or POSITIVE_PATH_RE.search(name):
        score += 35
    if re.search(r"rain.*empire|empire.*pt\d", name, re.IGNORECASE):
        score += 45
    if name.casefold().startswith("nlm"):
        score += 55
    if "forge" in name.casefold():
        score += 25
    score += min(len(POSITIVE_BODY_RE.findall(body)) * 2, 24)
    if body.count("http") > 18:
        score -= 20
    if score < 8:
        return None
    return score


def collect_scored_files(folders: list[Path]) -> list[ScoredFile]:
    ranked: list[ScoredFile] = []
    for folder in folders:
        if not folder.is_dir():
            print(f"SKIP missing folder: {folder}", file=sys.stderr)
            continue
        for path in sorted(folder.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in ALLOWED_SUFFIXES:
                continue
            points = score_file(path)
            if points is None:
                continue
            ranked.append(ScoredFile(path=path, score=points))
    ranked.sort(key=lambda item: (-item.score, str(item.path).casefold()))
    return ranked


def write_profile(selected: list[ScoredFile]) -> Path:
    CORE_OUTPUT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# USER CORE PROFILE (auto-generated)",
        "",
        "High-signal project and interest notes selected from Empire Workbench.",
        "Use for Eve chat recall — not a manual edit target unless you want overrides.",
        "",
    ]
    for index, item in enumerate(selected, start=1):
        rel = item.path.relative_to(WORKBENCH_ROOT)
        try:
            body = item.path.read_text(encoding="utf-8").strip()
        except (OSError, UnicodeError):
            continue
        excerpt = body[:PROFILE_EXCERPT_CHARS]
        if len(body) > PROFILE_EXCERPT_CHARS:
            excerpt += "\n\n…"
        lines.extend(
            [
                f"## {index}. {rel} (score {item.score})",
                "",
                excerpt,
                "",
            ]
        )
    PROFILE_FILE.write_text("\n".join(lines), encoding="utf-8")
    return PROFILE_FILE


def write_manifest(selected: list[ScoredFile], profile_path: Path) -> None:
    payload = {
        "dataset": DATASET,
        "profile": str(profile_path),
        "file_count": len(selected),
        "files": [
            {"path": str(item.path), "score": item.score}
            for item in selected
        ],
    }
    MANIFEST_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def run_worker(command: list[str]) -> dict[str, object]:
    result = subprocess.run(
        command,
        cwd=EMPIRE_ROOT,
        env=worker_env(),
        capture_output=True,
        text=True,
        timeout=INGEST_TIMEOUT_SECONDS,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "worker failed")
    for line in reversed(result.stdout.splitlines()):
        line = line.strip()
        if line.startswith("{"):
            return json.loads(line)
    return {"status": "ok"}


def forget_dataset(dataset: str) -> None:
    run_worker(
        [
            sys.executable,
            "-m",
            "pipeline.cognee_worker",
            "forget",
            "--dataset",
            dataset,
        ]
    )


def ingest_paths(paths: list[Path], dataset: str) -> dict[str, object]:
    job_id = f"eve-core-{uuid.uuid4().hex[:12]}"
    command = [
        sys.executable,
        "-m",
        "pipeline.cognee_worker",
        "ingest-files",
        "--dataset",
        dataset,
        "--job-id",
        job_id,
    ]
    for path in paths:
        command.extend(("--path", str(path)))
    return run_worker(command)


def memify_dataset(dataset: str) -> None:
    run_worker(
        [
            sys.executable,
            "-m",
            "pipeline.cognee_worker",
            "improve",
            "--dataset",
            dataset,
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Curate a small eve_core dataset for fast, useful Eve recall."
    )
    parser.add_argument("--max-files", type=int, default=60, help="Top scored files to keep")
    parser.add_argument(
        "--folders",
        nargs="*",
        default=[str(path) for path in DEFAULT_SCAN_FOLDERS],
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Score and write manifest/profile only; do not touch Cognee",
    )
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="Forget eve_core before ingesting (recommended first run)",
    )
    parser.add_argument(
        "--memify",
        action="store_true",
        help="Run Cognee memify/improve on eve_core after ingest (slow, optional)",
    )
    args = parser.parse_args()

    folders = [Path(folder) for folder in args.folders]
    ranked = collect_scored_files(folders)
    if not ranked:
        print("No high-signal files found. Adjust folders or scoring.", file=sys.stderr)
        return 1

    selected = ranked[: max(args.max_files, 1)]
    profile_path = write_profile(selected[: min(len(selected), 25)])
    write_manifest(selected, profile_path)

    print(f"Selected {len(selected)} files (top score {selected[0].score}).")
    print(f"Profile: {profile_path}")
    print(f"Manifest: {MANIFEST_FILE}")
    for item in selected[:10]:
        print(f"  {item.score:>3}  {item.path.name}")
    if len(selected) > 10:
        print(f"  ... and {len(selected) - 10} more")

    if args.dry_run:
        print("Dry run — no Cognee changes.")
        return 0

    ingest_paths_list = [profile_path, *[item.path for item in selected]]
    if args.fresh:
        print(f"Forgetting dataset {DATASET} ...")
        try:
            forget_dataset(DATASET)
        except RuntimeError as exc:
            print(f"Forget skipped or failed ({exc}); continuing.", file=sys.stderr)

    batch_size = 20
    ingested = 0
    for start in range(0, len(ingest_paths_list), batch_size):
        batch = ingest_paths_list[start : start + batch_size]
        result = ingest_paths(batch, DATASET)
        ingested += int(result.get("documents", 0))
        print(f"Ingested batch {start // batch_size + 1}: {result.get('documents', 0)} new docs")

    if args.memify:
        print(f"Running memify on {DATASET} (this can take a while) ...")
        memify_dataset(DATASET)
        print("Memify complete.")

    print(f"Done. eve_core ready ({ingested} new documents embedded).")
    print("Chat recall now prefers eve_core over eve_memory.")
    try:
        from frontend.project_catalog import save_project_catalog

        catalog = save_project_catalog()
        print(f"Project catalog refreshed ({catalog.get('project_count', 0)} projects).")
    except Exception as exc:
        print(f"Project catalog refresh skipped: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
