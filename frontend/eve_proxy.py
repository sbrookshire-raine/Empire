"""Constrained local proxy helpers for the Eve 0.25 HTTP API."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from http.client import HTTPConnection, HTTPException, HTTPResponse
from typing import BinaryIO, Iterator
from urllib.parse import parse_qs, urlsplit

EVE_HOST = "127.0.0.1"
EVE_PORT = 2000
EVE_TIMEOUT_SECONDS = 15
EVE_STREAM_READ_TIMEOUT_SECONDS = 30
MAX_NDJSON_LINE_BYTES = 1024 * 1024
MAX_RESPONSE_BYTES = 2 * 1024 * 1024
MAX_SAFE_INTEGER = 9_007_199_254_740_991
SESSION_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")
PROXY_ERROR_EVENT = {
    "type": "proxy.error",
    "data": {"message": "Eve disconnected. You can retry this message."},
}
LOGGER = logging.getLogger(__name__)


class EveRequestError(ValueError):
    """Raised before connecting when a proxy request is not allowlisted."""

    def __init__(self, message: str, status: int = 404) -> None:
        super().__init__(message)
        self.status = status


class EveConnectionError(ConnectionError):
    """Sanitized upstream connectivity failure."""


@dataclass
class EveResponse:
    """An Eve response whose upstream resources must be closed."""

    status: int
    headers: dict[str, str]
    body: bytes
    stream: HTTPResponse | BinaryIO | None
    connection: HTTPConnection

    @property
    def is_stream(self) -> bool:
        return self.stream is not None

    def close(self) -> None:
        try:
            if self.stream is not None:
                self.stream.close()
        finally:
            self.connection.close()


def _validated_path(method: str, path: str) -> tuple[str, bool]:
    method = method.upper()
    parsed = urlsplit(path)
    if parsed.scheme or parsed.netloc or parsed.fragment:
        raise EveRequestError("Unknown Eve route.")

    route = parsed.path
    allowed_method: str | None = None
    is_stream = False
    if route == "/eve/v1/info":
        allowed_method = "GET"
    elif route == "/eve/v1/session":
        allowed_method = "POST"
    else:
        prefix = "/eve/v1/session/"
        if route.startswith(prefix):
            suffix = route[len(prefix) :]
            parts = suffix.split("/")
            if len(parts) == 1 and SESSION_ID_PATTERN.fullmatch(parts[0]):
                allowed_method = "POST"
            elif (
                len(parts) == 2
                and SESSION_ID_PATTERN.fullmatch(parts[0])
                and parts[1] == "cancel"
            ):
                allowed_method = "POST"
            elif (
                len(parts) == 2
                and SESSION_ID_PATTERN.fullmatch(parts[0])
                and parts[1] == "stream"
            ):
                allowed_method = "GET"
                is_stream = True

    if allowed_method is None:
        raise EveRequestError("Unknown Eve route.")
    if method != allowed_method:
        raise EveRequestError("Method is not allowed for this Eve route.", status=405)

    if parsed.query:
        if not is_stream:
            raise EveRequestError("Query parameters are not allowed for this Eve route.", status=400)
        try:
            query = parse_qs(parsed.query, keep_blank_values=True, strict_parsing=True)
        except ValueError as exc:
            raise EveRequestError("Invalid Eve stream query.", status=400) from exc
        if set(query) != {"startIndex"} or len(query["startIndex"]) != 1:
            raise EveRequestError("Only one startIndex query parameter is allowed.", status=400)
        raw_index = query["startIndex"][0]
        if not re.fullmatch(r"-?\d+", raw_index):
            raise EveRequestError("startIndex must be an integer.", status=400)
        index = int(raw_index)
        if abs(index) > MAX_SAFE_INTEGER:
            raise EveRequestError("startIndex is outside the supported range.", status=400)

    return path, is_stream


def validate_eve_request(method: str, path: str) -> None:
    """Validate a method/path pair without opening a connection."""

    _validated_path(method, path)


def stream_start_index(path: str) -> int:
    """Return the validated absolute stream cursor, defaulting to zero."""

    _path, is_stream = _validated_path("GET", path)
    if not is_stream:
        raise EveRequestError("Unknown Eve stream route.")
    query = parse_qs(urlsplit(path).query, keep_blank_values=True)
    return int(query["startIndex"][0]) if query else 0


def with_upstream_next_index(event: dict, next_index: int) -> dict:
    """Attach a safe cursor without exposing filtered upstream event content."""

    projected = dict(event)
    projected["_proxy"] = {"upstreamNextIndex": next_index}
    return projected


def _read_finite(response: HTTPResponse | BinaryIO) -> bytes:
    chunks: list[bytes] = []
    total = 0
    while True:
        chunk = response.read(64 * 1024)
        if not chunk:
            return b"".join(chunks)
        total += len(chunk)
        if total > MAX_RESPONSE_BYTES:
            raise EveConnectionError("Eve response was too large.")
        chunks.append(chunk)


def _safe_headers(response: HTTPResponse) -> dict[str, str]:
    source = {name.casefold(): value for name, value in response.getheaders()}
    content_type = source.get("content-type", "application/json; charset=utf-8")
    lowered = content_type.casefold()
    if "\r" in content_type or "\n" in content_type or not (
        lowered.startswith("application/json")
        or lowered.startswith("application/problem+json")
        or lowered.startswith("text/plain")
    ):
        content_type = "application/octet-stream"
    safe = {"Content-Type": content_type}
    session_id = source.get("x-eve-session-id")
    if session_id and "\r" not in session_id and "\n" not in session_id:
        safe["X-Eve-Session-Id"] = session_id
    return safe


def eve_request(method: str, path: str, payload: dict | None = None) -> EveResponse:
    """Forward one allowlisted request to the loopback Eve service."""

    upstream_path, requested_stream = _validated_path(method, path)
    method = method.upper()
    if payload is not None and not isinstance(payload, dict):
        raise EveRequestError("Eve payload must be a JSON object.", status=400)

    body = None
    headers = {"Accept": "application/x-ndjson" if requested_stream else "application/json"}
    if method == "POST":
        body = json.dumps(payload or {}, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"

    connection = HTTPConnection(EVE_HOST, EVE_PORT, timeout=EVE_TIMEOUT_SECONDS)
    try:
        connection.request(method, upstream_path, body=body, headers=headers)
        response = connection.getresponse()
        if requested_stream and 200 <= response.status < 300:
            sock = getattr(connection, "sock", None)
            if sock is not None:
                sock.settimeout(EVE_STREAM_READ_TIMEOUT_SECONDS)
            return EveResponse(
                status=response.status,
                headers={},
                body=b"",
                stream=response,
                connection=connection,
            )
        response_body = _read_finite(response)
        result = EveResponse(
            status=response.status,
            headers=_safe_headers(response),
            body=response_body,
            stream=None,
            connection=connection,
        )
        response.close()
        return result
    except EveConnectionError:
        connection.close()
        raise
    except (HTTPException, OSError, TimeoutError) as exc:
        connection.close()
        raise EveConnectionError("Eve is unavailable.") from exc


def iter_ndjson_records(stream: BinaryIO) -> Iterator[dict | None]:
    """Yield every durable record, using None for safely dropped records."""

    while True:
        raw_line = stream.readline(MAX_NDJSON_LINE_BYTES + 1)
        if not raw_line:
            break
        if len(raw_line) > MAX_NDJSON_LINE_BYTES:
            LOGGER.warning("Dropped oversized Eve NDJSON record.")
            while raw_line and not raw_line.endswith(b"\n"):
                raw_line = stream.readline(MAX_NDJSON_LINE_BYTES + 1)
            yield None
            continue
        if not raw_line.strip():
            continue
        event = _parse_event_line(raw_line)
        yield event


def iter_ndjson(stream: BinaryIO) -> Iterator[dict]:
    """Yield valid object records as soon as each NDJSON line arrives."""

    for event in iter_ndjson_records(stream):
        if event is not None:
            yield event


def _parse_event_line(raw_line: bytes) -> dict | None:
    if not raw_line.strip():
        return None
    try:
        event = json.loads(raw_line)
    except (UnicodeDecodeError, json.JSONDecodeError):
        LOGGER.warning("Dropped malformed Eve NDJSON record.")
        return None
    if not isinstance(event, dict):
        LOGGER.warning("Dropped non-object Eve NDJSON record.")
        return None
    return event


def project_event(event: dict) -> dict | None:
    """Remove private reasoning events and reject malformed event envelopes."""

    event_type = event.get("type")
    if not isinstance(event_type, str) or not event_type:
        return None
    data = event.get("data")
    if data is not None and not isinstance(data, dict):
        return None
    normalized = re.sub(r"[^a-z0-9]+", ".", event_type.casefold()).strip(".")
    tokens = normalized.split(".")
    if "reasoning" in tokens or "thinking" in tokens:
        return None
    return event
