---
name: vision_describe
toolbelt: vision_local
one_line: Describe a local image/screenshot with Ollama qwen3-vl:8b
---

## Description (verbatim from the tool schema, pre-R-03)

Describe a local image/screenshot with Ollama qwen3-vl:8b. Takes a GPU lease — expect chat model unload. Writes scratch note under vision_notes. Requires Vision Local Toolbelt.

## Parameters

- `image_path` — (no description)
- `prompt` — What to look for / how to describe.

## Usage

Registered by the Toolbelt category `vision_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
