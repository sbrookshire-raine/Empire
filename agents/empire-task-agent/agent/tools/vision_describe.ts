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
              "Describe a local image/screenshot with Ollama qwen3-vl:8b. Takes a GPU lease — expect chat model unload. Writes scratch note under vision_notes. Requires Vision Local Toolbelt.",
            inputSchema: z.object({
              image_path: z.string().min(1),
              prompt: z
                .string()
                .optional()
                .describe("What to look for / how to describe."),
            }),
            async execute({ image_path, prompt }) {
              const args = [image_path];
              if (prompt) {
                args.push("--prompt", prompt);
              }
              return runPythonModule("pipeline.vision_local", args, 300_000);
            },
          })
        : null,
  },
});
