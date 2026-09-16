import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive, type ToolbeltCategory } from "#lib/toolbelt";

type AdmitResult = {
  ok?: boolean;
  error?: string;
  need_architect?: boolean;
};

/**
 * Ensure a light session limb is active for this turn.
 * Uses resource-gated admit_for_goal when the limb is off (no Toolbelt click).
 */
export async function ensureLightCapability(
  category: ToolbeltCategory,
  reason: string,
): Promise<{ ok: true } | { ok: false; error: string; admission: unknown }> {
  if (isCapabilityActive(category)) {
    return { ok: true };
  }
  const admission = (await runPythonModule("pipeline.resource_pulse", [
    "admit",
    category,
    "--reason",
    (reason || `eve ensure ${category}`).slice(0, 200),
  ])) as AdmitResult;
  if (admission && admission.ok && isCapabilityActive(category)) {
    return { ok: true };
  }
  const err =
    (admission && typeof admission.error === "string" && admission.error) ||
    (admission && admission.need_architect
      ? `Ask the Architect before enabling ${category}.`
      : `Could not admit ${category} for this turn.`);
  return { ok: false, error: err, admission };
}
