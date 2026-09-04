import { defineTool } from "eve/tools";
import { z } from "zod";
import { draftWorkOrderViaMcp } from "#lib/work-order-mcp";

/** Core brain handoff — always registered (not a Toolbelt limb). */
export default defineTool({
  description:
    "Draft a Work Order markdown for the Systems Mechanic (Cursor) in 05_Work_Orders. Use after triage when something is USEFUL NOW and needs forging. Not a PocketBase task.",
  inputSchema: z.object({
    capability_needed: z
      .string()
      .min(1)
      .describe("Short name of the capability the Mechanic should build."),
    justification: z
      .string()
      .min(1)
      .describe("Why this is USEFUL NOW and what EMPIRE gains."),
    source_file: z
      .string()
      .optional()
      .describe(
        "Optional basename or relative path under C:/Empire_Workbench/00_Resource_Queue/.",
      ),
  }),
  async execute({ capability_needed, justification, source_file }) {
    return draftWorkOrderViaMcp({
      capability_needed,
      justification,
      source_file,
    });
  },
});
