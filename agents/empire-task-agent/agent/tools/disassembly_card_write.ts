import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

const connectionSchema = z.object({
  from: z.string().min(1),
  to: z.string().min(1),
  kind: z.string().optional(),
  evidence_ref: z.string().optional(),
});

/** Always registered — one Disassembly Card per serious RE play session. */
export default defineDynamic({
  events: {
    "turn.started": () =>
      defineTool({
        description:
          "Write one local Disassembly Card after an RE session (connections + evidence). Auto-admits REA.",
        inputSchema: z.object({
          title: z.string().min(1),
          container: z
            .enum([
              "electron",
              "native_pe",
              "web",
              "game_logic",
              "audio_pipeline",
              "unknown",
            ])
            .optional(),
          target_summary: z.string().min(1),
          connections: z.array(connectionSchema).min(1).max(7),
          evidence_refs: z.array(z.string()).optional(),
          lego_hooks: z.array(z.string()).optional(),
          evolution_note: z.string().optional(),
          depends_on: z.array(z.string()).optional(),
          related_card_ids: z.array(z.string()).optional(),
        }),
        async execute(input) {
          const gate = await ensureLightCapability("rea", `disassembly card: ${input.title}`);
          if (!gate.ok) {
            return gate;
          }
          const dir = mkdtempSync(join(tmpdir(), "empire-dc-"));
          const filePath = join(dir, "payload.json");
          writeFileSync(
            filePath,
            JSON.stringify(
              {
                title: input.title,
                container: input.container ?? "unknown",
                target_summary: input.target_summary,
                connections: input.connections,
                evidence_refs: input.evidence_refs ?? [],
                lego_hooks: input.lego_hooks ?? [],
                evolution_note: input.evolution_note ?? "",
                depends_on: input.depends_on ?? [],
                related_card_ids: input.related_card_ids ?? [],
              },
              null,
              2,
            ),
            "utf8",
          );
          return runPythonModule("pipeline.disassembly_card", ["write", "--file", filePath]);
        },
      }),
  },
});
