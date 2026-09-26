import { createEmpireMcpClient } from "#lib/mcp-client";

const POCKETBASE_URL = process.env.POCKETBASE_URL ?? "http://127.0.0.1:8090";
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;

/** Omit invalid / natural-language dates so MCP defaults to today. */
export function sanitizeOptionalDate(value?: string): string | undefined {
  if (value == null) {
    return undefined;
  }
  const trimmed = value.trim();
  if (!trimmed) {
    return undefined;
  }
  if (ISO_DATE.test(trimmed)) {
    return trimmed;
  }
  if (/^(today|now|current)$/i.test(trimmed)) {
    return undefined;
  }
  return undefined;
}

const mcp = createEmpireMcpClient({
  label: "empire-daze",
  clientName: "eve-empire-daze",
  script: "daze_mcp.py",
  env: () => ({ POCKETBASE_URL }),
});

export const connectEmpireDazeMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireDazeMcp = (): Promise<void> => mcp.disconnect();

export async function dazeListDayViaMcp(input: {
  date?: string;
  phase?: string;
}): Promise<unknown> {
  return mcp.callTool("daze_list_day", {
    date: sanitizeOptionalDate(input.date) ?? "",
    phase: input.phase ?? "",
  });
}

export async function dazeUpsertBlockViaMcp(input: {
  title: string;
  start_minute: number;
  end_minute: number;
  date?: string;
  kind?: string;
  phase?: string;
  notes?: string;
  color?: string;
  record_id?: string;
}): Promise<unknown> {
  return mcp.callTool("daze_upsert_block", {
    title: input.title,
    start_minute: input.start_minute,
    end_minute: input.end_minute,
    date: sanitizeOptionalDate(input.date) ?? "",
    kind: input.kind ?? "focus",
    phase: input.phase ?? "planned",
    notes: input.notes ?? "",
    color: input.color ?? "",
    record_id: input.record_id ?? "",
  });
}

export async function dazeFreeWindowsViaMcp(input: {
  date?: string;
  phase?: string;
  min_minutes?: number;
}): Promise<unknown> {
  return mcp.callTool("daze_free_windows", {
    date: sanitizeOptionalDate(input.date) ?? "",
    phase: input.phase ?? "planned",
    min_minutes: input.min_minutes ?? 30,
  });
}

export async function dazeComparePhasesViaMcp(input: {
  date?: string;
}): Promise<unknown> {
  return mcp.callTool("daze_compare_phases", {
    date: sanitizeOptionalDate(input.date) ?? "",
  });
}
