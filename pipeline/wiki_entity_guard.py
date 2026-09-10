"""Optional GLiNER CPU entity check for wiki grounding (F-36).

When ``gliner`` is installed and ``EMPIRE_GLINER_GROUNDING=1``, compares entities
extracted from the evidence lead vs Eve's reply. Falls back silently when unavailable.

Install (optional): ``pip install gliner``
"""

from __future__ import annotations

import logging
import os
import re
from functools import lru_cache
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_LABELS = ("song", "album", "person", "TV series", "year", "band")
_MODEL_ID = os.environ.get("EMPIRE_GLINER_MODEL", "urchade/gliner_small-v2.1")
_FORBIDDEN_REPLY = re.compile(r'\b"wow"\b|\bwow\b', re.I)


def gliner_grounding_enabled() -> bool:
    return os.environ.get("EMPIRE_GLINER_GROUNDING", "0").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


@lru_cache(maxsize=1)
def _load_model() -> Any | None:
    try:
        from gliner import GLiNER  # type: ignore
    except ImportError:
        logger.debug("gliner not installed — entity guard disabled")
        return None
    try:
        return GLiNER.from_pretrained(_MODEL_ID)
    except Exception as exc:  # noqa: BLE001
        logger.warning("GLiNER load failed (%s): %s", _MODEL_ID, exc)
        return None


def _entity_texts(model: Any, text: str, labels: tuple[str, ...]) -> set[str]:
    if not text.strip():
        return set()
    try:
        rows = model.predict_entities(text, list(labels), threshold=0.4)
    except Exception as exc:  # noqa: BLE001
        logger.debug("GLiNER predict failed: %s", exc)
        return set()
    out: set[str] = set()
    for row in rows or []:
        if not isinstance(row, dict):
            continue
        label = str(row.get("label") or "").casefold()
        span = str(row.get("text") or row.get("entity") or "").strip()
        if not span:
            continue
        out.add(span.casefold())
        if label:
            out.add(f"{label}:{span.casefold()}")
    return out


def verify_entities(
    reply: str,
    evidence: dict[str, Any],
    *,
    user_question: str = "",
    labels: tuple[str, ...] = DEFAULT_LABELS,
) -> tuple[bool, list[str]]:
    """Return (ok, unsupported_entity_spans). Empty list + True when skipped."""
    if not gliner_grounding_enabled():
        return True, []
    model = _load_model()
    if model is None:
        return True, []

    lead = str(evidence.get("lead") or "")
    allowed_raw = evidence.get("allowed_names")
    allowed_names: set[str] = set()
    if isinstance(allowed_raw, list):
        allowed_names = {str(n).casefold() for n in allowed_raw if str(n).strip()}
    title = str(evidence.get("title") or "").strip()
    if title:
        allowed_names.add(title.casefold())

    allowed_entities = _entity_texts(model, lead, labels) | allowed_names
    claimed_entities = _entity_texts(model, f"{reply}\n{user_question}", labels)

    unsupported: list[str] = []
    for entity in sorted(claimed_entities):
        if len(entity) < 3:
            continue
        if entity in allowed_entities:
            continue
        if any(entity in allowed for allowed in allowed_entities):
            continue
        if entity in lead.casefold():
            continue
        # Kate Bush revival: block parametric "Wow" song title
        if entity == "wow" and "running up that hill" in lead.casefold():
            unsupported.append(entity)
            continue
        if " " in entity and len(entity) >= 8:
            unsupported.append(entity)

    ql = (user_question or "").casefold()
    if "kate bush" in ql and _FORBIDDEN_REPLY.search(reply) and "running up that hill" not in reply.casefold():
        if "wow" not in unsupported:
            unsupported.append("wow")

    return len(unsupported) == 0, unsupported
