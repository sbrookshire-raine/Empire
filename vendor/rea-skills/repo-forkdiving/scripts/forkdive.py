#!/usr/bin/env python3
"""Forkdive: enumerate a repository's fork network and derivative projects.

Read-only. Uses a layered set of sources so a GitHub API rate limit does not
stop the sweep:

  1. GitHub REST API   -- richest (forks, compare). 60 req/hr unauthenticated,
                          5000 with GITHUB_TOKEN.
  2. ungh.cc           -- unlimited cached proxy. No forks/compare endpoints.
  3. GitHub HTML       -- works when the API is exhausted. Stars, fork list.
  4. git ls-remote     -- no rate limit at all. Branch/ref enumeration.

Usage:
  python3 forkdive.py OWNER/REPO                 # full sweep
  python3 forkdive.py OWNER/REPO --forks-only
  python3 forkdive.py OWNER/REPO --derivatives-only
  python3 forkdive.py OWNER/REPO --json > out.json
  python3 forkdive.py OWNER/REPO --source html   # force a source

Never prints credentials. Only reads public metadata.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
UNGH = "https://ungh.cc"
HTML = "https://github.com"

RATE = {"core": None, "search": None, "warned": False}
# Which source actually served each result, for honest provenance.
SOURCE_USED = {}


def _headers():
    h = {"Accept": "application/vnd.github+json",
         "User-Agent": "forkdive/1.1"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h


def _note_rate(kind, remaining):
    if remaining is None:
        return
    try:
        RATE[kind] = int(remaining)
    except (TypeError, ValueError):
        return
    if RATE[kind] <= 2 and not RATE["warned"]:
        RATE["warned"] = True
        sys.stderr.write(
            f"WARNING: GitHub {kind} rate limit nearly exhausted "
            f"({RATE[kind]} left). Falling back to ungh.cc / HTML / git.\n")


def api(path, params=None, retries=2, kind="core"):
    """GET a GitHub API path. Returns (data, rate_remaining) or (None, None)."""
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=_headers())
            with urllib.request.urlopen(req, timeout=30) as r:
                remaining = r.headers.get("X-RateLimit-Remaining")
                _note_rate(kind, remaining)
                return json.loads(r.read().decode()), remaining
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, None
            if e.code in (403, 429) and attempt < retries - 1:
                time.sleep(2)
                continue
            return None, None
        except Exception:  # noqa: BLE001
            if attempt < retries - 1:
                time.sleep(2)
                continue
            return None, None
    return None, None


def ungh(path, retries=2):
    """GET an ungh.cc path. Unlimited, cached, no auth. Returns data or None."""
    url = UNGH + path
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "forkdive/1.1"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception:  # noqa: BLE001
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
    return None


def fetch_html(url, retries=2):
    """Fetch a GitHub HTML page. Works when the REST API is rate-limited."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 (compatible; "
                                            "forkdive/1.1)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:  # noqa: BLE001
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
    return None


def git_refs(repo_url, heads_only=True):
    """Enumerate refs via git ls-remote. No API, no rate limit."""
    cmd = ["git", "ls-remote"]
    if heads_only:
        cmd.append("--heads")
    cmd.append(repo_url)
    try:
        out = subprocess.run(cmd, capture_output=True, text=True,
                             timeout=90)
        if out.returncode != 0:
            return None
        refs = []
        for line in out.stdout.strip().splitlines():
            parts = line.split("\t")
            if len(parts) == 2:
                refs.append({"sha": parts[0], "ref": parts[1]})
        return refs
    except Exception:  # noqa: BLE001
        return None


def repo_meta(full_name):
    """Repository metadata, trying API then ungh then HTML."""
    d, _ = api(f"/repos/{full_name}")
    if d:
        SOURCE_USED["meta"] = "github-api"
        return {
            "full_name": d.get("full_name"),
            "description": d.get("description"),
            "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"),
            "open_issues": d.get("open_issues_count"),
            "created_at": (d.get("created_at") or "")[:10],
            "pushed_at": (d.get("pushed_at") or "")[:10],
            "license": (d.get("license") or {}).get("spdx_id"),
            "topics": d.get("topics") or [],
            "homepage": d.get("homepage"),
            "is_fork": d.get("fork"),
            "parent": (d.get("parent") or {}).get("full_name"),
            "archived": d.get("archived"),
            "source": "github-api",
        }

    u = ungh(f"/repos/{full_name}")
    if u and u.get("repo"):
        r = u["repo"]
        SOURCE_USED["meta"] = "ungh.cc"
        return {
            "full_name": r.get("repo"),
            "description": r.get("description"),
            "stars": r.get("stars"),
            "forks": r.get("forks"),
            "open_issues": None,
            "created_at": (r.get("createdAt") or "")[:10],
            "pushed_at": (r.get("pushedAt") or "")[:10],
            "license": None,
            "topics": [],
            "homepage": None,
            "is_fork": None,
            "parent": None,
            "archived": None,
            "source": "ungh.cc (cached; counts may lag)",
        }

    html = fetch_html(f"{HTML}/{full_name}")
    if html:
        stars = re.search(r'"stargazerCount":(\d+)', html)
        forks = re.search(r'"forkCount":(\d+)', html)
        desc = re.search(r'<meta name="description" content="([^"]{0,300})',
                         html)
        SOURCE_USED["meta"] = "github-html"
        return {
            "full_name": full_name,
            "description": (desc.group(1) if desc else None),
            "stars": int(stars.group(1)) if stars else None,
            "forks": int(forks.group(1)) if forks else None,
            "open_issues": None,
            "created_at": None,
            "pushed_at": None,
            "license": None,
            "topics": [],
            "homepage": None,
            "is_fork": None,
            "parent": None,
            "archived": None,
            "source": "github-html (partial)",
        }
    return None


def list_forks(full_name, sort="stargazers", per_page=30):
    """Forks via the API, falling back to HTML scraping when rate-limited."""
    d, _ = api(f"/repos/{full_name}/forks",
               {"sort": sort, "per_page": per_page})
    if isinstance(d, list):
        SOURCE_USED["forks"] = "github-api"
        return [{
            "full_name": x.get("full_name"),
            "stars": x.get("stargazers_count"),
            "created_at": (x.get("created_at") or "")[:10],
            "pushed_at": (x.get("pushed_at") or "")[:10],
            "size_kb": x.get("size"),
            "default_branch": x.get("default_branch"),
            "description": x.get("description"),
        } for x in d]

    # HTML fallback: the forks page lists fork owners.
    html = fetch_html(f"{HTML}/{full_name}/forks"
                      f"?include=active&sort={sort}")
    if not html:
        return []
    SOURCE_USED["forks"] = "github-html (owners only, no star counts)"
    short = full_name.split("/")[-1]
    owners = set()
    for m in re.finditer(r'href="/([A-Za-z0-9_.-]+)/' + re.escape(short) + r'"',
                         html):
        owners.add(m.group(1))
    # The upstream itself appears in its own fork listing; drop it.
    owners.discard(full_name.split("/")[0])
    return [{"full_name": f"{o}/{short}",
             "stars": None, "created_at": None, "pushed_at": None,
             "size_kb": None, "default_branch": None,
             "description": None} for o in sorted(owners)]


def git_compare(upstream, fork, branch=None, workdir=None):
    """Compute ahead/behind and the fork's own commits using git alone.

    No GitHub API, no rate limit. Clones upstream blobless, fetches the fork's
    refs into it, then counts divergence locally. Slower than the API but
    unlimited and gives full commit history and diffstat.
    """
    import tempfile
    tmp = workdir or tempfile.mkdtemp(prefix="forkdive-git-")
    up_dir = os.path.join(tmp, "up.git")
    try:
        r = subprocess.run(
            ["git", "clone", "--bare", "--filter=blob:none", "--quiet",
             f"https://github.com/{upstream}.git", up_dir],
            capture_output=True, text=True, timeout=600)
        if r.returncode != 0:
            return None

        r = subprocess.run(
            ["git", "fetch", "--quiet", "--filter=blob:none",
             f"https://github.com/{fork}.git",
             "refs/heads/*:refs/remotes/fork/*"],
            capture_output=True, text=True, cwd=up_dir, timeout=600)
        if r.returncode != 0:
            return None

        # Resolve the fork's branch: explicit, else develop/main/master, else first.
        refs = subprocess.run(
            ["git", "for-each-ref", "refs/remotes/fork",
             "--format=%(refname)"],
            capture_output=True, text=True, cwd=up_dir).stdout.split()
        if not refs:
            return None
        if branch:
            cand = f"refs/remotes/fork/{branch}"
            if cand not in refs:
                cand = None
        else:
            cand = None
        if not cand:
            for pref in ("develop", "main", "master"):
                if f"refs/remotes/fork/{pref}" in refs:
                    cand = f"refs/remotes/fork/{pref}"
                    break
        if not cand:
            cand = refs[0]

        # Upstream base ref.
        base = None
        for pref in ("main", "master", "develop"):
            chk = subprocess.run(
                ["git", "rev-parse", "--verify", "--quiet",
                 f"refs/heads/{pref}"],
                capture_output=True, text=True, cwd=up_dir)
            if chk.returncode == 0:
                base = f"refs/heads/{pref}"
                break
        if not base:
            return None

        def count(a, b):
            out = subprocess.run(
                ["git", "rev-list", "--count", a, b],
                capture_output=True, text=True, cwd=up_dir)
            try:
                return int(out.stdout.strip())
            except ValueError:
                return None

        ahead = count(cand, f"^{base}")
        behind = count(base, f"^{cand}")

        log = subprocess.run(
            ["git", "log", "--oneline", "--no-decorate", f"{cand}", f"^{base}"],
            capture_output=True, text=True, cwd=up_dir).stdout
        commits = []
        for line in log.strip().splitlines()[:20]:
            parts = line.split(" ", 1)
            if len(parts) == 2:
                commits.append({"sha": parts[0][:10],
                                "message": parts[1][:120]})

        stat = subprocess.run(
            ["git", "diff", "--shortstat", f"{base}...{cand}"],
            capture_output=True, text=True, cwd=up_dir).stdout.strip()
        files_changed = None
        m = re.search(r"(\d+) files? changed", stat)
        if m:
            files_changed = int(m.group(1))

        status = ("diverged" if ahead and behind
                  else "ahead" if ahead
                  else "behind" if behind
                  else "identical")
        return {
            "status": status,
            "ahead_by": ahead,
            "behind_by": behind,
            "total_commits": ahead,
            "files_changed": files_changed,
            "commits": commits,
            "source": "git (no rate limit)",
        }
    except Exception:  # noqa: BLE001
        return None
    finally:
        if workdir is None:
            import shutil
            shutil.rmtree(tmp, ignore_errors=True)


def compare_fork(upstream, fork, branch=None, allow_git=True):
    """Ahead/behind vs upstream. API first, then a git-only fallback."""
    owner, repo = fork.split("/", 1)
    if branch is None:
        meta, _ = api(f"/repos/{fork}")
        branch = (meta or {}).get("default_branch")
        if not branch:
            u = ungh(f"/repos/{fork}")
            branch = ((u or {}).get("repo") or {}).get("defaultBranch")
    head = f"{owner}:{repo}:{branch or 'main'}"
    d, _ = api(f"/repos/{upstream}/compare/main...{head}")
    if d:
        commits = []
        for c in (d.get("commits") or [])[:20]:
            commits.append({
                "sha": (c.get("sha") or "")[:10],
                "message": (c.get("commit", {}).get("message") or "").split("\n")[0][:120],
                "author": (c.get("commit", {}).get("author", {}) or {}).get("name"),
                "date": (c.get("commit", {}).get("author", {}) or {}).get("date", "")[:10],
            })
        return {
            "status": d.get("status"),
            "ahead_by": d.get("ahead_by"),
            "behind_by": d.get("behind_by"),
            "total_commits": d.get("total_commits"),
            "files_changed": len(d.get("files") or []),
            "commits": commits,
            "source": "github-api",
        }
    if allow_git:
        return git_compare(upstream, fork, branch)
    return None


def search_derivatives(query, per_page=20):
    d, _ = api("/search/repositories",
               {"q": query, "sort": "stars", "order": "desc",
                "per_page": per_page}, kind="search")
    if not isinstance(d, dict):
        return []
    return [{
        "full_name": x.get("full_name"),
        "stars": x.get("stargazers_count"),
        "forks": x.get("forks_count"),
        "description": (x.get("description") or "")[:160],
        "created_at": (x.get("created_at") or "")[:10],
        "pushed_at": (x.get("pushed_at") or "")[:10],
        "topics": x.get("topics") or [],
        "is_fork": x.get("fork"),
        "parent": (x.get("parent") or {}).get("full_name"),
    } for x in d.get("items", [])]


def _name_matches(text, name):
    """True when `name` appears as a standalone token, not inside a longer word.

    Prevents 'rea' from matching 'react', 'real', 'reach', and similar.
    """
    if not text:
        return False
    return re.search(rf"(?<![a-z0-9]){re.escape(name)}(?![a-z0-9])",
                     text, re.IGNORECASE) is not None


def find_curated_lists(owner_repo, name):
    """Look for awesome-lists / case collections that aggregate this project."""
    queries = [
        f"awesome {name} in:name,description",
        f"{name} cases in:name,description",
        f"{name} reverse engineering in:name,description",
    ]
    seen, out = set(), []
    for q in queries:
        for r in search_derivatives(q, per_page=15):
            fn = r["full_name"]
            if fn in seen or fn.lower() == owner_repo.lower():
                continue
            haystack = f"{fn} {r.get('description') or ''} " \
                       f"{' '.join(r.get('topics') or [])}"
            if not _name_matches(haystack, name):
                continue
            seen.add(fn)
            out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser(description="Forkdive a GitHub repository.")
    ap.add_argument("repo", help="OWNER/REPO")
    ap.add_argument("--forks-only", action="store_true")
    ap.add_argument("--derivatives-only", action="store_true")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--compare-top", type=int, default=5)
    ap.add_argument("--source", choices=["auto", "api", "ungh", "html", "git"],
                    default="auto",
                    help="force a data source instead of the layered fallback")
    args = ap.parse_args()

    owner_repo = args.repo.strip().strip("/")
    name = owner_repo.split("/")[-1]

    # --source forces one path; auto uses the layered fallback.
    if args.source == "git":
        result = {"repo": owner_repo, "meta": repo_meta(owner_repo)}
        refs = git_refs(f"https://github.com/{owner_repo}.git")
        if refs:
            SOURCE_USED["refs"] = "git ls-remote (forced)"
            result["upstream_refs"] = {
                "count": len(refs),
                "sample": [r["ref"] for r in refs[:10]],
            }
        result["rate_limit"] = {k: v for k, v in RATE.items()
                                if k != "warned"}
        result["sources_used"] = SOURCE_USED
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"# Forkdive (git only): {owner_repo}")
            print(f"branches: {(result.get('upstream_refs') or {}).get('count')}")
            for r in (result.get("upstream_refs") or {}).get("sample", []):
                print(f"  {r}")
        return

    result = {"repo": owner_repo, "meta": repo_meta(owner_repo)}

    if not args.derivatives_only:
        forks_star = list_forks(owner_repo, "stargazers", 30)
        forks_new = list_forks(owner_repo, "newest", 15)
        result["forks"] = {"by_stars": forks_star, "newest": forks_new}

        comparisons = []
        for f in forks_star[:args.compare_top]:
            cmp = compare_fork(owner_repo, f["full_name"])
            if cmp:
                comparisons.append({"fork": f["full_name"], **cmp})
        result["fork_comparisons"] = comparisons
        if any(c.get("source", "").startswith("git") for c in comparisons):
            SOURCE_USED["compare"] = "git (no rate limit)"

        # git ls-remote works with no API at all; useful when the API is spent.
        refs = git_refs(f"https://github.com/{owner_repo}.git")
        if refs:
            SOURCE_USED["refs"] = "git ls-remote (no rate limit)"
            result["upstream_refs"] = {
                "count": len(refs),
                "sample": [r["ref"] for r in refs[:10]],
            }

    if not args.forks_only:
        result["derivatives"] = search_derivatives(
            f"{name} reverse engineering in:name,description")
        result["curated_lists"] = find_curated_lists(owner_repo, name)

    result["rate_limit"] = {k: v for k, v in RATE.items() if k != "warned"}
    result["sources_used"] = SOURCE_USED

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    m = result["meta"]
    print(f"# Forkdive: {owner_repo}")
    if not m:
        print()
        print("ERROR: could not read repository metadata from any source.")
        print("Tried: GitHub API, ungh.cc, GitHub HTML.")
        print("Set GITHUB_TOKEN to raise the API limit, then re-run.")
        return

    print(f"stars={m.get('stars')} forks={m.get('forks')} "
          f"created={m.get('created_at')} pushed={m.get('pushed_at')} "
          f"license={m.get('license')}")
    print(f"desc: {m.get('description')}")
    print(f"source: {m.get('source')}")
    print()

    if "forks" in result:
        print("## Forks by stars")
        for f in result["forks"]["by_stars"][:15]:
            stars = f"{f['stars']:>5}" if f["stars"] is not None else "    ?"
            print(f"  {stars}  {f['full_name']:<45} "
                  f"pushed={f['pushed_at'] or '?'}")
        print("\n## Newest forks")
        for f in result["forks"]["newest"][:8]:
            print(f"  {f['full_name']:<45} created={f['created_at'] or '?'}")
        print("\n## Fork divergence (vs upstream)")
        for c in result.get("fork_comparisons", []):
            print(f"  {c['fork']}: {c['status']} "
                  f"ahead={c['ahead_by']} behind={c['behind_by']} "
                  f"files={c['files_changed']}")
            for cm in c["commits"][:3]:
                print(f"      {cm['sha']} {cm['message'][:70]}")
        if result.get("upstream_refs"):
            print(f"\n## Upstream refs (git ls-remote): "
                  f"{result['upstream_refs']['count']} branches")
        print()

    if "derivatives" in result:
        print("## Derivative projects (search)")
        for r in result["derivatives"][:12]:
            print(f"  {r['stars']:>5}  {r['full_name']:<42} "
                  f"{r['description'][:60]}")
        print()

    if "curated_lists" in result:
        print("## Curated lists / case collections")
        for r in result["curated_lists"][:12]:
            print(f"  {r['stars']:>5}  {r['full_name']:<42} "
                  f"{r['description'][:60]}")
        print()

    print("## Sources used")
    for k, v in SOURCE_USED.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
