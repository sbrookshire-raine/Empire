#!/usr/bin/env python3
"""MDX/HTML cleanup helpers for docs-guide-scraper (local EMPIRE)."""

from __future__ import annotations

import re

LEFT_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9]*(?:\s[^>]{0,60})?>")
ESCAPE_FIX = re.compile(r"\\([#\-_*])")


def strip_leftover_tags(text: str) -> str:
    return LEFT_TAG.sub("", text or "")


def fix_markdown_escapes(text: str) -> str:
    return ESCAPE_FIX.sub(r"\1", text or "")


def absolutize_links(text: str, origin: str) -> str:
    """Prefix root-relative href/src with origin."""
    if not origin:
        return text

    def repl(match: re.Match[str]) -> str:
        attr, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "#", "mailto:", "data:")):
            return match.group(0)
        if url.startswith("/"):
            return f'{attr}="{origin.rstrip("/")}{url}"'
        return match.group(0)

    return re.sub(r'(href|src)="([^"]+)"', repl, text or "")


def clean_page_markdown(text: str, *, origin: str = "") -> str:
    text = fix_markdown_escapes(text)
    text = strip_leftover_tags(text)
    if origin:
        text = absolutize_links(text, origin)
    return text.strip()
