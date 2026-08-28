"""Run Cognee operations in short-lived subprocesses to release Kuzu locks."""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _python_executable() -> str:
    venv_python = ROOT / "venv" / "Scripts" / "python.exe"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def _worker_env() -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT)
    return env


async def run_cognee_worker(*args: str) -> dict:
    cmd = [_python_executable(), "-m", "pipeline.cognee_worker", *args]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_worker_env(),
        cwd=str(ROOT),
    )
    stdout, stderr = await proc.communicate()

    if proc.returncode != 0:
        message = stderr.decode("utf-8", errors="replace").strip() or stdout.decode(
            "utf-8", errors="replace"
        ).strip()
        if "Could not set lock" in message:
            raise RuntimeError(
                "Cognee database lock conflict. Another ingest or MCP tool should release shortly; retry."
            ) from None
        raise RuntimeError(message or "Cognee worker failed")

    text = stdout.decode("utf-8", errors="replace").strip()
    return json.loads(text) if text else {}


async def run_ingest_file(file_path: Path) -> dict:
    cmd = [
        _python_executable(),
        "-m",
        "pipeline.ingest_local",
        "--file",
        str(file_path),
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_worker_env(),
        cwd=str(ROOT),
    )
    stdout, stderr = await proc.communicate()

    if proc.returncode != 0:
        message = stderr.decode("utf-8", errors="replace").strip()
        if "Could not set lock" in message:
            raise RuntimeError(
                "Cognee database lock conflict. Another ingest or MCP tool should release shortly; retry."
            ) from None
        raise RuntimeError(message or "Ingest subprocess failed")

    output = stdout.decode("utf-8", errors="replace").strip()
    return {"output": output, "status": "success"}


def _extract_sentinel_json(text: str, sentinel: str) -> dict | None:
    for line in reversed(text.splitlines()):
        if line.startswith(sentinel):
            try:
                return json.loads(line[len(sentinel):])
            except json.JSONDecodeError:
                return None
    return None


async def run_wiki_ingest(*args: str) -> dict:
    """Run pipeline.wiki_ingest in an isolated subprocess and parse its result sentinel."""
    cmd = [_python_executable(), "-m", "pipeline.wiki_ingest", *args]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_worker_env(),
        cwd=str(ROOT),
    )
    stdout, stderr = await proc.communicate()
    out_text = stdout.decode("utf-8", errors="replace")
    err_text = stderr.decode("utf-8", errors="replace").strip()

    if proc.returncode != 0:
        message = err_text or out_text.strip()
        if "Could not set lock" in message or "database lock" in message:
            raise RuntimeError(
                "Cognee database lock conflict. Another ingest or MCP tool should release shortly; retry."
            ) from None
        raise RuntimeError(message or "Wiki ingest subprocess failed")

    result = _extract_sentinel_json(out_text, "__WIKI_RESULT__")
    if result is None:
        raise RuntimeError(out_text.strip() or "Wiki ingest produced no result")
    return result


async def run_weaviate_export(*args: str) -> dict:
    """Run pipeline.weaviate_export in a subprocess and parse its result sentinel."""
    cmd = [_python_executable(), "-m", "pipeline.weaviate_export", *args]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_worker_env(),
        cwd=str(ROOT),
    )
    stdout, stderr = await proc.communicate()
    out_text = stdout.decode("utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(stderr.decode("utf-8", errors="replace").strip() or "Weaviate export failed")
    result = _extract_sentinel_json(out_text, "__WEAVIATE_EXPORT__")
    if result is None:
        raise RuntimeError(out_text.strip() or "Weaviate export produced no result")
    return result
