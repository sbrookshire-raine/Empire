import { defineTool } from "eve/tools";
import { z } from "zod";
import { switchChatModel } from "#lib/ollama";

export default defineTool({
  description:
    "Switch Eve's active Ollama chat model for subsequent agent steps. Use before coding, reasoning, or deep-quality work.",
  inputSchema: z.object({
    model: z
      .string()
      .min(1)
      .describe("Installed Ollama chat model id, e.g. llama3.1:8b or deepseek-r1:8b"),
    reason: z
      .string()
      .optional()
      .describe("Short note on why this model fits the task (for the user)."),
  }),
  async execute({ model, reason }) {
    const payload = await switchChatModel(model);
    if (!payload || typeof payload !== "object") {
      return { ok: false, error: "Invalid switch response." };
    }
    const record = payload as Record<string, unknown>;
    return {
      ok: Boolean(record.ok),
      active: record.active ?? model,
      models: Array.isArray(record.models) ? record.models : [],
      reason: reason ?? null,
      error: typeof record.error === "string" ? record.error : "",
      note: "Subsequent Eve steps use this model. Heavy models may be slower on 16 GB VRAM.",
    };
  },
});
