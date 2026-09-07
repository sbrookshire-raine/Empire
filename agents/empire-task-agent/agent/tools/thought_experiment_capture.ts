import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("thought_experiments")
        ? defineTool({
            description:
              "Capture a Manifesto Phase 3 thought-experiment note (optional YouTube/URL) under 04_Thought_Experiments. Scratch only — not Cognee until promoted. Requires Thought Experiments Toolbelt.",
            inputSchema: z.object({
              topic: z.string().min(1),
              source_url: z.string().optional(),
              notes: z.string().optional(),
            }),
            async execute({ topic, source_url, notes }) {
              const args = [topic];
              if (source_url) {
                args.push("--url", source_url);
              }
              if (notes) {
                args.push("--notes", notes);
              }
              return runPythonModule("pipeline.thought_experiment", args);
            },
          })
        : null,
  },
});
