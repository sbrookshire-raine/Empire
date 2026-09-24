import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

/** Read back past thought experiments — capture alone left them unreachable. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("thought_experiments")
        ? defineTool({
            description:
              "List or read the Architect's saved thought-experiment notes under 04_Thought_Experiments. " +
              "Use before starting a new experiment, to build on what was already tried.",
            inputSchema: z.object({
              name: z
                .string()
                .optional()
                .describe("Note name (or path inside 04_Thought_Experiments) to read in full."),
              limit: z.number().int().min(1).max(50).optional().describe("How many notes to list."),
            }),
            async execute({ name, limit }) {
              if (name) {
                return runPythonModule("pipeline.thought_experiment", ["--read", name]);
              }
              const args = ["--list"];
              if (limit != null) args.push("--limit", String(limit));
              return runPythonModule("pipeline.thought_experiment", args);
            },
          })
        : null,
  },
});
