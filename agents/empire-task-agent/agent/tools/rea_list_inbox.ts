import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

/** Always registered — lists Architect REA chat uploads. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description: "List REA chat uploads (ids and analysis_roots). Auto-admits REA.",
        inputSchema: z.object({
          limit: z
            .number()
            .int()
            .min(1)
            .max(50)
            .optional()
            .describe("Max uploads to return (default 20)."),
          upload_id: z
            .string()
            .optional()
            .describe("Optional upload id to show one bundle instead of listing."),
        }),
        async execute({ limit, upload_id }) {
          const gate = await ensureLightCapability("rea", "rea list inbox");
          if (!gate.ok) {
            return gate;
          }
          if (upload_id && upload_id.trim()) {
            return runPythonModule("pipeline.rea_inbox", [
              "show",
              upload_id.trim(),
            ]);
          }
          const args = ["list"];
          if (limit != null) {
            args.push("--limit", String(limit));
          }
          return runPythonModule("pipeline.rea_inbox", args);
        },
      }),
  },
});
