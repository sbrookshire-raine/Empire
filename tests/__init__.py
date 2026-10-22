# namespace package
"""The test package points the Toolbelt file at a temp file.

The toolbelt file is the OPERATOR's: it lives in %LOCALAPPDATA%\\EMPIRE and
holds the Architect's limb selection. A test that touches the toolbelt path
(e.g. `apply_active_tools`, which persists what it is given) used to write
that real file - so running the unit tests turned the voice_presence limb
OFF. The env override is read by `frontend.eve_toolbelt._toolbelt_path`.

This module is imported by BOTH pytest (package collection) and unittest
discovery (top_level_dir="."), so the guard covers the gate's own test run
as well as a developer's.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

if not os.environ.get("EMPIRE_TOOLBELT_PATH"):
    os.environ["EMPIRE_TOOLBELT_PATH"] = str(
        Path(tempfile.gettempdir()) / f"empire-test-toolbelt-{os.getpid()}.json"
    )

