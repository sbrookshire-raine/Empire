import { readFileSync } from "node:fs";
import { join } from "node:path";
import { EMPIRE_ROOT } from "./empire";

/** Shared nucleus sampling; temperature is per chat mode. */
export const GLOBAL_CHAT_OPTIONS = {
  topP: 0.9,
} as const;

/** Protect 16 GB VRAM — every mode shares this context window. */
export const SHARED_NUM_CTX = 8_192;

export type ChatModeId = "fast" | "deep" | "librarian";

export type ChatModeDefinition = {
  readonly id: ChatModeId;
  readonly label: string;
  readonly description: string;
  readonly model: string;
  readonly modelAliases: readonly string[];
  readonly numCtx: number;
  readonly temperature: number;
};

export const CHAT_MODES: Record<ChatModeId, ChatModeDefinition> = {
  fast: {
    id: "fast",
    label: "Fast Mode (14b)",
    description:
      "Daily driver — brainstorming, quick file reads, standard scripts, and tool calls.",
    model: "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
    modelAliases: ["richardyoung/qwen2.5-14b-instruct-abliterated"],
    numCtx: SHARED_NUM_CTX,
    temperature: 0.2,
  },
  deep: {
    id: "deep",
    label: "Deep Mode (32b)",
    description:
      "Architect — deep planning, complex MCP work, and highest-tier reasoning.",
    model: "qwen2.5:32b",
    modelAliases: [],
    numCtx: SHARED_NUM_CTX,
    temperature: 0.7,
  },
  librarian: {
    id: "librarian",
    label: "Librarian (Command-R 35b)",
    description:
      "Mass synthesis — cross-reference many flattened files and long memory snippets.",
    model: "command-r:35b",
    modelAliases: [],
    numCtx: SHARED_NUM_CTX,
    temperature: 0.4,
  },
};

export const DEFAULT_CHAT_MODE: ChatModeId = "fast";

export type ActiveChatConfig = {
  mode: ChatModeId;
  model: string;
  numCtx: number;
  temperature: number;
  topP: number;
};

type ActiveModelFile = {
  mode?: unknown;
  model?: unknown;
};

function activeModelCandidates(): string[] {
  const localAppData = process.env.LOCALAPPDATA;
  return [
    localAppData ? join(localAppData, "EMPIRE", "ollama-active-model.json") : "",
    join(EMPIRE_ROOT, "config", "ollama-active-model.json"),
  ].filter(Boolean);
}

function isChatModeId(value: unknown): value is ChatModeId {
  return typeof value === "string" && value in CHAT_MODES;
}

function resolveMode(modeId: unknown, modelId: string): ChatModeDefinition {
  if (isChatModeId(modeId)) {
    return CHAT_MODES[modeId];
  }
  for (const mode of Object.values(CHAT_MODES)) {
    if (modelId === mode.model || mode.modelAliases.includes(modelId)) {
      return mode;
    }
  }
  return CHAT_MODES[DEFAULT_CHAT_MODE];
}

export function loadActiveChatConfig(): ActiveChatConfig {
  const fallbackModel =
    process.env.OLLAMA_MODEL ?? CHAT_MODES[DEFAULT_CHAT_MODE].model;
  let modeId: unknown = DEFAULT_CHAT_MODE;
  let model = fallbackModel;

  for (const filePath of activeModelCandidates()) {
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as ActiveModelFile;
      if (typeof parsed.model === "string" && parsed.model.trim()) {
        model = parsed.model.trim();
      }
      if (parsed.mode !== undefined) {
        modeId = parsed.mode;
      }
      break;
    } catch {
      continue;
    }
  }

  const mode = resolveMode(modeId, model);
  return {
    mode: mode.id,
    model,
    numCtx: mode.numCtx,
    temperature: mode.temperature,
    topP: GLOBAL_CHAT_OPTIONS.topP,
  };
}

export function injectOllamaChatOptions(
  init: RequestInit | undefined,
  config: ActiveChatConfig,
): RequestInit | undefined {
  if (!init?.body || typeof init.body !== "string") {
    return init;
  }
  try {
    const payload = JSON.parse(init.body) as Record<string, unknown>;
    payload.temperature = config.temperature;
    payload.top_p = config.topP;
    const existingOptions =
      payload.options && typeof payload.options === "object"
        ? (payload.options as Record<string, unknown>)
        : {};
    payload.options = {
      ...existingOptions,
      num_ctx: config.numCtx,
    };
    return { ...init, body: JSON.stringify(payload) };
  } catch {
    return init;
  }
}
