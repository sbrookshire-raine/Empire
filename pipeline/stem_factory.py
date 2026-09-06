"""EMPIRE wrapper for Shard of the Division (music stem splitter / practice tracks).

Runs the isolated project CLI — does not rewrite Shard into Eve.
Default inbox/outbox live under C:\\Empire_Workbench\\stem_factory\\
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

AUDIO_SUFFIXES = {".mp3", ".wav", ".flac", ".m4a", ".ogg", ".aac", ".wma"}

DEFAULT_SHARD_DIR = Path(
    os.environ.get(
        "EMPIRE_STEM_FACTORY_DIR",
        r"C:\Users\m69nr\OneDrive\Desktop\HIDDEN\Shard_of_the_Division",
    )
)
DEFAULT_INBOX = Path(
    os.environ.get(
        "EMPIRE_STEM_INBOX",
        r"C:\Empire_Workbench\stem_factory\input",
    )
)
DEFAULT_OUTBOX = Path(
    os.environ.get(
        "EMPIRE_STEM_OUTBOX",
        r"C:\Empire_Workbench\stem_factory\output",
    )
)

ALLOWED_ROOTS = [
    Path(r"C:\Empire_Workbench\stem_factory"),
    DEFAULT_SHARD_DIR / "input",
    DEFAULT_SHARD_DIR / "output",
    Path(r"G:\My Drive\Music"),
    Path(r"G:\My Drive\Music\stem_factory"),
]


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _resolve_python(shard_dir: Path) -> Path:
    """Prefer a working venv. .venv-cuda may be broken if base Python moved."""
    candidates = [
        shard_dir / ".venv-cuda" / "Scripts" / "python.exe",
        shard_dir / ".venv" / "Scripts" / "python.exe",
    ]
    for candidate in candidates:
        if not candidate.is_file():
            continue
        try:
            proc = subprocess.run(
                [str(candidate), "-c", "import demucs"],
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
            if proc.returncode == 0:
                return candidate
        except (OSError, subprocess.TimeoutExpired):
            continue
    raise FileNotFoundError(
        f"No working Shard venv with demucs under {shard_dir} "
        "(.venv-cuda or .venv). Restore the project venv first."
    )


def _cuda_available(python_bin: Path) -> bool:
    try:
        proc = subprocess.run(
            [
                str(python_bin),
                "-c",
                "import torch; print('1' if torch.cuda.is_available() else '0')",
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        return proc.returncode == 0 and (proc.stdout or "").strip().startswith("1")
    except (OSError, subprocess.TimeoutExpired):
        return False


def _under_allowed(path: Path) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        return False
    for root in ALLOWED_ROOTS:
        try:
            resolved.relative_to(root.resolve())
            return True
        except ValueError:
            continue
        except OSError:
            continue
    # Also allow exact DEFAULT_INBOX / OUTBOX even if roots list lags
    for extra in (DEFAULT_INBOX, DEFAULT_OUTBOX):
        try:
            resolved.relative_to(extra.resolve())
            return True
        except (ValueError, OSError):
            continue
    return False


def ensure_dirs(
    inbox: Path | None = None,
    outbox: Path | None = None,
) -> dict[str, str]:
    in_dir = Path(inbox) if inbox else DEFAULT_INBOX
    out_dir = Path(outbox) if outbox else DEFAULT_OUTBOX
    in_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    return {"inbox": str(in_dir), "outbox": str(out_dir)}


def list_inbox(inbox: Path | None = None) -> dict[str, Any]:
    in_dir = Path(inbox) if inbox else DEFAULT_INBOX
    ensure_dirs(inbox=in_dir, outbox=DEFAULT_OUTBOX)
    if not _under_allowed(in_dir):
        return {
            "ok": False,
            "error": f"inbox path not allowed: {in_dir}",
            "files": [],
        }
    files: list[dict[str, Any]] = []
    try:
        for path in sorted(in_dir.iterdir()):
            if path.is_file() and path.suffix.lower() in AUDIO_SUFFIXES:
                try:
                    size = path.stat().st_size
                except OSError:
                    size = 0
                files.append({"name": path.name, "path": str(path), "bytes": size})
    except OSError as exc:
        return {"ok": False, "error": str(exc), "files": []}
    return {
        "ok": True,
        "inbox": str(in_dir),
        "count": len(files),
        "files": files,
        "note": "Drop songs here, then call stem_run (or ask Eve with Stem Factory Toolbelt ON).",
    }


def run_stems(
    *,
    input_dir: str | None = None,
    output_dir: str | None = None,
    device: str = "cuda",
    model: str = "htdemucs_ft",
    limit: int | None = 1,
    overwrite: bool = False,
    skip_separation: bool = False,
    jobs: int = 2,
    timeout_sec: int = 3600,
    shard_dir: Path | None = None,
) -> dict[str, Any]:
    """Run practice_generator.py against input/output folders."""
    shard = Path(shard_dir) if shard_dir else DEFAULT_SHARD_DIR
    in_dir = Path(input_dir) if input_dir else DEFAULT_INBOX
    out_dir = Path(output_dir) if output_dir else DEFAULT_OUTBOX
    ensure_dirs(inbox=in_dir, outbox=out_dir)

    if not shard.is_dir():
        return {
            "ok": False,
            "error": f"Shard of the Division not found at {shard}",
        }
    if not _under_allowed(in_dir) or not _under_allowed(out_dir):
        return {
            "ok": False,
            "error": (
                "input_dir/output_dir must stay under approved roots "
                "(Empire_Workbench\\stem_factory, Shard input/output, or G:\\My Drive\\Music)."
            ),
            "input_dir": str(in_dir),
            "output_dir": str(out_dir),
        }

    script = shard / "scripts" / "practice_generator.py"
    if not script.is_file():
        return {"ok": False, "error": f"Missing CLI script: {script}"}

    listed = list_inbox(in_dir)
    if not listed.get("ok"):
        return listed
    if listed.get("count", 0) == 0:
        return {
            "ok": False,
            "error": f"No audio files in inbox {in_dir}. Drop .mp3/.wav/.flac first.",
            "inbox": str(in_dir),
        }

    try:
        python_bin = _resolve_python(shard)
    except FileNotFoundError as exc:
        return {"ok": False, "error": str(exc)}

    # Auto-fall back to CPU when the working venv has no CUDA.
    resolved_device = device if device in {"cuda", "cpu"} else "cuda"
    if resolved_device == "cuda" and not _cuda_available(python_bin):
        resolved_device = "cpu"

    cmd: list[str] = [
        str(python_bin),
        str(script),
        "--input-dir",
        str(in_dir),
        "--output-dir",
        str(out_dir),
        "--device",
        resolved_device,
        "--model",
        model or "htdemucs_ft",
        "--jobs",
        str(max(1, int(jobs))),
    ]
    if limit is not None and int(limit) > 0:
        cmd.extend(["--limit", str(int(limit))])
    if overwrite:
        cmd.append("--overwrite")
    if skip_separation:
        cmd.append("--skip-separation")

    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(shard),
            capture_output=True,
            text=True,
            timeout=max(60, int(timeout_sec)),
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "error": f"Stem run timed out after {timeout_sec}s",
            "command": cmd,
            "input_dir": str(in_dir),
            "output_dir": str(out_dir),
        }
    except OSError as exc:
        return {"ok": False, "error": str(exc), "command": cmd}

    elapsed = round(time.time() - started, 1)
    stems_dir = out_dir / "output" / "1_stems"
    focus_dir = out_dir / "output" / "3_focus"
    produced: list[str] = []
    for folder in (stems_dir, focus_dir):
        try:
            if folder.is_dir():
                for path in sorted(folder.rglob("*")):
                    if path.is_file() and path.suffix.lower() in AUDIO_SUFFIXES:
                        produced.append(str(path))
        except OSError:
            pass

    ok = proc.returncode == 0
    stdout_tail = (proc.stdout or "")[-4000:]
    stderr_tail = (proc.stderr or "")[-2000:]
    return {
        "ok": ok,
        "returncode": proc.returncode,
        "elapsed_sec": elapsed,
        "command": cmd,
        "python": str(python_bin),
        "shard_dir": str(shard),
        "input_dir": str(in_dir),
        "output_dir": str(out_dir),
        "inbox_count_before": listed.get("count"),
        "produced_count": len(produced),
        "produced_sample": produced[:20],
        "stems_dir": str(stems_dir),
        "focus_dir": str(focus_dir),
        "stdout_tail": stdout_tail,
        "stderr_tail": stderr_tail,
        "fetched_at": _utc_now(),
        "note": (
            "Stems under output/1_stems; practice focus mixes under output/3_focus. "
            "Default limit=1 — raise limit for batch jobs (GPU heavy)."
            if ok
            else "Stem run failed — check stderr_tail and Shard .venv-cuda / CUDA."
        ),
    }


def status() -> dict[str, Any]:
    shard = DEFAULT_SHARD_DIR
    ensure_dirs()
    py_ok = False
    py_path = ""
    cuda_ok = False
    try:
        py_path = str(_resolve_python(shard))
        py_ok = True
        cuda_ok = _cuda_available(Path(py_path))
    except FileNotFoundError:
        pass
    inbox = list_inbox()
    return {
        "ok": shard.is_dir() and py_ok,
        "shard_dir": str(shard),
        "python": py_path,
        "cuda_available": cuda_ok,
        "device_default": "cuda" if cuda_ok else "cpu",
        "inbox": str(DEFAULT_INBOX),
        "outbox": str(DEFAULT_OUTBOX),
        "inbox_files": inbox.get("files") if inbox.get("ok") else [],
        "inbox_count": inbox.get("count", 0),
        "cli": "scripts/practice_generator.py --input-dir … --output-dir …",
        "project": "Shard of the Division (aka Stem Factory)",
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="EMPIRE Stem Factory / Shard wrapper")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sub.add_parser("list-inbox")
    run_p = sub.add_parser("run")
    run_p.add_argument("--input-dir", default=str(DEFAULT_INBOX))
    run_p.add_argument("--output-dir", default=str(DEFAULT_OUTBOX))
    run_p.add_argument("--device", default="cuda")
    run_p.add_argument("--limit", type=int, default=1)
    run_p.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    if args.cmd == "status":
        print(json.dumps(status(), indent=2))
        return 0 if status().get("ok") else 1
    if args.cmd == "list-inbox":
        print(json.dumps(list_inbox(), indent=2))
        return 0
    if args.cmd == "run":
        result = run_stems(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            device=args.device,
            limit=args.limit,
            overwrite=args.overwrite,
        )
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
