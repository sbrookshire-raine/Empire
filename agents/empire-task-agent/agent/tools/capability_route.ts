import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Keyword index for Eve's own tools, Toolbelt limbs, and playbook areas. " +
    "Use before claiming a capability is missing, before heavy limbs, or when the route is unclear. " +
    "Returns resource hints (GPU, network, admission). Does not search external catalog.db — use search_catalog for OSS repo rows.",
  inputSchema: z.object({
    query: z
      .string()
      .min(1)
      .describe("Goal or keywords (e.g. reverse engineer app, wiki discography, create task)."),
    limit: z.number().int().min(1).max(10).optional().describe("Max hits (default 5)."),
  }),
  async execute({ query, limit }) {
    const args = [query];
    if (limit != null) {
      args.push("--limit", String(limit));
    }
    return runPythonModule("pipeline.capability_index", args);
  },
});
