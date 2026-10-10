import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Headroom + inventory so Eve knows what she has and what she can safely admit. */
export default defineTool({
  description:
              "Resource pulse: capacity_meter (progress bars + headroom_score), activation map (ACTIVE/DORMANT/OFF/LOCKED), effective tools, can_admit_now, GPU lease.",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.resource_pulse", ["pulse"]);
  },
});
