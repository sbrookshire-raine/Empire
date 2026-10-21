#!/usr/bin/env python3
"""Signal-based repository discovery.

Find repos worth forkdiving BEFORE you have a target repo. Two signals:

  1. Topic/keyword search ranked by forks (GitHub search API).
  2. A methodology-artifact probe that separates technique-rich repos
     (AGENTS.md, .agents/skills/, SKILL.md, docs/, config ledgers) from
     mere tools that only have a README.

The probe is the discriminator. A repo with a README and nothing else is a
tool; a repo with AGENTS.md + skills/ + docs/ is a methodology source, and
methodology is what becomes a portable skill.

Usage:
    python3 discover.py --topics reverse-engineering ghidra decompiler \
        --min-stars 300 --top 40
    python3 discover.py --topics malware-analysis --probe --top 25
    python3 discover.py --query "topic:ghidra language:python" --probe

Rate limits: GitHub search is 10 req/min unauthenticated, 30/min with a
token. The script sleeps between queries and reports the remaining budget.
The probe uses raw.githubusercontent.com, which is NOT rate-limited the
same way, so probing many repos is cheap.
"""
import argparse
import concurrent.futures as cf
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "rea-scan-forkdive", "Accept": "application/vnd.github+json"}

# Methodology artifacts, in rough order of signal strength. The presence of
# any of these means the repo documents *how* it works, not just *what* it is.
METHODOLOGY_ARTIFACTS = [
    "AGENTS.md",
    ".agents/skills/README.md",
    "CLAUDE.md",
    "SKILL.md",
    "skills/README.md",
    "docs/methodology.md",
    "docs/design/README.md",
    "docs/",
    "config/README.md",
    "CONTRIBUTING.md",
    "Makefile",
]

# A repo that ships an agent skill is the strongest signal of all: it has
# already done the work of packaging technique for an agent to consume.
SKILL_MARKERS = ["SKILL.md", "skills/README.md", ".agents/skills/README.md"]


def _get(url, n=4000, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(n).decode("utf-8", "replace"), r.headers.get(
                "X-RateLimit-Remaining"
            )
    except Exception as e:  # noqa: BLE001 - report, do not crash a sweep
        return f"__ERR__ {e}", None


def search(query, per_page=40, token=None):
    """One GitHub repo search, sorted by forks desc."""
    url = (
        "https://api.github.com/search/repositories?q="
        + urllib.parse.quote(query)
        + f"&sort=forks&order=desc&per_page={per_page}"
    )
    headers = dict(UA)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
            rem = r.headers.get("X-RateLimit-Remaining")
    except Exception as e:  # noqa: BLE001
        return [], f"__ERR__ {e}"
    items = data.get("items", [])
    return [
        {
            "full_name": i["full_name"],
            "stars": i["stargazers_count"],
            "forks": i["forks_count"],
            "desc": (i.get("description") or "")[:200],
            "topics": i.get("topics", []),
            "lang": i.get("language"),
            "license": (i.get("license") or {}).get("spdx_id"),
            "archived": i.get("archived"),
            "pushed": i.get("pushed_at"),
        }
        for i in items
    ], rem


def probe(repo, timeout=20):
    """Return the methodology artifacts a repo actually ships."""
    hits = []
    for path in METHODOLOGY_ARTIFACTS:
        target = path + "README.md" if path.endswith("/") else path
        for br in ("main", "master"):
            body, _ = _get(
                f"https://raw.githubusercontent.com/{repo}/{br}/{target}",
                n=200,
                timeout=timeout,
            )
            if not body.startswith("__ERR__"):
                hits.append(path)
                break
    return repo, hits


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--topics", nargs="*", default=[],
                    help="GitHub topics to search, e.g. reverse-engineering")
    ap.add_argument("--query", action="append", default=[],
                    help="raw GitHub search query (repeatable)")
    ap.add_argument("--seeds", default=None,
                    help="a search_seeds.py output file; runs every use case's "
                         "queries so discovery is driven by the use-case layer")
    ap.add_argument("--min-stars", type=int, default=300)
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--probe", action="store_true",
                    help="probe each candidate for methodology artifacts")
    ap.add_argument("--out", default="discovery.json")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    queries = list(args.query) + [f"topic:{t}" for t in args.topics]

    # Seeds mode: drive discovery from the use-case layer. Each use case's
    # queries are run, and every candidate is tagged with the use case that
    # surfaced it, so a find can be linked back to the capability it serves.
    seed_map = {}
    if args.seeds:
        seeds = json.load(open(args.seeds))
        for slug, s in seeds.items():
            for q in s.get("queries", [])[:3]:
                queries.append(q)
                seed_map.setdefault(q, []).append(slug)

    if not queries:
        ap.error("give --topics, --query, and/or --seeds")

    seen = {}
    for q in queries:
        rows, rem = search(q, token=token)
        if isinstance(rem, str) and rem.startswith("__ERR__"):
            print(f"ERR {q:<34} {rem}", file=sys.stderr)
        else:
            print(f"OK  {q:<34} {len(rows):>3} repos  rate_remaining={rem}")
        for r in rows:
            k = r["full_name"]
            if k in seen:
                seen[k]["topics_hit"].append(q)
                seen[k].setdefault("use_cases_hit", [])
                seen[k]["use_cases_hit"].extend(seed_map.get(q, []))
            else:
                r["topics_hit"] = [q]
                r["use_cases_hit"] = list(seed_map.get(q, []))
                seen[k] = r
        time.sleep(7)  # search API: 10/min unauthenticated

    cand = [r for r in seen.values()
            if r["stars"] >= args.min_stars and not r["archived"]]
    cand.sort(key=lambda r: (-r["forks"], -r["stars"]))

    if args.probe:
        print(f"\nprobing {len(cand[:args.top])} repos for methodology artifacts...")
        with cf.ThreadPoolExecutor(12) as ex:
            for repo, hits in ex.map(probe, [r["full_name"] for r in cand[:args.top]]):
                for r in cand:
                    if r["full_name"] == repo:
                        r["methodology"] = hits
                        r["ships_skill"] = any(h in SKILL_MARKERS for h in hits)
                        break

    json.dump(cand, open(args.out, "w"), indent=1)

    print(f"\n{'repo':<46}{'stars':>8}{'forks':>8}  {'lang':<12}{'meth':>5} skill")
    print("-" * 92)
    for r in cand[:args.top]:
        m = len(r.get("methodology", []))
        sk = "YES" if r.get("ships_skill") else ""
        print(f"{r['full_name']:<46}{r['stars']:>8}{r['forks']:>8}  "
              f"{str(r['lang'])[:11]:<12}{m:>5} {sk}")
    print(f"\nsaved {len(cand)} candidates -> {args.out}")
    if args.probe:
        rich = [r for r in cand[:args.top] if len(r.get("methodology", [])) >= 3]
        print(f"methodology-rich (>=3 artifacts): {len(rich)}")
        for r in rich:
            print(f"  {r['full_name']:<46} {','.join(r['methodology'])}")


if __name__ == "__main__":
    sys.exit(main())
