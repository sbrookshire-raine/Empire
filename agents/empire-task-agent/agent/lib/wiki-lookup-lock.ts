import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { EMPIRE_ROOT } from "#lib/empire";

/**
 * When Workbench injects [[EMPIRE_WIKI_LOOKUP]], Python writes this lock so Eve
 * does not register wiki_scout_search / compare_years for the turn.
 */
function lockPaths(): string[] {
  const override = process.env.EMPIRE_WIKI_LOOKUP_LOCK?.trim();
  if (override) {
    return [override];
  }
  const localAppData = process.env.LOCALAPPDATA;
  return [
    localAppData ? join(localAppData, "EMPIRE", "eve-wiki-lookup-lock.json") : "",
    join(EMPIRE_ROOT, "config", "eve-wiki-lookup-lock.json"),
  ].filter(Boolean);
}

export function isWikiLookupLocked(): boolean {
  for (const filePath of lockPaths()) {
    if (!existsSync(filePath)) {
      continue;
    }
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as {
        active?: unknown;
        expires_at?: unknown;
      };
      if (!parsed.active) {
        continue;
      }
      const expires =
        typeof parsed.expires_at === "number"
          ? parsed.expires_at
          : Number(parsed.expires_at);
      if (!Number.isFinite(expires)) {
        continue;
      }
      // Python stores unix seconds; allow a small clock skew.
      if (Date.now() / 1000 <= expires) {
        return true;
      }
    } catch {
      continue;
    }
  }
  return false;
}

export const WIKI_LOOKUP_LOCK_REPLY = {
  ok: true,
  usable: false,
  source: "lookup_lock",
  cards: [] as unknown[],
  paths: [] as string[],
  titles: [] as string[],
  chat_reply_rule:
    "[[EMPIRE_WIKI_LOOKUP]] evidence was already injected for this turn. " +
    "Do NOT call wiki tools again. Answer only from that EVIDENCE / CONTRACT block. " +
    "Do NOT mention Weaviate, Docker, or port 8091.",
  coverage_note: "Wiki lookup lock active — refuse redundant tool call.",
};
