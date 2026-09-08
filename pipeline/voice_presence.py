"""Local OpenAI-compatible STT/TTS client (Speaches / Voicebox / vocal-ai).

Default base: http://127.0.0.1:8000 — start via scripts/start-voice.ps1.
Prefer CPU Piper TTS + small Whisper so chat VRAM stays free.
"""

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
from pipeline import voice_vad

DEFAULT_BASE = os.environ.get("EMPIRE_VOICE_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
DEFAULT_STT_MODEL = os.environ.get("EMPIRE_VOICE_STT_MODEL", "Systran/faster-whisper-base")
DEFAULT_TTS_VOICE = os.environ.get("EMPIRE_VOICE_TTS_VOICE", "af_heart")
DEFAULT_TTS_MODEL = os.environ.get("EMPIRE_VOICE_TTS_MODEL", "kokoro")


def _normalize_base(raw: str | None) -> str:
    value = (raw or DEFAULT_BASE).strip().rstrip("/")
    if not value:
        return DEFAULT_BASE
    if "://" not in value:
        value = f"http://{value}"
    if "://0.0.0.0" in value:
        value = value.replace("://0.0.0.0", "://127.0.0.1", 1)
    return value


def health(base_url: str | None = None) -> dict[str, Any]:
    base = _normalize_base(base_url)
    for path in ("/health", "/v1/models", "/"):
        try:
            with urlopen(Request(f"{base}{path}"), timeout=3) as resp:
                return {
                    "ok": resp.status < 500,
                    "base_url": base,
                    "probe": path,
                    "status": resp.status,
                }
        except Exception:
            continue
    return {
        "ok": False,
        "base_url": base,
        "error": "Speech API not reachable. Start Speaches/Voicebox (see docs/VOICE_PRESENCE.md).",
    }


def transcribe(
    audio_path: str | Path,
    *,
    base_url: str | None = None,
    model: str | None = None,
    lease: bool = True,
) -> dict[str, Any]:
    path = Path(audio_path)
    if not path.is_file():
        return {"ok": False, "error": f"not a file: {path}"}

    vad = voice_vad.detect(path)
    if vad.get("ok") and vad.get("speech") is False:
        return {
            "ok": True,
            "skipped": True,
            "text": "",
            "vad": vad,
            "note": "VAD detected no speech — STT skipped.",
        }

    if lease:
        acquired = gpu_lease.acquire("voice", holder="voice_transcribe", note="STT")
        if not acquired.get("ok"):
            # STT can run on CPU — warn but continue
            pass

    base = _normalize_base(base_url)
    stt_model = model or DEFAULT_STT_MODEL
    boundary = "----empirevoiceboundary"
    file_bytes = path.read_bytes()
    filename = path.name
    parts = [
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: application/octet-stream\r\n\r\n".encode("utf-8")
        + file_bytes
        + b"\r\n",
        (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="model"\r\n\r\n'
            f"{stt_model}\r\n"
        ).encode("utf-8"),
        f"--{boundary}--\r\n".encode("utf-8"),
    ]
    body = b"".join(parts)
    req = Request(
        f"{base}/v1/audio/transcriptions",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
        payload = json.loads(raw) if raw.strip().startswith("{") else {"text": raw}
        text = str(payload.get("text") or "").strip()
        return {"ok": True, "text": text, "raw": payload, "base_url": base}
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace") if exc.fp else str(exc)
        return {"ok": False, "error": f"HTTP {exc.code}: {detail}", "base_url": base}
    except URLError as exc:
        return {
            "ok": False,
            "error": f"Speech API unreachable: {exc.reason}",
            "base_url": base,
            "hint": "docs/VOICE_PRESENCE.md",
        }
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "base_url": base}
    finally:
        if lease:
            gpu_lease.release(expected="voice")


def speak(
    text: str,
    *,
    out_path: str | Path | None = None,
    base_url: str | None = None,
    voice: str | None = None,
    model: str | None = None,
    lease: bool = True,
) -> dict[str, Any]:
    cleaned = (text or "").strip()
    if not cleaned:
        return {"ok": False, "error": "text required"}

    if lease:
        gpu_lease.acquire("voice", holder="voice_speak", note="TTS (prefer CPU)")

    base = _normalize_base(base_url)
    payload = {
        "model": model or DEFAULT_TTS_MODEL,
        "input": cleaned,
        "voice": voice or DEFAULT_TTS_VOICE,
    }
    req = Request(
        f"{base}/v1/audio/speech",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=120) as resp:
            audio = resp.read()
        dest = Path(out_path) if out_path else Path(
            os.environ.get("TEMP", ".")
        ) / "empire-voice-out.mp3"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(audio)
        b64 = base64.b64encode(audio).decode("ascii")
        return {
            "ok": True,
            "path": str(dest),
            "bytes": len(audio),
            "audio_base64": b64[:80] + "…" if len(b64) > 80 else b64,
            "audio_base64_full": b64,
            "base_url": base,
        }
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace") if exc.fp else str(exc)
        return {"ok": False, "error": f"HTTP {exc.code}: {detail}", "base_url": base}
    except URLError as exc:
        return {
            "ok": False,
            "error": f"Speech API unreachable: {exc.reason}",
            "base_url": base,
            "hint": "docs/VOICE_PRESENCE.md",
        }
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "base_url": base}
    finally:
        if lease:
            gpu_lease.release(expected="voice")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE voice presence client")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("health")
    t = sub.add_parser("transcribe")
    t.add_argument("audio")
    s = sub.add_parser("speak")
    s.add_argument("text")
    s.add_argument("-o", "--output", default="")
    args = parser.parse_args(argv)

    if args.command == "health":
        result = health()
    elif args.command == "transcribe":
        result = transcribe(args.audio)
    else:
        result = speak(args.text, out_path=args.output or None)
        # Don't dump huge base64 in CLI
        if isinstance(result, dict):
            result = {k: v for k, v in result.items() if k != "audio_base64_full"}
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
