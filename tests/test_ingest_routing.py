"""P13 — document routing: which suffixes take the conversion path, and which are text.

The bug this pins: `pipeline/ingest_files.py` routed **only** `.pdf` through Docling, even though the converter it
called was generic and already handled docx/pptx/xlsx. A `.docx` could therefore be read by Eve and never
remembered. The condition is now a named predicate (`needs_docling`) precisely so a test can point at it.
"""

from __future__ import annotations

import pytest

from pipeline.ingest_files import (
    ALLOWED_SUFFIXES,
    DOCLING_SUFFIXES,
    TEXT_SUFFIXES,
    needs_docling,
    validate_memory_file,
)
from pipeline.read_document import _SUPPORTED_EXTENSIONS as READ_SUFFIXES


@pytest.mark.parametrize("suffix", [".pdf", ".docx", ".pptx", ".xlsx", ".DOCX", ".Pdf"])
def test_office_and_pdf_take_the_conversion_path(suffix: str) -> None:
    assert needs_docling(__import__("pathlib").Path(f"doc{suffix}")) is True


@pytest.mark.parametrize("suffix", [".md", ".txt", ".mdx", ".eml", ".MD"])
def test_text_formats_are_read_directly(suffix: str) -> None:
    assert needs_docling(__import__("pathlib").Path(f"doc{suffix}")) is False


def test_every_allowed_suffix_is_accounted_for() -> None:
    assert ALLOWED_SUFFIXES == TEXT_SUFFIXES | DOCLING_SUFFIXES
    assert not (TEXT_SUFFIXES & DOCLING_SUFFIXES), "a suffix must not be both text and converted"


def test_the_census_gap_is_closed() -> None:
    """The two things the format census found unclaimed, and the one it found read-only-but-not-storable."""
    for suffix in (".mdx", ".eml", ".docx", ".pptx", ".xlsx"):
        assert suffix in ALLOWED_SUFFIXES, f"{suffix} must be storable now"
        assert suffix in READ_SUFFIXES, f"{suffix} must be readable too"


@pytest.mark.parametrize("suffix", [".docx", ".mdx", ".eml", ".md", ".txt", ".pdf"])
def test_validate_memory_file_accepts_the_widened_set(tmp_path, suffix: str) -> None:
    candidate = tmp_path / f"note{suffix}"
    candidate.write_text("content", encoding="utf-8")
    assert validate_memory_file(candidate) == candidate


def test_validate_memory_file_still_rejects_archives(tmp_path) -> None:
    candidate = tmp_path / "bundle.zip"
    candidate.write_bytes(b"PK\x03\x04")
    with pytest.raises(ValueError) as excinfo:
        validate_memory_file(candidate)
    assert ".docx" in str(excinfo.value), "the message must name what is actually accepted"


def test_directive_guard_still_stands(tmp_path) -> None:
    """Widening the suffix set must not have widened the directive exclusion."""
    directives = tmp_path / "directives"
    directives.mkdir()
    candidate = directives / "note.md"
    candidate.write_text("lens", encoding="utf-8")
    with pytest.raises(ValueError):
        validate_memory_file(candidate)


def test_empty_file_is_still_refused(tmp_path) -> None:
    candidate = tmp_path / "empty.docx"
    candidate.write_bytes(b"")
    with pytest.raises(ValueError):
        validate_memory_file(candidate)
