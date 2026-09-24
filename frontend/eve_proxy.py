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
EVE_TIMEOUT_SECONDS = 30
EVE_STREAM_READ_TIMEOUT_SECONDS = 300
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


# Model "wrapper" tags that are scratch, never prose. `translation` is Qwen leaking its tool-call
# template: measured live, the model emitted `<translation>{"name": "wiki_scout_search", ...}
# </translation>` as assistant *content*, which then got displayed and spoken aloud.
_SCRATCH_TAG = r"(?:think|thinking|thought|thoughts|reasoning)"
_TAG_FAMILY = r"(?:think|thinking|thought|thoughts|reasoning|translation)"
_TAG_STEMS = (
    "<think",
    "<thinking",
    "<thought",
    "<thoughts",
    "<reasoning",
    "<translation",
)
_WRAPPER_BLOCK_RE = re.compile(
    rf"<{_TAG_FAMILY}\b[^>]*>.*?</{_TAG_FAMILY}>",
    re.DOTALL | re.IGNORECASE,
)
_THINK_BLOCK_RE = _WRAPPER_BLOCK_RE
# Only true reasoning scratch truncates everything after an unclosed tag — a lone
# `<translation …>` stage direction is dropped by itself and the answer below it survives.
_THINK_OPEN_RE = re.compile(rf"<{_SCRATCH_TAG}\b[^>]*>", re.IGNORECASE)
_TAG_OPEN_RE = re.compile(rf"<{_TAG_FAMILY}\b[^>]*>", re.IGNORECASE)
_THINK_CLOSE_RE = re.compile(rf"</{_TAG_FAMILY}\s*>", re.IGNORECASE)
_LONE_TRANSLATION_OPEN_RE = re.compile(r"<translation\b[^>]*>", re.IGNORECASE)


def _drop_trailing_partial_tag(text: str) -> str:
    """Drop a trailing tag fragment with no `>` yet (measured leaked value: `"<thought"`)."""

    cut = text.rfind("<")
    if cut == -1:
        return text
    tail = text[cut:]
    if ">" in tail or "</" in tail:
        return text
    candidate = tail.casefold()
    if any(stem.startswith(candidate) for stem in _TAG_STEMS):
        return text[:cut]
    return text


def strip_reasoning_blocks(text: str) -> str:
    """Drop `<thought>` / `<think>` scratch, including a block that is still streaming.

    The MANDATORY EXECUTION PROTOCOL makes the model write its reasoning in `<thought>`
    tags. Those are internal scratch: complete blocks are removed here, and a dangling
    opening tag (no closing tag yet, mid-stream) truncates the tail so partial reasoning
    never flashes in the user-visible transcript. Raw upstream text keeps the blocks for
    debugging.
    """

    if not text:
        return text
    cleaned = _WRAPPER_BLOCK_RE.sub("", text)
    dangling = _THINK_OPEN_RE.search(cleaned)
    if dangling:
        cleaned = cleaned[: dangling.start()]
    cleaned = _LONE_TRANSLATION_OPEN_RE.sub("", cleaned)
    return _drop_trailing_partial_tag(cleaned)


class ReasoningStreamFilter:
    """Stateful per-step filter for streamed assistant text.

    Per-event filtering is not enough: once a step has opened `<thought`, its *deltas* carry
    only the block body (`Have:none.`, `Next:…`) and would leak to the client — which is how
    the Workbench ended up *speaking* Eve's reasoning aloud. This filter tracks whether it is
    inside a block and withholds everything until the closing tag arrives.
    """

    def __init__(self) -> None:
        self.in_block = False
        self.pending = ""

    _TAG_STEMS = _TAG_STEMS  # module-level stems, shared with the stateless stripper

    def _split_partial_tag(self, text: str, *, inside_block: bool) -> tuple[str, str]:
        """Split a trailing partial tag off `text` — returns (kept, held-back).

        Streams split tags across deltas ("<thou" + "ght>"), so a trailing fragment that could
        still become a tag must be withheld, never emitted as text.
        """

        cut = text.rfind("<")
        if cut == -1:
            return text, ""
        tail = text[cut:]
        if ">" in tail:
            return text, ""
        candidate = tail.casefold()
        if candidate.startswith("</"):
            body = candidate[2:]
            if inside_block and any(stem[1:].startswith(body) for stem in self._TAG_STEMS):
                return text[:cut], tail
            return text, ""
        if any(stem.startswith(candidate) for stem in self._TAG_STEMS):
            return text[:cut], tail
        return text, ""

    def feed(self, text: str) -> str:
        """Return `text` minus reasoning scratch, remembering open blocks across calls."""

        combined = (self.pending or "") + (text or "")
        self.pending = ""
        if not combined:
            return combined
        combined, held = self._split_partial_tag(combined, inside_block=self.in_block)
        self.pending = held
        out: list[str] = []
        index = 0
        while index < len(combined):
            if self.in_block:
                closing = _THINK_CLOSE_RE.search(combined, index)
                if not closing:
                    return "".join(out)
                self.in_block = False
                index = closing.end()
                continue
            opening = _TAG_OPEN_RE.search(combined, index)
            if not opening:
                out.append(combined[index:])
                break
            out.append(combined[index : opening.start()])
            self.in_block = True
            index = opening.end()
        return "".join(out)


def filter_stream_event(event: dict, filters: dict) -> dict:
    """Apply reasoning filtering to one projected stream event.

    `messageDelta` fragments are filtered with a per-step *stateful* filter (a delta inside an
    open `<thought>` carries no tag, so stateless stripping would let it through); cumulative
    fields use the stateless stripper. Everything else passes through untouched.
    """

    event_type = str(event.get("type") or "")
    if event_type not in {"message.appended", "message.completed"}:
        return event
    data = event.get("data")
    if not isinstance(data, dict):
        return event
    role = data.get("role")
    if isinstance(role, str) and role.casefold() == "user":
        return event
    try:
        step = int(data.get("stepIndex") or 0)
    except (TypeError, ValueError):
        step = 0
    stream_filter = filters.get(step)
    if stream_filter is None:
        stream_filter = ReasoningStreamFilter()
        filters[step] = stream_filter
    patched = dict(data)
    delta = patched.get("messageDelta")
    if isinstance(delta, str):
        patched["messageDelta"] = stream_filter.feed(delta)
    for key in ("message", "messageSoFar", "delta", "text", "content"):
        value = patched.get(key)
        if isinstance(value, str):
            patched[key] = strip_reasoning_blocks(value)
    filtered = dict(event)
    filtered["data"] = patched
    return filtered


_META_TOOL_NARRATION_RE = re.compile(
    r"\b(?:will not call any tools?|no tools? (?:are )?needed|without (?:using|calling) tools?)\b",
    re.IGNORECASE,
)
_META_PREAMBLE_RE = re.compile(
    r"^(?:since|because)\b.+?(?:\.\s*|\s+)",
    re.IGNORECASE | re.DOTALL,
)
_QUOTED_REPLY_RE = re.compile(
    r'(?:A simple response would be|The (?:best )?response (?:is|would be)|I should (?:say|respond with)):\s*["“](.+?)["”]\.?\s*$',
    re.IGNORECASE | re.DOTALL,
)
_INSTRUCTION_LEAK_RE = re.compile(
    r"\b(?:according to (?:my )?instructions|as per (?:the )?guidelines|per my (?:system )?prompt)\b",
    re.IGNORECASE,
)
# Degenerate leading non-Latin runs (observed: Thai tokens before the answer on a long prompt).
# Only a *leading* run is dropped, so a foreign title mid-answer still survives.
_LEADING_NONLATIN_RE = re.compile(
    r"^[\s\u0e00-\u0e7f\u4e00-\u9fff\u3040-\u30ff\u0400-\u04ff\u0600-\u06ff\u0590-\u05ff]{3,}"
)
# Internal markers (chat digest, wiki evidence, pulse, NOW) are prompt scaffolding, not prose.
# A model that echoes them into its reply must not expose them to the user. The digest marker
# contains spaces ("[[EMPIRE CHAT SUMMARY]]") — measured 2026-09-24, it reached the speaker — and the
# digest body rides on the same line, so whole marker lines are dropped.
_INTERNAL_MARKER_RE = re.compile(r"\[\[EMPIRE[ _][A-Z0-9_ ]+\]\]")
# A marker at line start means the whole line is scaffolding (the digest body rides on it); a marker
# mid-line is just noise to remove, so real text on that line survives.
_INTERNAL_MARKER_LINE_RE = re.compile(r"^[ \t]*\[\[EMPIRE[ _][A-Z0-9_ ]+\]\].*$", re.MULTILINE)
# The injected blocks are multi-line: companion_api writes "[[EMPIRE_NOW]]\nCURRENT facts:\n<body>".
# Measured 2026-09-24: the marker line was stripped but the body was still *spoken*. Drop the marker
# line plus the following non-empty lines (bounded), because a marker only appears when the model is
# echoing injected scaffolding.
_INTERNAL_BLOCK_RE = re.compile(
    r"^[ \t]*\[\[EMPIRE[ _][A-Z0-9_ ]+\]\][^\n]*\n(?:(?![ \t]*\n)[^\n]*\n){0,14}",
    re.MULTILINE,
)
# Explicit end markers (companion_api) let us drop a block deterministically, whatever subset of its
# lines the model echoes.
_INTERNAL_MARKER_END_RE = re.compile(r"^[ \t]*\[\[EMPIRE[ _][A-Z0-9_ ]*END\]\][^\n]*$", re.MULTILINE)


# The companion payload continues *after* `[[EMPIRE_NOW_END]]` with its instruction tail — the ROLE
# line, "For greetings: …", "Do not mention these markers…" — and then the "User message:" header.
# Measured 2026-09-24: on a how-to question the model echoed the payload, and 499 chars of that tail
# survived the marker..END rule and reached the bubble. Those lines are never prose, and in an echoed
# reply everything after them is the user's own message, so the reply is truncated from the first tail
# line. Only applied when an internal marker is present, so an answer that legitimately quotes a line
# like "ROLE: backend engineer" is untouched.
_COMPANION_TAIL_RE = re.compile(
    r"^[ \t]*(?:ROLE:[^\n]*|For greetings:[^\n]*|Do not mention these markers[^\n]*|User message:)[ \t]*$",
    re.MULTILINE,
)


def _drop_scaffolding_blocks(text: str) -> str:
    """Remove injected prompt blocks: marker..END when present, else marker + bounded tail."""

    if _INTERNAL_MARKER_RE.search(text):
        tail_match = _COMPANION_TAIL_RE.search(text)
        if tail_match:
            text = text[: tail_match.start()]
    end_match = _INTERNAL_MARKER_END_RE.search(text)
    if end_match:
        start_match = _INTERNAL_MARKER_LINE_RE.search(text)
        if start_match and start_match.start() < end_match.start():
            last_end = list(_INTERNAL_MARKER_END_RE.finditer(text))[-1]
            return text[: start_match.start()] + text[last_end.end() :]
    return _INTERNAL_BLOCK_RE.sub("", text)
# Bare call-expression leaks: the model sometimes renders the call it *wanted* to make as text —
# measured 2026-09-24 on empire-fast:7b, whose entire reply was
# `wiki_read_section("magnetism", section="magnetic_fields_and_theory")` (and the speaker read it).
# Restricted to EMPIRE's tool namespace so real code the user may be discussing (`print("hi")`,
# `df.head()` inside an explanation) is never touched.
_TOOL_NAMESPACE = (
    r"wiki|cognee|daze|stem|switchboard|workbench|author|python|voice|vision|web|github|container|"
    r"loom|resource|admit|release|request|promote|remember|docling|docs|structured|retrieval|"
    r"browser|query|search|list|create|update|delete|read|write|check|drop|glob|grep|bash"
)
_BARE_TOOL_CALL_RE = re.compile(
    rf"^[ \t>*\-]*(?:{_TOOL_NAMESPACE})_[a-z0-9_]+\s*\(\s*"
    r"(?:\"[^\"]*\"|'[^']*'|[a-z_]+\s*=\s*[\"'][^\"']*[\"'])"
    r"(?:\s*,\s*[a-z_]+\s*=\s*(?:\"[^\"]*\"|'[^']*'|\d+|true|false))*\s*\)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
# Qwen's tool-call template sometimes renders as *prose* instead of a real tool_call, e.g.
# "Called wiki_read_section with object(title=magnetism, section=basics, year=2026)" (observed
# live 2026-09-23). It is template scaffolding, never a sentence to show or speak.
_TOOL_CALL_AS_TEXT_RE = re.compile(
    r"^\s*(?:[-*>]\s*)?(?:called|invoking|invoke|call|requesting|request)\s+"
    r"[a-z_][a-z0-9_]{2,}\s+(?:with|using)\s+(?:object\(|\{[^}]*\}|[a-z_]+\s*=).*$",
    re.IGNORECASE | re.MULTILINE,
)
# If stripping leaves nothing, the turn produced no usable answer — say so instead of an empty
# bubble (an empty bubble reads as a hung UI and hides the failure).
EMPTY_AFTER_CLEAN_REPLY = "That answer didn't come through — ask me again and I'll retry it."
# The reasoning protocol's scratch lines ("Ask: … Have: … Next: …") are supposed to live inside a
# <thought> block, but the model sometimes emits one *bare* (measured 2026-09-24: the speech path
# received "Ask:howdomagnetswork." while the final reply was clean). A leading label + colon is
# never prose, so drop the whole line; "Ask me anything" has no colon and survives.
_PROTOCOL_SCRATCH_LINE_RE = re.compile(
    r"^[ \t>*\-]*(?:ask|have|next|plan|step|thought|reasoning)\s*:.*$",
    re.IGNORECASE | re.MULTILINE,
)


def _looks_like_meta_preamble(text: str) -> bool:
    lowered = text.casefold()
    if _META_TOOL_NARRATION_RE.search(text):
        return True
    if _INSTRUCTION_LEAK_RE.search(text):
        return True
    if "since the input" in lowered or "since this is a question" in lowered:
        return True
    if "a simple response would be" in lowered:
        return True
    return False


# A model that wanders can emit stage-direction fragments at the start of a reply, e.g.
# "<translation into actionable steps>\n\n**Next Steps:** ..." (observed live on a long prompt).
# Restricted to prose-like fragments (letters, spaces, hyphens) so literal markup a user might be
# discussing — "<img src=x onerror=alert(1)>", "<div class=\"x\">" — is left untouched.
_LEADING_STAGE_DIRECTION_RE = re.compile(
    r"^\s*<(?![^<>\n]*[=/'\"\\])([A-Za-z][A-Za-z \-]{2,60})>\s*",
    re.MULTILINE,
)


def sanitize_assistant_text(text: str) -> str:
    """Strip leaked reasoning / meta-commentary from assistant-visible text."""

    if not text:
        return text
    cleaned = strip_reasoning_blocks(text).strip()
    cleaned = _LEADING_NONLATIN_RE.sub("", cleaned).strip()
    if _INTERNAL_MARKER_RE.search(cleaned):
        cleaned = _drop_scaffolding_blocks(cleaned)
        cleaned = _INTERNAL_MARKER_LINE_RE.sub("", cleaned)
        cleaned = _INTERNAL_MARKER_RE.sub("", cleaned).strip()
    # Drop tool-call scaffolding the model wrote as prose ("Called wiki_read_section with
    # object(title=...)") — it is never part of the answer and must not be spoken either.
    if _TOOL_CALL_AS_TEXT_RE.search(cleaned):
        cleaned = _TOOL_CALL_AS_TEXT_RE.sub("", cleaned).strip()
        if not cleaned:
            return EMPTY_AFTER_CLEAN_REPLY
    # Bare reasoning-protocol scratch lines (no <thought> wrapper) are scratch too.
    if _PROTOCOL_SCRATCH_LINE_RE.search(cleaned):
        stripped_lines = _PROTOCOL_SCRATCH_LINE_RE.sub("", cleaned).strip()
        if not stripped_lines:
            return EMPTY_AFTER_CLEAN_REPLY
        cleaned = stripped_lines
    # A bare call expression ("wiki_read_section(\"magnetism\", section=\"…\")") is not an answer.
    if _BARE_TOOL_CALL_RE.search(cleaned):
        stripped_call = _BARE_TOOL_CALL_RE.sub("", cleaned).strip()
        if not stripped_call:
            return EMPTY_AFTER_CLEAN_REPLY
        cleaned = stripped_call
    # Trim leading stage-direction fragments ("<translation into actionable steps>") that the
    # model sometimes emits before the real answer.
    while True:
        trimmed = _LEADING_STAGE_DIRECTION_RE.sub("", cleaned).strip()
        if trimmed == cleaned:
            break
        cleaned = trimmed
    if not cleaned:
        return cleaned

    quoted = _QUOTED_REPLY_RE.search(cleaned)
    if quoted and _looks_like_meta_preamble(cleaned[: quoted.start()]):
        return quoted.group(1).strip()

    if _looks_like_meta_preamble(cleaned):
        stripped = _META_PREAMBLE_RE.sub("", cleaned, count=1).strip()
        quoted_after = _QUOTED_REPLY_RE.search(stripped)
        if quoted_after:
            return quoted_after.group(1).strip()
        if stripped and stripped != cleaned:
            return stripped

    return cleaned


def _sanitize_message_data(data: dict) -> dict:
    sanitized = dict(data)
    for key in ("message", "messageSoFar", "messageDelta", "delta"):
        value = sanitized.get(key)
        if isinstance(value, str):
            sanitized[key] = sanitize_assistant_text(value)
    return sanitized


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
    if event_type in {"message.appended", "message.completed"} and isinstance(data, dict):
        role = data.get("role")
        if role is None or (isinstance(role, str) and role.casefold() != "user"):
            projected = dict(event)
            projected["data"] = _sanitize_message_data(data)
            return projected
    return event
