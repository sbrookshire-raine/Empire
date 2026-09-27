"""Tests for pipeline.paths — canonical path jailing (P1).

Acceptance for P1 is stated as: a traversal attempt AND a symlink escape must both be refused, while legitimate
paths keep working. These are those cases, plus the edges that decide whether the helper is usable at all
(a path that does not exist yet, the root itself, an empty value, a root that is not a directory).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from pipeline.paths import PathOutsideRoot, is_within, resolve_within


@pytest.fixture()
def root(tmp_path: Path) -> Path:
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "note.md").write_text("hello", encoding="utf-8")
    return tmp_path


def test_legitimate_nested_path_is_returned_resolved(root: Path) -> None:
    target = resolve_within("docs/note.md", root, label="document")
    assert target == (root / "docs" / "note.md").resolve()
    assert target.is_file()


def test_path_that_does_not_exist_yet_is_allowed(root: Path) -> None:
    # A tool writing a new transcript must be able to name a file that is not there yet.
    target = resolve_within("docs/new-output.md", root)
    assert target.parent == (root / "docs").resolve()


def test_root_itself_is_allowed(root: Path) -> None:
    assert resolve_within(root, root) == root.resolve()


def test_traversal_out_of_root_is_refused(root: Path) -> None:
    with pytest.raises(PathOutsideRoot) as excinfo:
        resolve_within(r"..\..\Windows\System32\config\SAM", root, label="mount")
    assert "mount" in str(excinfo.value)
    assert "outside the declared root" in str(excinfo.value)


def test_absolute_path_outside_root_is_refused(root: Path) -> None:
    with pytest.raises(PathOutsideRoot):
        resolve_within(Path(os.environ.get("WINDIR", r"C:\Windows")) / "System32", root)


def test_sibling_directory_with_shared_prefix_is_refused(root: Path) -> None:
    # The classic startswith() bug: "C:\data-evil" starts with "C:\data".
    sibling = root.parent / (root.name + "-evil")
    sibling.mkdir(exist_ok=True)
    try:
        assert is_within(sibling, root) is False
        with pytest.raises(PathOutsideRoot):
            resolve_within(sibling, root)
    finally:
        sibling.rmdir()


def test_empty_value_is_refused(root: Path) -> None:
    for value in ("", "   ", None):
        with pytest.raises(PathOutsideRoot):
            resolve_within(value, root)


def test_root_that_is_not_a_directory_is_refused(root: Path) -> None:
    with pytest.raises(PathOutsideRoot):
        resolve_within("docs/note.md", root / "docs" / "note.md")


def test_symlink_escape_is_refused(root: Path) -> None:
    """A link inside the root pointing outside it must not become a way out.

    Creating a symlink on Windows needs privilege (or Developer Mode), so this is skipped rather than failed
    when the OS refuses — but it is the case that matters most, so it is tested whenever the OS allows it.
    """
    outside = root.parent / "outside-secret.txt"
    outside.write_text("secret", encoding="utf-8")
    link = root / "escape.txt"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks not permitted on this host")

    assert is_within(link, root) is False
    with pytest.raises(PathOutsideRoot):
        resolve_within(link, root)


def test_is_within_is_true_for_the_root_and_its_children(root: Path) -> None:
    assert is_within(root, root) is True
    assert is_within(root / "docs", root) is True
    assert is_within(root.parent, root) is False
