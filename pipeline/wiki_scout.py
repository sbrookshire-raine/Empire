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

from pipeline.wiki_interpreter import (
    WIKI_CHAT_REPLY_RULE,
    candidate_pool_size,
    cards_for_chat,
    cards_public,
    clean_query_for_retrieval,
    expand_queries,
    interpret_hits,
)


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
# Final cards after Wiki Interpreter (retrieve pool is wider — see wiki_interpreter).
DEFAULT_SEARCH_TOP_K = int(os.environ.get("EMPIRE_WIKI_SEARCH_TOP_K", "5"))
DEFAULT_COMPARE_TOP_K = int(os.environ.get("EMPIRE_WIKI_COMPARE_TOP_K", "4"))
DEFAULT_COMPARE_YEARS = ("2017", "2021", "2026")
ALLOWED_SNAPSHOT_YEARS = frozenset(DEFAULT_COMPARE_YEARS)


def default_snapshot_year() -> str:
    """Primary archive for everyday lookup (override: EMPIRE_WIKI_DEFAULT_YEAR)."""
    raw = os.environ.get("EMPIRE_WIKI_DEFAULT_YEAR", "2026").strip()
    return raw if raw in ALLOWED_SNAPSHOT_YEARS else "2026"


_YEAR_IN_TEXT_RE = re.compile(
    r"\b(?:in|from|using|on|with)\s+(2017|2021|2026)\b|"
    r"\b(2017|2021|2026)\s+(?:archive|snapshot|wikipedia|wiki)\b",
    re.IGNORECASE,
)


def parse_snapshot_year_from_text(text: str) -> str | None:
    """Optional explicit archive year in a user question (e.g. 'in 2017')."""
    match = _YEAR_IN_TEXT_RE.search((text or "").strip())
    if not match:
        return None
    for group in match.groups():
        if group and group in ALLOWED_SNAPSHOT_YEARS:
            return group
    return None


YEAR_COLLECTIONS: dict[str, str] = {
    "2017": "WikiChunk",
    "2021": "WikiChunk2021",
    "2026": "WikiChunk2026",
}
COLLECTION_YEAR: dict[str, str] = {v: k for k, v in YEAR_COLLECTIONS.items()}

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
        default_year = default_snapshot_year()
        return YEAR_COLLECTIONS[default_year], default_year
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
    limit = max(1, min(int(limit), 50))
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
    properties: list[str] | None = None,
) -> list[dict[str, Any]]:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", collection):
        raise ValueError(f"Invalid collection name: {collection!r}")
    limit = max(1, min(int(limit), 50))
    query_literal = json.dumps(query)
    props_clause = ""
    if properties:
        safe_props = [p for p in properties if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", p)]
        if safe_props:
            props_clause = ", properties: [" + ", ".join(f'"{p}"' for p in safe_props) + "]"
    gql = f"""
    {{
      Get {{
        {collection}(
          bm25: {{ query: {query_literal}{props_clause} }}
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


def _graphql_exact_title(
    *,
    base_url: str,
    api_key: str,
    collection: str,
    title: str,
    limit: int = 5,
) -> list[dict[str, Any]]:
    """Fetch chunks whose title Exactly equals the string (canonical page inject)."""
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", collection):
        raise ValueError(f"Invalid collection name: {collection!r}")
    title = (title or "").strip()
    if not title:
        return []
    limit = max(1, min(int(limit), 10))
    title_literal = json.dumps(title)
    gql = f"""
    {{
      Get {{
        {collection}(
          where: {{
            path: ["title"]
            operator: Equal
            valueText: {title_literal}
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
          _additional {{ id }}
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

    # Weaviate text Equal is token-ish on this archive — keep only strict title matches.
    wanted = title.casefold()
    strict = [r for r in rows if str(r.get("title") or "").casefold() == wanted]

    def _ci(row: dict[str, Any]) -> int:
        try:
            return int(row.get("chunk_index") if row.get("chunk_index") is not None else 99)
        except (TypeError, ValueError):
            return 99

    return sorted(strict, key=_ci)[:limit]


def _merge_rows(*row_lists: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Dedupe GraphQL rows by object id / chunk_id preserving first-seen order."""
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for rows in row_lists:
        for row in rows:
            if not isinstance(row, dict):
                continue
            additional = row.get("_additional") if isinstance(row.get("_additional"), dict) else {}
            key = str(
                additional.get("id")
                or row.get("chunk_id")
                or f"{row.get('title')}|{row.get('page_id')}|{row.get('chunk_index')}"
            )
            if key in seen:
                continue
            seen.add(key)
            out.append(row)
    return out


def _retrieve_pool_for_query(
    *,
    query: str,
    collection: str,
    year_str: str,
    pool: int,
    base_url: str,
    api_key: str,
    vector: list[float] | None,
    use_hybrid: bool,
) -> list[dict[str, Any]]:
    """Wide hybrid + title-BM25 + exact-title inject + query expansion → hits."""
    retrieve_q = clean_query_for_retrieval(query) or query
    variants = expand_queries(query)
    hybrid_rows: list[dict[str, Any]] = []
    title_rows: list[dict[str, Any]] = []
    exact_rows: list[dict[str, Any]] = []
    per_variant = max(6, min(12, pool))

    # Exact title equality for each variant — BM25 often buries the canonical page
    # under Medal/School/film satellites that share the same tokens.
    for variant in variants:
        try:
            exact_rows.extend(
                _graphql_exact_title(
                    base_url=base_url,
                    api_key=api_key,
                    collection=collection,
                    title=variant,
                    limit=4,
                )
            )
        except Exception:
            continue

    hybrid_queries: list[str] = []
    for candidate in (retrieve_q, *variants):
        key = (candidate or "").strip().casefold()
        if key and key not in {q.casefold() for q in hybrid_queries}:
            hybrid_queries.append(candidate.strip())
    raw_q = (query or "").strip()
    if (
        raw_q
        and raw_q.casefold() not in {q.casefold() for q in hybrid_queries}
        and raw_q.casefold() != retrieve_q.casefold()
        and len(raw_q.split()) >= 5
    ):
        hybrid_queries.append(raw_q)

    for hybrid_q in hybrid_queries[:4]:
        try:
            if use_hybrid and vector:
                hybrid_rows.extend(
                    _graphql_hybrid_search(
                        base_url=base_url,
                        api_key=api_key,
                        collection=collection,
                        query=hybrid_q,
                        vector=vector,
                        limit=max(8, pool // max(len(hybrid_queries), 1)),
                    )
                )
            else:
                hybrid_rows.extend(
                    _graphql_bm25_search(
                        base_url=base_url,
                        api_key=api_key,
                        collection=collection,
                        query=hybrid_q,
                        limit=max(8, pool // max(len(hybrid_queries), 1)),
                    )
                )
        except Exception:
            continue

    for variant in variants:
        try:
            title_rows.extend(
                _graphql_bm25_search(
                    base_url=base_url,
                    api_key=api_key,
                    collection=collection,
                    query=variant,
                    limit=per_variant,
                    properties=["title"],
                )
            )
        except Exception:
            continue
        if variant.casefold() != retrieve_q.casefold():
            try:
                hybrid_rows.extend(
                    _graphql_bm25_search(
                        base_url=base_url,
                        api_key=api_key,
                        collection=collection,
                        query=variant,
                        limit=per_variant,
                    )
                )
            except Exception:
                pass

    # Exact rows first so they survive the pool cap
    merged = _merge_rows(exact_rows, title_rows, hybrid_rows)
    exact_keys = {
        str((r.get("_additional") or {}).get("id") or r.get("chunk_id") or "")
        for r in exact_rows
    }
    title_keys = {
        str((r.get("_additional") or {}).get("id") or r.get("chunk_id") or "")
        for r in title_rows
    }
    hits: list[dict[str, Any]] = []
    for row in merged[: max(pool * 2, 50)]:
        hit = _normalize_hit(row, collection=collection, year=year_str, query=query)
        oid = str((row.get("_additional") or {}).get("id") or row.get("chunk_id") or "")
        if oid and oid in exact_keys:
            hit["from_exact_title"] = True
        if oid and oid in title_keys:
            hit["from_title_bm25"] = True
        hits.append(hit)
    return hits


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
    from pipeline.provenance import provenance_fields

    fm = [
        "---",
        *provenance_fields(
            source="weaviate",
            kind="wiki_chunk",
            tool="wiki_scout_search",
            limb="wiki_local",
            extra={
                "collection": hit.get("collection"),
                "snapshot_year": year,
                "snapshot_id": hit.get("snapshot_id") or "",
                "title": title,
                "doc_id": hit.get("doc_id") or "",
                "chunk_id": hit.get("chunk_id") or "",
                "query": hit.get("query") or "",
                "cognee_dataset": "eve_memory",
            },
        ),
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
    from pipeline.provenance import provenance_fields

    fm = [
        "---",
        *provenance_fields(
            source="weaviate",
            kind="truth_drift_compare",
            tool="wiki_scout_compare_years",
            limb="wiki_local",
            extra={"query": query, "years": json.dumps(years), "cognee_dataset": "truth_drift"},
        ),
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
    limit: int = DEFAULT_SEARCH_TOP_K,
    base_url: str = DEFAULT_WEAVIATE_URL,
    api_key: str = DEFAULT_API_KEY,
    cache_dir: Path | None = None,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    embed_model: str = DEFAULT_EMBED_MODEL,
    write_files: bool = True,
    interpret: bool = True,
    use_rerank: bool | None = None,
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
                "(see docs/WEAVIATE_HEIST.md / docs/WIKI_SCOUT.md). "
                "Do not fall back to web search unless Web Scout is enabled."
            ),
            "paths": [],
            "titles": [],
        }

    try:
        coll, year_str = resolve_collection(year=year, collection=collection)
    except ValueError as exc:
        return {"ok": False, "error": str(exc), "paths": [], "titles": []}

    top_k = max(1, min(int(limit) or DEFAULT_SEARCH_TOP_K, 10))
    pool = candidate_pool_size(top_k) if interpret else top_k

    retrieve_q = clean_query_for_retrieval(query) or query
    vector: list[float] | None = None
    use_hybrid = True
    try:
        vector = embed_query(retrieve_q, ollama_url=ollama_url, model=embed_model)
    except Exception as embed_exc:  # noqa: BLE001
        use_hybrid = False
        try:
            hits = _retrieve_pool_for_query(
                query=query,
                collection=coll,
                year_str=year_str,
                pool=pool,
                base_url=base_url,
                api_key=api_key,
                vector=None,
                use_hybrid=False,
            )
        except Exception as bm25_exc:  # noqa: BLE001
            return {
                "ok": False,
                "error": f"hybrid/embed failed ({embed_exc}); retrieve failed ({bm25_exc})",
                "paths": [],
                "titles": [],
            }
    else:
        hits = _retrieve_pool_for_query(
            query=query,
            collection=coll,
            year_str=year_str,
            pool=pool,
            base_url=base_url,
            api_key=api_key,
            vector=vector,
            use_hybrid=use_hybrid,
        )

    if not hits:
        return {
            "ok": False,
            "error": "No Wikipedia hits returned for this query/year.",
            "paths": [],
            "titles": [],
        }

    interpreter_pack: dict[str, Any] = {}
    rerank = use_rerank if use_rerank is not None else None
    if interpret:
        interpret_kwargs: dict[str, Any] = {"top_k": top_k}
        if rerank is not None:
            interpret_kwargs["use_rerank"] = rerank
        interpreter_pack = interpret_hits(query, hits, **interpret_kwargs)
        hits = list(interpreter_pack.get("selected_hits") or [])

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

    cards = cards_public(list(interpreter_pack.get("cards") or []))
    # Attach cache paths onto cards in order
    for i, card in enumerate(cards):
        if i < len(paths):
            card["path"] = paths[i]

    note = (
        f"Interpreter selected {len(hits)} of {interpreter_pack.get('candidates_in', len(hits))} "
        f"candidates under {out_dir}. "
        if interpret and write_files
        else (
            f"Cached {len(paths)} hit(s) under {out_dir}. "
            if write_files
            else f"Found {len(hits)} hit(s); cache write skipped. "
        )
    )
    note += (
        "Hits are encyclopedia pages/chunks — NOT footnote counts. "
        "Promote to Cognee only after triage."
    )
    coverage_note = str(interpreter_pack.get("coverage_note") or "").strip()
    if coverage_note:
        note = f"{note} {coverage_note}"

    chat_cards = cards_for_chat(cards)
    return {
        "ok": True,
        "query": query,
        "collection": coll,
        "snapshot_year": year_str,
        "count": len(hits),
        "paths": paths,
        "titles": titles,
        "summaries": summaries,
        "cards": chat_cards,
        "chat_reply_rule": WIKI_CHAT_REPLY_RULE,
        "interpreter": interpreter_pack.get("interpreter") if interpret else None,
        "interpreter_note": interpreter_pack.get("note") if interpret else None,
        "coverage_note": coverage_note,
        "usable": (
            bool((interpreter_pack.get("interpreter") or {}).get("usable", True))
            if interpret
            else True
        ),
        "note": note,
    }


def compare_years(
    query: str,
    *,
    years: tuple[str, ...] | list[str] | None = None,
    limit_per_year: int = DEFAULT_COMPARE_TOP_K,
    base_url: str = DEFAULT_WEAVIATE_URL,
    api_key: str = DEFAULT_API_KEY,
    cache_dir: Path | None = None,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    embed_model: str = DEFAULT_EMBED_MODEL,
    write_files: bool = True,
    interpret: bool = True,
    use_rerank: bool | None = None,
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
                "(see docs/WEAVIATE_HEIST.md / docs/WIKI_SCOUT.md). "
                "Do not fall back to web search unless Web Scout is enabled."
            ),
            "path": "",
            "years_found": [],
        }

    year_list = [
        str(y).strip() for y in (years or DEFAULT_COMPARE_YEARS) if str(y).strip()
    ]
    if not year_list:
        year_list = list(DEFAULT_COMPARE_YEARS)

    top_k = max(1, min(int(limit_per_year) or DEFAULT_COMPARE_TOP_K, 10))
    pool = candidate_pool_size(top_k) if interpret else top_k

    retrieve_q = clean_query_for_retrieval(query) or query
    try:
        vector = embed_query(retrieve_q, ollama_url=ollama_url, model=embed_model)
        use_hybrid = True
    except Exception as embed_exc:  # noqa: BLE001
        vector = []
        use_hybrid = False
        embed_error = str(embed_exc)
    else:
        embed_error = ""

    hits_by_year: dict[str, list[dict[str, Any]]] = {}
    cards_by_year: dict[str, list[dict[str, Any]]] = {}
    years_found: list[str] = []
    errors: list[str] = []
    interpreter_meta: dict[str, Any] = {}
    if embed_error:
        errors.append(f"embed: {embed_error} (falling back to bm25)")
    for year in year_list:
        try:
            coll, year_str = resolve_collection(year=year)
            raw_hits = _retrieve_pool_for_query(
                query=query,
                collection=coll,
                year_str=year_str,
                pool=pool,
                base_url=base_url,
                api_key=api_key,
                vector=vector if use_hybrid else None,
                use_hybrid=use_hybrid,
            )
            if interpret:
                interpret_kwargs: dict[str, Any] = {
                    "top_k": top_k,
                    "focus_year": year_str,
                }
                if use_rerank is not None:
                    interpret_kwargs["use_rerank"] = use_rerank
                pack = interpret_hits(query, raw_hits, **interpret_kwargs)
                hits = list(pack.get("selected_hits") or [])
                cards_by_year[year_str] = cards_public(list(pack.get("cards") or []))
                interpreter_meta[year_str] = {
                    **(pack.get("interpreter") or {}),
                    "usable": pack.get("usable"),
                    "coverage_note": pack.get("coverage_note"),
                }
            else:
                hits = raw_hits[:top_k]
                cards_by_year[year_str] = []
            hits_by_year[year_str] = hits
            if hits:
                years_found.append(year_str)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{year}: {exc}")
            hits_by_year[str(year)] = []
            cards_by_year[str(year)] = []

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
        f"Truth Drift compare for {len(years_found)} year(s) with interpreter top-{top_k}/year.",
        "Hits are encyclopedia pages/chunks — NOT footnote/reference counts.",
        "Snapshot years are frozen dumps, not hypothetical futures.",
        "Promote to Cognee only after triage.",
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
        "summaries": summaries[:24],
        "cards_by_year": cards_by_year,
        "interpreter": interpreter_meta if interpret else None,
        "interpreter_note": (
            "INTERPRETER: Ranked Wikipedia hits per year. Do not invent citation counts. "
            "Do not call archive years hypothetical unless the article text says so."
        )
        if interpret
        else None,
        "note": " ".join(note_bits),
    }


PROMOTE_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "wiki-promote.json"
_KIND_RE = re.compile(r"^kind:\s*(\S+)", re.MULTILINE)
_COGNEE_DATASET_RE = re.compile(r"^cognee_dataset:\s*(\S+)", re.MULTILINE)


def _load_promote_config() -> dict[str, Any]:
    try:
        data = json.loads(PROMOTE_CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def parse_cache_front_matter(body: str) -> dict[str, str]:
    """Read kind / cognee_dataset from YAML front matter (best-effort)."""
    out: dict[str, str] = {}
    if not body.startswith("---"):
        return out
    end = body.find("\n---", 3)
    if end < 0:
        return out
    block = body[3:end]
    kind_match = _KIND_RE.search(block)
    if kind_match:
        out["kind"] = kind_match.group(1).strip().strip('"').strip("'")
    dataset_match = _COGNEE_DATASET_RE.search(block)
    if dataset_match:
        out["cognee_dataset"] = dataset_match.group(1).strip().strip('"').strip("'")
    return out


def allowed_promote_datasets() -> frozenset[str]:
    cfg = _load_promote_config()
    raw = cfg.get("allowed_datasets")
    if isinstance(raw, list) and raw:
        return frozenset(str(item).strip() for item in raw if str(item).strip())
    return frozenset({"eve_memory", "truth_drift", "eve_core", "primitives_test"})


def resolve_promote_dataset(
    path: str | Path,
    body: str,
    *,
    dataset: str | None = None,
) -> tuple[str | None, str | None]:
    """Pick Cognee dataset for promote. Returns (dataset, reason) or (None, error)."""
    allowed = allowed_promote_datasets()
    override = (dataset or "").strip()
    if override:
        if override not in allowed:
            return None, f"dataset must be one of: {', '.join(sorted(allowed))}"
        return override, "explicit_override"

    cfg = _load_promote_config()
    by_kind = cfg.get("by_kind") if isinstance(cfg.get("by_kind"), dict) else {}
    default_dataset = str(cfg.get("default_dataset") or "eve_memory").strip() or "eve_memory"

    front = parse_cache_front_matter(body)
    explicit = str(front.get("cognee_dataset") or "").strip()
    if explicit:
        if explicit not in allowed:
            return None, f"cognee_dataset in file not allowed: {explicit}"
        return explicit, "front_matter_cognee_dataset"

    kind = str(front.get("kind") or "").strip()
    if kind and kind in by_kind:
        chosen = str(by_kind[kind]).strip()
        if chosen in allowed:
            return chosen, f"kind:{kind}"

    name = Path(path).name.lower()
    if name.startswith("compare_"):
        if "truth_drift" in allowed:
            return "truth_drift", "filename_compare_prefix"

    if default_dataset in allowed:
        return default_dataset, "default"
    return None, "No valid promote dataset configured"


def promote_dataset_routing_help() -> dict[str, Any]:
    cfg = _load_promote_config()
    return {
        "ok": True,
        "by_kind": cfg.get("by_kind")
        or {"wiki_chunk": "eve_memory", "truth_drift_compare": "truth_drift"},
        "default_dataset": cfg.get("default_dataset") or "eve_memory",
        "allowed_datasets": sorted(allowed_promote_datasets()),
        "config_path": str(PROMOTE_CONFIG_PATH),
    }


def promote_wiki_cache(
    path: str | Path,
    *,
    dataset: str | None = None,
    max_chars: int = 12_000,
) -> dict[str, Any]:
    """Explicitly promote a wiki_cache markdown file into Cognee remember.

    Never called automatically from search/compare.
    Dataset auto-routes: truth_drift_compare → truth_drift, wiki_chunk → eve_memory
    unless --dataset / tool override is provided.
    """
    from pipeline.provenance import remember_preamble_from_front_matter

    target = Path(path)
    cache_root = DEFAULT_CACHE_DIR.resolve()
    try:
        resolved = target.resolve()
    except OSError as exc:
        return {"ok": False, "error": str(exc), "path": str(path)}

    try:
        resolved.relative_to(cache_root)
    except ValueError:
        # Also allow paths under Thought Experiments parent if env overrides
        if "wiki_cache" not in str(resolved).replace("\\", "/").lower():
            return {
                "ok": False,
                "error": f"Path must be under wiki_cache ({cache_root})",
                "path": str(resolved),
            }

    if not resolved.is_file() or resolved.suffix.lower() != ".md":
        return {"ok": False, "error": "Not a .md file", "path": str(resolved)}

    try:
        body = resolved.read_text(encoding="utf-8")
    except OSError as exc:
        return {"ok": False, "error": str(exc), "path": str(resolved)}

    chosen, route_reason = resolve_promote_dataset(resolved, body, dataset=dataset)
    if not chosen:
        return {
            "ok": False,
            "error": route_reason or "Could not resolve dataset",
            "path": str(resolved),
        }

    if len(body) > max_chars:
        body = body[: max_chars - 1] + "…"

    content = remember_preamble_from_front_matter(str(resolved), body)
    try:
        import subprocess
        import sys

        root = Path(__file__).resolve().parents[1]
        proc = subprocess.run(
            [
                sys.executable,
                "-m",
                "pipeline.cognee_worker",
                "remember",
                "--content",
                content,
                "--dataset",
                chosen,
            ],
            cwd=str(root),
            env={**os.environ, "PYTHONPATH": str(root)},
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
        if proc.returncode != 0:
            return {
                "ok": False,
                "error": (proc.stderr or proc.stdout or f"exit {proc.returncode}").strip(),
                "path": str(resolved),
                "dataset": chosen,
            }
        try:
            result = json.loads(proc.stdout.strip() or "{}")
        except json.JSONDecodeError:
            result = {"raw": proc.stdout.strip()}
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "error": str(exc),
            "path": str(resolved),
            "dataset": chosen,
        }
    return {
        "ok": True,
        "path": str(resolved),
        "dataset": chosen,
        "dataset_reason": route_reason,
        "chars": len(content),
        "result": result,
        "note": "Promoted explicitly — scratch cache file left in place.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Weaviate Wikipedia scout → wiki_cache markdown"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    search_p = sub.add_parser("search", help="Wiki Interpreter search one snapshot year")
    search_p.add_argument("query")
    search_p.add_argument("--year", default=default_snapshot_year())
    search_p.add_argument("--limit", type=int, default=DEFAULT_SEARCH_TOP_K)
    search_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    search_p.add_argument("--api-key", default=DEFAULT_API_KEY)
    search_p.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    search_p.add_argument("--no-write", action="store_true")
    search_p.add_argument("--no-interpret", action="store_true")

    compare_p = sub.add_parser("compare", help="Truth Drift compare across years")
    compare_p.add_argument("query")
    compare_p.add_argument("--years", default="2017,2021,2026")
    compare_p.add_argument("--limit-per-year", type=int, default=DEFAULT_COMPARE_TOP_K)
    compare_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    compare_p.add_argument("--api-key", default=DEFAULT_API_KEY)
    compare_p.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    compare_p.add_argument("--no-write", action="store_true")
    compare_p.add_argument("--no-interpret", action="store_true")

    ready_p = sub.add_parser("ready", help="Check Weaviate readiness")
    ready_p.add_argument("--url", default=DEFAULT_WEAVIATE_URL)
    ready_p.add_argument("--api-key", default=DEFAULT_API_KEY)

    promote_p = sub.add_parser("promote", help="Explicit Cognee promote of a cache .md")
    promote_p.add_argument("path")
    promote_p.add_argument(
        "--dataset",
        default=None,
        help="Cognee dataset (auto from cache kind when omitted)",
    )

    args = parser.parse_args(argv)

    if args.command == "ready":
        ok, detail = check_weaviate(args.url, args.api_key)
        print(json.dumps({"ok": ok, "detail": detail, "url": args.url}, indent=2))
        return 0 if ok else 1

    if args.command == "promote":
        result = promote_wiki_cache(args.path, dataset=args.dataset)
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1

    if args.command == "search":
        result = search(
            args.query,
            year=args.year,
            limit=args.limit,
            base_url=args.url,
            api_key=args.api_key,
            cache_dir=Path(args.cache_dir),
            write_files=not args.no_write,
            interpret=not args.no_interpret,
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
            interpret=not args.no_interpret,
        )
        print(json.dumps(result, indent=2, default=str))
        return 0 if result.get("ok") else 1

    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
