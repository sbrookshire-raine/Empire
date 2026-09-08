# skill-browser-local

When the Architect wants a page from the local EMPIRE UI inspected:

1. Toolbelt **Browser Local** ON.
2. Call `browser_local_fetch` only with allowlisted localhost URLs (Workbench `:8080`, PocketBase `:8090`).
3. If blocked, say the URL is outside the allowlist — do not invent page content.
4. Never submit forms or browse the public internet with this tool.
5. Never auto-`cognee_remember`.
