"""FastMCP: thought experiments + voice + vision + promote helpers."""

from __future__ import annotations

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from pipeline import thought_experiment, vision_local, voice_presence, wiki_scout
from pipeline import gpu_lease

mcp = FastMCP("empire-atlas")


def _json(data: Any) -> str:
    return json.dumps(data, indent=2, default=str)


@mcp.tool()
async def promote_wiki_cache(path: str, dataset: str = "") -> str:
    """Explicitly promote a wiki_cache .md into Cognee (never automatic)."""
    override = dataset.strip() or None
    return _json(wiki_scout.promote_wiki_cache(path, dataset=override))


@mcp.tool()
async def thought_experiment_capture(
    topic: str,
    source_url: str = "",
    notes: str = "",
) -> str:
    """Save a Phase 3 thought-experiment note under 04_Thought_Experiments."""
    return _json(
        thought_experiment.capture(topic, source_url=source_url, notes=notes)
    )


@mcp.tool()
async def voice_health() -> str:
    """Check local OpenAI-compatible speech API (Speaches/Voicebox)."""
    return _json(voice_presence.health())


@mcp.tool()
async def voice_transcribe(audio_path: str) -> str:
    """Transcribe a local audio file via the speech API."""
    return _json(voice_presence.transcribe(audio_path))


@mcp.tool()
async def voice_speak(text: str, output_path: str = "") -> str:
    """Synthesize speech to a local audio file via the speech API."""
    return _json(voice_presence.speak(text, out_path=output_path or None))


@mcp.tool()
async def vision_describe(
    image_path: str,
    prompt: str = "Describe this image for the Architect. Be concrete.",
) -> str:
    """Describe a local image with Ollama qwen3-vl (GPU lease)."""
    return _json(vision_local.describe_image(image_path, prompt=prompt))


@mcp.tool()
async def gpu_lease_status() -> str:
    """Show which heavy GPU tenant holds the EMPIRE lease."""
    return _json(gpu_lease.status())


@mcp.tool()
async def gpu_lease_release() -> str:
    """Force-release the GPU lease to idle."""
    return _json(gpu_lease.release())


@mcp.tool()
async def resource_pulse() -> str:
    """Headroom + inventory: what Eve has, what she can safely admit, what needs Architect OK."""
    from pipeline import resource_pulse as rp

    return _json(rp.pulse())


@mcp.tool()
async def admit_for_goal(category: str, reason: str = "", ttl_min: int = 0) -> str:
    """Admit a light session skill when headroom OK (no Research Partner toggle). GPU/heavy asks Architect."""
    from pipeline import resource_pulse as rp

    ttl = ttl_min if ttl_min and ttl_min >= 5 else None
    return _json(rp.admit_for_goal(category, reason, ttl_min=ttl))


if __name__ == "__main__":
    mcp.run()
