"""Container scout — Docker Hub search/detail + local empire-* Docker status.

Caches markdown under Thought Experiments/container_cache. Never auto-promotes
to Cognee. Never pulls or runs images.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_CONTAINER_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\container_cache",
    )
)
HUB_BASE = "https://hub.docker.com"
USER_AGENT = "EMPIRE-ContainerScout/1.0 (+local; Architect workbench)"
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")
DEFAULT_TIMEOUT = float(os.environ.get("EMPIRE_HUB_TIMEOUT", "25"))
# Gentle pause between Hub pages when listing many tags
_RATE_PAUSE_SEC = 0.15


def _safe_name(value: str, fallback: str = "hub") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(
        prefix="container-", suffix=".md", dir=str(path.parent)
    )
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp_path, path)
    except Exception:
        tmp_path.unlink(missing_ok=True)
        raise


def _hub_get(path: str, *, params: dict[str, Any] | None = None, timeout: float = DEFAULT_TIMEOUT) -> dict[str, Any]:
    query = f"?{urlencode(params)}" if params else ""
    url = f"{HUB_BASE}{path}{query}"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:  # noqa: S310 — public Hub API
            raw = resp.read(4_000_000)
            status = int(getattr(resp, "status", 200) or 200)
    except HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8", errors="replace")[:400]
        except Exception:
            pass
        return {"ok": False, "error": f"HTTP {exc.code}", "detail": body, "url": url}
    except URLError as exc:
        return {"ok": False, "error": str(exc.reason or exc), "url": url}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "url": url}

    try:
        data = json.loads(raw.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        return {"ok": False, "error": f"invalid JSON: {exc}", "url": url}

    return {"ok": True, "status": status, "url": url, "data": data}


def _repo_slug(namespace: str | None, name: str) -> str:
    ns = (namespace or "").strip()
    nm = (name or "").strip()
    if not nm:
        return ""
    if ns and ns not in {"_", "library"}:
        return f"{ns}/{nm}"
    return nm


def search_hub(
    query: str,
    *,
    limit: int = 10,
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
) -> dict[str, Any]:
    cleaned = (query or "").strip()
    if not cleaned:
        return {"ok": False, "error": "query required"}

    page_size = max(1, min(int(limit or 10), 25))
    fetched = _hub_get(
        "/v2/search/repositories/",
        params={"query": cleaned, "page_size": page_size, "page": 1},
    )
    if not fetched.get("ok"):
        return fetched

    payload = fetched.get("data") or {}
    results_raw = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(results_raw, list):
        return {"ok": False, "error": "unexpected Hub search shape", "raw_keys": list(payload) if isinstance(payload, dict) else None}

    results: list[dict[str, Any]] = []
    for item in results_raw[:page_size]:
        if not isinstance(item, dict):
            continue
        ns = item.get("repo_owner") or item.get("namespace")
        name = str(item.get("repo_name") or item.get("name") or "")
        slug = _repo_slug(str(ns) if ns else None, name)
        if not slug:
            continue
        results.append(
            {
                "name": slug,
                "description": (item.get("short_description") or item.get("description") or "")[:500],
                "stars": item.get("star_count"),
                "pulls": item.get("pull_count"),
                "official": bool(item.get("is_official")),
                "automated": bool(item.get("is_automated")),
                "last_updated": item.get("last_updated") or item.get("updated_at"),
                "hub_url": f"https://hub.docker.com/r/{quote(slug)}",
            }
        )

    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    stem = _safe_name(f"search_{cleaned}_{stamp}")
    path = out_dir / f"{stem}.md"
    path_str = ""

    if write_files:
        lines = [
            "---",
            *provenance_fields(
                source="docker_hub",
                kind="hub_search",
                tool="container_scout_search",
                limb="container_scout",
                extra={"query": cleaned, "result_count": len(results), "architect_note": note or ""},
            ),
            "---",
            f"# Docker Hub search: {cleaned}",
            "",
            f"Results: {len(results)} (limit {page_size}). **Scratch only** — do not auto-ingest to Cognee.",
            "",
        ]
        for row in results:
            lines.extend(
                [
                    f"## `{row['name']}`",
                    "",
                    f"- Official: {row['official']}",
                    f"- Stars: {row.get('stars')} · Pulls: {row.get('pulls')}",
                    f"- Updated: {row.get('last_updated') or 'n/a'}",
                    f"- Hub: {row.get('hub_url')}",
                    "",
                    (row.get("description") or "(no description)"),
                    "",
                ]
            )
        lines.append(
            provenance_markdown_footer(
                source="docker_hub",
                tool="container_scout_search",
                limb="container_scout",
            )
        )
        try:
            _atomic_write(path, "\n".join(lines))
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc), "query": cleaned}

    return {
        "ok": True,
        "query": cleaned,
        "count": len(results),
        "results": results,
        "path": path_str,
        "note": (
            f"Cached under {path_str}. Promote to Cognee only after triage (cognee_remember)."
            if path_str
            else "Search completed without writing cache."
        ),
    }


def _split_repo(repo: str) -> tuple[str, str] | None:
    cleaned = (repo or "").strip().strip("/")
    if not cleaned:
        return None
    if "/" in cleaned:
        ns, name = cleaned.split("/", 1)
        ns, name = ns.strip(), name.strip()
        if not ns or not name or "/" in name:
            return None
        return ns, name
    # Official library images on Hub live under library/
    return "library", cleaned


def detail_hub(
    repo: str,
    *,
    tag_limit: int = 15,
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
) -> dict[str, Any]:
    parts = _split_repo(repo)
    if not parts:
        return {"ok": False, "error": "repo required (e.g. semitechnologies/weaviate or redis)"}
    namespace, name = parts
    slug = name if namespace == "library" else f"{namespace}/{name}"

    meta = _hub_get(f"/v2/repositories/{quote(namespace)}/{quote(name)}/")
    if not meta.get("ok"):
        return meta

    repo_data = meta.get("data") if isinstance(meta.get("data"), dict) else {}
    time.sleep(_RATE_PAUSE_SEC)
    tags_resp = _hub_get(
        f"/v2/repositories/{quote(namespace)}/{quote(name)}/tags",
        params={"page_size": max(1, min(int(tag_limit or 15), 50)), "ordering": "last_updated", "page": 1},
    )
    tags: list[dict[str, Any]] = []
    if tags_resp.get("ok"):
        tag_payload = tags_resp.get("data") or {}
        for item in (tag_payload.get("results") if isinstance(tag_payload, dict) else None) or []:
            if not isinstance(item, dict):
                continue
            images = item.get("images") if isinstance(item.get("images"), list) else []
            arches = sorted(
                {
                    str(img.get("architecture") or "")
                    for img in images
                    if isinstance(img, dict) and img.get("architecture")
                }
            )
            digest = ""
            for img in images:
                if isinstance(img, dict) and img.get("digest"):
                    digest = str(img.get("digest"))
                    break
            tags.append(
                {
                    "name": item.get("name"),
                    "last_updated": item.get("last_updated"),
                    "digest": digest or item.get("digest") or "",
                    "architectures": arches,
                    "size": item.get("full_size") or item.get("size"),
                }
            )
    else:
        # Still return repo metadata if tags fail
        tags_error = tags_resp.get("error")

    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    stem = _safe_name(f"detail_{slug.replace('/', '_')}_{stamp}")
    path = out_dir / f"{stem}.md"
    path_str = ""

    description = (repo_data.get("full_description") or repo_data.get("description") or "")[:4000]
    summary = {
        "name": slug,
        "namespace": namespace,
        "description": (repo_data.get("description") or "")[:500],
        "stars": repo_data.get("star_count"),
        "pulls": repo_data.get("pull_count"),
        "last_updated": repo_data.get("last_updated"),
        "hub_url": f"https://hub.docker.com/r/{quote(slug)}",
        "tags": tags,
    }

    if write_files:
        lines = [
            "---",
            *provenance_fields(
                source="docker_hub",
                kind="hub_detail",
                tool="container_scout_detail",
                limb="container_scout",
                extra={"repo": slug, "tag_count": len(tags), "architect_note": note or ""},
            ),
            "---",
            f"# Docker Hub: `{slug}`",
            "",
            f"- Stars: {summary.get('stars')} · Pulls: {summary.get('pulls')}",
            f"- Updated: {summary.get('last_updated') or 'n/a'}",
            f"- Hub: {summary.get('hub_url')}",
            "",
            "## Description",
            "",
            description or "(no description)",
            "",
            "## Recent tags",
            "",
        ]
        if tags:
            for tag in tags:
                arch = ", ".join(tag.get("architectures") or []) or "n/a"
                digest = (tag.get("digest") or "")[:24]
                lines.append(
                    f"- `{tag.get('name')}` · updated {tag.get('last_updated') or 'n/a'} · arch [{arch}]"
                    + (f" · digest `{digest}…`" if digest else "")
                )
        else:
            lines.append("_No tags returned (or Hub rate-limited)._")
        lines.append(
            provenance_markdown_footer(
                source="docker_hub",
                tool="container_scout_detail",
                limb="container_scout",
            )
        )
        try:
            _atomic_write(path, "\n".join(lines))
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc), "repo": slug}

    out: dict[str, Any] = {
        "ok": True,
        "repo": slug,
        "detail": summary,
        "path": path_str,
        "note": (
            f"Cached under {path_str}. Do not pull/run without an Architect Work Order."
            if path_str
            else "Detail fetched without writing cache."
        ),
    }
    if not tags_resp.get("ok"):
        out["tags_warning"] = tags_resp.get("error")
    return out


def docker_status(*, name_filter: str = "empire-") -> dict[str, Any]:
    """List local Docker containers matching EMPIRE naming (default empire-*)."""

    docker = shutil.which("docker")
    if not docker:
        return {
            "ok": False,
            "error": "docker CLI not found on PATH",
            "hint": "Install Docker Desktop or ensure docker.exe is available. EMPIRE Weaviate uses scripts/start-weaviate.ps1.",
            "containers": [],
        }

    fmt = "{{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
    try:
        proc = subprocess.run(
            [docker, "ps", "-a", "--format", fmt],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except FileNotFoundError:
        return {
            "ok": False,
            "error": "docker CLI not found on PATH",
            "containers": [],
        }
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "docker ps timed out", "containers": []}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc), "containers": []}

    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "docker ps failed").strip()
        return {
            "ok": False,
            "error": err[:800],
            "hint": "Docker Desktop may be stopped. Start it, or ignore if you only need Hub search.",
            "containers": [],
        }

    prefix = (name_filter or "empire-").strip().lower()
    containers: list[dict[str, str]] = []
    for line in (proc.stdout or "").splitlines():
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        cid, names, image, status = parts[0], parts[1], parts[2], parts[3]
        ports = parts[4] if len(parts) > 4 else ""
        name_l = names.lower()
        if prefix and prefix not in name_l:
            continue
        running = status.lower().startswith("up")
        containers.append(
            {
                "id": cid,
                "name": names,
                "image": image,
                "status": status,
                "ports": ports,
                "running": "true" if running else "false",
            }
        )

    return {
        "ok": True,
        "filter": prefix,
        "count": len(containers),
        "containers": containers,
        "note": (
            "Status only — use Start/Stop scripts (e.g. start-weaviate.ps1) to change lifecycle."
            if containers
            else f"No containers matching '{prefix}'. Docker is reachable."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE Container Scout (Docker Hub + local status)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_search = sub.add_parser("search", help="Search Docker Hub")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=10)
    p_search.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    p_search.add_argument("--no-write", action="store_true")
    p_search.add_argument("--note", default="")

    p_detail = sub.add_parser("detail", help="Repo detail + recent tags")
    p_detail.add_argument("repo")
    p_detail.add_argument("--tag-limit", type=int, default=15)
    p_detail.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR))
    p_detail.add_argument("--no-write", action="store_true")
    p_detail.add_argument("--note", default="")

    p_docker = sub.add_parser("docker-status", help="List local empire-* containers")
    p_docker.add_argument("--filter", default="empire-", dest="name_filter")

    args = parser.parse_args(argv)
    if args.cmd == "search":
        result = search_hub(
            args.query,
            limit=args.limit,
            cache_dir=Path(args.cache_dir),
            write_files=not args.no_write,
            note=args.note,
        )
    elif args.cmd == "detail":
        result = detail_hub(
            args.repo,
            tag_limit=args.tag_limit,
            cache_dir=Path(args.cache_dir),
            write_files=not args.no_write,
            note=args.note,
        )
    elif args.cmd == "docker-status":
        result = docker_status(name_filter=args.name_filter)
    else:
        # Exhaustive for future subcommands
        raise SystemExit(f"unknown command: {args.cmd}")

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
