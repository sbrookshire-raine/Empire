import { spawn } from "node:child_process";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

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

export async function cogneeRecall(
  query: string,
  dataset?: string,
): Promise<unknown> {
  const args = ["pipeline.cognee_worker", "recall", "--query", query];
  if (dataset) {
    args.push("--dataset", dataset);
  }
  return runPythonModule(args);
}

export async function cogneeRemember(
  content: string,
  dataset = "eve_memory",
): Promise<unknown> {
  return runPythonModule([
    "pipeline.cognee_worker",
    "remember",
    "--content",
    content,
    "--dataset",
    dataset,
  ]);
}

export async function cogneeImprove(dataset = "eve_memory"): Promise<unknown> {
  return runPythonModule([
    "pipeline.cognee_worker",
    "improve",
    "--dataset",
    dataset,
  ]);
}

export async function cogneeForget(dataset = "eve_memory"): Promise<unknown> {
  return runPythonModule([
    "pipeline.cognee_worker",
    "forget",
    "--dataset",
    dataset,
  ]);
}
