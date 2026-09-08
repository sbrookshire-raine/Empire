"""Typed artifact lineage envelopes for EMPIRE workers (scratch, not Cognee)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from pipeline.provenance import utc_now_iso


def sha256_text(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str | None:
    try:
        h = hashlib.sha256()
        with path.open("rb") as stream:
            while True:
                chunk = stream.read(1024 * 1024)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def lineage_envelope(
    *,
    schema_id: str,
    tool: str,
    limb: str,
    model_id: str,
    model_hash: str | None = None,
    input_hash: str,
    validation_ok: bool,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "schema_id": schema_id,
        "tool": tool,
        "limb": limb,
        "model_id": model_id,
        "model_hash": model_hash or "",
        "input_hash": input_hash,
        "validation_ok": bool(validation_ok),
        "created_at": utc_now_iso(),
        "memory_status": "scratch",
        "promote": "explicit_only",
    }
    if extra:
        for key, value in extra.items():
            if value is None:
                continue
            payload[key] = value
    return payload


def lineage_markdown_block(envelope: dict[str, Any]) -> str:
    body = json.dumps(envelope, indent=2, default=str)
    return f"\n\n## Lineage\n\n```json\n{body}\n```\n"
