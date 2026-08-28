import { defineTool } from "eve/tools";
import { z } from "zod";
import { listChatModels } from "#lib/ollama";

export default defineTool({
  description:
    "List installed Ollama chat models and the active Eve chat model.",
  inputSchema: z.object({}),
  async execute() {
    const payload = await listChatModels();
    if (!payload || typeof payload !== "object") {
      return { ok: false, connected: false, error: "Invalid Ollama response." };
    }
    const record = payload as Record<string, unknown>;
    return {
      ok: Boolean(record.ok),
      connected: Boolean(record.connected),
      active: record.active ?? null,
      models: Array.isArray(record.models) ? record.models : [],
      error: typeof record.error === "string" ? record.error : "",
    };
  },
});
