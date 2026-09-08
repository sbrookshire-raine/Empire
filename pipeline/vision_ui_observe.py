"""UI/screen observation via local vision model — observation only (no actuators).

Uses Ollama qwen3-vl with a structured prompt. OmniParser remains an optional
future upgrade if Architect wants dedicated region parsing weights.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from pipeline import vision_local

UI_PROMPT = (
    "Observe this screenshot for EMPIRE. List visible UI regions as JSON array of "
    '{"label","approx_location","text_if_any"}. Observation only — do not suggest clicks '
    "or automation steps. Be concrete."
)


def observe(image_path: str | Path, *, note: str = "") -> dict[str, Any]:
    result = vision_local.describe_image(
        image_path,
        prompt=UI_PROMPT if not note else f"{UI_PROMPT}\nArchitect note: {note}",
        write_note=True,
    )
    if isinstance(result, dict):
        result["mode"] = "observation_only"
        result["actuators"] = False
        result["omniparser"] = "not_bundled_use_qwen3_vl_structured_observe"
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE UI observe (no actuators)")
    parser.add_argument("image_path")
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)
    result = observe(args.image_path, note=args.note)
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
