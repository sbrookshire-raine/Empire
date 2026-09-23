import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Drop a staging proposal — Architect deny, or Eve cleaning after they say drop. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("file_ops")
        ? defineTool({
  description:
    "Drop an eve_staging proposal (delete staging file + mark dropped). " +
    "Use when the Architect says drop/forget that staging id, or after TTL sweep.",
  inputSchema: z.object({
    entry_id: z.string().min(1).describe("Staging id to drop."),
  }),
  async execute({ entry_id }) {
    return runPythonModule("pipeline.eve_staging", ["drop", entry_id]);
  },
})
        : null,
  },
});
