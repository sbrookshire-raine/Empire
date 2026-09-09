import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("structured_extract")
        ? defineTool({
            description:
              "Extract DocumentMetadata (title, author, date, tags, summary) from text via local llama.cpp worker (Ollama JSON fallback). Scratch cache only — never Cognee. Requires Structured Extract Toolbelt.",
            inputSchema: z.object({
              text: z.string().min(1).describe("Plain text to extract from."),
              prefer: z
                .enum(["llama", "ollama"])
                .optional()
                .describe("Backend preference (default llama)."),
              note: z.string().optional().describe("Optional Architect note."),
            }),
            async execute({ text, prefer, note }) {
              const args = ["text", text, "--prefer", prefer || "llama"];
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.structured_extract", args);
            },
          })
        : null,
  },
});
