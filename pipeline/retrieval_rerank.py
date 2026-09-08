"""Offline retrieval rerank A/B — eval only. Never swaps production Cognee embeds (nomic).

Default scorer: lexical token overlap (always available).
Optional: sentence-transformers CrossEncoder when EMPIRE_RERANK_MODEL is installed.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from pipeline.artifact_lineage import lineage_envelope, sha256_text
from pipeline.provenance import utc_now_iso

EMPIRE_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = EMPIRE_ROOT / "data" / "eval" / "retrieval"
ACCEPTANCE_DIR = EMPIRE_ROOT / "data" / "eval" / "acceptance"
DEFAULT_CACHE = Path(
    os.environ.get(
        "EMPIRE_RERANK_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\rerank_cache",
    )
)
_TOKEN = re.compile(r"[a-z0-9]+", re.I)


def _tokens(text: str) -> set[str]:
    return {t.lower() for t in _TOKEN.findall(text or "") if len(t) > 1}


def lexical_score(query: str, document: str) -> float:
    q = _tokens(query)
    d = _tokens(document)
    if not q or not d:
        return 0.0
    inter = len(q & d)
    return inter / math.sqrt(len(q) * len(d))


def cross_encoder_scores(query: str, documents: list[str]) -> list[float] | None:
    model_id = os.environ.get("EMPIRE_RERANK_MODEL", "").strip()
    if not model_id:
        return None
    try:
        from sentence_transformers import CrossEncoder  # type: ignore
    except ImportError:
        return None
    try:
        model = CrossEncoder(model_id)
        pairs = [(query, doc) for doc in documents]
        scores = model.predict(pairs)
        return [float(s) for s in scores]
    except Exception:
        return None


def rerank(
    query: str,
    candidates: list[dict[str, Any]],
    *,
    top_k: int = 5,
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "query required"}
    docs = []
    for row in candidates:
        if isinstance(row, dict):
            docs.append(
                {
                    "id": str(row.get("id") or ""),
                    "text": str(row.get("text") or row.get("body") or ""),
                }
            )
        elif isinstance(row, str):
            docs.append({"id": "", "text": row})
    if not docs:
        return {"ok": False, "error": "candidates required"}

    texts = [d["text"] for d in docs]
    ce = cross_encoder_scores(cleaned, texts)
    backend = "cross_encoder" if ce is not None else "lexical"
    scored = []
    for i, d in enumerate(docs):
        score = float(ce[i]) if ce is not None else lexical_score(cleaned, d["text"])
        scored.append({**d, "score": round(score, 6)})
    scored.sort(key=lambda r: r["score"], reverse=True)
    top = scored[: max(1, min(int(top_k or 5), 50))]
    envelope = lineage_envelope(
        schema_id="RetrievalRerank.v1",
        tool="retrieval_rerank",
        limb="retrieval_rerank",
        model_id=os.environ.get("EMPIRE_RERANK_MODEL") or "lexical.v1",
        input_hash=sha256_text(cleaned + json.dumps(texts)),
        validation_ok=True,
        extra={"backend": backend, "candidate_count": len(docs)},
    )
    return {
        "ok": True,
        "backend": backend,
        "query": cleaned,
        "results": top,
        "lineage": envelope,
        "note": "Eval/scratch only. Production Cognee embeddings remain nomic-embed-text.",
    }


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp = tempfile.mkstemp(prefix="rerank-", suffix=".json", dir=str(path.parent))
    tmp_path = Path(tmp)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def run_eval() -> dict[str, Any]:
    cases_path = FIXTURE_DIR / "cases.json"
    try:
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": str(exc)}
    if not isinstance(cases, list):
        return {"ok": False, "error": "cases.json must be a list"}

    rows = []
    for case in cases:
        if not isinstance(case, dict):
            continue
        out = rerank(
            str(case.get("query") or ""),
            list(case.get("candidates") or []),
            top_k=int(case.get("top_k") or 5),
        )
        expected_ids = [str(x) for x in (case.get("expected_top_ids") or [])]
        got_ids = [str(r.get("id") or "") for r in (out.get("results") or [])]
        hit = bool(expected_ids) and any(e in got_ids[: max(1, len(expected_ids))] for e in expected_ids)
        rows.append(
            {
                "id": case.get("id"),
                "ok": out.get("ok"),
                "backend": out.get("backend"),
                "hit": hit,
                "got_ids": got_ids,
                "expected_top_ids": expected_ids,
            }
        )

    ACCEPTANCE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    path = ACCEPTANCE_DIR / f"retrieval_rerank_{stamp}.yaml"
    hits = sum(1 for r in rows if r.get("hit"))
    lines = [
        "candidate: retrieval_rerank",
        "status: pending_architect",
        f'evaluated_at: "{utc_now_iso()}"',
        f"case_count: {len(rows)}",
        f"hit_count: {hits}",
        "memory_promoted: false",
        "production_embed_unchanged: true",
        "production_embed: nomic-embed-text",
        'notes: "Eval only. Optional CrossEncoder via EMPIRE_RERANK_MODEL."',
        "results:",
    ]
    for r in rows:
        lines.append(f"  - id: {r.get('id')}")
        lines.append(f"    hit: {str(bool(r.get('hit'))).lower()}")
        lines.append(f"    backend: {r.get('backend')}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"ok": True, "hits": hits, "cases": len(rows), "acceptance_path": str(path), "rows": rows}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE retrieval rerank eval")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("rerank")
    p.add_argument("--query", required=True)
    p.add_argument("--candidates-json", required=True, help="JSON list of {id,text}")
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--write", action="store_true")
    sub.add_parser("eval")
    args = parser.parse_args(argv)

    if args.cmd == "eval":
        result = run_eval()
    else:
        try:
            cands = json.loads(args.candidates_json)
        except json.JSONDecodeError as exc:
            result = {"ok": False, "error": str(exc)}
            print(json.dumps(result, indent=2))
            return 1
        result = rerank(args.query, cands if isinstance(cands, list) else [], top_k=args.top_k)
        if args.write and result.get("ok"):
            out = DEFAULT_CACHE / f"rerank_{utc_now_iso().replace(':', '')}.json"
            _atomic_write(out, json.dumps(result, indent=2, default=str))
            result["path"] = str(out)
    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
