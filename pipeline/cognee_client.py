"""Cognee adapter — maps v1.0-style verbs onto the installed Cognee API."""

from __future__ import annotations

import asyncio
import os
import re
import sqlite3
from pathlib import Path
from typing import Any, Literal

from pipeline.cognee_lock import run_with_cognee_lock

ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / "config" / "cognee.env"

IngestMode = Literal["fast", "full"]


DEFAULT_COGNEE_ROOT = r"V:\Cognee"

# Dataset-filtered recall: initial candidate pool, then fallback when filter is empty.
DEFAULT_RECALL_TOP_K = 250
DEFAULT_RECALL_FALLBACK_TOP_K = 2000
MIN_RECALL_TOP_K = 1
MAX_RECALL_TOP_K = 5000
CURATED_DATASET = "primitives_test"
CURATED_FUEL = "curated_primitives"

# Hex UUID fragments only (e.g. ``1b41dc7c-1fdc``); not arbitrary text prefixes.
_UUID_FRAGMENT_RE = re.compile(r"^[0-9a-f]+(?:-[0-9a-f]+)*$")

# Prefer extracting frontmatter Truth-Drift triples already present in wiki documents.
WIKI_GRAPH_PROMPT = """You extract a knowledge graph as JSON matching this EXACT schema shape:

{"nodes":[{"id":"string","name":"string","type":"string","description":"string"}],"edges":[{"source_node_id":"string","target_node_id":"string","relationship_name":"string"}]}

Rules (strict):
- Prefer explicit triple lines already in the text (SnapshotEdges / Relationships).
- Keys must be EXACT: id, name, type, description, source_node_id, target_node_id, relationship_name. No spaces in keys.
- Every node field is a STRING (never numbers, never null). Empty description is "".
- Every edge field is a non-empty STRING. relationship_name is snake_case (snapshot_year, is_snapshot_of, links_to, in_category).
- Use human-readable ids from the text (e.g. "Cambrai (2017)").
- edges is a TOP-LEVEL array sibling of nodes — never nest edges inside a node.
- Return ONLY that JSON object. No markdown fences. No parent key like KnowledgeGraph.
- If unsure, return fewer correct nodes/edges (even {"nodes":[],"edges":[]}) rather than inventing broken structure.
"""


def _strip_json_keys(value: Any) -> Any:
    """Recursively strip whitespace from dict keys (llama often emits 'name ' etc.)."""
    if isinstance(value, dict):
        out: dict[str, Any] = {}
        for raw_key, raw_val in value.items():
            key = str(raw_key).strip()
            cleaned = _strip_json_keys(raw_val)
            if key in out and isinstance(out[key], dict) and isinstance(cleaned, dict):
                out[key] = {**out[key], **cleaned}
            else:
                out[key] = cleaned
        return out
    if isinstance(value, list):
        return [_strip_json_keys(item) for item in value]
    return value


def _as_nonempty_str(value: Any, fallback: str = "") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text if text else fallback


def _sanitize_node_dict(raw: Any) -> dict[str, str] | None:
    if not isinstance(raw, dict):
        return None
    node = {str(k).strip(): v for k, v in raw.items()}
    # Malformed LLM output sometimes nests edges inside a node object.
    node.pop("edges", None)
    node.pop("nodes", None)
    node_id = _as_nonempty_str(node.get("id"))
    name = _as_nonempty_str(node.get("name"), fallback=node_id)
    if not node_id and name:
        node_id = name
    if not node_id and not name:
        return None
    return {
        "id": node_id,
        "name": name or node_id,
        "type": _as_nonempty_str(node.get("type"), fallback="Entity"),
        "description": _as_nonempty_str(node.get("description")),
    }


def _sanitize_edge_dict(raw: Any) -> dict[str, str] | None:
    if not isinstance(raw, dict):
        return None
    edge = {str(k).strip(): v for k, v in raw.items()}
    source = _as_nonempty_str(edge.get("source_node_id"))
    target = _as_nonempty_str(edge.get("target_node_id"))
    rel = _as_nonempty_str(edge.get("relationship_name"), fallback="related_to")
    rel = rel.lstrip("+").strip().lower().replace(" ", "_")
    if not source or not target:
        return None
    return {
        "source_node_id": source,
        "target_node_id": target,
        "relationship_name": rel or "related_to",
    }


def sanitize_knowledge_graph_payload(payload: Any) -> dict[str, list]:
    """Coerce messy local-LLM JSON into a KnowledgeGraph-shaped dict.

    Overnight failures: trailing spaces in keys ('name '), int ids (1494), null edge
    endpoints, and edges nested inside node objects. Keep identity of KnowledgeGraph
    class intact for Cognee's `graph_model is KnowledgeGraph` checks.
    """
    if payload is None:
        return {"nodes": [], "edges": []}
    if hasattr(payload, "model_dump"):
        try:
            payload = payload.model_dump()
        except Exception:  # noqa: BLE001
            return {"nodes": [], "edges": []}
    if not isinstance(payload, dict):
        return {"nodes": [], "edges": []}

    data = _strip_json_keys(payload)
    # Some models wrap once: {"KnowledgeGraph": {...}} or {"graph": {...}}
    for wrap_key in ("KnowledgeGraph", "knowledge_graph", "graph", "data"):
        nested = data.get(wrap_key)
        if isinstance(nested, dict) and ("nodes" in nested or "edges" in nested):
            data = _strip_json_keys(nested)
            break

    raw_nodes = data.get("nodes") if isinstance(data.get("nodes"), list) else []
    raw_edges = data.get("edges") if isinstance(data.get("edges"), list) else []
    # Rescue edges mistakenly embedded inside node dicts.
    rescued_edges: list[Any] = []
    for item in raw_nodes:
        if isinstance(item, dict) and isinstance(item.get("edges"), list):
            rescued_edges.extend(item["edges"])

    nodes: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for item in raw_nodes:
        node = _sanitize_node_dict(item)
        if not node or node["id"] in seen_ids:
            continue
        seen_ids.add(node["id"])
        nodes.append(node)

    edges: list[dict[str, str]] = []
    for item in list(raw_edges) + rescued_edges:
        edge = _sanitize_edge_dict(item)
        if not edge:
            continue
        if edge["source_node_id"] not in seen_ids or edge["target_node_id"] not in seen_ids:
            continue
        edges.append(edge)

    return {"nodes": nodes, "edges": edges}


def default_cognee_system_dir() -> Path:
    """Cognee graph/vector DB location. Must be NTFS (never OneDrive, never exFAT I:).

    lancedb/kuzu/sqlite require NTFS semantics; the 4TB I: drive is exFAT and fails. To keep
    heavy storage off the C: Core Runtime drive, the graph/vector DB lives on an NTFS VHDX
    whose backing file sits on I: (I:\\EMPIRE_VHDX\\empire_cognee.vhdx) mounted at V:, so we
    default to V:\\Cognee. Lightweight control files (cognee.lock, wiki-checkpoint.json) stay
    on C: under %LOCALAPPDATA%\\EMPIRE by design. EMPIRE_COGNEE_ROOT overrides this.
    """
    override = os.environ.get("EMPIRE_COGNEE_ROOT")
    if override:
        return Path(override)
    return Path(DEFAULT_COGNEE_ROOT)


def load_cognee_env() -> None:
    if not ENV_FILE.exists():
        os.environ.setdefault("SYSTEM_ROOT_DIRECTORY", str(default_cognee_system_dir().resolve()))
        return

    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ[key.strip()] = value.strip()

    # EMPIRE_COGNEE_ROOT always wins so storage can be redirected without editing cognee.env
    # (e.g. away from an exFAT drive that cannot host lancedb/kuzu, onto an NTFS volume).
    override = os.environ.get("EMPIRE_COGNEE_ROOT")
    system_root = os.environ.get("SYSTEM_ROOT_DIRECTORY", "")
    if override:
        os.environ["SYSTEM_ROOT_DIRECTORY"] = str(Path(override).resolve())
    elif not system_root or system_root.startswith("."):
        os.environ["SYSTEM_ROOT_DIRECTORY"] = str(default_cognee_system_dir().resolve())

    system_dir = Path(os.environ["SYSTEM_ROOT_DIRECTORY"])
    system_dir.mkdir(parents=True, exist_ok=True)
    # SQLite maintenance only applies to the legacy embedded backend.
    if os.environ.get("DB_PROVIDER", "").strip().lower() != "postgres":
        _ensure_sqlite_wal(system_dir)
        _repair_pipeline_run_uuid_rows(system_dir)
    _quiet_cognee_logging()

    # Mirror official Cognee Just-Postgres vars from config into process env (already set
    # above from cognee.env). Also load cognee/.env if present for dual-path configs.
    alt_env = ROOT / "cognee" / ".env"
    if alt_env.exists():
        for line in alt_env.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            # config/cognee.env wins for keys already set from ENV_FILE.
            os.environ.setdefault(key.strip(), value.strip())

    # Operator LLM overrides always win over config/cognee.env (curated 14b cognify, etc.).
    for override_key in ("EMPIRE_PRIMITIVES_LLM_MODEL", "EMPIRE_LLM_MODEL"):
        override = os.environ.get(override_key, "").strip()
        if override:
            os.environ["LLM_MODEL"] = override
            break


def _ensure_sqlite_wal(system_dir: Path) -> None:
    """Enable WAL on Cognee's SQLite DB so concurrent cognify writers queue on the busy
    timeout instead of failing immediately with 'database is locked'. WAL persists in the
    file header, so all of Cognee's later connections inherit it. Best-effort / idempotent.
    """
    db_path = system_dir / "databases" / "cognee_db"
    try:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(db_path))
        try:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA busy_timeout=60000;")
        finally:
            conn.close()
    except Exception:  # noqa: BLE001 — never block ingest on this optimization
        pass


def _repair_pipeline_run_uuid_rows(system_dir: Path) -> None:
    """Delete ``pipeline_runs`` rows whose UUID ``id`` became a float (e.g. inf).

    Observed during Fast Mode overnight: one COMPLETED add_pipeline row with ``id=inf``
    makes every subsequent ``cognee.add`` fail with
    ``AttributeError: 'float' object has no attribute 'replace'`` inside SQLAlchemy UUID
    processing. Safe: only removes non-text / inf / nan ids.
    """
    db_path = system_dir / "databases" / "cognee_db"
    if not db_path.exists():
        return
    try:
        conn = sqlite3.connect(str(db_path))
        try:
            conn.execute("PRAGMA busy_timeout=60000;")
            cur = conn.execute(
                """
                DELETE FROM pipeline_runs
                WHERE typeof(id) != 'text'
                   OR id IS NULL
                   OR lower(cast(id AS text)) IN ('inf', '-inf', 'nan')
                """
            )
            if cur.rowcount:
                conn.commit()
                print(
                    f"[empire] repaired pipeline_runs: deleted {cur.rowcount} "
                    f"corrupt UUID id row(s)",
                    flush=True,
                )
        finally:
            conn.close()
    except Exception:  # noqa: BLE001 — never block ingest on repair
        pass


_EMBED_PATCHED = False
_LLM_RETRY_PATCHED = False
_SCHEMA_PATCHED = False
_LOGGING_QUIETED = False


def _env_flag(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


def _quiet_cognee_logging() -> None:
    """Reduce Cognee INFO spam during overnight (still logs WARNING+).

    Default on (``EMPIRE_QUIET_COGNEE=1``). Set to ``0`` for full pipeline chatter.
    High-signal ``[wiki]`` lines from wiki_ingest are unaffected.
    """
    global _LOGGING_QUIETED
    if _LOGGING_QUIETED:
        return
    _LOGGING_QUIETED = True
    if not _env_flag("EMPIRE_QUIET_COGNEE", default=True):
        return
    import logging

    level = logging.WARNING
    for name in (
        "cognee",
        "cognee.modules",
        "cognee.modules.pipelines",
        "cognee.modules.pipelines.layers.check_pipeline_run_qualification",
        "liteLLM",
        "LiteLLM",
        "httpx",
        "httpcore",
        "openai",
    ):
        logging.getLogger(name).setLevel(level)
    root = logging.getLogger()

    class _DropCogneeInfo(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:  # noqa: A003
            if record.levelno >= logging.WARNING:
                return True
            name = record.name or ""
            return not (
                name.startswith("cognee")
                or name.startswith("liteLLM")
                or name.startswith("LiteLLM")
                or name.startswith("httpx")
                or name.startswith("httpcore")
            )

    for handler in root.handlers:
        handler.addFilter(_DropCogneeInfo())


def _patch_structured_schema_defaults() -> None:
    """Make Cognee structured-output fields tolerant of local Ollama omissions.

    Stock Node.description / SummarizedContent fields are required; llama3.1 often omits
    them and instructor retries 3x (~tens of seconds wasted per chunk). Defaults keep the
    identity `graph_model is KnowledgeGraph` path (required for Kuzu expansion) intact.

    Also wraps KnowledgeGraph.model_validate / model_validate_json so messy keys (e.g.
    'name '), int ids, and null edge endpoints are coerced before pydantic rejects them.
    """
    global _SCHEMA_PATCHED
    if _SCHEMA_PATCHED:
        return
    try:
        from cognee.shared.data_models import KnowledgeGraph, Node, SummarizedContent
    except Exception:  # noqa: BLE001
        _SCHEMA_PATCHED = True
        return

    try:
        if "description" in Node.model_fields:
            Node.model_fields["description"].default = ""
        if "type" in Node.model_fields and Node.model_fields["type"].default is None:
            Node.model_fields["type"].default = "Entity"
        Node.model_rebuild(force=True)
        KnowledgeGraph.model_rebuild(force=True)
        if "summary" in SummarizedContent.model_fields:
            SummarizedContent.model_fields["summary"].default = ""
        if "description" in SummarizedContent.model_fields:
            SummarizedContent.model_fields["description"].default = ""
        SummarizedContent.model_rebuild(force=True)
    except Exception:  # noqa: BLE001 — never block ingest on schema softening
        pass

    if not getattr(KnowledgeGraph.__init__, "_empire_kg_sanitized", False):
        import json as _json

        _orig_init = KnowledgeGraph.__init__
        _orig_validate = KnowledgeGraph.model_validate
        _orig_validate_json = KnowledgeGraph.model_validate_json

        def _safe_init(self: Any, /, **data: Any) -> None:
            cleaned = sanitize_knowledge_graph_payload(data)
            try:
                _orig_init(self, **cleaned)
            except Exception:  # noqa: BLE001 — never abort cognify on one bad chunk
                _orig_init(self, nodes=[], edges=[])

        @classmethod  # type: ignore[misc]
        def _safe_model_validate(cls: Any, obj: Any, *args: Any, **kwargs: Any) -> Any:
            try:
                return _orig_validate(sanitize_knowledge_graph_payload(obj), *args, **kwargs)
            except Exception:  # noqa: BLE001
                return _orig_validate({"nodes": [], "edges": []}, *args, **kwargs)

        @classmethod  # type: ignore[misc]
        def _safe_model_validate_json(cls: Any, json_data: Any, *args: Any, **kwargs: Any) -> Any:
            try:
                if isinstance(json_data, (bytes, bytearray)):
                    json_data = json_data.decode("utf-8", errors="replace")
                parsed = _json.loads(json_data) if isinstance(json_data, str) else json_data
                return _orig_validate(sanitize_knowledge_graph_payload(parsed), *args, **kwargs)
            except Exception:  # noqa: BLE001
                try:
                    return _orig_validate_json(json_data, *args, **kwargs)
                except Exception:  # noqa: BLE001
                    return _orig_validate({"nodes": [], "edges": []}, *args, **kwargs)

        _safe_init._empire_kg_sanitized = True  # type: ignore[attr-defined]
        KnowledgeGraph.__init__ = _safe_init  # type: ignore[method-assign]
        KnowledgeGraph.model_validate = _safe_model_validate  # type: ignore[method-assign]
        KnowledgeGraph.model_validate_json = _safe_model_validate_json  # type: ignore[method-assign]

    _SCHEMA_PATCHED = True


def _patch_ollama_embeddings() -> None:
    """Guard Cognee's Ollama embedding engine against empty inputs.

    Cognee's cognify pipeline can emit empty/whitespace chunks; Ollama's /api/embed then
    returns {"embeddings": []} and the stock engine does data["embeddings"][0] -> IndexError,
    which aborts the whole cognify run. We wrap _get_embedding to return a zero vector for
    empty input or an empty response instead of crashing.
    """
    global _EMBED_PATCHED
    if _EMBED_PATCHED:
        return
    try:
        from cognee.infrastructure.databases.vector.embeddings.OllamaEmbeddingEngine import (
            OllamaEmbeddingEngine,
        )
    except Exception:  # noqa: BLE001 — different backend configured; nothing to patch
        _EMBED_PATCHED = True
        return

    original = OllamaEmbeddingEngine._get_embedding

    async def _safe_get_embedding(self: Any, prompt: str) -> list[float]:
        if not prompt or not str(prompt).strip():
            return [0.0] * self.dimensions
        try:
            result = await original(self, prompt)
        except IndexError:
            return [0.0] * self.dimensions
        if not result:
            return [0.0] * self.dimensions
        return result

    OllamaEmbeddingEngine._get_embedding = _safe_get_embedding
    _EMBED_PATCHED = True


def _patch_ollama_structured_retries() -> None:
    """Tune instructor max_retries on Cognee's Ollama adapter (stock default 2 => 3 attempts).

    Overnight: SummarizedContent failures benefited from fail-fast, but KnowledgeGraph extract
    after skip-summarize needs a bit more room — llama3.1 often needs a second repair pass.
    Default EMPIRE_OLLAMA_STRUCTURED_MAX_RETRIES=2 (3 attempts). KnowledgeGraph still has an
    empty-graph fallback so one bad chunk cannot abort the whole cognify slice.
    """
    global _LLM_RETRY_PATCHED
    if _LLM_RETRY_PATCHED:
        return
    try:
        from cognee.infrastructure.llm.structured_output_framework.litellm_instructor.llm.ollama import (
            adapter as ollama_adapter,
        )
    except Exception:  # noqa: BLE001
        _LLM_RETRY_PATCHED = True
        return

    try:
        max_retries = int(os.environ.get("EMPIRE_OLLAMA_STRUCTURED_MAX_RETRIES", "2"))
    except ValueError:
        max_retries = 2
    max_retries = max(0, max_retries)

    original = ollama_adapter.OllamaAPIAdapter.acreate_structured_output
    if getattr(original, "_empire_retry_patched", False):
        _LLM_RETRY_PATCHED = True
        return

    import logging

    import litellm
    from cognee.shared.rate_limiting import llm_rate_limiter_context_manager
    from tenacity import (
        before_sleep_log,
        retry,
        retry_if_not_exception_type,
        stop_after_delay,
        wait_exponential_jitter,
    )

    logger = logging.getLogger("empire.cognee_ollama")

    @retry(
        stop=stop_after_delay(128),
        wait=wait_exponential_jitter(8, 128),
        retry=retry_if_not_exception_type(litellm.exceptions.NotFoundError),
        before_sleep=before_sleep_log(logger, logging.DEBUG),
        reraise=True,
    )
    async def _acreate_structured_output(
        self: Any, text_input: str, system_prompt: str, response_model: Any, **kwargs: Any
    ) -> Any:
        is_kg = getattr(response_model, "__name__", "") == "KnowledgeGraph"
        try:
            async with llm_rate_limiter_context_manager():
                return await self.aclient.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": f"{text_input}"},
                        {"role": "system", "content": system_prompt},
                    ],
                    max_retries=max_retries,
                    response_model=response_model,
                )
        except Exception as exc:  # noqa: BLE001
            if is_kg:
                logger.warning(
                    "KnowledgeGraph extract failed after retries; using empty graph (%s)",
                    exc,
                )
                try:
                    return response_model.model_validate({"nodes": [], "edges": []})
                except Exception:  # noqa: BLE001
                    return response_model(nodes=[], edges=[])
            raise

    _acreate_structured_output._empire_retry_patched = True  # type: ignore[attr-defined]
    ollama_adapter.OllamaAPIAdapter.acreate_structured_output = _acreate_structured_output
    _LLM_RETRY_PATCHED = True


def _cognee_module() -> Any:
    load_cognee_env()
    import cognee  # noqa: WPS433

    _patch_structured_schema_defaults()
    _patch_ollama_embeddings()
    _patch_ollama_structured_retries()
    return cognee


async def remember(content: str, dataset: str = "mock", mode: IngestMode = "fast") -> None:
    """Store a document in Cognee (foundation step).

    Fast Mode (default): ``cognee.add`` only — no llama3.1 graph extract.
    Call ``embed_dataset`` after a batch of remembers for nomic-embed-text vectors.
    Full Mode: add + cognify (LLM graph extract). Prefer ``cognify_dataset`` once
    per batch from wiki_ingest instead of per-file full remember when possible.
    """
    await remember_many([content], dataset=dataset, mode=mode)


async def remember_many(
    contents: list[str],
    dataset: str = "mock",
    mode: IngestMode = "fast",
) -> None:
    """Store many documents via concurrent ``cognee.add`` (Postgres) or serialized (SQLite).

    Postgres / Just-Postgres: ``asyncio.gather`` with ``EMPIRE_REMEMBER_CONCURRENCY``
    (default 8) so multiple Wikipedia articles add in parallel.
    ``EMPIRE_REMEMBER_DATA_PER_BATCH`` (default 1) maps to Cognee ``add(..., data_per_batch=)``.
    When > 1, contents are chunked into list adds (Cognee's intended batch API) with
    concurrent add() calls capped so in-flight docs ≈ remember concurrency.
    Legacy SQLite: keep sequential adds under the file lock to avoid UUID corruption.
    """

    if not contents:
        return

    async def _run() -> None:
        cognee = _cognee_module()
        provider = os.environ.get("DB_PROVIDER", "").strip().lower()
        raw_conc = os.environ.get("EMPIRE_REMEMBER_CONCURRENCY", "8" if provider == "postgres" else "1")
        try:
            concurrency = max(1, int(raw_conc.strip()))
        except ValueError:
            concurrency = 8 if provider == "postgres" else 1

        # Default 1 preserves prior single-item add behavior; overnight may set 16.
        raw_dpb = os.environ.get("EMPIRE_REMEMBER_DATA_PER_BATCH", "1").strip()
        try:
            data_per_batch = max(1, int(raw_dpb))
        except ValueError:
            data_per_batch = 1

        if data_per_batch > 1 and len(contents) > 1:
            # List-batch path: fewer add_pipeline runs, Cognee-internal item parallelism.
            chunks = [
                contents[i : i + data_per_batch]
                for i in range(0, len(contents), data_per_batch)
            ]
            # ceil(concurrency / data_per_batch): keep ~concurrency docs in flight
            # via fewer list-add pipelines (helps PG vs many single-item add() runs).
            parallel_adds = max(1, (concurrency + data_per_batch - 1) // data_per_batch)
            sem = asyncio.Semaphore(parallel_adds)

            async def _add_chunk(chunk: list[str]) -> None:
                async with sem:
                    await cognee.add(
                        chunk,
                        dataset_name=dataset,
                        data_per_batch=data_per_batch,
                    )

            await asyncio.gather(*[_add_chunk(chunk) for chunk in chunks])
        elif concurrency > 1 and len(contents) > 1:
            sem = asyncio.Semaphore(concurrency)

            async def _add_one(content: str) -> None:
                async with sem:
                    await cognee.add(
                        content,
                        dataset_name=dataset,
                        data_per_batch=data_per_batch,
                    )

            await asyncio.gather(*[_add_one(content) for content in contents])
        else:
            for content in contents:
                await cognee.add(
                    content,
                    dataset_name=dataset,
                    data_per_batch=data_per_batch,
                )

        # CRITICAL: Fast Mode must not invoke cognify (llama3.1:latest graph extract).
        # Deep reasoning is deferred to runtime / explicit --mode full + cognify_dataset.
        if mode == "full":
            await cognee.cognify(
                datasets=dataset,
                custom_prompt=WIKI_GRAPH_PROMPT,
                data_per_batch=1,
            )
        # else: intentionally skip await cognee.cognify(...)

    await run_with_cognee_lock(_run)


async def embed_dataset(dataset: str) -> None:
    """Chunk + nomic-embed-text only — no llama3.1 extract_graph / summarize.

    Pipeline: classify → chunk → add_data_points (vector index). Truth-Drift edges
    already live in document text from the normalizer; LLM graph build is deferred.
    """

    async def _run() -> None:
        cognee = _cognee_module()
        from cognee.api.v1.cognify.cognify import get_default_tasks
        from cognee.modules.pipelines import run_pipeline
        from cognee.modules.pipelines.layers.pipeline_execution_mode import get_pipeline_executor

        tasks = await get_default_tasks()
        # Cognee 1.x merges graph+summarize into extract_graph_and_summarize; skip that
        # and DLT FK extraction. Keep classify → chunk → add_data_points only.
        skip_names = {
            "extract_graph_and_summarize",
            "extract_graph_from_data",
            "summarize_text",
            "extract_dlt_fk_edges",
        }
        kept = []
        for task in tasks:
            name = getattr(getattr(task, "executable", None), "__name__", "")
            if name in skip_names:
                continue
            kept.append(task)
        tasks = kept
        kept_names = [
            getattr(getattr(t, "executable", None), "__name__", "?") for t in tasks
        ]
        if "classify_documents" not in kept_names or "add_data_points" not in kept_names:
            raise RuntimeError(
                f"EMPIRE embed-only: expected classify+chunk+add_data_points, got {kept_names}"
            )

        pipeline_executor_func = get_pipeline_executor(run_in_background=False)
        # Fast Mode headroom: chunk+embed parallelism (nomic-only; no llama writers).
        # Override with EMPIRE_EMBED_DATA_PER_BATCH (default 8 on 16GB VRAM / 64GB hosts).
        raw_batch = os.environ.get("EMPIRE_EMBED_DATA_PER_BATCH", "8").strip()
        try:
            data_per_batch = max(1, int(raw_batch))
        except ValueError:
            data_per_batch = 8
        await pipeline_executor_func(
            pipeline=run_pipeline,
            tasks=tasks,
            datasets=dataset,
            # CRITICAL (Cognee 1.x): use_pipeline_cache=True marks the whole dataset
            # COMPLETED after the first successful run and skips ALL later slices.
            # Keep incremental_loading so per-item already-embedded rows are skipped.
            # See https://github.com/topoteretes/cognee pipeline cache / qualification.
            incremental_loading=True,
            use_pipeline_cache=False,
            pipeline_name="empire_embed_only_pipeline",
            data_per_batch=data_per_batch,
        )

    await run_with_cognee_lock(_run)


async def recall(
    query: str,
    dataset: str | None = None,
    mode: IngestMode = "fast",
) -> Any:
    async def _run() -> Any:
        cognee = _cognee_module()
        datasets = dataset if dataset else None
        query_type = (
            cognee.SearchType.GRAPH_COMPLETION
            if mode == "full"
            else cognee.SearchType.CHUNKS
        )
        # only_context=True returns empty {} payloads on Cognee 0.5.x CHUNKS search;
        # False returns the chunk dicts (text includes SnapshotYear / Title (YEAR) edges).
        # With access control OFF, search is global — pull a wide candidate set then
        # keep only chunks whose document_name belongs to ``dataset``.
        if dataset:
            initial_top_k = _bounded_recall_top_k("EMPIRE_RECALL_TOP_K", DEFAULT_RECALL_TOP_K)
            fallback_top_k = _bounded_recall_top_k(
                "EMPIRE_RECALL_FALLBACK_TOP_K", DEFAULT_RECALL_FALLBACK_TOP_K
            )
        else:
            initial_top_k = 15
            fallback_top_k = initial_top_k
        allowed_names: set[str] = set()
        allowed_ids: set[str] = set()
        if dataset:
            allowed_names, allowed_ids = await _dataset_document_keys(dataset)
        raw = await cognee.search(
            query,
            query_type=query_type,
            datasets=datasets,
            only_context=False,
            top_k=initial_top_k,
        )
        if not dataset or not isinstance(raw, list):
            return raw
        filtered = _filter_hits_for_dataset(
            raw, dataset, allowed_names=allowed_names, allowed_ids=allowed_ids
        )
        if not filtered and fallback_top_k > initial_top_k:
            raw = await cognee.search(
                query,
                query_type=query_type,
                datasets=datasets,
                only_context=False,
                top_k=fallback_top_k,
            )
            if isinstance(raw, list):
                filtered = _filter_hits_for_dataset(
                    raw, dataset, allowed_names=allowed_names, allowed_ids=allowed_ids
                )
        return filtered

    return await run_with_cognee_lock(_run)


def _bounded_recall_top_k(env_name: str, default: int) -> int:
    raw = os.environ.get(env_name, str(default)).strip()
    try:
        value = int(raw)
    except ValueError:
        value = default
    return max(MIN_RECALL_TOP_K, min(MAX_RECALL_TOP_K, value))


def _normalized_key(value: object) -> str:
    return str(value or "").strip().lower()


def _is_curated_dataset(dataset: str) -> bool:
    return _normalized_key(dataset) == CURATED_DATASET


def _hit_fields(hit: object) -> tuple[str, str, str]:
    if not isinstance(hit, dict):
        return str(hit), "", ""
    payload = hit.get("payload")
    nested = payload if isinstance(payload, dict) else {}
    text = hit.get("text") or nested.get("text") or ""
    document_name = hit.get("document_name") or nested.get("document_name") or ""
    document_id = hit.get("document_id") or nested.get("document_id") or ""
    return str(text), _normalized_key(document_name), _normalized_key(document_id)


def _parse_marker_value(line: str, prefix: str) -> str | None:
    """Return normalized value after ``prefix`` (e.g. ``dataset:`` or ``fuel:``)."""
    stripped = line.strip()
    if not stripped.lower().startswith(prefix):
        return None
    return _normalized_key(stripped[len(prefix) :])


def _text_dataset_values(text: str) -> set[str]:
    """Extract normalized dataset names from stamped header lines (exact line values)."""
    values: set[str] = set()
    for line in text.splitlines():
        for prefix in ("dataset:", "dataset="):
            parsed = _parse_marker_value(line, prefix)
            if parsed:
                values.add(parsed)
                break
    return values


def _text_fuel_value(text: str) -> str:
    """Return normalized fuel marker value from stamped header lines, or ``\"\"``."""
    for line in text.splitlines():
        parsed = _parse_marker_value(line, "fuel:")
        if parsed:
            return parsed
    return ""


def _matches_allowed_id(candidate: str, allowed_ids: set[str]) -> bool:
    """Match exact ids or abbreviated UUID prefixes at hyphen segment boundaries."""
    if not candidate or not allowed_ids:
        return False
    if candidate in allowed_ids:
        return True
    if "-" not in candidate or not _UUID_FRAGMENT_RE.fullmatch(candidate):
        return False
    boundary = candidate + "-"
    return any(allowed.startswith(boundary) for allowed in allowed_ids)


async def _dataset_document_keys(dataset: str) -> tuple[set[str], set[str]]:
    """Return (data.name set, data.id set) for a Cognee dataset."""
    # cognee.modules DB accessors read connection settings from os.environ set by
    # load_cognee_env() inside _cognee_module(). Import here (not module top) so recall
    # never touches Cognee before env is loaded; _dataset_document_keys runs only
    # after _cognee_module() in recall's _run().
    try:
        from cognee.modules.data.methods import get_dataset_data, get_datasets
        from cognee.modules.users.methods import get_default_user

        user = await get_default_user()
        datasets = await get_datasets(user.id)
        target_key = _normalized_key(dataset)
        target = next(
            (
                d
                for d in datasets
                if _normalized_key(_dataset_field(d, "name")) == target_key
            ),
            None,
        )
        if target is None:
            return set(), set()
        rows = await get_dataset_data(target.id)
        names: set[str] = set()
        ids: set[str] = set()
        for row in rows:
            name = _dataset_field(row, "name")
            if name:
                names.add(_normalized_key(name))
            rid = _dataset_field(row, "id")
            if rid is not None:
                ids.add(_normalized_key(rid))
        return names, ids
    except Exception:  # noqa: BLE001
        return set(), set()


def _dataset_field(dataset: object, field: str) -> Any:
    """Read a field from either legacy dict records or Cognee 1.x models."""
    if isinstance(dataset, dict):
        return dataset.get(field)
    return getattr(dataset, field, None)


def _filter_hits_for_dataset(
    hits: list,
    dataset: str,
    *,
    allowed_names: set[str] | None = None,
    allowed_ids: set[str] | None = None,
) -> list:
    """Keep chunks that belong to ``dataset`` despite the global pgvector index.

    Prefer document_name / document_id membership (covers body chunks without Fuel
    headers). Fall back to stamped ``dataset:`` / ``fuel:`` markers in text.
    """
    names = {_normalized_key(n) for n in (allowed_names or set()) if _normalized_key(n)}
    ids = {_normalized_key(i) for i in (allowed_ids or set()) if _normalized_key(i)}
    target_dataset = _normalized_key(dataset)
    curated = _is_curated_dataset(dataset)
    kept: list = []
    for hit in hits:
        text, doc_name, doc_id = _hit_fields(hit)
        if names and doc_name in names:
            kept.append(hit)
            continue
        if ids and (_matches_allowed_id(doc_id, ids) or _matches_allowed_id(doc_name, ids)):
            kept.append(hit)
            continue
        if target_dataset in _text_dataset_values(text):
            kept.append(hit)
            continue
        if curated and _text_fuel_value(text) == CURATED_FUEL:
            kept.append(hit)
            continue
    return kept


async def _cognify_fast(cognee: Any, dataset: str) -> None:
    """Light cognify for Cognee 1.x: skip extract_graph_and_summarize LLM step when possible.

    Fast wiki ingest already embeds Truth-Drift triples in document text. Full graph
    extract remains available via EMPIRE_COGNIFY_FULL=1 / --mode full.
    """
    from cognee.api.v1.cognify.cognify import get_default_tasks
    from cognee.modules.pipelines import run_pipeline
    from cognee.modules.pipelines.layers.pipeline_execution_mode import get_pipeline_executor

    tasks = await get_default_tasks(custom_prompt=WIKI_GRAPH_PROMPT)
    skip_names = {"summarize_text", "extract_dlt_fk_edges"}
    # Keep extract_graph_and_summarize for full-ish fast path (graph + vectors).
    tasks = [
        t
        for t in tasks
        if getattr(getattr(t, "executable", None), "__name__", "") not in skip_names
    ]
    if len(tasks) < 3:
        raise RuntimeError(
            f"EMPIRE fast cognify: expected >=3 tasks after filtering, got {len(tasks)}"
        )

    pipeline_executor_func = get_pipeline_executor(run_in_background=False)
    await pipeline_executor_func(
        pipeline=run_pipeline,
        tasks=tasks,
        datasets=dataset,
        incremental_loading=True,
        use_pipeline_cache=False,
        pipeline_name="cognify_pipeline",
        data_per_batch=1,
    )


async def cognify_dataset(dataset: str) -> None:
    """Run one cognify pass over a whole dataset (chunks + embeddings + graph).

    Cognee 0.5.x only creates the searchable vector collections during cognify, so this
    must run for BOTH fast and full ingests. Doing it once per batch (instead of per file)
    is far cheaper than calling cognify inside every remember().

    Fast path (default): skip summarize_text + wiki graph prompt + schema/retry patches.
    Set EMPIRE_COGNIFY_SKIP_SUMMARIZE=0 to restore stock summarize.
    Set EMPIRE_COGNIFY_FULL=1 for stock cognify (schema/retry patches still apply).
    """

    async def _run() -> None:
        cognee = _cognee_module()
        # data_per_batch=1 serializes data-item pipelines: Cognee's default (20 in parallel)
        # floods local SQLite with concurrent writers -> "database is locked". One at a time
        # is the reliable choice for the single-writer SQLite backend.
        if _env_flag("EMPIRE_COGNIFY_FULL", default=False):
            await cognee.cognify(datasets=dataset, data_per_batch=1)
            return

        if _env_flag("EMPIRE_COGNIFY_SKIP_SUMMARIZE", default=True):
            await _cognify_fast(cognee, dataset)
            return

        await cognee.cognify(
            datasets=dataset,
            custom_prompt=WIKI_GRAPH_PROMPT,
            data_per_batch=1,
        )

    await run_with_cognee_lock(_run)


async def improve(dataset: str = "mock") -> None:
    async def _run() -> None:
        cognee = _cognee_module()
        try:
            await cognee.memify(dataset=dataset)
        except Exception:
            return

    await run_with_cognee_lock(_run)


async def forget(dataset: str = "mock") -> bool:
    async def _run() -> bool:
        cognee = _cognee_module()
        datasets = await cognee.datasets.list_datasets()
        target = next(
            (
                item
                for item in datasets
                if _normalized_key(_dataset_field(item, "name")) == _normalized_key(dataset)
            ),
            None,
        )
        target_id = _dataset_field(target, "id") if target is not None else None
        if not target_id:
            return False
        await cognee.datasets.empty_dataset(dataset_id=target_id)
        remaining = await cognee.datasets.list_datasets()
        if any(
            _normalized_key(_dataset_field(item, "name")) == _normalized_key(dataset)
            for item in remaining
        ):
            raise RuntimeError(f"Cognee dataset still exists after forget: {dataset}")
        return True

    return await run_with_cognee_lock(_run)
