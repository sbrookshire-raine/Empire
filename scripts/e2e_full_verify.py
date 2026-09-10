"""Comprehensive Truth Drift / Eve / glasses verification harness."""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from typing import Any

ORIGIN = "http://127.0.0.1:8080"
REPORT = r"C:\Empire_Workbench\04_Thought_Experiments\wiki_cache\e2e_full_verify_last.json"


@dataclass
class CaseResult:
    name: str
    ok: bool
    detail: str


def _req(
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    *,
    timeout: float = 180,
) -> tuple[int, Any]:
    data = None
    headers = {"Origin": ORIGIN, "Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(
        ORIGIN + path, data=data, headers=headers, method=method
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            return exc.code, json.loads(body) if body else {}
        except json.JSONDecodeError:
            return exc.code, {"raw": body}
    except Exception as exc:  # noqa: BLE001
        return 599, {"error": str(exc)}


def stream_final_text(session_id: str, *, max_seconds: float = 240) -> dict[str, Any]:
    url = f"{ORIGIN}/api/eve/session/{session_id}/stream?startIndex=0"
    request = urllib.request.Request(
        url, headers={"Origin": ORIGIN, "Accept": "application/x-ndjson"}
    )
    tools: list[str] = []
    final = ""
    errors: list[str] = []
    deadline = time.time() + max_seconds
    with urllib.request.urlopen(request, timeout=max_seconds) as resp:
        while time.time() < deadline:
            line = resp.readline()
            if not line:
                break
            raw = line.decode("utf-8", errors="replace").strip()
            if not raw:
                continue
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            et = str(event.get("type") or "")
            data = event.get("data") if isinstance(event.get("data"), dict) else {}
            if et == "actions.requested":
                for action in data.get("actions") or []:
                    if isinstance(action, dict):
                        tools.append(str(action.get("toolName") or ""))
            if et == "message.appended":
                final = str(data.get("messageSoFar") or final)
            if et == "message.completed":
                content = (
                    data.get("text")
                    or data.get("content")
                    or data.get("messageSoFar")
                )
                if content:
                    final = str(content)
            if et in {"session.error", "proxy.error", "error"}:
                errors.append(json.dumps(data)[:300])
            if et == "session.waiting":
                break
    return {"text": final, "tools": tools, "errors": errors}


def eve_ask(message: str, *, mode: str = "fast") -> dict[str, Any]:
    status, payload = _req(
        "POST",
        "/api/eve/session",
        {
            "message": message,
            "mode": mode,
            "active_tools": ["wiki_local"],
        },
        timeout=150,
    )
    if status >= 400 or not isinstance(payload, dict) or not payload.get("sessionId"):
        return {
            "ok": False,
            "error": f"session {status}: {payload}",
            "text": "",
            "tools": [],
        }
    sid = str(payload["sessionId"])
    stream = stream_final_text(sid, max_seconds=240)
    return {
        "ok": True,
        "session_id": sid,
        "text": stream["text"],
        "tools": stream["tools"],
        "errors": stream["errors"],
    }


def main() -> int:
    from frontend.memory_api import is_memory_chat_query
    from frontend.wiki_drift_api import (
        WIKI_DRIFT_MARKER,
        WIKI_LOOKUP_MARKER,
        enrich_eve_message_payload,
        is_truth_drift_query,
        is_wiki_lookup_query,
        pick_compare_topic,
    )
    from frontend import companion_api

    results: list[CaseResult] = []

    # --- Gates ---
    gate_cases = [
        (
            "drift_ai_truth",
            "Truth Drift: has truth changed between 2017 and 2026 for AI creating vs absorbing?",
            False,
            True,
            "post-truth",
        ),
        (
            "drift_explicit",
            "Compare post-truth across 2017, 2021, and 2026",
            False,
            True,
            "post-truth",
        ),
        (
            "memory_ok",
            "what do you know about me from memory?",
            True,
            False,
            None,
        ),
        (
            "plain_chat",
            "hows it going?",
            False,
            False,
            None,
        ),
        (
            "wiki_access_not_drift",
            "Can you access my Wikipedia data?",
            False,
            False,
            None,
        ),
        (
            "artist_lookup",
            "Who is Kate Bush?",
            False,
            False,
            None,
        ),
    ]
    for name, text, want_mem, want_drift, want_topic in gate_cases:
        mem = is_memory_chat_query(text)
        drift = is_truth_drift_query(text)
        topic = pick_compare_topic(text) if drift else None
        ok = mem == want_mem and drift == want_drift
        if want_topic is not None:
            ok = ok and topic == want_topic
        results.append(
            CaseResult(
                name=f"gate:{name}",
                ok=ok,
                detail=f"mem={mem} drift={drift} topic={topic}",
            )
        )

    # --- Glasses inject ---
    for name, text, must_substr in [
        (
            "inject_post_truth",
            "Truth Drift compare post-truth 2017 vs 2026",
            "Post-truth",
        ),
        (
            "inject_ai_truth",
            "Truth Drift: truth and AI models between 2017 and 2026",
            "2017",
        ),
    ]:
        enriched = enrich_eve_message_payload({"message": text})
        msg = str(enriched.get("message") or "")
        ok = (
            WIKI_DRIFT_MARKER in msg
            and "[[EMPIRE_NOW]]" not in msg
            and must_substr.casefold() in msg.casefold()
        )
        results.append(
            CaseResult(
                name=f"glasses:{name}",
                ok=ok,
                detail=f"chars={len(msg)} head={msg[:120]!r}",
            )
        )

    # --- Greeting companion ---
    greet_payload = companion_api.enrich_eve_message_payload({"message": "hows it going?"})
    greet_msg = str(greet_payload.get("message") or "")
    results.append(
        CaseResult(
            name="greet:now_only",
            ok=(
                "[[EMPIRE_NOW]]" in greet_msg
                and "START FROM ZERO" not in greet_msg
                and "GADGET" not in greet_msg
            ),
            detail=greet_msg[:160].replace("\n", " / "),
        )
    )

    # --- Live Eve Truth Drift ---
    drift_q = (
        "Truth Drift: has the scope and terms related to truth changed between "
        "2017 and 2026? Focus on AI creating vs absorbing data — use local wiki archives."
    )
    drift = eve_ask(drift_q, mode="fast")
    text = drift.get("text") or ""
    lowered = text.casefold()
    grounded = (
        drift.get("ok")
        and bool(text)
        and ("2017" in text or "2021" in text or "2026" in text)
        and ("post-truth" in lowered or "truth" in lowered)
    )
    contract_hole = "contract" in lowered and "post-truth" not in lowered and "truth" not in lowered
    invent_essay = (
        "key findings" in lowered
        and "theoretical" in lowered
        and "mature" in lowered
        and "post-truth" not in lowered
    )
    results.append(
        CaseResult(
            name="eve:truth_drift_fast",
            ok=bool(grounded and not contract_hole and not invent_essay and not drift.get("errors")),
            detail=(
                f"grounded={grounded} contract_hole={contract_hole} invent={invent_essay} "
                f"tools={drift.get('tools')} head={text[:220]!r}"
            ),
        )
    )

    # Second topic: epistemology years
    epi_q = "Truth Drift across years for epistemology — what differs in 2017 vs 2021 vs 2026?"
    epi = eve_ask(epi_q, mode="fast")
    epi_text = epi.get("text") or ""
    epi_ok = (
        epi.get("ok")
        and "epistemolog" in epi_text.casefold()
        and ("2017" in epi_text or "2021" in epi_text or "2026" in epi_text)
    )
    results.append(
        CaseResult(
            name="eve:epistemology_drift",
            ok=bool(epi_ok),
            detail=f"head={epi_text[:220]!r}",
        )
    )

    # Greeting live
    hi = eve_ask("hows it going?", mode="fast")
    hi_text = (hi.get("text") or "").casefold()
    hi_ok = hi.get("ok") and bool(hi_text) and "graduation" not in hi_text and "summer semester" not in hi_text
    results.append(
        CaseResult(
            name="eve:greeting",
            ok=bool(hi_ok),
            detail=f"head={(hi.get('text') or '')[:220]!r}",
        )
    )

    # Memory path should still work as API (not Eve) without 5s fail for a real memory query
    status, mem_payload = _req(
        "POST",
        "/api/memory/answer",
        {"query": "what are my interests from memory?", "fast": True},
        timeout=180,
    )
    mem_ok = status == 200 and isinstance(mem_payload, dict) and mem_payload.get("ok") is True
    err = str((mem_payload or {}).get("error") or "")
    results.append(
        CaseResult(
            name="memory:answer_api",
            ok=bool(mem_ok) and "timed out after 5s" not in err,
            detail=f"status={status} err={err[:120]!r} answer_head={str((mem_payload or {}).get('answer') or '')[:120]!r}",
        )
    )

    passed = sum(1 for r in results if r.ok)
    failed = [r for r in results if not r.ok]
    report = {
        "passed": passed,
        "total": len(results),
        "failed": [asdict(r) for r in failed],
        "all": [asdict(r) for r in results],
        "drift_sample": (drift.get("text") or "")[:2000],
        "epi_sample": epi_text[:1500],
        "greet_sample": (hi.get("text") or "")[:800],
    }
    with open(REPORT, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)

    print(f"SCORE {passed}/{len(results)}")
    for r in results:
        print(("PASS" if r.ok else "FAIL"), r.name, "::", r.detail[:180])
    print("WROTE", REPORT)
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
