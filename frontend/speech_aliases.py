"""Normalize common STT mis-hearings before intent routing and Eve sees the ask."""

from __future__ import annotations

import re

_DOCKER_HUB_TOKEN = "__EMPIRE_DOCKER_HUB__"

# STT often emits "get hub" / "git hub" for GitHub — not Docker Hub.
_GITHUB_ALIASES = (
    re.compile(r"\bget[\s-]?hub\b", re.IGNORECASE),
    re.compile(r"\bgit\s+hub\b", re.IGNORECASE),
)

# Common STT / typo near "Beach Boys"
_BEACH_BOYS_ALIASES = re.compile(r"\bbeach\s+boises?\b", re.IGNORECASE)


def apply_speech_aliases(text: str) -> str:
    """Rewrite spoken aliases in user text; preserve explicit 'docker hub'."""
    if not text or not text.strip():
        return text
    protected = re.sub(r"\bdocker\s+hub\b", _DOCKER_HUB_TOKEN, text, flags=re.IGNORECASE)
    for pattern in _GITHUB_ALIASES:
        protected = pattern.sub("GitHub", protected)
    protected = _BEACH_BOYS_ALIASES.sub("Beach Boys", protected)
    return protected.replace(_DOCKER_HUB_TOKEN, "docker hub")
