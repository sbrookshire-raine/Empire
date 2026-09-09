import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Show Research Autopilot status: partner mode, session capabilities, TTL, GPU lease, effective Toolbelt.",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.admission_controller", ["status"]);
  },
});
