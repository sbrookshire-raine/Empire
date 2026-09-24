import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("wiki_local")
        ? defineTool({
  description:
              "Explicitly promote a wiki_cache .md file into Cognee memory.",
  inputSchema: z.object({
    path: z.string().min(1),
    dataset: z
      .string()
      .optional()
      ,
  }),
  async execute({ path, dataset }) {
    const args = ["promote", path];
    if (dataset) {
      args.push("--dataset", dataset);
    }
    return runPythonModule("pipeline.wiki_scout", args);
  },
})
        : null,
  },
});
