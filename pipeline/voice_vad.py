"""Voice activity detection gate for EMPIRE STT.

Prefers Silero VAD when torch+hub available; else energy heuristic.
Does not replace the speech API — only decides if audio looks like speech.
"""

from __future__ import annotations

import argparse
import json
import wave
from pathlib import Path
from typing import Any


def _energy_vad(path: Path, *, threshold: float = 0.01) -> dict[str, Any]:
    try:
        with wave.open(str(path), "rb") as wf:
            frames = wf.readframes(wf.getnframes())
            width = wf.getsampwidth()
            rate = wf.getframerate()
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "backend": "energy"}

    if width == 1:
        # unsigned 8-bit
        samples = [((b - 128) / 128.0) for b in frames]
    elif width == 2:
        import struct

        n = len(frames) // 2
        samples = [struct.unpack_from("<h", frames, i * 2)[0] / 32768.0 for i in range(n)]
    else:
        return {"ok": False, "error": f"unsupported sample width {width}", "backend": "energy"}

    if not samples:
        return {"ok": True, "speech": False, "backend": "energy", "rms": 0.0, "sample_rate": rate}

    mean_sq = sum(s * s for s in samples) / len(samples)
    rms = mean_sq**0.5
    return {
        "ok": True,
        "speech": rms >= threshold,
        "backend": "energy",
        "rms": round(rms, 6),
        "threshold": threshold,
        "sample_rate": rate,
        "note": "Heuristic energy VAD. Install torch+silero for Silero backend.",
    }


def _silero_vad(path: Path) -> dict[str, Any] | None:
    try:
        import torch  # type: ignore
    except ImportError:
        return None
    try:
        model, utils = torch.hub.load(  # type: ignore
            repo_or_dir="snakers4/silero-vad",
            model="silero_vad",
            trust_repo=True,
        )
        get_speech_timestamps, _, read_audio, *_rest = utils
        wav = read_audio(str(path))
        ts = get_speech_timestamps(wav, model, sampling_rate=16000)
        return {
            "ok": True,
            "speech": bool(ts),
            "backend": "silero",
            "segments": len(ts) if isinstance(ts, list) else 0,
            "note": "Silero VAD",
        }
    except Exception:
        return None


def detect(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    if not p.is_file():
        return {"ok": False, "error": f"not a file: {p}"}
    silero = _silero_vad(p)
    if silero is not None:
        return silero
    return _energy_vad(p)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE voice VAD")
    parser.add_argument("path")
    args = parser.parse_args(argv)
    result = detect(args.path)
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
