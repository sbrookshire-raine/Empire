import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Headroom-gated service start. Light ensures auto-admit; GPU tenants need Architect. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("switchboard")
        ? defineTool({
  description:
    "Start the EMPIRE services a task needs (pocketbase, frontend) after a headroom check. Never starts Ollama or Eve (external/self). Defaults to dry-run planning; pass dry_run=false to actually start. If ok is false with headroom reasons, do not retry — ask the Architect.",
  inputSchema: z.object({
    services: z
      .array(z.string())
      .min(1)
      .describe("Service ids to ensure, e.g. ['pocketbase', 'frontend']."),
    dry_run: z
      .boolean()
      .optional()
      .describe("Plan only (default true). Set false to actually start."),
  }),
  async execute({ services, dry_run }) {
    const args = ["ensure", ...services];
    if (dry_run !== false) {
      args.push("--dry-run");
    }
    return runPythonModule("pipeline.switchboard", args);
  },
})
        : null,
  },
});
