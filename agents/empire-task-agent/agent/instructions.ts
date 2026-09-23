import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { defineDynamic, defineInstructions } from "eve/instructions";
import { EMPIRE_ROOT } from "./lib/empire";

const agentDir = dirname(fileURLToPath(import.meta.url));
const eveInstructionsPath = join(EMPIRE_ROOT, "eve_instructions.md");

/**
 * Routing prompt candidates, in priority order.
 *
 * In dev the agent runs from `agent/`, so `agentDir` resolves correctly. In the
 * built server (`.output/server/index.mjs`) `agentDir` is the *bundle* directory,
 * which does not contain `empire-routing.md` — the source tree holds the only
 * copy. Without this fallback the routing table was silently dropped from the
 * production system prompt, so Eve never learned which local tool to call and
 * hallucinated refusals ("I don't have direct access to local tools").
 */
const ROUTING_CANDIDATES = [
  join(agentDir, "empire-routing.md"),
  join(EMPIRE_ROOT, "agents", "empire-task-agent", "agent", "empire-routing.md"),
];

function readInstructionsFile(filePath: string): string {
  try {
    return readFileSync(filePath, "utf8").trim();
  } catch {
    return "";
  }
}

function readFirstFile(paths: string[], label: string): string {
  for (const candidate of paths) {
    const text = readInstructionsFile(candidate);
    if (text) {
      return text;
    }
  }
  console.warn(`[eve] ${label} not found. Tried: ${paths.join(", ")}`);
  return "";
}

function loadSystemPrompt(): string {
  const parts = [
    readInstructionsFile(eveInstructionsPath),
    readFirstFile(ROUTING_CANDIDATES, "empire-routing.md"),
  ].filter(Boolean);

  if (parts.length === 0) {
    return "You are Eve, the local EMPIRE assistant.";
  }

  return parts.join("\n\n---\n\n");
}

export default defineDynamic({
  events: {
    "session.started": () =>
      defineInstructions({
        markdown: loadSystemPrompt(),
      }),
  },
});
