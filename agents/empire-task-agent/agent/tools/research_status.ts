import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * Where a research job is now, or everything still waiting on the desk (E-37).
 *
 * With no job id it lists open jobs, which is how she comes back to work she started earlier.
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("web_research")
        ? defineTool({
            description:
              "Check a research job's state (or list open jobs when called with no id). Cheap; safe to call every turn.",
            inputSchema: z.object({
              job_id: z.string().optional().describe("Job id from research_start; omit to list open jobs."),
            }),
            async execute({ job_id }) {
              const args = job_id && job_id.trim() ? ["status", job_id.trim()] : ["open"];
              return runPythonModule("pipeline.research_desk", args);
            },
          })
        : null,
  },
});
