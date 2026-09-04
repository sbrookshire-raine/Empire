import { disableTool } from "eve/tools";

// Local Ollama has no shell sandbox for EMPIRE day-to-day work. Use workbench_* tools.
export default disableTool();
