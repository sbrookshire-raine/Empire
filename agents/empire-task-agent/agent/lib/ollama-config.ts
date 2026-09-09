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
    model: "qwen2.5:14b-instruct",
    modelAliases: ["qwen2.5:14b"],
    numCtx: SHARED_NUM_CTX,
    temperature: 0.2,
  },
    deep: {
    id: "deep",
    label: "Deep Mode (Qwen3 14b)",
    description:
      "Architect — deep planning, complex MCP work, and highest-tier reasoning.",
    model: "qwen3:14b",
    modelAliases: ["qwen2.5:32b"],
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

function fastAbCandidates(): string[] {
  const localAppData = process.env.LOCALAPPDATA;
  return [
    localAppData ? join(localAppData, "EMPIRE", "ollama-fast-ab.json") : "",
    join(EMPIRE_ROOT, "config", "ollama-fast-ab.json"),
  ].filter(Boolean);
}

function resolveFastAbModel(defaultModel: string): string {
  for (const filePath of fastAbCandidates()) {
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as {
        variant?: unknown;
        b_model?: unknown;
      };
      const variant = String(parsed.variant || "a").toLowerCase();
      if (variant === "b" && typeof parsed.b_model === "string" && parsed.b_model.trim()) {
        return parsed.b_model.trim();
      }
      break;
    } catch {
      continue;
    }
  }
  return defaultModel;
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
  const resolvedModel =
    mode.id === "fast" ? resolveFastAbModel(mode.model) : model;
  return {
    mode: mode.id,
    model: resolvedModel,
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
