import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Search the local EMPIRE capability catalog for tools by capability, description, category, or name. Read-only; use before claiming a local tool is unavailable.",
  inputSchema: z.object({
    query: z.string().min(1).describe("Capability or tool search, for example minimax or decision making."),
    limit: z.number().int().min(1).max(20).optional().describe("Maximum catalog results."),
  }),
  async execute({ query, limit }) {
    const args = [query];
    if (limit != null) args.push("--limit", String(limit));
    return runPythonModule("pipeline.discovery_catalog", args);
  },
});
