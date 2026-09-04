import { disableTool } from "eve/tools";

// Sandbox FS tools invent /home/vercel-sandbox paths. Use workbench_read_file instead.
export default disableTool();
