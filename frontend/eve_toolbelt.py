"""Persist Workbench toolbelt categories so Eve can filter heavy limb tools.

Core brain tools (Cognee memory + PocketBase tasks + health/models) are NEVER
gated here — they stay permanently registered. This file only tracks optional
limbs, grouped into clarity buckets (Always / Session / Products).

See docs/EMPIRE_CLARITY.md.
"""

from __future__ import annotations

import json
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Literal

Bucket = Literal["always", "session", "products"]

# Optional limbs only — default Voice + Wiki Local (session glasses).
ALLOWED_CATEGORIES = (
    "gumloop_cloud",
    "web_research",
    "tool_forge",
    "wiki_local",
    "time_reclaim",
    "stem_factory",
    "web_scout",
    "thought_experiments",
    "voice_presence",
    "vision_local",
    "container_scout",
    "github_scout",
    "structured_extract",
    "retrieval_rerank",
    "browser_local",
    "loom_intake",
    "workspace_search",
    "query_data",
    "read_document",
    "create_spreadsheet",
    "author_code",
    "python_verify",
    "switchboard",
    "system_ops",
    "file_ops",
    "rea",
    "rea_skills",
    "claim_ledger",
    "heptabase",
)

CATEGORY_BUCKETS: dict[str, Bucket] = {
    "voice_presence": "always",
    "wiki_local": "session",
    "web_scout": "session",
    "github_scout": "session",
    "thought_experiments": "session",
    "container_scout": "session",
    "structured_extract": "session",
    "retrieval_rerank": "session",
    "browser_local": "session",
    "loom_intake": "session",
    "tool_forge": "session",
    "web_research": "session",
    "gumloop_cloud": "session",
    "vision_local": "session",
    "time_reclaim": "products",
    "stem_factory": "products",
    "workspace_search": "session",
    "query_data": "session",
    "read_document": "session",
    "create_spreadsheet": "session",
    "author_code": "session",
    "python_verify": "session",
    "switchboard": "session",
    "system_ops": "session",
    "file_ops": "session",
    "rea": "session",
    "rea_skills": "session",
    "claim_ledger": "session",
    "heptabase": "session",
}

BUCKET_ORDER: tuple[Bucket, ...] = ("always", "session", "products")
BUCKET_LABELS: dict[Bucket, str] = {
    "always": "Always (core UX)",
    "session": "Session",
    "products": "Products (LEGO)",
}

# Fresh installs: no optional limbs ON (Voice/Wiki/ scouts start via header strip or Eve ACTIVATE).
DEFAULT_ACTIVE_TOOLS: tuple[str, ...] = ()
# v1 toolbelt files without defaults_version were upgraded to voice+wiki automatically.
_LEGACY_V1_AUTO_DEFAULTS: tuple[str, ...] = ("voice_presence", "wiki_local")
DEFAULTS_VERSION = 3


def _toolbelt_path() -> Path:
    # An explicit override. The toolbelt file is the OPERATOR's: it lives in
    # %LOCALAPPDATA%\EMPIRE, and the test suite points it at a temp file so
    # no test can rewrite the Architect's selection (it did - see
    # tests/__init__.py).
    override = os.environ.get("EMPIRE_TOOLBELT_PATH", "").strip()
    if override:
        return Path(override)
    local_app = os.environ.get("LOCALAPPDATA", "").strip()
    if local_app:
        folder = Path(local_app) / "EMPIRE"
        try:
            folder.mkdir(parents=True, exist_ok=True)
            return folder / "eve-toolbelt.json"
        except OSError:
            pass
    root = Path(__file__).resolve().parents[1]
    return root / "config" / "eve-toolbelt.json"


def category_bucket(category: str) -> Bucket:
    return CATEGORY_BUCKETS.get(category, "session")


def categories_by_bucket() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {b: [] for b in BUCKET_ORDER}
    for cat in ALLOWED_CATEGORIES:
        out[category_bucket(cat)].append(cat)
    return out


def normalize_active_tools(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return list(DEFAULT_ACTIVE_TOOLS)
    selected: list[str] = []
    for item in raw:
        if not isinstance(item, str):
            continue
        cleaned = item.strip()
        if cleaned in ALLOWED_CATEGORIES and cleaned not in selected:
            selected.append(cleaned)
    return selected


def write_active_tools(categories: list[str]) -> Path:
    path = _toolbelt_path()
    payload = {
        "active_tools": categories,
        "defaults_version": DEFAULTS_VERSION,
        "buckets": categories_by_bucket(),
    }
    encoded = json.dumps(payload, indent=2) + "\n"
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        # Atomic: the agent reads this file on every tool check, so a
        # half-written file must never be observable.
        handle, tmp_name = tempfile.mkstemp(
            prefix="toolbelt-", suffix=".json", dir=str(path.parent)
        )
        tmp_path = Path(tmp_name)
        try:
            with os.fdopen(handle, "w", encoding="utf-8") as stream:
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(tmp_path, path)
        except Exception:
            tmp_path.unlink(missing_ok=True)
            raise
    except OSError:
        pass
    return path


def _version_number(raw: Any) -> int:
    """Coerce a stored defaults_version to int, tolerating legacy shapes.

    Older/foreign toolbelt files may hold a string ("1", "2.0") or junk. An
    unparsable value reads as 0 so the file is treated as legacy and migrated
    toward DEFAULT_ACTIVE_TOOLS instead of raising inside session creation.
    """
    if isinstance(raw, bool):
        return int(raw)
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw)
    if isinstance(raw, str):
        try:
            return int(float(raw.strip()))
        except ValueError:
            return 0
    return 0


def load_active_tools() -> list[str]:
    path = _toolbelt_path()
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return list(DEFAULT_ACTIVE_TOOLS)
    if not isinstance(parsed, dict):
        return list(DEFAULT_ACTIVE_TOOLS)
    selected = normalize_active_tools(parsed.get("active_tools"))
    version = _version_number(parsed.get("defaults_version"))
    if version < DEFAULTS_VERSION:
        if version < 2:
            for default_tool in _LEGACY_V1_AUTO_DEFAULTS:
                if default_tool not in selected:
                    selected = normalize_active_tools([*selected, default_tool])
        parsed["active_tools"] = selected
        parsed["defaults_version"] = DEFAULTS_VERSION
        parsed["buckets"] = categories_by_bucket()
        try:
            path.write_text(json.dumps(parsed, indent=2) + "\n", encoding="utf-8")
        except OSError:
            pass
    return selected


def category_enabled(category: str) -> bool:
    return category in load_active_tools()


def capability_enabled(category: str) -> bool:
    """Manual Toolbelt OR valid Research Autopilot session grant."""
    try:
        from pipeline import admission_controller

        return admission_controller.capability_active(category)
    except Exception:
        return category_enabled(category)


def load_effective_tools() -> list[str]:
    try:
        from pipeline import admission_controller

        return admission_controller.load_effective_tools()
    except Exception:
        return load_active_tools()


def extract_active_tools(payload: Any) -> list[str] | None:
    """Read the requested toolbelt from a chat payload — flat or nested.

    Two shapes reach the Workbench:

    - flat: ``{"active_tools": ["wiki_local"]}`` — what the browser sends.
    - nested: ``{"toolbelt": {"active_tools": ["wiki_local"]}}`` — what the live
      harnesses used to send. The toolbelt path only ever read the flat shape,
      so the nested one was silently discarded: the harness measured Eve
      against a toolbelt it never actually asked for.

    The flat shape wins when both are present. ``None`` means "this payload
    carries no toolbelt" and must never be confused with "an empty toolbelt":
    the first leaves the persisted selection alone, the second clears it.
    """

    if not isinstance(payload, dict):
        return None
    raw = payload.get("active_tools")
    if isinstance(raw, list):
        return normalize_active_tools(raw)
    nested = payload.get("toolbelt")
    if isinstance(nested, dict):
        inner = nested.get("active_tools")
        if isinstance(inner, list):
            return normalize_active_tools(inner)
    return None


def apply_active_tools(payload: dict[str, Any]) -> dict[str, Any]:
    """Read the requested toolbelt from the chat payload, persist, strip before Eve.

    Both shapes are accepted (see `extract_active_tools`) and both keys are
    stripped: Eve reads the persisted toolbelt file, so a leftover `toolbelt`
    object in the forwarded payload is dead weight the upstream must not see.
    """

    categories = extract_active_tools(payload)
    if categories is None:
        return payload
    write_active_tools(categories)
    cleaned = dict(payload)
    cleaned.pop("active_tools", None)
    cleaned.pop("toolbelt", None)
    return cleaned


def _snapshot_toolbelt() -> tuple[bool, bytes | None]:
    """The operator's toolbelt file, verbatim.

    Returns ``(existed, payload)``. A MISSING file and a file holding an
    empty list are NOT the same state: the agent falls back to Voice + Wiki
    only when the file is absent, so the restore has to be byte-exact.
    """

    path = _toolbelt_path()
    try:
        return True, path.read_bytes()
    except FileNotFoundError:
        return False, None
    except OSError:
        return True, None


def _restore_toolbelt(snapshot: tuple[bool, bytes | None]) -> None:
    """Put the operator's toolbelt file back exactly as it was found."""

    existed, payload = snapshot
    path = _toolbelt_path()
    try:
        if not existed:
            path.unlink(missing_ok=True)
        elif payload is not None:
            path.write_bytes(payload)
    except OSError:
        pass


@contextmanager
def temporary_active_tools(
    categories: list[str], *, merge: bool = False
) -> Iterator[list[str]]:
    """Run with a temporary toolbelt, then restore the operator's selection.

    The live harnesses ask for a specific toolbelt so a measurement is
    attributable to a known surface. Writing it is a side effect on the
    operator's file, so the previous selection is restored — including when
    the harness fails part-way.

    The restore is BYTE-EXACT: the file is put back exactly as it was found,
    and a file that did not exist is removed again. Re-writing a normalised
    (possibly empty) list instead would silently turn the voice_presence
    limb OFF on a fresh install, because the agent only falls back to its
    default Voice + Wiki selection when the file is ABSENT.

    ``merge=True`` keeps the operator's current limbs and ADDS ``categories``
    to them — for a harness that needs wiki + voice without switching the
    operator's other limbs off for the duration of the run.
    """

    # Snapshot FIRST. `load_active_tools` migrates a legacy file in place
    # (it rewrites the file), so reading it before the snapshot would
    # capture the migrated version instead of the operator's original.
    snapshot = _snapshot_toolbelt()
    current = load_active_tools()
    wanted = [*current, *categories] if merge else categories
    applied = normalize_active_tools(wanted)
    write_active_tools(applied)
    try:
        yield applied
    finally:
        _restore_toolbelt(snapshot)


def toolbelt_meta() -> dict[str, Any]:
    """API-shaped metadata for Workbench grouping."""
    return {
        "buckets": [
            {
                "id": bucket,
                "label": BUCKET_LABELS[bucket],
                "categories": categories_by_bucket()[bucket],
            }
            for bucket in BUCKET_ORDER
        ],
        "defaults": list(DEFAULT_ACTIVE_TOOLS),
        "defaults_version": DEFAULTS_VERSION,
    }
