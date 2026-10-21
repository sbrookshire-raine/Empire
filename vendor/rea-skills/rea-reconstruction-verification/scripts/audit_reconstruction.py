#!/usr/bin/env python3
"""Audit a reconstruction project's claim ledgers for consistency.

Reads the ledger files a byte-exact reconstruction project keeps (functions,
implemented, matches, origins, fragments) and checks the invariants that keep
"source present" from being confused with "byte-exact".

Usage:
  python3 audit_reconstruction.py --config-dir ./config
  python3 audit_reconstruction.py --config-dir ./config --json

Exit codes: 0 all checks pass, 1 a check failed, 2 input unreadable.

The ledger names are the convention used by the DX-Ball and TH04
reconstructions; pass --map to override any of them.
"""
import argparse
import csv
import json
import os
import sys

DEFAULT_MAP = {
    "functions": "functions.csv",       # provisional entries + extents
    "implemented": "implemented.csv",   # source-present claims
    "matches": "matches.csv",           # byte-exact claims
    "origins": "function-origins.csv",  # authored / runtime / generated
    "fragments": "compiler-fragments.csv",  # parent-owned compiler output
    "semantic": "semantic-acceptance.csv",  # scoped semantic claims
}


def read_csv(path):
    if not os.path.exists(path):
        return None
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def norm_addr(a):
    """Normalize an address to lowercase 0x-prefixed hex for comparison."""
    if a is None:
        return None
    s = str(a).strip()
    if not s:
        return None
    try:
        return hex(int(s, 0)).lower()
    except ValueError:
        return s.lower()


def audit(cfg):
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    functions = read_csv(os.path.join(cfg, DEFAULT_MAP["functions"]))
    implemented = read_csv(os.path.join(cfg, DEFAULT_MAP["implemented"]))
    matches = read_csv(os.path.join(cfg, DEFAULT_MAP["matches"]))
    origins = read_csv(os.path.join(cfg, DEFAULT_MAP["origins"]))
    fragments = read_csv(os.path.join(cfg, DEFAULT_MAP["fragments"]))
    semantic = read_csv(os.path.join(cfg, DEFAULT_MAP["semantic"]))

    if functions is None:
        add("functions_ledger_present", False,
            f"{DEFAULT_MAP['functions']} not found in {cfg}")
        return checks

    fn_addrs = {norm_addr(r.get("address")) for r in functions}
    fn_addrs.discard(None)
    add("functions_ledger_present", True, f"{len(functions)} entries")

    # 1. Every exact match must also be source-present.
    if matches is not None and implemented is not None:
        impl = {norm_addr(r.get("address")) for r in implemented}
        orphan = [norm_addr(r.get("address")) for r in matches
                  if norm_addr(r.get("address")) not in impl]
        add("exact_implies_source_present", not orphan,
            f"exact without source: {orphan[:5]}" if orphan
            else f"{len(matches)} exact, all source-present")

    # 2. Every match address must exist in the functions ledger.
    if matches is not None:
        unknown = [norm_addr(r.get("address")) for r in matches
                   if norm_addr(r.get("address")) not in fn_addrs]
        add("matches_reference_known_functions", not unknown,
            f"unknown addresses: {unknown[:5]}" if unknown else "all known")

    # 3. Every implemented address must exist in the functions ledger.
    if implemented is not None:
        unknown = [norm_addr(r.get("address")) for r in implemented
                   if norm_addr(r.get("address")) not in fn_addrs]
        add("implemented_reference_known_functions", not unknown,
            f"unknown addresses: {unknown[:5]}" if unknown else "all known")

    # 4. No duplicate addresses in any ledger.
    for label, rows in (("functions", functions), ("implemented", implemented),
                        ("matches", matches), ("origins", origins)):
        if rows is None:
            continue
        seen, dupes = set(), []
        for r in rows:
            a = norm_addr(r.get("address"))
            if a in seen:
                dupes.append(a)
            seen.add(a)
        add(f"no_duplicate_addresses_{label}", not dupes,
            f"duplicates: {dupes[:5]}" if dupes else "unique")

    # 5. Exact matches must carry a zero difference count when the column exists.
    if matches is not None:
        bad = []
        for r in matches:
            dc = r.get("difference_count")
            if dc is None or dc == "":
                continue
            try:
                if int(dc) != 0:
                    bad.append((norm_addr(r.get("address")), dc))
            except ValueError:
                bad.append((norm_addr(r.get("address")), dc))
        add("exact_matches_zero_difference", not bad,
            f"nonzero: {bad[:5]}" if bad else "all zero")

    # 6. Exact matches must carry digests binding them to inputs and outputs.
    if matches is not None and matches:
        cols = set(matches[0].keys())
        digest_cols = [c for c in cols if c.endswith("_sha256")]
        add("exact_matches_carry_digests", len(digest_cols) >= 3,
            f"digest columns: {sorted(digest_cols)}")

    # 7. Origin ledger must classify every entry it lists.
    if origins is not None:
        allowed = {"authored", "runtime", "compiler_generated", "unknown"}
        bad = [(norm_addr(r.get("address")), r.get("origin"))
               for r in origins if r.get("origin") not in allowed]
        add("origins_use_known_classes", not bad,
            f"unexpected: {bad[:5]}" if bad else "all classified")

    # 8. Compiler fragments must name a parent (they are not standalone source).
    if fragments is not None and fragments:
        missing = [norm_addr(r.get("address")) for r in fragments
                   if not (r.get("parent_address") or r.get("parent_symbol"))]
        add("compiler_fragments_have_parents", not missing,
            f"parentless: {missing[:5]}" if missing else
            f"{len(fragments)} fragments, all parented")

    # 9. Semantic claims must be scoped (a bare "semantic" claim is not exact).
    if semantic is not None and semantic:
        cols = set(semantic[0].keys())
        has_scope = "scope" in cols or "semantic_unit" in cols
        add("semantic_claims_are_scoped", has_scope,
            f"columns: {sorted(cols)}")

    # 10. Counts must be internally consistent.
    if implemented is not None and matches is not None:
        add("exact_not_greater_than_source",
            len(matches) <= len(implemented),
            f"exact={len(matches)} source={len(implemented)}")

    return checks


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config-dir", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.config_dir):
        print(json.dumps({"error": f"not a directory: {args.config_dir}"}))
        return 2

    checks = audit(args.config_dir)
    passed = all(c["ok"] for c in checks)

    if args.json:
        print(json.dumps({"config_dir": args.config_dir,
                          "passed": passed, "checks": checks}, indent=2))
    else:
        for c in checks:
            mark = "PASS" if c["ok"] else "FAIL"
            print(f"[{mark}] {c['check']}: {c['detail']}")
        print(f"\nOverall: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
