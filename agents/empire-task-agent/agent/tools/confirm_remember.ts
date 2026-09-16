import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Confirm a staging proposal into eve_memory or eve_core — only when Architect says keep. */
export default defineTool({
  description:
    "Promote a staging entry into permanent Cognee memory (eve_memory or eve_core). " +
    "Only when the Architect explicitly says to keep/save/confirm that staging id.",
  inputSchema: z.object({
    entry_id: z.string().min(1).describe("Staging id from list_staging / propose_remember."),
    dataset: z
      .string()
      .optional()
      .describe("Target dataset: eve_memory (default) or eve_core."),
  }),
  async execute({ entry_id, dataset }) {
    const args = ["confirm", entry_id];
    if (dataset) args.push("--dataset", dataset);
    return runPythonModule("pipeline.eve_staging", args);
  },
});
