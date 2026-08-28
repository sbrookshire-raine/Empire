"""One-time, read-only export of Weaviate wikichunk collections to Markdown staging.

The Weaviate v2 archive at D:\\weaviate_v2_archive is a raw binary DB, not Markdown. To read
its already-chunked data without adding Weaviate as a runtime dependency, the user boots a
*temporary* Weaviate Docker container against the archive; this script queries it read-only
over the REST API and dumps each object to a Markdown file with frontmatter. Those files then
route through the normal wiki ingestion path. Weaviate is shut down permanently afterward.

Usage:
    python -m pipeline.weaviate_export --collection wikichunk --limit 500
    python -m pipeline.wiki_ingest --export-dir mock_data_ingest/wiki_export/wikichunk ...

This performs NO writes to Weaviate or the archive.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import httpx

from pipeline.config import ROOT

DEFAULT_WEAVIATE_URL = "http://localhost:8080"
# Heavy dump lands on the external 4TB drive (I:), never C:/OneDrive.
DEFAULT_OUT = Path(os.environ.get("WEAVIATE_DUMP_DIR", r"I:\EMPIRE_DATA\weaviate_dump"))
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")


def _safe_name(value: str, fallback: str) -> str:
    cleaned = _SAFE.sub("_", value).strip("_")
    return (cleaned or fallback)[:120]


def _auth_headers(api_key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {api_key}"} if api_key else {}


def check_weaviate(base_url: str) -> tuple[bool, str]:
    try:
        response = httpx.get(f"{base_url}/v1/.well-known/ready", timeout=5.0)
        if response.status_code < 300:
            return True, "ready"
        return False, f"HTTP {response.status_code}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def _derive_year(snapshot_id: str) -> str:
    sid = str(snapshot_id or "").strip()
    if len(sid) >= 4 and sid[:4].isdigit():
        return sid[:4]
    return ""


def _pick_text(props: dict) -> str:
    for key in ("text", "content", "chunk", "body", "passage"):
        if isinstance(props.get(key), str) and props[key].strip():
            return props[key]
    return json.dumps(props, ensure_ascii=False, indent=2)


def _pick_title(props: dict, fallback: str) -> str:
    for key in ("title", "page_title", "article", "name"):
        if isinstance(props.get(key), str) and props[key].strip():
            return props[key].strip()
    return fallback


def _to_markdown(
    obj: dict,
    collection: str,
    *,
    snapshot_id_override: str = "",
    snapshot_year_override: str = "",
) -> tuple[str, str]:
    obj_id = str(obj.get("id", ""))
    props = obj.get("properties", {}) or {}
    title = _pick_title(props, obj_id or "chunk")
    text = _pick_text(props)
    external_id = f"weaviate:{collection}:{obj_id}"

    # snapshot_id drives the Truth-Drift year. Prefer the object's own value, else the
    # override (used to tag an unlabeled collection, e.g. base wikichunk -> 2017).
    snapshot_id = str(props.get("snapshot_id", "")).strip() or snapshot_id_override
    snapshot_year = snapshot_year_override or _derive_year(snapshot_id)
    doc_id = str(props.get("doc_id", "")).strip() or external_id
    page_id = str(props.get("page_id", "")).strip()
    body_sha = str(props.get("body_sha256", "")).strip()
    corpus_rel_path = str(props.get("corpus_rel_path", "")).strip()
    chunk_index = props.get("chunk_index")

    fm = [
        "---",
        "source_type: wikipedia",
        f"external_id: {json.dumps(external_id)}",
        f"doc_id: {json.dumps(doc_id)}",
        f"title: {json.dumps(title)}",
    ]
    if page_id:
        fm.append(f"page_id: {json.dumps(page_id)}")
    if snapshot_id:
        fm.append(f"snapshot_id: {json.dumps(snapshot_id)}")
    if snapshot_year:
        fm.append(f"snapshot_year: {json.dumps(snapshot_year)}")
    if isinstance(chunk_index, int):
        fm.append(f"chunk_index: {chunk_index}")
    if body_sha:
        fm.append(f"body_sha256: {json.dumps(body_sha)}")
    if corpus_rel_path:
        fm.append(f"corpus_rel_path: {json.dumps(corpus_rel_path)}")
    fm.append(f"origin: weaviate/{collection}")
    fm.append("---")

    lines = [*fm, f"# {title}", "", text]

    ci = chunk_index if isinstance(chunk_index, int) else 0
    stem = _safe_name(f"{doc_id}_c{ci}", "chunk")
    filename = f"{stem}_{obj_id[:8]}.md"
    return filename, "\n".join(lines)


def export_collection(
    *,
    base_url: str,
    collection: str,
    limit: int,
    out_dir: Path,
    page_size: int = 100,
    api_key: str = "",
    snapshot_id: str = "",
    snapshot_year: str = "",
    out_subdir: str = "",
) -> dict:
    ready, detail = check_weaviate(base_url)
    if not ready:
        raise RuntimeError(
            f"Weaviate not reachable at {base_url} ({detail}). Boot the temporary Docker "
            "container against D:\\weaviate_v2_archive first."
        )

    # Read-only discipline: this function issues ONLY GET requests (no writes/schema changes).
    target = out_dir / _safe_name(out_subdir or collection, "collection")
    target.mkdir(parents=True, exist_ok=True)

    headers = _auth_headers(api_key)
    exported = 0
    after: str | None = None
    # Progress every N files to stderr so redirected .err.log grows during multi-hour dumps.
    progress_every = max(1, int(os.environ.get("WEAVIATE_EXPORT_PROGRESS_EVERY", "1000")))
    with httpx.Client(base_url=base_url, timeout=60.0, headers=headers) as client:
        while True:
            params: dict[str, str | int] = {"class": collection, "limit": page_size}
            if after:
                params["after"] = after
            response = client.get("/v1/objects", params=params)
            response.raise_for_status()
            objects = response.json().get("objects", [])
            if not objects:
                break
            for obj in objects:
                filename, content = _to_markdown(
                    obj,
                    collection,
                    snapshot_id_override=snapshot_id,
                    snapshot_year_override=snapshot_year,
                )
                (target / filename).write_text(content, encoding="utf-8")
                exported += 1
                after = str(obj.get("id", "")) or after
                if exported % progress_every == 0:
                    print(
                        f"progress: exported={exported} last_id={after} out={target}",
                        file=sys.stderr,
                        flush=True,
                    )
                if 0 < limit <= exported:
                    break
            if 0 < limit <= exported:
                break

    return {
        "collection": collection,
        "exported": exported,
        "out_dir": str(target),
        "snapshot_year": snapshot_year or "(from object snapshot_id)",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="One-time read-only Weaviate -> Markdown export")
    parser.add_argument("--collection", required=True, help="Weaviate class, e.g. WikiChunk, WikiChunk2021, WikiChunk2026")
    parser.add_argument("--url", default=DEFAULT_WEAVIATE_URL, help="Temporary Weaviate REST URL")
    parser.add_argument("--limit", type=int, default=0, help="Max objects (0 = all)")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Output staging directory")
    parser.add_argument("--out-subdir", default="", help="Subfolder name under --out (default: collection)")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument(
        "--api-key",
        default=os.environ.get("WEAVIATE_API_KEY", ""),
        help="Bearer API key (archive has anonymous access disabled)",
    )
    parser.add_argument(
        "--snapshot-id",
        default="",
        help="Force snapshot_id when the collection lacks one (e.g. 20170301 for base wikichunk)",
    )
    parser.add_argument(
        "--snapshot-year",
        default="",
        help="Force snapshot_year (e.g. 2017); otherwise derived from snapshot_id",
    )
    args = parser.parse_args()

    try:
        result = export_collection(
            base_url=args.url.rstrip("/"),
            collection=args.collection,
            limit=args.limit,
            out_dir=Path(args.out),
            page_size=args.page_size,
            api_key=args.api_key,
            snapshot_id=args.snapshot_id,
            snapshot_year=args.snapshot_year,
            out_subdir=args.out_subdir,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Exported {result['exported']} objects from {result['collection']} -> {result['out_dir']}")
    print("__WEAVIATE_EXPORT__" + json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
