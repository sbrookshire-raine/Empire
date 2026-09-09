import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { loomProcessShellCsvViaMcp } from "#lib/loom-intake-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("loom_intake")
        ? defineTool({
            description:
              "Process a 12-column Shell Packet CSV through the Keeper Knowledge Shell (validate, throttle max 7/cycle, gate, append to primitive_ledger.csv). CSV may be in Resource Queue or an absolute path. Requires Loom Intake Toolbelt.",
            inputSchema: z.object({
              csv_path: z
                .string()
                .describe(
                  "Path or filename of Shell Packet CSV (12 columns). Tries Resource Queue then loom/intake.",
                ),
              domain_bucket: z
                .string()
                .optional()
                .describe(
                  "Domain bucket label for gap matrix (e.g. education, software, general).",
                ),
              max_per_cycle: z
                .number()
                .int()
                .min(1)
                .max(7)
                .optional()
                .describe("Promotion cap per cycle (default 7, hard max 7)."),
            }),
            async execute({ csv_path, domain_bucket, max_per_cycle }) {
              return loomProcessShellCsvViaMcp({
                csv_path,
                domain_bucket,
                max_per_cycle,
              });
            },
          })
        : null,
  },
});
