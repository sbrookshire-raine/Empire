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
  "web_scout",
  "thought_experiments",
  "voice_presence",
  "vision_local",
  "container_scout",
  "github_scout",
  "structured_extract",
  "retrieval_rerank",
  "browser_local",
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

function sessionPaths(): string[] {
  const localAppData = process.env.LOCALAPPDATA;
  return [
    localAppData ? join(localAppData, "EMPIRE", "eve-capability-session.json") : "",
    join(EMPIRE_ROOT, "config", "eve-capability-session.json"),
  ].filter(Boolean);
}

function parseSession(): {
  researchPartnerMode: boolean;
  sessionCapabilities: ToolbeltCategory[];
  expiresAt: string;
} {
  for (const filePath of sessionPaths()) {
    try {
      const parsed = JSON.parse(readFileSync(filePath, "utf8")) as {
        research_partner_mode?: unknown;
        session_capabilities?: unknown;
        expires_at?: unknown;
      };
      const caps = Array.isArray(parsed.session_capabilities)
        ? parsed.session_capabilities.filter(
            (item): item is ToolbeltCategory =>
              typeof item === "string" && isToolbeltCategory(item),
          )
        : [];
      return {
        researchPartnerMode: Boolean(parsed.research_partner_mode),
        sessionCapabilities: caps,
        expiresAt: typeof parsed.expires_at === "string" ? parsed.expires_at : "",
      };
    } catch {
      continue;
    }
  }
  return { researchPartnerMode: false, sessionCapabilities: [], expiresAt: "" };
}

function sessionStillValid(expiresAt: string): boolean {
  if (!expiresAt.trim()) {
    return false;
  }
  const expires = Date.parse(expiresAt);
  if (Number.isNaN(expires)) {
    return false;
  }
  return Date.now() < expires;
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

/** Manual Toolbelt OR valid Research Autopilot session grant. */
export function isCapabilityActive(category: ToolbeltCategory): boolean {
  if (isCategoryEnabled(category)) {
    return true;
  }
  const session = parseSession();
  if (!session.researchPartnerMode || !sessionStillValid(session.expiresAt)) {
    return false;
  }
  return session.sessionCapabilities.includes(category);
}

export function loadEffectiveToolCategories(): ToolbeltCategory[] {
  const manual = loadActiveToolCategories();
  const session = parseSession();
  if (!session.researchPartnerMode || !sessionStillValid(session.expiresAt)) {
    return manual;
  }
  const merged: ToolbeltCategory[] = [];
  for (const item of [...manual, ...session.sessionCapabilities]) {
    if (!merged.includes(item)) {
      merged.push(item);
    }
  }
  return merged;
}
