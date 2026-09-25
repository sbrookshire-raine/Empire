"""What constrained output does THIS Ollama actually give us? (E-36's evaluation ask, F-38's input.)

E-36 put reliability before capability on record: *"malformed tool calls on local Ollama are what got
`ask_question` disabled; structured decoding makes a malformed call structurally impossible."* Before
wiring `format` into anything, measure what the installed server + installed model actually honour:

    .\\venv\\Scripts\\python.exe scripts\\probe-constrained-output.py
    .\\venv\\Scripts\\python.exe scripts\\probe-constrained-output.py --model empire-fast:14b

Probes (native /api/chat, the path the agent uses):
    1 baseline      - free text, no constraint                    (does the server answer at all)
    2 format json   - `format: "json"`                            (is the mode available)
    3 enum pick     - schema with an `enum` of candidate titles   (the closed-choice case, F-38)
    4 bad schema    - a schema the server should reject           (does failure surface or degrade)
    5 tools+format  - a tool call AND `format` together           (grammar-constrained tool calling)

Nothing is wired on the strength of this script; it produces the measurement the queue entry asks for.
"""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:11434"
CANDIDATE_TITLES = [
    "The White Stripes",
    "Elephant (album)",
    "White Stripes (disambiguation)",
    "Jack White",
    "The Raconteurs",
]

PICK_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "enum": CANDIDATE_TITLES},
        "confidence": {"type": "number"},
    },
    "required": ["title", "confidence"],
    "additionalProperties": False,
}

BAD_SCHEMA = {
    "type": "object",
    "properties": {"title": {"type": "string", "enum": "not-a-list"}},
    "required": ["title", "additionalProperties"],
}


def call(payload: dict, timeout: float = 120.0) -> tuple[dict | None, float, str]:
    """POST /api/chat. Returns (body, seconds, error)."""

    request = urllib.request.Request(
        f"{BASE}/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    started = time.time()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
        return json.loads(raw), time.time() - started, ""
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:200]
        return None, time.time() - started, f"HTTP {exc.code}: {detail}"
    except Exception as exc:  # noqa: BLE001 - the point is to see whatever happens
        return None, time.time() - started, f"{type(exc).__name__}: {exc}"


def message_of(body: dict | None) -> str:
    if not body:
        return ""
    return str(((body.get("message") or {}).get("content")) or "")



def probe(name: str, payload: dict, *, expect_json: bool = False) -> dict:
    body, seconds, error = call(payload)
    text = message_of(body)
    verdict: dict = {"probe": name, "seconds": round(seconds, 2)}
    if error:
        verdict.update({"result": "ERROR", "detail": error})
        return verdict
    verdict["chars"] = len(text)
    if expect_json:
        try:
            parsed = json.loads(text)
            verdict["result"] = "VALID JSON"
            verdict["json"] = parsed
            verdict["title_in_enum"] = parsed.get("title") in CANDIDATE_TITLES
        except json.JSONDecodeError:
            verdict["result"] = "NOT JSON"
            verdict["raw_head"] = text[:160]
            found = re.search(r"\{.*\}", text, re.DOTALL)
            if found:
                try:
                    json.loads(found.group(0))
                    verdict["result"] = "JSON buried in prose"
                except json.JSONDecodeError:
                    pass
    else:
        verdict["result"] = "ANSWERED" if text.strip() else "EMPTY"
        verdict["head"] = " ".join(text.split())[:120]
    tools = ((body or {}).get("message") or {}).get("tool_calls") or []
    verdict["tool_calls"] = len(tools)
    if tools:
        verdict["tool_names"] = [t.get("function", {}).get("name") for t in tools]
    return verdict


def main(argv: list[str] | None = None) -> int:
    global BASE
    parser = argparse.ArgumentParser(description="Probe constrained output on local Ollama")
    parser.add_argument("--model", default="empire-fast:14b")
    parser.add_argument("--base", default=BASE)
    args = parser.parse_args(argv)
    BASE = args.base.rstrip("/")
    model = args.model
    print(f"# constrained-output probe - model={model} base={BASE}\n")
    small = {"num_predict": 32}
    results = [
        probe(
            "1 baseline (no constraint)",
            {
                "model": model,
                "stream": False,
                "options": dict(small),
                "messages": [{"role": "user", "content": "Reply with the word ready and nothing else."}],
            },
        ),
        probe(
            "2 format=json",
            {
                "model": model,
                "stream": False,
                "format": "json",
                "options": {"num_predict": 64},
                "messages": [{"role": "user", "content": 'Return {"status":"ok","n":3} as JSON only.'}],
            },
            expect_json=True,
        ),
        probe(
            "3 enum pick (title choice)",
            {
                "model": model,
                "stream": False,
                "format": PICK_SCHEMA,
                "options": {"num_predict": 96},
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            'Pick the best Wikipedia title for this ask: "make me a spreadsheet of the '
                            'White Stripes studio albums". Answer with the schema fields only.'
                        ),
                    }
                ],
            },
            expect_json=True,
        ),
        probe(
            "4 malformed schema",
            {
                "model": model,
                "stream": False,
                "format": BAD_SCHEMA,
                "options": dict(small),
                "messages": [{"role": "user", "content": "Pick a title."}],
            },
            expect_json=True,
        ),
        probe(
            "5 tools + format together",
            {
                "model": model,
                "stream": False,
                "format": {"type": "object", "properties": {"title": {"type": "string"}}},
                "options": {"num_predict": 96},
                "tools": [
                    {
                        "type": "function",
                        "function": {
                            "name": "wiki_scout_search",
                            "description": "Local Wikipedia lookup for a subject you name.",
                            "parameters": {
                                "type": "object",
                                "properties": {"subject": {"type": "string"}},
                                "required": ["subject"],
                            },
                        },
                    }
                ],
                "messages": [
                    {"role": "user", "content": "Look up the White Stripes in the local archive."}
                ],
            },
            expect_json=True,
        ),
    ]

    for row in results:
        print(json.dumps(row, ensure_ascii=False))
    print("\n# summary")
    for row in results:
        print(f"  {row['probe']:<28} -> {row['result']:<20} {row['seconds']}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
