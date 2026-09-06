import { readFileSync } from "node:fs";
import { join } from "node:path";
import { EMPIRE_ROOT } from "#lib/empire";

/**
 * Optional heavy limbs only. Cognee memory and PocketBase tasks are core brain
 * tools and must never be gated here.
 *
 * PocketBase = Tasks. Work Orders = separate .md requests for Cursor — do not
 * conflate the two.
 */
export const TOOLBELT_CATEGORIES = [
  "gumloop_cloud",
  "web_research",
  "tool_forge",
  "wiki_local",
  "time_reclaim",
  "stem_factory",
] as const;

export type ToolbeltCategory = (typeof TOOLBELT_CATEGORIES)[number];

const DEFAULT_ACTIVE: ToolbeltCategory[] = [];

function isToolbeltCategory(value: string): value is ToolbeltCategory {
  return (TOOLBELT_CATEGORIES as readonly string[]).includes(value);
}

function candidatePaths(): string[] {
  const localAppData = process.env.LOCALAPPDATA;
  return [
    localAppData ? join(localAppData, "EMPIRE", "eve-toolbelt.json") : "",
    join(EMPIRE_ROOT, "config", "eve-toolbelt.json"),
  ].filter(Boolean);
}

export function loadActiveToolCategories(): ToolbeltCategory[] {
  for (const filePath of candidatePaths()) {
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as {
        active_tools?: unknown;
      };
      if (!Array.isArray(parsed.active_tools)) {
        continue;
      }
      const selected = parsed.active_tools.filter(
        (item): item is ToolbeltCategory =>
          typeof item === "string" && isToolbeltCategory(item),
      );
      return selected;
    } catch {
      continue;
    }
  }
  return DEFAULT_ACTIVE;
}

export function isCategoryEnabled(category: ToolbeltCategory): boolean {
  return loadActiveToolCategories().includes(category);
}
