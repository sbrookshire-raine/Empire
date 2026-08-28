import { spawn } from "node:child_process";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

type JsonRecord = Record<string, unknown>;

function runPythonModule(moduleArgs: string[]): Promise<unknown> {
  return new Promise((resolve, reject) => {
    const child = spawn(PYTHON_BIN, ["-m", ...moduleArgs], {
      cwd: EMPIRE_ROOT,
      env: { ...process.env, PYTHONPATH: EMPIRE_ROOT },
      windowsHide: true,
    });

    let stdout = "";
    let stderr = "";

    child.stdout.setEncoding("utf8");
    child.stderr.setEncoding("utf8");
    child.stdout.on("data", (chunk: string) => {
      stdout += chunk;
    });
    child.stderr.on("data", (chunk: string) => {
      stderr += chunk;
    });

    child.on("error", (error) => {
      reject(error);
    });

    child.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(stderr.trim() || stdout.trim() || `exit ${code}`));
        return;
      }
      const trimmed = stdout.trim();
      if (!trimmed) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(trimmed));
      } catch {
        resolve({ raw: trimmed });
      }
    });
  });
}

export async function getModelSuite(): Promise<unknown> {
  return runPythonModule(["frontend.ollama_cli", "inventory"]);
}

export async function listChatModels(): Promise<unknown> {
  return runPythonModule(["frontend.ollama_cli", "models"]);
}

export async function switchChatModel(model: string): Promise<unknown> {
  return runPythonModule(["frontend.ollama_cli", "set-active", model]);
}

export function summarizeSuite(payload: unknown): JsonRecord {
  if (!payload || typeof payload !== "object") {
    return { ok: false, error: "Invalid inventory payload." };
  }
  const record = payload as JsonRecord;
  const recommendations = record.recommendations;
  if (!recommendations || typeof recommendations !== "object") {
    return {
      ok: Boolean(record.ok),
      connected: record.connected ?? true,
      error: typeof record.error === "string" ? record.error : "",
      summary: "",
      eveGuidance: {},
      pullGaps: [],
      removeSuggestions: [],
    };
  }
  const rec = recommendations as JsonRecord;
  const suite = Array.isArray(rec.suite) ? rec.suite : [];
  return {
    ok: Boolean(record.ok ?? true),
    summary: typeof rec.summary === "string" ? rec.summary : "",
    activeChat: rec.activeChat ?? null,
    eveGuidance: rec.eveGuidance ?? {},
    eveBriefing:
      typeof rec.eveBriefing === "string" ? rec.eveBriefing : "",
    suite: suite.map((slot) => {
      if (!slot || typeof slot !== "object") return slot;
      const item = slot as JsonRecord;
      return {
        id: item.id,
        label: item.label,
        status: item.status,
        installedId: item.installedId ?? null,
        idealId:
          item.ideal && typeof item.ideal === "object"
            ? (item.ideal as JsonRecord).id
            : null,
        whenToUse:
          item.ideal && typeof item.ideal === "object"
            ? (item.ideal as JsonRecord).whenToUse
            : "",
        pull:
          item.pull && typeof item.pull === "object"
            ? (item.pull as JsonRecord).command
            : null,
      };
    }),
    pullGaps: rec.pullGaps ?? [],
    removeSuggestions: rec.removeSuggestions ?? [],
    recommendedKeep: rec.recommendedKeep ?? [],
  };
}
