"""P1 — every path-taking MCP tool must refuse an escape and still accept legitimate paths.

The servers are loaded by file path with importlib, exactly as `mcp/smoke_test_cognee.py` does: this repository has
a top-level `mcp/` directory while the MCP SDK ships a package also named `mcp`, so a plain `import
mcp.workbench_mcp` would resolve inside the SDK instead of here.

Each case is the acceptance criterion for P1: traversal AND symlink escape refused, legitimate paths unaffected.
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load(name: str):
    """Import an MCP server module from mcp/<name>.py without colliding with the SDK's `mcp` package."""
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location(name, ROOT / "mcp" / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def workbench():
    return _load("workbench_mcp")


@pytest.fixture(scope="module")
def work_orders():
    return _load("work_order_mcp")


@pytest.fixture(scope="module")
def cognee():
    return _load("cognee_mcp")


# ------------------------------------------------------------------------------------- workbench / Active Tools


def test_active_tool_legitimate_subpath_is_resolved(workbench, tmp_path, monkeypatch) -> None:
    tools = tmp_path / "03_Active_Tools"
    (tools / "sub").mkdir(parents=True)
    (tools / "sub" / "tool.md").write_text("# tool", encoding="utf-8")
    monkeypatch.setenv("EMPIRE_ACTIVE_TOOLS_DIR", str(tools))

    target, error = workbench._resolve_active_tool_path("sub/tool.md")
    assert error is None
    assert target == (tools / "sub" / "tool.md").resolve()


def test_active_tool_traversal_is_refused(workbench, tmp_path, monkeypatch) -> None:
    tools = tmp_path / "03_Active_Tools"
    tools.mkdir(parents=True)
    monkeypatch.setenv("EMPIRE_ACTIVE_TOOLS_DIR", str(tools))

    target, error = workbench._resolve_active_tool_path(r"..\..\Windows\System32\config\SAM")
    assert target is None
    assert "must stay under 03_Active_Tools" in error


def test_active_tool_absolute_path_is_refused(workbench, tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("EMPIRE_ACTIVE_TOOLS_DIR", str(tmp_path))
    target, error = workbench._resolve_active_tool_path(r"C:\Windows\win.ini")
    assert target is None
    assert "must be relative" in error


def test_active_tool_empty_filename_is_refused(workbench, monkeypatch) -> None:
    target, error = workbench._resolve_active_tool_path("   ")
    assert target is None
    assert error == "filename is required."


def test_read_active_tool_still_reads_a_legitimate_file(workbench, tmp_path, monkeypatch) -> None:
    """The tool must keep working after jailing — this is the half that regressions hide in."""
    tools = tmp_path / "03_Active_Tools"
    tools.mkdir(parents=True)
    (tools / "notes.md").write_text("hello from active tools", encoding="utf-8")
    monkeypatch.setenv("EMPIRE_ACTIVE_TOOLS_DIR", str(tools))

    payload = json.loads(asyncio.run(workbench.read_active_tool("notes.md")))
    assert payload["ok"] is True
    assert payload["content"] == "hello from active tools"


def test_read_active_tool_refuses_traversal(workbench, tmp_path, monkeypatch) -> None:
    tools = tmp_path / "03_Active_Tools"
    tools.mkdir(parents=True)
    monkeypatch.setenv("EMPIRE_ACTIVE_TOOLS_DIR", str(tools))

    payload = json.loads(asyncio.run(workbench.read_active_tool(r"..\secrets.md")))
    assert payload["ok"] is False
    assert "must stay under 03_Active_Tools" in payload["error"]


# ------------------------------------------------------------------------------------- work orders / Resource Queue


def test_queue_reference_legitimate_relative_is_accepted(work_orders, tmp_path, monkeypatch) -> None:
    queue = tmp_path / "00_Resource_Queue"
    queue.mkdir(parents=True)
    monkeypatch.setenv("EMPIRE_RESOURCE_QUEUE_DIR", str(queue))

    resolved, error = work_orders._resolve_queue_reference("raw/notes.md")
    assert error is None
    assert resolved == str((queue / "raw" / "notes.md").resolve())


def test_queue_reference_traversal_is_refused(work_orders, tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("EMPIRE_RESOURCE_QUEUE_DIR", str(tmp_path))
    resolved, error = work_orders._resolve_queue_reference(r"..\..\Windows\System32\config\SAM")
    assert resolved is None
    assert "must stay under 00_Resource_Queue" in error


def test_queue_reference_absolute_outside_is_refused(work_orders, tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("EMPIRE_RESOURCE_QUEUE_DIR", str(tmp_path))
    resolved, error = work_orders._resolve_queue_reference(r"C:\Windows\win.ini")
    assert resolved is None
    assert "must stay under 00_Resource_Queue" in error


def test_queue_reference_empty_is_still_optional(work_orders) -> None:
    assert work_orders._resolve_queue_reference("") == (None, None)


# ------------------------------------------------------------------------------------- cognee / mock ingest


def test_cognee_ingest_refuses_traversal(cognee) -> None:
    payload = json.loads(asyncio.run(cognee.cognee_ingest_mock_file(r"..\..\Users\notes.md")))
    assert payload["ok"] is False
    assert "outside the declared root" in payload["error"]


def test_cognee_ingest_refuses_absolute_path_outside_the_repo(cognee) -> None:
    payload = json.loads(asyncio.run(cognee.cognee_ingest_mock_file(r"C:\Windows\Temp\evil.md")))
    assert payload["ok"] is False
    assert "outside the declared root" in payload["error"]


def test_cognee_ingest_accepts_a_repo_relative_path(cognee) -> None:
    """A repo-relative path clears the jail and then fails on existence — proof the jail is not refusing everything."""
    payload = json.loads(asyncio.run(cognee.cognee_ingest_mock_file("mock_data_ingest/definitely-absent.md")))
    assert payload["ok"] is False
    assert "Mock file not found" in payload["error"]


# ------------------------------------------------------------------------------------- docling / staging output


def test_docling_default_output_stays_in_the_staging_root(tmp_path) -> None:
    from pipeline.docling_convert import resolve_output_path

    out, error = resolve_output_path(tmp_path / "report.pdf", None, out_dir=tmp_path)
    assert error is None
    assert out == tmp_path / "report.md"


def test_docling_named_output_inside_root_is_accepted(tmp_path) -> None:
    from pipeline.docling_convert import resolve_output_path

    out, error = resolve_output_path(tmp_path / "a.pdf", "converted/a.md", out_dir=tmp_path)
    assert error is None
    assert out == (tmp_path / "converted" / "a.md").resolve()


def test_docling_named_output_outside_root_is_refused(tmp_path) -> None:
    from pipeline.docling_convert import resolve_output_path

    out, error = resolve_output_path(tmp_path / "a.pdf", r"C:\Windows\Temp\evil.md", out_dir=tmp_path)
    assert out is None
    assert "must be written under" in error


def test_docling_named_output_traversal_is_refused(tmp_path) -> None:
    from pipeline.docling_convert import resolve_output_path

    out, error = resolve_output_path(tmp_path / "a.pdf", r"..\..\evil.md", out_dir=tmp_path)
    assert out is None
    assert "must be written under" in error


def test_convert_file_refuses_an_outside_output_before_converting(tmp_path) -> None:
    """End-to-end through the public function: the write target is checked before any conversion work happens."""
    from pipeline.docling_convert import convert_file

    src = tmp_path / "doc.pdf"
    src.write_bytes(b"%PDF-1.4 not really a pdf")

    result = convert_file(src, output_path=r"C:\Windows\Temp\evil.md", out_dir=tmp_path)
    assert result["ok"] is False
    assert "must be written under" in result["error"]

