import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("browser_local")
        ? defineTool({
            description:
              "Screenshot then vision UI observe for localhost URL or local HTML.",
            inputSchema: z.object({
              url: z
                .string()
                .optional()
                .describe("Allowlisted http(s) URL to open in headless Chromium."),
              html_path: z
                .string()
                .optional()
                .describe("Absolute path to HTML under REA inbox or Empire_Workbench."),
              full_page: z.boolean().optional(),
              note: z.string().optional().describe("What to look for in the UI."),
            }),
            async execute({ url, html_path, full_page, note }) {
              const browserGate = await ensureLightCapability(
                "browser_local",
                `visual observe capture: ${url || html_path || "target"}`,
              );
              if (!browserGate.ok) {
                return browserGate;
              }
              const visionGate = await ensureLightCapability(
                "vision_local",
                `visual observe vision: ${url || html_path || "target"}`,
              );
              if (!visionGate.ok) {
                return visionGate;
              }
              const args: string[] = [];
              if (url) {
                args.push("--url", url);
              }
              if (html_path) {
                args.push("--html-path", html_path);
              }
              if (full_page) {
                args.push("--full-page");
              }
              if (note) {
                args.push("--note", note);
              }
              return runPythonModule("pipeline.app_visual_observe", args);
            },
          })
        : null,
  },
});
