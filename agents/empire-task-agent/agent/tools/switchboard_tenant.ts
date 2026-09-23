import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Serial GPU tenant: acquire/release/status. One heavy tenant at a time. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("switchboard")
        ? defineTool({
  description:
    "GPU lease: acquire a heavy tenant (chat/stem/vision/voice/extract), release it, or check status. Only one heavy tenant at a time; release the prior tenant before acquiring another. Acquire defaults to dry-run; pass dry_run=false to actually lease.",
  inputSchema: z.object({
    action: z
      .enum(["acquire", "release", "status"])
      .describe("Lease action to perform."),
    tenant: z
      .string()
      .optional()
      .describe("Tenant id when action=acquire (chat/stem/vision/voice/extract)."),
    dry_run: z
      .boolean()
      .optional()
      .describe("Plan only (default true). Set false to actually mutate."),
  }),
  async execute({ action, tenant, dry_run }) {
    const args = ["tenant", action];
    if (tenant) {
      args.push("--tenant", tenant);
    }
    if (dry_run !== false) {
      args.push("--dry-run");
    }
    return runPythonModule("pipeline.switchboard", args);
  },
})
        : null,
  },
});
