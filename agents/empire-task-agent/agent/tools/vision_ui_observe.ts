import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("vision_local")
        ? defineTool({
            description:
              "Observe a local screenshot for UI regions (structured). Observation only — no clicks/automation. Uses qwen3-vl. Requires Vision Local Toolbelt.",
            inputSchema: z.object({
              image_path: z.string().min(1),
              note: z.string().optional(),
            }),
            async execute({ image_path, note }) {
              const args = [image_path];
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.vision_ui_observe", args);
            },
          })
        : null,
  },
});
