import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Always registered — auto-admits github_scout when headroom allows. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("github_scout")
        ? defineTool({
  description:
    "Search GitHub repositories by keyword; cache markdown under 04_Thought_Experiments/github_cache. " +
    "Auto-admits GitHub Scout when resource headroom allows (no Toolbelt click). " +
    "Does NOT clone or write Cognee. Never claim you lack internet — call this tool.",
  inputSchema: z.object({
    query: z.string().min(1).describe("Search keywords (e.g. duckdb mcp server local)."),
    limit: z.number().int().min(1).max(30).optional().describe("Max results (default 10)."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ query, limit, note }) {
    const gate = await ensureLightCapability("github_scout", `github search: ${query}`);
    if (!gate.ok) {
      return gate;
    }
    const args = ["search", query];
    if (limit != null) {
      args.push("--limit", String(limit));
    }
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.github_scout", args);
  },
})
        : null,
  },
});
