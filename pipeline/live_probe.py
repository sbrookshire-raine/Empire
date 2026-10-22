"""Live turn evidence: what Eve actually called, and whether it was the *right* tool.

Why this exists
---------------
The live harnesses so far proved "a tool was called" by grepping the raw
NDJSON blob for a tool name and the string ``"tool-call"``. That is weak in
two ways, both measured on the live stack (2026-10-21):

1. A **string match is not a tool call.** The model sometimes writes its
   tool call as *content* ("Called wiki_read_section with object(...)") and
   no ``actions.requested`` event is ever emitted. The blob still contains
   the tool name, so a grep says "called" when nothing ran.
2. The **wrong** tool matches just as well as the right one. "Eve called
   some tool" is not a routing claim.

So this module reads the **structured** events the framework actually emits
and turns one turn into evidence:

- ``actions.requested`` -> ``data.actions[]`` with ``toolName`` (the request)
- ``action.result``     -> ``data.result.toolName`` + ``data.status`` (the outcome)
- ``message.completed`` -> ``data.message`` (the answer)

A ``TurnEvidence`` therefore knows which tools were requested, which
succeeded, and what was said — and ``assert_correct_tool`` can then ask the
routing question the corpus cares about: *for this intent, was the tool that
belongs to the route the one that actually ran?*

The expected tool is not hard-coded here. It is derived from the **same**
shared classifier and intent codex the running system uses
(``pipeline.route_classifier`` + ``pipeline.intent_codex``), so the battery
cannot drift from the routing rules it is supposed to police.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any

from pipeline import intent_codex, route_classifier

# The events the framework emits for one turn. Names match `eve_proxy`'s
# projected stream (`frontend/serve.py` proxies them verbatim).
ACTIONS_REQUESTED = "actions.requested"
ACTION_RESULT = "action.result"
MESSAGE_COMPLETED = "message.completed"
MESSAGE_APPENDED = "message.appended"

# Turn-ending events. `turn.completed` fires per step, `session.waiting` when
# Eve hands control back — either is the end of what we asked for.
TURN_END_EVENTS = frozenset({"session.waiting", "turn.completed", "session.completed"})


@dataclass
class ToolCall:
    """One tool request, as the framework reported it."""

    tool: str
    call_id: str = ""
    arguments: dict[str, Any] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return self.tool or "<unnamed>"


@dataclass
class ToolOutcome:
    """One tool result: did it succeed, and what did it say?"""

    tool: str
    status: str = ""
    output: Any = None

    @property
    def ok(self) -> bool:
        return str(self.status).casefold() in {"completed", "ok", "success"}


@dataclass
class TurnEvidence:
    """Everything one live turn proved."""

    prompt: str = ""
    assistant_text: str = ""
    calls: list[ToolCall] = field(default_factory=list)
    outcomes: list[ToolOutcome] = field(default_factory=list)
    ended: bool = False
    error: str = ""

    @property
    def tools_called(self) -> list[str]:
        """Tool names requested, in order, de-duplicated."""
        seen: list[str] = []
        for call in self.calls:
            if call.tool and call.tool not in seen:
                seen.append(call.tool)
        return seen

    @property
    def succeeded_tools(self) -> list[str]:
        return [o.tool for o in self.outcomes if o.ok and o.tool]

    def called(self, tool: str) -> bool:
        return any(call.tool == tool for call in self.calls)

    def summary(self) -> dict[str, Any]:
        return {
            "prompt": self.prompt,
            "tools_called": self.tools_called,
            "succeeded_tools": self.succeeded_tools,
            "ended": self.ended,
            "error": self.error,
            "assistant_text": self.assistant_text[:400],
        }


def _action_tool_names(data: Any) -> list[tuple[str, str, dict[str, Any]]]:
    """(toolName, callId, input) for each tool-call action in an event payload."""
    if not isinstance(data, dict):
        return []
    out: list[tuple[str, str, dict[str, Any]]] = []
    for action in data.get("actions") or []:
        if not isinstance(action, dict):
            continue
        if str(action.get("kind") or "tool-call") != "tool-call":
            continue
        name = str(action.get("toolName") or "").strip()
        if not name:
            continue
        args = action.get("input")
        out.append((name, str(action.get("callId") or ""), args if isinstance(args, dict) else {}))
    return out


def read_turn(events: Iterable[dict], *, prompt: str = "") -> TurnEvidence:
    """Turn a stream of framework events into structured evidence.

    Accepts the raw NDJSON records (dicts) in arrival order. Malformed or
    unrelated records are ignored rather than fatal: a probe must report
    what it saw, not crash on one odd line.
    """
    evidence = TurnEvidence(prompt=prompt)
    for event in events:
        if not isinstance(event, dict):
            continue
        etype = str(event.get("type") or "")
        data = event.get("data")
        if etype == ACTIONS_REQUESTED:
            for name, call_id, args in _action_tool_names(data):
                evidence.calls.append(ToolCall(tool=name, call_id=call_id, arguments=args))
        elif etype == ACTION_RESULT:
            tool = ""
            output: Any = None
            status = ""
            if isinstance(data, dict):
                status = str(data.get("status") or "")
                result = data.get("result")
                if isinstance(result, dict):
                    tool = str(result.get("toolName") or "").strip()
                    output = result.get("output")
            if tool:
                evidence.outcomes.append(ToolOutcome(tool=tool, status=status, output=output))
        elif etype == MESSAGE_COMPLETED:
            if isinstance(data, dict):
                text = data.get("message")
                if isinstance(text, str) and text.strip():
                    evidence.assistant_text = text
        elif etype in TURN_END_EVENTS:
            evidence.ended = True
    return evidence


def parse_ndjson(lines: Iterable[str]) -> list[dict]:
    """Parse NDJSON lines into records, skipping blanks and malformed lines."""
    records: list[dict] = []
    for line in lines:
        text = (line or "").strip()
        if not text:
            continue
        try:
            record = json.loads(text)
        except (TypeError, ValueError):
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def expected_tools_for(prompt: str) -> tuple[str, list[str]]:
    """(route, tools) that this prompt should route to, per the shared rules.

    This is the whole point: the expectation is derived from the *same*
    classifier and codex the live system uses, so the battery cannot assert
    something the system does not claim.
    """
    route = route_classifier.classify(prompt)
    primary = (intent_codex.resolve(prompt).get("primary") or {})
    tools = [str(t) for t in (primary.get("local_tools") or []) if str(t).strip()]
    return route, tools


# The codex intent that owns each named route, and the tools it owns. Read
# from the codex file itself so the families cannot drift from the policy the
# running system applies.
ROUTE_INTENTS: dict[str, str] = {
    route_classifier.WIKI: "wiki_fact",
    route_classifier.MEMORY: "remember_recall",
    route_classifier.TASK: "task_todo",
}


def route_tool_families() -> dict[str, list[str]]:
    """{route: [tools]} for the three named routes, read from the codex."""
    families: dict[str, list[str]] = {}
    for route, intent_id in ROUTE_INTENTS.items():
        tools: list[str] = []
        for intent in intent_codex.load_intents():
            if str(intent.get("id") or "") != intent_id:
                continue
            policy = intent.get("policy") or {}
            tools = [str(t) for t in (policy.get("local_tools") or []) if str(t).strip()]
            break
        families[route] = tools
    return families


def forbidden_tools_for(route: str) -> list[str]:
    """Tools that belong to a *different* named route than this one.

    A non-wiki ask that reaches for the wiki tools is the exact regression
    this battery exists to catch: "what is my disk space" was routed to the
    encyclopedia because the bare verb "what" scored.
    """
    families = route_tool_families()
    return sorted({t for name, tools in families.items() if name != route for t in tools})

def assert_correct_tool(
    evidence: TurnEvidence,
    prompt: str,
    *,
    allowed: Iterable[str] | None = None,
) -> dict[str, Any]:
    """Did the turn use a tool its route implies, and avoid the others?

    The contract has two halves, because "did she call a tool" is the wrong
    question on its own:

    1. **No foreign tool.** A tool from another named route (the wiki tools
       for a task question, say) is a routing error even if the turn
       answered well. This is the regression the shared classifier fixed.
    2. **Right tool, when one is due.** A route that owns tools should
       reach one of them -- but only when the server did not already
       prefetch the evidence. The green path (frontend/wiki_green_path.py)
       answers a wiki ask from a prefetched extract and tells Eve to skip
       the tool call, so "no tool called" is CORRECT there. The caller
       passes ``allowed`` to say which tools that route may use.
    """
    route, expected = expected_tools_for(prompt)
    permitted = [t for t in (allowed if allowed is not None else expected) if t]
    called = evidence.tools_called
    foreign = [name for name in forbidden_tools_for(route) if name in called]

    base = {
        "route": route,
        "expected": permitted,
        "called": called,
        "foreign": foreign,
    }

    if foreign:
        return {
            **base,
            "ok": False,
            "reason": f"called {foreign}, which belong to a different route than {route!r}",
        }
    if not called:
        # No tool call. That is only a failure when the route demands one and
        # the server did not prefetch the answer for it.
        if permitted:
            return {
                **base,
                "ok": False,
                "reason": (
                    f"no tool was called; route {route!r} expects one of {permitted} "
                    "and no prefetched evidence was supplied"
                ),
            }
        return {
            **base,
            "ok": True,
            "reason": "no tool called, and this route requires none",
        }
    if not permitted:
        return {
            **base,
            "ok": True,
            "reason": f"called {called}; this route has no tool requirement",
        }
    matched = [name for name in called if name in permitted]
    if not matched:
        return {
            **base,
            "ok": False,
            "reason": f"called {called} but this route expects one of {permitted}",
        }
    return {
        **base,
        "ok": True,
        "reason": f"called {matched}",
    }
