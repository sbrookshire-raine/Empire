import json
from pathlib import Path

from pipeline.wiki_title_matcher import (
    decide_match,
    normalize_text,
    score_subject_against_titles,
)

FIXTURE = json.loads(
    Path("tests/pipeline/fixtures/wiki_title_catalog.json").read_text(encoding="utf-8")
)


def test_normalize_collapses_whitespace():
    assert normalize_text("  Battle   of  Cambrai ") == "battle of cambrai"


def test_exact_alias_auto_accepts_cambrai():
    cands = score_subject_against_titles("Battle of Cambrai", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "auto"
    assert decision["primary"].title == "Cambrai"


def test_guitar_needs_confirm_does_not_auto_all_contains():
    cands = score_subject_against_titles("guitar", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "needs_confirm"
    assert len(decision["candidates"]) >= 2


def test_unmatched_subject():
    cands = score_subject_against_titles("zzzxnotapage999", FIXTURE)
    decision = decide_match(cands)
    assert decision["decision"] == "unmatched"


def test_rejects_stopword_and_letter_titles():
    catalog = [
        {"title": "The", "path": "a.md", "page_id": "1"},
        {"title": "T", "path": "b.md", "page_id": "2"},
        {"title": "A", "path": "c.md", "page_id": "3"},
        {"title": "An", "path": "d.md", "page_id": "4"},
        {"title": "Bala", "path": "bala.md", "page_id": "7"},
        {"title": "Emer", "path": "emer.md", "page_id": "8"},
        {"title": "Positive feedback", "path": "e.md", "page_id": "5"},
        {"title": "Reinforcing loop", "path": "f.md", "page_id": "6"},
    ]
    cands = score_subject_against_titles("The Reinforcing Loop", catalog)
    titles = {c.title for c in cands}
    assert "The" not in titles
    assert "T" not in titles
    assert "A" not in titles
    assert "An" not in titles
    assert "Bala" not in titles
    assert "Emer" not in titles
    assert "Reinforcing loop" in titles
