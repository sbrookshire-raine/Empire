import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Resolve everyday language (scrape, research, lookup, remember, …) to Eve intents, " +
    "local-first tool order, limbs, and playbook area. Use when the user's verbs imply a goal " +
    "but they did not name a tool. Then call the listed tools — do not skip to training memory.",
  inputSchema: z.object({
    message: z
      .string()
      .min(1)
      .describe("The user's ask or the operative sentence (plain English)."),
    limit: z.number().int().min(1).max(5).optional().describe("Max intent hits (default 3)."),
  }),
  async execute({ message, limit }) {
    const args = [message];
    if (limit != null) {
      args.push("--limit", String(limit));
    }
    return runPythonModule("pipeline.intent_codex", args);
  },
});
