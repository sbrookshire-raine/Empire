"""Normalize local mock JSON/MD files into Cognee-ready documents."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text

    meta: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, parts[2].strip()


def normalize_file(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        source_type = payload.get("source_type", "mock")
        external_id = payload.get("external_id", path.stem)
        document = _normalize_json(payload)
    elif suffix == ".md":
        meta, body = _parse_frontmatter(path.read_text(encoding="utf-8"))
        source_type = meta.get("source_type", "mock")
        external_id = meta.get("external_id", path.stem)
        document = _normalize_markdown(meta, body)
    else:
        raise ValueError(f"Unsupported file type: {path}")

    return {
        "source_type": source_type,
        "external_id": external_id,
        "source_file": str(path),
        "document": document,
        "dataset": source_type,
    }


def _normalize_json(payload: dict[str, Any]) -> str:
    lines = [
        f"SourceType: {payload.get('source_type', 'mock')}",
        f"ExternalId: {payload.get('external_id', 'unknown')}",
    ]

    if "channel" in payload:
        lines.append(f"Channel: {payload['channel']}")
        lines.append(f"Thread: {payload.get('thread_id', 'unknown')}")
        for message in payload.get("messages", []):
            lines.append(f"Person: {message.get('author', 'unknown')}")
            lines.append(f"Timestamp: {message.get('timestamp', '')}")
            lines.append(message.get("text", ""))

    if "repo" in payload:
        lines.append(f"Repo: {payload['repo']}")
        issue = payload.get("issue", {})
        lines.append(f"Issue: {issue.get('number', 'unknown')} - {issue.get('title', '')}")
        lines.append(f"Person: {issue.get('author', 'unknown')}")
        lines.append(f"State: {issue.get('state', '')}")
        for label in issue.get("labels", []):
            lines.append(f"Label: {label}")
        lines.append(issue.get("body", ""))
        for comment in payload.get("comments", []):
            lines.append(f"Person: {comment.get('author', 'unknown')}")
            lines.append(comment.get("body", ""))

    return "\n".join(line for line in lines if line)


def _normalize_markdown(meta: dict[str, str], body: str) -> str:
    lines = [
        f"SourceType: {meta.get('source_type', 'mock')}",
        f"ExternalId: {meta.get('external_id', 'unknown')}",
        f"From: {meta.get('from', '')}",
        f"To: {meta.get('to', '')}",
        f"Subject: {meta.get('subject', '')}",
        f"Date: {meta.get('date', '')}",
        body,
    ]
    return "\n".join(line for line in lines if line)
