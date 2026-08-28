import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent, defineDynamic } from "eve";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { EMPIRE_ROOT } from "./lib/empire";

const ollama = createOpenAI({
  baseURL: process.env.OLLAMA_BASE_URL ?? "http://localhost:11434/v1",
  apiKey: process.env.OLLAMA_API_KEY ?? "ollama",
});

const modelId = process.env.OLLAMA_MODEL ?? "llama3.1:8b";

function selectedOllamaModel(): string {
  const fallback = process.env.OLLAMA_MODEL ?? "llama3.1:8b";
  const localAppData = process.env.LOCALAPPDATA;
  const candidates = [
    localAppData ? join(localAppData, "EMPIRE", "ollama-active-model.json") : "",
    join(EMPIRE_ROOT, "config", "ollama-active-model.json"),
  ].filter(Boolean);
  for (const filePath of candidates) {
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as {
        model?: unknown;
      };
      if (typeof parsed.model === "string" && parsed.model.trim()) {
        return parsed.model.trim();
      }
    } catch {
      continue;
    }
  }
  return fallback;
}

export default defineAgent({
  model: defineDynamic({
    fallback: ollama.chat(modelId),
    events: {
      "step.started": () => ollama.chat(selectedOllamaModel()),
    },
  }),
  modelContextWindowTokens: 32_768,
});
