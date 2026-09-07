import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Explicitly promote a wiki_cache .md file into Cognee memory. Never automatic — only when the Architect asks. Path must be under 04_Thought_Experiments/wiki_cache.",
  inputSchema: z.object({
    path: z.string().min(1).describe("Full path to a wiki_cache markdown file."),
    dataset: z
      .string()
      .optional()
      .describe("Cognee dataset (default eve_memory; use truth_drift for compares)."),
  }),
  async execute({ path, dataset }) {
    const args = ["promote", path];
    if (dataset) {
      args.push("--dataset", dataset);
    }
    return runPythonModule("pipeline.wiki_scout", args);
  },
});
