import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { loomStatusViaMcp } from "#lib/loom-intake-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("loom_intake")
        ? defineTool({
            description:
              "Report Loom workspace status: primitive ledger row count, buffer/rejects, paths to seeker prompt and gap report. Requires Loom Intake Toolbelt.",
            inputSchema: z.object({}),
            async execute() {
              return loomStatusViaMcp();
            },
          })
        : null,
  },
});
