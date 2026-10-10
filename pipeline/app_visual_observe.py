"""Capture a allowlisted or local HTML surface, then observe UI with local vision."""

from __future__ import annotations

import argparse
import json
from typing import Any

from pipeline import browser_local, vision_ui_observe


def observe(
    *,
    url: str = "",
    html_path: str = "",
    note: str = "",
    full_page: bool = False,
) -> dict[str, Any]:
    capture = browser_local.capture_screenshot(
        url=url,
        html_path=html_path,
        full_page=full_page,
        note=note,
    )
    if not capture.get("ok"):
        return capture
    screenshot_path = str(capture.get("screenshot_path") or "")
    if not screenshot_path:
        return {"ok": False, "error": "screenshot path missing", "capture": capture}
    vision = vision_ui_observe.observe(screenshot_path, note=note)
    return {
        "ok": bool(vision.get("ok")),
        "capture": capture,
        "vision": vision,
        "screenshot_path": screenshot_path,
        "note": "Playwright screenshot + qwen3-vl observation. Does not drive clicks or launch arbitrary EXEs.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE app visual observe")
    parser.add_argument("--url", default="")
    parser.add_argument("--html-path", default="")
    parser.add_argument("--full-page", action="store_true")
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)
    result = observe(
        url=args.url,
        html_path=args.html_path,
        note=args.note,
        full_page=args.full_page,
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
