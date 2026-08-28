"""Automated EMPIRE stack integration verification.

Checks service liveness and cross-service communication paths (not just open ports).
"""

from __future__ import annotations

import argparse
import asyncio
import importlib.util
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCAL_APPDATA = Path(os.environ.get("LOCALAPPDATA", "")) / "EMPIRE"
DEFAULT_OLLAMA_MODEL = "llama3.1:8b"


@dataclass
class CheckResult:
    id: str
    label: str
    ok: bool
    detail: str
    skipped: bool = False
    duration_ms: int = 0


@dataclass
class VerifyReport:
    version: int = 1
    updated: str = ""
    ok: bool = False
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    checks: list[CheckResult] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["summary"] = {
            "passed": self.passed,
            "failed": self.failed,
            "skipped": self.skipped,
            "total": len(self.checks),
            "allPassed": self.ok,
        }
        return payload


def load_dotenv_local() -> dict[str, str]:
    values: dict[str, str] = {}
    for name in (".env.local", ".env"):
        path = ROOT / name
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def http_json(
    url: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    timeout: float = 10.0,
) -> tuple[bool, str, Any]:
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            if not raw:
                return True, f"HTTP {response.status}", None
            try:
                return True, f"HTTP {response.status}", json.loads(raw)
            except json.JSONDecodeError:
                return True, f"HTTP {response.status}", raw
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", errors="replace")[:240]
        return False, f"HTTP {err.code}: {detail or err.reason}", None
    except Exception as err:  # noqa: BLE001
        return False, str(err), None


def run_check(check_id: str, label: str, fn) -> CheckResult:
    started = time.perf_counter()
    try:
        ok, detail = fn()
        skipped = detail.startswith("SKIP:")
        if skipped:
            detail = detail.removeprefix("SKIP:").strip()
        duration_ms = int((time.perf_counter() - started) * 1000)
        return CheckResult(
            id=check_id,
            label=label,
            ok=ok or skipped,
            detail=detail,
            skipped=skipped,
            duration_ms=duration_ms,
        )
    except Exception as err:  # noqa: BLE001
        duration_ms = int((time.perf_counter() - started) * 1000)
        return CheckResult(
            id=check_id,
            label=label,
            ok=False,
            detail=str(err),
            duration_ms=duration_ms,
        )


def load_mcp_module(relative: str):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


async def run_async_check(coro) -> tuple[bool, str]:
    ok, detail, _ = await coro()
    return ok, detail


def build_checks(env: dict[str, str], args: argparse.Namespace) -> list[tuple[str, str, Any]]:
    pb_url = env.get("POCKETBASE_URL", "http://127.0.0.1:8090").rstrip("/")
    ollama_base = env.get("OLLAMA_BASE_URL", "http://localhost:11434/v1").rstrip("/")
    ollama_root = ollama_base.removesuffix("/v1")
    ollama_model = env.get("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL)
    frontend_url = "http://127.0.0.1:8080"
    eve_url = "http://127.0.0.1:2000"
    python_bin = ROOT / "venv" / "Scripts" / "python.exe"

    checks: list[tuple[str, str, Any]] = []

    def add(check_id: str, label: str, fn):
        checks.append((check_id, label, fn))

    add(
        "ollama.tags",
        "Ollama API reachable",
        lambda: http_json(f"{ollama_root}/api/tags")[:2],
    )

    def ollama_model_check() -> tuple[bool, str]:
        ok, detail, payload = http_json(f"{ollama_root}/api/tags")
        if not ok:
            return ok, detail
        models = payload.get("models", []) if isinstance(payload, dict) else []
        names = {m.get("name", "") for m in models if isinstance(m, dict)}
        if ollama_model in names or f"{ollama_model}:latest" in names:
            return True, f"model available: {ollama_model}"
        if any(ollama_model.split(":")[0] in name for name in names):
            return True, f"compatible model found for {ollama_model}"
        return False, f"model missing: {ollama_model} (ollama pull {ollama_model})"

    add("ollama.model", "Ollama chat model present", ollama_model_check)

    add(
        "pocketbase.health",
        "PocketBase health endpoint",
        lambda: http_json(f"{pb_url}/api/health")[:2],
    )

    def pocketbase_tasks_check() -> tuple[bool, str]:
        ok, detail, payload = http_json(
            f"{pb_url}/api/collections/tasks/records?perPage=1&sort=-created"
        )
        if not ok:
            return ok, detail
        total = payload.get("totalItems") if isinstance(payload, dict) else None
        return True, f"tasks collection readable (totalItems={total})"

    add("pocketbase.tasks", "PocketBase tasks API", pocketbase_tasks_check)

    add(
        "frontend.static",
        "Tasks UI static server",
        lambda: http_json(f"{frontend_url}/")[:2],
    )

    def frontend_to_pocketbase_check() -> tuple[bool, str]:
        ok, detail, _ = http_json(f"{pb_url}/api/collections/tasks/records?perPage=1")
        if not ok:
            return False, f"Tasks UI dependency failed: {detail}"
        return True, "Tasks UI can reach PocketBase (same API path as index.html)"

    add("frontend.to_pocketbase", "Tasks UI -> PocketBase", frontend_to_pocketbase_check)

    def dashboard_control_check() -> tuple[bool, str]:
        ok, detail, payload = http_json(f"{frontend_url}/api/services/status")
        if not ok:
            return True, (
                "SKIP: Control API unavailable (restart with .\\scripts\\start-frontend.ps1 for dashboard Start/Stop)"
            )
        healthy = None
        if isinstance(payload, dict):
            healthy = payload.get("summary", {}).get("healthy")
        return True, f"dashboard control API ok (healthy={healthy})"

    add("frontend.control_api", "Dashboard control API", dashboard_control_check)

    add(
        "eve.info",
        "Eve agent API",
        lambda: http_json(f"{eve_url}/eve/v1/info")[:2],
    )

    def eve_to_pocketbase_check() -> tuple[bool, str]:
        ok, detail, _ = http_json(f"{pb_url}/api/health")
        if not ok:
            return False, f"Eve dependency PocketBase unreachable: {detail}"
        return True, f"Eve configured PocketBase reachable at {pb_url}"

    add("eve.to_pocketbase", "Eve -> PocketBase path", eve_to_pocketbase_check)

    def eve_to_ollama_check() -> tuple[bool, str]:
        ok, detail, _ = http_json(f"{ollama_root}/api/tags")
        if not ok:
            return False, f"Eve dependency Ollama unreachable: {detail}"
        return True, f"Eve configured Ollama reachable at {ollama_base}"

    add("eve.to_ollama", "Eve -> Ollama path", eve_to_ollama_check)

    def eve_python_worker_check() -> tuple[bool, str]:
        if args.skip_cognee:
            return True, "SKIP: Cognee worker check disabled"
        if not python_bin.exists():
            return False, f"Python venv missing: {python_bin}"
        result = subprocess.run(
            [
                str(python_bin),
                "-m",
                "pipeline.cognee_worker",
                "recall",
                "--query",
                "integration probe",
                "--dataset",
                "mock",
            ],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=90,
            env={**os.environ, "PYTHONPATH": str(ROOT)},
        )
        if result.returncode != 0:
            stderr = (result.stderr or result.stdout or "").strip()[:240]
            return False, stderr or f"exit {result.returncode}"
        return True, "Eve Python/Cognee worker subprocess ok"

    add("eve.to_cognee_worker", "Eve -> Python/Cognee worker", eve_python_worker_check)

    async def mcp_pocketbase_async() -> tuple[bool, str, Any]:
        mod = load_mcp_module("mcp/pocketbase_mcp.py")
        health = await mod.pb_health()
        records = await mod.pb_list_records("tasks")
        return True, f"MCP PocketBase tools ok ({len(records)} chars)", None

    def mcp_pocketbase_check() -> tuple[bool, str]:
        return asyncio.run(run_async_check(mcp_pocketbase_async))

    add("mcp.pocketbase", "MCP empire-pocketbase -> PocketBase", mcp_pocketbase_check)

    async def mcp_cognee_async() -> tuple[bool, str, Any]:
        if args.skip_cognee:
            return True, "SKIP: Cognee checks disabled", None
        mod = load_mcp_module("mcp/cognee_mcp.py")
        recall = await mod.cognee_recall("integration probe", dataset="mock")
        if not recall or len(recall) < 20:
            return False, "Cognee recall returned empty/weak response"
        return True, f"MCP Cognee recall ok ({len(recall)} chars)", None

    def mcp_cognee_check() -> tuple[bool, str]:
        return asyncio.run(run_async_check(mcp_cognee_async))

    add("mcp.cognee", "MCP empire-cognee -> Cognee", mcp_cognee_check)

    def roundtrip_task_check() -> tuple[bool, str]:
        marker = f"__verify_stack__{int(time.time())}"
        create_ok, create_detail, created = http_json(
            f"{pb_url}/api/collections/tasks/records",
            method="POST",
            body={
                "title": marker,
                "description": "automated integration probe",
                "status": "todo",
                "priority": 0,
            },
        )
        if not create_ok or not isinstance(created, dict):
            return False, f"create failed: {create_detail}"
        task_id = created.get("id")
        if not task_id:
            return False, "create response missing id"

        list_ok, list_detail, listed = http_json(
            f"{pb_url}/api/collections/tasks/records?filter="
            + urllib.parse.quote(f'title="{marker}"')
        )
        if not list_ok or not isinstance(listed, dict):
            http_json(
                f"{pb_url}/api/collections/tasks/records/{task_id}",
                method="DELETE",
            )
            return False, f"list failed: {list_detail}"

        items = listed.get("items", [])
        if not items:
            http_json(
                f"{pb_url}/api/collections/tasks/records/{task_id}",
                method="DELETE",
            )
            return False, "created task not found on read-back"

        delete_ok, delete_detail, _ = http_json(
            f"{pb_url}/api/collections/tasks/records/{task_id}",
            method="DELETE",
        )
        if not delete_ok:
            return False, f"delete failed: {delete_detail}"
        return True, "task create -> read -> delete round-trip ok"

    add("integration.task_roundtrip", "Task write/read/delete round-trip", roundtrip_task_check)

    if args.full_ingest:
        def ingest_verify_check() -> tuple[bool, str]:
            if not python_bin.exists():
                return False, f"Python venv missing: {python_bin}"
            result = subprocess.run(
                [str(python_bin), str(ROOT / "pipeline" / "verify_ingest.py")],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
                timeout=300,
                env={**os.environ, "PYTHONPATH": str(ROOT)},
            )
            if result.returncode != 0:
                stderr = (result.stderr or result.stdout or "").strip()[:240]
                return False, stderr or f"exit {result.returncode}"
            return True, "pipeline/verify_ingest.py passed"

        add("pipeline.verify_ingest", "Ingest pipeline + Cognee recall", ingest_verify_check)

    return checks


def run_verification(args: argparse.Namespace) -> VerifyReport:
    env = load_dotenv_local()
    checks = build_checks(env, args)
    results: list[CheckResult] = []

    for check_id, label, fn in checks:
        results.append(run_check(check_id, label, fn))

    passed = sum(1 for r in results if r.ok and not r.skipped)
    skipped = sum(1 for r in results if r.skipped)
    failed = sum(1 for r in results if not r.ok and not r.skipped)
    report = VerifyReport(
        updated=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        ok=failed == 0,
        passed=passed,
        failed=failed,
        skipped=skipped,
        checks=results,
    )
    return report


def write_report(report: VerifyReport, json_out: Path | None) -> None:
    targets = [
        LOCAL_APPDATA / "verify-stack.json",
        ROOT / "frontend" / "verify-stack.json",
    ]
    if json_out:
        targets.append(json_out)
    payload = json.dumps(report.to_dict(), indent=2)
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(payload, encoding="utf-8")


def print_report(report: VerifyReport) -> None:
    print("EMPIRE stack integration verification")
    print("=====================================")
    for check in report.checks:
        if check.skipped:
            flag = "[SKIP]"
        elif check.ok:
            flag = "[ OK ]"
        else:
            flag = "[FAIL]"
        print(f"{flag} {check.label}")
        print(f"       {check.detail} ({check.duration_ms} ms)")
    print("")
    print(
        f"Summary: {report.passed} passed, {report.failed} failed, {report.skipped} skipped"
    )
    if report.ok:
        print("Result: PASSED")
    else:
        print("Result: FAILED")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify EMPIRE service integration")
    parser.add_argument(
        "--skip-cognee",
        action="store_true",
        help="Skip Cognee/MCP-cognee checks (faster; no graph memory required)",
    )
    parser.add_argument(
        "--full-ingest",
        action="store_true",
        help="Also run pipeline/verify_ingest.py (slow; re-ingests mock fixture)",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Optional extra path for JSON report",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON report to stdout")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report = run_verification(args)
    write_report(report, args.json_out)
    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print_report(report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
