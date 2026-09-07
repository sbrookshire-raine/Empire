import { spawn } from "node:child_process";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

/** Run `python -m <module> ...` and parse JSON stdout. */
export function runPythonModule(
  moduleName: string,
  args: string[],
  timeoutMs = 300_000,
): Promise<unknown> {
  return new Promise((resolve) => {
    const child = spawn(PYTHON_BIN, ["-m", moduleName, ...args], {
      cwd: EMPIRE_ROOT,
      env: { ...process.env, PYTHONPATH: EMPIRE_ROOT },
      windowsHide: true,
    });

    let stdout = "";
    let stderr = "";
    const timer = setTimeout(() => {
      try {
        child.kill();
      } catch {
        /* ignore */
      }
      resolve({
        ok: false,
        error: `Timed out after ${timeoutMs}ms running ${moduleName}`,
      });
    }, timeoutMs);

    child.stdout.setEncoding("utf8");
    child.stderr.setEncoding("utf8");
    child.stdout.on("data", (chunk: string) => {
      stdout += chunk;
    });
    child.stderr.on("data", (chunk: string) => {
      stderr += chunk;
    });
    child.on("error", (error) => {
      clearTimeout(timer);
      resolve({ ok: false, error: error.message });
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      const trimmed = stdout.trim();
      if (!trimmed) {
        resolve({
          ok: code === 0,
          error: code === 0 ? undefined : stderr.trim() || `exit ${code}`,
        });
        return;
      }
      try {
        resolve(JSON.parse(trimmed) as unknown);
      } catch {
        resolve({
          ok: code === 0,
          raw: trimmed,
          error: code === 0 ? undefined : stderr.trim(),
        });
      }
    });
  });
}
