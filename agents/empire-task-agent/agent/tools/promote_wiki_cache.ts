import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Explicitly promote a wiki_cache .md file into Cognee memory. Never automatic — only when the Architect asks. Compare files route to truth_drift; single hits to eve_memory unless dataset override is set.",
  inputSchema: z.object({
    path: z.string().min(1).describe("Full path to a wiki_cache markdown file."),
    dataset: z
      .string()
      .optional()
      .describe(
        "Optional Cognee dataset override (eve_memory, truth_drift, eve_core, primitives_test). Omit to auto-route from cache kind.",
      ),
  }),
  async execute({ path, dataset }) {
    const args = ["promote", path];
    if (dataset) {
      args.push("--dataset", dataset);
    }
    return runPythonModule("pipeline.wiki_scout", args);
  },
});
