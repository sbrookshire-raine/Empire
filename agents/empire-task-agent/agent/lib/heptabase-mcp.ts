import { createEmpireMcpClient } from "#lib/mcp-client";

const mcp = createEmpireMcpClient({
  label: "empire-heptabase",
  clientName: "eve-empire-heptabase",
  script: "heptabase_mcp.py",
});

export async function heptabaseHealthViaMcp(): Promise<unknown> {
  return mcp.callTool("heptabase_health", {});
}

export async function heptabaseSearchViaMcp(input: {
  query?: string;
  limit?: number;
}): Promise<unknown> {
  return mcp.callTool("heptabase_search", {
    query: input.query ?? "",
    limit: input.limit ?? 20,
  });
}

export async function heptabaseReadNoteViaMcp(cardId: string): Promise<unknown> {
  return mcp.callTool("heptabase_read_note", { card_id: cardId });
}

export async function heptabaseWhiteboardStructureViaMcp(input: {
  whiteboard_id?: string;
}): Promise<unknown> {
  return mcp.callTool("heptabase_whiteboard_structure", {
    whiteboard_id: input.whiteboard_id ?? "",
  });
}

export async function disassemblyCardWriteViaMcp(payloadJson: string): Promise<unknown> {
  return mcp.callTool("disassembly_card_write", { payload_json: payloadJson });
}

export async function disassemblyCardListViaMcp(limit?: number): Promise<unknown> {
  return mcp.callTool("disassembly_card_list", { limit: limit ?? 30 });
}

export async function disassemblyPublishHeptabaseViaMcp(input: {
  card_id: string;
  architect_confirm: boolean;
}): Promise<unknown> {
  return mcp.callTool("disassembly_publish_heptabase", {
    card_id: input.card_id,
    architect_confirm: input.architect_confirm,
  });
}

export async function disassemblyMarkMatureViaMcp(input: {
  card_id: string;
  architect_confirm: boolean;
}): Promise<unknown> {
  return mcp.callTool("disassembly_mark_mature", {
    card_id: input.card_id,
    architect_confirm: input.architect_confirm,
  });
}
