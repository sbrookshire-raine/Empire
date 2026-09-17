import { defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";

/** Read-only DuckDB over local data files. */
export default defineTool({
  description:
    "Run a read-only SQL query (DuckDB) over a local CSV/JSON/Parquet/SQLite file. Pass data_file (allowlisted local path) and query against table `data`; or pass a full SELECT with no file. No network, no writes, no extensions. Caps rows/bytes/time.",
  inputSchema: z.object({
    sql: z
      .string()
      .min(1)
      .describe("SQL query, e.g. 'SELECT * FROM data WHERE age > 40 LIMIT 20'."),
    data_file: z
      .string()
      .optional()
      .describe("Optional allowlisted local data file to register as table `data`."),
    max_rows: z
      .number()
      .int()
      .min(1)
      .max(10000)
      .optional()
      .describe("Max rows to return (default 1000)."),
  }),
  async execute({ sql, data_file, max_rows }) {
    const args = [sql];
    if (data_file) {
      args.push("--data-file", data_file);
    }
    if (max_rows != null) {
      args.push("--max-rows", String(max_rows));
    }
    return runPythonModule("pipeline.query_data", args);
  },
});
