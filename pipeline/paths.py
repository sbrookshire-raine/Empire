"""Canonical path jailing — one implementation for every tool that accepts a path.

Why this exists: the servers disagreed. Some called `.resolve()`, others did not, and **nothing enforced
containment**, so a tool handed a model-supplied path had no guarantee it stayed inside its declared root.
Independently flagged by two reviewers (2026-09-27); it is the highest-value open item because it fixes code
that already ships rather than adding code to maintain.

**Why this file is not under `mcp/`.** Outside advice proposed `mcp/lib/security.py`. That is a trap here: this
repository has a top-level `mcp/` directory, and the MCP SDK ships a package also named `mcp`. Our directory only
behaves as an implicit namespace package because the SDK's *regular* package (with `__init__.py`) takes
precedence — so `from mcp.lib.security import ...` would resolve inside the SDK and fail. `pipeline/` is a real
package here and is already where shared code lives (`pipeline.cognee_subprocess` is imported by the servers).

Usage::

    from pipeline.paths import PathOutsideRoot, resolve_within

    target = resolve_within(raw_path, ROOT, label="document")   # raises PathOutsideRoot if it escapes
"""

from __future__ import annotations

from pathlib import Path


class PathOutsideRoot(Exception):
    """A requested path resolves outside its declared root.

    Raised rather than returned so a caller cannot accidentally continue with an unsafe path. Servers turn this
    into their own structured failure (`{ok: false, error}`), naming the server — per OPERATING_CONTRACT §5.
    """


def is_within(candidate: Path | str, root: Path | str) -> bool:
    """True when `candidate` canonicalises to `root` itself or something beneath it.

    Both sides are resolved, so a symlink inside the root that points outside it is refused, and a root that is
    itself reached through a link still compares correctly.
    """
    try:
        resolved_root = Path(root).expanduser().resolve()
        resolved_candidate = Path(candidate).expanduser().resolve()
    except (OSError, RuntimeError):  # unresolvable path (broken link, illegal name, loop)
        return False
    return resolved_candidate == resolved_root or resolved_candidate.is_relative_to(resolved_root)


def resolve_within(raw: Path | str, root: Path | str, *, label: str = "path") -> Path:
    """Canonicalise `raw` and require it to live inside `root`.

    Returns the resolved absolute path on success. Raises `PathOutsideRoot` when the value is empty, when the
    root is not a directory, or when the path escapes — including via `..`, an absolute path elsewhere, or a
    symlink. The error text names the label and the root so the message is actionable without leaking the
    caller's internals.
    """
    if raw is None or not str(raw).strip():
        raise PathOutsideRoot(f"{label} is required")

    resolved_root = Path(root).expanduser().resolve()
    if not resolved_root.is_dir():
        raise PathOutsideRoot(f"{label} root is not a directory: {resolved_root}")

    # Relative values are interpreted against the declared root, never the process working directory: a tool
    # receives paths like "02_Skills_and_Prompts" and means "inside the root". The first version resolved them
    # against cwd and refused every legitimate relative path — caught by tests/test_paths.py, 2026-09-27.
    candidate = Path(raw).expanduser()
    if not candidate.is_absolute():
        candidate = resolved_root / candidate

    if not is_within(candidate, resolved_root):
        raise PathOutsideRoot(f"{label} resolves outside the declared root ({resolved_root})")

    return candidate.resolve()
