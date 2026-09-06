import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { stemRunViaMcp } from "#lib/stem-factory-mcp";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("stem_factory")
        ? defineTool({
            description:
              "Run Demucs stem separation + practice focus tracks on songs in the stem inbox (default C:/Empire_Workbench/stem_factory/input). Writes to stem_factory/output. Default limit=1. GPU preferred; may take minutes. Requires Stem Factory Toolbelt.",
            inputSchema: z.object({
              limit: z
                .number()
                .int()
                .min(1)
                .max(20)
                .optional()
                .describe("Max songs to process (default 1)."),
              device: z
                .string()
                .optional()
                .describe("cuda or cpu (default cuda, auto-falls back)."),
              overwrite: z
                .boolean()
                .optional()
                .describe("Reprocess even if outputs exist."),
            }),
            async execute({ limit, device, overwrite }) {
              return stemRunViaMcp({ limit, device, overwrite });
            },
          })
        : null,
  },
});
