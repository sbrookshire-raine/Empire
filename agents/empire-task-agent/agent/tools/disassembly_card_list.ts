import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("rea")
        ? defineTool({
            description: "List recent local Disassembly Cards on disk.",
            inputSchema: z.object({
              limit: z.number().int().min(1).max(100).optional(),
            }),
            async execute({ limit }) {
              const gate = await ensureLightCapability("rea", "disassembly list");
              if (!gate.ok) {
                return gate;
              }
              const args = ["list"];
              if (limit != null) {
                args.push("--limit", String(limit));
              }
              return runPythonModule("pipeline.disassembly_card", args);
            },
          })
        : null,
  },
});
