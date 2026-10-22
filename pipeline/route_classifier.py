"""One classifier for "is this a wiki ask, a memory ask, a task ask, or something else".

Why this exists
---------------
Four places used to decide, independently, whether a user message was an
encyclopedia ask or a memory ask:

- `frontend/wiki_drift_api.py::is_wiki_lookup_query` — regexes over the raw text.
- `frontend/memory_api.py::is_memory_chat_query` — its own regexes, with its
  own copy of the wiki check.
- `frontend/eve-workbench.js::isMemoryQuery` — a *third* set of regexes, in
  the browser, deciding whether to bypass Eve entirely.
- `pipeline/intent_codex.py::context_block` — scored the message with the
  codex, then *overrode* the result with a wiki rule.

Four answers to the same question is four ways to be wrong, and they were
wrong in different directions: "what is my disk space" was a wiki ask, and
"what can you tell me about my memory of the project" was an encyclopedia
ask. The frontend's browser-side copy could not see the server's rules at
all, so it disagreed with the server on purpose.

The contract
------------
One function, `classify()`, returns one of four labels:

- ``wiki``   — an encyclopedia ask. Eve calls the wiki tools.
- ``memory`` — a question about the Architect's own stored context. The
  memory path may answer it directly.
- ``task``   — a request about the PocketBase task list.
- ``other``  — anything else. Eve handles it.

Precedence (deliberate, and the whole point of the module)
-----------------------------------------------------------
1. **Explicit wiki signal** — the message names Wikipedia, the wiki archive,
   a page, an article, a discography, or asks to compare years. This wins
   even over a memory anchor: "look up the album we discussed" is a wiki
   ask, because "look up" is a wiki verb.
2. **Memory anchor** — the message is about the Architect's own context
   (memory, interests, uploads, projects, notes). This wins over the
   generic wiki verbs: "what do you know about my notes" is memory, not an
   encyclopedia ask.
3. **Generic wiki verb** — "who is X", "what is X", "tell me about X"
   without a memory anchor. This is the ambiguous middle, and it is the
   one that used to go wrong.
4. Otherwise: ``other``.

The rule that makes step 3 safe: a generic wiki verb only fires when the
message carries *no* memory anchor and *no* stack/capability subject.
"what is my disk space" is not an encyclopedia ask.
"""

from __future__ import annotations

import re
from typing import Any, Literal

Route = Literal["wiki", "memory", "task", "other"]

WIKI: Route = "wiki"
MEMORY: Route = "memory"
TASK: Route = "task"
OTHER: Route = "other"

ROUTES: tuple[Route, ...] = (WIKI, MEMORY, TASK, OTHER)

# --- 1. Explicit wiki signal -------------------------------------------------
#
# Words that mean "the encyclopedia", not "some page of text". These are
# unambiguous: a message that says "Wikipedia" is a wiki ask, whatever else
# it also says.

EXPLICIT_WIKI_RE = re.compile(
    r"\b(?:"
    r"wikipedia|wiki\b|encyclopedia|weaviate|"
    r"title\s+dns|"
    r"discograph(?:y|ies)|"
    r"wikitable|infobox|"
    r"the\s+wiki\s+page|"
    r"wiki\s+local"
    r")\b",
    re.IGNORECASE,
)

# Explicit cross-year comparison: Weaviate-backed, never a plain lookup.
COMPARE_YEARS_RE = re.compile(
    r"\b(?:compare\s+years?|across\s+years?|truth\s*drift)\b"
    r"|\bbetween\s+20\d{2}\s+and\s+20\d{2}\b"
    r"|\bfrom\s+20\d{2}\s+to\s+20\d{2}\b",
    re.IGNORECASE,
)

# "look up", "open", "search" applied to the encyclopedia.
WIKI_VERB_RE = re.compile(
    r"\b(?:look\s*up|lookup|go\s+to|open|search|query|pull\s+up)\b"
    r"[^.?!]{0,40}?\b(?:wikipedia|wiki|encyclopedia|local\s+archive|my\s+archive)\b"
    r"|\b(?:wikipedia|wiki|encyclopedia)\b[^.?!]{0,24}\b(?:say|says|about|entry|article|page)\b"
    r"|\bmy\s+(?:local\s+)?(?:wikipedia|wiki|encyclopedia)\b",
    re.IGNORECASE,
)

# --- 2. Memory anchor --------------------------------------------------------
#
# The Architect's own context. A message carrying one of these is a memory
# ask unless it *also* carries an explicit wiki signal (step 1).

MEMORY_ANCHOR_RE = re.compile(
    r"\b(?:"
    r"memory|memories|remember|remembered|recall|recalled|recollect|remind|"
    r"interests?|"
    r"my\s+(?:notes|docs|documents|files|work|workbench|goals|plans|projects?)|"
    r"projects?\s+in\s+(?:your\s+)?memory|"
    r"memory\s+(?:graph|bank)|"
    r"about\s+me|know\s+about\s+me|"
    r"uploaded|uploads?|"
    r"from\s+memory|in\s+memory|"
    # Past-tense recall: "did we already build X", "what did we decide Y".
    # These carry no literal memory word, but they are unmistakably a
    # question about what *we* already did — the Architect's own history.
    r"did\s+we\s+(?:already\s+)?(?:build|decide|discuss|agree|plan|start|try|find|"
    r"set\s+up|create|write|ship)\b|"
    r"what\s+did\s+we\s+(?:decide|build|discuss|agree|plan|start|try|find|"
    r"set\s+up|create|write|ship)\b|"
    r"have\s+we\s+(?:already\s+)?(?:built|decided|discussed|agreed|planned|"
    r"started|tried|found)\b|"
    r"what\s+were\s+we\s+(?:doing|planning|building)\b"
    r")\b",
    re.IGNORECASE,
)

# The memory *question* shapes: an anchor plus a recall verb.
MEMORY_QUESTION_RE = re.compile(
    r"\b(?:memory|memories|interests?|recall|recalled|remember|remembered)\b"
    r"|\bwhat\s+do\s+you\s+know\b"
    r"|\bwhat\s+can\s+you\s+tell\s+me\b"
    r"|\bwhat\s+am\s+i\b"
    r"|\bmy\s+projects?\b"
    r"|\bfrom\s+(?:my\s+)?memory\b"
    r"|\buploaded\b"
    r"|\bmemory\s+(?:graph|bank)\b"
    r"|\bprojects?\s+in\s+(?:your\s+)?memory\b"
    r"|\bwhat\s+did\s+we\s+(?:decide|build|say)\b"
    r"|\bwhat\s+are\s+my\b",
    re.IGNORECASE,
)

# --- 3. Task ------------------------------------------------------------------

TASK_RE = re.compile(
    r"\b(?:"
    r"tasks?|todos?|to-?dos?|checklist|"
    r"my\s+list|"
    r"add\s+(?:a\s+)?task|"
    r"mark\s+(?:it\s+)?done|"
    r"to\s+do\s+list"
    r")\b",
    re.IGNORECASE,
)

# --- Stack / capability subjects ---------------------------------------------
#
# "what is my disk space" is a question about the machine, not about
# magnetism. These subjects must suppress the generic wiki verb.

STACK_SUBJECT_RE = re.compile(
    r"\b(?:"
    r"disk|space|ram|vram|gpu|cpu|headroom|"
    r"capabilit(?:y|ies)|tools?|limbs?|toolbelt|skills?|"
    r"stack|service|server|port|container|docker|"
    r"drive|drives|backup|estate|inventory|"
    r"status|health|version|config|configuration|log|logs|"
    r"task|tasks|todo|checklist|"
    r"machine|system|"
    r"my\s+notes|my\s+files|my\s+workbench"
    r")\b",
    re.IGNORECASE,
)

# --- Generic wiki verbs -------------------------------------------------------
#
# "who is X", "what is X", "tell me about X". These are the ambiguous
# middle: an encyclopedia question *or* a question about the Architect's own
# machine. They only become a wiki ask when nothing else claims the message.

GENERIC_WIKI_VERB_RE = re.compile(
    r"\b(?:"
    r"who\s+(?:is|are|was|were)\b|"
    r"who'?s\b|"
    r"what\s+(?:is|are|was|were)\b|"
    r"what'?s\b|"
    r"when\s+(?:is|was|did)\b|"
    r"where\s+(?:is|was|does)\b|"
    r"tell\s+me\s+about\b|"
    r"summarize\s+about\b|"
    r"look\s*up\b"
    r")",
    re.IGNORECASE,
)

# "tell me about X" and "look up X" take *any* object: the verb itself
# carries the encyclopedia intent, so the object only has to not be a stack
# subject. "what is X" needs a real subject — otherwise "what is my disk
# space" would be an encyclopedia ask.
WIKI_VERB_ANY_OBJECT_RE = re.compile(
    r"\b(?:tell\s+me\s+about|summarize\s+about|look\s*up)\b",
    re.IGNORECASE,
)

# A concrete encyclopedic subject: a proper noun, a quoted phrase, a year,
# or a genre/media noun. "what is the capital of France" has one; "what is
# my disk space" does not.
ENCYCLOPEDIC_SUBJECT_RE = re.compile(
    r"\b(?:"
    r"'[^']{2,40}'|\"[^\"]{2,40}\"|"  # quoted title
    r"\b(?:19|20)\d{2}\b|"  # a year
    r"\b(?:albums?|songs?|singles?|discography|episodes?|cast|actors?|"
    r"novel|film|movie|album|band|singer|song|series|show|game|"
    r"capital|population|reception|filmography|black\s+holes?)\b"
    r")",
    re.IGNORECASE,
)

# A proper-noun subject: two capitalised words in a row ("Kate Bush"), or a
# single capitalised word that is not the first word of the sentence
# ("Who is Kate?"). The sentence-initial exclusion keeps a question like
# "What is the answer?" from counting "What" as a proper noun.
#
# The rule is case-sensitive by design — it needs the capitalisation — but
# the *message* may arrive in any case. So the capitalisation is only
# evidence when the message is not entirely upper-case: an upper-cased
# message carries no capitalisation signal at all, and treating it as such
# would turn "WHAT'S FREE ON THE MACHINE?" into an encyclopedia ask.
PROPER_NOUN_RE = re.compile(
    r"\b[A-Z][a-zA-Z'’-]+(?:\s+[A-Z][a-zA-Z'’-]+)+\b"
    r"|(?<![.!?]\s)(?<!^)\b[A-Z][a-zA-Z'’-]{2,}\b",
)


def _has_proper_noun(text: str) -> bool:
    """True when the message names a proper noun.

    The rule reads capitalisation, so an all-upper-case message carries no
    capitalisation signal. Rather than drop the rule there (which would
    make "WHO IS KATE BUSH?" a non-wiki ask), the message is title-cased
    first — the words are the same, only the capitalisation is restored.
    """

    if not any(char.islower() for char in text):
        text = text.title()
    return bool(PROPER_NOUN_RE.search(text))



def _has_explicit_wiki_signal(text: str) -> bool:
    """True when the message names the encyclopedia unambiguously."""

    if EXPLICIT_WIKI_RE.search(text):
        return True
    if COMPARE_YEARS_RE.search(text):
        return True
    return bool(WIKI_VERB_RE.search(text))


def _has_memory_anchor(text: str) -> bool:
    """True when the message is about the Architect's own stored context."""

    return bool(MEMORY_ANCHOR_RE.search(text))


def _has_task_signal(text: str) -> bool:
    """True when the message is about the PocketBase task list."""

    return bool(TASK_RE.search(text))


def _generic_wiki_verb_fires(text: str) -> bool:
    """True for "who is X" / "what is X" that look encyclopedic.

    Two tiers:

    - "tell me about X" / "look up X" / "summarize about X" take *any*
      object — the verb carries the encyclopedia intent on its own.
    - "who is X" / "what is X" need a real encyclopedic subject (a proper
      noun, a quoted title, a year, a media noun), and are suppressed by a
      stack subject.

    "what is my disk space" fails on both counts; "who is Kate Bush" passes
    on both.
    """

    if STACK_SUBJECT_RE.search(text):
        return False
    if WIKI_VERB_ANY_OBJECT_RE.search(text):
        return True
    if not GENERIC_WIKI_VERB_RE.search(text):
        return False
    if ENCYCLOPEDIC_SUBJECT_RE.search(text):
        return True
    return _has_proper_noun(text)


# --- Encyclopedic subject nouns, anywhere in the message ---------------------
#
# "What albums did Kate Bush release?" asks about a discography, not about
# the machine. A media noun is a subject in its own right, wherever it sits
# in the sentence — it does not need a leading "who is" to count.

MEDIA_NOUN_RE = re.compile(
    r"\b(?:"
    r"albums?|songs?|singles?|discograph(?:y|ies)|"
    r"episodes?|seasons?|cast|actors?|actresses?|"
    r"novels?|films?|movies?|"
    r"bands?|singers?|artists?|"
    r"series|shows?|games?|"
    r"filmograph(?:y|ies)|"
    r"capital|population|reception|"
    r"black\s+holes?"
    r")\b",
    re.IGNORECASE,
)


def _has_media_subject(text: str) -> bool:
    """True when the message names something encyclopedic (a discography, a cast)."""

    if STACK_SUBJECT_RE.search(text):
        return False
    return bool(MEDIA_NOUN_RE.search(text))


# A follow-up about the page currently being discussed. Only meaningful when
# the previous turn was a wiki page — the caller supplies that state.
_WIKI_FOLLOWUP_RE = re.compile(
    r"\b(?:"
    r"that\s+page|this\s+page|the\s+same\s+page|"
    r"on\s+it|about\s+it|about\s+them|"
    r"more\s+about\s+(?:it|that|this)|"
    r"what\s+else\s+(?:is\s+)?on\b|"
    r"tell\s+me\s+more\b|"
    r"their\s+(?:albums?|songs?|discography|history|legacy|awards?)\b|"
    r"who\s+else\b"
    r")",
    re.IGNORECASE,
)


def classify(text: str, *, wiki_followup: bool = False) -> Route:
    """Classify one user message into a route.

    This is the single decision point. Every caller — the intent codex, the
    wiki green path, the memory API, the wiki lookup, the browser — must
    agree with this function, or one of them is wrong.

    `wiki_followup` carries the conversational state the classifier cannot
    see by itself: True when the *previous* turn was a wiki page (so "what
    else is on that page" is a wiki ask). The caller owns that state; the
    classifier owns the decision.
    """

    raw = str(text or "").strip()
    if not raw:
        return OTHER

    # 0. A follow-up on a page we are already discussing is a wiki ask.
    if wiki_followup and _WIKI_FOLLOWUP_RE.search(raw):
        return WIKI

    # 1. An explicit wiki signal wins outright.
    if _has_explicit_wiki_signal(raw):
        return WIKI

    # 2. A memory anchor wins over the generic wiki verbs.
    if _has_memory_anchor(raw):
        return MEMORY

    # 3. Tasks.
    if _has_task_signal(raw):
        return TASK

    # 4. A media/encyclopedic subject ("what albums did X release?") is a
    # wiki ask in its own right — it does not need a leading "who is".
    if _has_media_subject(raw):
        return WIKI

    # 5. The generic wiki verb — only when it really looks encyclopedic.
    if _generic_wiki_verb_fires(raw):
        return WIKI

    return OTHER


def is_wiki(text: str) -> bool:
    """True when the message is an encyclopedia ask."""

    return classify(text) == WIKI


def is_memory(text: str) -> bool:
    """True when the message is a question about the Architect's own context."""

    return classify(text) == MEMORY


def is_task(text: str) -> bool:
    """True when the message is about the task list."""

    return classify(text) == TASK


def explain(text: str, *, wiki_followup: bool = False) -> dict[str, Any]:
    """The classification plus the reason, for the gate report and debugging.

    `reason` names the rule that fired, so a wrong route can be diagnosed
    without re-deriving the precedence.
    """

    raw = str(text or "").strip()
    if not raw:
        return {"route": OTHER, "reason": "empty message"}
    if wiki_followup and _WIKI_FOLLOWUP_RE.search(raw):
        return {"route": WIKI, "reason": "follow-up on a wiki page"}
    if _has_explicit_wiki_signal(raw):
        return {"route": WIKI, "reason": "explicit wiki signal"}
    if _has_memory_anchor(raw):
        if MEMORY_QUESTION_RE.search(raw):
            return {"route": MEMORY, "reason": "memory anchor + recall verb"}
        return {"route": MEMORY, "reason": "memory anchor"}
    if _has_task_signal(raw):
        return {"route": TASK, "reason": "task signal"}
    if _has_media_subject(raw):
        return {"route": WIKI, "reason": "encyclopedic subject"}
    if _generic_wiki_verb_fires(raw):
        return {"route": WIKI, "reason": "generic wiki verb + encyclopedic subject"}
    return {"route": OTHER, "reason": "no route matched"}
