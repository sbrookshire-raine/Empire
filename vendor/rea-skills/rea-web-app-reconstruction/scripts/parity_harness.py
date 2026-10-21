#!/usr/bin/env python3
"""Language-independent parity harness for a reconstruction.

Compares a REFERENCE program and a CANDIDATE reconstruction against the same
frozen literal expectations, over a scenario corpus, and reports each separately.
The candidate may be written in any language: the interface is JSON over stdin
and stdout, plus an exit code.

This is the pattern the REA-Reconstruction-Companion's Pocket Tasks trial uses
(`evals/reference/check.mjs`), generalized to Python and to any command pair.

Why compare each to literals rather than to each other: two programs that share
a defect agree with each other. Agreement between two wrong programs is not
evidence. Each is checked against expectations written independently.

**Process contract.** Every step runs as a *fresh process* in a per-scenario
working directory. State does not survive in memory between steps; a program
that must carry state across steps persists it on disk inside its cwd (the
Companion's `--store <file>` pattern). This is deliberate: it makes restart
behavior testable, which is where real defects live. A program that keeps state
only in memory will fail step 2 of a multi-step scenario — that is a finding
about the program, not a harness fault.

Usage:
    python3 parity_harness.py \
        --reference "node target/app.mjs" \
        --candidate "python3 my_rebuild.py" \
        --scenarios scenarios.json \
        --out report.json

scenarios.json:
{
  "target": "Pocket Tasks", "version": "1.0.0",
  "scenarios": [
    {"name": "add and save",
     "steps": [
       {"input": "{\"op\":\"add\",\"title\":\"Alpha\"}",
        "expected": {"ok": true, "id": 1},
        "exit": 0},
       {"input": "{\"op\":\"list\"}",
        "expected": {"items": [{"id": 1, "title": "Alpha"}]},
        "exit": 0}
     ]}
  ]
}

Exit status: 0 if every scenario passes for BOTH programs, 1 otherwise.
"""
import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
import tempfile


def _sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def absolutize(command, base):
    """Resolve path-like arguments against the invocation cwd.

    The harness runs each scenario in its own temporary cwd for isolation, so a
    relative command like `python3 ref.py` would otherwise fail to resolve and
    look like a candidate defect. Any argument that names an existing file
    relative to the invocation directory is made absolute. Flags and bare
    program names are left alone.
    """
    resolved = []
    for index, arg in enumerate(command):
        if index == 0:
            # The executable: leave bare names to PATH lookup, absolutize paths.
            if os.path.sep in arg and not os.path.isabs(arg):
                resolved.append(os.path.abspath(os.path.join(base, arg)))
            else:
                resolved.append(arg)
            continue
        if arg.startswith("-"):
            resolved.append(arg)
            continue
        candidate = os.path.join(base, arg)
        if os.path.exists(candidate) and not os.path.isabs(arg):
            resolved.append(os.path.abspath(candidate))
        else:
            resolved.append(arg)
    return resolved


def run_step(command, stdin_text, timeout, cwd):
    """Run one step. Returns (exit_code, stdout, stderr, error_or_None)."""
    try:
        proc = subprocess.run(
            command,
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd,
            shell=False,
        )
        return proc.returncode, proc.stdout, proc.stderr, None
    except subprocess.TimeoutExpired:
        return None, "", "", "timeout"
    except Exception as exc:  # noqa: BLE001 - a harness must report, not crash
        return None, "", "", f"spawn failed: {exc}"


def compare(exit_code, stdout, stderr, step):
    """Compare one run against the frozen literal expectation for that step."""
    want_exit = step.get("exit", 0)
    if exit_code is None:
        return False, "process failed or timed out"
    if exit_code != want_exit:
        return False, f"exit {exit_code} != {want_exit}"
    if want_exit != 0:
        # An error step: stdout must be empty and stderr must say something.
        if stdout.strip():
            return False, "error step wrote to stdout"
        if not stderr.strip():
            return False, "error step wrote nothing to stderr"
        return True, None
    try:
        actual = json.loads(stdout)
    except json.JSONDecodeError:
        return False, "stdout is not one JSON value"
    if actual != step.get("expected"):
        return False, "response mismatch"
    return True, None


def run_program(label, command, scenarios, timeout, root):
    """Run every scenario against one program, comparing to literals."""
    results = []
    for index, scenario in enumerate(scenarios):
        cwd = os.path.join(root, f"{label}-{index}")
        os.makedirs(cwd, exist_ok=True)
        failed = False
        for step_index, step in enumerate(scenario.get("steps", [])):
            name = f"{scenario['name']}: step {step_index + 1}"
            if failed:
                results.append({"label": name, "status": "not-run",
                                "reason": "earlier step failed"})
                continue
            code, out, err, spawn_err = run_step(
                command, step.get("input", ""), timeout, cwd)
            ok, reason = (False, spawn_err) if spawn_err else \
                compare(code, out, err, step)
            results.append({
                "label": name,
                "status": "passed" if ok else "failed",
                "reason": reason,
                "stdoutSha256": _sha(out),
            })
            if not ok:
                failed = True
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reference", required=True,
                    help="command for the original, e.g. 'node target/app.mjs'")
    ap.add_argument("--candidate", required=True,
                    help="command for the reconstruction, any language")
    ap.add_argument("--scenarios", required=True, help="scenario corpus JSON")
    ap.add_argument("--timeout", type=float, default=5.0, help="seconds per step")
    ap.add_argument("--out", default=None, help="write the JSON report here")
    args = ap.parse_args()

    corpus = json.load(open(args.scenarios))
    scenarios = corpus["scenarios"]
    base = os.getcwd()
    ref_cmd = absolutize(shlex.split(args.reference), base)
    cand_cmd = absolutize(shlex.split(args.candidate), base)

    with tempfile.TemporaryDirectory(prefix="parity-") as root:
        ref_results = run_program("reference", ref_cmd, scenarios,
                                  args.timeout, root)
        cand_results = run_program("candidate", cand_cmd, scenarios,
                                   args.timeout, root)

    def tally(rows):
        return {
            "passed": sum(1 for r in rows if r["status"] == "passed"),
            "failed": sum(1 for r in rows if r["status"] == "failed"),
            "notRun": sum(1 for r in rows if r["status"] == "not-run"),
        }

    ref_t, cand_t = tally(ref_results), tally(cand_results)
    all_passed = (ref_t["failed"] == 0 and ref_t["notRun"] == 0
                  and cand_t["failed"] == 0 and cand_t["notRun"] == 0)

    report = {
        "schema": 1,
        "target": corpus.get("target"),
        "targetVersion": corpus.get("version"),
        "status": "comparisons-passed" if all_passed else "failed",
        "corpusSha256": _sha(json.dumps(corpus, sort_keys=True)),
        "reference": {"command": ref_cmd, **ref_t},
        "candidate": {"command": cand_cmd, **cand_t},
        "oracle": ("Frozen literals, checked separately against reference and "
                   "candidate; not self-comparison"),
        "limitations": ("Finite corpus; agreement within this corpus and "
                        "environment only, not global equivalence. A passing "
                        "run does not establish instruction following, "
                        "performance, or security."),
        "referenceRows": ref_results,
        "candidateRows": cand_results,
    }

    text = json.dumps(report, indent=2)
    if args.out:
        open(args.out, "w").write(text)
    print(text)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
