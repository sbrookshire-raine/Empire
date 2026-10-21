#!/usr/bin/env python3
"""Verify an REA Evidence record against the claims made about it.

Reads one or more REA Evidence JSON files (as produced by `rea ... --json`)
and checks the structural and epistemic invariants that make an REA finding
trustworthy. It does NOT re-run analysis; it audits the record.

Usage:
  python3 verify_evidence.py evidence.json
  python3 verify_evidence.py evidence.json --claims claims.json
  python3 verify_evidence.py *.json --json

Exit codes:
  0  all checks passed
  1  one or more checks failed
  2  input could not be read or parsed

A "claim" is a statement the agent intends to make, with the evidence it
rests on. claims.json is a list of:
  {"text": "...", "evidence_id": "ev_...", "kind": "observed|inferred|unknown"}
"""
import argparse
import json
import sys

# Fields every REA Evidence record must carry.
REQUIRED_TOP = ["evidence_id", "operation", "normalized_result",
                "confidence", "authority", "limitations"]

# Confidence values REA uses. "observed" is the strongest.
KNOWN_CONFIDENCE = {"observed", "inferred", "unknown", "reported", "derived"}

# Phrases that overclaim beyond what static evidence can support.
OVERCLAIM_PATTERNS = [
    "proves that", "proves the", "definitely", "guaranteed",
    "always executes", "always runs", "is executed at runtime",
    "no vulnerabilities", "secure", "backdoor", "malware",
    "bypasses", "cracks", "unlocks", "decrypts the key",
]


def load(path):
    try:
        with open(path) as f:
            return json.load(f), None
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def check_record(rec, path):
    """Return (checks, findings) for one Evidence record."""
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    if not isinstance(rec, dict):
        add("is_object", False, "record is not a JSON object")
        return checks, []

    # 1. Required top-level fields.
    missing = [k for k in REQUIRED_TOP if k not in rec]
    add("required_fields", not missing,
        f"missing: {missing}" if missing else "all present")

    # 2. Evidence identity.
    eid = rec.get("evidence_id")
    add("has_evidence_id",
        isinstance(eid, str) and eid.startswith("ev_") and len(eid) > 10,
        f"evidence_id={eid!r}")

    # 3. Confidence is a recognized value.
    conf = rec.get("confidence")
    add("confidence_recognized", conf in KNOWN_CONFIDENCE,
        f"confidence={conf!r}")

    # 4. Limitations are declared (the core REA discipline).
    lim = rec.get("limitations")
    add("limitations_declared",
        isinstance(lim, list) and len(lim) > 0,
        f"{len(lim) if isinstance(lim, list) else 0} limitation(s)")

    # 5. Authority is stated.
    auth = rec.get("authority")
    add("authority_stated", isinstance(auth, str) and len(auth) > 0,
        f"authority={auth!r}")

    # 6. Normalized result present and non-empty.
    nr = rec.get("normalized_result")
    add("normalized_result_present",
        isinstance(nr, (dict, list)) and len(nr) > 0,
        f"type={type(nr).__name__}")

    # 7. Provider identity recorded.
    prov = rec.get("provider")
    add("provider_recorded",
        isinstance(prov, dict) and bool(prov.get("id")),
        f"provider={(prov or {}).get('id')!r}")

    # 8. Static analysis must not claim runtime observation.
    op = str(rec.get("operation") or "")
    text_blob = json.dumps(rec, ensure_ascii=False).lower()
    static_ops = ("analyze_", "inspect_", "decompile", "search_",
                  "open_binary", "list_")
    runtime_ops = ("capture_", "observe_", "process_", "scenario")
    is_static = any(op.startswith(p) for p in static_ops)
    is_runtime = any(p in op for p in runtime_ops)
    if is_static and not is_runtime:
        overclaims = [p for p in OVERCLAIM_PATTERNS if p in text_blob]
        add("no_runtime_overclaim_from_static", not overclaims,
            f"flagged: {overclaims}" if overclaims else "clean")
    else:
        add("no_runtime_overclaim_from_static", True,
            "operation is runtime or unclassified; check manually")

    # 9. Coverage fields, when the operation produces them.
    cov = rec.get("relationship_coverage")
    if cov is not None:
        add("coverage_is_structured", isinstance(cov, (dict, list)),
            f"type={type(cov).__name__}")

    # 10. Environment recorded for runtime observations.
    if is_runtime:
        env = rec.get("environment")
        add("runtime_environment_recorded",
            isinstance(env, dict) and bool(env.get("id")),
            f"environment={(env or {}).get('id')!r}")

    return checks, []


def check_claims(claims, records):
    """Cross-check stated claims against the Evidence they cite."""
    by_id = {}
    for r in records:
        if isinstance(r, dict) and r.get("evidence_id"):
            by_id[r["evidence_id"]] = r

    out = []
    for c in claims:
        text = c.get("text", "")
        eid = c.get("evidence_id")
        kind = c.get("kind", "observed")
        issues = []

        if eid not in by_id:
            issues.append(f"cited evidence_id {eid!r} not among supplied records")
        else:
            rec = by_id[eid]
            # A claim of "observed" must rest on an observed-confidence record.
            if kind == "observed" and rec.get("confidence") != "observed":
                issues.append(
                    f"claim says 'observed' but evidence confidence is "
                    f"{rec.get('confidence')!r}")
            # A claim must not exceed the record's own limitations.
            low = text.lower()
            for p in OVERCLAIM_PATTERNS:
                if p in low:
                    issues.append(f"claim text contains overclaim phrase {p!r}")

        # Every claim needs at least one citation.
        if not eid:
            issues.append("claim cites no evidence_id")

        out.append({"text": text[:120], "evidence_id": eid,
                    "kind": kind, "ok": not issues, "issues": issues})
    return out


def main():
    ap = argparse.ArgumentParser(description="Verify REA Evidence records.")
    ap.add_argument("files", nargs="+", help="REA Evidence JSON file(s)")
    ap.add_argument("--claims", help="claims.json to cross-check")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    records, errors = [], []
    for p in args.files:
        d, err = load(p)
        if err:
            errors.append({"file": p, "error": err})
            continue
        # Accept a single record or a list of records.
        if isinstance(d, list):
            records.extend(d)
        else:
            records.append(d)

    if not records:
        print(json.dumps({"error": "no records parsed", "errors": errors},
                         indent=2))
        return 2

    report = {"records": [], "errors": errors}
    all_ok = True
    for i, rec in enumerate(records):
        checks, _ = check_record(rec, args.files[0] if args.files else "")
        ok = all(c["ok"] for c in checks)
        all_ok = all_ok and ok
        report["records"].append({
            "index": i,
            "evidence_id": (rec or {}).get("evidence_id"),
            "operation": (rec or {}).get("operation"),
            "confidence": (rec or {}).get("confidence"),
            "passed": ok,
            "checks": checks,
        })

    if args.claims:
        cd, err = load(args.claims)
        if err:
            report["errors"].append({"file": args.claims, "error": err})
        else:
            # Accept either a bare list of claims or {"claims": [...]}. A
            # dict would otherwise iterate its keys and crash on the first
            # string.
            if isinstance(cd, dict):
                cd = cd.get("claims", [])
            if not isinstance(cd, list):
                report["errors"].append({
                    "file": args.claims,
                    "error": "claims must be a list or {'claims': [...]}"})
            else:
                claim_results = check_claims(cd, records)
            report["claims"] = claim_results
            all_ok = all_ok and all(c["ok"] for c in claim_results)

    report["passed"] = all_ok

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        for r in report["records"]:
            mark = "PASS" if r["passed"] else "FAIL"
            print(f"[{mark}] {r['operation']} ({r['confidence']}) "
                  f"{r['evidence_id']}")
            for c in r["checks"]:
                if not c["ok"]:
                    print(f"        x {c['check']}: {c['detail']}")
        if "claims" in report:
            print("\nClaims:")
            for c in report["claims"]:
                mark = "PASS" if c["ok"] else "FAIL"
                print(f"  [{mark}] {c['text']}")
                for i in c["issues"]:
                    print(f"        x {i}")
        for e in report["errors"]:
            print(f"[ERROR] {e['file']}: {e['error']}")
        print(f"\nOverall: {'PASS' if all_ok else 'FAIL'}")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
