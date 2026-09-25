"""Measure what belongs in VRAM versus system RAM, on this machine, with numbers.

The question this answers (Architect, 2026-09-24): *"this laptop is powerful — use it to its
capability. How much can be offloaded to RAM so the VRAM is maximized for what needs it?"*

Measured reality on this machine (RTX 5080 Laptop 16 GB, Ultra 9 275HX, 63 GB RAM): the GPU is
~4x faster at generating, and on a *long* prompt only ~1.4x faster at prefilling when half the model
is offloaded — so the number that decides placement is "how long before she says the first word".
This probe reports that per placement, projects it onto Eve's real prompt floor, and writes
`eve-audit/placement.json` as evidence.

    .\\venv\\Scripts\\python.exe scripts\\measure-placement.py                  # cpu / half / all
    .\\venv\\Scripts\\python.exe scripts\\measure-placement.py --num-gpu 0,16,999
    .\\venv\\Scripts\\python.exe scripts\\measure-placement.py --prompt short

Placement is only settable on Ollama's **native** endpoint: the OpenAI-compat endpoint ignores
per-request `options` (E-02), which is why this posts to `/api/chat`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OLLAMA = "http://127.0.0.1:11434"
DEFAULT_MODEL = "empire-fast:14b"
LONG_UNIT = (
    "The White Stripes released six studio albums between 1999 and 2007, and the local archive "
    "holds each page as markdown with a lead section. "
)
SHORT_PROMPT = "List three ways a local wiki archive beats a web search for facts. One line each."


def _post(path: str, body: dict[str, Any], timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        OLLAMA + path,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _get(path: str, timeout: float = 10) -> dict[str, Any]:
    with urllib.request.urlopen(OLLAMA + path, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def resident(model: str = "") -> dict[str, Any]:
    """What Ollama currently holds for `model`: size, VRAM share, context — the `ollama ps` truth.

    Picks by name because the embedder is pinned warm (`keep_alive=-1`), so `models[0]` is not
    necessarily the chat model — attributing nomic's few hundred MB to the 14B would corrupt the
    VRAM numbers this probe exists to report.
    """

    try:
        models = _get("/api/ps").get("models") or []
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
        return {}
    if not models:
        return {}
    entry = models[0]
    if model:
        wanted = model.split(":")[0]
        for candidate in models:
            name = str(candidate.get("name") or candidate.get("model") or "")
            if name.startswith(wanted):
                entry = candidate
                break
    size = float(entry.get("size") or 0)
    vram = float(entry.get("size_vram") or 0)
    return {
        "name": entry.get("name") or entry.get("model"),
        "size_gb": round(size / 1e9, 1),
        "vram_gb": round(vram / 1e9, 1),
        "gpu_percent": round(100 * vram / size) if size else 0,
        "context": entry.get("context_length"),
    }


def _powershell(command: str) -> str:
    """Best-effort hardware line — a missing label must never stop the measurement."""

    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def machine() -> dict[str, str]:
    return {
        "cpu": _powershell(
            "(Get-CimInstance Win32_Processor).Name + ' cores=' "
            "+ (Get-CimInstance Win32_Processor).NumberOfLogicalProcessors"
        ),
        "ram": _powershell(
            "'{0:N1} GB total / {1:N1} GB free' -f "
            "((Get-CimInstance Win32_OperatingSystem).TotalVisibleMemorySize/1MB), "
            "((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1MB)"
        ),
        "gpu": _powershell(
            "nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv,noheader"
        ),
    }


def prompt_floor_tokens() -> int:
    """Eve's always-on floor, from the same source the prompt-budget tests use."""

    try:
        from pipeline import prompt_budget

        return int(prompt_budget.measure()["floor_tokens"])
    except Exception:  # noqa: BLE001 - a missing floor must not stop the measurement
        return 0


def block_count(model: str) -> int:
    """Transformer layers, so \"half offload\" means half the model rather than a guessed 24."""

    try:
        info = _post("/api/show", {"name": model}, 60).get("model_info") or {}
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
        return 0
    for key, value in info.items():
        if key.endswith(".block_count") and isinstance(value, int):
            return value
    return 0


def measure(
    model: str,
    num_gpu: int,
    prompt: str,
    *,
    num_predict: int,
    num_ctx: int = 0,
    timeout: float = 900,
) -> dict[str, Any]:
    """One placement: latency, rates, and what Ollama ended up holding."""

    options: dict[str, Any] = {"num_predict": num_predict, "num_gpu": num_gpu}
    if num_ctx:
        options["num_ctx"] = num_ctx
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": options,
    }
    started = time.perf_counter()
    try:
        payload = _post("/api/chat", body, timeout)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"num_gpu": num_gpu, "error": str(exc)}
    wall = time.perf_counter() - started

    gen_s = float(payload.get("eval_duration") or 0) / 1e9
    pre_s = float(payload.get("prompt_eval_duration") or 0) / 1e9
    gen_tokens = float(payload.get("eval_count") or 0)
    pre_tokens = float(payload.get("prompt_eval_count") or 0)
    return {
        "num_gpu": num_gpu,
        "num_ctx": num_ctx or None,
        "prefill_tokens": int(pre_tokens),
        "prefill_tok_s": round(pre_tokens / pre_s, 1) if pre_s else None,
        "gen_tok_s": round(gen_tokens / gen_s, 1) if gen_s else None,
        "load_s": round(float(payload.get("load_duration") or 0) / 1e9, 1),
        "wall_s": round(wall, 1),
        "resident": resident(model),
        "answer_head": str((payload.get("message") or {}).get("content") or "")[:120],
    }


def _label(num_gpu: int, layers: int) -> str:
    if num_gpu <= 0:
        return "100% CPU"
    if layers and num_gpu >= layers:
        return "100% GPU"
    if layers:
        return f"~{round(100 * num_gpu / layers)}% GPU"
    return f"num_gpu={num_gpu}"


def _print_table(rows: list[dict[str, Any]], floor: int) -> None:
    header = f"{'placement':<12} {'vram':>7} {'size':>7} {'prefill':>9} {'gen':>8} {'floor':>8}"
    print(header)
    for row in rows:
        if row.get("error"):
            print(f"{row.get('label', '?'):<12} ERROR {row['error'][:60]}")
            continue
        held = row.get("resident") or {}
        floor_s = (
            f"{floor / row['prefill_tok_s']:.1f}s" if row.get("prefill_tok_s") and floor else "?"
        )
        print(
            f"{row.get('label', '?'):<12} {held.get('vram_gb', '?'):>6}G {held.get('size_gb', '?'):>6}G "
            f"{str(row.get('prefill_tok_s')):>8} {str(row.get('gen_tok_s')):>7} {floor_s:>8}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure VRAM/RAM placement for a local model")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--num-gpu", default="", help="Comma list of GPU layer counts (default: 0, half, all)")
    parser.add_argument("--prompt", choices=["long", "short"], default="long")
    parser.add_argument("--num-predict", type=int, default=24)
    parser.add_argument("--num-ctx", type=int, default=0, help="Override context (native endpoint only)")
    parser.add_argument("--out", type=Path, default=ROOT / "eve-audit" / "placement.json")
    args = parser.parse_args()

    layers = block_count(args.model)
    half = max(1, layers // 2) if layers else 24
    wanted = (
        [int(part) for part in args.num_gpu.split(",") if part.strip()]
        if args.num_gpu
        else [0, half, 999]
    )
    prompt = LONG_UNIT * 30 if args.prompt == "long" else SHORT_PROMPT
    floor = prompt_floor_tokens()
    info = machine()

    print(f"machine: {info}")
    print(
        f"model: {args.model}  layers={layers or '?'}  floor={floor} tokens  "
        f"ctx={args.num_ctx or 'model default'}"
    )
    rows: list[dict[str, Any]] = []
    for num_gpu in wanted:
        row = measure(args.model, num_gpu, prompt, num_predict=args.num_predict, num_ctx=args.num_ctx)
        row["layers"] = layers
        row["label"] = _label(num_gpu, layers)
        rows.append(row)
        held = row.get("resident") or {}
        print(
            f"  {row['label']:<12} prefill={row.get('prefill_tok_s')} tok/s  "
            f"gen={row.get('gen_tok_s')} tok/s  vram={held.get('vram_gb', '?')} GB  "
            f"load={row.get('load_s')}s"
        )

    print()
    _print_table(rows, floor)
    payload = {
        "model": args.model,
        "layers": layers,
        "floor_tokens": floor,
        "prompt_tokens": rows[0].get("prefill_tokens") if rows else None,
        "machine": info,
        "rows": rows,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"\nevidence: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
