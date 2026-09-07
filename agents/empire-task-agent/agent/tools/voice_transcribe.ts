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
              "Transcribe a local audio file via the OpenAI-compatible speech API (Speaches/Voicebox on :8000). Requires Voice Presence Toolbelt.",
            inputSchema: z.object({
              audio_path: z.string().min(1),
            }),
            async execute({ audio_path }) {
              return runPythonModule("pipeline.voice_presence", [
                "transcribe",
                audio_path,
              ]);
            },
          })
        : null,
  },
});
