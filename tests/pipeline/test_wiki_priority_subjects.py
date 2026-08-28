"""Unit tests for ranked priority subject queue helpers."""

from __future__ import annotations

from pathlib import Path

from pipeline.wiki_priority_subjects import (
    add_subjects,
    delete_subject,
    empty_queue,
    load_subjects,
    move_subject,
    patch_subject,
    renumber,
    save_subjects,
)


def test_add_move_renumber_dense(tmp_path: Path):
    path = tmp_path / "priority_subjects.json"
    doc = empty_queue("2017")
    doc = add_subjects(doc, ["Alpha", "Beta", "Gamma"], updated_by="test")
    save_subjects(doc, path)
    doc = load_subjects(path)
    assert [s["rank"] for s in doc["subjects"]] == [1, 2, 3]
    beta_id = doc["subjects"][1]["id"]
    doc = move_subject(doc, beta_id, "up")
    save_subjects(doc, path)
    doc = load_subjects(path)
    assert [s["subject"] for s in doc["subjects"]] == ["Beta", "Alpha", "Gamma"]
    assert [s["rank"] for s in doc["subjects"]] == [1, 2, 3]


def test_edit_subject_resets_pending(tmp_path: Path):
    path = tmp_path / "priority_subjects.json"
    doc = empty_queue()
    doc = add_subjects(doc, [{"subject": "guitar", "intent": "demo"}], updated_by="test")
    doc["subjects"][0]["status"] = "needs_confirm"
    doc["subjects"][0]["candidates"] = [{"title": "Guitar"}]
    sid = doc["subjects"][0]["id"]
    doc = patch_subject(doc, sid, subject="Bass guitar")
    assert doc["subjects"][0]["status"] == "pending"
    assert doc["subjects"][0]["candidates"] == []
    assert doc["subjects"][0]["intent"] == "demo"
    save_subjects(doc, path)


def test_intent_only_keeps_status(tmp_path: Path):
    path = tmp_path / "priority_subjects.json"
    doc = empty_queue()
    doc = add_subjects(doc, [{"subject": "Cambrai", "intent": "old"}], updated_by="test")
    doc["subjects"][0]["status"] = "queued"
    sid = doc["subjects"][0]["id"]
    doc = patch_subject(doc, sid, intent="new note")
    assert doc["subjects"][0]["status"] == "queued"
    assert doc["subjects"][0]["intent"] == "new note"
    save_subjects(doc, path)


def test_delete_removes_id(tmp_path: Path):
    path = tmp_path / "priority_subjects.json"
    doc = empty_queue()
    doc = add_subjects(doc, ["A", "B"], updated_by="test")
    sid = doc["subjects"][0]["id"]
    doc = delete_subject(doc, sid)
    assert len(doc["subjects"]) == 1
    assert doc["subjects"][0]["subject"] == "B"
    assert doc["subjects"][0]["rank"] == 1
    save_subjects(doc, path)
    assert renumber(doc)["subjects"][0]["rank"] == 1
