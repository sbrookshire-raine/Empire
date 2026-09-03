import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { defineDynamic, defineInstructions } from "eve/instructions";
import { EMPIRE_ROOT } from "./lib/empire";

const agentDir = dirname(fileURLToPath(import.meta.url));
const eveInstructionsPath = join(EMPIRE_ROOT, "eve_instructions.md");
const routingInstructionsPath = join(agentDir, "empire-routing.md");

function readInstructionsFile(filePath: string): string {
  try {
    return readFileSync(filePath, "utf8").trim();
  } catch {
    return "";
  }
}

function loadSystemPrompt(): string {
  const parts = [
    readInstructionsFile(eveInstructionsPath),
    readInstructionsFile(routingInstructionsPath),
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
