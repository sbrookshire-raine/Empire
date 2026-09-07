import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("container_scout")
        ? defineTool({
            description:
              "List local Docker containers matching EMPIRE names (default empire-*). Status awareness only — does not start/stop. Requires Container Scout Toolbelt.",
            inputSchema: z.object({
              name_filter: z
                .string()
                .optional()
                .describe("Substring filter for container names (default empire-)."),
            }),
            async execute({ name_filter }) {
              const args = ["docker-status"];
              if (name_filter) {
                args.push("--filter", name_filter);
              }
              return runPythonModule("pipeline.container_scout", args);
            },
          })
        : null,
  },
});
