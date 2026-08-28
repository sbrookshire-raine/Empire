from pathlib import Path

from pipeline.wiki_codex_seed import parse_codex_primitives, seed_from_codex
from pipeline.wiki_priority_resolve import resolve_pending_subjects
from pipeline.wiki_priority_subjects import empty_queue, load_subjects, save_subjects
from pipeline.wiki_priority_resolved import load_resolved_lines
from pipeline.wiki_title_matcher import decide_match, score_subject_against_titles
import json


FIXTURE = json.loads(
    Path("tests/pipeline/fixtures/wiki_title_catalog.json").read_text(encoding="utf-8")
)

SAMPLE = """# THE MASTER CODEX

## I. CYBERNETICS & SYSTEM DYNAMICS (Feedback & Flow)

*italic blurb*

1. **The Reinforcing Loop:** Output feeds back into input.
2. **The Balancing Loop:** Counter-forces restore equilibrium.

## II. OTHER

1. **The Structural Echo (Conway's Law):** Org charts shape systems.
"""


def test_parse_codex_primitives():
    rows = parse_codex_primitives(SAMPLE)
    assert len(rows) == 3
    assert rows[0]["subject"] == "The Reinforcing Loop"
    assert "CYBERNETICS" in rows[0]["intent"]


def test_seed_skips_duplicates(tmp_path: Path, monkeypatch):
    subjects = tmp_path / "subjects.json"
    codex = tmp_path / "codex.md"
    codex.write_text(SAMPLE, encoding="utf-8")
    doc = empty_queue()
    doc["subjects"] = [
        {
            "id": "subj_x",
            "rank": 1,
            "subject": "The Reinforcing Loop",
            "intent": "existing",
            "added_at": "2026-01-01T00:00:00Z",
            "status": "pending",
            "candidates": [],
            "selected_articles": [],
            "resolved": None,
            "suggestions": [],
        }
    ]
    save_subjects(doc, subjects)
    result = seed_from_codex(codex_path=codex, subjects_file=subjects, dry_run=False)
    assert result["added"] == 2
    loaded = load_subjects(subjects)
    assert len(loaded["subjects"]) == 3


def test_resolve_cambrai_auto(tmp_path: Path, monkeypatch):
    subjects = tmp_path / "subjects.json"
    reports = tmp_path / "reports" / "2017"
    reports.mkdir(parents=True)
    monkeypatch.setenv("EMPIRE_PRIORITY_SUBJECTS", str(subjects))
    monkeypatch.setenv("EMPIRE_WIKI_REPORTS_ROOT", str(tmp_path / "reports"))
    doc = empty_queue("2017")
    from pipeline.wiki_priority_subjects import add_subjects

    doc = add_subjects(doc, ["Cambrai"], updated_by="test")
    save_subjects(doc, subjects)
    summary = resolve_pending_subjects("2017", catalog=FIXTURE)
    assert summary["counts"]["auto"] == 1
    lines = load_resolved_lines("2017")
    assert len(lines) == 1
    assert lines[0]["title"] == "Cambrai"


def test_resolve_guitar_needs_confirm_zero_resolved(tmp_path: Path, monkeypatch):
    subjects = tmp_path / "subjects.json"
    monkeypatch.setenv("EMPIRE_PRIORITY_SUBJECTS", str(subjects))
    monkeypatch.setenv("EMPIRE_WIKI_REPORTS_ROOT", str(tmp_path / "reports"))
    (tmp_path / "reports" / "2017").mkdir(parents=True)
    doc = empty_queue("2017")
    from pipeline.wiki_priority_subjects import add_subjects

    doc = add_subjects(doc, ["guitar"], updated_by="test")
    save_subjects(doc, subjects)
    summary = resolve_pending_subjects("2017", catalog=FIXTURE)
    assert summary["counts"]["needs_confirm"] == 1
    assert summary["counts"]["resolved_appended"] == 0
    assert load_resolved_lines("2017") == []
    cands = score_subject_against_titles("guitar", FIXTURE)
    assert decide_match(cands)["decision"] == "needs_confirm"
