"""GitHub scout — repository search + README excerpt cache.

Caches markdown under Thought Experiments/github_cache. Never auto-promotes
to Cognee. Never clones or installs repos.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from pipeline.provenance import provenance_fields, provenance_markdown_footer, utc_now_iso

DEFAULT_CACHE_DIR = Path(
    os.environ.get(
        "EMPIRE_GITHUB_CACHE_DIR",
        r"C:\Empire_Workbench\04_Thought_Experiments\github_cache",
    )
)
GITHUB_API = "https://api.github.com"
USER_AGENT = "EMPIRE-GitHubScout/1.0 (+local; Architect workbench)"
_SAFE = re.compile(r"[^A-Za-z0-9_.-]+")
DEFAULT_TIMEOUT = float(os.environ.get("EMPIRE_GITHUB_TIMEOUT", "25"))
README_MAX_CHARS = int(os.environ.get("EMPIRE_GITHUB_README_MAX", "8000"))


def _safe_name(value: str, fallback: str = "github") -> str:
    cleaned = _SAFE.sub("_", (value or "").strip()).strip("_")
    return (cleaned or fallback)[:100]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, tmp_name = tempfile.mkstemp(prefix="github-", suffix=".md", dir=str(path.parent))
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


def _github_headers() -> dict[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    }
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _github_get(path: str, *, timeout: float = DEFAULT_TIMEOUT) -> dict[str, Any]:
    url = f"{GITHUB_API}{path}"
    req = Request(url, headers=_github_headers())
    try:
        with urlopen(req, timeout=timeout) as resp:  # noqa: S310 — public GitHub API
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


def _split_repo(repo: str) -> tuple[str, str] | None:
    cleaned = (repo or "").strip().strip("/")
    if not cleaned or cleaned.count("/") != 1:
        return None
    owner, name = cleaned.split("/", 1)
    owner, name = owner.strip(), name.strip()
    if not owner or not name:
        return None
    return owner, name


def search_repos(
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

    page_size = max(1, min(int(limit or 10), 30))
    fetched = _github_get(
        f"/search/repositories?q={quote(cleaned)}&per_page={page_size}&sort=stars&order=desc"
    )
    if not fetched.get("ok"):
        return fetched

    payload = fetched.get("data") or {}
    items_raw = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items_raw, list):
        return {"ok": False, "error": "unexpected GitHub search shape"}

    results: list[dict[str, Any]] = []
    for item in items_raw[:page_size]:
        if not isinstance(item, dict):
            continue
        full_name = str(item.get("full_name") or "")
        if not full_name:
            continue
        license_info = item.get("license") if isinstance(item.get("license"), dict) else {}
        results.append(
            {
                "full_name": full_name,
                "description": (item.get("description") or "")[:500],
                "stars": item.get("stargazers_count"),
                "forks": item.get("forks_count"),
                "language": item.get("language"),
                "license": license_info.get("spdx_id") or license_info.get("name") or "",
                "updated_at": item.get("updated_at"),
                "html_url": item.get("html_url") or f"https://github.com/{full_name}",
                "topics": item.get("topics") if isinstance(item.get("topics"), list) else [],
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
                source="github_api",
                kind="github_search",
                tool="github_scout_search",
                limb="github_scout",
                extra={"query": cleaned, "result_count": len(results), "architect_note": note or ""},
            ),
            "---",
            f"# GitHub search: {cleaned}",
            "",
            f"Results: {len(results)} (limit {page_size}). **Scratch only** — do not auto-ingest to Cognee.",
            "",
        ]
        for row in results:
            topics = ", ".join(str(t) for t in (row.get("topics") or [])[:8])
            lines.extend(
                [
                    f"## `{row['full_name']}`",
                    "",
                    f"- Stars: {row.get('stars')} · Forks: {row.get('forks')}",
                    f"- Language: {row.get('language') or 'n/a'} · License: {row.get('license') or 'n/a'}",
                    f"- Updated: {row.get('updated_at') or 'n/a'}",
                    f"- URL: {row.get('html_url')}",
                ]
            )
            if topics:
                lines.append(f"- Topics: {topics}")
            lines.extend(["", (row.get("description") or "(no description)"), ""])
        lines.append(
            provenance_markdown_footer(
                source="github_api",
                tool="github_scout_search",
                limb="github_scout",
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
            f"Cached under {path_str}. Triage before forge or Cognee promote."
            if path_str
            else "Search completed without writing cache."
        ),
    }


def repo_readme(
    repo: str,
    *,
    cache_dir: Path | None = None,
    write_files: bool = True,
    note: str = "",
) -> dict[str, Any]:
    parts = _split_repo(repo)
    if not parts:
        return {"ok": False, "error": "repo required (owner/name)"}
    owner, name = parts
    slug = f"{owner}/{name}"

    fetched = _github_get(f"/repos/{quote(owner)}/{quote(name)}/readme")
    if not fetched.get("ok"):
        return fetched

    data = fetched.get("data") if isinstance(fetched.get("data"), dict) else {}
    encoding = str(data.get("encoding") or "")
    content_raw = data.get("content")
    if not isinstance(content_raw, str):
        return {"ok": False, "error": "README missing content", "repo": slug}

    try:
        decoded = base64.b64decode(content_raw).decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": f"README decode failed: {exc}", "repo": slug}

    excerpt = decoded[:README_MAX_CHARS]
    truncated = len(decoded) > len(excerpt)

    meta = _github_get(f"/repos/{quote(owner)}/{quote(name)}")
    repo_meta = meta.get("data") if meta.get("ok") and isinstance(meta.get("data"), dict) else {}

    out_dir = Path(cache_dir) if cache_dir else DEFAULT_CACHE_DIR
    stamp = utc_now_iso().replace(":", "").replace("+00:00", "Z")
    stem = _safe_name(f"readme_{slug}_{stamp}")
    path = out_dir / f"{stem}.md"
    path_str = ""

    if write_files:
        lines = [
            "---",
            *provenance_fields(
                source="github_api",
                kind="github_readme",
                tool="github_scout_readme",
                limb="github_scout",
                extra={"repo": slug, "architect_note": note or "", "truncated": truncated},
            ),
            "---",
            f"# README excerpt: `{slug}`",
            "",
            f"- Stars: {repo_meta.get('stargazers_count', 'n/a')}",
            f"- License: {(repo_meta.get('license') or {}).get('spdx_id', 'n/a') if isinstance(repo_meta.get('license'), dict) else 'n/a'}",
            f"- URL: {repo_meta.get('html_url') or f'https://github.com/{slug}'}",
            "",
            "## Excerpt",
            "",
            excerpt,
            "",
        ]
        if truncated:
            lines.append(f"*(truncated at {README_MAX_CHARS} chars)*")
            lines.append("")
        lines.append(
            provenance_markdown_footer(
                source="github_api",
                tool="github_scout_readme",
                limb="github_scout",
            )
        )
        try:
            _atomic_write(path, "\n".join(lines))
            path_str = str(path)
        except OSError as exc:
            return {"ok": False, "error": str(exc), "repo": slug}

    return {
        "ok": True,
        "repo": slug,
        "path": path_str,
        "truncated": truncated,
        "chars": len(excerpt),
        "summary": excerpt[:400].replace("\n", " "),
        "note": f"Cached under {path_str}" if path_str else "README fetched without cache write.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="EMPIRE GitHub scout")
    sub = parser.add_subparsers(dest="command", required=True)
    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--note", default="")
    readme = sub.add_parser("readme")
    readme.add_argument("repo")
    readme.add_argument("--note", default="")
    args = parser.parse_args(argv)

    if args.command == "search":
        result = search_repos(args.query, limit=args.limit, note=args.note)
    elif args.command == "readme":
        result = repo_readme(args.repo, note=args.note)
    else:
        raise SystemExit(f"unknown command: {args.command}")

    print(json.dumps(result, indent=2, default=str))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
