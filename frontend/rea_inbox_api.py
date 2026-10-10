"""HTTP helpers for REA chat uploads and Eve message enrichment."""

from __future__ import annotations

from email import policy
from email.parser import BytesParser
from typing import Any

from pipeline import rea_inbox


def parse_multipart(body: bytes, content_type: str) -> tuple[list, dict[str, str]]:
    if not content_type.casefold().startswith("multipart/form-data"):
        raise ValueError("REA uploads require multipart/form-data.")
    if "\r" in content_type or "\n" in content_type:
        raise ValueError("Invalid Content-Type.")
    synthetic = (
        f"Content-Type: {content_type}\r\n"
        "MIME-Version: 1.0\r\n"
        "\r\n"
    ).encode("ascii", errors="strict")
    message = BytesParser(policy=policy.default).parsebytes(synthetic + body)
    if not message.is_multipart():
        raise ValueError("Malformed multipart upload.")
    parts: list = []
    fields: dict[str, str] = {}
    for part in message.iter_parts():
        if part.get_content_disposition() != "form-data":
            continue
        filename = part.get_filename()
        field_name = part.get_param("name", header="content-disposition")
        if filename is not None:
            parts.append(part)
        elif field_name:
            content = part.get_payload(decode=True) or b""
            fields[str(field_name)] = content.decode(
                part.get_content_charset() or "utf-8",
                errors="strict",
            )
    return parts, fields


def save_upload(body: bytes, content_type: str) -> dict[str, Any]:
    if len(body) > rea_inbox.MAX_REQUEST_BYTES:
        raise ValueError("Upload exceeds REA inbox size limit.")
    parts, fields = parse_multipart(body, content_type)
    label = str(fields.get("label") or "").strip()
    bundle = rea_inbox.save_multipart_upload(parts, label=label)
    return {"ok": True, "upload": rea_inbox.public_bundle(bundle)}


def enrich_eve_message_payload(payload: dict[str, Any]) -> dict[str, Any]:
    raw_ids = payload.get("rea_uploads")
    if not isinstance(raw_ids, list) or not raw_ids:
        return payload
    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        enriched = dict(payload)
        enriched.pop("rea_uploads", None)
        return enriched
    if rea_inbox.REA_UPLOAD_MARKER in message:
        enriched = dict(payload)
        enriched.pop("rea_uploads", None)
        return enriched

    upload_ids = [str(item).strip() for item in raw_ids if str(item).strip()]
    block = rea_inbox.context_block_for_upload_ids(upload_ids)
    if not block:
        enriched = dict(payload)
        enriched.pop("rea_uploads", None)
        return enriched

    enriched = dict(payload)
    enriched.pop("rea_uploads", None)
    text = message.strip()
    if "\n\nUser message:\n" in text:
        user_part = text.rsplit("\n\nUser message:\n", 1)[-1].strip()
        prefix = text[: text.rfind("\n\nUser message:\n")]
        enriched["message"] = prefix + block + f"\n\nUser message:\n{user_part}"
    else:
        enriched["message"] = block + f"\n\nUser message:\n{text}"
    return enriched
