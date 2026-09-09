"""Embedding A/B eval — nomic (production) vs qwen3-embedding trial.

Never re-embeds production Cognee datasets. Uses Ollama /api/embed locally.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Any

import httpx

from pipeline.provenance import utc_now_iso

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = EMPIRE_ROOT / "config" / "embedding-ab.json"
FIXTURE_DIR = EMPIRE_ROOT / "data" / "eval" / "embedding_ab"
ACCEPTANCE_DIR = EMPIRE_ROOT / "data" / "eval" / "acceptance"
REPORT_DIR = EMPIRE_ROOT / "data" / "eval" / "embedding_ab"

DEFAULT_OLLAMA = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
PRODUCTION_MODEL = "nomic-embed-text"
CANDIDATE_MODEL = "qwen3-embedding:0.6b"


def _load_config() -> dict[str, Any]:
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def production_model() -> str:
    cfg = _load_config()
    return str(cfg.get("production_model") or PRODUCTION_MODEL).strip() or PRODUCTION_MODEL


def candidate_model() -> str:
    cfg = _load_config()
    return str(cfg.get("candidate_model") or CANDIDATE_MODEL).strip() or CANDIDATE_MODEL


def ollama_base() -> str:
    return os.environ.get("EMPIRE_OLLAMA_URL", DEFAULT_OLLAMA).rstrip("/")


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def embed_text(text: str, *, model: str, base_url: str | None = None) -> list[float]:
    cleaned = (text or "").strip()
    if not cleaned:
        raise ValueError("empty text for embed")
    base = (base_url or ollama_base()).rstrip("/")
    errors: list[str] = []
    with httpx.Client(timeout=120.0) as client:
        try:
            response = client.post(
                f"{base}/api/embed",
                json={"model": model, "input": cleaned},
            )
            if response.status_code == 200:
                data = response.json()
                embeddings = data.get("embeddings")
                if isinstance(embeddings, list) and embeddings:
                    vec = embeddings[0]
                    if isinstance(vec, list) and vec:
                        return [float(x) for x in vec]
                embedding = data.get("embedding")
                if isinstance(embedding, list) and embedding:
                    return [float(x) for x in embedding]
            errors.append(f"/api/embed HTTP {response.status_code}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"/api/embed {exc}")

        try:
            response = client.post(
                f"{base}/api/embeddings",
                json={"model": model, "prompt": cleaned},
            )
            response.raise_for_status()
            data = response.json()
            vector = data.get("embedding")
            if isinstance(vector, list) and vector:
                return [float(x) for x in vector]
            errors.append("/api/embeddings returned no vector")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"/api/embeddings {exc}")

    raise RuntimeError("; ".join(errors) or f"embed failed for {model!r}")


def model_available(model: str, *, base_url: str | None = None) -> tuple[bool, str]:
    base = (base_url or ollama_base()).rstrip("/")
    try:
        with httpx.Client(timeout=20.0) as client:
            response = client.get(f"{base}/api/tags")
            response.raise_for_status()
            data = response.json()
    except Exception as exc:  # noqa: BLE001
        return False, f"Ollama unreachable at {base}: {exc}"
    names: set[str] = set()
    for row in data.get("models") or []:
        if isinstance(row, dict):
            name = str(row.get("name") or "").strip()
            if name:
                names.add(name)
                if ":" in name:
                    names.add(name.split(":")[0])
    target = model.strip()
    if target in names:
        return True, "ok"
    prefix = target.split(":")[0]
    if any(n == target or n.startswith(prefix + ":") for n in names):
        return True, "ok"
    return False, f"model {target!r} not in ollama list"


def rank_candidates(
    query: str,
    candidates: list[dict[str, Any]],
    *,
    model: str,
    top_k: int = 5,
    base_url: str | None = None,
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "query required"}
    docs: list[dict[str, str]] = []
    for row in candidates:
        if not isinstance(row, dict):
            continue
        docs.append(
            {
                "id": str(row.get("id") or ""),
                "text": str(row.get("text") or row.get("body") or ""),
            }
        )
    if not docs:
        return {"ok": False, "error": "candidates required"}

    try:
        query_vec = embed_text(cleaned, model=model, base_url=base_url)
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "model": model}

    scored: list[dict[str, Any]] = []
    for doc in docs:
        try:
            doc_vec = embed_text(doc["text"], model=model, base_url=base_url)
            score = cosine_similarity(query_vec, doc_vec)
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "error": str(exc), "model": model, "doc_id": doc["id"]}
        scored.append({**doc, "score": round(score, 6)})

    scored.sort(key=lambda row: row["score"], reverse=True)
    top = scored[: max(1, min(int(top_k or 5), 50))]
    return {
        "ok": True,
        "model": model,
        "query": cleaned,
        "dimension": len(query_vec),
        "results": top,
    }


def _case_hit(expected_ids: list[str], got_ids: list[str], top_k: int) -> bool:
    if not expected_ids:
        return False
    window = got_ids[: max(1, top_k)]
    return any(item in window for item in expected_ids)


def run_eval(
    *,
    fixture_path: Path | None = None,
    models: list[str] | None = None,
    base_url: str | None = None,
) -> dict[str, Any]:
    path = fixture_path or (FIXTURE_DIR / "cases.json")
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": str(exc)}

    if not isinstance(cases, list):
        return {"ok": False, "error": "cases.json must be a list"}

    model_list = models or [production_model(), candidate_model()]
    availability: dict[str, Any] = {}
    for model in model_list:
        ok, detail = model_available(model, base_url=base_url)
        availability[model] = {"available": ok, "detail": detail}

    per_model: dict[str, Any] = {}
    for model in model_list:
        if not availability.get(model, {}).get("available"):
            per_model[model] = {
                "ok": False,
                "error": availability[model]["detail"],
                "hits": 0,
                "cases": [],
            }
            continue
        rows: list[dict[str, Any]] = []
        hits = 0
        for case in cases:
            if not isinstance(case, dict):
                continue
            top_k = int(case.get("top_k") or 3)
            out = rank_candidates(
                str(case.get("query") or ""),
                list(case.get("candidates") or []),
                model=model,
                top_k=top_k,
                base_url=base_url,
            )
            expected = [str(x) for x in (case.get("expected_top_ids") or [])]
            got = [str(r.get("id") or "") for r in (out.get("results") or [])]
            hit = out.get("ok") and _case_hit(expected, got, top_k)
            if hit:
                hits += 1
            rows.append(
                {
                    "id": case.get("id"),
                    "ok": out.get("ok"),
                    "hit": hit,
                    "expected_top_ids": expected,
                    "got_ids": got,
                    "dimension": out.get("dimension"),
                    "error": out.get("error"),
                }
            )
        per_model[model] = {
            "ok": True,
            "hits": hits,
            "case_count": len(rows),
            "cases": rows,
        }

    prod = production_model()
    cand = candidate_model()
    prod_hits = int((per_model.get(prod) or {}).get("hits") or 0)
    cand_hits = int((per_model.get(cand) or {}).get("hits") or 0)
    if cand_hits > prod_hits:
        verdict = "candidate_ahead"
        recommendation = (
            f"{cand} beat {prod} on fixture hits ({cand_hits}>{prod_hits}). "
            "Architect may trial embed_ab_test ingest — do not re-embed eve_memory yet."
        )
    elif cand_hits == prod_hits:
        verdict = "tie"
        recommendation = (
            f"{cand} tied {prod} ({cand_hits} hits). No production embed change recommended yet."
        )
    else:
        verdict = "production_ahead"
        recommendation = (
            f"{prod} ahead of {cand} ({prod_hits}>{cand_hits}). Keep nomic-embed-text in cognee.env."
        )

    stamp = utc_now_iso().replace("+00:00", "Z").replace(":", "").replace("T", "_")
    ACCEPTANCE_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    acceptance_path = ACCEPTANCE_DIR / f"embedding_ab_{stamp}.yaml"
    report_path = REPORT_DIR / f"embedding_ab_{stamp}.json"

    yaml_lines = [
        "candidate: embedding_ab",
        "status: pending_architect",
        f'evaluated_at: "{utc_now_iso()}"',
        f"production_model: {prod}",
        f"candidate_model: {cand}",
        f"production_hits: {prod_hits}",
        f"candidate_hits: {cand_hits}",
        f"verdict: {verdict}",
        "memory_promoted: false",
        "production_embed_unchanged: true",
        f'notes: "{recommendation}"',
        "models:",
    ]
    for model, info in per_model.items():
        yaml_lines.append(f"  - model: {model}")
        yaml_lines.append(f"    available: {str(bool(availability.get(model, {}).get('available'))).lower()}")
        yaml_lines.append(f"    hits: {info.get('hits', 0)}")
    acceptance_path.write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")

    payload = {
        "ok": True,
        "evaluated_at": utc_now_iso(),
        "production_model": prod,
        "candidate_model": cand,
        "production_hits": prod_hits,
        "candidate_hits": cand_hits,
        "verdict": verdict,
        "recommendation": recommendation,
        "availability": availability,
        "models": per_model,
        "acceptance_path": str(acceptance_path),
        "report_path": str(report_path),
        "note": "Eval only. Production Cognee embeddings remain nomic-embed-text.",
    }
    report_path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE embedding A/B eval (Ollama)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("eval", help="Run fixture eval for production vs candidate embed models")

    rank_p = sub.add_parser("rank", help="Rank candidates for one query with one model")
    rank_p.add_argument("--query", required=True)
    rank_p.add_argument("--model", default=production_model())
    rank_p.add_argument("--candidates-json", required=True)
    rank_p.add_argument("--top-k", type=int, default=5)

    sub.add_parser("status", help="Show configured models and Ollama availability")

    args = parser.parse_args(argv)

    if args.cmd == "eval":
        result = run_eval()
    elif args.cmd == "status":
        prod = production_model()
        cand = candidate_model()
        ok_prod, detail_prod = model_available(prod)
        ok_cand, detail_cand = model_available(cand)
        result = {
            "ok": ok_prod,
            "production_model": prod,
            "production_available": ok_prod,
            "production_detail": detail_prod,
            "candidate_model": cand,
            "candidate_available": ok_cand,
            "candidate_detail": detail_cand,
            "config_path": str(CONFIG_PATH),
            "fixture_path": str(FIXTURE_DIR / "cases.json"),
        }
    else:
        try:
            cands = json.loads(args.candidates_json)
        except json.JSONDecodeError as exc:
            print(json.dumps({"ok": False, "error": str(exc)}, indent=2))
            return 1
        result = rank_candidates(
            args.query,
            cands if isinstance(cands, list) else [],
            model=args.model,
            top_k=args.top_k,
        )

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
