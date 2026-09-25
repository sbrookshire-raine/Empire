import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * Read a finished research job's bounded digest (E-37).
 *
 * The desk keeps the full pages; this returns a capped digest plus whether more is available, so her
 * window is spent reading what matters rather than holding a corpus.
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("web_research")
        ? defineTool({
            description:
              "Read a research job's digest (bounded). Returns more_available when the desk holds more than the budget allowed.",
            inputSchema: z.object({
              job_id: z.string().describe("Job id from research_start."),
              budget: z.number().optional().describe("Max characters to return (default 2400)."),
            }),
            async execute({ job_id, budget }) {
              const args = ["read", job_id.trim()];
              if (budget && budget > 0) {
                args.push("--budget", String(Math.trunc(budget)));
              }
              return runPythonModule("pipeline.research_desk", args);
            },
          })
        : null,
  },
});
