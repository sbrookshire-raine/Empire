import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Read-only snapshot of services + headroom + GPU lease. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("switchboard")
        ? defineTool({
  description:
    "Switchboard status: which EMPIRE services are up, machine headroom, and the current GPU lease. Read-only. Use before deciding to start/stop services for a task.",
  inputSchema: z.object({}),
  async execute() {
    return runPythonModule("pipeline.switchboard", ["status"]);
  },
})
        : null,
  },
});
