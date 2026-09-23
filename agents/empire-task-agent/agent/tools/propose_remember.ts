import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/** Propose a short note into eve_staging (Architect must confirm to keep). */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("file_ops")
        ? defineTool({
  description:
    "Propose remembering a short note into Eve's staging sandbox (eve_staging). " +
    "Use when something seems worth keeping. Do NOT confirm permanence yourself — " +
    "ask the Architect to keep or drop. Never bulk-ingest Wikipedia.",
  inputSchema: z.object({
    content: z.string().min(1).max(8000).describe("Short note to stage."),
    reason: z
      .string()
      .optional()
      .describe("Why this might have value (one line)."),
    crumb: z
      .string()
      .optional()
      .describe("Optional success marker / recall crumb (not encyclopedia dump)."),
  }),
  async execute({ content, reason, crumb }) {
    const args = ["propose", "--content", content];
    if (reason) args.push("--reason", reason);
    if (crumb) args.push("--crumb", crumb);
    return runPythonModule("pipeline.eve_staging", args);
  },
})
        : null,
  },
});
