"""On-demand Weaviate Wikipedia scout → Truth Drift markdown cache.

Queries local WikiChunk collections (nearVector via Ollama nomic embeddings),
writes triage-friendly .md under Empire_Workbench/04_Thought_Experiments/wiki_cache,
and returns short summaries + paths for Eve / MCP. Never auto-promotes to Cognee.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

def _normalize_ollama_url(raw: str | None) -> str:
    """Client URL for embeddings. Ignore bind-all OLLAMA_HOST=0.0.0.0."""
    value = (raw or "").strip().rstrip("/")
    if not value or value in {"0.0.0.0", "http://0.0.0.0", "https://0.0.0.0"}:
        return "http://127.0.0.1:11434"
    if "://" not in value:
        value = f"http://{value}"
    # host was 0.0.0.0:port
    if "://0.0.0.0" in value:
        value = value.replace("://0.0.0.0", "://127.0.0.1", 1)
    return value


DEFAULT_WEAVIATE_URL = os.environ.get("WEAVIATE_URL", "http://127.0.0.1:8091").rstrip("/")
DEFAULT_API_KEY = os.environ.get(
    "WEAVIATE_API_KEY",
    "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih",
)
DEFAULT_OLLAMA_URL = _normalize_ollama_url(
    os.environ.get("EMPIRE_OLLAMA_URL") or os.environ.get("OLLAMA_HOST")
)
DEFAULT_EMBED_MODEL = os.environ.get("EMPIRE_WIKI_EMBED_MODEL", "nomic-embed-text")
DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_WIKI_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache",
    )
)
DEFAULT_BODY_MAX_CHARS = int(os.environ.get("EMPIRE_WIKI_BODY_MAX_CHARS", "6000"))
DEFAULT_SUMMARY_CHARS = int(os.environ.get("EMPIRE_WIKI_SUMMARY_CHARS", "280"))

YEAR_COLLECTIONS: dict[str, str] = {
    "2017": "WikiChunk",
    "2021": "WikiChunk2021",
    "2026": "WikiChunk2026",
}
COLLECTION_YEAR: dict[str, str] = {v: k for k, v in YEAR_COLLECTIONS.items()}
DEFAULT_COMPARE_YEARS = ("2017", "2021", "2026")

_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _safe_name(value: str, fallback: str = "chunk") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def _auth_headers(api_key: str) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def check_weaviate(base_url: str, api_key: str = "") -> tuple[bool, str]:
    try:
        response = httpx.get(
            f"{base_url.rstrip('/')}/v1/.well-known/ready",
            headers=_auth_headers(api_key),
            timeout=5.0,
        )
        if response.status_code < 300:
            return True, "ready"
        return False, f"HTTP {response.status_code}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def _pick_text(props: dict[str, Any]) -> str:
    for key in ("text", "content", "chunk", "body", "passage"):
        value = props.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return ""


def _pick_title(props: dict[str, Any], fallback: str) -> str:
    for key in ("title", "page_title", "article", "name"):
        value = props.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return fallback


def _truncate(text: str, max_chars: int) -> str:
    cleaned = (text or "").strip()
    if max_chars <= 0 or len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 1].rstrip() + "…"


def _yaml_quote(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.stem}_",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            if not content.endswith("\n"):
                handle.write("\n")
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def resolve_collection(
    year: str | int | None = None, collection: str | None = None
) -> tuple[str, str]:
    """Return (collection_name, snapshot_year_str)."""
    if collection:
        name = str(collection).strip()
        year_str = COLLECTION_YEAR.get(name, "")
        return name, year_str
    if year is None or str(year).strip() == "":
        return YEAR_COLLECTIONS["2021"], "2021"
    year_str = str(year).strip()
    if year_str not in YEAR_COLLECTIONS:
        raise ValueError(
            f"Unsupported year {year_str!r}. Use one of: {', '.join(YEAR_COLLECTIONS)}"
        )
    return YEAR_COLLECTIONS[year_str], year_str


def embed_query(
    query: str,
    *,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    model: str = DEFAULT_EMBED_MODEL,
) -> list[float]:
    payload = {"model": model, "prompt": query}
    with httpx.Client(timeout=60.0) as client:
        response = client.post(f"{ollama_url}/api/embeddings", json=payload)
        response.raise_for_status()
        data = response.json()
    vector = data.get("embedding")
    if not isinstance(vector, list) or not vector:
        raise RuntimeError(f"Ollama returned no embedding for model {model!r}")
    return [float(x) for x in vector]


def _graphql_hybrid_search(
    *,
    base_url: str,
    api_key: str,
    collection: str,
    query: str,
    vector: list[float],
    limit: int,
    alpha: float = 0.5,
) -> list[dict[str, Any]]:
    """Hybrid BM25 + vector. Pure nearVector returns empty on this Weaviate archive."""
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", collection):
        raise ValueError(f"Invalid collection name: {collection!r}")
    limit = max(1, min(int(limit), 20))
    alpha = max(0.0, min(float(alpha), 1.0))
    vector_literal = json.dumps(vector)
    query_literal = json.dumps(query)
    # WikiChunk schema is BYO/named vector "default" with properties title/text/...
    gql = f"""
    {{
      Get {{
        {collection}(
          hybrid: {{
            query: {query_literal}
            vector: {vector_literal}
            alpha: {alpha}
            targetVectors: ["default"]
          }}
          limit: {limit}
        ) {{
          title
          text
          doc_id
          chunk_id
          page_id
          snapshot_id
          chunk_index
          corpus_rel_path
          _additional {{ id distance score }}
        }}
      }}
    }}
    """
    with httpx.Client(
        base_url=base_url.rstrip("/"),
        timeout=60.0,
        headers=_auth_headers(api_key),
    ) as client:
        response = client.post("/v1/graphql", json={"query": gql})
        response.raise_for_status()
        payload = response.json()
    errors = payload.get("errors")
    if errors:
        raise RuntimeError(f"Weaviate GraphQL error: {errors}")
    rows = (((payload.get("data") or {}).get("Get") or {}).get(collection)) or []
    if not isinstance(rows, list):
        return []
    return rows


def _graphql_bm25_search(
    *,
    base_url: str,
    api_key: str,
    collection: str,
    query: str,
    limit: int,
) -> list[dict[str, Any]]:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", collection):
        raise ValueError(f"Invalid collection name: {collection!r}")
    limit = max(1, min(int(limit), 20))
    query_literal = json.dumps(query)
    gql = f"""
    {{
      Get {{
        {collection}(
          bm25: {{ query: {query_literal} }}
          limit: {limit}
        ) {{
          title
          text
          doc_id
          chunk_id
          page_id
          snapshot_id
          chunk_index
          corpus_rel_path
          _additional {{ id score }}
        }}
      }}
    }}
    """
    with httpx.Client(
        base_url=base_url.rstrip("/"),
        timeout=60.0,
        headers=_auth_headers(api_key),
    ) as client:
        response = client.post("/v1/graphql", json={"query": gql})
        response.raise_for_status()
        payload = response.json()
    errors = payload.get("errors")
    if errors:
        raise RuntimeError(f"Weaviate GraphQL error: {errors}")
    rows = (((payload.get("data") or {}).get("Get") or {}).get(collection)) or []
    if not isinstance(rows, list):
        return []
    return rows


def _normalize_hit(
    row: dict[str, Any], *, collection: str, year: str, query: str
) -> dict[str, Any]:
    additional = row.get("_additional") or {}
    obj_id = str(additional.get("id") or "")
    distance = additional.get("distance")
    score = additional.get("score")
    try:
        distance_f = float(distance) if distance is not None else None
    except (TypeError, ValueError):
        distance_f = None
    try:
        score_f = float(score) if score is not None else None
    except (TypeError, ValueError):
        score_f = None
    title = _pick_title(row, obj_id or "chunk")
    text = _pick_text(row)
    snapshot_id = str(row.get("snapshot_id") or "").strip()
    if not year and len(snapshot_id) >= 4 and snapshot_id[:4].isdigit():
        year = snapshot_id[:4]
    return {
        "collection": collection,
        "snapshot_year": year,
        "snapshot_id": snapshot_id,
        "title": title,
        "text": text,
        "doc_id": str(row.get("doc_id") or "").strip(),
        "chunk_id": str(row.get("chunk_id") or "").strip(),
        "page_id": str(row.get("page_id") or "").strip(),
        "object_id": obj_id,
        "distance": distance_f,
        "score": score_f,
        "query": query,
        "chunk_index": row.get("chunk_index"),
    }


def write_cache_hit(
    hit: dict[str, Any],
    *,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    body_max_chars: int = DEFAULT_BODY_MAX_CHARS,
) -> Path:
    year = str(hit.get("snapshot_year") or "unknown")
    title = str(hit.get("title") or "chunk")
    obj_id = str(hit.get("object_id") or "noid")
    stem = _safe_name(f"{title}_{year}_{obj_id[:8]}")
    path = cache_dir / f"{stem}.md"
    body = _truncate(str(hit.get("text") or ""), body_max_chars)
    distance = hit.get("distance")
    fm = [
        "---",
        "source: weaviate",
        "kind: wiki_chunk",
        f"collection: {hit.get('collection')}",
        f"snapshot_year: {_yaml_quote(year)}",
        f"snapshot_id: {_yaml_quote(hit.get('snapshot_id') or '')}",
        f"title: {_yaml_quote(title)}",
        f"doc_id: {_yaml_quote(hit.get('doc_id') or '')}",
        f"chunk_id: {_yaml_quote(hit.get('chunk_id') or '')}",
        f"query: {_yaml_quote(hit.get('query') or '')}",
        f"fetched_at: {_yaml_quote(_utc_now_iso())}",
    ]
    if distance is not None:
        fm.append(f"distance: {distance}")
    if hit.get("score") is not None:
        fm.append(f"score: {hit.get('score')}")
    if hit.get("page_id"):
        fm.append(f"page_id: {_yaml_quote(hit.get('page_id'))}")
    fm.append("---")
    content = "\n".join([*fm, f"# {title} ({year})", "", body])
    _atomic_write(path, content)
    return path


def write_compare_cache(
    query: str,
    hits_by_year: dict[str, list[dict[str, Any]]],
    *,
    cache_dir: Path = DEFAULT_CACHE_DIR,
    body_max_chars: int = DEFAULT_BODY_MAX_CHARS,
) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = _safe_name(f"compare_{query}_{stamp}")
    path = cache_dir / f"{stem}.md"
    years = [y for y in DEFAULT_COMPARE_YEARS if y in hits_by_year] or sorted(
        hits_by_year.keys()
    )
    fm = [
        "---",
        "source: weaviate",
        "kind: truth_drift_compare",
        f"query: {_yaml_quote(query)}",
        f"fetched_at: {_yaml_quote(_utc_now_iso())}",
        f"years: {json.dumps(years)}",
        "---",
    ]
    sections: list[str] = [f"# Truth Drift: {query}", ""]
    for year in years:
        sections.append(f"## {year}")
        sections.append("")
        year_hits = hits_by_year.get(year) or []
        if not year_hits:
            sections.append("_No hits._")
            sections.append("")
            continue
        for hit in year_hits:
            title = hit.get("title") or "chunk"
            distance = hit.get("distance")
            dist_note = f" (distance={distance})" if distance is not None else ""
            body = _truncate(str(hit.get("text") or ""), body_max_chars)
            sections.append(f"### {title}{dist_note}")
            sections.append("")
            sections.append(body)
            sections.append("")
    _atomic_write(path, "\n".join([*fm, *sections]))
    return path


def _summarize_hit(hit: dict[str, Any]) -> str:
    title = hit.get("title") or "chunk"
    year = hit.get("snapshot_year") or "?"
    snippet = _truncate(str(hit.get("text") or ""), DEFAULT_SUMMARY_CHARS)
    return f"{title} ({year}): {snippet}"


def search(
    query: str,
    *,
    year: str | int | None = None,
    collection: str | None = None,
    limit: int = 3,
    base_url: str = DEFAULT_WEAVIATE_URL,
    api_key: str = DEFAULT_API_KEY,
    cache_dir: Path | None = None,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    embed_model: str = DEFAULT_EMBED_MODEL,
    write_files: bool = True,
) -> dict[str, Any]:
    query = (query or "").strip()
    if not query:
        return {"ok": False, "error": "query is required", "paths": [], "titles": []}

    ready, detail = check_weaviate(base_url, api_key)
    if not ready:
        return {
            "ok": False,
            "error": (
                f"Weaviate not reachable at {base_url} ({detail}). "
                "Boot the temporary Docker container on port 8091 "
                "(see docs/WEAVIATE_HEIST.md / docs/WIKI_SCOUT.md)."
            ),
            "paths": [],
            "titles": [],
        }

    try:
        coll, year_str = resolve_collection(year=year, collection=collection)
    except ValueError as exc:
        return {"ok": False, "error": str(exc), "paths": [], "titles": []}

    try:
        vector = embed_query(query, ollama_url=ollama_url, model=embed_model)
        rows = _graphql_hybrid_search(
            base_url=base_url,
            api_key=api_key,
            collection=coll,
            query=query,
            vector=vector,
            limit=limit,
        )
    except Exception as embed_exc:  # noqa: BLE001
        try:
            rows = _graphql_bm25_search(
                base_url=base_url,
                api_key=api_key,
                collection=coll,
                query=query,
                limit=limit,
            )
        except Exception as bm25_exc:  # noqa: BLE001
            return {
                "ok": False,
                "error": f"hybrid/embed failed ({embed_exc}); bm25 failed ({bm25_exc})",
                "paths": [],
                "titles": [],
            }

    hits = [
        _normalize_hit(row, collection=coll, year=year_str, query=query) for row in rows
    ]
    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    paths: list[str] = []
    titles: list[str] = []
    summaries: list[str] = []
    for hit in hits:
        titles.append(str(hit.get("title") or ""))
        summaries.append(_summarize_hit(hit))
        if write_files:
            path = write_cache_hit(hit, cache_dir=out_dir)
            paths.append(str(path))

    return {
        "ok": True,
        "query": query,
        "collection": coll,
        "snapshot_year": year_str,
        "count": len(hits),
        "paths": paths,
        "titles": titles,
        "summaries": summaries,
        "note": (
            f"Cached {len(paths)} hit(s) under {out_dir}. "
            "Promote to Cognee only after triage via cognee_remember."
            if write_files
            else f"Found {len(hits)} hit(s); cache write skipped."
        ),
    }


def compare_years(
    query: str,
    *,
    years: tuple[str, ...] | list[str] | None = None,
    limit_per_year: int = 2,
    base_url: str = DEFAULT_WEAVIATE_URL,
    api_key: str = DEFAULT_API_KEY,
    cache_dir: Path | None = None,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    embed_model: str = DEFAULT_EMBED_MODEL,
    write_files: bool = True,
) -> dict[str, Any]:
    query = (query or "").strip()
    if not query:
        return {"ok": False, "error": "query is required", "path": "", "years_found": []}

    ready, detail = check_weaviate(base_url, api_key)
    if not ready:
        return {
            "ok": False,
            "error": (
                f"Weaviate not reachable at {base_url} ({detail}). "
                "Boot the temporary Docker container on port 8091 "
                "(see docs/WEAVIATE_HEIST.md / docs/WIKI_SCOUT.md)."
            ),
            "path": "",
            "years_found": [],
        }

    year_list = [
        str(y).strip() for y in (years or DEFAULT_COMPARE_YEARS) if str(y).strip()
    ]
    if not year_list:
        year_list = list(DEFAULT_COMPARE_YEARS)

    try:
        vector = embed_query(query, ollama_url=ollama_url, model=embed_model)
        use_hybrid = True
    except Exception as embed_exc:  # noqa: BLE001
        vector = []
        use_hybrid = False
        embed_error = str(embed_exc)
    else:
        embed_error = ""

    hits_by_year: dict[str, list[dict[str, Any]]] = {}
    years_found: list[str] = []
    errors: list[str] = []
    if embed_error:
        errors.append(f"embed: {embed_error} (falling back to bm25)")
    for year in year_list:
        try:
            coll, year_str = resolve_collection(year=year)
            if use_hybrid:
                rows = _graphql_hybrid_search(
                    base_url=base_url,
                    api_key=api_key,
                    collection=coll,
                    query=query,
                    vector=vector,
                    limit=limit_per_year,
                )
            else:
                rows = _graphql_bm25_search(
                    base_url=base_url,
                    api_key=api_key,
                    collection=coll,
                    query=query,
                    limit=limit_per_year,
                )
            hits = [
                _normalize_hit(row, collection=coll, year=year_str, query=query)
                for row in rows
            ]
            hits_by_year[year_str] = hits
            if hits:
                years_found.append(year_str)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{year}: {exc}")
            hits_by_year[str(year)] = []

    if not any(hits_by_year.values()) and errors:
        return {
            "ok": False,
            "error": "; ".join(errors),
            "path": "",
            "years_found": [],
        }

    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    path_str = ""
    if write_files:
        path = write_compare_cache(query, hits_by_year, cache_dir=out_dir)
        path_str = str(path)

    summaries: list[str] = []
    for year in year_list:
        for hit in hits_by_year.get(str(year), []):
            summaries.append(_summarize_hit(hit))

    note_bits = [
        f"Truth Drift compare for {len(years_found)} year(s) with hits.",
        "Promote to Cognee only after triage via cognee_remember.",
    ]
    if path_str:
        note_bits.insert(0, f"Wrote {path_str}.")
    if errors:
        note_bits.append("Partial errors: " + "; ".join(errors))

    return {
        "ok": True,
        "query": query,
        "path": path_str,
        "years_found": years_found,
        "summaries": summaries[:12],
        "note": " ".join(note_bits),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Weaviate Wikipedia scout → wiki_cache markdown"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    search_p = sub.add_parser("search", help="nearVector search one snapshot year")
    search_p.add_argument("query")
    search_p.add_argument("--year", default="2021")
    search_p.add_argument("--limit", type=int, default=3)
    search_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    search_p.add_argument("--api-key", default=DEFAULT_API_KEY)
    search_p.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    search_p.add_argument("--no-write", action="store_true")

    compare_p = sub.add_parser("compare", help="Truth Drift compare across years")
    compare_p.add_argument("query")
    compare_p.add_argument("--years", default="2017,2021,2026")
    compare_p.add_argument("--limit-per-year", type=int, default=2)
    compare_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    compare_p.add_argument("--api-key", default=DEFAULT_API_KEY)
    compare_p.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    compare_p.add_argument("--no-write", action="store_true")

    ready_p = sub.add_parser("ready", help="Check Weaviate readiness")
    ready_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    ready_p.add_argument("--api-key", default=DEFAULT_API_KEY)

    args = parser.parse_args(argv)

    if args.command == "ready":
        ok, detail = check_weaviate(args.url, args.api_key)
        print(json.dumps({"ok": ok, "detail": detail, "url": args.url}, indent=2))
        return 0 if ok else 1

    if args.command == "search":
        result = search(
            args.query,
            year=args.year,
            limit=args.limit,
            base_url=args.url,
            api_key=args.api_key,
            cache_dir=Path(args.cache_dir),
            write_files=not args.no_write,
        )
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1

    if args.command == "compare":
        years = tuple(y.strip() for y in str(args.years).split(",") if y.strip())
        result = compare_years(
            args.query,
            years=years,
            limit_per_year=args.limit_per_year,
            base_url=args.url,
            api_key=args.api_key,
            cache_dir=Path(args.cache_dir),
            write_files=not args.no_write,
        )
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1

    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
