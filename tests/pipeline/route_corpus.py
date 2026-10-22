"""The shared routing corpus — the contract every caller must agree with.

Why this corpus exists
----------------------
Four places used to answer "is this an encyclopedia ask or a memory ask?"
independently: the wiki drift API, the memory API, the browser's
`isMemoryQuery`, and the intent codex's `context_block` override. They
disagreed, and the disagreements were silent:

- "what is my disk space" was a *wiki* ask (the bare verb "what" scored).
- "what can you tell me about my memory of the project" was an
  *encyclopedia* ask (the same bare verb, plus "about").
- "what did you find for me earlier?" landed on a container-search intent
  by score, which is neither of the routes it should have been.

The corpus below is the contract. It is imported by
`tests/pipeline/test_route_classifier.py` (the classifier itself) and
`tests/frontend/test_route_classifier_parity.py` (every caller must
agree with it), so the two can never drift apart.
"""

from __future__ import annotations

# (message, expected route)
#
# Grouped by the rule that is meant to fire, so a failure names the broken
# rule rather than just a number.
CORPUS: tuple[tuple[str, str], ...] = (
    # --- 1. Explicit wiki signal (wins over everything) ------------------------
    ("Who is Kate Bush on Wikipedia?", "wiki"),
    ("Go to my local Wikipedia and find the Beach Boys albums", "wiki"),
    ("use my wiki archive to look up magnetism", "wiki"),
    ("what does the encyclopedia say about post-truth?", "wiki"),
    ("search my local wikipedia for the 1984 TV series", "wiki"),
    ("tell me the names of the albums by the Beach Boys", "wiki"),
    ("compare years for artificial intelligence 2017 vs 2026", "wiki"),
    ("truth drift: what changed between 2017 and 2026?", "wiki"),
    ("what is the discography of Kate Bush", "wiki"),
    ("look up the white stripes on wikipedia", "wiki"),
    # --- 2. Memory anchor (wins over the generic wiki verbs) ----------------
    ("what do you know about me", "memory"),
    ("what do you remember about the language barrier", "memory"),
    ("recall what we decided about the vault", "memory"),
    ("what is in my memory about the project", "memory"),
    ("what can you tell me about my notes", "memory"),
    ("what are my projects in your memory", "memory"),
    ("did we already build a version of this", "memory"),
    ("what did we decide about the architecture", "memory"),
    ("what do you know about my uploaded files", "memory"),
    ("remind me what my interests are", "memory"),
    # --- 3. Tasks -------------------------------------------------------------
    ("list my tasks", "task"),
    ("add a task to buy milk", "task"),
    ("mark the first task done", "task"),
    ("what is on my todo list?", "task"),
    ("show my checklist", "task"),
    # --- 4. Generic wiki verbs (the ambiguous middle) ------------------------
    ("Who is Kate Bush?", "wiki"),
    ("Who was Marie Curie?", "wiki"),
    ("What albums did Kate Bush release?", "wiki"),
    ("what is the capital of France", "wiki"),
    ("tell me about black holes please?", "wiki"),
    ("tell me about a sci-fi series in the 80s called 'V'", "wiki"),
    ("what actors played in the TV show 'The Following'?", "wiki"),
    ("summarize about Kate Bush albums", "wiki"),
    ("what popular 80s song got re-popularized in stranger things?", "wiki"),
    # --- 5. Stack / capability subjects (must NOT be wiki) -------------------
    ("what is my disk space", "other"),
    ("how much free disk space is available on the machine?", "other"),
    ("what capabilities do you have right now?", "other"),
    ("what's free on the machine right now?", "other"),
    ("check the health of the Workbench using your local tools", "other"),
    ("what is the status of the docker containers?", "other"),
    ("is anything processing to my z drive currently", "other"),
    # --- 6. Everything else ---------------------------------------------------
    ("hello", "other"),
    ("hows it going?", "other"),
    ("what did you find for me earlier?", "other"),
    ("please scrape https://example.com/foo and summarize", "other"),
    ("research the yt-dlp release notes", "other"),
    ("can you look at this JS file and tell me what it does?", "other"),
)
