"""Drain awaiting priority_resolved rows via mock callback (no Cognee)."""

from __future__ import annotations

from pathlib import Path

from pipeline.wiki_priority_resolved import append_resolved, drain_awaiting, list_awaiting


def test_drain_awaiting_counts(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("EMPIRE_WIKI_REPORTS_ROOT", str(tmp_path))
    (tmp_path / "2017").mkdir(parents=True)
    append_resolved(
        "2017",
        {
            "subject_id": "subj_1",
            "subject": "Cambrai",
            "subject_rank": 1,
            "title": "Cambrai",
            "path": str(tmp_path / "Cambrai.md"),
            "match_score": 1.0,
            "match_reason": "exact_normalized_title",
        },
    )
    append_resolved(
        "2017",
        {
            "subject_id": "subj_2",
            "subject": "Arras",
            "subject_rank": 2,
            "title": "Arras",
            "path": str(tmp_path / "Arras.md"),
            "match_score": 1.0,
            "match_reason": "user_confirm",
        },
    )
    calls: list[str] = []

    def cb(row: dict) -> str:
        calls.append(row["title"])
        return "ingested"

    result = drain_awaiting("2017", cb)
    assert result["drained"] == 2
    assert calls == ["Cambrai", "Arras"]
    assert list_awaiting("2017") == []
