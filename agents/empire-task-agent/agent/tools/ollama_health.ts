import { defineTool } from "eve/tools";
import { z } from "zod";
import { listChatModels } from "#lib/ollama";

export default defineTool({
  description: "Check whether local Ollama is reachable and which chat model is active.",
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
      modelCount: Array.isArray(record.models) ? record.models.length : 0,
      error: typeof record.error === "string" ? record.error : "",
    };
  },
});
