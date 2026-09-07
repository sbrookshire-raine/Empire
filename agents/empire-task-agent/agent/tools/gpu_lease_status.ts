import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Show which heavy GPU tenant holds the EMPIRE lease (chat/stem/vision/voice/idle).",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.gpu_lease", ["status"]);
  },
});
