import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCategoryEnabled } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCategoryEnabled("voice_presence")
        ? defineTool({
            description:
              "Speak text via local TTS (Piper/Kokoro through speech API). Prefer short replies. Requires Voice Presence Toolbelt.",
            inputSchema: z.object({
              text: z.string().min(1).max(4000),
              output_path: z.string().optional(),
            }),
            async execute({ text, output_path }) {
              const args = ["speak", text];
              if (output_path) {
                args.push("-o", output_path);
              }
              return runPythonModule("pipeline.voice_presence", args);
            },
          })
        : null,
  },
});
