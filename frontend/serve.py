"""Serve EMPIRE frontend static files and a local-only service control API."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from email import policy
from email.parser import BytesParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

try:
    from frontend import (
        chat_history,
        eve_proxy,
        eve_toolbelt,
        memory_api,
        ollama_api,
        ollama_inventory,
        primitives_api,
        project_catalog,
        wiki_api,
    )
except ModuleNotFoundError:
    import chat_history  # type: ignore[no-redef]
    import eve_proxy  # type: ignore[no-redef]
    import eve_toolbelt  # type: ignore[no-redef]
    import memory_api  # type: ignore[no-redef]
    import ollama_api  # type: ignore[no-redef]
    import ollama_inventory  # type: ignore[no-redef]
    import project_catalog  # type: ignore[no-redef]
    import primitives_api  # type: ignore[no-redef]
    import wiki_api  # type: ignore[no-redef]

ROOT = Path(__file__).resolve().parents[1]
FRONTEND = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config" / "services.json"
HOST = "127.0.0.1"
PORT = 8080
PS = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File"]
MEMORY_ALLOWED_ORIGINS = {
    "http://127.0.0.1:8080",
    "http://localhost:8080",
}


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def run_ps_script(script: Path, extra_args: list[str] | None = None, timeout: int = 120) -> dict:
    cmd = [*PS, str(script), *(extra_args or [])]
    result = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def run_ps_command(command: str, timeout: int = 30) -> dict:
    result = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def get_port_pid(port: int) -> int | None:
    result = run_ps_command(
        f"(Get-NetTCPConnection -LocalPort {port} -State Listen -ErrorAction SilentlyContinue "
        f"| Select-Object -First 1).OwningProcess"
    )
    if not result["ok"] or not result["stdout"]:
        return None
    try:
        pid = int(result["stdout"].strip())
        return pid if pid > 0 else None
    except ValueError:
        return None


def port_listening(port: int) -> bool:
    return get_port_pid(port) is not None


def check_health(url: str, timeout_sec: int = 8) -> dict:
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            return {"ok": 200 <= resp.status < 300, "detail": f"HTTP {resp.status}"}
    except urllib.error.HTTPError as err:
        return {"ok": False, "detail": f"HTTP {err.code}"}
    except Exception as err:  # noqa: BLE001
        return {"ok": False, "detail": str(err)}


def resolve_path(relative: str) -> Path:
    path = Path(relative.replace("/", os.sep))
    if path.is_absolute():
        return path
    return ROOT / path


def resolve_executable(exe: str) -> str:
    if exe.startswith("npm"):
        for candidate in ("npm.cmd", "npm"):
            resolved = shutil_which(candidate)
            if resolved:
                return resolved
    if exe.startswith("python"):
        resolved = shutil_which("python")
        if resolved:
            return resolved
    resolved = resolve_path(exe)
    return str(resolved)


def shutil_which(name: str) -> str | None:
    return shutil.which(name)


def expand_env(values: dict[str, str]) -> dict[str, str]:
    expanded: dict[str, str] = {}
    for key, value in values.items():
        expanded[key] = value.replace("{{EMPIRE_ROOT}}", str(ROOT))
    return expanded


def wait_for_health(service: dict, defaults: dict) -> dict:
    retries = int(defaults.get("healthRetries", 12))
    delay = int(defaults.get("healthRetrySec", 1))
    timeout = int(defaults.get("healthTimeoutSec", 8))
    health = {"ok": False, "detail": "not checked"}
    for attempt in range(1, retries + 1):
        health = check_health(service["healthUrl"], timeout)
        if health["ok"]:
            return health
        if attempt < retries:
            time.sleep(delay)
    return health


def start_managed_service(name: str, config: dict) -> dict:
    service = config["services"][name]
    defaults = config["defaults"]

    if not service.get("managed"):
        health = wait_for_health(service, defaults)
        if not health["ok"]:
            return {"ok": False, "error": f"External service '{name}' unhealthy: {health['detail']}"}
        return {"ok": True, "stdout": f"[{name}] external service healthy"}

    port = int(service["port"])
    if port_listening(port):
        health = wait_for_health(service, defaults)
        if health["ok"]:
            return {"ok": True, "stdout": f"[{name}] already listening on port {port}"}
        return {"ok": False, "error": f"[{name}] port {port} in use but unhealthy: {health['detail']}"}

    start = service["start"]
    prepare = start.get("prepare")
    if prepare:
        prepare_result = subprocess.run(
            [
                resolve_executable(str(prepare["exe"])),
                *[str(item) for item in prepare.get("args", [])],
            ],
            cwd=str(resolve_path(str(prepare.get("cwd", ".")))),
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
        if prepare_result.returncode != 0:
            detail = prepare_result.stderr.strip() or prepare_result.stdout.strip()
            return {
                "ok": False,
                "error": f"[{name}] runtime preparation failed: {detail}",
            }
    exe = resolve_executable(start["exe"])
    cwd = str(resolve_path(start["cwd"]))
    args = [str(a) for a in start.get("args", [])]
    env = os.environ.copy()
    env.update(expand_env(start.get("env", {})))

    creationflags = 0
    if os.name == "nt" and start.get("hidden"):
        creationflags = subprocess.CREATE_NO_WINDOW  # type: ignore[attr-defined]

    subprocess.Popen(  # noqa: S603
        [exe, *args],
        cwd=cwd,
        env=env,
        creationflags=creationflags,
    )

    health = wait_for_health(service, defaults)
    if not health["ok"]:
        return {"ok": False, "error": f"[{name}] failed health check: {health['detail']}"}
    return {"ok": True, "stdout": f"[{name}] started on port {port}"}


def stop_managed_service(name: str, config: dict) -> dict:
    service = config["services"][name]
    defaults = config["defaults"]

    if not service.get("managed"):
        return {"ok": True, "stdout": f"[{name}] external - left running"}

    port = int(service["port"])
    pid = get_port_pid(port)
    if not pid:
        return {"ok": True, "stdout": f"[{name}] not running"}

    grace = int(defaults.get("stopGraceSec", 5))
    run_ps_command(f"Stop-Process -Id {pid} -ErrorAction SilentlyContinue")
    deadline = time.time() + grace
    while time.time() < deadline:
        if not get_port_pid(port):
            return {"ok": True, "stdout": f"[{name}] stopped pid {pid}"}
        time.sleep(0.4)

    run_ps_command(f"Stop-Process -Id {pid} -Force -ErrorAction SilentlyContinue")
    time.sleep(int(defaults.get("stopForceSec", 3)))
    return {"ok": True, "stdout": f"[{name}] forced stop pid {pid}"}


def roll_services(action: str, only: list[str] | None, config: dict) -> dict:
    order_key = "rollInOrder" if action == "start" else "rollOutOrder"
    order = config[order_key]
    if only:
        order = [name for name in order if name in only]

    lines: list[str] = []
    ok = True
    for name in order:
        if name not in config["services"]:
            continue
        if action == "start":
            result = start_managed_service(name, config)
        else:
            result = stop_managed_service(name, config)
        line = result.get("stdout") or result.get("error") or f"[{name}] done"
        lines.append(line)
        if not result.get("ok"):
            ok = False
            break

    return {"ok": ok, "stdout": "\n".join(lines), "stderr": "" if ok else lines[-1]}


class EmpireHTTPServer(ThreadingHTTPServer):
    """Frontend server that owns and cleanly drains its memory-job executor."""

    def __init__(
        self,
        server_address,
        request_handler_class,
        *,
        memory_runner: memory_api.MemoryJobRunner | None = None,
    ) -> None:
        self.memory_runner = memory_runner or memory_api.JOB_RUNNER
        super().__init__(server_address, request_handler_class)

    def server_close(self) -> None:
        try:
            super().server_close()
        finally:
            self.memory_runner.shutdown()


class EmpireHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND), **kwargs)

    def end_headers(self) -> None:
        path = urlparse(self.path).path
        origin = self.headers.get("Origin")
        local_only_api = (
            path.startswith("/api/memory/")
            or path.startswith("/api/projects/")
            or path.startswith("/api/eve/")
            or path.startswith("/api/ollama/")
        )
        if local_only_api:
            if origin in MEMORY_ALLOWED_ORIGINS:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")
        else:
            self.send_header("Access-Control-Allow-Origin", "*")
        methods = "GET, POST, OPTIONS" if path.startswith("/api/eve/") else (
            "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        )
        self.send_header("Access-Control-Allow-Methods", methods)
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        if path.endswith((".html", ".js", ".css")) or path in {"/", "/eve.html"}:
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self) -> None:
        path = urlparse(self.path).path
        if (
            path.startswith("/api/memory/")
            or path.startswith("/api/projects/")
            or path.startswith("/api/eve/")
            or path.startswith("/api/ollama/")
            or path.startswith("/api/chat-history")
        ) and not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        if path.startswith("/api/eve/"):
            requested_method = self.headers.get("Access-Control-Request-Method", "GET")
            try:
                eve_proxy.validate_eve_request(
                    requested_method,
                    self._eve_upstream_path(),
                )
            except eve_proxy.EveRequestError as exc:
                return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        self.send_response(204)
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/eve/"):
            return self._eve_proxy_request("GET")
        if path == "/api/ollama/models":
            return self._ollama_models()
        if path == "/api/ollama/inventory":
            return self._ollama_inventory()
        if path == "/api/chat-history" or path.startswith("/api/chat-history/"):
            return self._chat_history_get(path)
        if path == "/api/memory/status":
            return self._memory_status()
        if path == "/api/projects/catalog":
            return self._projects_catalog_get()
        if path.startswith("/api/memory/jobs/"):
            return self._memory_job_get(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_get(path)
        if path == "/api/primitives/status":
            return self._primitives_get()
        if path == "/api/services/status":
            snapshot_path = FRONTEND / "dashboard-status.json"
            if not snapshot_path.exists() or snapshot_path.stat().st_size == 0:
                run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
            if snapshot_path.exists() and snapshot_path.stat().st_size > 0:
                try:
                    payload = json.loads(snapshot_path.read_text(encoding="utf-8"))
                    return self._send_json(200, payload)
                except json.JSONDecodeError:
                    run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
                    try:
                        payload = json.loads(snapshot_path.read_text(encoding="utf-8"))
                        return self._send_json(200, payload)
                    except json.JSONDecodeError:
                        pass
            return self._send_json(503, {"ok": False, "error": "Status snapshot missing or invalid"})
        if path == "/api/verify/stack":
            report_path = FRONTEND / "verify-stack.json"
            if report_path.exists() and report_path.stat().st_size > 0:
                try:
                    return self._send_json(200, json.loads(report_path.read_text(encoding="utf-8")))
                except json.JSONDecodeError:
                    pass
            return self._send_json(404, {"ok": False, "error": "No verification report yet"})
        return super().do_GET()

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/eve/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            payload = self._read_eve_json()
            if payload is None:
                return None
            payload = eve_toolbelt.apply_active_tools(payload)
            payload = ollama_api.apply_chat_mode_payload(payload)
            payload = memory_api.enrich_eve_message_payload(payload)
            return self._eve_proxy_request("POST", payload)
        if path.startswith("/api/memory/") and not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        if path == "/api/memory/recall":
            return self._memory_recall()
        if path == "/api/memory/answer":
            return self._memory_answer()
        if path == "/api/memory/optimize":
            return self._memory_optimize()
        if path == "/api/projects/catalog/refresh":
            return self._projects_catalog_refresh()
        if path == "/api/memory/upload":
            return self._memory_upload()
        if path == "/api/ollama/summarize-tasks":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._ollama_summarize_tasks()
        if path.startswith("/api/memory/jobs/") and path.endswith("/retry"):
            return self._memory_retry(path)
        payload = self._read_json()

        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("POST", path, payload)

        if path == "/api/primitives/ingest":
            return self._primitives_ingest(payload)

        if path == "/api/services/refresh":
            result = run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
            return self._finish_control(result)

        if path == "/api/verify/stack":
            return self._run_verify_stack(payload)

        if path == "/api/services/start":
            return self._service_action("start", payload)

        if path == "/api/services/stop":
            return self._service_action("stop", payload)

        self.send_error(404)

    def _memory_origin_allowed(self) -> bool:
        origin = self.headers.get("Origin")
        return origin is None or origin in MEMORY_ALLOWED_ORIGINS

    def _eve_upstream_path(self) -> str:
        parsed = urlparse(self.path)
        upstream = "/eve/v1/" + parsed.path[len("/api/eve/") :]
        return upstream + (f"?{parsed.query}" if parsed.query else "")

    def _read_eve_json(self) -> dict | None:
        raw_length = self.headers.get("Content-Length", "0")
        try:
            length = int(raw_length)
        except ValueError:
            self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
            return None
        if length < 0 or length > 1024 * 1024:
            status = 413 if length > 1024 * 1024 else 400
            self._send_json(status, {"ok": False, "error": "Invalid Eve request size."})
            return None
        if not length:
            return {}
        content_type = self.headers.get("Content-Type", "")
        if not content_type.casefold().startswith("application/json"):
            self._send_json(415, {"ok": False, "error": "Eve requests require application/json."})
            return None
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"ok": False, "error": "Invalid JSON body."})
            return None
        if not isinstance(payload, dict):
            self._send_json(400, {"ok": False, "error": "Expected a JSON object."})
            return None
        return payload

    def _eve_proxy_request(self, method: str, payload: dict | None = None) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        upstream_path = self._eve_upstream_path()
        try:
            response = eve_proxy.eve_request(method, upstream_path, payload)
        except eve_proxy.EveRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except eve_proxy.EveConnectionError:
            return self._send_json(502, {"ok": False, "error": "Eve is unavailable."})

        if response.is_stream:
            self.send_response(response.status)
            self.send_header("Content-Type", "application/x-ndjson; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            return self._write_eve_stream(
                response,
                eve_proxy.stream_start_index(upstream_path),
            )

        try:
            self.send_response(response.status)
            for name, value in response.headers.items():
                self.send_header(name, value)
            self.send_header("Content-Length", str(len(response.body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(response.body)
        except (BrokenPipeError, ConnectionResetError):
            return None
        finally:
            response.close()

    def _write_eve_stream(
        self,
        response: eve_proxy.EveResponse,
        upstream_next_index: int = 0,
    ) -> None:
        client_connected = True
        try:
            if response.stream is None:
                return
            for event in eve_proxy.iter_ndjson_records(response.stream):
                upstream_next_index += 1
                if event is None:
                    continue
                projected = eve_proxy.project_event(event)
                if projected is None:
                    continue
                projected = eve_proxy.with_upstream_next_index(
                    projected,
                    upstream_next_index,
                )
                line = json.dumps(projected, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
                self.wfile.write(line + b"\n")
                self.wfile.flush()
        except BrokenPipeError:
            client_connected = False
        except (OSError, TimeoutError):
            if client_connected:
                try:
                    line = json.dumps(
                        eve_proxy.PROXY_ERROR_EVENT,
                        separators=(",", ":"),
                    ).encode("utf-8")
                    self.wfile.write(line + b"\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, OSError):
                    pass
        finally:
            response.close()

    def _memory_recall(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        if content_length <= 0:
            return self._send_json(400, {"ok": False, "error": "Request body is required."})
        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON body must be an object."})
        query = str(payload.get("query") or "").strip()
        if not query:
            return self._send_json(400, {"ok": False, "error": "Query is required."})
        dataset = str(payload.get("dataset") or memory_api.DEFAULT_CHAT_RECALL_DATASET)
        try:
            result = memory_api.recall_for_chat(query, dataset=dataset)
        except ValueError as exc:
            return self._send_json(400, {"ok": False, "error": str(exc)})
        if not result.get("ok"):
            return self._send_json(503, result)
        return self._send_json(
            200,
            {
                "ok": True,
                "query": result.get("query"),
                "dataset": result.get("dataset"),
                "chunkCount": result.get("chunkCount", 0),
                "contextBlock": result.get("contextBlock", ""),
            },
        )

    def _memory_answer(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        if content_length <= 0:
            return self._send_json(400, {"ok": False, "error": "Request body is required."})
        try:
            body = self.rfile.read(content_length)
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        if not isinstance(payload, dict):
            return self._send_json(400, {"ok": False, "error": "JSON body must be an object."})
        query = str(payload.get("query") or "").strip()
        if not query:
            return self._send_json(400, {"ok": False, "error": "Query is required."})
        fast = bool(payload.get("fast"))
        result = memory_api.answer_memory_chat(query, fast=fast)
        if not result.get("ok"):
            return self._send_json(503, result)
        return self._send_json(
            200,
            {
                "ok": True,
                "answer": result.get("answer", ""),
                "chunkCount": result.get("chunkCount", 0),
                "model": result.get("model"),
                "sources": result.get("sources") or [],
            },
        )

    def _memory_optimize(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            content_length = 0
        payload: dict[str, object] = {}
        if content_length > 0:
            try:
                body = self.rfile.read(content_length)
                parsed = json.loads(body.decode("utf-8"))
                if isinstance(parsed, dict):
                    payload = parsed
            except (UnicodeDecodeError, json.JSONDecodeError):
                return self._send_json(400, {"ok": False, "error": "Could not parse JSON body."})
        max_files = payload.get("maxFiles", 60)
        fresh = bool(payload.get("fresh"))
        try:
            max_files_int = int(max_files)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            max_files_int = 60
        try:
            result = memory_api.run_optimize_eve_core(
                max_files=max_files_int,
                fresh=fresh,
            )
        except RuntimeError as exc:
            return self._send_json(503, {"ok": False, "error": str(exc)})
        return self._send_json(200, result)

    def _projects_catalog_get(self) -> None:
        rebuild = urlparse(self.path).query.find("rebuild=1") >= 0
        catalog = project_catalog.load_project_catalog(rebuild=rebuild)
        projects = [
            project_catalog.public_project(item)
            for item in catalog.get("projects", [])
            if isinstance(item, dict)
        ]
        return self._send_json(
            200,
            {
                "ok": True,
                "generatedAt": catalog.get("generated_at"),
                "projectCount": catalog.get("project_count", len(projects)),
                "inEveCoreCount": catalog.get("in_eve_core_count"),
                "flattenedCount": catalog.get("flattened_count"),
                "projects": projects,
            },
        )

    def _projects_catalog_refresh(self) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        catalog = project_catalog.save_project_catalog()
        projects = [
            project_catalog.public_project(item)
            for item in catalog.get("projects", [])
            if isinstance(item, dict)
        ]
        return self._send_json(
            200,
            {
                "ok": True,
                "generatedAt": catalog.get("generated_at"),
                "projectCount": len(projects),
                "projects": projects,
            },
        )

    def _memory_status(self) -> None:
        jobs = [memory_api.public_job(job) for job in memory_api.JOB_STORE.list()]
        return self._send_json(
            200,
            {
                "ok": True,
                "readiness": memory_api.memory_readiness(),
                "statuses": memory_api.STATUS_LABELS,
                "config": memory_api.memory_stack_config(),
                "eveCore": memory_api.eve_core_status(),
                "jobs": jobs,
            },
        )

    def _memory_job_get(self, path: str) -> None:
        job_id = path[len("/api/memory/jobs/") :].strip("/")
        if not job_id or "/" in job_id:
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            job = memory_api.JOB_STORE.read(job_id)
        except (KeyError, ValueError):
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        return self._send_json(200, {"ok": True, "job": memory_api.public_job(job)})

    def _memory_upload(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Length."})
        try:
            memory_api.DEFAULT_UPLOAD_POLICY.validate_request_size(content_length)
        except ValueError as exc:
            status = 413 if content_length > memory_api.DEFAULT_UPLOAD_POLICY.max_request_bytes else 400
            return self._send_json(status, {"ok": False, "error": str(exc)})

        content_type = self.headers.get("Content-Type", "")
        if not content_type.casefold().startswith("multipart/form-data"):
            return self._send_json(
                415,
                {"ok": False, "error": "Memory uploads require multipart/form-data."},
            )
        if "\r" in content_type or "\n" in content_type:
            return self._send_json(400, {"ok": False, "error": "Invalid Content-Type."})

        try:
            body = self.rfile.read(content_length)
            synthetic = (
                f"Content-Type: {content_type}\r\n"
                "MIME-Version: 1.0\r\n"
                "\r\n"
            ).encode("ascii", errors="strict")
            message = BytesParser(policy=policy.default).parsebytes(synthetic + body)
            if not message.is_multipart():
                raise ValueError("Malformed multipart upload.")
            parts = []
            fields: dict[str, str] = {}
            for part in message.iter_parts():
                disposition = part.get_content_disposition()
                if disposition != "form-data":
                    continue
                filename = part.get_filename()
                field_name = part.get_param("name", header="content-disposition")
                if filename is not None:
                    parts.append(part)
                elif field_name:
                    content = part.get_payload(decode=True) or b""
                    fields[str(field_name)] = content.decode(
                        part.get_content_charset() or "utf-8",
                        errors="strict",
                    )
            dataset = fields.get("dataset", "eve_memory").strip() or "eve_memory"
            full_graph_value = fields.get("full_graph", "false").strip().casefold()
            if full_graph_value not in {"true", "false", "1", "0", "yes", "no"}:
                raise ValueError("full_graph must be true or false.")
            full_graph = full_graph_value in {"true", "1", "yes"}
        except (UnicodeError, ValueError) as exc:
            message_text = str(exc)
            status = 413 if "too large" in message_text.casefold() or "exceeds" in message_text.casefold() else 400
            return self._send_json(status, {"ok": False, "error": message_text})
        except Exception:
            return self._send_json(
                400,
                {"ok": False, "error": "Could not parse multipart upload."},
            )

        try:
            job = memory_api.save_uploads(parts, dataset, full_graph)
        except memory_api.MemoryJobQueueError:
            return self._send_json(
                503,
                {"ok": False, "error": "Memory job queue is unavailable."},
            )
        except memory_api.MemoryUploadStorageError:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not save memory upload."},
            )
        except ValueError as exc:
            message_text = str(exc)
            status = 413 if "too large" in message_text.casefold() or "exceeds" in message_text.casefold() else 400
            return self._send_json(status, {"ok": False, "error": message_text})
        except Exception:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not save memory upload."},
            )
        return self._send_json(
            202,
            {"ok": True, "job": memory_api.public_job(job)},
        )

    def _memory_retry(self, path: str) -> None:
        prefix = "/api/memory/jobs/"
        job_id = path[len(prefix) : -len("/retry")].strip("/")
        if not job_id or "/" in job_id:
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            memory_api.JOB_STORE.read(job_id)
        except (KeyError, ValueError):
            return self._send_json(404, {"ok": False, "error": "Memory job not found."})
        try:
            memory_api.JOB_RUNNER.retry(job_id)
        except ValueError as exc:
            return self._send_json(409, {"ok": False, "error": str(exc)})
        except memory_api.MemoryJobQueueError:
            return self._send_json(
                503,
                {"ok": False, "error": "Memory job queue is unavailable."},
            )
        except Exception:
            return self._send_json(
                500,
                {"ok": False, "error": "Could not retry memory job."},
            )
        job = memory_api.JOB_STORE.read(job_id)
        return self._send_json(
            202,
            {"ok": True, "job": memory_api.public_job(job)},
        )

    def do_PUT(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/ollama/model":
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._ollama_set_model()
        if path.startswith("/api/chat-history/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._chat_history_put(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("PUT", path, self._read_json())
        self.send_error(404)

    def _ollama_models(self) -> None:
        try:
            tags = ollama_api.fetch_tags()
        except ollama_api.OllamaConnectionError:
            return self._send_json(
                503,
                ollama_api.models_status(
                    None,
                    connected=False,
                    error="Ollama is unavailable.",
                ),
            )
        payload = ollama_api.models_status(tags, connected=True)
        payload["inventory"] = ollama_inventory.build_inventory(tags)
        return self._send_json(200, payload)

    def _ollama_inventory(self) -> None:
        try:
            tags = ollama_api.fetch_tags()
        except ollama_api.OllamaConnectionError:
            return self._send_json(
                503,
                {"ok": False, "error": "Ollama is unavailable.", "models": [], "recommendations": {}},
            )
        return self._send_json(200, ollama_inventory.build_inventory(tags))

    def _ollama_set_model(self) -> None:
        payload = self._read_json()
        try:
            tags = ollama_api.fetch_tags()
            mode = payload.get("mode")
            if isinstance(mode, str) and mode.strip():
                result = ollama_api.set_active_model("", tags, mode=mode.strip())
            else:
                result = ollama_api.set_active_model(str(payload.get("model") or ""), tags)
        except ollama_api.OllamaConnectionError:
            return self._send_json(503, {"ok": False, "error": "Ollama is unavailable."})
        except ollama_api.OllamaRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        result["inventory"] = ollama_inventory.build_inventory(tags)
        return self._send_json(200, result)

    def _ollama_summarize_tasks(self) -> None:
        payload = self._read_json()
        tasks = payload.get("tasks") if isinstance(payload, dict) else None
        if not isinstance(tasks, list):
            tasks = []
        model = str(payload.get("model") or "").strip() if isinstance(payload, dict) else ""
        try:
            result = ollama_api.summarize_tasks(tasks, model=model or None)
        except ollama_api.OllamaConnectionError:
            return self._send_json(
                503,
                {"ok": False, "error": "Ollama could not summarize tasks."},
            )
        except ollama_api.OllamaRequestError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        return self._send_json(200, result)

    def do_PATCH(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("PATCH", path, self._read_json())
        self.send_error(404)

    def do_DELETE(self) -> None:
        path = urlparse(self.path).path
        if path.startswith("/api/chat-history/"):
            if not self._memory_origin_allowed():
                return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
            return self._chat_history_delete(path)
        if path.startswith("/api/wiki/"):
            return self._wiki_mutate("DELETE", path, {})
        self.send_error(404)

    def _chat_history_get(self, path: str) -> None:
        if not self._memory_origin_allowed():
            return self._send_json(403, {"ok": False, "error": "Origin is not allowed."})
        try:
            if path == "/api/chat-history":
                return self._send_json(200, chat_history.public_list())
            chat_id = path[len("/api/chat-history/") :].strip("/")
            if not chat_id or "/" in chat_id:
                return self._send_json(404, {"ok": False, "error": "Chat not found."})
            if chat_id == "active":
                active_id = chat_history.get_active_chat_id()
                return self._send_json(200, {"ok": True, "activeId": active_id})
            chat = chat_history.get_chat(chat_id)
            return self._send_json(200, {"ok": True, "chat": chat})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not load chat history."})

    def _chat_history_put(self, path: str) -> None:
        chat_id = path[len("/api/chat-history/") :].strip("/")
        if not chat_id or "/" in chat_id:
            return self._send_json(404, {"ok": False, "error": "Chat not found."})
        payload = self._read_json()
        try:
            chat = chat_history.upsert_chat(chat_id, payload)
            return self._send_json(200, {"ok": True, "chat": chat})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not save chat history."})

    def _chat_history_delete(self, path: str) -> None:
        chat_id = path[len("/api/chat-history/") :].strip("/")
        if not chat_id or "/" in chat_id:
            return self._send_json(404, {"ok": False, "error": "Chat not found."})
        try:
            if chat_id == "active":
                chat_history.clear_active_chat_id()
                return self._send_json(200, {"ok": True, "activeId": None})
            chat_history.delete_chat(chat_id)
            return self._send_json(200, {"ok": True, "id": chat_id})
        except chat_history.ChatHistoryError as exc:
            return self._send_json(exc.status, {"ok": False, "error": str(exc)})
        except Exception:
            return self._send_json(500, {"ok": False, "error": "Could not delete chat."})

    def _primitives_get(self) -> None:
        try:
            return self._send_json(200, primitives_api.primitives_status())
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _primitives_ingest(self, payload: dict) -> None:
        try:
            skip = bool(payload.get("skip_cognify"))
            return self._send_json(
                200,
                primitives_api.primitives_run_ingest(skip_cognify=skip),
            )
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _wiki_get(self, path: str) -> None:
        try:
            qs = wiki_api.parse_query(self.path)
            year = (qs.get("year") or ["2017"])[0]
            if path == "/api/wiki/status":
                return self._send_json(200, wiki_api.wiki_status(year))
            if path == "/api/wiki/titles":
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                q = (qs.get("q") or [""])[0]
                return self._send_json(
                    200,
                    wiki_api.wiki_titles(year, q=q, offset=offset, limit=limit),
                )
            if path == "/api/wiki/titles/letters":
                return self._send_json(200, wiki_api.wiki_letters(year))
            if path == "/api/wiki/titles/by-letter":
                letter = (qs.get("letter") or ["A"])[0]
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                q = (qs.get("q") or [""])[0]
                only_missing_raw = (qs.get("only_missing") or ["1"])[0].strip().lower()
                only_missing = only_missing_raw not in ("0", "false", "no")
                return self._send_json(
                    200,
                    wiki_api.wiki_titles_by_letter(
                        year,
                        letter,
                        offset=offset,
                        limit=limit,
                        q=q,
                        only_missing=only_missing,
                    ),
                )
            if path == "/api/wiki/new-titles":
                offset = int((qs.get("offset") or ["0"])[0])
                limit = int((qs.get("limit") or ["100"])[0])
                return self._send_json(
                    200,
                    wiki_api.wiki_new_titles(year, offset=offset, limit=limit),
                )
            if path == "/api/wiki/priorities":
                return self._send_json(200, wiki_api.wiki_priorities_get())
            return self._send_json(404, {"ok": False, "error": "Unknown wiki route"})
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _wiki_mutate(self, method: str, path: str, payload: dict) -> None:
        try:
            if path == "/api/wiki/priorities" and method == "PUT":
                return self._send_json(200, wiki_api.wiki_priorities_put(payload))
            if path == "/api/wiki/priorities" and method == "POST":
                return self._send_json(200, wiki_api.wiki_priorities_post(payload))
            if path == "/api/wiki/priorities/confirm" and method == "POST":
                return self._send_json(200, wiki_api.wiki_priorities_confirm(payload))
            if path == "/api/wiki/titles/queue" and method == "POST":
                return self._send_json(200, wiki_api.wiki_queue_articles(payload))
            if path.startswith("/api/wiki/priorities/") and method in ("PATCH", "DELETE"):
                subject_id = path[len("/api/wiki/priorities/") :].strip("/")
                if not subject_id or subject_id == "confirm":
                    return self._send_json(404, {"ok": False, "error": "Missing subject id"})
                if method == "PATCH":
                    return self._send_json(
                        200,
                        wiki_api.wiki_priorities_patch(subject_id, payload),
                    )
                return self._send_json(200, wiki_api.wiki_priorities_delete(subject_id))
            return self._send_json(404, {"ok": False, "error": "Unknown wiki route"})
        except Exception as exc:  # noqa: BLE001
            return self._send_json(400, {"ok": False, "error": str(exc)})

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length).decode("utf-8"))
        except json.JSONDecodeError:
            return {}

    def _run_verify_stack(self, payload: dict) -> None:
        python = ROOT / "venv" / "Scripts" / "python.exe"
        script = ROOT / "scripts" / "verify-stack.py"
        cmd = [str(python), str(script), "--json"]
        if payload.get("skipCognee"):
            cmd.append("--skip-cognee")
        if payload.get("fullIngest"):
            cmd.append("--full-ingest")
        result = subprocess.run(
            cmd,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=360,
        )
        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError:
            report = {
                "ok": False,
                "error": result.stderr.strip() or result.stdout.strip() or "verify-stack failed",
            }
        status = 200 if report.get("ok") else 500
        self._send_json(status, report)

    def _service_action(self, action: str, payload: dict) -> None:
        service = payload.get("service")
        services = payload.get("services") or ([] if not service else [service])

        if action == "stop" and "frontend" in services:
            return self._send_json(
                400,
                {
                    "ok": False,
                    "error": "Stopping the Tasks UI from the dashboard would shut down this page.",
                },
            )

        if action == "start" and payload.get("all"):
            services = []

        if action == "stop" and payload.get("all"):
            services = []

        config = load_config()
        if action == "start" and payload.get("all"):
            if not payload.get("skipOllamaCheck"):
                ollama = config["services"]["ollama"]
                health = wait_for_health(ollama, config["defaults"])
                if not health["ok"]:
                    return self._send_json(
                        500,
                        {"ok": False, "error": f"Ollama is not healthy: {health['detail']}"},
                    )
            result = roll_services("start", None, config)
            return self._finish_control(result)

        if action == "stop" and payload.get("all"):
            result = roll_services("stop", None, config)
            return self._finish_control(result)

        if not services:
            return self._send_json(400, {"ok": False, "error": "Missing service or services"})

        result = roll_services(action, services, config)
        return self._finish_control(result)

    def _finish_control(self, result: dict) -> None:
        refresh = run_ps_script(ROOT / "scripts" / "refresh-dashboard.ps1", timeout=60)
        status = 200 if result.get("ok") else 500
        result["refresh"] = refresh
        self._send_json(status, result)

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args) -> None:
        request = args[0] if args else ""
        if str(request).startswith("GET /api/") or str(request).startswith("POST /api/"):
            super().log_message(format, *args)


def main() -> int:
    server = EmpireHTTPServer((HOST, PORT), EmpireHandler)
    print(f"EMPIRE frontend + control API: http://{HOST}:{PORT}/")
    print(f"Dashboard: http://{HOST}:{PORT}/dashboard.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        return 0
    finally:
        server.server_close()


if __name__ == "__main__":
    sys.exit(main())
