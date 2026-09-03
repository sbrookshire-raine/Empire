import { createOpenAI } from "@ai-sdk/openai";
import { defineAgent, defineDynamic } from "eve";
import {
  CHAT_MODES,
  DEFAULT_CHAT_MODE,
  injectOllamaChatOptions,
  loadActiveChatConfig,
} from "./lib/ollama-config";

const ollama = createOpenAI({
  baseURL: process.env.OLLAMA_BASE_URL ?? "http://localhost:11434/v1",
  apiKey: process.env.OLLAMA_API_KEY ?? "ollama",
  fetch: async (input, init) => {
    const config = loadActiveChatConfig();
    return fetch(input, injectOllamaChatOptions(init, config));
  },
});

const fallbackConfig = loadActiveChatConfig();

export default defineAgent({
  build: {
    externalDependencies: ["@modelcontextprotocol/sdk"],
  },
  model: defineDynamic({
    fallback: ollama.chat(fallbackConfig.model),
    events: {
      "step.started": () => {
        const config = loadActiveChatConfig();
        const mode = CHAT_MODES[config.mode] ?? CHAT_MODES[DEFAULT_CHAT_MODE];
        return {
          model: ollama.chat(config.model),
          modelContextWindowTokens: mode.numCtx,
        };
      },
    },
  }),
  modelContextWindowTokens: CHAT_MODES[DEFAULT_CHAT_MODE].numCtx,
});
