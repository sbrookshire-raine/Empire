import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { isCapabilityActive } from "#lib/toolbelt";
import { runPythonModule } from "#lib/python-pipeline";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("retrieval_rerank")
        ? defineTool({
            description:
              "Rerank candidate text passages for a query (lexical or optional CrossEncoder). Eval/scratch only — does NOT change Cognee production embeddings (nomic). Requires Retrieval Rerank Toolbelt.",
            inputSchema: z.object({
              query: z.string().min(1),
              candidates_json: z
                .string()
                .describe('JSON list of {"id","text"} candidates.'),
              top_k: z.number().int().min(1).max(50).optional(),
            }),
            async execute({ query, candidates_json, top_k }) {
              const args = [
                "rerank",
                "--query",
                query,
                "--candidates-json",
                candidates_json,
                "--write",
              ];
              if (top_k != null) {
                args.push("--top-k", String(top_k));
              }
              return runPythonModule("pipeline.retrieval_rerank", args);
            },
          })
        : null,
  },
});
