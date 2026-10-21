"""REA skills runner — the six approved Bin-1 skills, executed locally and fail-closed.

What this is
------------
The Gumloop REA bundle ships 22 agent skills. Six were approved (Bin-1) for
EMPIRE: the five that run standalone (only Python 3 stdlib) plus `claim-ledger`,
which is the only other skill that needs neither the `rea` CLI nor a paid engine.

This module runs those skills' bundled scripts on the local host. It does not
reimplement them, and it does not trust them blindly: every invocation is

- **allowlisted** — only the six approved skill ids exist here; anything else
  is refused by name, and the deferred Bin-3 set is not present at all.
- **path-jailed** — inputs are resolved with `pipeline.paths.resolve_within`
  against a declared root, so a model-supplied path cannot escape.
- **create-only** — this module never writes into the vendored skill tree; it
  copies a skill's scripts into a scratch workdir before running them, so the
  vendored source stays byte-identical to upstream.
- **fail-closed** — a missing interpreter, a missing script, or a non-zero exit
  returns `{ok: false, ...}` naming the cause. It never degrades silently.

Why the interpreter is not `python3`
-----------------------------------
Upstream skills document `python3 ...`. On this Windows host `python3` resolves
to the Microsoft Store alias stub, which prints "Python was not found" and
exits non-zero. The runner therefore resolves an interpreter in this order:
`EMPIRE_REA_PYTHON` -> the repo venv -> a real `python3` on PATH. The
interpreter that was actually used is reported in every result, so a report can
never claim a check ran under an interpreter that did not exist.

Provenance
----------
Skills are vendored from the Gumloop REA bundle (REA 6.5.0 packaging, upstream
morluto/rea, MIT). The vendored tree carries the bundle's own SHA-256
`manifest.json`, and every vendored file is checked against it — see
`tests/pipeline/test_rea_skills.py`. See `docs/rea-integration/probe-log.md`
for the evidence trail and `docs/rea-integration/approval-matrix.md` for the
Bin-1/Bin-3 split.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from pipeline.paths import PathOutsideRoot, resolve_within

ROOT = Path(__file__).resolve().parents[1]
VENDOR_ROOT = ROOT / "vendor" / "rea-skills"
SCRATCH_ROOT = ROOT / "eve-output" / "rea-skills"

# --- the approved set -------------------------------------------------------
# Exactly six. The other sixteen (eleven REA-CLI skills and five
# protocol/utility skills) are deliberately absent from this tree; they were
# triaged to Bin-3 and are out of scope. A skill id that is not here does not
# exist as far as the runner is concerned.
BIN1_SKILLS: tuple[str, ...] = (
    "claim-ledger",
    "rea-evidence-verification",
    "rea-reconstruction-verification",
    "rea-target-free-readers",
    "rea-web-app-reconstruction",
    "repo-forkdiving",
)

# Scripts that need the network are marked here rather than discovered, so the
# network flag is always explicit in a result rather than inferred.
NETWORK_SKILLS: frozenset[str] = frozenset({"repo-forkdiving"})

# Default timeout per script run (seconds).
DEFAULT_TIMEOUT = int(os.environ.get("EMPIRE_REA_TIMEOUT", "120"))
MAX_OUTPUT_CHARS = 40_000


def skills_root() -> Path:
    """Where the vendored Bin-1 skills live (overridable for tests)."""

    override = os.environ.get("EMPIRE_REA_SKILLS_DIR", "").strip()
    return Path(override) if override else VENDOR_ROOT


def scratch_root() -> Path:
    """Scratch directory for copied scripts and their outputs."""

    override = os.environ.get("EMPIRE_REA_SCRATCH_DIR", "").strip()
    return Path(override) if override else SCRATCH_ROOT


def list_skills() -> dict[str, Any]:
    """The approved Bin-1 set and what each one can run on this host."""

    root = skills_root()
    rows: list[dict[str, Any]] = []
    for name in BIN1_SKILLS:
        skill_dir = root / name
        scripts = (
            sorted(p.name for p in (skill_dir / "scripts").glob("*.py"))
            if (skill_dir / "scripts").is_dir()
            else []
        )
        rows.append(
            {
                "name": name,
                "present": (skill_dir / "SKILL.md").is_file(),
                "scripts": scripts,
                "network": name in NETWORK_SKILLS,
            }
        )
    return {
        "ok": True,
        "root": str(root),
        "count": len(rows),
        "skills": rows,
        "deferred_bin3_count": 16,
    }


def resolve_python() -> str | None:
    """The interpreter used to run skill scripts.

    `python3` first is wrong on this host (Store alias stub), so the repo venv
    wins. Resolution order is deliberate and reported in the result.
    """

    override = os.environ.get("EMPIRE_REA_PYTHON", "").strip()
    if override and Path(override).is_file():
        return override
    venv = ROOT / "venv" / "Scripts" / "python.exe"
    if venv.is_file():
        return str(venv)
    found = shutil.which("python3")
    if found and not _is_store_stub(found):
        return found
    return shutil.which("python")


def _is_store_stub(path: str) -> bool:
    """True for the WindowsApps `python3` alias that prints 'Python was not found'."""

    return "/windowsapps/" in path.replace("\\", "/").lower()


def _copy_skill_scripts(skill: str, workdir: Path) -> Path:
    """Copy a skill's scripts into the scratch workdir (create-only upstream).

    Upstream files are never modified: the copy is what runs, so the vendored
    tree stays byte-identical to upstream and a rollback is a directory delete.
    `examples/` and `references/` travel with the scripts because a skill's own
    fixtures are what make its checks runnable offline.
    """

    source = skills_root() / skill / "scripts"
    if not source.is_dir():
        raise FileNotFoundError(f"no scripts directory for skill {skill!r}")
    skill_target = workdir / skill
    target = skill_target / "scripts"
    target.mkdir(parents=True, exist_ok=True)
    for script in sorted(source.glob("*.py")):
        shutil.copy2(script, target / script.name)
    for extra in ("examples", "references"):
        src = skills_root() / skill / extra
        if not src.is_dir():
            continue
        dst = skill_target / extra
        dst.mkdir(parents=True, exist_ok=True)
        for item in sorted(src.rglob("*")):
            if item.is_file():
                out = dst / item.relative_to(src)
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, out)
    return target


def run_script(
    skill: str,
    script: str,
    args: list[str],
    *,
    work_dir: str = "",
    timeout: int = DEFAULT_TIMEOUT,
) -> dict[str, Any]:
    """Run one vendored skill script with path-jailed inputs.

    `work_dir` is the only writable location a script may use, and it must
    resolve inside the declared scratch root. A script is never run from the
    vendored tree itself.
    """

    if skill not in BIN1_SKILLS:
        return {
            "ok": False,
            "error": f"skill {skill!r} is not in the approved Bin-1 set",
            "approved": list(BIN1_SKILLS),
        }

    interpreter = resolve_python()
    if not interpreter:
        return {"ok": False, "error": "no Python interpreter available for skill scripts"}

    source_dir = skills_root() / skill / "scripts"
    script_path = source_dir / script
    if not script_path.is_file():
        return {
            "ok": False,
            "error": f"script {script!r} not found in skill {skill!r}",
            "available": sorted(p.name for p in source_dir.glob("*.py")),
        }

    scratch = scratch_root()
    scratch.mkdir(parents=True, exist_ok=True)

    # Resolve the working directory inside the scratch root, then copy the
    # skill scripts next to it so relative paths in the skill body still work.
    workdir = scratch / skill
    workdir.mkdir(parents=True, exist_ok=True)
    try:
        resolved_work = resolve_within(work_dir or str(workdir), scratch, label="work_dir")
    except PathOutsideRoot as exc:
        return {"ok": False, "error": str(exc)}

    try:
        scripts_dir = _copy_skill_scripts(skill, scratch)
    except FileNotFoundError as exc:
        return {"ok": False, "error": str(exc)}

    run_cwd = scripts_dir if resolved_work == scripts_dir else resolved_work
    run_cwd.mkdir(parents=True, exist_ok=True)

    command = [interpreter, str(scripts_dir / script), *args]
    try:
        completed = subprocess.run(
            command,
            cwd=str(run_cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=max(1, int(timeout)),
            check=False,
            env={**os.environ, "PYTHONPATH": str(ROOT)},
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "error": f"timed out after {timeout}s",
            "skill": skill,
            "script": script,
        }
    except OSError as exc:
        return {"ok": False, "error": f"could not start interpreter: {exc}"}

    stdout = (completed.stdout or "")[:MAX_OUTPUT_CHARS]
    stderr = (completed.stderr or "")[:MAX_OUTPUT_CHARS]
    payload: dict[str, Any] = {
        "ok": completed.returncode == 0,
        "skill": skill,
        "script": script,
        "exit_code": completed.returncode,
        "interpreter": interpreter,
        "work_dir": str(run_cwd),
        "stdout": stdout,
        "stderr": stderr,
    }
    # These scripts speak JSON on stdout with --json; surface it when it parses
    # so the caller does not have to re-parse text.
    parsed = _maybe_json(stdout)
    if parsed is not None:
        payload["result"] = parsed
    if completed.returncode != 0:
        payload["error"] = (stderr or stdout or f"exit {completed.returncode}").strip()[-500:]
    return payload


def _maybe_json(text: str) -> Any:
    """Parse stdout as JSON when it is a single JSON document, else None."""

    cleaned = text.strip()
    if not cleaned or not (cleaned.startswith("{") or cleaned.startswith("[")):
        return None
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None


# --- the six skill entry points --------------------------------------------


def verify_evidence(files: list[str], claims: str = "", work_dir: str = "") -> dict[str, Any]:
    """Audit REA Evidence records and the claims resting on them."""

    if not files:
        return {"ok": False, "error": "at least one evidence file is required"}
    scratch = scratch_root()
    scratch.mkdir(parents=True, exist_ok=True)
    resolved: list[str] = []
    for raw in files:
        try:
            resolved.append(str(resolve_within(raw, scratch, label="evidence file")))
        except PathOutsideRoot as exc:
            return {"ok": False, "error": str(exc)}
    args = [*resolved, "--json"]
    if claims:
        try:
            args += ["--claims", str(resolve_within(claims, scratch, label="claims file"))]
        except PathOutsideRoot as exc:
            return {"ok": False, "error": str(exc)}
    return run_script(
        "rea-evidence-verification", "verify_evidence.py", args, work_dir=work_dir
    )


def audit_reconstruction(config_dir: str, work_dir: str = "") -> dict[str, Any]:
    """Audit a reconstruction's ledgers/oracles against its config directory."""

    if not config_dir:
        return {"ok": False, "error": "config_dir is required"}
    scratch = scratch_root()
    scratch.mkdir(parents=True, exist_ok=True)
    try:
        resolved = resolve_within(config_dir, scratch, label="config_dir")
    except PathOutsideRoot as exc:
        return {"ok": False, "error": str(exc)}
    return run_script(
        "rea-reconstruction-verification",
        "audit_reconstruction.py",
        ["--config-dir", str(resolved), "--json"],
        work_dir=work_dir,
    )


def parity_check(
    reference: str, candidate: str, scenarios: str, work_dir: str = ""
) -> dict[str, Any]:
    """Prove a reconstruction matches its reference across a scenario corpus.

    `reference` and `candidate` are *commands* (the harness runs them as
    processes, in any language), not bare paths. Every path-like token inside
    them is jailed to the scratch root, so a command cannot reach outside it.
    """

    scratch = scratch_root()
    scratch.mkdir(parents=True, exist_ok=True)
    try:
        ref_cmd = _jail_command(reference, scratch)
        cand_cmd = _jail_command(candidate, scratch)
        scen = resolve_within(scenarios, scratch, label="scenarios")
    except PathOutsideRoot as exc:
        return {"ok": False, "error": str(exc)}
    return run_script(
        "rea-web-app-reconstruction",
        "parity_harness.py",
        ["--reference", ref_cmd, "--candidate", cand_cmd, "--scenarios", str(scen)],
        work_dir=work_dir,
    )


def _jail_command(command: str, root: Path) -> str:
    """Rewrite a command so every path-like argument stays inside `root`.

    The *program* token (index 0) is left alone: it names an interpreter or
    executable, not a file the harness reads — and on this host the Python
    interpreter lives outside the scratch root by design. Every later token
    that names an existing file or directory is resolved inside `root`, and an
    absolute path that escapes `root` is refused rather than rewritten.

    A token that does not exist (a flag, or a bare program name) is left alone,
    so the harness resolves it the way its author intended.

    Paths are emitted with forward slashes. The upstream harness splits the
    command with POSIX `shlex`, where a backslash is an escape character — so
    `C:\\EMPIRE\\python.exe` arrives at the harness as `C:EMPIREpython.exe` and
    the program cannot be found. Forward slashes survive that split intact and
    Windows accepts them.
    """

    cleaned = (command or "").strip()
    if not cleaned:
        raise PathOutsideRoot("command is required")
    tokens = shlex.split(cleaned, posix=False) if _is_windows() else shlex.split(cleaned)
    out: list[str] = []
    for index, token in enumerate(tokens):
        stripped = token.strip('"')
        if index == 0:
            out.append(stripped.replace("\\", "/") if _is_windows() else stripped)
            continue
        looks_absolute = stripped.startswith(("/", "\\")) or (
            len(stripped) > 1 and stripped[1] == ":"
        )
        exists = (root / stripped).exists() or Path(stripped).exists()
        if not looks_absolute and not exists:
            out.append(token)
            continue
        resolved = resolve_within(stripped, root, label="command path")
        out.append(resolved.as_posix())
    return " ".join(out)


def _is_windows() -> bool:
    return os.name == "nt"


def build_fixtures(out: str = "", work_dir: str = "") -> dict[str, Any]:
    """Build the target-free readers' local fixtures (no engine needed)."""

    scratch = scratch_root()
    scratch.mkdir(parents=True, exist_ok=True)
    target = out or str(scratch / "rea-target-free-readers" / "fixtures")
    try:
        resolved = resolve_within(target, scratch, label="out")
    except PathOutsideRoot as exc:
        return {"ok": False, "error": str(exc)}
    return run_script(
        "rea-target-free-readers",
        "build_fixtures.py",
        ["--out", str(resolved), "--json"],
        work_dir=work_dir,
    )


def forkdive(
    repo: str, source: str = "auto", top: int = 5, work_dir: str = ""
) -> dict[str, Any]:
    """Mine a repository's fork network for proven use cases (network required)."""

    if not repo or "/" not in repo:
        return {"ok": False, "error": "repo must be OWNER/REPO"}
    return run_script(
        "repo-forkdiving",
        "forkdive.py",
        [repo, "--json", "--source", source, "--compare-top", str(int(top))],
        work_dir=work_dir,
    )


def discover(
    topics: list[str] | None = None,
    query: list[str] | None = None,
    min_stars: int = 300,
    top: int = 40,
    work_dir: str = "",
) -> dict[str, Any]:
    """Discover high-signal repositories for a topic (network required)."""

    args: list[str] = [
        "--min-stars",
        str(int(min_stars)),
        "--top",
        str(int(top)),
        "--json",
    ]
    if topics:
        args += ["--topics", *topics]
    for item in query or []:
        args += ["--query", item]
    return run_script("repo-forkdiving", "discover.py", args, work_dir=work_dir)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="REA Bin-1 skill runner")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List the approved Bin-1 skills and their scripts")

    ev = sub.add_parser("verify-evidence", help="Audit REA Evidence records")
    ev.add_argument("files", nargs="+")
    ev.add_argument("--claims", default="")
    ev.add_argument("--work-dir", default="")

    rec = sub.add_parser("audit-reconstruction", help="Audit a reconstruction config dir")
    rec.add_argument("--config-dir", required=True)
    rec.add_argument("--work-dir", default="")

    par = sub.add_parser("parity", help="Parity-check a reconstruction against a reference")
    par.add_argument("--reference", required=True)
    par.add_argument("--candidate", required=True)
    par.add_argument("--scenarios", required=True)
    par.add_argument("--work-dir", default="")

    fix = sub.add_parser("build-fixtures", help="Build target-free reader fixtures")
    fix.add_argument("--out", default="")
    fix.add_argument("--work-dir", default="")

    fd = sub.add_parser("forkdive", help="Mine a repo's fork network (network)")
    fd.add_argument("repo")
    fd.add_argument("--source", default="auto")
    fd.add_argument("--top", type=int, default=5)
    fd.add_argument("--work-dir", default="")

    disc = sub.add_parser("discover", help="Discover repos by topic (network)")
    disc.add_argument("--topics", nargs="*", default=[])
    disc.add_argument("--query", action="append", default=[])
    disc.add_argument("--min-stars", type=int, default=300)
    disc.add_argument("--top", type=int, default=40)
    disc.add_argument("--work-dir", default="")

    args = parser.parse_args(argv)
    if args.cmd == "list":
        out: dict[str, Any] = list_skills()
    elif args.cmd == "verify-evidence":
        out = verify_evidence(args.files, args.claims, args.work_dir)
    elif args.cmd == "audit-reconstruction":
        out = audit_reconstruction(args.config_dir, args.work_dir)
    elif args.cmd == "parity":
        out = parity_check(args.reference, args.candidate, args.scenarios, args.work_dir)
    elif args.cmd == "build-fixtures":
        out = build_fixtures(args.out, args.work_dir)
    elif args.cmd == "forkdive":
        out = forkdive(args.repo, args.source, args.top, args.work_dir)
    else:
        out = discover(args.topics, args.query, args.min_stars, args.top, args.work_dir)

    print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
