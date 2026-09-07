"""Local vision via Ollama qwen3-vl (Toolbelt vision_local)."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pipeline import gpu_lease
from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_OLLAMA = os.environ.get("EMPIRE_OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
DEFAULT_MODEL = os.environ.get("EMPIRE_VISION_MODEL", "qwen3-vl:8b")
DEFAULT_NOTES_DIR = Path(
    os.environ.get(
        "EMPIRE_VISION_NOTES_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\vision_notes",
    )
)


def _normalize_ollama(raw: str | None) -> str:
    value = (raw or DEFAULT_OLLAMA).strip().rstrip("/")
    if not value:
        return "http://127.0.0.1:11434"
    if "://" not in value:
        value = f"http://{value}"
    if "://0.0.0.0" in value:
        value = value.replace("://0.0.0.0", "://127.0.0.1", 1)
    return value


def describe_image(
    image_path: str | Path,
    *,
    prompt: str = "Describe this image for the Architect. Be concrete.",
    model: str | None = None,
    ollama_url: str | None = None,
    write_note: bool = True,
) -> dict[str, Any]:
    path = Path(image_path)
    if not path.is_file():
        return {"ok": False, "error": f"not a file: {path}"}

    lease = gpu_lease.acquire(
        "vision",
        holder="vision_describe",
        note=f"{model or DEFAULT_MODEL}",
    )
    if not lease.get("ok"):
        return lease

    try:
        raw = path.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        base = _normalize_ollama(ollama_url)
        payload = {
            "model": model or DEFAULT_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                    "images": [b64],
                }
            ],
            "stream": False,
            "options": {"num_ctx": 8192, "temperature": 0.2},
        }
        req = Request(
            f"{base}/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        message = data.get("message") if isinstance(data, dict) else {}
        text = ""
        if isinstance(message, dict):
            text = str(message.get("content") or "").strip()
        if not text:
            text = str(data.get("response") or "").strip()

        note_path = ""
        if write_note and text:
            DEFAULT_NOTES_DIR.mkdir(parents=True, exist_ok=True)
            stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
            out = DEFAULT_NOTES_DIR / f"vision_{path.stem}_{stamp}.md"
            fm = [
                "---",
                *provenance_fields(
                    source="ollama_vision",
                    kind="vision_note",
                    tool="vision_describe",
                    limb="vision_local",
                    extra={"image": str(path), "model": model or DEFAULT_MODEL},
                ),
                "---",
            ]
            body = "\n".join(
                [
                    *fm,
                    f"# Vision: {path.name}",
                    "",
                    f"Prompt: {prompt}",
                    "",
                    text,
                    provenance_markdown_footer(
                        source="ollama_vision",
                        tool="vision_describe",
                        limb="vision_local",
                    ),
                ]
            )
            out.write_text(body, encoding="utf-8")
            note_path = str(out)

        return {
            "ok": True,
            "image": str(path),
            "model": model or DEFAULT_MODEL,
            "text": text,
            "path": note_path,
            "note": "Vision note is scratch — promote to Cognee only if useful.",
        }
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace") if exc.fp else str(exc)
        return {"ok": False, "error": f"HTTP {exc.code}: {detail}"}
    except URLError as exc:
        return {"ok": False, "error": f"Ollama unreachable: {exc.reason}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}
    finally:
        gpu_lease.release(expected="vision")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE local vision (qwen3-vl)")
    parser.add_argument("image")
    parser.add_argument("--prompt", default="Describe this image for the Architect. Be concrete.")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args(argv)
    result = describe_image(
        args.image,
        prompt=args.prompt,
        model=args.model,
        write_note=not args.no_write,
    )
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
