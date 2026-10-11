import { defineSandbox } from "eve/sandbox";
import { justbash } from "eve/sandbox/just-bash";

/**
 * EMPIRE runs locally with bash/glob/read_file disabled — workbench_* tools hit Windows paths.
 * defaultBackend() would pick Docker on Windows and leave one container per chat session;
 * just-bash keeps isolation in-process with no Docker churn.
 */
export default defineSandbox({
  backend: justbash(),
  async onSession({ use }) {
    await use({ networkPolicy: "deny-all" });
  },
});
