import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("vision_local")
        ? defineTool({
            description: "Structured UI regions from a local screenshot (qwen3-vl).",
            inputSchema: z.object({
              image_path: z.string().min(1),
              note: z.string().optional(),
            }),
            async execute({ image_path, note }) {
              const gate = await ensureLightCapability(
                "vision_local",
                `vision observe: ${image_path}`,
              );
              if (!gate.ok) {
                return gate;
              }
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
