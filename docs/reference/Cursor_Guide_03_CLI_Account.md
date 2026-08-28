# Cursor Documentation — Complete Guide (Part 3: CLI and Account/Enterprise)

> **NotebookLM ingestion note:** This is 3 of 3 companion files covering the official Cursor documentation. Upload all 3 parts (plus the index file, if provided) as sources in the same NotebookLM notebook to build a complete learning plan. Each page below is a cleaned, self-contained section with its original source URL cited.

- **Source:** https://cursor.com/docs (official Cursor documentation)
- **Pages in this file:** 41
- **Total pages across all parts:** 101
- **Date compiled:** 2026-07-18

## Table of Contents

- [CLI](#cli)
  - [Cursor CLI](#cursor-cli)
  - [Installation](#installation)
  - [Using Agent in CLI](#using-agent-in-cli)
  - [CLI Changelog](#cli-changelog)
  - [Shell Mode](#shell-mode)
  - [ACP](#acp)
  - [Using Headless CLI](#using-headless-cli)
  - [Slash commands](#slash-commands)
  - [Parameters](#parameters)
  - [Authentication](#authentication)
  - [Permissions](#permissions)
  - [Configuration](#configuration)
  - [GitHub Actions](#github-actions)
  - [Output format](#output-format)
  - [Terminal setup](#terminal-setup)
- [Account & Enterprise](#account-enterprise)
  - [Get Started](#get-started)
  - [Team Pricing](#team-pricing)
  - [Members, Roles, and Seat Types](#members-roles-and-seat-types)
  - [SSO](#sso)
  - [Dashboard](#dashboard)
  - [Usage Analytics](#usage-analytics)
  - [Enterprise](#enterprise)
  - [Organizations](#organizations)
  - [Organization Groups](#organization-groups)
  - [Identity and Access Management](#identity-and-access-management)
  - [SCIM](#scim)
  - [Privacy and Data Governance](#privacy-and-data-governance)
  - [Network Configuration](#network-configuration)
  - [Private Connectivity](#private-connectivity)
  - [Endpoint Security Configuration](#endpoint-security-configuration)
  - [LLM Safety and Controls](#llm-safety-and-controls)
  - [Model and Integration Management](#model-and-integration-management)
  - [Cyber Safeguards](#cyber-safeguards)
  - [Pooled usage](#pooled-usage)
  - [Compliance and Monitoring](#compliance-and-monitoring)
  - [HIPAA Business Associate Agreements](#hipaa-business-associate-agreements)
  - [Deployment Patterns](#deployment-patterns)
  - [Service Accounts](#service-accounts)
  - [Billing Groups](#billing-groups)
  - [Security and Privacy Hardening](#security-and-privacy-hardening)
  - [Cursor Blame](#cursor-blame)

---
## CLI

### Cursor CLI

*Cursor CLI lets you interact with AI agents directly from your terminal to write, review, and modify code. Whether you prefer an interactive terminal interface or print automation for scripts and CI pipelines, the CLI provides powerful coding assistance right where you work.*

**Source:** https://cursor.com/docs/cli/overview

Cursor CLI lets you interact with AI agents directly from your terminal to write, review, and modify code. Whether you prefer an interactive terminal interface or print automation for scripts and CI pipelines, the CLI provides powerful coding assistance right where you work.

#### Getting started

```bash
# Install (macOS, Linux, WSL)
curl https://cursor.com/install -fsS | bash

# Install (Windows PowerShell)
irm 'https://cursor.com/install?win32=true' | iex

# Run interactive session
agent
```

[Media](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/uploads/plan-mode.mp4)

#### Interactive mode

Start a conversational session with the agent to describe your goals, review proposed changes, and approve commands:

```bash
# Start interactive session
agent

# Start with initial prompt
agent "refactor the auth module to use JWT tokens"
```

#### Modes

The CLI supports the same modes as the editor. Switch between modes using slash commands, keyboard shortcuts, or the `--mode` flag.

| Mode      | Description                                                  | Shortcut                                    |
| :-------- | :----------------------------------------------------------- | :------------------------------------------ |
| **Agent** | Full access to all tools for complex coding tasks            | Default (no `--mode` value needed)          |
| **Plan**  | Design your approach before coding with clarifying questions | Shift+Tab, `/plan`, `--plan`, `--mode=plan` |
| **Ask**   | Read-only exploration without making changes                 | `/ask`, `--mode=ask`                        |

#### Non-interactive mode

Use print mode for non-interactive scenarios like scripts, CI pipelines, or automation:

```bash
# Run with specific prompt and model
agent -p "find and fix performance issues" --model "gpt-5"

# Use with git changes included for review
agent -p "review these changes for security issues" --output-format text
```

#### Cloud Agent handoff

Push your conversation to a [Cloud Agent](https://cursor.com/docs/cloud-agent.md) to continue running while you're away. Prepend `&` to any message:

```bash
# Send a task to Cloud Agent mid-conversation
& refactor the auth module and add comprehensive tests
```

Pick up your Cloud Agent tasks on web or mobile at [cursor.com/agents](https://cursor.com/agents).

#### Sessions

Resume previous conversations to maintain context across multiple interactions:

```bash
# Open previous chats and resume one
agent ls

# Resume latest conversation
agent resume

# Continue the previous session
agent --continue

# Resume specific conversation
agent --resume="chat-id-here"
```

#### Sandbox controls

Configure command execution settings with `/sandbox` or the `--sandbox <mode>` flag (`enabled` or `disabled`). Toggle sandbox mode on or off and control network access through an interactive menu. Settings persist across sessions.

[Media](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/uploads/sandox.mp4)

#### Sudo password prompting

Run commands requiring elevated privileges without leaving the CLI. When a command needs `sudo`, Cursor displays a secure, masked password prompt. Your password flows directly to `sudo` via a secure IPC channel; the AI model never sees it.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Installation

*Install Cursor CLI with a single command:*

**Source:** https://cursor.com/docs/cli/installation

#### Installation

##### macOS, Linux and Windows (WSL)

Install Cursor CLI with a single command:

```bash
curl https://cursor.com/install -fsS | bash
```

##### Windows (native)

Install Cursor CLI on Windows using PowerShell:

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

##### Verification

After installation, verify that Cursor CLI is working correctly:

```bash
agent --version
```

#### Post-installation setup

1. **Add \~/.local/bin to your PATH:**

   For bash:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   For zsh:

   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Start using Cursor Agent:**
   ```bash
   agent
   ```

#### Updates

Cursor CLI will try to auto-update by default to ensure you always have the latest version.

To manually update Cursor CLI to the latest version:

```bash
agent update
```


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Using Agent in CLI

*The CLI supports the same [modes](https://cursor.com/docs/agent/overview.md) as the editor. Switch modes using slash commands or the `--mode` flag.*

**Source:** https://cursor.com/docs/cli/using

#### Modes

The CLI supports the same [modes](https://cursor.com/docs/agent/overview.md) as the editor. Switch modes using slash commands or the `--mode` flag.

##### Plan mode

Use Plan mode to design your approach before coding. The agent asks clarifying questions to refine your plan.

- Press Shift+Tab to rotate to Plan mode
- Use `/plan` to switch to Plan mode
- Start with `--plan` or `--mode=plan` flag

##### Ask mode

Use Ask mode to explore code without making changes. The agent searches your codebase and provides answers without editing files.

- Use `/ask` to switch to Ask mode
- Start with `--mode=ask` flag

#### Prompting

Stating intent clearly is recommended for the best results. For example, you can use the prompt "do not write any code" to ensure that the agent won't edit any files. This is generally helpful when planning tasks before implementing them.

Agent has tools for file operations, searching, running shell commands, and web access.

#### MCP

Agent supports [MCP (Model Context Protocol)](https://cursor.com/marketplace) for extended functionality and integrations. The CLI will automatically detect and respect your `mcp.json` configuration file, enabling the same MCP servers and tools that you've configured for the editor.

#### ACP

Agent also supports [ACP (Agent Client Protocol)](https://cursor.com/docs/cli/acp.md) for custom client integrations. Use `agent acp` to run Cursor CLI as an ACP server over `stdio` with JSON-RPC messaging.

#### Rules

The CLI agent supports the same [rules system](https://cursor.com/docs/rules.md) as the editor. You can create rules in the `.cursor/rules` directory to provide context and guidance to the agent. These rules will be automatically loaded and applied based on their configuration, allowing you to customize the agent's behavior for different parts of your project or specific file types.

The CLI also reads `AGENTS.md` and `CLAUDE.md` at the project root (if
present) and applies them as rules alongside `.cursor/rules`.

#### Working with Agent

##### Navigation

Previous messages can be accessed using arrow up (ArrowUp) where you can cycle through them.

##### Input shortcuts

- Shift+Tab — Rotate between modes (Agent, Plan, Ask)
- Shift+Enter — Insert a newline instead of submitting, making it easier to write multi-line prompts.
- Ctrl+D — Exit the CLI. Follows standard shell behavior, requiring a double-press to exit.
- Ctrl+J or +Enter — Universal alternatives for inserting newlines that work in all terminals.

Shift+Enter works in iTerm2, Ghostty, Kitty, Warp, and Zed. For tmux users, use Ctrl+J instead. See [Terminal setup](https://cursor.com/docs/cli/reference/terminal-setup.md) for configuration options and troubleshooting.

##### Review

Review changes with Ctrl+R. Press i to add follow-up instructions. Use ArrowUp/ArrowDown to scroll, and ArrowLeft/ArrowRight to switch files.

##### Selecting context

Select files and folders to include in context with @. Free up space in the context window by running `/summarize`. `/compress` remains an alias.

#### Cloud Agent handoff

Push your conversation to a [Cloud Agent](https://cursor.com/docs/cloud-agent.md) and let it keep running while you're away. Prepend `&` to any message to send it to the cloud. Pick it back up on web or mobile at [cursor.com/agents](https://cursor.com/agents).

```bash
# Send a task to Cloud Agent mid-conversation
& refactor the auth module and add comprehensive tests
```

#### CLI worktrees

Pass `-w` or `--worktree [name]` to run the agent in a new Git worktree instead of editing your current checkout directly. Cursor creates these checkouts under `~/.cursor/worktrees/<reponame>/<name>`, alongside worktrees created from the editor. If you omit `name`, Cursor generates one.

Cursor cleans up CLI worktrees with the same retention rules it uses for editor worktrees. For cleanup settings and limits, see [How are old worktrees cleaned up?](https://cursor.com/docs/configuration/worktrees.md#how-are-old-worktrees-cleaned-up).

Combine `--workspace <path>` when you need an explicit repository root. Otherwise the CLI uses the current working directory. `--worktree` only changes where the agent makes file edits inside that project.

```bash
# Create a temporary worktree from the current repository with a generated name
agent --worktree "upgrade the test runner and fix any broken snapshots"

# Create a named worktree from another repository
agent --workspace ~/src/my-app --worktree auth-fix "fix the flaky auth test and open a PR"
```

#### History

Continue from an existing thread with `--resume [thread id]` to load prior context.

To resume the most recent conversation, use `agent resume`, `--continue`, or the `/resume` slash command.

You can also run `agent ls` to open previous chats and resume one.

#### Command approval

Before running terminal commands, CLI will ask you to approve (y) or reject (n) execution.

#### Non-interactive mode

Use `-p` or `--print` to run Agent in non-interactive mode. This will print the response to the console.

With non-interactive mode, you can invoke Agent in a non-interactive way. This allows you to integrate it in scripts, CI pipelines, etc.

You can combine this with `--output-format` to control how the output is formatted. For example, use `--output-format json` for structured output that's easier to parse in scripts, or `--output-format text` for plain text output of the agent's final response.

Cursor has full write access in non-interactive mode.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### CLI Changelog

*The latest features, improvements, and fixes shipping to Cursor CLI. Run `agent --version` to check your installed version, and `agent update` to upgrade in place.*

**Source:** https://cursor.com/docs/cli/changelog

The latest features, improvements, and fixes shipping to Cursor CLI. Run `agent --version` to check your installed version, and `agent update` to upgrade in place.

#### July 6, 2026 release

##### Models and skills

- **New installs start on Auto.** Fresh CLI installs default to Auto model routing. Existing choices are unchanged; switch anytime with `/model` or `--model`.
- **Switch models instantly from slash commands.** Type a shortcut like `/opus` or `/composer` to jump straight to a model, no picker needed; each family shortcut remembers your last choice. `/fast` toggles Fast when the current model supports it. Disable shortcuts under Model slash commands in `/config`.
- **Keep model-only skills out of slash commands.** Set `user-invocable: false` in a skill's `SKILL.md` frontmatter to hide it from `/` autocomplete and typed `/skill-name` resolution while keeping it available to the model.

##### Reliability

- **Fixed memory growth from per-turn cancellation state.** Long chats no longer accumulate abort listeners and controllers; each turn releases them when it finishes.
- **Quitting returns you to the shell promptly.** Exit no longer waits on MCP servers or other background tasks to wind down, and quitting from the workspace-trust prompt no longer flashes "Trusting workspace…".
- **Fixed config corruption when running several agents at once.** Concurrent CLI processes could interleave writes to `cli-config.json` and block later startups. Each write now stages to its own temp file before an atomic rename.

##### Sessions and subagents

- **Resume chats from any directory.** `agent ls`, `agent --resume`, and `/resume` open All chats across workspaces by default. Use Left/Right to switch to This workspace; chats from other directories show a folder label, and resuming one loads the full conversation instead of an empty one.
- **Subagents keep their context across resumes.** Completed subagents persist checkpoints, so resuming one restores its prior context instead of starting empty. Background subagents include their final message in the completion notification, and resuming an unavailable subagent fails clearly.

##### Login and MCP

- **Log in from another device with a QR code.** During `agent login` or first-run onboarding, press `q` to reveal a QR code for the same login URL, then scan it from a phone to finish authentication over SSH without copying a long link. Narrow terminals and non-interactive sessions continue to show the URL only.
- **Filter MCP servers and see login start immediately.** Type to filter the `/mcp` server list. Selecting Login shows "Preparing login…" right away, and SSH OAuth instructions no longer use `ssh -N`, which failed through some proxies.
- **Fixed MCP allowlist and approval bugs.** Team network allowlists now accept HTTP(S) origins with explicit ports, such as local servers on non-default ports. Personal MCP tool approvals work again when team admin tool controls are empty or unset.

##### Input and terminal

- **Long prompts stay within six visual lines.** The prompt bar and queued-message editor scroll to keep the cursor visible instead of growing without bound. Large pastes stay collapsed as a pill when recalled from history while the agent receives their full content, and Working appears immediately after you submit.
- **Fixed terminal state after Ctrl+Z.** Suspending the CLI restores your shell's keyboard modes until you `fg`. Backspace no longer swallows the letters typed right after it when the interface briefly stalls, and typing stays responsive while the agent streams output.
- **Fixed queued sudo prompts.** Each sudo request opens a fresh password prompt instead of sticking on "Authenticating…". Escape and Ctrl+C cancel during submission, and the mask uses `•` instead of `*` to avoid misalignment with terminal font ligatures.
- **Debug mode cards use debug mode colors.** The reproduction-steps decision card uses the red debug accent instead of plan-mode yellow, so the active mode stays clear.

#### June 29, 2026 release

##### Workspaces and commands

- **Start multi-root sessions from the command line.** Repeat `--add-dir <path>` to add directories at launch, including with `--workspace`. `/add-dir` refreshes slash skills and custom commands immediately; restart only when you want the agent to discover new skills automatically.
- **Plugin reloads refresh commands.** Reloading a plugin refreshes its slash commands and palette. Long skill and custom-command names resolve correctly, and `/add-dir` keeps directory completion open while you browse.
- **Queued follow-ups send on the second Enter.** Press Enter again on an empty prompt to stop the current turn and send your queued message immediately, including while a `beforeSubmitPrompt` hook is running.
- **Fixed input lag during agent runs.** Typing and queuing follow-ups no longer rerender the full transcript on every keystroke while output streams.
- **Fixed model options resetting.** Changing Fast, reasoning effort, or context in `/model` preserves your other compatible choices and keeps Max Mode in sync.

##### Cloud and Auto-review

- **Cloud transfers preserve model and workspace context.** For Git repositories with Cloud Agents access, transfers preserve the selected model and workspace path. The prompt shows transfer status, `Esc` or `Ctrl-C` cancels, and failure details remain visible.
- **Auto-review considers invoked instructions.** Admins can control availability. When Auto-review is enabled for your account and selected model, the classifier can inspect invoked skill and file-backed custom-command files before deciding whether a tool call needs approval. Existing hard approval boundaries are unchanged.

##### Authentication and MCP

- **Run Cursor in sandboxes without macOS Keychain.** Set `AGENT_CLI_CREDENTIAL_STORE=file` to store credentials unencrypted in an owner-only file. Use private storage that persists across runs; packaged Unix builds also skip system CA loading in this mode.
- **Fixed false MCP connection errors.** Working servers no longer appear disconnected in `/mcp` and `agent mcp list` when their tools or instructions are available.

##### Reliability and updates

- **Windows updates suppress PowerShell progress output.** Native updates no longer draw PowerShell's progress bar over the CLI or incur its download overhead.
- **Fixed memory growth in long CLI sessions.** The CLI now saves only new transcript entries at each checkpoint instead of reloading and rewriting the full conversation.

#### June 22, 2026

##### Auto-review

- **Auto-review run mode.** Cursor's Auto-review run mode comes to the CLI: a middle ground between Allowlist and Run Everything that keeps the agent moving with fewer approval prompts. Shell, MCP, and Fetch calls are checked in order: allowlisted calls run immediately, calls that can be sandboxed run in the sandbox, and the rest go to a classifier that allows the call, tries a different approach, or asks you to approve. Turn it on with `--auto-review`, in `/config`, or with `/auto-review`, and steer the classifier with `allow`/`block` instructions in `permissions.json`.

##### Workspaces

- **Named multi-directory workspaces.** Run the agent across several repositories at once: add directories mid-session with `/add-dir`, save the set with `/save-workspace`, reload it later with `/load-workspace`, or start scoped with `--workspace`.

##### Commands

- **`/rewind` is on by default.** The turn-by-turn undo timeline no longer needs turning on in `/config`.
- **`/vim` anywhere in the prompt.** Trigger inline Vim editing from any position, not just an empty prompt.
- **Richer `/copy`.** Pick a single step of a multi-step reply from a per-step picker, copy the agent's responses alongside your own messages, and copy long replies without the terminal stalling.
- **`/logs` on shared machines.** Debug logs are written per user so multi-user hosts don't hit permission errors, and the `/logs` path lingers on screen longer.

##### Terminal experience

- **Prompt history is per conversation.** Up-arrow recalls what you typed in this session instead of a single history shared across every chat.
- **The jobs list shows everything running.** Foreground shells and subagents appear in the jobs pager alongside background tasks.
- **Steadier rendering.** Mermaid diagrams stay drawn after a turn finishes, long shell-output previews clip instead of wrapping, and the screen clears once per resize instead of twice.
- **Your draft survives the resume picker.** Cancelling `/resume` keeps what you had already typed.
- **Plan editing.** Esc returns to Vim normal mode while you revise a plan.

##### Reliability

- **Lower memory in long sessions.** Fixed a leak where per-turn abort signals held on to conversation state.
- **No crash on missing approval state.** Sessions tolerate credential stores that haven't recorded an approval mode yet.

##### MCP and skills

- **Editor-provided MCP servers are trusted.** MCP servers passed in over the Agent Client Protocol (Zed and other editors) load instead of being silently dropped.
- **MCP tools survive a plugin reload.** The MCP lease refreshes after a plugin reloads, so its tools no longer wedge with "Not connected" errors.
- **Skills found through symlinks.** The skills menu follows symlinked directories when discovering skills.

##### Install and updates

- **Reliable channel switching.** Switching release channels applies on the first try and immediately fetches the target channel's build.
- **Windows and shim fixes.** The Windows launcher matches timestamped version directories, and the `cursor` shim no longer errors on shells that treat unset variables as failures.

##### Enterprise and team controls

- **Team gating for Auto-review.** Admins control whether Auto-review is available to their members.
- **Stable self-hosted worker identity.** `worker start` waits for the bridge to connect before reporting ready, and workers keep a stable logical ID scoped per authenticated user, so fleets on shared machines match the right worker to the right person.

#### June 9, 2026

##### Terminal experience

- **Cleaner edit display.** File edits render borderless (an `Editing`/`Edited` header plus the diff), with memoized diff rendering so large edits don't slow the UI.
- **Faster, richer resume picker.** Session metadata is cached so `/resume` (Ctrl+Y) opens quickly even on network filesystems, with Created and Last updated columns and reliable ordering.
- **Working status pinned above the prompt.** Progress, token counts (with an optional elapsed-time display), and hints stay in one stable place.
- **Long shell output truncates from the top.** You see the latest output of a streaming command, not the oldest.
- **Wrapped URLs stay clickable.** Long links re-emit hyperlink codes on every wrapped line.
- **Model picker shows Max Mode state**, and the footer model summary drops redundant labels.

##### Commands

- **`/fork`** Branch the current conversation into a copy and continue down a different path (aliases `/branch`, `/duplicate`).
- **`/update`** Update the CLI in place from inside the session.
- **`/context`** Visualize what's consuming the context window, broken down by category.
- **`/logs`** Debug logs are written for every session; `/logs` shows the path and copies it to the clipboard.
- **Background task controls.** Arrow-key navigation in the task viewer and a kill shortcut.

##### Reliability

- **HTTP/2 keepalive pings.** Silent connection stalls mid-stream are detected in seconds and retried.
- **Transport interruptions retry automatically.** Network-level cancels and aborts no longer end the turn as if Ctrl+C had been pressed.
- **Freeze fixes.** Eliminated hard UI freezes caused by layout feedback loops, an input freeze after first-run onboarding, and swallowed or reordered keystrokes while pasting.
- **Faster first paint on slow networks.** Team settings lookups no longer block interactive startup (about 2 seconds on high-latency connections).
- **Works on restricted networks.** Feature defaults apply when corporate firewalls block the configuration service.
- **direnv support.** The agent's shell loads `.envrc` automatically, in interactive and agent-dispatched shells.
- **Drag-and-drop and paste fixes.** File drag-and-drop paths arrive intact, and pasting a copied image file on macOS attaches the actual image.

##### Enterprise and team controls

- **Admins can disable headless mode.** A team setting blocks non-interactive CLI usage org-wide.
- **"Run Everything" controls.** Auto-run renamed consistently across the product; admin-controlled auto-run treats the command allowlist as the always-available baseline.
- **MCP user-extension governance.** Admin "Allow User Extension" toggles for MCP servers and tools are enforced at runtime.
- **Team-managed MCP servers.** Centrally configured servers load reliably, with server group selection; MCP tool policy is decoupled from the terminal auto-run setting.
- **MCP OAuth over SSH.** The CLI shows port-forwarding instructions when authenticating a remote MCP server from an SSH session.

#### May 20, 2026

- **Composer 2.5 is the default model** for new CLI sessions.
- **`/summarize`.** Renamed from `/compress` to match the IDE; `/compact` and `/compress` remain as aliases, and aliases execute directly.
- **Local plugins via `~/.cursor/settings.json`.** Point an `enabled_plugins` key at local plugin folders; no marketplace needed.
- **Multi-root workers.** Self-hosted workers span multiple repositories with repeatable `--worker-dir` flags and keep a stable identity.
- **Rewind preserves images.** Rewinding to an earlier turn restores that turn's image attachments to the prompt.
- **Faster `/plugins`.** Quicker plugin details, with each plugin's MCP servers linked into `/mcp` management.
- **MCP tools refresh in-session.** Logging in, enabling, or disabling a server from `/mcp` updates the agent's available tools immediately.
- **Readable diffs in light mode.** Character-level diff highlights are legible on light terminal themes.
- **Hooks accept payloads over stdin.** Avoids argv length limits and keeps payloads out of process listings.

#### May 14, 2026

- **Vim visual mode.** Visual selection with delete and change operators; the active Vim mode shows in the footer.
- **Ctrl+G opens your prompt in `$EDITOR`.** Compose long prompts in your real editor and drop the result back into the prompt bar.
- **MCP management revamped.** `/mcp` opens a per-server detail view: browse tool schemas, log in, log out (clears stored OAuth credentials), enable, and disable, all without leaving the session.
- **Headless runs wait for MCP tools.** Fixed a startup race where slow stdio MCP servers were missing from `-p` runs.
- **Nested rules and skills.** `.cursor/rules` and `.cursor/skills` in subdirectories are discovered everywhere, matching the IDE.
- **Long conversations redraw instantly.** Full repaints render only recent turns (`/full-conversation` to opt out), keeping resizes and resumes fast in old sessions.
- **Proxy support for agent streams.** `HTTPS_PROXY` is honored on the streaming connection, completing corporate proxy support end to end.
- **Auto-run survives resume.** Resuming a conversation recomputes Run Everything from your config and team policy.
- **Model variants work headless.** Fast or high-effort model slugs passed to `--model` keep their parameters in `-p` mode.
- **Early keystrokes are buffered** and replayed once the UI loads; stale input over SSH and tmux fixed.
- **tmux focus awareness.** The prompt cursor stops blinking in unfocused panes (with `focus-events on`).
- **Pathological diffs render safely.** Very long lines are capped before syntax highlighting, so minified files can't stall the UI.

#### May 7, 2026

- **Plugin marketplaces.** Add a marketplace by git URL (`/plugin marketplace add`), browse and manage marketplaces by scope, see which marketplace each plugin came from, and load local plugin dirs with `--plugin-dir`. Plugins imported from Claude Code appear alongside native ones.
- **Ctrl+L clears the screen** like a shell: clears screen and scrollback, keeps your session running.
- **Smooth typing from the first keystroke.** Fixed an event-loop stall (about 1 second on large repos) that batched early keystrokes; closing pagers no longer repaints the whole screen.
- **Skills everywhere.** Skills load in interactive, headless, and editor-integration modes; `/skill-name` invocations work in `-p` print mode.
- **Linux clipboard image paste.** Paste images on Wayland and X11.
- **`/model` typeahead.** Type `/model sonnet` and the picker opens pre-filtered, without submitting your prompt.
- **Theme follows your terminal.** Switching your terminal between light and dark repaints the CLI automatically.
- **Stall detection with persistent retries.** Stalled streams are detected and retried instead of hanging, and the backend can fall back to HTTP/1 transport on networks where HTTP/2 misbehaves.
- **`/mcp` grouped by scope.** Servers are organized under User / Project / Team, and failed servers show their actual error.
- **Privacy hardening.** Conversation summarization fails closed for no-storage teams.
- **Delegated worker tokens.** Team service accounts can mint short-lived user-scoped tokens so self-hosted workers run attributed to a specific team member.
- **Interrupting keeps partial results.** Stopping a turn preserves the output of in-flight shell commands, and follow-ups move running tools to the background instead of killing them.

#### April 2026

- **`/rewind`: undo agent turns.** An interactive timeline restores files and conversation state to any earlier turn, with per-turn file diffs, conversation-only restore, and `/undo`/`/restore` aliases (enable in `/config`).
- **Desktop notifications.** Get notified when a turn finishes or the agent is blocked on you (approvals, questions, sudo) across iTerm2, Ghostty, Warp, Kitty, and Terminal.app, with tmux/screen passthrough and focus-aware muting. Approval notifications include the pending command.
- **Interactive `/config`.** A full settings editor inside the CLI replaces hand-editing JSON, including a version and account page.
- **Custom status line.** Point `statusLine` at your own command and render its output (with live token usage data) in the prompt footer.
- **`/btw` side questions.** Ask a quick read-only question mid-turn; the answer streams into a dismissible overlay with full conversation context and never touches your conversation history.
- **Lighter startup.** MCP loading moved off the first-paint path, server config and model are cached between runs, the syntax-highlighting bundle shrank from 9.1 MB to 2.4 MB, and one-shot commands skip UI initialization entirely.
- **HTTP/2 connection pooling on by default.** Better throughput for parallel tool calls and subagents.
- **Vim find motions.** `f`/`F`/`t`/`T`/`;`/`,` with operator composition (`df,`, `ct.`).
- **Image paste shortcuts.** Ctrl+V pastes a clipboard image; pasting a copied image file resolves the actual image.
- **Markdown and diff rendering.** Tighter spacing, styled headings, git-style unified diffs with context lines, accurate new-file diffs, and a fix for gray-on-dark text that was invisible in many themes (including dark mode over SSH).
- **Context in the footer.** Working directory, git branch, and the open PR for your branch (as a clickable link) stay visible while you type.
- **`?` shortcut cheat sheet, `/copy`, `/rename`.** Discover input shortcuts, copy past messages, and name your sessions.
- **One question at a time.** Clarifying questions present individually with a freeform "Other" answer option.
- **Headless improvements.** `--format json` for `status`/`about`, plan mode works with `-p`, and errors are recorded in transcripts so scripts can detect failed runs.
- **Hooks fire reliably.** `afterAgentThought`/`afterAgentResponse` events emit in the CLI, and Claude Code-format hook responses are accepted.
- **Global MCP servers auto-approved.** Servers from `~/.cursor/mcp.json` load without per-workspace prompts (project-level servers still require approval), and MCP approval screens hide secrets in URLs.
- **Install plugins from a git URL.** Paste a repo URL into the plugin search to install directly.
- **Trust and approval hardening.** Worktrees inherit workspace trust, approval prompts can't be skipped by a stray Enter, and the CLI offers to persist "Run Everything" after repeated use.

#### March 2026

- **Subagents in the CLI.** Parallel agents execute locally with live status in interactive, headless, and editor sessions, inheriting your credentials, rules, and approval policy. Max mode and custom-key setups propagate to subagents.
- **Run Everything is its own toggle.** Auto-approval is controlled by `/auto-run` (and `--force`/`--yolo`) separately from the Shift+Tab mode cycle, and team-configured approval modes are respected in headless runs.
- **Plugins arrived.** Browse the marketplace and install or uninstall plugins at user or project scope from `/plugin`; plugin skills, slash commands, subagents, and MCP servers all load into the session.
- **Retries on by default.** Dropped and stalled streams retry automatically in all modes, and classified server errors (like rate limits) render with their real message.
- **`permissions.json` support.** The CLI reads the same terminal/MCP allowlist file as the IDE.
- **Corporate proxy support for auth.** Login and API-key validation route through `HTTPS_PROXY`, unblocking Zscaler-style networks.
- **Background tasks.** Double Ctrl+B sends a running shell to the background, headless runs wait for background work to finish (emitting events for `stream-json` consumers), and completion notifications render cleanly.
- **Self-hosted worker improvements.** No sudo required, fixed idle disconnects, automatic token refresh, a Prometheus metrics endpoint, Windows support, custom names, and proxy support.
- **Skills from other tools' directories.** Skills are also discovered in `.claude/skills`, `.agents/skills`, and `.codex/skills`.
- **Remote MCP OAuth fixes.** Strict OAuth servers (state/scopes) work with `/mcp login`, and `${VAR}` placeholders expand in MCP configs everywhere.
- **`--image` everywhere.** Attach images in any session, not just print mode.
- **Editor integrations.** Model and mode selection over the Agent Client Protocol (Zed, JetBrains), host-provided MCP servers respected, richer streaming with thinking and file locations, and skill slash commands.
- **Locked macOS keychain detected over SSH.** A clear "unlock your keychain" message replaces opaque credential failures.
- **Admin controls.** Network allow and deny lists are enforced unconditionally (including for MCP traffic), admin-disabled sandboxing is respected by auto-run, and image generation asks before running.
- **Claude Sonnet 4.6 on Bedrock.** Added to the bring-your-own-key model list.
- **Richer hook payloads.** Per-turn token usage and a stable session ID.

#### February 2026

- **Git worktrees.** `--worktree`/`-w` runs the agent in an isolated worktree (with `--worktree-base` for the base branch), keeping agent changes off your checkout; the sandbox fully understands worktree layouts.
- **Headless hang fixed.** `-p` runs no longer block when spawned with an open stdin pipe (Node, Python, CI runners), and connection failover on partially unreachable networks dropped from about 20 seconds to 8.
- **`--yolo`.** Fully autonomous runs that auto-approve consistently across trust, MCP, and command approvals.
- **AWS Bedrock with your own credentials.** `agent bedrock` configures access keys or a team IAM role; works across interactive, headless, and editor sessions.
- **Automatic reconnection.** Transport errors retry with a visible "Reconnecting…" indicator.
- **Review UI.** Unified `/changes` (Ctrl+R) with a Session tab showing only this session's edits, `o`/`O` to open diffs in your editor, and a zen toggle while reviewing.
- **Token usage for scripts.** Per-turn input/output/cache token totals and a `request_id` in `stream-json` output; headless transcripts write Claude Code-compatible JSONL.
- **Repeatable `-H/--header`.** Pass multiple headers curl-style.
- **Sandbox policy files.** `~/.cursor/sandbox.json` and `.cursor/sandbox.json` are honored (including over SSH), network access has clear modes, and the CLI fails fast with a clear reason when sandboxing is enabled but unavailable.
- **Plan mode improvements.** A persistent plan menu with Build Locally / Build in Cloud, and plan content transfers correctly to cloud agents.
- **Faster startup, snappier turns.** Parallelized initialization, deferred update checks, and optimistic message rendering.
- **Rendering improvements.** Markdown tables wrap to your terminal width, thinking blocks render markdown, shell commands get syntax highlighting, and Mermaid renders more diagram types.
- **Input fixes across terminals.** Vim `r` (replace char), Alt+Delete word deletion, Ctrl+J newline in iTerm2, Windows Delete key, Wayland clipboard support, and session-local prompt history.
- **Enterprise attribution control.** Admin-disabled commit/PR attribution is enforced in the CLI regardless of local settings.
- **Clear errors for blocked screenshots.** macOS permission failures show a warning and workaround instead of failing silently.

#### January 2026

- **Hooks.** Session start/end, stop hooks with follow-up loops (autonomous "keep going" patterns), pre-compaction, and subagent lifecycle hooks; Claude Code `settings.json` hooks are read and merged; admins can push team-managed hooks with enterprise > team > project > user precedence.
- **Permissions and sandboxing aligned with the IDE.** A three-mode model (Run Everything / Auto-Run in Sandbox / Ask Every Time), an interactive `/sandbox` menu, a default-deny network proxy for sandboxed commands, and team-admin network allowlists enforced in the CLI.
- **`sudo` works.** Commands needing sudo trigger a masked password prompt delivered over a locked-down local socket; the model never sees your password.
- **Plan and Ask modes.** `--mode plan|ask` startup flags, `/plan <prompt>`, Shift+Tab mode cycling, and native UIs for questions, mode switches, and plan review, with plans saved to disk.
- **Responsive typing while streaming.** Buffered input with deferred rendering of streaming output, and queued follow-ups submit instantly.
- **Hand off to Cloud Agents.** Type `&` to transfer the live conversation to a cloud agent and keep working.
- **`--continue`.** Resume your most recent chat without looking up an ID; transcripts persist to disk for tooling and hooks.
- **Headless trust enforcement.** Non-interactive runs in untrusted workspaces fail with guidance unless `--trust` (or `--force`) is passed.
- **MCP management.** `/mcp list` is an interactive pager with status, login, enable, and tool browsing; OAuth login fixed; project config correctly overrides user config; tool-level allowlisting from the approval prompt.
- **Skills, rules, and commands in the CLI.** `/skills` browsing and inline `/skill-name` invocation, curated built-in skills, and interactive `/rules` and `/commands` browsers with inline editing.
- **`/model` autocomplete and Max Mode.** Fuzzy model search with friendly names, plus `/max-mode` with a footer indicator that persists across sessions.
- **Markdown rendering.** Aligned tables, clickable links, horizontal rules, and word-level inline diffs in file reviews.
- **Subagent UI.** Live rendering for parallel subagents with per-agent status, streamed activity, and token counts.
- **Editor integration groundwork.** Session resume, real agent modes, granular tool rendering, and custom slash commands over the Agent Client Protocol (Zed and others).
- **Windows reliability.** Works under restricted PowerShell execution policies, detects Git Bash, fixes browser-based login; clipboard support landed on Windows and Linux.
- **Auth and updates.** Expired tokens prompt re-login instead of crashing, transient server errors no longer log you out, parallel auto-updates can't corrupt an install, and `--disable-auto-update` turns background updates off.
- **Faster startup.** Compile caching and lazy initialization cut warm boot time about 10%.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Shell Mode

*Shell Mode runs shell commands directly from the CLI without leaving your conversation. Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.*

**Source:** https://cursor.com/docs/cli/shell-mode

Shell Mode runs shell commands directly from the CLI without leaving your conversation. Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.

[Media](https://cursor.com/docs-static/images/cli/shell-mode/cli-shell-mode.mp4)

#### Command execution

Commands run in your login shell (`$SHELL`) with the CLI's working directory and environment. Chain commands to run in other directories:

```bash
cd subdir && npm test
```

#### Output

Large outputs are truncated automatically and long-running processes timeout to maintain performance.

#### Limitations

- Commands timeout after 30 seconds
- Long-running processes, servers, and interactive prompts are not supported
- Use short, non-interactive commands for best results

#### Permissions

Commands are checked against your permissions and team settings before execution. See [Permissions](https://cursor.com/docs/cli/reference/permissions.md) for detailed configuration.

Admin policies may block certain commands, and commands with redirection cannot be allowlisted inline.

#### Usage guidelines

Shell Mode works well for status checks, quick builds, file operations, and environment inspection.

Avoid long-running servers, interactive applications, and commands requiring input.

Each command runs independently - use `cd <dir> && ...` to run commands in other directories.

#### Troubleshooting

- If a command hangs, cancel with Ctrl+C and add non-interactive flags
- When prompted for permissions, approve once or add to allowlist with Tab
- For truncated output, use Ctrl+O to expand
- To run in different directories, use `cd <dir> && ...` since changes don't persist
- Shell Mode supports zsh and bash from your `$SHELL` variable

#### FAQ

##### Does \`cd\` persist across runs?

No. Each command runs independently. Use `cd <dir> && ...` to run commands in different directories.

##### Can I change the timeout?

No. Commands are limited to 30 seconds and this is not configurable.

##### Where are permissions configured?

Permissions are managed by CLI and team configuration. Use the decision banner to add commands to allowlists.

##### How do I exit Shell Mode?

Press Escape when the input is empty, Backspace/Delete on empty input, or Ctrl+C to clear and exit.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### ACP

*Cursor CLI supports **ACP (Agent Client Protocol)** for advanced integrations. You can run `agent acp` and connect a custom client over `stdio` using JSON-RPC.*

**Source:** https://cursor.com/docs/cli/acp

#### Overview

Cursor CLI supports **ACP (Agent Client Protocol)** for advanced integrations. You can run `agent acp` and connect a custom client over `stdio` using JSON-RPC.

Learn more in the official [Agent Client Protocol docs](https://agentclientprotocol.com/).

ACP is intended for building custom clients and integrations. For normal terminal
workflows, use the interactive CLI with `agent`.

#### Start ACP server

Start Cursor CLI in ACP mode:

```bash
agent acp
```

#### Transport and message format

- Transport: `stdio`
- Protocol envelope: JSON-RPC 2.0
- Framing: newline-delimited JSON (one message per line)
- Direction:
  - Client writes requests/notifications to `stdin`
  - Cursor CLI writes responses/notifications to `stdout`
  - Logs may be written to `stderr`

#### Request flow

Typical ACP session flow:

1. `initialize`
2. `authenticate` with `methodId: "cursor_login"`
3. `session/new` (or `session/load`)
4. `session/prompt`
5. Handle `session/update` notifications while the model streams output
6. Handle `session/request_permission` by returning a decision
7. Optionally send `session/cancel`

#### Authentication

Cursor CLI advertises `cursor_login` as the ACP auth method. In practice, you can pre-authenticate before startup using existing CLI auth paths:

- `agent login`
- `--api-key` (or `CURSOR_API_KEY`)
- `--auth-token` (or `CURSOR_AUTH_TOKEN`)

You can also pass endpoint and TLS options from the root CLI command:

```bash
agent --api-key "$CURSOR_API_KEY" acp
agent -e https://api2.cursor.sh acp
agent -k acp
```

#### Sessions, modes, and permissions

##### Sessions

- Create a session with `session/new`
- Resume an existing conversation with `session/load`

##### Modes

ACP sessions support the same core modes as CLI:

- `agent` (full tool access)
- `plan` (planning, read-only behavior)
- `ask` (Q\&A/read-only behavior)

##### Permissions

When tools need approval, Cursor sends `session/request_permission`. Clients should return one of:

- `allow-once`
- `allow-always`
- `reject-once`

If your client does not answer permission requests, tool execution can block.

#### MCP servers

ACP supports [MCP servers](https://cursor.com/docs/mcp.md) defined in a project-level or user-level `.cursor/mcp.json`. Launch `agent` from your project directory and approve the servers you want to use.

Team-level MCP servers configured through the Cursor dashboard are not supported in ACP mode.

#### Cursor extension methods

Cursor sends ACP extension methods for richer client UX. There are two types:

- **Blocking methods** (`cursor/ask_question`, `cursor/create_plan`): The agent waits for a response before continuing. Your client must reply with a JSON-RPC response.
- **Notification methods** (`cursor/update_todos`, `cursor/task`, `cursor/generate_image`): The agent sends these as fire-and-forget notifications. Your client can display them but doesn't need to respond.

| Method                  | Type         | Use                                          |
| :---------------------- | :----------- | :------------------------------------------- |
| `cursor/ask_question`   | Blocking     | Ask users multiple-choice questions          |
| `cursor/create_plan`    | Blocking     | Request explicit plan approval               |
| `cursor/update_todos`   | Notification | Notify client about todo state updates       |
| `cursor/task`           | Notification | Notify client about subagent task completion |
| `cursor/generate_image` | Notification | Notify client about generated image output   |

##### `cursor/ask_question`

Present multiple-choice questions to the user. The agent blocks until the client responds.

**Request:**

```ts
interface CursorAskQuestionRequest {
  toolCallId: string;
  title?: string;
  questions: Array<{
    id: string;
    prompt: string;
    options: Array<{ id: string; label: string }>;
    allowMultiple?: boolean;
  }>;
}
```

**Response:**

```ts
interface CursorAskQuestionResponse {
  outcome:
    | {
        outcome: "answered";
        answers: Array<{
          questionId: string;
          selectedOptionIds: string[];
        }>;
      }
    | { outcome: "skipped"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example request:**

```json
{
  "toolCallId": "call_123",
  "title": "Need input",
  "questions": [
    {
      "id": "q1",
      "prompt": "Which mode should I use?",
      "options": [
        { "id": "agent", "label": "Agent" },
        { "id": "plan", "label": "Plan" }
      ],
      "allowMultiple": false
    }
  ]
}
```

##### `cursor/create_plan`

Request plan approval from the user. The agent blocks until the client accepts or rejects the plan.

**Request:**

```ts
interface CursorCreatePlanRequest {
  toolCallId: string;
  name?: string;
  overview?: string;
  plan: string;
  todos: Array<{
    id: string;
    content: string;
    status: "pending" | "in_progress" | "completed" | "cancelled";
  }>;
  isProject?: boolean;
  phases?: Array<{
    name: string;
    todos: Array<{
      id: string;
      content: string;
      status: "pending" | "in_progress" | "completed" | "cancelled";
    }>;
  }>;
}
```

- `plan`: A markdown string describing the full plan.
- `phases`: Optional grouping of todos into named phases for larger plans.

**Response:**

```ts
interface CursorCreatePlanResponse {
  outcome:
    | { outcome: "accepted"; planUri?: string }
    | { outcome: "rejected"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example request:**

```json
{
  "toolCallId": "call_124",
  "name": "Refactor tabs layout",
  "overview": "Tighten layout behavior and preserve existing UX.",
  "plan": "1. Inspect current tab sizing logic.\n2. Update layout calculations.\n3. Verify editor behavior.",
  "todos": [
    { "id": "todo-1", "content": "Inspect current tab sizing logic", "status": "completed" },
    { "id": "todo-2", "content": "Update layout calculations", "status": "in_progress" },
    { "id": "todo-3", "content": "Verify editor behavior", "status": "pending" }
  ],
  "isProject": false
}
```

##### `cursor/update_todos`

Update the client's todo list. Sent as a notification; no response required.

**Request:**

```ts
interface CursorUpdateTodosRequest {
  toolCallId: string;
  todos: Array<{
    id: string;
    content: string;
    status: "pending" | "in_progress" | "completed" | "cancelled";
  }>;
  merge: boolean;
}
```

- `merge`: When `true`, merge these todos into the existing list. When `false`, replace the entire list.

**Response:**

```ts
interface CursorUpdateTodosResponse {
  outcome:
    | {
        outcome: "accepted";
        todos: Array<{
          id: string;
          content: string;
          status: "pending" | "in_progress" | "completed" | "cancelled";
        }>;
      }
    | { outcome: "rejected"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example request:**

```json
{
  "toolCallId": "call_125",
  "todos": [
    { "id": "1", "content": "Set up project structure", "status": "completed" },
    { "id": "2", "content": "Add authentication", "status": "in_progress" },
    { "id": "3", "content": "Write unit tests", "status": "pending" }
  ],
  "merge": true
}
```

##### `cursor/task`

Notify the client about a subagent task. Sent as a notification; no response required.

**Request:**

```ts
interface CursorTaskRequest {
  toolCallId: string;
  description: string;
  prompt: string;
  subagentType:
    | "unspecified"
    | "computer_use"
    | "explore"
    | "video_review"
    | "browser_use"
    | "shell"
    | "vm_setup_helper"
    | { custom: string };
  model?: string;
  agentId?: string;
  durationMs?: number;
}
```

- `subagentType`: The type of subagent to run. Use `{ custom: "your_type" }` for custom subagent types.
- `agentId`: Set this to resume a previously created subagent.
- `durationMs`: How long the task ran, included in the response.

**Response:**

```ts
interface CursorTaskResponse {
  outcome:
    | { outcome: "completed"; agentId?: string; durationMs?: number }
    | { outcome: "rejected"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example request:**

```json
{
  "toolCallId": "call_126",
  "description": "Explore codebase",
  "prompt": "Find where authentication is handled and report the file paths.",
  "subagentType": "explore"
}
```

##### `cursor/generate_image`

Notify the client about a generated image. Sent as a notification; no response required.

**Request:**

```ts
interface CursorGenerateImageRequest {
  toolCallId: string;
  description: string;
  filePath?: string;
  referenceImagePaths?: string[];
}
```

- `filePath`: Suggested file path for the generated image.
- `referenceImagePaths`: Paths to reference images used as input.

**Response:**

```ts
interface CursorGenerateImageResponse {
  outcome:
    | { outcome: "generated"; filePath: string; imageData?: string }
    | { outcome: "rejected"; reason?: string }
    | { outcome: "cancelled" };
}
```

**Example request:**

```json
{
  "toolCallId": "call_127",
  "description": "Minimal flat app icon for a note-taking app",
  "filePath": "/tmp/icon.png",
  "referenceImagePaths": ["/tmp/reference.png"]
}
```

#### Minimal Node.js client

This example shows the minimum control flow for a custom ACP client:

```js
import { spawn } from "node:child_process";
import readline from "node:readline";

const agent = spawn("agent", ["acp"], { stdio: ["pipe", "pipe", "inherit"] });

let nextId = 1;
const pending = new Map();

function send(method, params) {
  const id = nextId++;
  agent.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n");
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

function respond(id, result) {
  agent.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, result }) + "\n");
}

const rl = readline.createInterface({ input: agent.stdout });
rl.on("line", line => {
  const msg = JSON.parse(line);

  if (msg.id && (msg.result || msg.error)) {
    const waiter = pending.get(msg.id);
    if (!waiter) return;
    pending.delete(msg.id);
    msg.error ? waiter.reject(msg.error) : waiter.resolve(msg.result);
    return;
  }

  if (msg.method === "session/update") {
    const update = msg.params?.update;
    if (update?.sessionUpdate === "agent_message_chunk" && update.content?.text) {
      process.stdout.write(update.content.text);
    }
    return;
  }

  if (msg.method === "session/request_permission") {
    respond(msg.id, { outcome: { outcome: "selected", optionId: "allow-once" } });
  }
});

const init = async () => {
  await send("initialize", {
    protocolVersion: 1,
    clientCapabilities: { fs: { readTextFile: false, writeTextFile: false }, terminal: false },
    clientInfo: { name: "acp-minimal-client", version: "0.1.0" }
  });

  await send("authenticate", { methodId: "cursor_login" });
  const { sessionId } = await send("session/new", { cwd: process.cwd(), mcpServers: [] });
  const result = await send("session/prompt", {
    sessionId,
    prompt: [{ type: "text", text: "Say hello in one sentence." }]
  });

  console.log(`\n\n[stopReason=${result.stopReason}]`);
};

init().finally(() => {
  agent.stdin.end();
  agent.kill();
});
```

#### IDE integrations

ACP enables Cursor's AI agent to work with editors beyond the Cursor desktop app. Build or use third-party integrations for your preferred development environment.

##### Example use cases

- **JetBrains IDEs** — Connect IntelliJ IDEA, WebStorm, PyCharm, or other JetBrains IDEs to Cursor's agent. See the [JetBrains integration guide](https://cursor.com/docs/integrations/jetbrains.md) for setup instructions.

- **Neovim (avante.nvim)** — Use [avante.nvim](https://github.com/yetone/avante.nvim) to connect Neovim to Cursor's agent through ACP. See [Neovim setup](https://cursor.com/docs/cli/acp.md#neovim-avantenvim) below.

- **Zed** — Integrate with Zed's modern editor by spawning `agent acp` and communicating over stdio. Zed extensions can implement the ACP client protocol to route AI requests to Cursor.

- **Custom editors** — Any editor with extension support can implement an ACP client. Spawn the agent process, send JSON-RPC messages over stdio, and handle responses in your editor's UI.

##### Neovim (avante.nvim)

[avante.nvim](https://github.com/yetone/avante.nvim) is a Neovim plugin that provides an AI-powered coding assistant. It supports ACP, so you can connect it to Cursor's agent for agentic coding inside Neovim.

Add the following to your lazy.nvim plugin configuration (e.g., `~/.config/nvim/lua/plugins/avante.lua`):

```lua
return {
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    version = false,
    build = "make",
    opts = {
      provider = "cursor",
      mode = "agentic",
      acp_providers = {
        cursor = {
          command = os.getenv("HOME") .. "/.local/bin/agent",
          args = { "acp" },
          auth_method = "cursor_login",
          env = {
            HOME = os.getenv("HOME"),
            PATH = os.getenv("PATH"),
          },
        },
      },
    },
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
      {
        "MeanderingProgrammer/render-markdown.nvim",
        opts = {
          file_types = { "markdown", "Avante" },
        },
        ft = { "markdown", "Avante" },
      },
    },
  },
}
```

Key settings:

- **`provider`**: Set to `"cursor"` to route requests through Cursor's agent.
- **`mode`**: Set to `"agentic"` for full tool access (file edits, terminal commands). Use `"normal"` for chat-only mode.
- **`command`**: Points to the `agent` binary. The default install path is `~/.local/bin/agent`. Adjust if you installed it elsewhere.
- **`auth_method`**: Uses `"cursor_login"`. Run `agent login` in your terminal first to authenticate.

##### Building an integration

1. Spawn `agent acp` as a child process
2. Communicate over stdin/stdout using JSON-RPC
3. Handle `session/update` notifications to display streaming responses
4. Respond to `session/request_permission` when tools need approval
5. Optionally implement Cursor extension methods for richer UX

See the [minimal Node.js client](https://cursor.com/docs/cli/acp.md#minimal-nodejs-client) above for a working reference implementation.

#### Related

##### MCP in CLI

Manage and use MCP servers from Cursor CLI

##### MCP Overview

Learn MCP transports, configuration, and server setup


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Using Headless CLI

*Use Cursor CLI in scripts and automation workflows for code analysis, generation, and refactoring tasks.*

**Source:** https://cursor.com/docs/cli/headless

Use Cursor CLI in scripts and automation workflows for code analysis, generation, and refactoring tasks.

#### How it works

Use [print mode](https://cursor.com/docs/cli/using.md#non-interactive-mode) (`-p, --print`) for non-interactive scripting and automation.

##### File modification in scripts

Combine `--print` with `--force` (or `--yolo`) to modify files in scripts:

```bash
# Enable file modifications in print mode
agent -p --force "Refactor this code to use modern ES6+ syntax"

# Without --force, changes are only proposed, not applied
agent -p "Add JSDoc comments to this file"  # Won't modify files

# Batch processing with actual file changes
find src/ -name "*.js" | while read file; do
  agent -p --force "Add comprehensive JSDoc comments to $file"
done
```

The `--force` flag allows the agent to make direct file changes without
confirmation

#### Setup

See [Installation](https://cursor.com/docs/cli/installation.md) and [Authentication](https://cursor.com/docs/cli/reference/authentication.md) for complete setup details.

```bash
# Install Cursor CLI (macOS, Linux, WSL)
curl https://cursor.com/install -fsS | bash

# Install Cursor CLI (Windows PowerShell)
irm 'https://cursor.com/install?win32=true' | iex

# Set API key for scripts
export CURSOR_API_KEY=your_api_key_here
agent -p "Analyze this code"
```

#### Example scripts

Use different output formats for different script needs. See [Output format](https://cursor.com/docs/cli/reference/output-format.md) for details.

##### Searching the codebase

By default, `--print` uses `text` format for clean, final-answer-only responses:

```bash
#!/bin/bash
# Simple codebase question - uses text format by default

agent -p "What does this codebase do?"
```

##### Automated code review

Use `--output-format json` for structured analysis:

```bash
#!/bin/bash
# simple-code-review.sh - Basic code review script

echo "Starting code review..."

# Review recent changes
agent -p --force --output-format text \
  "Review the recent code changes and provide feedback on:
  - Code quality and readability
  - Potential bugs or issues
  - Security considerations
  - Best practices compliance

  Provide specific suggestions for improvement and write to review.txt"

if [ $? -eq 0 ]; then
  echo "✅ Code review completed successfully"
else
  echo "❌ Code review failed"
  exit 1
fi
```

##### Real-time progress tracking

Use `--output-format stream-json` for message-level progress tracking, or add `--stream-partial-output` for incremental streaming of deltas:

```bash
#!/bin/bash
# stream-progress.sh - Track progress in real-time

echo "🚀 Starting stream processing..."

# Track progress in real-time
accumulated_text=""
tool_count=0
start_time=$(date +%s)

agent -p --force --output-format stream-json --stream-partial-output \
  "Analyze this project structure and create a summary report in analysis.txt" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Using model: $model"
        fi
        ;;
        
      "assistant")
        # Only process streaming deltas (timestamp_ms present, no model_call_id).
        # Skip buffered flushes before tool calls and at end of turn.
        has_ts=$(echo "$line" | jq 'has("timestamp_ms")')
        has_mc=$(echo "$line" | jq 'has("model_call_id")')
        if [ "$has_ts" = "true" ] && [ "$has_mc" = "false" ]; then
          content=$(echo "$line" | jq -r '.message.content[0].text // empty')
          accumulated_text="$accumulated_text$content"
          printf "\r📝 Generating: %d chars" ${#accumulated_text}
        fi
        ;;

      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))

          # Extract tool information
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 Tool #$tool_count: Creating $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 Tool #$tool_count: Reading $path"
          fi

        elif [ "$subtype" = "completed" ]; then
          # Extract and show tool results
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ Created $lines lines ($size bytes)"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ Read $lines lines"
          fi
        fi
        ;;

      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))

        echo -e "\n\n🎯 Completed in ${duration}ms (${total_time}s total)"
        echo "📊 Final stats: $tool_count tools, ${#accumulated_text} chars generated"
        ;;
    esac
  done
```

#### Working with images

To send images, media files, or other binary data to the agent, include file paths in your prompts. The agent can read any files through tool calling, including images, videos, and other formats.

##### Including file paths in prompts

Simply reference file paths in your prompt text. The agent will automatically read the files when needed:

```bash
# Analyze an image
agent -p "Analyze this image and describe what you see: ./screenshot.png"

# Process multiple media files
agent -p "Compare these two images and identify differences: ./before.png ./after.png"

# Combine file paths with text instructions
agent -p "Review the code in src/app.ts and the design mockup in designs/homepage.png. Suggest improvements to match the design."
```

##### How it works

When you include file paths in your prompt:

1. The agent receives your prompt with the file path references
2. The agent uses tool calling to read the files automatically
3. Images are handled transparently
4. You can reference files using relative or absolute paths

##### Example: Image analysis script

```bash
#!/bin/bash
# analyze-image.sh - Analyze images using the headless CLI

IMAGE_PATH="./screenshots/ui-mockup.png"

agent -p --output-format json \
  "Analyze this image and provide a detailed description: $IMAGE_PATH" | \
  jq -r '.result'
```

##### Example: Batch media processing

```bash
#!/bin/bash
# process-media.sh - Process multiple media files

for image in images/*.png; do
  echo "Processing $image..."
  agent -p --output-format text \
    "Describe what's in this image: $image" > "${image%.png}.description.txt"
done
```

File paths can be relative to the current working directory or absolute paths.
The agent will read files through tool calls, so ensure the files exist and
are accessible from where you run the command.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Slash commands

*| Command                                | Description                                                                                                            |*

**Source:** https://cursor.com/docs/cli/reference/slash-commands

| Command                                | Description                                                                                                            |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `/model [filter]`                      | Select a model. Press `Tab` to edit.                                                                                   |
| `/run-everything [on\|off\|status]`    | Toggle Run Everything or show its status. `/auto-run` is an alias.                                                     |
| `/plan [prompt]`                       | Switch to Plan mode, show the current plan, or submit a prompt in Plan mode                                            |
| `/ask`                                 | Toggle Ask mode for read-only questions                                                                                |
| `/debug [prompt]`                      | Toggle Debug mode or submit a prompt in Debug mode                                                                     |
| `/logs`                                | Show the debug log path and copy it to the clipboard                                                                   |
| `/update`                              | Update Cursor Agent to the latest version                                                                              |
| `/max-mode`                            | Toggle Max Mode on legacy request-based plans                                                                          |
| `/rename <name>`                       | Rename the current chat session                                                                                        |
| `/clear`                               | Start a new chat session. `/new`, `/new-chat`, and `/newchat` are aliases.                                             |
| `/resume`                              | Open recent chats and resume one                                                                                       |
| `/fork`                                | Fork the current chat into a new session                                                                               |
| `/summarize`                           | Summarize the conversation to reduce context. `/compress` is an alias.                                                 |
| `/rewind`                              | Jump back to a previous message                                                                                        |
| `/vim`                                 | Toggle Vim keys                                                                                                        |
| `/line-numbers`                        | Toggle line numbers in code blocks                                                                                     |
| `/show-thinking`                       | Toggle thinking block display                                                                                          |
| `/status-indicators`                   | Toggle terminal title status indicators                                                                                |
| `/shell [command]`                     | Enter Shell Mode. `/sh` and `/run` are aliases.                                                                        |
| `/about`                               | Show CLI version, system, and account info. Also copies it to the clipboard.                                           |
| `/setup-terminal`                      | Configure terminal newline keybindings. See [Terminal setup](https://cursor.com/docs/cli/reference/terminal-setup.md). |
| `/help [command]`                      | Show help. Use `/help <command>` for command details.                                                                  |
| `/feedback <message>`                  | Share feedback with the team                                                                                           |
| `/open`                                | Open the repository's Git root in Cursor. `/cursor` is an alias.                                                       |
| `/copy-request-id`                     | Copy the last request ID to the clipboard                                                                              |
| `/copy-conversation-id`                | Copy the current conversation ID to the clipboard                                                                      |
| `/logout`                              | Sign out from Cursor                                                                                                   |
| `/quit`                                | Exit                                                                                                                   |
| `/exit`                                | Exit                                                                                                                   |
| `/mcp [list\|list-tools] [identifier]` | Manage MCP servers and list tools for a server                                                                         |
| `/plugin [subcommand]`                 | Manage plugins and marketplaces                                                                                        |
| `/config`                              | Configure CLI settings interactively                                                                                   |
| `/copy`                                | Copy a previous user message to the clipboard                                                                          |
| `/sandbox`                             | Configure sandbox mode and network access settings                                                                     |
| `/bedrock [subcommand]`                | Configure Bedrock when the Bedrock feature is enabled                                                                  |


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Parameters

*Global options can be used with any command:*

**Source:** https://cursor.com/docs/cli/reference/parameters

#### Global options

Global options can be used with any command:

| Option                     | Description                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `-v, --version`            | Output the version number                                                                                            |
| `--api-key <key>`          | API key for authentication (can also use `CURSOR_API_KEY` env var)                                                   |
| `-H, --header <header>`    | Add custom header to agent requests (format: `Name: Value`, can be used multiple times)                              |
| `-p, --print`              | Print responses to console (for scripts or non-interactive use). Has access to all tools, including write and shell. |
| `--output-format <format>` | Output format (only works with `--print`): `text`, `json`, or `stream-json` (default: `text`)                        |
| `--stream-partial-output`  | Stream partial output as individual text deltas (only works with `--print` and `stream-json` format)                 |
| `--resume [chatId]`        | Resume a chat session                                                                                                |
| `--continue`               | Continue the previous session (alias for `--resume=-1`)                                                              |
| `--model <model>`          | Model to use                                                                                                         |
| `--mode <mode>`            | Set agent mode: `plan` or `ask` (agent is the default when no mode is specified)                                     |
| `--plan`                   | Start in plan mode (shorthand for `--mode=plan`)                                                                     |
| `--list-models`            | List all available models                                                                                            |
| `-f, --force`              | Force allow commands unless explicitly denied                                                                        |
| `--yolo`                   | Alias for `--force`                                                                                                  |
| `--sandbox <mode>`         | Set sandbox mode: `enabled` or `disabled`                                                                            |
| `--approve-mcps`           | Automatically approve all MCP servers                                                                                |
| `--trust`                  | Trust the workspace without prompting (headless mode only)                                                           |
| `--workspace <path>`       | Workspace directory to use                                                                                           |
| `--plugin-dir <path>`      | Load a local plugin directory (can be specified multiple times)                                                      |
| `-w, --worktree [name]`    | Run in a new Git worktree under `~/.cursor/worktrees/<reponame>/<name>`. If omitted, a name is generated.            |
| `--worktree-base <branch>` | Branch or ref to base the new worktree on (default: current HEAD)                                                    |
| `--skip-worktree-setup`    | Skip running worktree setup scripts from `.cursor/worktrees.json`                                                    |
| `-h, --help`               | Display help for command                                                                                             |

#### Commands

| Command                       | Description                                                       | Usage                               |
| ----------------------------- | ----------------------------------------------------------------- | ----------------------------------- |
| `agent [prompt...]`           | Start in agent mode (the default)                                 | `agent agent "fix the tests"`       |
| `login`                       | Authenticate with Cursor                                          | `agent login`                       |
| `logout`                      | Sign out and clear stored authentication                          | `agent logout`                      |
| `status` \| `whoami`          | View authentication status                                        | `agent status`                      |
| `about`                       | Display version, system, and account info                         | `agent about`                       |
| `models`                      | List available models for this account                            | `agent models`                      |
| `mcp`                         | Manage MCP servers                                                | `agent mcp`                         |
| `sandbox`                     | Configure sandbox mode or run one command in a sandbox (hidden)   | `agent sandbox enable`              |
| `worker`                      | Start a private cloud worker that runs agents in your environment | `agent worker start`                |
| `acp`                         | Start ACP server mode (advanced, hidden command)                  | `agent acp`                         |
| `update`                      | Update Cursor Agent to the latest version                         | `agent update`                      |
| `ls`                          | Resume a chat session                                             | `agent ls`                          |
| `resume`                      | Resume the latest chat session                                    | `agent resume`                      |
| `create-chat`                 | Create a new empty chat and return its ID                         | `agent create-chat`                 |
| `generate-rule` \| `rule`     | Generate a new Cursor rule with interactive prompts               | `agent generate-rule`               |
| `install-shell-integration`   | Install shell integration to `~/.zshrc`                           | `agent install-shell-integration`   |
| `uninstall-shell-integration` | Remove shell integration from `~/.zshrc`                          | `agent uninstall-shell-integration` |
| `help [command]`              | Display help for command                                          | `agent help [command]`              |

`agent acp` is intended for custom ACP clients and advanced integrations. It is
hidden from default command help output.

When no command is specified, Cursor Agent starts in interactive agent mode by
default.

#### MCP

Manage MCP servers configured for Cursor Agent.

| Subcommand                | Description                                                                              | Usage                               |
| ------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- |
| `login <identifier>`      | Authenticate with an MCP server configured in `.cursor/mcp.json` or `~/.cursor/mcp.json` | `agent mcp login <identifier>`      |
| `list`                    | List configured MCP servers and their status                                             | `agent mcp list`                    |
| `list-tools <identifier>` | List available tools and their argument names for a specific MCP                         | `agent mcp list-tools <identifier>` |
| `enable <identifier>`     | Add an MCP server to the local approved list                                             | `agent mcp enable <identifier>`     |
| `disable <identifier>`    | Disable an MCP server so it won't load or prompt for approval                            | `agent mcp disable <identifier>`    |

All MCP commands support `-h, --help` for command-specific help.

#### Sandbox

Configure sandbox mode or run one command in a sandbox.

| Subcommand            | Description                                          | Usage                   |
| --------------------- | ---------------------------------------------------- | ----------------------- |
| `enable`              | Enable sandbox mode for command execution            | `agent sandbox enable`  |
| `disable`             | Disable sandbox mode and use allowlist mode          | `agent sandbox disable` |
| `reset`               | Reset sandbox configuration to defaults              | `agent sandbox reset`   |
| `run <cmd> [args...]` | Run a command in a sandbox with workspace read/write | `agent sandbox run ls`  |
| `help [command]`      | Display help for command                             | `agent sandbox help`    |

| Command       | Option                          | Description                                                        |
| ------------- | ------------------------------- | ------------------------------------------------------------------ |
| `sandbox run` | `--allow-paths <paths>`         | Comma-separated list of extra read/write paths                     |
| `sandbox run` | `--readonly-paths <paths>`      | Comma-separated list of extra read-only paths                      |
| `sandbox run` | `--blocked-patterns <patterns>` | Comma-separated list of gitignore-style patterns to block          |
| `sandbox run` | `--sandbox`                     | Run with the workspace read/write sandbox policy (default: `true`) |
| `sandbox run` | `--network`                     | Enable network access in the sandbox (default: `false`)            |
| `sandbox run` | `--sb-debug`                    | Write sandbox debug logs to a temp folder and print the path       |

All sandbox commands support `-h, --help` for command-specific help.

#### Worker

Start a private cloud worker that connects to Cursor and runs agents in your environment.

| Subcommand       | Description                                                             | Usage                |
| ---------------- | ----------------------------------------------------------------------- | -------------------- |
| `start`          | Start the worker and connect to Cursor                                  | `agent worker start` |
| `debug`          | Run private worker preflight diagnostics for auth, privacy, and routing | `agent worker debug` |
| `help [command]` | Display help for command                                                | `agent worker help`  |

| Command        | Option                             | Description                                                                                         |
| -------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| `worker`       | `--auth-token-file <path>`         | Path to a file containing the worker auth token                                                     |
| `worker`       | `--worker-dir <path>`              | Workspace root to expose to agents. Repeatable. The first value is the assignment identity.         |
| `worker`       | `--management-addr <address>`      | Listen address for `/healthz`, `/readyz`, and `/metrics`                                            |
| `worker`       | `--label <key=value>`              | Add a worker label. Can be used multiple times. Can't be used with `--labels-file`.                 |
| `worker`       | `--labels-file <path>`             | Path to a JSON or TOML labels file. Can also use `CURSOR_WORKER_LABELS_FILE`.                       |
| `worker`       | `--idle-release-timeout <seconds>` | Seconds the worker may stay connected after becoming idle. Default `0` disables idle-based release. |
| `worker`       | `--pool`                           | Register for pool assignment. One cloud agent claims the worker at a time.                          |
| `worker`       | `--single-use`                     | Legacy alias for `--pool`                                                                           |
| `worker`       | `--pool-name <name>`               | Pool label for pool workers. Requires `--pool` or `--single-use`. Defaults to `default`.            |
| `worker`       | `--name <name>`                    | Custom display name. Defaults to the machine hostname.                                              |
| `worker`       | `--data-dir <path>`                | Base directory for logs, artifacts, and recording data                                              |
| `worker`       | `--debug`                          | Print worker debug diagnostics before starting bridge mode                                          |
| `worker start` | `--verbose`                        | Enable verbose startup logs                                                                         |
| `worker debug` | `--json`                           | Output the debug report as JSON                                                                     |

#### Command-specific options

| Command            | Option              | Description                                       |
| ------------------ | ------------------- | ------------------------------------------------- |
| `status`, `whoami` | `--format <format>` | Output format: `text` or `json` (default: `text`) |
| `about`            | `--format <format>` | Output format: `text` or `json` (default: `text`) |

#### Arguments

When starting in chat mode (default behavior), you can provide an initial prompt:

**Arguments:**

- `prompt` — Initial prompt for the agent

#### Getting help

All commands support the global `-h, --help` option to display command-specific help.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Authentication

*Cursor CLI supports two authentication methods: browser-based login (recommended) and API keys.*

**Source:** https://cursor.com/docs/cli/reference/authentication

Cursor CLI supports two authentication methods: browser-based login (recommended) and API keys.

#### Browser authentication (recommended)

Use the browser flow for the easiest authentication experience:

```bash
# Log in using browser flow
agent login

# Check authentication status
agent status

# Log out and clear stored authentication
agent logout
```

The login command opens your default browser and prompts you to authenticate with your Cursor account. Set `NO_OPEN_BROWSER=1` to print the login URL without opening a browser. Once complete, your credentials are securely stored locally.

#### API key authentication

For automation, scripts, or CI environments, use API key authentication:

##### Step 1: Generate an API key

Generate a user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api).

##### Step 2: Set the API key

You can provide the API key in two ways:

**Option 1: Environment variable (recommended)**

```bash
export CURSOR_API_KEY=your_api_key_here
agent "implement user authentication"
```

**Option 2: Command line flag**

```bash
agent --api-key your_api_key_here "implement user authentication"
```

#### Authentication status

Check your current authentication status:

```bash
agent status
```

This command will display:

- Whether you're authenticated
- Your account information
- Current endpoint configuration

#### Troubleshooting

- **"Not authenticated" errors:** Run `agent login` or ensure your API key is correctly set
- **Browser doesn't open:** Run `NO_OPEN_BROWSER=1 agent login` and open the printed URL manually


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Permissions

*Configure what the agent is allowed to do using permission tokens in your CLI configuration. Permissions are set in `~/.cursor/cli-config.json` (global) or `<project>/.cursor/cli.json` (project-specific).*

**Source:** https://cursor.com/docs/cli/reference/permissions

Configure what the agent is allowed to do using permission tokens in your CLI configuration. Permissions are set in `~/.cursor/cli-config.json` (global) or `<project>/.cursor/cli.json` (project-specific).

#### Permission types

##### Shell commands

**Format:** `Shell(commandBase)`

Controls access to shell commands. The `commandBase` is the first token in the command line. Supports glob patterns and an optional `command:args` syntax for finer control.

| Example         | Description                                        |
| --------------- | -------------------------------------------------- |
| `Shell(ls)`     | Allow running `ls` commands                        |
| `Shell(git)`    | Allow any `git` subcommand                         |
| `Shell(npm)`    | Allow npm package manager commands                 |
| `Shell(curl:*)` | Allow `curl` with any arguments                    |
| `Shell(rm)`     | Deny destructive file removal (commonly in `deny`) |

##### File reads

**Format:** `Read(pathOrGlob)`

Controls read access to files and directories. Supports glob patterns.

| Example             | Description                             |
| ------------------- | --------------------------------------- |
| `Read(src/**/*.ts)` | Allow reading TypeScript files in `src` |
| `Read(**/*.md)`     | Allow reading markdown files anywhere   |
| `Read(.env*)`       | Deny reading environment files          |
| `Read(/etc/passwd)` | Deny reading system files               |

##### File writes

**Format:** `Write(pathOrGlob)`

Controls write access to files and directories. Supports glob patterns. Print mode can use write and shell tools. Use `permissions.allow`, `permissions.deny`, and `--force` to control what runs without prompts.

| Example               | Description                           |
| --------------------- | ------------------------------------- |
| `Write(src/**)`       | Allow writing to any file under `src` |
| `Write(package.json)` | Allow modifying package.json          |
| `Write(**/*.key)`     | Deny writing private key files        |
| `Write(**/.env*)`     | Deny writing environment files        |

##### Web fetch

**Format:** `WebFetch(domainOrPattern)`

Controls which domains the agent can fetch when using the web fetch tool (e.g., to retrieve documentation or web pages). Without an allowlist entry, each fetch prompts for approval. Add domains to `allow` to auto-approve fetches from trusted sources.

| Example                     | Description                                       |
| --------------------------- | ------------------------------------------------- |
| `WebFetch(docs.github.com)` | Allow fetches from `docs.github.com`              |
| `WebFetch(*.example.com)`   | Allow fetches from any subdomain of `example.com` |
| `WebFetch(*)`               | Allow fetches from any domain (use with caution)  |

**Domain pattern matching:**

- `*` matches all domains
- `*.example.com` matches subdomains (e.g., `docs.example.com`, `api.example.com`)
- `example.com` matches that exact domain only

##### MCP tools

**Format:** `Mcp(server:tool)`

Controls which MCP (Model Context Protocol) tools the agent can run. Use `server` (from `mcp.json`) and `tool` name, with `*` for wildcards.

| Example          | Description                                 |
| ---------------- | ------------------------------------------- |
| `Mcp(datadog:*)` | Allow all tools from the Datadog MCP server |
| `Mcp(*:search)`  | Allow any server's `search` tool            |
| `Mcp(*:*)`       | Allow all MCP tools (use with caution)      |

#### Configuration

Add permissions to the `permissions` object in your CLI configuration file:

```json
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)",
      "Read(src/**/*.ts)",
      "Write(package.json)",
      "WebFetch(docs.github.com)",
      "WebFetch(*.github.com)",
      "Mcp(datadog:*)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)",
      "WebFetch(malicious-site.com)"
    ]
  }
}
```

#### Pattern matching

- Glob patterns use `**`, `*`, and `?` wildcards
- Relative paths are scoped to the current workspace
- Absolute paths can target files outside the project
- Deny rules take precedence over allow rules
- Use `command:args` (e.g., `curl:*`) to match both command and arguments with globs


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Configuration

*Configure the Agent CLI using the `cli-config.json` file.*

**Source:** https://cursor.com/docs/cli/reference/configuration

Configure the Agent CLI using the `cli-config.json` file.

#### File location

| Type    | Platform    | Path                                       |
| :------ | :---------- | :----------------------------------------- |
| Global  | macOS/Linux | `~/.cursor/cli-config.json`                |
| Global  | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
| Project | All         | `<project>/.cursor/cli.json`               |

Only permissions can be configured at the project level. All other CLI
settings must be set globally.

Override with environment variables:

- **`CURSOR_CONFIG_DIR`**: custom directory path
- **`XDG_CONFIG_HOME`** (Linux/BSD): uses `$XDG_CONFIG_HOME/cursor/cli-config.json`

#### Schema

##### Required fields

| Field               | Type      | Description                                                                                    |
| :------------------ | :-------- | :--------------------------------------------------------------------------------------------- |
| `version`           | number    | Config schema version (current: `1`)                                                           |
| `editor.vimMode`    | boolean   | Enable Vim keybindings (default: `false`)                                                      |
| `permissions.allow` | string\[] | Permitted operations (see [Permissions](https://cursor.com/docs/cli/reference/permissions.md)) |
| `permissions.deny`  | string\[] | Forbidden operations (see [Permissions](https://cursor.com/docs/cli/reference/permissions.md)) |

##### Optional fields

| Field                                 | Type    | Description                                                             |
| :------------------------------------ | :------ | :---------------------------------------------------------------------- |
| `channel`                             | string  | Release channel used for CLI updates                                    |
| `model`                               | object  | Selected model configuration                                            |
| `maxMode`                             | boolean | Persisted preference for max mode in the model picker                   |
| `hasChangedDefaultModel`              | boolean | CLI-managed model override flag                                         |
| `notifications`                       | boolean | Send a terminal notification when the agent finishes or needs input     |
| `hints`                               | boolean | Show CLI hints while the agent is working                               |
| `rewind`                              | boolean | Enable `/rewind` to restore an earlier message in the session           |
| `suggestNextPrompt`                   | boolean | Suggest a follow-up prompt at the end of each turn                      |
| `display.showLineNumbers`             | boolean | Show line numbers in rendered code blocks                               |
| `display.showThinkingBlocks`          | boolean | Render model thinking blocks when available                             |
| `display.showStatusIndicators`        | boolean | Enable terminal title status indicators                                 |
| `display.showStatusLineRunningTime`   | boolean | Show elapsed running time in the status line                            |
| `approvalMode`                        | string  | Approval mode: `allowlist`, `auto-review`, or `unrestricted`            |
| `sandbox.mode`                        | string  | Sandbox mode override                                                   |
| `sandbox.networkAccess`               | string  | Network access setting for sandbox mode                                 |
| `network.useHttp1ForAgent`            | boolean | Use HTTP/1.1 instead of HTTP/2 for agent connections (default: `false`) |
| `attribution.attributeCommitsToAgent` | boolean | Add "Made with Cursor" trailer to Agent commits (default: `true`)       |
| `attribution.attributePRsToAgent`     | boolean | Add "Made with Cursor" footer to Agent PRs (default: `true`)            |

#### Examples

##### Minimal config

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

##### Enable Vim mode

```json
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

##### Configure permissions

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

See [Permissions](https://cursor.com/docs/cli/reference/permissions.md) for available permission types and examples.

#### Troubleshooting

**Config errors**: Move the file aside and restart:

```bash
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Changes don't persist**: Ensure valid JSON and write permissions. Some fields are CLI-managed and may be overwritten.

#### Notes

- Pure JSON format (no comments)
- CLI performs self-repair for missing fields
- Corrupted files are backed up as `.bad` and recreated
- Permission entries are exact strings (see [Permissions](https://cursor.com/docs/cli/reference/permissions.md) for details)

#### Models

You can select a model for the CLI using the `/model` slash command.

```bash
/model auto
/model gpt-5
/model sonnet-4-thinking
```

See the [Slash commands](https://cursor.com/docs/cli/reference/slash-commands.md) docs for other commands.

#### Proxy configuration

If your network routes traffic through a proxy server, configure the CLI using environment variables and the config file.

##### Environment variables

Set these environment variables before running the CLI:

```bash
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
export NODE_USE_ENV_PROXY=1
```

If your proxy performs SSL inspection (man-in-the-middle), also trust your organization's CA certificate:

```bash
export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca-cert.pem
```

##### HTTP/1.1 fallback

Some enterprise proxies (like Zscaler) don't support HTTP/2 bidirectional streaming. Enable HTTP/1.1 mode in your config:

```json
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": [], "deny": [] },
  "network": {
    "useHttp1ForAgent": true
  }
}
```

This switches agent connections to HTTP/1.1 with Server-Sent Events (SSE), which works with most corporate proxies.

See [Network Configuration](https://cursor.com/docs/enterprise/network-configuration.md) for proxy testing commands and troubleshooting.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GitHub Actions

*Use Cursor CLI in GitHub Actions and other CI/CD systems to automate development tasks.*

**Source:** https://cursor.com/docs/cli/github-actions

Use Cursor CLI in GitHub Actions and other CI/CD systems to automate development tasks.

#### GitHub Actions integration

Basic setup:

```yaml
- name: Install Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Run Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    agent -p "Your prompt here" --model gpt-5
```

For Windows runners, use PowerShell: `irm 'https://cursor.com/install?win32=true' | iex`

#### Cookbook examples

See our cookbook examples for practical workflows: [updating documentation](https://cursor.com/docs/cli/headless.md) and [fixing CI issues](https://cursor.com/docs/cli/headless.md).

#### Other CI systems

Use Cursor CLI in any CI/CD system with:

- **Shell script execution** (bash, zsh, etc.)
- **Environment variables** for API key configuration
- **Internet connectivity** to reach Cursor's API

#### Autonomy levels

Choose your agent's autonomy level:

##### Full autonomy approach

Give the agent complete control over git operations, API calls, and external interactions. Simpler setup, requires more trust.

**Example:** In our [Update Documentation](https://cursor.com/docs/cli/headless.md) cookbook, the first workflow lets the agent:

- Analyze PR changes
- Create and manage git branches
- Commit and push changes
- Post comments on pull requests
- Handle all error scenarios

```yaml
- name: Update docs (full autonomy)
  run: |
    agent -p "You have full access to git, GitHub CLI, and PR operations. 
    Handle the entire docs update workflow including commits, pushes, and PR comments."
```

##### Restricted autonomy approach

We recommend using this approach with **permission-based restrictions** for
production CI workflows. This gives you the best of both worlds: the agent can
intelligently handle complex analysis and file modifications while critical
operations remain deterministic and auditable.

Limit agent operations while handling critical steps in separate workflow steps. Better control and predictability.

**Example:** The second workflow in the same cookbook restricts the agent to only file modifications:

```yaml
- name: Generate docs updates (restricted)
  run: |
    agent -p "IMPORTANT: Do NOT create branches, commit, push, or post PR comments. 
    Only modify files in the working directory. A later workflow step handles publishing."

- name: Publish docs branch (deterministic)
  run: |
    # Deterministic git operations handled by CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: update for PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Post PR comment (deterministic)
  run: |
    # Deterministic PR commenting handled by CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs updated"
```

##### Permission-based restrictions

Use [permission configurations](https://cursor.com/docs/cli/reference/permissions.md) to enforce restrictions at the CLI level:

```json
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": ["Shell(git)", "Shell(gh)", "Write(.env*)", "Write(package.json)"]
  }
}
```

#### Authentication

##### Generate your API key

First, [generate an API key](https://cursor.com/docs/cli/reference/authentication.md#api-key-authentication) from your Cursor dashboard.

##### Configure repository secrets

Store your Cursor API key securely in your repository using the GitHub CLI:

```bash
# Repository secret
gh secret set CURSOR_API_KEY --repo OWNER/REPO --body "$CURSOR_API_KEY"

# Organization secret (all repos)
gh secret set CURSOR_API_KEY --org ORG --visibility all --body "$CURSOR_API_KEY"
```

Alternatively, use the GitHub UI: Go to your repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

##### Use in workflows

Set your `CURSOR_API_KEY` environment variable:

```yaml
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Output format

*The Cursor Agent CLI provides multiple output formats with the `--output-format` option when combined with `--print`. These formats include structured formats for programmatic use (`json`, `stream-json`) and a simplified text format for human-readable output (`text`).*

**Source:** https://cursor.com/docs/cli/reference/output-format

The Cursor Agent CLI provides multiple output formats with the `--output-format` option when combined with `--print`. These formats include structured formats for programmatic use (`json`, `stream-json`) and a simplified text format for human-readable output (`text`).

The default `--output-format` is `text`. This option is only valid when
printing (`--print`) or when print mode is inferred (non-TTY stdout or piped
stdin).

#### JSON format

The `json` output format emits a single JSON object (followed by a newline) when the run completes successfully. Deltas and tool events are not emitted; text is aggregated into the final result.

On failure, the process exits with a non-zero code and writes an error message to stderr. No well-formed JSON object is emitted in failure cases.

##### Success response

When successful, the CLI outputs a JSON object with the following structure:

```json
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<full assistant text>",
  "session_id": "<uuid>",
  "request_id": "<optional request id>"
}
```

| Field             | Description                                                         |
| ----------------- | ------------------------------------------------------------------- |
| `type`            | Always `"result"` for terminal results                              |
| `subtype`         | Always `"success"` for successful completions                       |
| `is_error`        | Always `false` for successful responses                             |
| `duration_ms`     | Total execution time in milliseconds                                |
| `duration_api_ms` | API request time in milliseconds (currently equal to `duration_ms`) |
| `result`          | Complete assistant response text (concatenation of all text deltas) |
| `session_id`      | Unique session identifier                                           |
| `request_id`      | Optional request identifier (may be omitted)                        |

#### Stream JSON format

The `stream-json` output format emits newline-delimited JSON (NDJSON). Each line contains a single JSON object representing an event during execution. This format aggregates text deltas and outputs **one line per assistant message** (the complete message between tool calls).

The stream ends with a terminal `result` event on success. On failure, the process exits with a non-zero code and the stream may end early without a terminal event; an error message is written to stderr.

**Streaming partial output:** For real-time character-level streaming, use `--stream-partial-output` with `--output-format stream-json`. This emits text as it's generated in small chunks, with multiple `assistant` events per message.

With `--stream-partial-output`, the CLI emits three kinds of `assistant` events. Only the first kind contains new text:

| `timestamp_ms` | `model_call_id` | What it is                                    | Action                                    |
| -------------- | --------------- | --------------------------------------------- | ----------------------------------------- |
| Present        | Absent          | Streaming delta with new text                 | **Use** — append `message.content[].text` |
| Present        | Present         | Buffered flush before a tool call (duplicate) | **Skip**                                  |
| Absent         | Absent          | Final flush at end of turn (duplicate)        | **Skip**                                  |

If you don't need real-time streaming and only want the finished answer, skip all `assistant` events and read the `result` field from the terminal `result` event.

##### Event types

###### System initialization

Emitted once at the beginning of each session:

```json
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/absolute/path",
  "session_id": "<uuid>",
  "model": "<model display name>",
  "permissionMode": "default"
}
```

Future fields like `tools` and `mcp_servers` may be added to this event.

###### User message

Contains the user's input prompt:

```json
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

###### Assistant message

Emitted once per complete assistant message (between tool calls). Each event contains the full text of that message segment:

```json
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<complete message text>" }]
  },
  "session_id": "<uuid>"
}
```

When `--stream-partial-output` is enabled, assistant events may include two additional fields:

| Field           | Description                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| `timestamp_ms`  | Present on streaming deltas and pre-tool-call flushes. Absent on the final flush at the end of a turn.       |
| `model_call_id` | Present only on the buffered flush emitted before a tool call. Use this to identify and skip duplicate text. |

See the [streaming partial output note](https://cursor.com/docs/cli/reference/output-format.md#stream-json-format) above for how to filter these events.

###### Tool call events

Tool calls are tracked with start and completion events:

**Tool call started:**

```json
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Tool call completed:**

```json
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "file contents...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

###### Tool call types

**Read file tool:**

- **Started**: `tool_call.readToolCall.args` contains `{ "path": "file.txt" }`
- **Completed**: `tool_call.readToolCall.result.success` contains file metadata and content

**Write file tool:**

- **Started**: `tool_call.writeToolCall.args` contains `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
- **Completed**: `tool_call.writeToolCall.result.success` contains `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Other tools:**

- May use `tool_call.function` structure with `{ "name": "tool_name", "arguments": "..." }`

###### Terminal result

The final event emitted on successful completion:

```json
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<full assistant text>",
  "session_id": "<uuid>",
  "request_id": "<optional request id>"
}
```

##### Example sequence

Here's a representative NDJSON sequence showing the typical flow of events:

```json
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Read README.md and create a summary"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"I'll read the README.md file"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Project\n\nThis is a sample project...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Based on the README, I'll create a summary"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Done! I've created the summary in summary.txt"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"I'll read the README.md fileBased on the README, I'll create a summaryDone! I've created the summary in summary.txt","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

#### Text format

The `text` output format provides only the final assistant message without any intermediate progress updates or tool call summaries. This is the cleanest output format for scripts that only need the agent's final response.

This format is ideal when you want just the answer or final message from the agent, without any progress indicators or tool execution details.

##### Example output

```
The command to move this branch onto main is `git rebase --onto main HEAD~3`.
```

Only the final assistant message (after the last tool call) is output, with no tool call summaries or intermediate text.

#### Notes

- Each event is emitted as a single line terminated by `\n`
- `thinking` events are suppressed in print mode and will not appear in any output format
- Field additions may occur over time in a backward-compatible way (consumers should ignore unknown fields)
- The `json` format waits for completion before outputting results
- The `stream-json` format outputs complete agent messages
- The `--stream-partial-output` flag provides real-time text deltas for character-level streaming (only works with `stream-json` format)
- Tool call IDs can be used to correlate start/completion events
- Session IDs remain consistent throughout a single agent execution


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Terminal setup

*Configure your terminal for the best Cursor CLI experience. This guide covers keybindings for multi-line input, Vim mode, and theme synchronization.*

**Source:** https://cursor.com/docs/cli/reference/terminal-setup

Configure your terminal for the best Cursor CLI experience. This guide covers keybindings for multi-line input, Vim mode, and theme synchronization.

#### Quick start

If Shift+Enter doesn't work for newlines in your terminal, run `/setup-terminal` for guidance on configuring alternatives:

```bash
/setup-terminal
```

This command detects your terminal and provides instructions for configuring Option+Enter as an alternative way to insert newlines.

#### Universal options

These methods work in **all terminals**, including tmux, screen, and SSH sessions:

| Method | Description                                              |
| :----- | :------------------------------------------------------- |
| +Enter | Type a backslash, then press Enter to insert a newline   |
| Ctrl+J | Standard control character for newline (ASCII line feed) |

If you're in tmux or having trouble with other keybindings, Ctrl+J is the most reliable option.

#### Terminal support

##### Native Shift+Enter support

These terminals support Shift+Enter for newlines out of the box:

- **iTerm2** (macOS)
- **Ghostty**
- **Kitty**
- **Warp**
- **Zed** (integrated terminal)

##### Requires `/setup-terminal`

These terminals need `/setup-terminal` to configure Option+Enter for newlines:

- **Apple Terminal** (macOS)
- **Alacritty**
- **VS Code** (integrated terminal)

##### Terminal multiplexers

**tmux** and **screen** intercept Shift+Enter before it reaches applications. Use the universal options instead:

- Ctrl+J — Works reliably in all multiplexer sessions
- +Enter — Also works universally

You can configure your outer terminal (e.g., iTerm2) for Shift+Enter, but the keybinding won't pass through tmux. Use the universal options for the most consistent experience.

#### Vim mode

Enable Vim keybindings for navigation and editing in the CLI input area.

##### Toggle with slash command

```bash
/vim
```

This toggles Vim mode on or off for the current session and saves the preference.

##### Configure in settings

Add to your `~/.cursor/cli-config.json`:

```json
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": [], "deny": [] }
}
```

##### Modes

Vim mode uses modal editing:

- **Normal mode** — Navigate and execute commands (default when Vim mode is enabled)
- **Insert mode** — Type text normally

Press Esc to return to normal mode from insert mode.

##### Navigation

| Key     | Description                                           |
| :------ | :---------------------------------------------------- |
| h, l    | Move left / right                                     |
| j, k    | Move down / up                                        |
| w, b    | Next / previous word                                  |
| e       | End of word                                           |
| W, B, E | Same as above, but for WORD (non-whitespace sequence) |
| 0, $    | Start / end of line                                   |

##### Editing

| Key        | Description                                 |
| :--------- | :------------------------------------------ |
| x          | Delete character under cursor               |
| X          | Delete character before cursor              |
| d + motion | Delete range (e.g., `dw` deletes word)      |
| dd         | Delete entire line                          |
| D          | Delete to end of line                       |
| s          | Substitute character (delete + insert mode) |
| S, cc      | Change entire line                          |
| C          | Change to end of line                       |

##### Entering insert mode

| Key | Description             |
| :-- | :---------------------- |
| i   | Insert at cursor        |
| a   | Insert after cursor     |
| I   | Insert at start of line |
| A   | Insert at end of line   |
| o   | Open new line below     |
| O   | Open new line above     |

##### Counts

Prefix commands with a number to repeat them. For example, `3w` moves forward 3 words, `2dd` deletes 2 lines.

Vim mode affects the input area only. Navigation through chat history and other UI elements uses standard keybindings.

#### Terminal theme

Cursor CLI automatically detects your terminal's color scheme and adapts its appearance.

##### Automatic detection

The CLI queries your terminal for its background color using standard escape sequences. Most modern terminals support this:

- **Dark terminals** → CLI uses dark theme
- **Light terminals** → CLI uses light theme

##### Terminals with automatic detection

These terminals report their color scheme correctly:

- iTerm2
- Ghostty
- Kitty
- Alacritty
- Apple Terminal
- Windows Terminal
- VS Code integrated terminal

##### Forcing a theme

If automatic detection doesn't work, you can override it with an environment variable:

```bash
# Force dark theme
export COLORFGBG="15;0"

# Force light theme
export COLORFGBG="0;15"
```

Add this to your shell profile (`.bashrc`, `.zshrc`, etc.) to make it permanent.

##### Troubleshooting theme issues

**Colors look wrong:**

- Ensure your terminal supports 256 colors or true color
- Check that `TERM` is set correctly (e.g., `xterm-256color`)
- Try setting `COLORFGBG` explicitly

**tmux users:**

- Add to your `.tmux.conf` to pass through color detection:
  ```
  set -g default-terminal "tmux-256color"
  set -ag terminal-overrides ",xterm-256color:RGB"
  ```
- Restart tmux after making changes

#### Manual configuration

If `/setup-terminal` doesn't work for your terminal, you can manually configure keybindings.

##### Option+Enter for newlines

Option+Enter sends a special escape sequence that Cursor CLI recognizes as a newline. Configure your terminal to send `\x1b\r` (Escape followed by carriage return) when Option+Enter is pressed.

**iTerm2:**

1. Open **Preferences** → **Profiles** → **Keys** → **Key Mappings**
2. Click **+** to add a new mapping
3. Set **Keyboard Shortcut** to Option+Enter
4. Set **Action** to "Send Escape Sequence"
5. Enter `\r` as the escape sequence

**Alacritty:**

Add to your `alacritty.toml`:

```toml
[keyboard]
bindings = [
  { key = "Return", mods = "Alt", chars = "\u001b\r" }
]
```

**Kitty:**

Add to your `kitty.conf`:

```
map alt+enter send_text all \x1b\r
```

##### Shift+Enter

Shift+Enter support depends on your terminal correctly reporting the key modifier. Most modern terminals handle this automatically, but some may need configuration.

**VS Code terminal:**

VS Code's integrated terminal may not pass Shift+Enter correctly. Add to your `keybindings.json`:

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "\u001b[13;2u" },
  "when": "terminalFocus"
}
```

#### Troubleshooting

**Keybindings not working:**

- Verify your terminal is detecting the keys correctly using `cat` or `showkey`
- Check if a terminal multiplexer (tmux/screen) is intercepting the keys
- Use Ctrl+J as a reliable fallback

**tmux users:**

- Shift+Enter and Option+Enter won't work through tmux
- Use Ctrl+J or +Enter instead
- These universal options work everywhere, including nested tmux sessions

**SSH sessions:**

- Remote terminal capabilities depend on your local terminal emulator
- Ctrl+J works reliably over SSH
- +Enter is another reliable option

#### Summary

| Keybinding   | Works in                          | Notes                                                      |
| :----------- | :-------------------------------- | :--------------------------------------------------------- |
| Ctrl+J       | All terminals                     | Most reliable, works everywhere                            |
| +Enter       | All terminals                     | Universal alternative                                      |
| Shift+Enter  | iTerm2, Ghostty, Kitty, Warp, Zed | Native support, no config needed                           |
| Option+Enter | After `/setup-terminal`           | Newline alternative for Apple Terminal, Alacritty, VS Code |


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---

## Account & Enterprise

### Get Started

*Cursor works for individuals and teams. The Teams plan provides tools for organizations: SSO, team management, access controls, and usage analytics.*

**Source:** https://cursor.com/docs/account/teams/setup

#### Cursor for Teams

Cursor works for individuals and teams. The Teams plan provides tools for organizations: SSO, team management, access controls, and usage analytics.

#### Creating a Team

Create a team by following these steps:

##### Set up Teams plan

To create a Team, follow these steps:

1. **For new users**: Visit [cursor.com/team/new-team](https://cursor.com/team/new-team) to create a new account and team
2. **For existing users**: Go to your [dashboard](https://cursor.com/docs/account/teams/dashboard.md) and click "Upgrade to Teams"

##### Enter Team details

Select a Team name and billing cycle

##### Invite members

Invite team members. User counts are prorated - you only pay for the time users are members.

You can opt in to domain matching so teammates with verified, matching email domains can join your team without an invite. Configure it in [team settings](https://cursor.com/dashboard/settings#domain-join).

##### Enable SSO (optional)

Enable [SSO](https://cursor.com/docs/account/teams/sso.md) for security and automated onboarding.

#### FAQ

##### My team uses ZScalar / a proxy / a VPN, will Cursor work?

Cursor uses HTTP/2 by default. Some proxies and VPNs block this.

Go to `Cursor Settings` > `Network`, then set `HTTP Compatibility Mode` to `HTTP/1.1`.

##### How can I purchase licenses for my company?

Cursor bills per active user, not seats. Add or remove users anytime - new members are charged pro-rata for their remaining time. If a removed user has used any credits, their seat remains occupied until the end of the billing cycle.

Your renewal date stays the same.

##### How can I set up a team when I'm not using Cursor?

Set yourself as an [Unpaid Admin](https://cursor.com/docs/account/teams/members.md) to manage without a license.

Teams need at least one paid member. You can set up, invite a member, then change your role before billing.

##### How can I add Cursor to my company's MDM?

Download links for all platforms are available at [cursor.com/downloads](https://cursor.com/downloads).

MDM instructions:

- [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (formerly VMware)
- [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
- [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
- [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)

##### Can I be a member of more than one team?

No, a Cursor account cannot be a member of more than one team at a time. If you need to switch teams, you'll need to leave your current team first before joining another.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Team Pricing

*There are two business plans: Teams and Enterprise (Custom). Teams offers two types of seats: Standard ($40/user/mo) and Premium (5x usage at $120/user/mo).*

**Source:** https://cursor.com/docs/account/teams/pricing

There are two business plans: Teams and Enterprise (Custom). Teams offers two types of seats: Standard ($40/user/mo) and Premium (5x usage at $120/user/mo).

Team plans provide additional features like:

- Centralized team billing and administration, with usage stats also available via the [Admin API](https://cursor.com/docs/account/teams/admin-api.md)
- Team marketplace for internal rules, skills, and plugins
- Agentic code reviews with Bugbot
- Cloud agents and automations with shared team context
- Usage analytics to understand team behavior
- Team-wide privacy mode enforcement
- SAML/OIDC SSO

We recommend Teams for any customer that is happy self-serving. We recommend [Enterprise](https://cursor.com/docs/enterprise.md) for customers that need priority support, pooled usage, invoicing, SCIM, or advanced security controls. [Contact sales](https://cursor.com/contact-sales?source=docs-teams-pricing) to get started.

#### How pricing works

Teams pricing is based on paid seats and usage. Each paid seat includes monthly usage, and you can continue using Cursor beyond that with on-demand usage.

##### Seat types

Teams has two paid seat types and one free admin-only seat type:

- **Standard**: $40/user/mo with the standard Teams usage allowance
- **Premium**: $120/user/mo with 5x the usage of a Standard seat
- **Free**: $0/user/mo for Unpaid Admins who manage the team without Cursor access

Seat type is separate from role. Members and Admins can have either a Standard or Premium seat. Unpaid Admins don't use a paid seat.

##### Included usage

Each paid seat comes with included usage across two pools:

- First-party models (Auto, Composer 2.5, and Grok 4.5)
- Third-party API models

Usage is allocated per user based on seat type, does not transfer between team members, and resets at the start of each billing cycle. Third-party API model usage is charged at public list API prices plus the Cursor Token Rate. First-party models, including Auto, Composer 2.5, and Grok 4.5, are exempt from the Cursor Token Rate.

The [usage dashboard](https://cursor.com/dashboard/usage) tracks included usage separately for:

- First-party models
- Third-party API models

Our [Enterprise plan](https://cursor.com/docs/enterprise.md) offers pooled usage shared between all users in a team. [Get in touch](https://cursor.com/contact-sales?source=docs-teams-pricing) with our team to learn more.

##### On-demand usage

On-demand usage allows you to continue using models after included usage is consumed, billed in arrears.

When a team member consumes all of their included third-party API model usage, Cursor switches them to the First-party models pool. If they continue using third-party API models, or if they fully consume their First-party models pool usage, they continue with **on-demand usage** if it is enabled.

- Third-party API models are billed monthly at public list API prices plus the Cursor Token Rate
- First-party models, including Auto, Composer 2.5, and Grok 4.5, are billed monthly at their token rates with no Cursor Token Rate
- No interruption in service or quality
- Tracked per user in your admin dashboard (see [spending data API](https://cursor.com/docs/account/teams/admin-api.md#get-spending-data))
- Can be controlled with spending limits

On-demand usage is enabled by default for the Teams plan.

##### Cursor Token Rate

The Cursor Token Rate is **$0.25 per million tokens** and is charged only on non-Auto, third-party model requests. This covers:

- Custom model execution (Tab, Apply, etc.)
- Infrastructure and processing costs

The Cursor Token Rate applies to input tokens, output tokens, and cached tokens on eligible third-party model requests. This applies to [BYOK](https://cursor.com/help/models-and-usage/api-keys.md) as well. Auto requests and all first-party models, including Composer 2.5 and Grok 4.5, are exempt.

#### Active seats

Cursor bills per active paid seat, not pre-allocated seats. Add, remove, upgrade, or downgrade users anytime and billing will adjust based on seat type.

- Adding a member mid-cycle creates a pro-rated charge
- Removing a member who used credits keeps the seat occupied until the cycle ends
- Billing adjustments appear as account credit on a future invoice when applicable
- Your renewal date stays the same

#### Spending controls

Teams can configure monthly team-wide spending limits. You can manage these limits through the dashboard. Per-member spend limits are available on [Enterprise](https://cursor.com/docs/enterprise.md) plans.

Contact `enterprise@cursor.com` for volume discounts on larger teams.

#### Model Pricing

All prices are per million tokens. Teams are charged at public list API prices plus [Cursor Token Rate](https://cursor.com/docs/account/teams/pricing.md#cursor-token-rate) only for non-Auto third-party model requests.

| Model                                                                                         | Provider  | Input | Cache write | Cache read | Output | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------- | --------- | ----- | ----------- | ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Claude 4 Sonnet](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Thinking variant counts as 2 requests in legacy pricing                                                                                                                                                                                                                                                                                                                                                                      |
| [Claude 4 Sonnet 1M](https://www.anthropic.com/claude/sonnet)                                 | Anthropic | $6    | $7.5        | $0.6       | $22.5  | Hidden by default; Thinking variant counts as 2 requests in legacy pricing; This model can be very expensive due to the large context window; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                 |
| [Claude 4.5 Haiku](https://www.anthropic.com/claude/haiku)                                    | Anthropic | $1    | $1.25       | $0.1       | $5     | Hidden by default; Bedrock/Vertex: regional endpoints +10% surcharge; Cache: writes 1.25x, reads 0.1x                                                                                                                                                                                                                                                                                                                                           |
| [Claude 4.5 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans                                                                                                                                                                                                                                                                                                                                                                              |
| [Claude 4.5 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.6 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude 4.7 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                                                                               |
| [Claude Fable 5](https://www.anthropic.com/claude)                                            | Anthropic | $10   | $12.5       | $1         | $50    | Requires data retention approval for Enterprise customers, Teams and individual customers with Privacy Mode enabled; Anthropic stores agent input and output data for harm-prevention processes; this data is not used to train or improve Anthropic models or products; Requests that trip a security guardrail are automatically routed to Claude Opus; About 2x the cost of Claude Opus 4.8; Requires Max Mode on legacy request-based plans |
| [Claude Opus 4.7 (fast mode)](https://www.anthropic.com/claude/opus)                          | Anthropic | $30   | $37.5       | $3         | $150   | Hidden by default; Requires Max Mode on legacy request-based plans; Limited research preview; Up to 1M tokens with extended context at the same per-token rates as shorter context                                                                                                                                                                                                                                                              |
| [Claude Opus 4.8](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Requires Max Mode on legacy request-based plans; Fast mode (\`claude-opus-4-8-fast\`) requires Max Mode on legacy request-based plans; Fast mode is 3x lower per-token pricing than Opus 4.7 fast mode; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge)                                                                                                                                           |
| [Claude Sonnet 5](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | $3    | $3.75       | $0.3       | $15    | Launch promotion: $2/M input and $10/M output through August 31, 2026; Requires Max Mode on legacy request-based plans; Up to 1M tokens with extended context at the same per-token rates (no long-context surcharge); Uses an updated tokenizer, so the same input can map to more tokens                                                                                                                                                      |
| [Composer 1](https://cursor.com)                                                              | Cursor    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Composer 2.5](https://cursor.com/blog/composer-2-5)                                          | Cursor    | $0.5  | -           | $0.2       | $2.5   | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 2.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/) | Google    | $0.3  | -           | $0.03      | $2.5   | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs)                                       | Google    | $0.5  | -           | $0.05      | $3     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro](https://ai.google.dev/gemini-api/docs)                                         | Google    | $2    | -           | $0.2       | $12    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs)                           | Google    | $2    | -           | $0.2       | $12    | Hidden by default; Native image generation model optimized for speed, flexibility, and contextual understanding; Text input and output priced the same as Gemini 3 Pro; Image output: $120/1M tokens (\~$0.134 per 1K/2K image, \~$0.24 per 4K image); Preview models may change before becoming stable and have more restrictive rate limits                                                                                                   |
| [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs)                                       | Google    | $2    | -           | $0.2       | $12    | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs)                                     | Google    | $1.5  | -           | $0.15      | $9     | -                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GLM 5.2](https://z.ai)                                                                       | Z.ai      | $1.4  | -           | $0.26      | $4.4   | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5](https://openai.com/index/gpt-5/)                                                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5-high                                                                                                                                                                                                                                                                                                                                         |
| [GPT-5 Fast](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $2.5  | -           | $0.25      | $20    | Hidden by default; Faster speed but 2x price; Available reasoning effort variants are gpt-5-high-fast, gpt-5-low-fast                                                                                                                                                                                                                                                                                                                           |
| [GPT-5 Mini](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5-Codex](https://platform.openai.com/docs/models/gpt-5-codex)                            | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.1 Codex Max](https://platform.openai.com/docs/models/gpt-5-codex)                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [GPT-5.1 Codex Mini](https://platform.openai.com/docs/models/gpt-5-codex)                     | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default; Agentic and reasoning capabilities; 4x rate limits compared to GPT-5.1 Codex                                                                                                                                                                                                                                                                                                                                                 |
| [GPT-5.2](https://openai.com/index/gpt-5/)                                                    | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.2-high                                                                                                                                                                                                                                                                                                                                       |
| [GPT-5.2 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                                                                                                                           |
| [GPT-5.3 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.3-codex-high                                                                                                                                                                                                                                                                                |
| [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)                              | OpenAI    | $2.5  | -           | $0.25      | $15    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; 90% discount on cached input tokens; Fast mode is 15% faster with 2x pricing; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                                                                               |
| [GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)                    | OpenAI    | $0.75 | -           | $0.075     | $4.5   | Hidden by default; Smaller, faster variant of GPT-5.4; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                                      |
| [GPT-5.4 Nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)                    | OpenAI    | $0.2  | -           | $0.02      | $1.25  | Hidden by default; Smallest GPT-5.4 variant, optimized for cost; 90% discount on cached input tokens                                                                                                                                                                                                                                                                                                                                            |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)                              | OpenAI    | $5    | -           | $0.5       | $30    | Hidden by default; Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; More token-efficient than GPT-5.4 on comparable tasks; Improved persistence on long-running tasks; Fast mode is available at higher rates; Long context supports up to 1M tokens with 2x input pricing                                                                                                                                  |
| [GPT-5.6 Luna](https://openai.com/index/previewing-gpt-5-6-sol/)                              | OpenAI    | $1    | $1.25       | $0.1       | $6     | Smallest GPT-5.6 variant, optimized for cost and speed; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                      |
| [GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)                               | OpenAI    | $5    | $6.25       | $0.5       | $30    | Requires Max Mode on legacy request-based plans; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Long context supports up to 1M tokens with 2x input pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                |
| [GPT-5.6 Terra](https://openai.com/index/previewing-gpt-5-6-sol/)                             | OpenAI    | $2.5  | $3.125      | $0.25      | $15    | Mid-tier GPT-5.6 variant between Sol and Luna; Agentic and reasoning capabilities; Fast mode is available at 2x pricing; Cache writes are billed at 1.25x the uncached input rate                                                                                                                                                                                                                                                               |
| Grok 4.5                                                                                      | Cursor    | $2    | -           | $0.5       | $6     | Jointly trained by Cursor and SpaceXAI                                                                                                                                                                                                                                                                                                                                                                                                          |
| Kimi K2.7 Code                                                                                | Moonshot  | $0.95 | -           | $0.19      | $4     | Hidden by default                                                                                                                                                                                                                                                                                                                                                                                                                               |


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Members, Roles, and Seat Types

*Cursor Teams use roles for permissions and seat types for usage limits.*

**Source:** https://cursor.com/docs/account/teams/members

Cursor Teams use roles for permissions and seat types for usage limits.

#### Roles

**Members** are the default role with access to Cursor's Pro features.

- Full access to Cursor's Pro features
- No access to billing settings or admin dashboard
- Can see their own usage and remaining included usage

**Admins** control team management and security settings.

- Full access to Pro features
- Add/remove members, modify roles, set up SSO
- Configure on-demand usage and spending limits
- Access to team analytics

**Unpaid Admins** manage teams without using a paid seat - ideal for IT or finance staff who don't need Cursor access.

- Not billable, no Pro features
- Same administrative capabilities as Admins

Unpaid Admins require at least one paid user on the team.

#### Seat Types

Teams offers two paid seat types, plus a free admin-only seat type:

**Standard seats** are for light coding agent users.

- $40/user/mo
- Includes the standard Teams usage allowance
- Can be assigned to Members or Admins

**Premium seats** are for coding agent power users who need more included usage.

- $120/user/mo
- Includes 5x the usage of a Standard seat
- Can be assigned to Members or Admins

**Unpaid Admin seats** are for IT, security, or finance admins who manage Cursor without using it.

- Free
- No Cursor product access or included usage
- Can only be assigned to Unpaid Admins

##### Change a seat type

Admins can upgrade a paid user from Standard to Premium from the member context menu. The upgrade takes effect immediately, and billing is adjusted for the rest of the billing cycle.

Admins can downgrade a paid user from Premium to Standard from the member context menu. The user keeps Premium through the end of the current billing cycle, then moves to Standard at the next renewal.

#### Role Comparison

| Capability             |                                         Member                                        |                                         Admin                                         |                                      Unpaid Admin                                     |
| ---------------------- | :-----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| Use Cursor features    |                                           ✓                                           |                                           ✓                                           |                                                                                       |
| Invite members         |                                           ✓                                           |                                           ✓                                           |                                           ✓                                           |
| Remove members         |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Change user role       |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Admin dashboard        |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Configure SSO/Security |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Manage Billing         |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| View Analytics         |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Manage Access          |                                                                                       |                                           ✓                                           |                                           ✓                                           |
| Set usage controls     | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#team-level-limits) | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#team-level-limits) | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#team-level-limits) |
| Requires paid seat     |                                           ✓                                           |                                           ✓                                           |                                                                                       |

#### Managing members

##### Add member

Add members in several ways:

1. **Email invitation**

   - Click `Invite Members`
   - Enter email addresses
   - Users receive email invites

2. **Invite link**

   - Click `Invite Members`
   - Copy `Invite Link`
   - Share with team members

3. **SSO**
   - Configure SSO in [admin dashboard](https://cursor.com/docs/account/teams/sso.md)
   - Users auto-join when logging in via SSO email

4. **Domain matching**
   - Teammates with a verified, matching email domain can join your team without an invite
   - Enable this in [team settings](https://cursor.com/dashboard/settings#domain-join)

Invite links have a long expiration date. Anyone with the link can join.
Revoke them regularly, or use [SSO](https://cursor.com/docs/account/teams/sso.md) or [domain restrictions](https://cursor.com/docs/account/teams/members.md#domain-settings) to control access.

##### Remove member

Admins can remove members anytime via context menu → "Remove".

**Billing:**

- If a member has used any credits, their seat remains occupied until the end of the billing cycle
- Billing is automatically adjusted with pro-rated credit for removed members applied to the next invoice

**Data deletion:**

- When a user is removed from the team, their data (including Memories and Cloud Agent data) is permanently deleted
- When an entire team is deleted, all associated data is permanently deleted
- There must be at least one Admin and one paid member on the team at all times

##### Change role

Admins can change roles for other members by clicking the context menu and then use the "Change role" option.

There must be at least one Admin, and one paid member on the team at all times.

#### Domain settings

Admins can configure two domain-based controls in [team settings](https://cursor.com/dashboard/settings#domain-join). Both require at least one verified domain and are available on Team and Enterprise plans for teams not using SCIM provisioning.

##### Domain matching

When enabled, anyone with a verified, matching email domain can join your team directly from the dashboard, no invite needed. This is useful for letting teammates self-serve without admins manually sending invitations.

##### Restrict invites to verified domains

When enabled, team members can only invite users whose email addresses match a verified domain. Invitations to email addresses outside your verified domains are blocked.

This prevents accidental or unauthorized additions and gives admins tighter control over who joins the team.

These settings are for teams that don't use SCIM provisioning. If your team uses SCIM, member management is handled through your identity provider.

#### Security & SSO

SAML 2.0 Single Sign-On (SSO) is available on Team plans. Key features include:

- Configure SSO connections ([learn more](https://cursor.com/docs/account/teams/sso.md))
- Set up domain verification
- Automatic user enrollment
- SSO enforcement options
- Identity provider integration (Okta, etc)

Domain verification is required to enable SSO.

#### Usage Controls

Access usage settings to:

- Enable on-demand usage
- Set admin-only modifications
- Set monthly spending limits
- Monitor team-wide usage

#### Billing

When adding team members:

- Each member or admin adds a billable seat (see [pricing](https://cursor.com/pricing))
- New members are charged pro-rata for their remaining time in the billing period
- Unpaid admin seats aren't counted

Mid-month additions charge only for days used. The seat price depends on whether the user has a Standard or Premium seat. When removing members who have used credits, their seat remains occupied until the end of the billing cycle.

Role changes (e.g., Admin to Unpaid Admin) adjust billing from the change date. Choose monthly or yearly billing.

Monthly/yearly renewal occurs on your original signup date, regardless of member changes.

##### Switch to Yearly billing

Save **20%** by switching from monthly to yearly:

1. Go to [cursor.com/dashboard/billing](https://cursor.com/dashboard/billing)
2. Click **Upgrade Now** on the green banner at the top

There is no way to switch from yearly to monthly mid-plan. You'll need to cancel, wait for the year to end, then re-subscribe on a monthly plan.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### SSO

*SAML 2.0 SSO is available at no additional cost on Teams and Enterprise plans. Use your existing identity provider (IdP) to authenticate team members without separate Cursor accounts.*

**Source:** https://cursor.com/docs/account/teams/sso

#### Overview

SAML 2.0 SSO is available at no additional cost on Teams and Enterprise plans. Use your existing identity provider (IdP) to authenticate team members without separate Cursor accounts.

#### Prerequisites

- Cursor Team plan
- Admin access to your identity provider (e.g., Okta)
- Admin access to your Cursor organization

#### Configuration Steps

##### Sign in to your Cursor account

Navigate to [cursor.com/dashboard/settings](https://www.cursor.com/dashboard/settings) with an admin account.

##### Locate the SSO configuration

Find the "Single Sign-On (SSO)" section and expand it.

##### Begin the setup process

Click the "SSO Provider Connection settings" button to start SSO setup and follow the wizard.

##### Configure your identity provider

In your identity provider (e.g., Okta):

- Create new SAML application
- Configure SAML settings using Cursor's information
- Set up Just-in-Time (JIT) provisioning

##### Verify domain

Verify the domain of your users in Cursor by clicking the "Domain verification settings" button.

##### Identity Provider Setup Guides

For provider-specific setup instructions:

##### Identity Provider Guides

Setup instructions for Okta, Azure AD, Google Workspace, and more.

#### Additional Settings

- Manage SSO enforcement through admin dashboard
- New users auto-enroll when signing in through SSO
- Handle user management through your identity provider

#### Multiple domains

To handle multiple domains in your organization:

1. **Verify each domain separately** in Cursor through the domain verification settings
2. **Configure each domain** in your identity provider
3. Each domain needs to go through the verification process independently

#### Troubleshooting

If issues occur:

- Verify domain is verified in Cursor
- Ensure SAML attributes are properly mapped
- Check SSO is enabled in admin dashboard
- Match first and last names between identity provider and Cursor
- Check provider-specific guides above
- Visit the [SSO help center](https://cursor.com/help/security-and-privacy/sso.md) if issues persist


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Dashboard

*The dashboard lets you access billing, set up usage-based pricing, and manage your Team.*

**Source:** https://cursor.com/docs/account/teams/dashboard

The dashboard lets you access billing, set up usage-based pricing, and manage your Team.

#### Overview

Get a quick summary of your team's activity, usage statistics, and recent changes. The overview page provides at-a-glance insights into your workspace.

![Team dashboard](https://cursor.com/docs-static/images/account/team/dashboard.png)

#### Settings

![Team settings](https://cursor.com/docs-static/images/account/team/settings.png)

Configure team-wide preferences and security settings. The settings page includes:

#### Teams & Enterprise Settings

##### Privacy Settings

Control data sharing preferences for your team. Configure whether your data can be used for training, and manage team-wide privacy enforcement.

##### Usage-Based Pricing Settings

Enable usage-based pricing and set spending limits. Configure monthly team
spending limits. Control whether only admins can modify these settings.

##### Team Marketplaces

Import private marketplaces from GitHub or use the Default marketplace to
distribute shared Team MCP servers. Set **Marketplace Access** for the whole
team, selected Organization Groups, or an existing SCIM directory-group
configuration. Teams plans can add up to 1 team marketplace. Enterprise plans
can add unlimited team marketplaces. Learn more in [Team
Marketplaces](https://cursor.com/docs/plugins.md#team-marketplaces).

##### Bedrock IAM Role

Configure AWS Bedrock IAM roles for secure cloud integration.

##### Single Sign-On (SSO)

Set up SSO authentication for enterprise teams to streamline user access and
improve security.

##### Protected Git Scopes

Lock a Git organization, group, or namespace to your Cursor organization so
only your teams can use its repositories with Cloud Agents, automations, and
Bugbot. Learn more in [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes).

##### Cursor Admin API Keys

Create and manage API keys for programmatic access to Cursor's admin features.

##### Active Sessions

Monitor and manage active user sessions across your team.

##### Invite Code Management

Create and manage invite codes for adding new team members.

##### API Endpoints

Access Cursor's REST API endpoints for programmatic integration. All API endpoints are available on both Team and [Enterprise](https://cursor.com/docs/enterprise.md) plans, except for the [AI Code Tracking API](https://cursor.com/docs/account/teams/ai-code-tracking-api.md) which requires Enterprise plan.

#### Enterprise-Only Settings

**Device-level enforcement:** In addition to dashboard settings, enterprises can enforce policies like allowed team IDs and allowed extensions on user devices through MDM. See [Identity and Access Management](https://cursor.com/docs/enterprise/identity-and-access-management.md#mdm-policies) and [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for details.

##### Model Access Control

Control which AI models are available to team members. Set restrictions on
specific models or model tiers to manage costs and ensure appropriate usage
across your organization. Learn more in [Model and Integration Management](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

##### Enhanced Spend Limits

Set individual spending limits for each team member. Configure member-level overrides, group-based limits via directory sync, or default per-member caps.

##### Auto Run Configuration

Configure automatic command execution settings. Control which commands can be executed automatically and set security
policies for code execution.

##### Repository Blocklist

Prevent access to specific repositories for security or compliance reasons. Learn more in [Model and Integration Management](https://cursor.com/docs/enterprise/model-and-integration-management.md#repository-blocklist).

##### MCP Configuration

Configure Model Context Protocol settings.
Manage how models access and process context from your development
environment. Learn more in [Model and Integration Management](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-server-trust-management).

##### Cursor Ignore Configuration

Set up ignore patterns for files and directories. Control which files and directories are excluded from AI analysis and
suggestions. Learn more in [Security Guardrails](https://cursor.com/docs/enterprise/llm-safety-and-controls.md#cursorignore).

##### .cursor Directory Protection

Protect the .cursor directory from unauthorized agent access. Ensure sensitive configuration and cache files remain secure. Learn more in [Security Guardrails](https://cursor.com/docs/enterprise/llm-safety-and-controls.md#cursor-directory-protection).

##### AI Code Tracking API

Access detailed AI-generated code analytics for your team's repositories. Retrieve per-commit AI usage metrics and granular accepted AI changes through REST API endpoints. Requires Enterprise team plan. Learn more in [AI Code Tracking API](https://cursor.com/docs/account/teams/ai-code-tracking-api.md).

##### Audit Log

View comprehensive, tamper-proof records of security events and administrative actions. Track authentication, team changes, permission updates, API key actions, settings modifications, and more. Requires an Enterprise subscription. Learn more in [Compliance and Monitoring](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs).

**SCIM** (System for Cross-domain Identity Management) provisioning is also
available for [Enterprise](https://cursor.com/docs/enterprise.md) plans. See our [SCIM
documentation](https://cursor.com/docs/account/teams/scim.md) for setup instructions.

#### Members

Manage your team members, invite new users, and control access permissions. Set role-based permissions and monitor member activity.

![Team members](https://cursor.com/docs-static/images/account/team/members.png)

#### Audit Log

Track security events, administrative actions, and team changes with comprehensive audit logs. View detailed records of who did what, when, and from where. Audit logs capture authentication events, membership changes, permission updates, API key actions, settings modifications, and more.

![Audit Log](https://cursor.com/docs-static/images/account/team/audit-log.png)

**Audit Log** is available exclusively on [Enterprise](https://cursor.com/docs/enterprise.md) plans and can only be viewed by admins.

#### Integrations

![Integrations](https://cursor.com/docs-static/images/account/team/integrations.png)

Connect Cursor with your favorite tools and services. Configure integrations with version control systems, project management tools, and other developer services.

#### Cloud Agents

Monitor and manage cloud agents running in your workspace. View agent status, logs, and resource usage. See [Cloud Agent settings](https://cursor.com/docs/cloud-agent/settings.md) for configuration details.

#### Bugbot

Access automated bug detection and fixing capabilities. Bugbot helps identify and resolve common issues in your codebase automatically.

![Bugbot code review](https://cursor.com/docs-static/images/account/team/bugbot.png)

#### Active Directory Management

For enterprise teams, manage user authentication and access through Active Directory integration. Configure SSO and user provisioning.

#### Usage

Track detailed usage metrics including AI requests, model usage, and resource consumption. Monitor usage across team members and projects.

![Usage](https://cursor.com/docs-static/images/account/team/usage.png)

#### Billing & Invoices

Manage your subscription, update payment methods, and access billing history. Download invoices and manage usage-based pricing settings.

![Billing](https://cursor.com/docs-static/images/account/team/billing.png)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Usage Analytics

*Usage Analytics are available for Team and Enterprise customers.*

**Source:** https://cursor.com/docs/account/teams/analytics

Usage Analytics are available for Team and Enterprise customers.

The Cursor [Web Dashboard](https://cursor.com/dashboard/analytics) provides usage analytics so you can understand how your team is using Cursor.

#### Data Access and Visibility

Team admins have access to data for themselves and all other users in the team. Team members without admin privileges can see data for themselves and in some cases (like the Usage Leaderboard) for select other users on the team.

Analytics data is collected only from users running client version 1.5 or higher.

##### CSV Download

Each chart has a button on the bottom-right corner which allows for CSV download of visible data. Additionally, users can download data for all charts by clicking the download icon in the page header.

##### API Access

See our [Admin API documentation](https://cursor.com/docs/account/teams/analytics-api.md) to access analytics data programmatically. Available only for Enterprise customers.

#### Filtering Data

Dashboard users can filter usage shown for specific users, [active directory groups](https://cursor.com/docs/account/teams/scim.md#managing-users-and-groups), and dates via the header. Filtering supports up to 10 users and 90 continuous days of data.

Clicking on the gear icon in the header allows users to select timezone as well as whether weekends are shown.

#### Tracking AI Code in Git Commits

Cursor keeps a log of the signature of every AI line (Tab or Agent) that is suggested to the user during their chat session.

These lines are stored and later compared to the signatures of each line in subsequent git commits that were written by the same author. Cursor will detect all the line changes (additions or deletions) written by the Cursor Agent or Tab, and attribute the line as being written by AI.

All the AI detection is done on device, and never leaves the user's computer. We store the line counts as metadata and make them available via API or in the Analytics Dashboard.

###### Known Limitations:

- Diff signatures may be invalidated if automated code formatting is modifying lines.

- AI Code Tracking has not been implemented for Background Agents, or the Cursor CLI yet.

- All code signatures are stored on-device. The git commit must be scored on the same machine as the AI code was authored.

#### AI Output

##### AI Share of Committed Code

![AI Share of Committed Code chart](https://cursor.com/docs-static/images/account/team/analytics/ai-share-committed-code.png)

AI Share of Committed Code shows the lines of code changed in commits to your repositories, and what % of that code was generated by Cursor. Users can filter for production branch, which will use:

- The optional default branch set to the git repo

- Fallback to common default branch names such as: `main`, `master`, `production`, `prod`.

We use the following definitions:

- **Cursor AI**: Any line that can be attributed to Cursor Agent or Tab based on diff signatures.

- **Other**: Any line of code that can't be detected as being written by Cursor

##### Agent Edits

![Agent Edits chart](https://cursor.com/docs-static/images/account/team/analytics/agent-edits.png)

Agent Edits shows the amount of code edited by the Agent, and Cmd+K, and whether those changes were accepted by the user. Viewers can group the data by suggested / accepted or by file extension.

##### Tab Completions

![Tab Completions chart](https://cursor.com/docs-static/images/account/team/analytics/tab-completions.png)

Tab Completions shows the number of times Tab code has been suggested (and accepted) by users. The unit is Tab suggestions, regardless of lines of code changed in that suggestion.

You can access the number of lines of code suggested by Tab through the [Analytics API](https://cursor.com/docs/account/teams/analytics-api.md).

##### Messages Sent

![Messages Sent chart](https://cursor.com/docs-static/images/account/team/analytics/messages-sent.png)

Messages Sent shows the number of messages sent by users to Cursor. Users can filter this data by the mode (e.g., Agent, Ask, Cmd+K) or by models used.

#### Active Users

![Active Users chart](https://cursor.com/docs-static/images/account/team/analytics/active-users.png)

The Active Users chart shows the number of unique active Cursor users in your team across different products. A user is defined as active in a period if they use at least one AI feature (Tab, Agent, Background Agent, CLI). Bugbot users are synced to Github accounts (not Cursor) and therefore not included in the `All` active user rollup.

#### Daily Usage

![Daily Usage chart](https://cursor.com/docs-static/images/account/team/analytics/daily-usage.png)

The Daily Usage chart visualizes Cursor activity over the preceding 365 days.

Users can toggle to see this view by:

- **All**: shows lines of code edits suggested by AI in Cursor (Tab and Agent).

- **Tab:** shows the number of suggestions made by Tab.

- **Agent:** shows lines of code suggested by Agent.

- **DAU**: shows daily active users across all Cursor products.

Data collection for this chart starts in early September for customers on the 1.5+ desktop release.

#### Usage Leaderboard

![Usage Leaderboard chart](https://cursor.com/docs-static/images/account/team/analytics/usage-leaderboard.png)

The Usage Leaderboard shows top Cursor users across your team alongside their favorite model and select usage stats for the selected time period.

We provide the following metrics:

- **Chats**: number of messages sent by the user in the chat interface (Agent, Plan Mode, Ask Mode, etc).

- **Tab Completions**: number of Tab suggestions accepted by the user.

- **Agent Lines of Code:** Lines of code written by the Agent and accepted by the user.

The top ten users and any filtered users are always shown. All users in the team are able to view the leaderboard.

#### Repository Insights

![Repository Insights chart](https://cursor.com/docs-static/images/account/team/analytics/repository-insights.png)

Repository Insights allow you to see how Cursor is used across different repositories. We report on:

- **AI Lines of Code Committed**: Code written by Cursor (Tab and Agent) that was committed by a user.

- **Total Lines of Code Committed**: All code committed by users.

- **Code Committed by AI %**: The % of lines of code committed that were edited by Cursor (Tab and Agent).

Some commits will be associated with `Unknown` repository if the user makes commits to a local git repository that doesn't contain a remote origin, or a remote that couldn't be resolved by Cursor

#### Conversation Insights

Conversation Insights is enabled by default for Enterprise customers. You can disable it via **Disable Conversation Insights** in team settings.

Cursor analyzes the code and context in each agent session to understand what kind of work is occurring. This makes Cursor the first self-aware software engineering platform, synthesizing the type of work happening across your team.

Teams no longer need high-toil, lossy analysis of tickets or low-response surveys to understand engineering work. Conversation Insights lets you deeply understand the type of work being done with Cursor.

![Conversation Insights dashboard showing categories and work type charts](https://cursor.com/docs-static/images/account/team/analytics/conversation-insights-dashboard.png)

##### Classification Dimensions

Conversation Insights classifies work across these dimensions:

- **Category**: Bug Fixing & Debugging, Code Refactoring, Code Explanation, Configuration, New Features, UI/Styling, Architecture, Data/Database, Documentation, DevOps/Deployment, Learning, Testing

- **Work Type**: Maintenance (KTLO), Bug Fixing, New Features

- **Complexity**: Distinguishes between the complexity of tasks teams assign to agents

- **Specificity**: Measures how specific the prompts developers use with agents are

Enterprise customers can extend these default categories or define their own across the organization or within specific teams.

##### Compare

Compare allows you to select and compare usage across teams and individual developers within your organization. Use this to identify adoption patterns, find power users, and understand how different groups use Cursor.

##### Privacy and Data Handling

All classification runs on-device. Default classifiers ensure no PII or sensitive data leaves the machine. The model outputs are validated against expected values. Any responses that don't match are discarded.

##### Pricing

Conversation Insights is free during the preview period. Starting January 1st, 2026, customers will be charged for inference. The Cursor Token Rate applies only when the underlying request is a non-Auto third-party model request.

#### Cloud Agent Usage

##### Agents Created

![Agents Created chart](https://cursor.com/docs-static/images/account/team/analytics/agents-created.png)

Agents Created shows Cloud Agent usage by the originating source. Each time a Cloud Agent starts up counts as one Agent.

##### Pull Requests

![Pull Requests chart](https://cursor.com/docs-static/images/account/team/analytics/pull-requests.png)

Pull Requests shows Pull Requests Opened and Merged that originate from Cloud Agents.

##### Lines of Code

![Lines of Code chart](https://cursor.com/docs-static/images/account/team/analytics/lines-of-code.png)

Lines of Code shows code written and merged by Cloud Agents.

#### Cloud Agent Top Repositories

![Cloud Agent Top Repositories chart](https://cursor.com/docs-static/images/account/team/analytics/cloud-agent-top-repositories.png)

Cloud Agent Top Repositories shows repositories by number of Pull Requests opened and merged.

#### Top Cloud Agent Users

![Top Cloud Agent Users chart](https://cursor.com/docs-static/images/account/team/analytics/top-cloud-agent-users.png)

Top Cloud Agent Users shows top users by number of Agents Created. Viewers can also view data by Pull Requests opened and merged.

#### Client Versions

![Client Versions chart](https://cursor.com/docs-static/images/account/team/analytics/client-versions.png)

Client Versions shows which versions of the Cursor editor your team is using. Each user's version is the Cursor version they last opened during that day.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Enterprise

*Cursor provides enterprise-grade security, compliance, and administrative controls for organizations deploying AI-assisted development at scale.*

**Source:** https://cursor.com/docs/enterprise

Cursor provides enterprise-grade security, compliance, and administrative controls for organizations deploying AI-assisted development at scale.

If you are rolling out multiple linked teams, start with [Organizations](https://cursor.com/docs/enterprise/organizations.md).

#### Security and compliance resources

For security reviews and compliance assessments, start with these resources:

- [Trust Center](https://trust.cursor.com/) - Security practices, certifications, and compliance information
- [Security page](https://cursor.com/security) - Detailed security architecture and controls
- [Privacy Overview](https://cursor.com/privacy-overview) - Data handling and privacy guarantees
- [Data Processing Agreement](https://cursor.com/terms/dpa) - GDPR-compliant DPA with data protection commitments

Our certifications include SOC2 Type II, and we maintain GDPR compliance. Visit the [Trust Center](https://trust.cursor.com/) for the latest certification documents and third-party assessment reports.

#### Enterprise documentation

Learn how to deploy, configure, and manage Cursor for your organization. This documentation covers:

- [Security and Privacy Hardening](https://cursor.com/docs/enterprise/security-hardening.md) - One-page checklist of security and privacy controls with links to configure each one
- [Organizations](https://cursor.com/docs/enterprise/organizations.md) - Org-wide team membership sync and organization groups
- [Identity & access](https://cursor.com/docs/enterprise/identity-and-access-management.md) - SSO, SCIM, RBAC, and MDM policies
- [Privacy & data governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) - Data flows, Privacy Mode, and data residency
- [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md) - Proxy setup, IP allowlisting, and encryption
- [Private connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) - AWS PrivateLink and Cloudflare Tunnel for private source control access
- [Endpoint security](https://cursor.com/docs/enterprise/endpoint-security.md) - Configure antivirus, EDR, and DLP software
- [LLM safety & controls](https://cursor.com/docs/enterprise/llm-safety-and-controls.md) - Hooks, terminal sandboxing, and agent controls
- [Models & integrations](https://cursor.com/docs/enterprise/model-and-integration-management.md) - Model controls, MCP, and third-party integrations
- [Cyber Safeguards](https://cursor.com/docs/account/enterprise/cyber-safeguards.md) - Apply for Anthropic's Cyber Verification Program (CVP) to use eligible Claude models without cyber safeguards
- [Spend Limits](https://cursor.com/help/account-and-billing/spend-limits.md) - Configure spending limits to control costs
- [Compliance & monitoring](https://cursor.com/docs/enterprise/compliance-and-monitoring.md) - Audit logs and tracking
- [HIPAA Business Associate Agreements](https://cursor.com/docs/enterprise/baa.md) - Request BAA support for Enterprise customers
- [Deployment patterns](https://cursor.com/docs/enterprise/deployment-patterns.md) - MDM-managed editor vs self-hosted CLI

#### Key features

##### Identity and access

- [SSO and SAML](https://cursor.com/docs/account/teams/sso.md) - Single sign-on for streamlined authentication
- [SCIM](https://cursor.com/docs/account/teams/scim.md) - Automated user provisioning and deprovisioning
- [MDM policies](https://cursor.com/docs/enterprise/identity-and-access-management.md#mdm-policies) - Enforce allowed team IDs and extensions on user devices

##### Privacy and security

- [Privacy Mode](https://cursor.com/privacy-overview) - No training on your data by Cursor or other AI providers
- [Agent Security](https://cursor.com/docs/agent/security.md) - Guardrails for agent tool execution
- [Hooks](https://cursor.com/docs/hooks.md) - Custom security and compliance workflows

##### Administrative controls

- [Dashboard](https://cursor.com/docs/account/teams/dashboard.md) - Team management, settings, and monitoring
- [Admin API](https://cursor.com/docs/account/teams/admin-api.md) - Programmatic access to admin features
- [Analytics](https://cursor.com/docs/account/teams/analytics.md) - Usage metrics and insights
- [Conversation Insights](https://cursor.com/docs/account/teams/analytics.md#conversation-insights) - Understand the type of work being done with Cursor (Enterprise only)
- [AI Code Tracking API](https://cursor.com/docs/account/teams/ai-code-tracking-api.md) - Per-commit AI usage metrics (Enterprise only)
- [Cursor Blame](https://cursor.com/docs/integrations/cursor-blame.md) - AI-aware git blame that shows AI vs human code attribution (Enterprise only)
- [Analytics API](https://cursor.com/docs/account/teams/analytics-api.md) - Usage metrics and insights
- [Billing Groups](https://cursor.com/docs/account/enterprise/billing-groups.md) - Manage spend across groups of users for reporting and chargebacks (Enterprise only)
- [Service Accounts](https://cursor.com/docs/account/enterprise/service-accounts.md) - Non-human accounts for automated workflows (Enterprise only)

##### Models and integrations

- [Models](https://cursor.com/docs/models-and-pricing.md) - Available models and configuration
- [Cyber Safeguards](https://cursor.com/docs/account/enterprise/cyber-safeguards.md) - Anthropic Cyber Verification Program (CVP) access for security groups (Enterprise only)
- [MCP](https://cursor.com/docs/mcp.md) - Model Context Protocol server trust management
- [Slack](https://cursor.com/docs/integrations/slack.md) - Cloud Agents in Slack
- [GitHub](https://cursor.com/docs/integrations/github.md) - Repository integration
- [Linear](https://cursor.com/docs/integrations/linear.md) - Issue tracking integration
- [Bugbot](https://cursor.com/docs/bugbot.md) - Automated bug detection and fixing

##### Monitoring and compliance

- Audit logs - Track authentication, user management, and administrative actions (Enterprise only)
- SIEM integration - Stream audit logs to your security tools
- [HIPAA Business Associate Agreements](https://cursor.com/docs/enterprise/baa.md) - BAA support for Enterprise customers

#### Getting started

1. Review the [Trust Center](https://trust.cursor.com/) and [Security page](https://cursor.com/security) for your security assessment
2. Read through the [enterprise documentation](https://cursor.com/docs/enterprise.md) to understand deployment options
3. Set up [SSO](https://cursor.com/docs/account/teams/sso.md) and [SCIM](https://cursor.com/docs/account/teams/scim.md) for user management
4. Deploy Cursor and configure [MDM policies](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) to enforce team IDs and extensions
5. Review the [Dashboard](https://cursor.com/docs/account/teams/dashboard.md) to monitor team usage

#### Plan Comparison

##### Team Admin & Billing

| Capability                                                                                                          | Individual Plans | Teams                                                                     | Enterprise                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Centralized Billing                                                                                                 |                  | ✓                                                                         | ✓                                                                                                                                                                                                                                                                 |
| Usage Spend Controls                                                                                                | Personal limits  | Team limits                                                               | [Pooled usage + admin-only controls](https://cursor.com/help/account-and-billing/spend-limits.md#enterprise)                                                                                                                                                      |
| [Billing Groups](https://cursor.com/docs/account/enterprise/billing-groups.md)                                      |                  |                                                                           | ✓                                                                                                                                                                                                                                                                 |
| [Team Usage Analytics](https://cursor.com/docs/account/teams/analytics.md#analytics)                                |                  | [Analytics Dashboard](https://cursor.com/docs/account/teams/analytics.md) | [Analytics Dashboard](https://cursor.com/docs/account/teams/analytics.md),[AI Code Tracking API](https://cursor.com/docs/account/teams/ai-code-tracking-api.md),[Conversation Insights](https://cursor.com/docs/account/teams/analytics.md#conversation-insights) |
| [Cursor Blame](https://cursor.com/docs/integrations/cursor-blame.md)                                                |                  |                                                                           | ✓                                                                                                                                                                                                                                                                 |
| [SSO (SAML/OIDC)](https://cursor.com/docs/enterprise/identity-and-access-management.md#single-sign-on-sso-and-saml) |                  | ✓                                                                         | ✓                                                                                                                                                                                                                                                                 |
| [SCIM Provisioning](https://cursor.com/docs/account/teams/scim.md)                                                  |                  |                                                                           | ✓                                                                                                                                                                                                                                                                 |
| [Audit Logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs)                            |                  |                                                                           | ✓                                                                                                                                                                                                                                                                 |
| [Service Accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)                                  |                  |                                                                           | ✓                                                                                                                                                                                                                                                                 |

##### Marketplace

| Capability                        | Individual Plans | Teams                 | Enterprise                                                                                                         |
| --------------------------------- | ---------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Team marketplaces                 |                  | 1 team marketplace    | Unlimited team marketplaces                                                                                        |
| Community plugin import           |                  | On by default         | Off by default                                                                                                     |
| Marketplace edits                 |                  | All teams can edit    | Only admin edits                                                                                                   |
| SCIM distribution & access gating |                  | No SCIM access gating | Scope distribution and gate access via SCIM (control who sees which marketplace based on identity provider groups) |

##### Centralized Agent Controls

| Capability                                                                                                              | Individual Plans | Teams                  | Enterprise                                                                           |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------- | ------------------------------------------------------------------------------------ |
| [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#privacy-mode-enforcement)              | User choice      | Enforce org-wide       | Enforce org-wide                                                                     |
| [Team Rules](https://cursor.com/docs/rules.md#team-rules)                                                               |                  | Enforceable + Optional | Enforceable + Optional                                                               |
| [Hooks for Logging,Auditing, and more](https://cursor.com/docs/hooks.md#hooks)                                          | ✓                | MDM Distribution       | [MDM & Server-side distribution](https://cursor.com/docs/hooks.md#team-distribution) |
| [Agent Sandbox Mode](https://cursor.com/docs/agent/security/run-modes.md#sandboxing)                                    | ✓                | ✓                      | Enforce org-wide                                                                     |
| [Repository Blocklist](https://cursor.com/docs/enterprise/model-and-integration-management.md#git-repository-blocklist) |                  |                        | ✓                                                                                    |
| [Model Access Restrictions](https://cursor.com/docs/enterprise/model-and-integration-management.md)                     |                  |                        | ✓                                                                                    |
| [Auto-run, Browser, and Network Controls](https://cursor.com/docs/enterprise/llm-safety-and-controls.md)                |                  |                        | ✓                                                                                    |

##### User Access Controls

| Capability   | Individual & Teams Plans | Enterprise                                     |
| ------------ | ------------------------ | ---------------------------------------------- |
| Cursor CLI   |                          | Restrict which users can access agents via CLI |
| Cloud Agents |                          | Restrict which users can create Cloud Agents   |
| Analytics    |                          | Restrict analytics dashboard to admins only    |
| BYOK         |                          | Disable users from using their own API keys    |

##### Support & Legal

| Capability        | Individual Plans                                          | Teams                                                     | Enterprise                                                          |
| ----------------- | --------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- |
| Technical Support | [Community & Standard Support](https://forum.cursor.com/) | [Community & Standard Support](https://forum.cursor.com/) | First human response times: 8 hours (critical), 24 hours (standard) |
| Terms             | [Online Terms](https://cursor.com/terms-of-service)       | [MSA & DPA](https://cursor.com/terms/msa)                 | [MSA & DPA](https://cursor.com/terms/msa)                           |

For security vulnerabilities, see our [responsible disclosure program](https://cursor.com/docs/agent/security.md#responsible-disclosure).

##### Ready to deploy Cursor at scale?

Contact our team to discuss your organization's needs.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Organizations

*Organizations are the top-level container for Enterprise customers. They sit above teams and give you one place to manage shared identity, administration, and organization-wide settings.*

**Source:** https://cursor.com/docs/enterprise/organizations

Organizations are the top-level container for Enterprise customers. They sit above teams and give you one place to manage shared identity, administration, and organization-wide settings.

#### Organizations model

Organizations can include multiple teams, created around departments, business units, regions, or roles. Each team defines its own membership, roles, usage views, privacy settings, usage controls, and other team-level settings. Organizations sit above those teams and provide shared identity, administration, and org-wide settings.

Each Organization has a default team that acts as a stable home team for login and routing.

Users can belong to multiple teams in the same Organization, and their role can differ by team. For example, one person can be an admin in one team, a member in another, and not belong to a third team.

#### Identity model

Organizations support org-level SSO with your identity provider integration. This is the recommended model when you want one login setup across the company.

Team-level SSO is still supported for team-specific identity requirements. Organizations add a shared identity layer, but they do not remove team-level SSO options.

#### Usage and contract boundaries

Usage can be tracked at the team level for day-to-day reporting. With organization-pooled billing, teams can draw from a shared committed pool.

See [Pooled usage](https://cursor.com/docs/enterprise/pooled-usage.md) for details.

#### Groups

Organization Groups help you organize users across teams. Organization Groups are useful for org-wide cohorts such as Engineering, Contractors, or Pilot Users. Members can belong to multiple teams, so organization admins can apply settings to the same cohort regardless of each user's team membership.

See [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md) for setup, SCIM mapping, membership management, and group-level controls.

#### How limits and permissions combine

Users may have different effective settings, such as usage limits and allowed models, across organization-level groups and team-level directory groups. Cursor reconciles these settings with a "most permissive wins" model.

For example, if a user is in an organization-level group and a team, Cursor uses the highest spend limit setting between the two.

| Layer                 | What it controls                         | How multiple sources combine                                                                 |
| --------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| Team default          | Baseline per-user spend caps             | Used only when nothing more specific is set                                                  |
| Per-user on team      | Override for one user                    | Wins over team defaults and directory group settings                                         |
| Directory Group(s)    | SCIM-synced spend caps and team policies | Spend limits use the highest value; policy behavior is generally most permissive             |
| Organization Group(s) | Org-level allowances and policy          | Across org groups, highest value applies; compared with team baseline, highest value applies |

When choosing between team-level settings and Organization Group-level settings, use a bottom-up model from least permissive to most permissive. Set the strictest defaults at the team level, then use Organization Groups to give specific user cohorts more permissive settings.

#### Roles

Organizations add org-level administration on top of team-level roles. Org admins can manage organization settings, organization membership, shared identity configuration, and view teams in the Organization. Team admins and team owners manage settings and members for their own teams.

Team admin access does not automatically grant org admin access. Users can also have different roles at each layer. For example, a user can be an org admin while only being a member of specific teams.

#### Organization API

For org-level automation, use the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md).

#### Related docs

- [Enterprise overview](https://cursor.com/docs/enterprise.md)
- [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md)
- [Identity & access management](https://cursor.com/docs/enterprise/identity-and-access-management.md)
- [SCIM](https://cursor.com/docs/account/teams/scim.md)
- [Admin API](https://cursor.com/docs/account/teams/admin-api.md)
- [Billing groups](https://cursor.com/docs/account/enterprise/billing-groups.md)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Organization Groups

*Organization Groups let Enterprise admins organize users across teams in the same Cursor Organization. Use them for cohorts such as Engineering, Contractors, Executives, or Pilot Users when the same set of people needs shared settings even if they belong to different teams.*

**Source:** https://cursor.com/docs/enterprise/organization-groups

Organization Groups let Enterprise admins organize users across teams in the same Cursor Organization. Use them for cohorts such as Engineering, Contractors, Executives, or Pilot Users when the same set of people needs shared settings even if they belong to different teams.

Organization Groups are separate from [Billing Groups](https://cursor.com/docs/account/enterprise/billing-groups.md). Billing Groups help a team report and attribute spend. Organization Groups manage organization-level cohorts and the settings that apply to them.

#### When to use Organization Groups

Use Organization Groups when you want to:

- Apply model access or usage controls to a cross-team cohort
- Manage a group from your identity provider through SCIM
- Give a pilot group access to a new model or setting before enabling it broadly
- Restrict a team marketplace to selected cohorts
- Keep team defaults strict while allowing specific users more permissive settings
- Manage group membership through the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups)

#### Create a group

In the dashboard, open your Organization and go to **Groups**.

You can create:

- **Manual groups**: Cursor admins add, remove, import, and move members in the dashboard or through the Organization API.
- **SCIM-synced groups**: Cursor maps the Organization Group to a directory group from your identity provider. Membership is managed in your identity provider and synced into Cursor.

For SCIM-synced groups, manage membership in your identity provider. Cursor
shows the synced members but disables manual membership changes that would be
overwritten by the next sync.

#### Manage members

Open a group and select **Members** to view and manage membership.

For manual groups, admins can:

- Add existing Organization members
- Import members by CSV
- Move members to another Organization Group
- Remove members
- Search and sort the member list

SCIM-synced groups are read-only for membership. Admins can still manage Cursor-owned settings for the group, such as spend limits and model access.

#### Configure group settings

Open a group and select **Settings** to manage group-level controls.

##### Spend limits

Organization Groups can set per-user monthly spend limits. When a user belongs to multiple groups or has team-level limits, Cursor applies the most permissive applicable limit.

For example, if a team default is stricter and an Organization Group has a higher limit, the group limit applies to that user. If a group limit is lower than an already more permissive team setting, it does not make the user's access stricter.

##### Model access

Use the **Models** tab to configure model access for a group. This is useful for controlled rollouts, approvals, or giving specific cohorts access to models that are not enabled for everyone.

Group model settings combine with team settings using a permissive model: set restrictive defaults at the team level, then use Organization Groups to widen access for selected cohorts.

##### Auto-run and Smart Auto

Organization Groups can also carry group-level agent and model-routing controls, including auto-run and Smart Auto settings where available.

When the same Auto-run setting is defined at both the team level and the Organization Group level, Cursor merges each field independently. Inactive Auto-run policies do not participate. If the team Auto-run policy is disabled and the Organization Group policy is active, Cursor uses the Organization Group policy.

| Setting                    | How team and Organization Group settings combine                                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Run modes                  | Union. A mode is available if either level enables it: Allowlist, Auto-review, or Run Everything.                                              |
| Terminal command allowlist | Union with deduplication. Commands allowed by either level are allowed.                                                                        |
| Delete File Protection     | Enabled if either level enables it.                                                                                                            |
| Browser Protection         | Enabled if either level enables it.                                                                                                            |
| Sandboxing Mode            | Loosest setting wins. `disabled` beats `enabled`, so sandboxing is enabled only when both levels enable it.                                    |
| Sandbox Networking         | Loosest setting wins. `user_controlled` beats `always_disabled`, so networking is always disabled only when both levels set `always_disabled`. |
| Sandbox Git Access         | Same as Sandbox Networking: `user_controlled` beats `always_disabled`.                                                                         |

When multiple Organization Groups apply to the same user, Cursor applies the same field-wise merge rules across those groups.

Auto-review instructions have separate precedence. If an Organization Group defines instructions, they replace the team-level instructions for that user.

Because groups can include users from multiple teams, team-level restrictions still matter. If a user's team blocks a model required by a group setting, that team-level restriction can affect the user's experience.

##### Team marketplace access

Team admins can use Organization Groups to control who can see and use a [team marketplace](https://cursor.com/docs/plugins.md#team-marketplaces). Open **Dashboard -> Plugins**, select a marketplace, then choose groups under **Marketplace Settings -> Marketplace Access**.

A team marketplace remains scoped to its owning team. Selecting an Organization Group grants access only to group members who also belong to that team. Team admins retain access, and a marketplace with no selected groups is available to everyone in the team.

Existing marketplaces that use team-level SCIM directory groups keep those assignments. Cursor does not migrate them to Organization Groups automatically.

#### Organization Groups and SCIM

SCIM lets your identity provider control who belongs to a group. This is the recommended approach when the group mirrors an existing department, role, or access cohort in your IdP.

Before mapping SCIM groups, make sure [SCIM provisioning](https://cursor.com/docs/account/teams/scim.md) is configured for your Organization. Then create or edit an Organization Group and connect it to the matching directory group.

An SCIM-synced Organization Group is an organization-level cohort. A legacy team directory group is a separate team-level access source. Existing team marketplaces can continue using directory groups while new marketplace assignments use Organization Groups.

#### API access

You can list groups, read members, and add or remove members through the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups).

Organization Group API routes use Organization API keys and group IDs with the `g_` prefix.

##### Organization Groups are available on Enterprise

Contact our team to learn more about organization-level administration.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Identity and Access Management

*Identity and access management controls who can use Cursor in your organization and what they can do. You'll set up authentication, automate user provisioning, and enforce policies through device management.*

**Source:** https://cursor.com/docs/enterprise/identity-and-access-management

Identity and access management controls who can use Cursor in your organization and what they can do. You'll set up authentication, automate user provisioning, and enforce policies through device management.

We recommend implementing identity controls in this order:

1. **Set up SSO**: Get centralized authentication working first
2. **Enable SCIM**: Automate user lifecycle management
3. **Deploy MDM policies**: Enforce allowed team IDs and extensions
4. **Assign roles**: Grant admin access to the right people

#### Single Sign-On (SSO) and SAML

SSO lets your users authenticate to Cursor using your existing identity provider. Instead of creating separate Cursor passwords, users log in with their corporate credentials.

Cursor supports SAML 2.0 integration with providers like Okta, Azure AD, Google Workspace, and OneLogin. When you enable SSO, you can require it for all team members, preventing password-based authentication entirely.

If your company has multiple linked teams, we recommend a shared org-level SSO model through [Organizations](https://cursor.com/docs/enterprise/organizations.md). Team-level SSO setups are still supported for team-specific identity requirements.

See [SSO and SAML setup](https://cursor.com/docs/account/teams/sso.md) for detailed configuration instructions.

#### SCIM provisioning

SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider. Available on Enterprise plans with SSO enabled.

Without SCIM, you need to manually add users to your Cursor team and remove them when they leave. With SCIM:

- New employees get Cursor access automatically when added to the right group
- Departing employees lose access when removed from your IDP
- Group membership changes propagate automatically

See [SCIM provisioning](https://cursor.com/docs/account/teams/scim.md) for setup instructions.

#### Role-Based Access Control (RBAC)

Cursor teams have three roles: Members, Admins, and Unpaid Admins.

See [Members, Roles, and Seat Types](https://cursor.com/docs/account/teams/members.md) for more information.

#### MDM policies

Mobile Device Management (MDM) systems let you enforce policies on user devices. Cursor supports MDM-based policies on macOS and Intune / Group Policy on Windows to ensure users comply with organizational requirements.

See [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for platform-specific MDM configuration instructions.

##### Allowed Team IDs

The most important MDM policy prevents users from logging into personal Cursor accounts on corporate devices.

When you set an allowed team ID policy, Cursor only permits authentication to those specific team IDs. If a user tries to log in with a different team ID (like a personal account), Cursor logs them out immediately.

For example, if your employees have corporate laptops, you can set the allowed team ID to your enterprise team ID. This prevents them from accidentally using personal accounts that might not have Privacy Mode enabled.

The `cursorAuth.allowedTeamId` Cursor setting controls which team IDs are permitted to log into Cursor. This setting accepts a comma-separated list of team IDs that are authorized for access.

For example, setting `cursorAuth.allowedTeamId` to `"1,3,7"` allows users from those specific team IDs to log in.

When a user attempts to log in with a team ID that is not in the allowed list:

- They are forcefully logged out immediately
- An error message is displayed
- The application prevents further authentication attempts until a valid team ID is used

To centrally manage allowed team IDs for your organization, configure the `AllowedTeamId` policy using your device management solution. This policy overrides the `cursorAuth.allowedTeamId` setting on users' devices. The value of this policy is a string containing the comma-separated list of authorized team IDs.

See [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for platform-specific MDM configuration instructions.

##### Allowed Extensions

Control which extensions users can install in Cursor. Extensions can access your workspace, so you want to ensure only trusted extensions run.

**How it works:**

The `extensions.allowed` Cursor setting controls which extensions can be installed. This setting accepts a JSON object where keys are publisher names or full extension IDs, and values are booleans indicating whether they are allowed.

> **Important:** `extensions.allowed` uses an allowlist model. As soon as you add any entries, only explicitly allowed entries are permitted, and everything else is blocked. There is no implicit "allow all" fallback. For example, setting `extensions.allowed` to `{"anysphere": false}` does not only block Anysphere extensions; it blocks every other publisher too, because nothing else is on the allowlist.

To block specific extensions while keeping everything else allowed, use the `"*": true` wildcard alongside the entries you want to deny. The wildcard is the least specific match, so publisher and extension ID entries override it:

```json
{
  "*": true,
  "untrusted-publisher": false
}
```

To restrict installs to an approved set of publishers and extensions, omit the wildcard and list only what you trust. You can include full extension IDs, pin to specific versions, or pin to a release channel:

```json
{
  "anysphere": true,
  "github": true,
  "esbenp.prettier-vscode": true,
  "ms-azuretools.vscode-containers": false,
  "dbaeumer.vscode-eslint": ["3.0.0"],
  "github.vscode-pull-request-github": "stable"
}
```

**Admin Portal Configuration:**

Team admins can configure allowed extensions through the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) in the Security & Identity section. The configuration is applied automatically to all team members' Cursor clients. Leave the field empty to stop pushing a value to clients.

> **Resetting clients to "allow all":** Clearing the admin portal field stops pushing a new value, but it does not remove the policy that clients already applied locally. Users keep enforcing the last value they received. To reset everyone back to allowing all extensions, deploy `{"*": true}` first, wait for clients to pick it up, and then clear the field if you no longer want to manage the setting centrally.

> **Note:** Admin portal configuration for this feature requires Cursor client version 2.1 or later. Users on older versions will not have extension restrictions applied.

**MDM Configuration:**

To centrally manage allowed extensions using device management, configure the `AllowedExtensions` policy. This policy overrides both the admin portal setting and user-configured `extensions.allowed` settings. The value of this policy is a JSON string that defines the allowed extensions.

To centrally manage allowed extensions for your organization, configure the `AllowedExtensions` policy using your device management solution. This policy overrides the `extensions.allowed` setting on users' devices. The value of this policy is a JSON string that defines the allowed publishers.

See [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for platform-specific MDM configuration instructions.

##### The .cursor folder

When you open a project in Cursor, the editor creates a `.cursor` folder at the root of your repository. This folder contains:

- Project-specific settings
- Indexing cache
- Project rules and context

This folder can be checked into source control. Your team members benefit from shared rules and settings, but be aware that these configurations are visible to anyone with repository access.

For repositories you don't control access to, review the `.cursor` folder contents before committing. Don't put sensitive information in rules files.

You can also manage rules and commands through the server on the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md).

##### Workspace Trust

The `security.workspace.trust.enabled` Cursor setting controls whether the Workspace Trust feature is enabled. This setting accepts a boolean value that determines if users will be prompted to trust workspaces before full functionality is enabled.

For example, setting `security.workspace.trust.enabled` to `true` enables workspace trust prompts, while setting it to `false` disables the feature entirely (all workspaces are automatically trusted).

When workspace trust is enabled:

- Users are prompted to trust each new workspace when opening it for the first time
- Untrusted workspaces run in a restricted mode with limited functionality
- Trust decisions are saved and remembered for each workspace

To centrally manage workspace trust for your organization, configure the `WorkspaceTrustEnabled` policy using your device management solution. This policy overrides the `security.workspace.trust.enabled` setting on users' devices. The value of this policy is a boolean (`true` or `false`).

See [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for platform-specific MDM configuration instructions.

##### Advanced identity controls are available on Enterprise

Contact our team to learn about SCIM, MDM policies, and more.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### SCIM

*SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider. Available on Enterprise plans with SSO enabled, [contact sales](https://cursor.com/contact-sales?source=docs-scim) to get access.*

**Source:** https://cursor.com/docs/account/teams/scim

#### Overview

SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider. Available on Enterprise plans with SSO enabled, [contact sales](https://cursor.com/contact-sales?source=docs-scim) to get access.

If you also manage multiple linked teams, see [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md) for org-level cohorts and group controls.

#### Prerequisites

- Cursor Enterprise plan
- SSO must be configured first - **SCIM requires an active SSO connection**
- Admin access to your identity provider (Okta, Azure AD, etc.)
- Admin access to your Cursor organization

#### How it works

##### User provisioning

Users are automatically added to Cursor when assigned to the SCIM application in your identity provider. When unassigned, they're removed. Changes sync in real-time.

##### Directory groups

Directory groups and their membership sync from your identity provider. Group and user management must be done through your identity provider - Cursor displays this information as read-only.

##### Spend management

Set different per-user spend limits for each directory group. Directory group limits take precedence over team-level limits. Users in multiple groups receive the highest applicable spend limit.

#### Setup

##### Ensure SSO is configured

SCIM requires SSO to be set up first. If you haven't configured SSO yet,
follow the [SSO setup guide](https://cursor.com/docs/account/teams/sso.md) before proceeding.

##### Access Active Directory Management

Navigate to
[cursor.com/dashboard/members?subtab=active-directory](https://www.cursor.com/dashboard/members?subtab=active-directory)
with an admin account, or go to your dashboard settings and select the "Members
& Groups" tab followed by the "Directory Groups" subtab.

##### Start SCIM setup

Once SSO is verified, you'll see a link for step-by-step SCIM setup. Click
this to begin the configuration wizard.

##### Configure SCIM in your identity provider

In your identity provider: - Create or configure your SCIM application - Use
the SCIM endpoint and token provided by Cursor - Enable user and push group
provisioning - Test the connection

##### Configure spend limits (optional)

Back in Cursor's Active Directory Management page: - View your synchronized
directory groups - Set per-user spend limits for specific groups as needed -
Review which limits apply to users in multiple groups

##### Identity provider setup

For provider-specific setup instructions:

##### Identity Provider Guides

Setup instructions for Okta, Azure AD, Google Workspace, and more.

#### Managing users and groups

All user and group management must be done through your identity provider.
Changes made in your identity provider will automatically sync to Cursor, but
you cannot modify users or groups directly in Cursor.

##### User management

- Add users by assigning them to your SCIM application in your identity provider
- Remove users by unassigning them from the SCIM application
- User profile changes (name, email) sync automatically from your identity provider

##### Group management

- Directory groups are automatically synced from your identity provider
- Group membership changes are reflected in real-time
- Use groups to organize users and set different spend limits

##### Spend limits

- Set different per-user limits for each directory group
- Users inherit the highest spend limit from their groups
- Group limits override the default team-wide per-user limit

#### FAQ

##### Why isn't SCIM management showing up in my dashboard?

Ensure SSO is properly configured and working before setting up SCIM. SCIM requires an active SSO connection to function.

##### Why aren't users syncing?

Verify that users are assigned to the SCIM application in your identity provider. Users must be explicitly assigned to appear in Cursor.

##### Why aren't groups appearing?

Check that push group provisioning is enabled in your identity provider's SCIM settings. Group sync must be configured separately from user sync.

##### Why aren't spend limits applying?

Confirm users are properly assigned to the expected groups in your identity provider. Group membership determines which spend limits apply.

##### Can I manage SCIM users and groups directly in Cursor?

No. All user and group management must be done through your identity provider. Cursor displays this information as read-only.

##### How quickly do changes sync?

Changes made in your identity provider sync to Cursor in real-time. There may be a brief delay for large bulk operations.

##### Can I sync user roles from my IdP?

No. Currently, the SCIM integration doesn't support role mapping and all users are provisioned as Members. Any role updates need to be done in the Cursor dashboard.

##### Why are there users on my Members dashboard that aren't in the provisioned IdP groups?

When SCIM is set up, existing users are not automatically removed from Cursor. You can either remove them manually, or sync them with SCIM once and deprovision them from your IdP to have them removed from Cursor.

##### Why don't the users from my synced groups match the users on the Cursor Members dashboard?

Once a user account is provisioned, they won't appear on the Cursor Members Dashboard until they sign in for the first time.

##### SCIM is available on the Enterprise plan

Contact our team to request access.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Privacy and Data Governance

*Understanding how data flows through Cursor is critical for security reviews and compliance assessments. This documentation explains what data goes where, what guarantees you have, and where that data lives geographically.*

**Source:** https://cursor.com/docs/enterprise/privacy-and-data-governance

Understanding how data flows through Cursor is critical for security reviews and compliance assessments. This documentation explains what data goes where, what guarantees you have, and where that data lives geographically.

#### Two data flows

There are two ways data leaves your local environment when using Cursor:

##### 1. LLM requests

When you use AI features, we send prompts and code context to language model providers like OpenAI, Anthropic, and Google. If you are using Cursor's custom models (e.g. Composer), your data may also be processed by our inference providers. See our list of [sub-processors](https://trust.cursor.com/subprocessors).

**With Privacy Mode enabled** your code is never used for training by Cursor or other AI model providers.

Privacy Mode is on by default for Enterprise teams. See [Privacy Overview](https://cursor.com/privacy-overview) for details.

##### 2. Cloud Agents

Cloud Agents are the only feature that requires Cursor to store code. Unlike the indexing process or LLM requests, Cloud Agents need access to your repository over time to make changes.

**Architecture:**

- Agents run in isolated virtual machines
- Each agent has a dedicated environment
- Isolated from other agents and users

**What gets stored:**

- Encrypted copies of repositories that Cloud Agents work on
- Stored temporarily while the agent runs
- Deleted after the agent completes

Cloud Agents are optional. If your security policy prohibits code storage, don't enable Cloud Agents. You can still use all other Cursor features.

See [Cloud Agents](https://cursor.com/docs/cloud-agent.md) for details.

#### Models with data retention

Most models run under Cursor's ZDR agreements, so providers don't store inputs or outputs or train on your data ([read more](https://cursor.com/data-use) about our data use policies). A few models require data retention with the provider and fall outside these agreements. For Enterprise customers, Teams with Privacy Mode enabled, and individual customers with Privacy Mode enabled, Cursor requires admin approval before use.

[Claude Fable 5](https://cursor.com/docs/models/claude-fable-5.md) works this way. Anthropic stores its inputs and outputs to run automatic and human harm-prevention reviews. This data is not used for training or product improvement. For Enterprise customers and customers with Privacy Mode enabled, requests to Fable 5 fail until the model's data retention policy is approved from the [dashboard](https://cursor.com/dashboard/restricted_models/claude-fable-5). Opting in applies to the whole team. Enterprise admins can still limit which user groups can select the model with [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

When a Fable 5 request trips one of its security guardrails, Cursor routes that request to Claude Opus automatically so your work continues.

#### Privacy Mode enforcement

Privacy Mode can be enabled at the team level to ensure all team members benefit from ZDR guarantees.

**Team-level enforcement:**

1. Go to your [team dashboard](https://cursor.com/dashboard)
2. Navigate to Settings
3. Enable Privacy Mode for the team
4. Optionally enforce it so members can't disable it

**MDM enforcement:**
For additional assurance, use the Allowed Team IDs policy. This prevents users from logging into personal accounts (which might not have Privacy Mode enabled) on corporate devices.

See [Identity and Access Management](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-team-ids) for policy details and [Deployment Patterns](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) for MDM configuration.

#### Compliance and contracts

Our [DPA](https://cursor.com/terms/dpa) includes comprehensive data protection commitments that follow industry standards, including data minimization, access control, and secure processing.

All [sub-processors](https://trust.cursor.com/subprocessors) are covered by appropriate data processing agreements.

#### Data encryption

Cursor encrypts data for all infrastructure, including:

- TLS 1.2+ in transit
- AES-256 at rest

For enhanced security control, enterprise customers can use Customer Managed Encryption Keys (CMEK) for encrypting data stored in Cursor's infrastructure.

With CMEK enabled:

- Embeddings are encrypted using your customer encryption key
- Cloud Agent data is encrypted using your customer encryption key
- You control key rotation and access
- Provides additional layer of security beyond standard encryption

[Contact sales](https://cursor.com/contact-sales?source=docs-cmek) to enable CMEK for your organization.

#### Data residency

Data residency controls let customers enrolled in the program manage where their code and data are processed and stored. When data residency is enabled for a team, model inference, data processing, and data storage for in-scope features stay in the selected region.

##### What data residency covers

Data residency applies across three independent layers for supported features and models:

| Layer               | Scope                                                                   |
| :------------------ | :---------------------------------------------------------------------- |
| **Inference**       | Model inference runs entirely in the selected region.                   |
| **Data processing** | Data pipelines that touch your content run only in the selected region. |
| **Data storage**    | Customer Data is stored only in the selected region, including backups. |

- Today, customers can enroll in **US-only data residency** (inference, processing, and storage in the US).
- EU + Iceland inference-only coverage is available on request. Broader EU support and additional regions are in active development.
- Contact your account executive if you are interested in either option.

##### US data residency

###### Model availability

Under US-only data residency, only the following model families run in-region:

- GPT (`gpt-*`)
- Claude 4.6 and above
- Gemini 2.5 Flash
- Composer
- Grok 4.5

Selecting a model that isn't eligible returns an error, and the model is unavailable while data residency is enabled. Auto will select from only models on this list.

###### What stays in-region

When US-only data residency is enabled for a team, the following stay on US-based infrastructure:

- Inference on inputs and suggestions for supported models
- Data processing pipelines that handle your content
- Storage of your Customer Data
- Use of Cloud Agents, including inference, processing, and storage
- Tab, editing, autocomplete, and semantic search

**Traveling users:** If a user on a US-only team is abroad, their requests still route to US-only infrastructure. This may add latency.

###### Pricing

US-only data residency incurs a 10% uplift on Model pricing for eligible Models.

###### How to enable

US-only data residency is available to Enterprise customers and is enabled per team. Enablement is handled by your account team while self-serve controls are built out; plan for up to two weeks from the time the request comes in. Contact your account team to enroll a team.

###### FAQ

##### Does US-only data residency apply to my whole organization?

It's enabled per team, so you can scope it to the teams that need it.

##### Does it cover Cloud Agents?

Yes. Inference, processing, and storage for Cloud Agents can be US-only today.

##### What happens if a user travels outside the US?

Their requests still route to US-only infrastructure. Expect some added latency, but the US-only guarantee is preserved.

##### Can I use any model I want?

No. Only the eligible model families listed under Model availability are supported. Choosing an unsupported model returns an error while US-only data residency is active.

##### What might leave the region?

Some functionality depends on external services or on infrastructure Cursor doesn't control, so US data residency can't be provided for it:

- **SSO / authentication** — Routes through Cursor's identity provider (WorkOS) regardless of region.
- **Codebase indexing** — If your codebase is stored outside of the US, we cannot guarantee US-only indexing.
- **Bring your own key (BYOK)** — US data residency is not supported for BYOK.
- **Custom models** — A custom model reached via an OpenAI-compatible base URL override or a third-party gateway carries the region of that gateway or model, which may not be in the US.
- **MCPs and external integrations** — `@Web`, `@Docs`, and user-configured MCPs or connectors are separate services, each with its own region.
- **Bugbot / code review** — Runs against your repository's infrastructure, so its region depends on where your repositories are located.
- **Shared links** — If a link is shared outside a US-only team, US-only residency can't be guaranteed for the recipient.
- **Slack- or web-triggered Cloud Agents** — The region of the issuing command can't be guaranteed.

##### Is data residency available outside the US?

US-only data residency is available today. Coverage for the EU/EEA and APAC is in active development. Please reach out to your account manager for more information.

##### Enterprise privacy and data controls

Contact our team to learn about data residency, CMEK, Privacy Mode enforcement, and more.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Network Configuration

*Cursor needs to communicate with backend services and AI providers. This documentation covers how to configure Cursor to work within your network infrastructure, including proxies, firewalls, and encryption requirements.*

**Source:** https://cursor.com/docs/enterprise/network-configuration

Cursor needs to communicate with backend services and AI providers. This documentation covers how to configure Cursor to work within your network infrastructure, including proxies, firewalls, and encryption requirements.

#### Proxy configuration

Many enterprises route traffic through proxy servers for monitoring and security. Cursor works with most proxy configurations, but some proxy settings can cause issues with streaming responses.

##### HTTP/2 vs HTTP/1.1

Cursor uses HTTP/2 bidirectional streaming by default for real-time chat and agent experiences. Some enterprise proxies don't support HTTP/2 streaming correctly. Zscaler is the most widely used proxy with this limitation.

If you experience issues with streaming, Cursor automatically falls back to HTTP/1.1 Server-Sent Events (SSE) mode. This fallback was specifically designed to work with Zscaler and similar proxies that buffer or break HTTP/2 streams. The fallback happens transparently when HTTP/2 bidirectional streaming doesn't work.

##### SSL inspection and DLP

Many corporate proxies perform SSL man-in-the-middle inspection to scan traffic for security threats or data loss prevention (DLP). This replaces Cursor's SSL certificates with your proxy's certificates.

When Cursor traffic goes through Secure Web Gateways (SWG), SSL inspection, or DLP, it often causes timeouts, slowness, or errors when using Cursor's Agent capabilities. This is one of the most common deployment blockers for enterprise customers. For endpoint security software (AV, EDR, DLP) that runs on the machine itself rather than at the network level, see [Endpoint Security Configuration](https://cursor.com/docs/enterprise/endpoint-security.md).

Cursor's services are already encrypted end-to-end. We recommend disabling SSL inspection for these domains:

- `.cursor.sh`
- `cursor-cdn.com`
- `marketplace.cursorapi.com`
- `authenticate.cursor.sh`
- `authenticator.cursor.sh`
- `*.cursorvm.com`
- `*.*.cursorvm.com`

If your security policy requires SSL inspection on all traffic, your proxy must support:

- HTTP/2 bidirectional streaming (or that Cursor's HTTP/1.1 fallback works)
- Server-Sent Events (SSE) passthrough without buffering
- Long-running connections without forced timeouts
- Disabling response buffering for streaming content types

##### Testing proxy connectivity

If you experience connection issues, you can test connectivity manually using curl commands. These commands simulate the requests Cursor makes to backend services.

**Test basic connectivity:**

```bash
curl -v https://api2.cursor.sh |& grep -C1 issuer:
```

This shows which SSL certificate is in use. You should see Amazon RSA. If you see your proxy provider (like Zscaler), SSL inspection is active.

**Test HTTP/1.1 streaming:**

```bash
echo -ne "\x0\x0\x0\x0\x11{\"payload\":\"foo\"}" | \
  curl --http1.1 -No - -XPOST \
  -H "Content-Type: application/connect+json" \
  --data-binary @- \
  https://api2.cursor.sh/aiserver.v1.HealthService/StreamSSE
```

You should see output appear line by line over 5 seconds. If it appears all at once after 5 seconds, your proxy is buffering streaming responses.

**Test HTTP/2 bidirectional streaming:**

```bash
(for i in 1 2 3 4 5; do \
  echo -ne "\x0\x0\x0\x0\x12{\"payload\":\"foo$i\"}"; \
  sleep 1; \
done) | curl -No - -XPOST \
  -H "Content-Type: application/connect+json" \
  -T - \
  https://api2.cursor.sh/aiserver.v1.HealthService/StreamBidi
```

Output should appear once per second. If buffered for 5 seconds, your proxy doesn't support HTTP/2 bidirectional streaming.

#### IP allowlisting

If your network uses IP-based access controls, you need to allow traffic to Cursor's backend services.

Rather than maintaining IP address lists (which can change), configure your firewall to allow traffic to these domain patterns:

- `*.cursor.sh`
- `*.cursor-cdn.com`
- `*.cursorapi.com`
- `*.cursorvm.com`
- `*.*.cursorvm.com`

We generally recommend allowlisting with the domain patterns above. However, if your firewall mandates granular subdomain allowlists without wildcards, use the following list:

- `api2.cursor.sh`: Used for most API requests.
- `api5.cursor.sh`: Used for Cursor's agent requests.
- `api3.cursor.sh`: Used for Cursor Tab requests (HTTP/2 only).
- `repo42.cursor.sh`: Used for codebase indexing (HTTP/2 only).
- `api4.cursor.sh`, `us-asia.gcpp.cursor.sh`, `us-eu.gcpp.cursor.sh`, `us-only.gcpp.cursor.sh`: Used for Cursor Tab requests depending on your location (HTTP/2 only).
- `adminportal42.cursor.sh`: Used to configure SSO and domain verification.
- `marketplace.cursorapi.com`, `cursor-cdn.com`, `downloads.cursor.com`, `anysphere-binaries.s3.us-east-1.amazonaws.com`: Used for client updates and downloading extensions from the extension marketplace.
- `api5.cursor.sh`: Used for network access layer (NAL) requests. These subdomains are also used:
  - `agent.api5.cursor.sh`
  - `agentn.api5.cursor.sh`
  - `agent.us.api5.cursor.sh`
  - `agentn.us.api5.cursor.sh`
  - `agent.global.api5.cursor.sh`
  - `agentn.global.api5.cursor.sh`
- `authenticate.cursor.sh`: Authorization endpoint.
- `authenticator.cursor.sh`: Auth UI and login webview.
- `prod.authentication.cursor.sh`: Production token issuer.
- `authentication.cursor.sh`: JWT issuer (backend).

#### Private connectivity

Cursor supports [private connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) for Enterprise teams that need Cloud Agents, Bugbot, or Cursor backend services to access private source control systems. Supported options include AWS PrivateLink and Cloudflare Tunnel.

Cursor does not currently offer VPC peering or customer-facing Google Private Service Connect.

When you run Cursor agents in the editor or via the CLI, they inherit your existing network configuration. If you run Cursor on a machine within your VPC, agent operations inherit:

- Your network security groups
- Your firewall rules
- Your DNS configuration
- Your VPN or private network access

This means Cursor agents can access internal resources that the machine can reach, while following your existing network security controls.

#### Encryption

Cursor encrypts data both in transit and at rest.

##### In transit

- TLS 1.2 or higher for all connections to Cursor services
- TLS for connections to third-party AI providers
- Certificate pinning for critical services

##### At rest

- AES-256 encryption for stored data
- Encrypted vector database storage
- Encrypted code storage for Cloud Agents (when enabled)

##### Key management

Cursor manages encryption keys. Keys are rotated according to security best practices and stored in secure key management systems.

For enhanced security control, enterprise customers can use Customer Managed Encryption Keys (CMEK) for encrypting data stored in Cursor's infrastructure. See [Data Encryption](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#data-encryption) for details.

#### LLM gateways

Some enterprises want to route LLM traffic through their own gateways for additional monitoring and control.

Custom gateways can introduce additional latency, rate limiting, and compatibility issues. We instead recommend using Cursor's built-in hooks feature to implement your own security controls.

Cursor's [Zero Data Retention policy](https://cursor.com/docs/account/teams/dashboard.md#privacy-settings) does not apply when using your own API keys. Your data handling will be subject to the privacy policies of your chosen AI provider (OpenAI, Anthropic, Google, Azure, or AWS).

See [Hooks](https://cursor.com/docs/hooks.md) and [Security Guardrails](https://cursor.com/docs/enterprise/llm-safety-and-controls.md) for details.

#### Cloud Agents networking

Cloud Agents run on Cursor's infrastructure, not your local network. They can access:

- Public GitHub repositories
- GitHub Enterprise Cloud repositories you've granted access to
- GitHub Enterprise Server (self-hosted GitHub Enterprise)
- On-prem and cloud-based GitLab
- Bitbucket Cloud repositories
- Public package registries (npm, PyPI, etc.)

Cloud Agents cannot access:

- Resources behind your corporate firewall
- On-premises GitHub Enterprise Server
- Private package registries without internet access

If your development workflow requires access to internal resources, use the Cursor editor on machines within your network instead of Cloud Agents.

#### Troubleshooting checklist

If you experience connection issues:

1. **Test basic connectivity** to `api2.cursor.sh`
2. **Check if SSL inspection is active** and consider excluding Cursor domains
3. **Verify streaming works** using the curl tests above
4. **Check firewall rules** allow traffic to `*.cursor.sh` and related domains
5. **Review proxy logs** for connection errors or timeouts
6. **Test from a machine outside your network** to isolate network-specific issues

Most connectivity issues stem from proxies buffering streaming responses. Work with your network team to disable buffering for Cursor domains or implement proper streaming support.

##### Need help with enterprise network setup?

Contact our team for deployment assistance and priority support.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Private Connectivity

*Cursor supports private network connectivity for Enterprise teams that need Cursor to work with systems that are not reachable from the public internet. This includes self-hosted GitHub Enterprise Server, GitLab Enterprise, Bitbucket Data Center, private source control APIs, and webhook traffic from those systems back to Cursor.*

**Source:** https://cursor.com/docs/enterprise/private-connectivity

Cursor supports private network connectivity for Enterprise teams that need Cursor to work with systems that are not reachable from the public internet. This includes self-hosted GitHub Enterprise Server, GitLab Enterprise, Bitbucket Data Center, private source control APIs, and webhook traffic from those systems back to Cursor.

The same private connectivity setup is used across Cursor services that need access to your source control system, including [Cloud Agents](https://cursor.com/docs/cloud-agent.md), [Bugbot](https://cursor.com/docs/bugbot.md), and Cursor backend services.

To set up private connectivity, contact [hi@cursor.com](mailto:hi@cursor.com) or your Cursor sales representative.

#### Supported options

| Option            | Best for                                                                                            | Cloud provider                             | Status    |
| :---------------- | :-------------------------------------------------------------------------------------------------- | :----------------------------------------- | :-------- |
| AWS PrivateLink   | Private connectivity between Cursor and your Git provider, including webhook traffic back to Cursor | AWS                                        | Supported |
| Cloudflare Tunnel | Cursor accessing a private origin when AWS PrivateLink is not practical                             | Any environment that can run `cloudflared` | Supported |

#### How to choose

Use AWS PrivateLink when your private Git provider is in AWS or can sit behind an AWS Network Load Balancer. This is the preferred path for self-hosted GitHub Enterprise Server and GitLab Enterprise.

AWS PrivateLink can cover two traffic directions:

- Cursor accessing your private Git provider to clone repositories and call Git APIs.
- Your Git provider sending webhooks or callbacks to Cursor over `api2.cursor.sh` without public internet egress.

Use Cloudflare Tunnel when you cannot publish an AWS endpoint service or when you need a deployment model that only requires an outbound tunnel from your network.

If your team requires Google Private Service Connect (PSC), contact Cursor. Cursor does not currently offer a customer-facing PSC service.

#### Prerequisites

Before starting, make sure you have:

- A Cursor Enterprise workspace
- A self-hosted GitHub Enterprise Server or GitLab Enterprise instance reachable over HTTPS on port 443
- A publicly trusted TLS certificate for the Git hostname
- DNS ownership for the Git hostname
- AWS permissions to create endpoint services or interface VPC endpoints, if using AWS PrivateLink
- Permission to run `cloudflared`, if using Cloudflare Tunnel

Cursor does not support self-signed certificates, unencrypted connections, SSH, custom ports, or IPv6-only endpoint services for these private connectivity paths.

If you run a proxy in front of GitHub Enterprise Server, make sure it allows Cursor's GitHub App integration to use authenticated GitHub REST and GraphQL APIs.

#### AWS PrivateLink

AWS PrivateLink supports private traffic in either direction between Cursor and your Git provider. You may need one direction or both, depending on your network policy.

##### Direction 1: Cursor to your Git provider

Use this option when Cursor needs to clone repositories or call APIs on your private GitHub Enterprise Server or GitLab Enterprise host.

###### 1. Create an AWS endpoint service

Create a Network Load Balancer in front of your Git provider's HTTPS endpoint. Publish that load balancer as an AWS VPC endpoint service.

Send Cursor:

- Endpoint service name, for example `com.amazonaws.vpce.us-east-1.vpce-svc-0123456789abcdef0`
- AWS region
- Git hostname, for example `github.example.com`
- Whether your endpoint service has AWS-managed private DNS enabled
- Whether your Network Load Balancer preserves client IPs or your backend filters source IPs

If your endpoint service is outside `us-east-1`, enable cross-region access on the endpoint service.

###### 2. Allow Cursor's AWS principal

Cursor will provide the AWS principal to add to your endpoint service allowed principals. Add the exact principal Cursor provides:

```text
arn:aws:iam::<cursor-aws-account-id>:role/<cursor-provided-role>
```

Cursor cannot create its interface endpoint until this principal is allowed. If the principal is missing or does not match exactly, AWS returns `InvalidServiceName`.

If your load balancer preserves client IPs, or if your backend filters source IPs, allow these Cursor PrivateLink subnet CIDRs:

```text
10.2.8.0/21
10.2.24.0/21
10.2.40.0/21
```

###### 3. Accept the endpoint connection

After Cursor creates the interface endpoint, accept the endpoint connection in your AWS account if your endpoint service requires manual acceptance.

###### 4. Configure DNS

If your endpoint service exposes AWS-managed private DNS for your Git hostname, Cursor enables private DNS on its interface endpoint.

If your endpoint service does not expose private DNS, Cursor creates private DNS on its side and maps your Git hostname to the endpoint DNS name.

Use the same hostname in Cursor that appears on the TLS certificate and in DNS.

##### Direction 2: Your Git provider to `api2.cursor.sh`

Use this option when your GitHub Enterprise Server or GitLab Enterprise host cannot reach the public internet but still needs to send webhooks or callbacks to Cursor.

Cursor publishes an AWS PrivateLink endpoint service for `api2.cursor.sh`. You create an interface VPC endpoint in your AWS account and enable private DNS so `api2.cursor.sh` resolves to private endpoint IPs from your Git provider network.

###### Endpoint service details

Cursor will confirm your AWS principal is allowlisted before you create the endpoint.

| Field                      | Value                                                                                |
| :------------------------- | :----------------------------------------------------------------------------------- |
| Service name               | `com.amazonaws.vpce.us-east-1.vpce-svc-054b15427d4bea2b7`                            |
| Service ID                 | `vpce-svc-054b15427d4bea2b7`                                                         |
| Home region                | `us-east-1`                                                                          |
| Supported consumer regions | `us-east-1`, `us-east-2`, `us-west-2`, `eu-central-1`, `eu-west-1`, `ap-southeast-2` |
| IP address types           | IPv4 only                                                                            |
| Private DNS name           | `api2.cursor.sh`                                                                     |

###### Mode 1: AWS-managed private DNS

This is the recommended mode. Set `private_dns_enabled = true`.

```hcl
resource "aws_vpc_endpoint" "cursor_api2" {
  vpc_id              = aws_vpc.app.id
  service_name        = "com.amazonaws.vpce.us-east-1.vpce-svc-054b15427d4bea2b7"
  service_region      = "us-east-1"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = [for subnet in aws_subnet.app_private : subnet.id]
  private_dns_enabled = true
  security_group_ids  = [aws_security_group.cursor_api2_endpoint.id]
}
```

AWS associates your VPC with the managed private hosted zone for `api2.cursor.sh`. Inside the VPC, `api2.cursor.sh` resolves to the endpoint ENI IPs. No Route 53 record is required.

###### Mode 2: Customer-managed private hosted zone

Use this mode if you want to own the DNS record. Set `private_dns_enabled = false`, then create a private hosted zone for `api2.cursor.sh` scoped to the consumer VPC.

```hcl
resource "aws_vpc_endpoint" "cursor_api2" {
  vpc_id              = aws_vpc.app.id
  service_name        = "com.amazonaws.vpce.us-east-1.vpce-svc-054b15427d4bea2b7"
  service_region      = "us-east-1"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = [for subnet in aws_subnet.app_private : subnet.id]
  private_dns_enabled = false
  security_group_ids  = [aws_security_group.cursor_api2_endpoint.id]
}

resource "aws_route53_zone" "cursor_api2" {
  name    = "api2.cursor.sh"
  comment = "Customer-managed PHZ for api2.cursor.sh scoped to the app VPC."

  vpc {
    vpc_id = aws_vpc.app.id
  }
}

resource "aws_route53_record" "cursor_api2_a" {
  zone_id = aws_route53_zone.cursor_api2.zone_id
  name    = "api2.cursor.sh"
  type    = "A"

  alias {
    name                   = aws_vpc_endpoint.cursor_api2.dns_entry[0].dns_name
    zone_id                = aws_vpc_endpoint.cursor_api2.dns_entry[0].hosted_zone_id
    evaluate_target_health = false
  }
}
```

If GitHub Enterprise Server or GitLab Enterprise uses DNS outside the endpoint VPC, forward `api2.cursor.sh` queries to the VPC resolver or create an equivalent private DNS override. Do not create a public DNS override.

#### Cloudflare Tunnel

Use Cloudflare Tunnel when AWS PrivateLink is not a fit.

Cursor creates the tunnel and shares:

- A public hostname under Cursor-controlled DNS
- A tunnel token through a secure 1Password share
- A sample `cloudflared` configuration

Your network runs `cloudflared` and opens outbound connections to Cloudflare. No inbound firewall rule is required.

Example `cloudflared` configuration:

```yaml
ingress:
  - hostname: <cursor-provided-hostname>
    service: https://<your-internal-service>:443
  - service: http_status:404
```

Example run command:

```bash
docker run -d --restart=always --name cloudflared \
  -v /path/to/config.yml:/etc/cloudflared/config.yml \
  cloudflare/cloudflared:latest \
  tunnel --config /etc/cloudflared/config.yml \
  run --token <TUNNEL_TOKEN>
```

Keep the tunnel token secret. Do not send it through email or chat.

#### Complete the source control connection

After private networking is configured, complete the source control setup in Cursor:

- For GitHub Enterprise Server, follow the [GitHub integration setup](https://cursor.com/docs/integrations/github.md#setup).
- For GitLab Enterprise, follow the [GitLab integration setup](https://cursor.com/docs/integrations/gitlab.md#setup).
- For Bitbucket Data Center, follow the [Bitbucket integration setup](https://cursor.com/docs/integrations/bitbucket.md#setup).
- Use the same hostname that is covered by your TLS certificate and private DNS configuration.
- If a proxy sits in front of your Git provider, make sure it allows the authenticated API traffic described in [Prerequisites](https://cursor.com/docs/enterprise/private-connectivity.md#prerequisites).

Cursor uses the connected source control integration for Cloud Agents, Bugbot, and other Cursor services that need repository access.

##### Check the private webhook path

If your Git provider sends webhooks to Cursor through the `api2.cursor.sh` PrivateLink path, run these checks from the same network path used by GitHub Enterprise Server or GitLab Enterprise:

```bash
getent hosts api2.cursor.sh
# or, if dig is available
dig +short api2.cursor.sh
curl -sS https://api2.cursor.sh/
```

Every resolved IP should be inside your consumer VPC CIDR. If you see public IPs such as `3.x.x.x` or `44.x.x.x`, private DNS is not in effect.

The `curl` request should return HTTP `200` with a body that starts with `Welcome to Cursor.` That response means the request reached a live Cursor `api2` backend.

#### Troubleshooting

| Symptom                                                                                            | Likely cause                                                                                        | Fix                                                                                                                                       |
| :------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Cursor cannot complete the private connection to your Git provider                                 | Cursor cannot reach or attach to the endpoint service                                               | Confirm the endpoint service name, region, and allowed principal match the values Cursor provided, then contact Cursor with the timestamp |
| Cursor reports that the endpoint connection is waiting for customer action                         | The endpoint service requires approval in your AWS account                                          | Review pending endpoint connection requests for the service and approve the Cursor request                                                |
| Bugbot or Cloud Agents connect to GHES but fail during app setup, repo sync, or webhook processing | A proxy in front of GHES is blocking or rewriting authenticated GitHub REST or GraphQL API requests | Allow Cursor's GitHub App integration to use authenticated GitHub REST and GraphQL APIs                                                   |
| `api2.cursor.sh` resolves to public IPs                                                            | Private DNS is not in the resolver path used by GitHub Enterprise Server or GitLab Enterprise       | Enable AWS-managed private DNS, or forward DNS to the endpoint VPC resolver                                                               |
| TCP to `api2.cursor.sh:443` times out                                                              | Security group, NACL, route table, or firewall blocks traffic to endpoint ENIs                      | Allow TCP 443 from your Git provider network to the endpoint ENIs                                                                         |
| TLS fails for `api2.cursor.sh`                                                                     | DNS points to the wrong target or the client is not using SNI                                       | Check endpoint DNS and retry with SNI enabled                                                                                             |
| `curl https://api2.cursor.sh/` does not return `Welcome to Cursor.`                                | Traffic is not reaching a healthy Cursor backend                                                    | Send Cursor the timestamp, source VPC, and resolved endpoint IPs                                                                          |
| Cloudflare Tunnel does not connect                                                                 | `cloudflared` cannot reach Cloudflare or the token/config is wrong                                  | Check outbound firewall rules, token, and `cloudflared` logs                                                                              |

#### Google Private Service Connect

Cursor does not currently offer customer-facing Google Private Service Connect.

If you need private connectivity from a GCP VPC to Cursor services, or from Cursor to a private service in your GCP project, contact Cursor so we can scope the requirement. Today, use AWS PrivateLink or Cloudflare Tunnel when those deployment models fit.

#### What to send Cursor

For AWS PrivateLink to your Git provider:

- Endpoint service name
- AWS region
- Git hostname
- Whether private DNS is enabled
- Whether your load balancer preserves client IPs or filters source IPs

For `api2.cursor.sh` over AWS PrivateLink:

- AWS principal Cursor should allowlist
- VPC and region where you will create the interface endpoint
- Whether you plan to use AWS-managed private DNS or customer-managed DNS

For Cloudflare Tunnel:

- Internal origin URL
- Customer contacts for the secure 1Password share
- Any hostname or naming restrictions

#### Further reading

- [AWS: Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html)
- [AWS: Manage DNS names for VPC endpoint services](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html)
- [AWS: Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)
- [Cloudflare Tunnel documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Endpoint Security Configuration

*Cursor loads JavaScript modules and performs file I/O during startup. Endpoint security software that intercepts file operations or injects into processes can slow startup past internal timeouts, causing features like Agent to fail. This page covers how to configure exclusions so Cursor works alongside your security stack.*

**Source:** https://cursor.com/docs/enterprise/endpoint-security

Cursor loads JavaScript modules and performs file I/O during startup. Endpoint security software that intercepts file operations or injects into processes can slow startup past internal timeouts, causing features like Agent to fail. This page covers how to configure exclusions so Cursor works alongside your security stack.

#### What to exclude

Add the following processes and paths to your security product's exclusion list.

##### Windows

**Processes:** each process has a user install path and a system install path. Add the path that matches your install type.

| Process            | Install type | Path                                                                                             |
| ------------------ | ------------ | ------------------------------------------------------------------------------------------------ |
| `Cursor.exe`       | User         | `%LOCALAPPDATA%\Programs\cursor\Cursor.exe`                                                      |
| `Cursor.exe`       | System       | `%ProgramFiles%\cursor\Cursor.exe`                                                               |
| `rg.exe`           | User         | `%LOCALAPPDATA%\Programs\cursor\resources\app\node_modules\@vscode\ripgrep\bin\rg.exe`           |
| `rg.exe`           | System       | `%ProgramFiles%\cursor\resources\app\node_modules\@vscode\ripgrep\bin\rg.exe`                    |
| `inno_updater.exe` | User         | `%LOCALAPPDATA%\Programs\cursor\resources\app\node_modules\cursor-inno-updater\inno_updater.exe` |
| `inno_updater.exe` | System       | `%ProgramFiles%\cursor\resources\app\node_modules\cursor-inno-updater\inno_updater.exe`          |

**Paths:**

| Path                              | Description                                               |
| --------------------------------- | --------------------------------------------------------- |
| `%LOCALAPPDATA%\Programs\cursor\` | Application binaries and bundled modules (user install)   |
| `%ProgramFiles%\cursor\`          | Application binaries and bundled modules (system install) |
| `%APPDATA%\Cursor\`               | User data, settings, and workspace storage                |

##### macOS

**Processes:** `Cursor.app`

**Paths:**

| Path                        | Description        |
| --------------------------- | ------------------ |
| `/Applications/Cursor.app/` | Application bundle |

#### Why exclusions may be needed

Cursor's extension host reads JavaScript files from its own install directory at startup. When security software adds per-file scanning latency, the cumulative delay can exceed Cursor's startup timeout.

This primarily affects startup. Once modules are loaded into memory, ongoing file operations are infrequent and unlikely to cause issues.

Cursor's own files are code-signed binaries and bundled JavaScript, not user-generated content. Excluding them from real-time scanning is low-risk and does not reduce protection for user files or network traffic.

Both **process exclusions** and **path exclusions** may be needed. Some products use kernel-level minifilter drivers that scan all file I/O regardless of which process is reading. A process-only exclusion may not be sufficient — add path exclusions for the Cursor install directory as well.

#### Identifying active security software

These commands can help identify which products are running so you know where you may need to configure exclusions. On Windows, run in an **Administrator PowerShell** window:

```powershell
# Registered AV products
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct |
  Select-Object displayName, pathToSignedProductExe

# Kernel-level filesystem filter drivers
fltmc

# Check for EDR process injection via environment variables
[System.Environment]::GetEnvironmentVariables() |
  Where-Object { $_.Keys -match "BPP|COR_PROFILER|COMPLUS|__COMPAT" }

# Windows Defender status
Get-MpComputerStatus |
  Select-Object IsTamperProtected, RealTimeProtectionEnabled, AMRunningMode
```

**How to read `fltmc` output:** Standard Windows drivers you can ignore include `WdFilter`, `storqosflt`, `wcifs`, `CldFlt`, `bfs`, `FileCrypt`, `luafv`, `Wof`, `FileInfo`, `npsvctrig`, `bindflt`, and `UnionFS`. Other drivers are likely from third-party security software.

**How to read the environment variable output:** If it returns any results, an EDR product is injecting code into every new process on the machine, and an exclusion may be necessary.

#### Verifying exclusions are working

After applying exclusions, restart Cursor and verify that Agent features work without timing out. If you previously saw empty Extension Host logs (Cmd/Ctrl+Shift+P → "Output" → "Extension Host"), they should now show normal startup output.

#### Troubleshooting checklist

1. Run the [identification commands above](https://cursor.com/docs/enterprise/endpoint-security.md#identifying-active-security-software) to determine which security products are running
2. Add both process and path exclusions for the identified products in their management consoles
3. Restart Cursor and test Agent — this is the definitive test of whether exclusions are working
4. If exclusions don't resolve the issue, [export logs](https://cursor.com/help/troubleshooting/agent-issues.md#what-if-i-see-agent-execution-timed-out) and contact Cursor support with the diagnostic output\`


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### LLM Safety and Controls

*AI models can behave unexpectedly. This documentation covers how to control what agents can do, set up safety guardrails, and guide LLM behavior toward desired outcomes.*

**Source:** https://cursor.com/docs/enterprise/llm-safety-and-controls

AI models can behave unexpectedly. This documentation covers how to control what agents can do, set up safety guardrails, and guide LLM behavior toward desired outcomes.

#### Understanding model behavior

LLMs generate text based on probability distributions, not by retrieving facts from a database or executing deterministic logic. They can produce different outputs for the same input, hallucinate facts or code that seems plausible but is wrong, and be influenced by carefully crafted prompts (prompt injection).

You can't rely on LLMs to always make safe decisions. Instead, you combine two approaches: **security controls** that enforce hard boundaries on what agents can do, and **steering mechanisms** that guide LLM behavior toward better outcomes.

For a deeper understanding of how LLMs work, see [How AI Models Work](https://cursor.com/learn/how-ai-models-work.md).

#### Two approaches to safety

Cursor provides two complementary approaches to managing AI agent behavior:

**Security controls (deterministic enforcement)**: Hard boundaries that block dangerous operations regardless of what the LLM suggests. These include terminal command restrictions, enforcement hooks that reject operations, approval workflows, and sandboxing. Security controls are your primary defense against harmful agent actions.

**LLM steering (non-deterministic guidance)**: Mechanisms that guide the LLM toward better behavior by shaping its context and available actions. These include Rules that add instructions to prompts, Commands that provide reusable workflows, and integrations that enrich the agent's knowledge. Steering improves agent quality but doesn't guarantee prevention of harmful actions.

Use both approaches together. Security controls provide the safety net. Steering reduces how often agents attempt problematic actions in the first place.

#### Security controls

These deterministic controls enforce hard boundaries on what agents can do. They work regardless of what the LLM suggests.

##### Terminal command restrictions

By default, Cursor requires your approval before executing any terminal command. This protects against destructive commands (deleting files, dropping databases), commands that expose sensitive data, and commands with unintended side effects.

When an agent wants to run a command, you see a prompt showing the full command. You can approve and run it, deny it, or modify it before running.

###### Auto-approval risks

You can enable auto-approval for terminal commands, but understand the risks. Agents might run destructive commands without your knowledge, commands execute before you can review them, and bugs or prompt injection could cause unintended operations.

###### Run Mode configuration

Enterprise teams can configure Run Mode policies in the team dashboard. In Cursor 3.6 and above, end users choose between **Auto-review** (the default), **Allowlist**, and **Run Everything** modes. **Auto-review** runs allowlisted calls, sandboxes shell commands when it can, and routes the rest through an LLM classifier that returns allow or block based on safety and how well the call matches the user's intent. You can create an allowlist of commands that don't require approval, such as `npm install`, `pip install`, `cargo build`, or `make test`.

The allowlist is best-effort, not a security boundary. Determined agents or prompt injection might bypass it. Always combine allowlists with other security controls like hooks.

See [Run Modes](https://cursor.com/docs/agent/security/run-modes.md#run-mode) and [Agent Security](https://cursor.com/docs/agent/security.md) for details.

##### Enforcement hooks

Hooks let you run custom logic at key points in the agent loop.

- Before prompt submission: Scan prompts for sensitive data before they're sent to LLMs. Block submissions that contain API keys or credentials, personal identifiable information (PII), or proprietary information.
- Before file reading: Scan files before agents read them. Redact or block access to configuration files with secrets, PII in databases or logs, or proprietary algorithms.
- After code generation: Scan generated code before it's written to disk. Check for security vulnerabilities (SQL injection, XSS), licensed code that might cause IP issues, or API keys and credentials in code.
- Before terminal execution: Block dangerous commands or route them through approval workflows. For example, block all `git push` commands, require approval for any `sudo` command, or block database `DROP` statements.

###### Example: Blocking git commands

This hook intercepts shell commands and blocks raw git usage, directing users to the GitHub CLI instead:

```bash
#!/bin/bash
input=$(cat)
command=$(echo "$input" | jq -r '.command')

if [[ "$command" =~ git[[:space:]] ]]; then
    cat << EOF
{
  "permission": "deny",
  "userMessage": "Git command blocked. Please use gh tool instead.",
  "agentMessage": "Use 'gh' commands instead of raw git."
}
EOF
fi
```

###### Example: Redacting secrets

This hook scans file contents for GitHub API keys and blocks access if found:

```bash
#!/bin/bash
input=$(cat)
content=$(echo "$input" | jq -r '.content')

if echo "$content" | grep -qE 'gh[ps]_[A-Za-z0-9]{36}'; then
    cat << EOF
{
  "permission": "deny"
}
EOF
    exit 3
fi
```

See [Hooks](https://cursor.com/docs/hooks.md) for complete documentation and more examples.

##### Protecting sensitive files

Not all files in your repositories should be accessible to AI. Configuration files, secrets, and sensitive data need protection.

###### .cursorignore

The `.cursorignore` file works like `.gitignore` but controls what Cursor can access. Files matching patterns in `.cursorignore` are excluded from:

- Agent file reading
- Context selection

`.cursorignore` is not a security boundary. It's a convenience feature to exclude files from AI processing, but:

- Users can manually read ignored files
- Agents might find ways to access ignored content
- It doesn't prevent file access, only excludes from indexing

For true security, use file system permissions or encrypt sensitive data.

See [Ignore Files](https://cursor.com/docs/reference/ignore-file.md) for detailed syntax.

###### .cursor directory protection

The `.cursor` directory in repositories contains project-specific settings, rules, and cache files. Enterprise teams can prevent agents from modifying this directory.

When enabled, agents cannot:

- Modify files in `.cursor/`
- Delete the `.cursor/` directory
- Change cursor rules or settings files

Users can still manually edit these files, but agents require approval.

Configure in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) under ".cursor Directory Protection" (Enterprise only).

###### Browser origin controls

Enterprise teams can restrict which websites agents can navigate to when using the [browser tool](https://cursor.com/docs/agent/tools/browser.md). Define an allowlist of approved domains—agents attempting to visit other origins are blocked.

Configure in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) under "Browser Controls" (Enterprise only).

##### Integration with DLP tools

Many enterprises have existing Data Loss Prevention (DLP) tools that scan for sensitive data. You can integrate Cursor with your DLP tools in three ways.

###### Endpoint DLP agents

Most endpoint DLP software can inspect Cursor's network traffic. Configure your DLP to monitor traffic to `*.cursor.sh` domains, scan for sensitive patterns in outbound requests, and block or alert on policy violations.

Network DLP may impact performance. See [Network Configuration](https://cursor.com/docs/enterprise/network-configuration.md) for proxy considerations.

###### Hooks-based DLP

Use Cursor's hooks feature to implement custom DLP logic:

**Before prompt submission:**
Scan prompts for sensitive patterns before sending to LLMs:

```bash
#!/bin/bash
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')

# Check for API keys
if echo "$prompt" | grep -qE 'api[_-]?key.*[A-Za-z0-9]{32}'; then
    cat << EOF
{
  "continue": false,
  "userMessage": "Prompt contains what looks like an API key. Remove it and try again."
}
EOF
    exit 1
fi

# Allow if no sensitive data found
cat << EOF
{
  "continue": true
}
EOF
```

**After code generation:**
Scan generated code before it's written to disk:

```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.file_path')
edits=$(echo "$input" | jq -r '.edits[].new_string')

# Check for hardcoded credentials
if echo "$edits" | grep -qE 'password.*=.*["\047][^"\047]+["\047]'; then
    # Send to your DLP API for analysis
    curl -X POST "https://dlp.yourcompany.com/scan" \
      -H "Content-Type: application/json" \
      -d "{\"content\":\"$edits\",\"file\":\"$file_path\"}"
    
    # Check API response and act accordingly
fi
```

###### Third-party DLP integration

Call your existing DLP vendor's API from hooks:

```bash
#!/bin/bash
input=$(cat)
content=$(echo "$input" | jq -r '.content')

# Send to DLP API
response=$(curl -s -X POST "https://dlp-api.company.com/analyze" \
  -H "Authorization: Bearer $DLP_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"$content\"}")

# Parse response
is_allowed=$(echo "$response" | jq -r '.allowed')

if [ "$is_allowed" = "true" ]; then
    cat << EOF
{
  "permission": "allow"
}
EOF
else
    violation=$(echo "$response" | jq -r '.violation_type')
    cat << EOF
{
  "permission": "deny",
  "userMessage": "Content blocked by DLP policy: $violation"
}
EOF
fi
```

This approach gives you centralized DLP policy management across all development tools.

##### Approval workflows

You can configure Cursor to ask for approval on every agent action. Users can set their agent to always ask before reading files, editing files, running terminal commands, or making network requests.

However, this approach significantly slows down the development experience. Agents need multiple actions to complete tasks, and requiring approval for each action makes the workflow tedious. Most teams instead choose to use hooks to block dangerous operations automatically.

##### Model provider safety

All model providers (OpenAI, Anthropic, Google, SpaceXAI) implement safety systems that filter harmful content. These systems reject prompts requesting harmful information, refuse to generate dangerous code, and filter outputs for safety.

Cursor works with providers to ensure models meet safety standards before deployment to users. Providers continuously evaluate models for safety issues. However, these are not security boundaries. Safety systems can be bypassed or tricked. Always implement your own controls through hooks and access policies.

##### Sandboxing considerations

Cursor agents run on your local machine by default. They can read files you can read, write files you can write, execute commands you can execute, and access network resources you can access.

There is no security boundary between agents and your user account. If your account can delete files, agents can delete files (with approval by default).

###### Sandboxing options

If you need stronger isolation, run Cursor in a separate VM using Cloud Agents, use file system permissions to limit what the Cursor process can access, or run Cursor on a dedicated development machine with limited access to production systems.

For most enterprises, the built-in approval requirements and hooks provide sufficient control.

##### File system permissions

For further defense, use file system permissions to protect sensitive files:

**Restrict access to secret files:**

```bash
# Make secrets readable only by specific users
chmod 600 .env
chown app-user:app-user .env

# Or use separate directories with restricted access
chmod 700 /etc/app/secrets
```

**Separate sensitive repos:**
Keep highly sensitive code in separate repositories with restricted access. Don't clone these repositories to machines where Cursor runs.

**Encrypted filesystems:**
For very sensitive data, use encrypted filesystems that require explicit mounting. Don't mount these filesystems in directories where Cursor has access.

#### LLM steering

Security controls block harmful actions after the LLM suggests them. Steering mechanisms guide the LLM to make better suggestions in the first place. These are non-deterministic. They improve outcomes but don't guarantee prevention.

##### Rules

Rules add instructions to the LLM's context window before every request. Use rules to establish coding standards, enforce architectural patterns, set security requirements, or define project-specific conventions.

Rules work at three scopes:

**User rules**: Apply to all projects for a specific user. Use these for personal preferences like code style or preferred libraries.

**Project rules**: Apply to everyone working on a project. Use these for project-specific standards like naming conventions or framework usage.

**Team rules**: Apply to all projects in your organization. Use these for company-wide standards like security requirements or compliance rules.

The LLM sees all applicable rules when generating responses. It will attempt to follow them, but rules are suggestions, not guarantees. Combine rules with enforcement hooks for requirements that must be followed.

See [Rules](https://cursor.com/docs/rules.md) for configuration and examples.

##### Commands and workflows

Commands package reusable prompts that agents can invoke with slash commands like `/test` or `/deploy`. Commands help standardize common workflows across your team.

**Workflows**: Create multi-step processes that guide agents through complex tasks. For example, a `/security-review` command might instruct the agent to scan for SQL injection, check for exposed secrets, validate input sanitization, and generate a security report.

**Prompt libraries**: Build a collection of tested prompts for common tasks. This reduces variation in agent behavior and captures institutional knowledge.

Commands are scoped to teams, projects, or users. Team admins can create organization-wide commands that appear for all developers.

See [Commands](https://cursor.com/help/customization/rules.md) for configuration and examples.

##### Context enrichment with MCPs

Model Context Protocol (MCP) servers let agents access external data sources. Use MCPs to pull in company documentation, query internal APIs, access knowledge bases, or integrate with development tools.

MCPs enrich the agent's context with information it wouldn't otherwise have. For example, an MCP might provide access to your API specifications, so agents can generate code that correctly calls your internal services.

MCPs are scoped to teams or users. Unlike hooks, MCPs don't enforce policies—they provide information that helps agents make better decisions.

See [MCP Integration](https://cursor.com/docs/mcp.md) for configuration and examples.

##### Advanced safety controls for Enterprise

Contact our team to learn about org-wide enforcement and security policies.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Model and Integration Management

*Your team can access multiple AI models and integrate Cursor with various services. This documentation covers how to control which models are available, manage MCP server trust, and set up integrations with tools like Slack, GitHub, and Linear.*

**Source:** https://cursor.com/docs/enterprise/model-and-integration-management

Your team can access multiple AI models and integrate Cursor with various services. This documentation covers how to control which models are available, manage MCP server trust, and set up integrations with tools like Slack, GitHub, and Linear.

#### Model access control

Enterprise teams can control which AI models team members can use, [contact sales](https://cursor.com/contact-sales?source=docs-model-controls) to get access. This helps manage costs, ensure appropriate usage, and comply with organizational policies.

Model access controls are configured through the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md). Navigate to Settings and look for "Model Access Control" (Enterprise only).

##### How enterprise model rollout works

When new models become available, Cursor doesn't immediately enable them for all enterprise teams.

Instead, Enterprise teams can opt in to new models for their organization.

See [Models](https://cursor.com/docs/models-and-pricing.md) for the current list of available models.

#### Restrict personal API keys (BYOK controls)

Enterprise teams can prevent team members from using their own API keys with third-party providers (OpenAI, Anthropic, Azure, AWS Bedrock) in Cursor. All usage goes through Cursor's included models and usage pool.

Configure this in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) under Settings (Enterprise only).

#### MCP server trust management

The Model Context Protocol (MCP) lets you connect external tools and data sources to Cursor. MCP servers can:

- Read files from external systems
- Execute operations on your behalf
- Access databases and APIs
- Integrate with third-party services

MCP servers are designed and implemented by external vendors, not Cursor. We work with partners to provide a [vetted marketplace](https://cursor.com/marketplace) of trusted servers, but you should review each server's capabilities and permissions before enabling it for your team.

Because MCP servers have significant capabilities, you need to manage which servers your team can use.

##### MCP Allowlist

Enterprise teams can control which MCP servers team members are allowed to use. Configure this in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) under "MCP Configuration" (Enterprise only).

Add each approved server as a command or URL entry, then configure its tool controls and network policy. Approving a trusted set of servers and domains is usually enough; apply stricter tool and network controls per server when you need them.

You can also distribute `~/.cursor/permissions.json` through MDM to set the per-user MCP auto-run allowlist from a managed file.

In that file, `mcpAllowlist` must be a JSON array of strings using `server:tool` syntax:

| Entry         | Meaning                                      |
| :------------ | :------------------------------------------- |
| `server:tool` | One specific tool on one specific MCP server |
| `server:*`    | All tools from one MCP server                |
| `*:tool`      | One tool name from any MCP server            |
| `*:*`         | All MCP tools                                |

Cursor resolves the effective MCP allowlist in this order:

1. Team dashboard or other admin-controlled settings
2. `~/.cursor/permissions.json`
3. The MCP allowlist in editor settings and inline **Add to allowlist**

Higher-priority sources replace lower-priority ones. They do not merge.

When an allowlist is active, only servers matching an allowlist entry can run. Servers that don't match are blocked.

Adding a server to the allowlist does not push it to users' machines. Team members still need to configure the server in their own [Cursor settings](https://cursor.com/docs/mcp.md).

To distribute an approved server, add it to a [team marketplace](https://cursor.com/docs/plugins.md#team-marketplaces). Admins can link existing standalone Team MCP servers to the Default marketplace so teammates can install and configure them in the Agent Window, IDE, and CLI.

All allowlist entries support wildcards using `*` to match any sequence of characters.

###### Command-based servers (stdio)

For local MCP servers configured with `command` and `args`, the allowlist matches against the **full command string**: the `command` value and all `args` values joined with spaces.

Given this `mcp.json` config:

```json
{
  "mcpServers": {
    "my-tool": {
      "command": "npx",
      "args": ["-y", "@acme/mcp-tool@latest"]
    }
  }
}
```

The full command string is `npx -y @acme/mcp-tool@latest`. On most systems, the shell resolves `npx` to a full path like `/usr/local/bin/npx` or `/opt/homebrew/bin/npx`, so the actual string becomes `/usr/local/bin/npx -y @acme/mcp-tool@latest`.

Use a leading `*` wildcard to match regardless of the install path:

| Allowlist entry                               | Matches                                                           |
| :-------------------------------------------- | :---------------------------------------------------------------- |
| `*npx -y @acme/mcp-tool@latest`               | `npx` at any path, with these exact arguments                     |
| `/usr/local/bin/npx -y @acme/mcp-tool@latest` | Only this exact path                                              |
| `*npx -y @acme/*`                             | Any `@acme`-scoped MCP package                                    |
| `*python */scripts/mcp-server.py*`            | A Python server at any matching path, with any trailing arguments |

###### URL-based servers (HTTP/SSE)

For remote MCP servers configured with `url`, the allowlist matches against the URL.

Given this `mcp.json` config:

```json
{
  "mcpServers": {
    "acme-tools": {
      "url": "https://mcp.acme.com/sse"
    }
  }
}
```

The allowlist entry matches against the full URL `https://mcp.acme.com/sse`:

| Allowlist entry            | Matches                                 |
| :------------------------- | :-------------------------------------- |
| `https://mcp.acme.com/sse` | This exact URL                          |
| `https://*.acme.com/*`     | Any subdomain and path under `acme.com` |
| `https://mcp.acme.com/*`   | Any path on this host                   |

##### Per-server tool controls

Tool controls live in the MCP Configuration section and are set per server, not in a separate auto-run list. For each approved server, restrict which tools can run by listing them in that server's Tools field. Leave the field empty to allow all tools from that server.

##### Per-server network controls

Each approved server has its own network policy, so you control what it can reach.

Remote (URL) MCP servers are restricted to the configured URL entry pattern.

Local command-based (`stdio`) servers run in a sandbox with one of these network modes:

| Network mode   | Behavior                                                |
| :------------- | :------------------------------------------------------ |
| **Allow all**  | No egress restrictions.                                 |
| **Allowlist**  | Only listed destinations are reachable.                 |
| **Deny all**   | Run the server locally with no outbound network access. |
| **No sandbox** | Run without command or network sandboxing.              |

#### Git repository blocklist

You can prevent Cursor from accessing specific repositories.

Add repository URLs or patterns in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) under "Repository Blocklist" (Enterprise only). Cursor will refuse to index or work with blocked repositories.

#### Protected Git Scopes

Lock a Git organization, group, or namespace to your Cursor organization so only your teams can use its repositories with [Cloud Agents](https://cursor.com/docs/cloud-agent.md), [automations](https://cursor.com/docs/cloud-agent/automations.md), and [Bugbot](https://cursor.com/docs/bugbot.md). Cursor always verifies that a user can access a repository's connected source before it runs an agent or Bugbot check. Protected Git Scopes adds an organization-level guarantee on top of that per-user check, so enterprises can be confident their code can't be reached through unsanctioned ("shadow IT") Cursor accounts or outside teams, even ones that already have legitimate Git access.

Protect or remove a scope from the [Integrations & MCP](https://cursor.com/dashboard/integrations) tab of your dashboard (Teams and Enterprise). Claiming a scope requires a Cursor team admin who is also a Git provider admin. Works with cloud and self-hosted GitHub and GitLab.

#### Integration: Slack

The Slack integration enables Cloud Agents to run directly from Slack. Team members can mention `@cursor` with a prompt and get automated code changes delivered as pull requests.

Cursor requires permissions to read messages, post responses, and access channel metadata. See the [Slack integration documentation](https://cursor.com/docs/integrations/slack.md#permissions) for the full list.

See [Slack integration](https://cursor.com/docs/integrations/slack.md) for detailed setup and usage instructions.

#### Integration: GitHub, GHES, and GitLab

Connect Cursor to your version control system to work with Cloud Agents.

Cursor requires read access to repositories and write access to create PRs. You control which repositories the Cursor app can access.

See [GitHub integration](https://cursor.com/docs/integrations/github.md) for setup.

#### Integration: Linear

Connect Linear to start Cloud Agents from issues.

Cursor requires read access to issues and write access to update issue status.

See [Linear integration](https://cursor.com/docs/integrations/linear.md) for details.

##### Model controls are available on the Enterprise plan

Contact our team to learn about model restrictions and MCP management.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cyber Safeguards

*Cyber Safeguards settings are available on the [Enterprise plan](https://cursor.com/docs/enterprise.md) and are configured per [Organization Group](https://cursor.com/docs/enterprise/organizations.md#groups) at **Organization → Groups**. These are not [billing groups](https://cursor.com/docs/account/enterprise/billing-groups.md) or SCIM [directory groups](https://cursor.com/docs/account/teams/scim.md).*

**Source:** https://cursor.com/docs/account/enterprise/cyber-safeguards

Cyber Safeguards settings are available on the [Enterprise plan](https://cursor.com/docs/enterprise.md) and are configured per [Organization Group](https://cursor.com/docs/enterprise/organizations.md#groups) at **Organization → Groups**. These are not [billing groups](https://cursor.com/docs/account/enterprise/billing-groups.md) or SCIM [directory groups](https://cursor.com/docs/account/teams/scim.md).

Anthropic applies cyber safeguards to its latest generations of Opus models. These safeguards can limit responses to some legitimate security and cyber-defense tasks. Through Anthropic's Cyber Verification Program (CVP), approved organizations can use eligible models without those safeguards for legitimate defensive work.

Cursor facilitates your application for the CVP, but any agreement for the program is only between your organization and Anthropic. All terms are set by Anthropic, and Cursor does not take on any of its obligations.

Once approved for the CVP by Anthropic, you can turn on the Cyber option for Opus 4.7 and Opus 4.8 from your settings.

It's important to understand that the blocks you might experience in Cursor when interacting with a model don't come from Cursor; they come directly from Anthropic's API.

#### About the program

The CVP belongs to Anthropic. You apply with Anthropic, and any agreement is between your organization and Anthropic. Cursor surfaces the application and the model controls in the dashboard so you can manage everything in one place. Cursor is not a party to the program, sets none of its terms, and takes on none of its obligations.

Anthropic sets the privacy policy for cyber-verified models. Today, zero data retention is turned off for requests going through these models.

#### Privacy and data retention

When you use Opus models with cyber safeguards turned off, Anthropic's CVP terms apply. Cursor cannot honor zero data retention or your team's [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) policy for those requests.

This applies only to the cyber-verified model you select. Other models in the same conversation, and every other request on your account, still follow your normal Privacy Mode settings.

Turning on Cyber for a group does not disable Privacy Mode organization-wide.

#### Setting up a dedicated group

Your organization can apply for the CVP only at the [Organization Group](https://cursor.com/docs/enterprise/organizations.md#groups) level so access stays with only the people who need it.

Turning on the Cyber option in a group only grants it to that group's members. It does not change anything for the rest of your team.

#### Apply for the program

Read Anthropic's terms in full before you apply. By applying, you confirm that you're an authorized representative of your organization and that you agree to Anthropic's terms, not Cursor's.

##### Open your Organization

Click your profile in the bottom-left corner and select **Organization** from the menu.

##### Create or open an Organization Group

In the left sidebar, open **Groups**. Create a new group for your security team (for example, `Security` or `CVP`) and add the relevant members, or click an existing group. If you see "No groups yet", create one before continuing.

##### Open Cyber Safeguards Models Settings

On that group's settings page, find the **Cyber Safeguards Models Settings** section. It appears alongside Spend Limit Overrides and Auto-Run Controls.

##### Start the application

Click **Apply** to open the program terms.

##### Review the terms and confirm

Read the **Apply for Cyber Verification Program** dialog. Click **I understand** only if you agree and are authorized to apply on behalf of your company, then click **Save**.

#### Anthropic Approval Process

Anthropic reviews your application directly and contacts you about the outcome. Cursor rechecks your status every two hours, so the dashboard updates on its own and shows **Approved** once you're cleared. Cursor is not responsible for the status of your application or for tracking its progress. If you'd like to see your status in real time, check the [Anthropic portal](https://portal.anthropic.com).

#### Enabling Cyber on a specific model

Once your group is approved, turn on the Cyber option in the same group's model access settings, shown above the Cyber Safeguards section.

Requests through a cyber-verified model run with Privacy Mode off for that model only. Cursor cannot honor zero data retention for those requests. See [Privacy and data retention](https://cursor.com/docs/account/enterprise/cyber-safeguards.md#privacy-and-data-retention) for details.

#### Supported models

Enabling this mode works with Anthropic models today: **Opus 4.7** and **Opus 4.8**.

#### FAQ

##### How does pricing work for cyber-verified models?

Pricing is the same as the base model. See [models & pricing](https://cursor.com/docs/models-and-pricing.md) for details.

##### Who can apply for the CVP through Cursor?

Only Organization admins can apply for the CVP, as they have to first create a group.

##### What is the privacy policy for cyber-verified models?

Anthropic sets the policy for cyber-verified models. Today, zero data retention is turned off for requests going through these models. When you use a model with cyber safeguards off, Privacy Mode is off for that model only. Cursor cannot honor your data retention policy for those requests. Other models in the same conversation still follow your normal Privacy Mode settings.

##### I applied for the CVP but don't see approval?

Approval is not instant. After you apply for the CVP, Cursor checks for your approval every two hours. Cursor is not responsible for the status of your application or for tracking its progress. If you'd like to see your status in real time, check the [Anthropic portal](https://portal.anthropic.com).

##### Is Mythos included as a part of the CVP?

No. Only Opus 4.7 and Opus 4.8 are a part of the program.

##### I only see Spend Limit Overrides and Auto-Run Controls

You're likely in team directory groups or billing groups, not Organization Groups. Open **Organization → Groups** from your profile menu, then click into a specific group. Cyber Safeguards Models Settings appear on that group's settings page.

##### My group is synced from Okta via SCIM. Does that work for CVP?

CVP applies to Organization Groups under **Organization → Groups**. SCIM [directory groups](https://cursor.com/docs/account/teams/scim.md) are a separate concept used for team-level spend and policy. Create or use a group in your organization's Groups page to apply for CVP.

##### A link in the email took me to the Overview page

CVP settings aren't on the org Overview page. Go to **Organization → Groups**, open your group, and look for **Cyber Safeguards Models Settings** on that group's settings page.

##### Cyber Safeguards are available on the Enterprise plan

Talk to our team about applying for Anthropic's Cyber Verification Program for your security group.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Pooled usage

*Pooled usage gives your Enterprise team a shared usage pool instead of fixed per-user allocations. Everyone draws from a single committed amount that spans your contract period, so agent usage is available wherever it's needed most.*

**Source:** https://cursor.com/docs/enterprise/pooled-usage

Pooled usage gives your Enterprise team a shared usage pool instead of fixed per-user allocations. Everyone draws from a single committed amount that spans your contract period, so agent usage is available wherever it's needed most.

#### Why pooled usage matters

Without pooled usage, unused capacity from team members can't be redirected to those doing the most demanding work. Pooled usage removes that constraint, letting your full budget serve your team's highest-priority projects.

##### Fewer interruptions

Without pooled usage, a developer working on a critical project can hit their cap while other allocations sit unused. With a shared pool, the team's committed budget is available to whoever needs it.

##### Dynamic spend alerts and limits

Admins can configure team-wide [Dynamic Spend Limits](https://cursor.com/help/account-and-billing/spend-limits.md#what-are-dynamic-spend-limits) that automatically scale with team size. Pair these with [Spend Alerts](https://cursor.com/help/account-and-billing/spend-alerts.md) to get email notifications when usage reaches configurable thresholds, so you stay informed without blocking anyone's work.

#### How it works

Your team commits to a total usage amount for your contract period. All team members share this pool, and usage is tracked cumulatively across the contract term. Dynamic spend limits and alerts give you ongoing governance while the shared pool remains the primary budget constraint.

##### Key details

- **Shared pool**: All team members draw from a single committed budget.
- **Cumulative tracking**: Usage is tracked across the full contract term, not month by month.
- **Spend alerts**: Get notified when team or member spending reaches thresholds you set. See [Spend Alerts](https://cursor.com/help/account-and-billing/spend-alerts.md) for configuration.
- **Dynamic limits**: Team-wide spend limits that scale automatically as your team grows or shrinks. See [Dynamic Spend Limits](https://cursor.com/help/account-and-billing/spend-limits.md#what-are-dynamic-spend-limits).
- **Admin controls**: Only admins can adjust pooled usage settings. See the [Dashboard](https://cursor.com/docs/account/teams/dashboard.md) for management tools.

##### Pooled usage is available on the Enterprise plan

Contact our team to learn about pooled usage for your organization.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Compliance and Monitoring

*Compliance requires visibility into who did what, when, and why. This documentation covers audit logs, AI code tracking, certifications, and how to meet regulatory requirements.*

**Source:** https://cursor.com/docs/enterprise/compliance-and-monitoring

Compliance requires visibility into who did what, when, and why. This documentation covers audit logs, AI code tracking, certifications, and how to meet regulatory requirements.

#### Audit logs

Audit logs provide a record of security events and administrative actions. Available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-audit-logs), audit logs help you meet compliance requirements and investigate security incidents.

We log the following events:

- **Authentication events:** Logins and logouts
- **User management:** User additions (via SSO, invite, signup, team creation, or auto-enrollment), removals, role changes, and individual spend limits
- **API key management:** Team and user API key creation and revocation
- **Team settings:** Team-wide and per-user spending limits, admin settings, team name changes, Slack integration settings, and repository mappings
- **Repository management:** Repository creation, deletion, and settings updates
- **Cloud Agent environments:** Environment creation, updates, restores, and lifecycle changes
- **Directory groups:** Directory group creation, updates, deletion, membership changes, and permission modifications
- **Privacy settings:** Privacy Mode changes at user or team level
- **Team rules:** Team rule management (including Bugbot rules) for custom workflows
- **Team commands:** Custom command creation, updates, and deletion

We do not log agent responses or generated code content.

Instead, we recommend using [hooks](https://cursor.com/docs/hooks.md) to log prompts and code.

##### Accessing audit logs

View audit logs in the [team dashboard](https://cursor.com/dashboard/audit-log). This is available on Enterprise plans, and requires admin access.

##### Streaming audit logs

For compliance and security monitoring, stream audit logs to your existing systems:

- SIEM systems (Splunk, Sumo Logic, Datadog, etc.)
- Webhook endpoints for custom processing
- S3 buckets for long-term retention
- Log aggregators like Elasticsearch or CloudWatch

Please contact [hi@cursor.com](mailto:hi@cursor.com) if you would like to receive streaming audit logs.

##### Log format

Audit logs are delivered as JSON and include metadata and event-specific fields:

```json
{
  "metadata": {
    "timestamp": "2024-10-14T18:30:45Z",
    "event_id": "evt_abc123xyz789"
  },
  "team_id": "team_xyz789",
  "ip_address": "203.0.113.42",
  "user_email": "alice@company.com",
  "event": { /* event-specific fields */ }
}
```

The `event_type` values include:

- `login` - User login events (web or app)
- `logout` - User logout events
- `add_user` - User additions (with source: `sso`, `invite`, `signup`, `createTeam`, or `autoEnroll`)
- `remove_user` - User removals from team
- `update_user_role` - Role changes (OWNER, ADMIN, MEMBER)
- `user_spend_limit` - Individual user spending limit changes
- `team_api_key` - Team API key actions (create, revoke)
- `user_api_key` - User API key actions (create, revoke)
- `team_settings` - Team setting modifications, including:
- `team_hard_limit_dollars` - Team-wide spending hard limit
- `team_hard_limit_per_user_dollars` - Per-user hard limit
- `per_user_monthly_limit_dollars` - Monthly spending limits per user
- `admin_only_usage_pricing` - Admin-only usage pricing settings
- `team_admin_settings` - General admin settings
- `team_name` - Team name changes
- `slack_default_repo` - Slack integration repository settings
- `slack_default_branch` - Slack integration branch settings
- `slack_default_model` - Slack integration model settings
- `slack_share_summary` - Slack summary sharing settings
- `slack_share_summary_in_external_channel` - External channel sharing
- `slack_channel_repo_mappings` - Slack channel to repository mappings
- `mcp_server_config` - MCP server configuration changes
- `team_repo` - Repository actions (create, delete, update\_settings)
- `create_directory_group` - Directory group creation
- `update_directory_group` - Directory group updates
- `update_directory_group_permissions` - Directory group permission changes
- `delete_directory_group` - Directory group deletion
- `add_user_to_directory_group` - Adding users to directory groups
- `remove_user_from_directory_group` - Removing users from directory groups
- `privacy_mode` - Privacy Mode changes (scope: "user" or "team")
- `team_rule` - Team rule management (create, update, delete)
- `team_hook` - Team hooks management (create, update, delete)
- `bugbot_installation` - Bugbot installation events
- `bugbot_installation_settings` - Bugbot installation settings changes
- `bugbot_repo_settings` - Bugbot repository settings changes
- `bugbot_team_rule` - Bugbot-specific rule management (create, update, delete)
- `bugbot_team_settings` - Bugbot team settings changes
- `bugbot_bulk_repo_update` - Bugbot bulk repository update events
- `team_command` - Custom team command management (create, update, delete)

##### Searching and filtering

Filter audit logs in the dashboard by:

- Date range
- Event type (authentication, user management, settings)
- Actor (specific user)

Export filtered results to CSV for analysis or compliance reports.

#### Using hooks for compliance logging

Audit logs track administrative actions, but some compliance requirements need logging of development activity. Use hooks to log:

##### Prompts submitted hook

```bash
#!/bin/bash
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')
user_id=$(echo "$input" | jq -r '.user_id')

# Log to your compliance system
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"prompt\",\"user\":\"$user_id\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

cat << EOF
{
  "continue": true
}
EOF
```

##### Code generated hook

```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.file_path')
edits=$(echo "$input" | jq -r '.edits')

# Log the code generation event (not the actual code)
curl -X POST "https://compliance.company.com/log" \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"generation\",\"file\":\"$file_path\",\"timestamp\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

exit 0
```

**Important:** Be careful logging actual code or prompts. They may contain sensitive information. Log metadata (who, when, what file) rather than content when possible.

See [Hooks](https://cursor.com/docs/hooks.md) for hook implementation details.

#### Certifications and compliance

Cursor maintains compliance with industry standards, including SOC 2 Type II, GDPR, and more.

Access compliance documentation through the [Trust Center](https://trust.cursor.com/) including:

- SOC 2 reports
- Penetration test summaries
- Security architecture documentation
- Data flow diagrams

#### Responsible disclosure

If you discover a security vulnerability in Cursor, report it through our responsible disclosure program:

Email [security-reports@cursor.com](mailto:security-reports@cursor.com) with the following information:

1. A detailed description of the vulnerability
2. Steps to reproduce the issue
3. Any relevant screenshots or proof of concept

##### Audit logs are available on the Enterprise plan

Contact our team to learn more about compliance features.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### HIPAA Business Associate Agreements

*Cursor supports HIPAA Business Associate Agreements (BAAs) for Enterprise customers.*

**Source:** https://cursor.com/docs/enterprise/baa

Cursor supports HIPAA Business Associate Agreements (BAAs) for Enterprise customers.

Organizations that are covered entities or business associates under HIPAA can request a BAA as part of their Enterprise agreement. A signed BAA is required before submitting protected health information (PHI) to Cursor.

#### Request a BAA

BAAs are available on the Enterprise plan. To request one:

1. [Contact sales](https://cursor.com/contact-sales?source=docs-baa)
2. Tell us that you need a HIPAA BAA
3. Share whether you are evaluating Cursor, moving from a Teams plan, or already on Enterprise

##### Request a HIPAA BAA

Contact sales to request BAA support for Cursor Enterprise.

#### Using Cursor with PHI

The HIPAA Implementation and Configuration Guide is part of the BAA. It includes current details about Eligible Services, Eligible Models, required controls, and customer responsibilities. [Request access in the Trust Center](https://trust.cursor.com/resources?s=i7h69cmvekn7rag2pc9y4r\&name=cursor-hipaa-implementation-guide.pdf).

A BAA does not automatically make every product, configuration, or workflow appropriate for PHI. Your organization is responsible for configuring Cursor and instructing users in accordance with your BAA, HIPAA requirements, and the HIPAA Guide.

Before using Cursor with PHI:

- Sign an Enterprise agreement and BAA with Cursor
- Review the HIPAA Guide in the Trust Center
- Enable and lock [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#privacy-mode-enforcement) organization-wide
- Train users to submit PHI only through Eligible Services and approved workflows

Third-party services and integrations are not automatically covered by Cursor's BAA. Your organization remains responsible for assessing and configuring any third-party services it uses with Cursor.

#### Eligible Services

The listed Eligible Services are covered for Enterprise customers with Privacy Mode enabled and locked organization-wide:

- Desktop IDE, including Agent, Tab, Edit, local agent mode, and inline edit
- Cloud Agents
- Cursor for iOS
- CLI
- Tab
- BugBot
- Automations

The HIPAA Guide has the latest details about Eligible Services and implementation requirements. [Request access in the Trust Center](https://trust.cursor.com/resources?s=i7h69cmvekn7rag2pc9y4r\&name=cursor-hipaa-implementation-guide.pdf).

#### FAQ

##### Who can request a BAA?

Enterprise customers and prospects evaluating Enterprise can request a BAA for Cursor. This typically applies to healthcare organizations and vendors that act as covered entities or business associates.

##### Is BAA support available on Teams?

BAA support is available on Enterprise. If your organization is currently on a Teams plan, [contact sales](https://cursor.com/contact-sales?source=docs-baa) to discuss moving to Enterprise and requesting a BAA.

##### Can we submit PHI before the BAA is signed?

No. Do not submit PHI to Cursor until your Enterprise agreement and BAA are signed and your organization has completed the required implementation steps.

##### Which Cursor services are covered?

Your signed BAA and the HIPAA Guide list the Eligible Services covered for PHI. [Request access in the Trust Center](https://trust.cursor.com/resources?s=i7h69cmvekn7rag2pc9y4r\&name=cursor-hipaa-implementation-guide.pdf).

##### Which models are covered?

The HIPAA Guide lists the current Eligible Models. [Request access in the Trust Center](https://trust.cursor.com/resources?s=i7h69cmvekn7rag2pc9y4r\&name=cursor-hipaa-implementation-guide.pdf).

##### Does Cursor's BAA cover third-party model providers or integrations?

Cursor's BAA does not automatically cover third-party services. Review your approved configuration, model provider settings, integration usage, and the HIPAA Guide before submitting PHI.

##### How do we get security and compliance documents?

Visit the [Trust Center](https://trust.cursor.com/) to request access to available security and compliance documents.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Deployment Patterns

*This guide covers how to deploy the Cursor editor and CLI tools to developer machines in your organization. Most organizations deploy both the editor (for daily development work) and the CLI (for automation, CI/CD, and scripting).*

**Source:** https://cursor.com/docs/enterprise/deployment-patterns

This guide covers how to deploy the Cursor editor and CLI tools to developer machines in your organization. Most organizations deploy both the editor (for daily development work) and the CLI (for automation, CI/CD, and scripting).

For other deployment options like SCM integrations (bugbot, BGA apps) or web-based access, see the relevant integration documentation.

#### Editor deployment with MDM

Deploy the Cursor editor and agent to user workstations and enforce policies through Mobile Device Management (MDM) systems.

##### How it works

1. Your IT team packages the Cursor application for deployment
2. Push to user machines via MDM (Jamf, Intune, etc.)
3. Users receive Cursor on their primary development machines

MDM allows you to enforce policies for Cursor, such as allowed team IDs and extensions.

You can also enforce settings like workspace trust, and control auto-updates and deployment of new versions.

##### MDM Configuration

You can centrally manage specific features of Cursor through device management solutions to ensure it meets the needs of your organization. When you specify a Cursor policy, its value overrides the corresponding Cursor setting on users' devices.

Cursor supports policies on Windows (Group Policy), macOS (configuration profiles), and Linux (JSON policy files, version 2.0+).

Cursor currently provides policies to control the following admin-controlled features:

| Policy                     | Description                                                                                                | Cursor setting                     |
| -------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| AllowedExtensions          | Controls which extensions can be installed.                                                                | `extensions.allowed`               |
| AllowedTeamId              | Controls which team IDs are allowed to log in. Users with unauthorized team IDs are forcefully logged out. | `cursorAuth.allowedTeamId`         |
| ExtensionGalleryServiceUrl | Configures a custom extension marketplace URL.                                                             | `extensions.gallery.serviceUrl`    |
| NetworkDisableHttp2        | Disables HTTP/2 for all requests, using HTTP/1.1 instead.                                                  | `cursor.general.disableHttp2`      |
| UpdateMode                 | Controls automatic update behavior. Set to 'none' to disable updates.                                      | `update.mode`                      |
| WorkspaceTrustEnabled      | Controls whether Workspace Trust is enabled.                                                               | `security.workspace.trust.enabled` |

###### Managing Run Mode allowlists with MDM

You can also deploy Cursor's permissions file through MDM to manage which terminal commands and MCP tools run without prompting and to steer the **Auto-review** mode classifier.

The file path is `~/.cursor/permissions.json`. Users can layer a per-repo file at `<workspace>/.cursor/permissions.json`; entries from both files are concatenated.

The file format is:

| Key                 | Type       | Required | Meaning                                                                                                                                                                                                                                                                                              |
| :------------------ | :--------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `terminalAllowlist` | `string[]` | No       | Terminal commands that may run without approval. With sandboxing enabled, supported terminal commands outside the allowlist can run in the sandbox. Each entry is matched against the full command string.                                                                                           |
| `mcpAllowlist`      | `string[]` | No       | MCP tools that may run without approval. MCP tools do not run inside the local sandbox. Each entry uses `server:tool` syntax.                                                                                                                                                                        |
| `autoRun`           | `object`   | No       | Steers the **Auto-review** mode classifier with natural-language `allow_instructions` and `block_instructions` arrays. Applies to shell, MCP, and Fetch calls in Cursor 3.6 and above. See the [permissions.json reference](https://cursor.com/docs/reference/permissions.md#autorun-configuration). |

`mcpAllowlist` entries support these forms:

| Entry         | Meaning                                      |
| :------------ | :------------------------------------------- |
| `server:tool` | One specific tool on one specific MCP server |
| `server:*`    | All tools from one MCP server                |
| `*:tool`      | One tool name from any MCP server            |
| `*:*`         | All MCP tools                                |

`terminalAllowlist`, `mcpAllowlist`, and `autoRun` are all optional. If a key is omitted or empty (after concatenating per-user and per-repo files), Cursor falls back to the editor-managed allowlist for that category.

Example:

```json
{
  "terminalAllowlist": [
    "npm install",
    "pnpm test",
    "python -m pytest"
  ],
  "mcpAllowlist": [
    "linear:*",
    "github:create_pull_request",
    "*:search"
  ],
  "autoRun": {
    "block_instructions": [
      "Block any command that drops or truncates a database table."
    ]
  }
}
```

Because this is a regular file, you can distribute it with Jamf, Kandji, Intune, or any other device management tool that writes files into a user's Cursor data directory.

Allowlist precedence is:

1. Team dashboard or other admin-controlled settings
2. Managed `~/.cursor/permissions.json` concatenated with `<workspace>/.cursor/permissions.json`
3. Editor settings and inline **Add to allowlist**

Admin-controlled settings replace the file-defined values for that category. Per-user and per-repo files merge by concatenation; editor settings do not merge with either.

Cursor watches both `permissions.json` paths, so updates apply automatically without requiring a restart.

###### Windows Group Policy

Cursor has support for Windows Registry-based Group Policy. When policy definitions are installed, admins can use the Local Group Policy Editor to manage the policy values.

To add a policy:

1. Copy the Policy ADMX and ADML files from `AppData\Local\Programs\cursor\policies`.
2. Paste the ADMX file into the `C:\Windows\PolicyDefinitions` directory, and the ADML file into the `C:\Windows\PolicyDefinitions\<your-locale>\` directory.
3. Restart the Local Group Policy Editor.
4. Set the appropriate policy values (e.g. `{"anysphere": true, "github": true}` for the `AllowedExtensions` policy) in the Local Group Policy Editor.

Policies can be set both at the Computer level and the User level. If both are set, Computer level will take precedence.

**Important:** When a policy value is set, it overrides the Cursor setting value configured at any level (default, user, workspace, etc.). This is a global override that prevents users from changing these settings.

In Cursor 2.1, we renamed the category name to Cursor in the Group Policy Editor. Old keys still work. We recommend using the current ADMX policy file.

###### Windows Installer

The Windows installer is based on Inno Setup. To install Cursor fully in the background without user interaction, use the following command-line flags:

**For fresh installations:**

```cmd
CursorSetup-x64-2.0.exe /SILENT /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /CLOSEAPPLICATIONS /LOG=install.log
```

**For updating existing installations:**

When updating an existing Cursor installation, you must use different flags that include the `/update` parameter pointing to a flag file. The flag file is an empty file that signals to the installer this is an update operation.

Create a temporary flag file and pass its path to the installer:

```cmd
CursorSetup-x64-2.0.exe /VERYSILENT /update="%TEMP%\cursor-update.flag" /CLOSEAPPLICATIONS /LOG=update.log
```

**Note:** Installers pre-2.0 may incorrectly not respect `/SILENT` flags. Future installers (version 2.0 and later) will ensure that silent installs work correctly.

###### macOS Configuration Profiles

Configuration profiles manage settings on macOS devices. A profile is an XML file with key/value pairs that correspond to available policy. These profiles can be deployed using Mobile Device Management (MDM) solutions like Jamf, Kandji, or Microsoft Intune, or installed manually.

**Bundle ID per channel:**

The `PayloadType` in your configuration profile must match the Cursor bundle ID for your channel:

| Channel    | Bundle ID                     |
| ---------- | ----------------------------- |
| Production | com.todesktop.230313mzl4w4u92 |
| Nightly    | co.anysphere.cursor.nightly   |

For most enterprise deployments, use the production bundle ID: `com.todesktop.230313mzl4w4u92`.

##### Example .mobileconfig file

An example `.mobileconfig` file for macOS is shown below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
	<dict>
		<key>PayloadContent</key>
		<array>
			<dict>
				<key>PayloadDisplayName</key>
				<string>Cursor</string>
				<key>PayloadIdentifier</key>
				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
				<key>PayloadType</key>
				<string>com.todesktop.230313mzl4w4u92</string>
				<key>PayloadUUID</key>
				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
				<key>PayloadVersion</key>
				<integer>1</integer>
				<key>AllowedExtensions</key>
				<string>{"anysphere":true}</string>
				<key>AllowedTeamId</key>
				<string>1,2</string>
				<key>ExtensionGalleryServiceUrl</key>
				<string>https://marketplace.example.com</string>
				<key>NetworkDisableHttp2</key>
				<true/>
				<key>UpdateMode</key>
				<string>none</string>
				<key>WorkspaceTrustEnabled</key>
				<true/>
			</dict>
		</array>
		<key>PayloadDescription</key>
		<string>This profile manages Cursor.</string>
		<key>PayloadDisplayName</key>
		<string>Cursor</string>
		<key>PayloadIdentifier</key>
		<string>com.todesktop.230313mzl4w4u92</string>
		<key>PayloadOrganization</key>
		<string>Anysphere</string>
		<key>PayloadType</key>
		<string>Configuration</string>
		<key>PayloadUUID</key>
		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
		<key>PayloadVersion</key>
		<integer>1</integer>
		<key>TargetDeviceType</key>
		<integer>5</integer>
	</dict>
</plist>
```

##### String policies

The example below demonstrates configuration of the `AllowedExtensions` policy. The policy value starts empty in the sample file (no extensions are allowed).

```bash
<key>AllowedExtensions</key>
<string></string>
```

Add the appropriate JSON string defining your policy between the `<string>` tags.

```bash
<key>AllowedExtensions</key>
<string>{"anysphere": true, "github": true}</string>
```

**Extension control semantics:**

The `AllowedExtensions` policy accepts a JSON object where:

- Keys can be publisher names (e.g., `"github"`) or full extension IDs (e.g., `"ms-azuretools.vscode-docker"`)
- Values are booleans indicating whether extensions from that publisher or specific extension are allowed
- If a publisher is set to `true`, all extensions from that publisher are allowed
- Specific extension IDs take precedence over publisher rules

For the `AllowedTeamId` policy, add the comma-separated list of team IDs:

```bash
<key>AllowedTeamId</key>
<string>1,3,7</string>
```

For the `NetworkDisableHttp2` policy, use a boolean value to disable HTTP/2:

```bash
<key>NetworkDisableHttp2</key>
<true/>
```

##### Boolean policies

For boolean policies like `WorkspaceTrustEnabled`, use `<true/>` or `<false/>` tags:

```bash
<key>WorkspaceTrustEnabled</key>
<false/>
```

Or to enable the feature:

```bash
<key>WorkspaceTrustEnabled</key>
<true/>
```

##### UpdateMode policy

The `UpdateMode` policy controls how Cursor handles automatic updates. This is useful for organizations that want to control when and how updates are deployed.

Available values:

- `none` - Disables all automatic updates
- `manual` - Users can manually check for updates
- `start` - Check for updates when Cursor starts
- `default` - Default behavior (same as `start`)
- `silentlyApplyOnQuit` - Download updates in the background and apply when Cursor quits

To disable automatic updates:

```bash
<key>UpdateMode</key>
<string>none</string>
```

##### WorkspaceTrustEnabled policy

The `WorkspaceTrustEnabled` policy controls whether [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) is enabled. When enabled, Cursor prompts users to choose between normal or restricted mode for new workspaces.

Use a boolean value:

```bash
<key>WorkspaceTrustEnabled</key>
<true/>
```

##### ExtensionGalleryServiceUrl policy

The `ExtensionGalleryServiceUrl` policy configures the extension marketplace URL. This is useful for organizations that want to use a custom extension marketplace or mirror.

Set the URL as a string value:

```bash
<key>ExtensionGalleryServiceUrl</key>
<string>https://marketplace.example.com</string>
```

##### Deploying with MDM solutions

The `.mobileconfig` file can be uploaded directly to your MDM solution:

- **Jamf**: Upload as a custom configuration profile
- **Kandji**: Add as a custom profile in Library
- **Microsoft Intune**: Deploy as a custom profile with the correct payload domain

Ensure the `PayloadType` matches your Cursor channel's bundle ID.

##### Reference configuration file

A complete example configuration profile is included with Cursor at:

```bash
# Production channel
/Applications/Cursor.app/Contents/Resources/app/policies/com.todesktop.230313mzl4w4u92.mobileconfig

# Nightly channel
/Applications/Cursor Nightly.app/Contents/Resources/app/policies/co.anysphere.cursor.nightly.mobileconfig
```

The file path varies by channel. Use the appropriate path for your Cursor installation.

**Important security considerations:**

- The provided `.mobileconfig` file initializes **all** policies available in that version of Cursor
- Delete any policies that are not needed to avoid unintentionally restrictive defaults
- If you do not edit or remove a policy from the sample, that policy will be enforced with its default value
- Policy values override all user and workspace settings globally

Manually install a configuration profile by double-clicking on the `.mobileconfig` profile in Finder and then enabling it in System Preferences under **General** > **Device Management**. Removing the profile from System Preferences will remove the policies from Cursor.

For more information on configuration profiles, refer to Apple's documentation.

###### Linux Policy File

Linux distributions don't have a standardized enterprise policy system like Windows Registry or macOS configuration profiles. Cursor reads policies from a JSON file to provide equivalent functionality.

**Note:** Linux policy file support is available in Cursor version 2.0 and later.

The policy file is located at `~/.cursor/policy.json`.

##### Creating a policy file

Create a JSON file at the location above with policy names as keys and their values. All policies are optional?include only the policies you want to enforce.

##### Example policy.json file

```json
{
  "AllowedExtensions": "{\"anysphere\": true, \"github\": true}",
  "AllowedTeamId": "1,3,7",
  "WorkspaceTrustEnabled": true
}
```

##### Policy format

Each policy in the JSON file maps to a policy name:

- **AllowedExtensions**: A JSON string defining allowed extension publishers
  ```json
  "AllowedExtensions": "{\"anysphere\": true, \"github\": true}"
  ```

- **AllowedTeamId**: A comma-separated string of team IDs
  ```json
  "AllowedTeamId": "1,3,7"
  ```

- **WorkspaceTrustEnabled**: A boolean controlling workspace trust
  ```json
  "WorkspaceTrustEnabled": true
  ```

**Note:** The `AllowedExtensions` value must be a JSON string (escaped quotes), not a JSON object. This matches the format used on Windows and macOS.

##### Deploying policies

Deploy the policy file using your organization's configuration management tools:

- Ansible, Puppet, or Chef for automated deployment
- NFS or shared network storage for centralized policy files
- Package managers with post-install scripts
- Container base images for containerized environments

Changes to the policy file take effect when Cursor restarts. The file is monitored for changes, so updates propagate automatically to running instances.

If the policy file doesn't exist, Cursor runs without policy restrictions.

##### Automatic updates for non-admin users

Due to Electron framework limitations, Cursor updates require administrator privileges on macOS.

**Recommended approaches:**

- **MDM deployment**: Use MDM tools (Jamf, Kandji, Intune) to deploy updates centrally with appropriate privileges
- **Automated deployment tools**: Consider tools like [Installomator](https://github.com/Installomator/Installomator) for scripted updates
- **Disable update prompts**: Set the `UpdateMode` policy to `none` to prevent users from seeing failed update notifications

For organizations with non-admin users, the most reliable approach is to manage Cursor updates through your existing software deployment pipeline and disable automatic updates via MDM policy.

#### CLI deployment

Run Cursor agents as a headless CLI tool on your infrastructure.

##### How it works

1. Deploy the CLI to your environment (on-prem, corporate cloud, Kubernetes clusters, CI/CD systems)
2. The CLI is scripted or run in the background or as part of CI
3. The CLI can access whatever the user can access from their machine (VPN, internal APIs, private package registries, etc.)

##### Installation and setup

Install the Cursor CLI:

```bash
# Install Cursor CLI (macOS, Linux, WSL)
curl https://cursor.com/install -fsS | bash

# Install Cursor CLI (Windows PowerShell)
irm 'https://cursor.com/install?win32=true' | iex

# Set API key for scripts
export CURSOR_API_KEY=your_api_key_here
agent -p "Analyze this code"
```

See [CLI headless mode documentation](https://cursor.com/docs/cli/headless.md) for full details.

##### GitHub Actions integration

Cursor CLI works in GitHub Actions and other CI systems.

See [GitHub Actions integration](https://cursor.com/docs/cli/github-actions.md) for examples.

#### Cursor CLI considerations

Whether running in the desktop app or as a standalone CLI, Cursor agents have the same security controls:

**Same features:**

- Privacy Mode applies equally
- Hooks work for both the desktop app and CLI
- Same model access controls
- Same audit logging
- Same usage tracking

**Same requirements:**

- Both need network access to Cursor services
- Both send code to LLMs (with Privacy Mode protections)
- Both require appropriate authentication

The CLI is the same agent with a different interface.

#### Network considerations

User machines need access to the following endpoints. Configure firewall and proxy rules accordingly:

- `*.cursor.sh` - Backend services and API endpoints
- `cursor-cdn.com` - Application downloads and updates
- `marketplace.cursorapi.com` - Extension marketplace
- Third-party AI provider endpoints (OpenAI, Anthropic, Google, etc.)

When using the `UpdateMode` policy set to `none`, you can restrict access to update endpoints while maintaining access to other services.

The Cursor editor inherits the machine's network configuration, including VPN access, internal service endpoints, and private package registries.

This means agents running in the editor can access whatever the user can access from their machine.

See [Network Configuration](https://cursor.com/docs/enterprise/network-configuration.md) for detailed firewall and proxy requirements.

#### Minimum Versions

We recommend users stay within one version of our most recent release. Users three or more versions behind our current release will start to see a warning indicating that they need to upgrade. Users four or more versions behind our latest release will see an error forcing them to update. This allows users to experience our latest features, while also staying up to date with our latest performance improvements, stability updates and bug fixes.

For example, if the latest release is 1.7, we recommend all users to be on version 1.6 or 1.7. Users on 1.4 or below will see a warning telling them to update. Users on 1.3 or below will see an error forcing them to update.

When managing Cursor deployments for your organization, we recommend updating your Cursor version regularly.

#### Troubleshooting

- Proxy configuration problems (see [Network Configuration](https://cursor.com/docs/enterprise/network-configuration.md))
- Model access issues (check [Model and Integration Management](https://cursor.com/docs/enterprise/model-and-integration-management.md) or your [team dashboard](https://cursor.com/docs/account/teams/dashboard.md))
- Spending limit reached (see [Spend Limits](https://cursor.com/help/account-and-billing/spend-limits.md))

#### Frequently asked questions

##### Does Cursor support policies on Linux?

Yes, starting with version 2.0. Linux uses a file-based policy system at `~/.cursor/policy.json`. See the "Linux Policy File" section above for details on the format and deployment.

##### Can I use environment variables in the policy file?

No. The policy file must be a valid JSON file with static values. Use your configuration management tools to generate the file dynamically if needed.

##### What happens if the policy file has invalid JSON?

Cursor logs an error and runs without policy restrictions. Check the main process logs for parsing errors.

##### What is my team ID?

You can find your team ID by clicking on your team name from [https://cursor.com/dashboard](https://cursor.com/dashboard).

##### Need help deploying Cursor at scale?

Contact our team for MDM deployment guidance and priority support.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Service Accounts

*Service accounts are available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).*

**Source:** https://cursor.com/docs/account/enterprise/service-accounts

Service accounts are available on the [Enterprise plan](https://cursor.com/docs/enterprise.md).

Service accounts are non-human accounts that enable teams to securely automate Cursor-powered workflows at scale. With service accounts, you can consume APIs, authenticate the [CLI](https://cursor.com/docs/cli/overview.md), and invoke [cloud agents](https://cursor.com/docs/cloud-agent.md) without tying integrations to individual developers' personal accounts.

#### Why use service accounts

As teams find new ways to automate coding tasks with Cursor cloud agents, APIs, and CLI, the need for centralized, secure automation becomes critical. Service accounts address this by:

- **Decoupling from individuals**: Automations continue running even as people and roles change
- **Secure credential management**: Easily rotate API keys without disrupting workflows
- **Centralized access control**: Admins manage all service account permissions in one place
- **Attribution and auditability**: Tie cloud agent runs to the initiating service or system

#### Key features

##### No additional seat required

Service accounts are included with your Enterprise plan at no extra cost. They do not consume a seat license.

##### Usage consumption

Service accounts consume usage from your team's usage pool, just like human users. All usage is tracked and visible in your team's analytics and billing.

##### Cloud agent integration

Service accounts can initiate [cloud agent](https://cursor.com/docs/cloud-agent.md) runs programmatically. This enables automation scenarios such as:

- A ticket created in Linear triggering a cloud agent to implement a feature
- An error in Sentry initiating a cloud agent to investigate and fix the issue
- Internal engineering services kicking off migrations or refactoring tasks

##### Admin visibility

Cloud agent runs initiated by service accounts are accessible to all team admins. This ensures visibility and oversight of automated workflows across your organization.

##### Repository access

Service accounts can initiate cloud agent runs on any repository that has been authorized via the [Cursor GitHub app](https://cursor.com/docs/integrations/github.md).

The GitHub integration must be connected at the team level for service accounts to access repositories. If you have a personal GitHub integration but no team-level integration, service accounts will not be able to initiate cloud agent runs.

To connect GitHub at the team level:

1. Navigate to **Dashboard** → **Settings** → **Integrations**
2. Connect the Cursor GitHub app to your organization
3. Authorize the repositories you want service accounts to access

Repository access is governed by the permissions configured for your team's GitHub app installation.

#### Creating a service account

Admins can create and manage service accounts from the [Cursor Dashboard](https://cursor.com/dashboard).

1. Navigate to **Dashboard** → **Settings** → **API Keys** → **Service Accounts**
2. Click **New Service Account**
3. Enter a name and optional description for the service account
4. Click **Create**

When you create a service account, an API key is generated. Copy this key immediately—it will only be shown once and cannot be retrieved later.

Store your API key securely. If you lose it, you'll need to rotate it to generate a new one.

#### Managing API keys

Each service account can have API keys associated with it. You can:

- **View masked keys**: See the last few characters of each key for identification
- **Rotate keys**: Generate a new key and invalidate the old one
- **Archive service accounts**: Archive a service account and revoke all its API keys

##### Rotating an API key

To rotate an API key:

1. Navigate to **Dashboard** → **Settings** → **API Keys** → **Service Accounts**
2. Find the service account and click the rotate icon next to its API key
3. Copy the new key immediately

The old key is immediately invalidated. Update any integrations using the old key.

#### Using service accounts with the API

Service accounts authenticate using their API key. Use the key in the `Authorization` header when making requests to the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md):

```bash
curl -X POST https://api.cursor.com/agents \
  -H "Authorization: Bearer YOUR_SERVICE_ACCOUNT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repo": "owner/repo",
    "prompt": "Implement the feature described in issue #123"
  }'
```

See the [Cloud Agents API documentation](https://cursor.com/docs/cloud-agent/api/endpoints.md) for the full API reference.

#### Using service accounts with the CLI

Service accounts can authenticate the [Cursor CLI](https://cursor.com/docs/cli/overview.md) by setting the API key as `CURSOR_API_KEY`. This is the recommended way to run the CLI in CI/CD pipelines, cron jobs, and other non-interactive environments where browser login isn't possible.

```bash
export CURSOR_API_KEY=your_service_account_api_key

# Run a task in a CI pipeline
agent -p --force "Refactor the authentication module to use OAuth 2.0"
```

The same environment variable works in any context, including local development. See the [CLI authentication docs](https://cursor.com/docs/cli/reference/authentication.md) for all authentication options and the [headless CLI guide](https://cursor.com/docs/cli/headless.md) for scripting patterns.

#### Security best practices

- **Rotate keys regularly**: Establish a key rotation schedule for your service accounts
- **Use descriptive names**: Name service accounts after their purpose (e.g., "Linear Integration", "Sentry Auto-Fix")
- **Limit scope**: Create separate service accounts for different automation workflows
- **Monitor usage**: Review service account activity in your team's analytics dashboard
- **Revoke unused accounts**: Archive service accounts that are no longer in use

#### Archiving a service account

Archiving a service account:

- Revokes all API keys associated with the account
- Breaks any integrations using those keys
- Preserves the account record for auditability

To archive a service account:

1. Navigate to **Dashboard** → **Settings** → **API Keys** → **Service Accounts**
2. Click the archive icon next to the service account
3. Confirm the archive action

Archived accounts can be viewed by clicking **Show Archived** on the Service Accounts page. This helps maintain a complete audit trail of service accounts used by your team.

##### Service accounts are available on the Enterprise plan

Automate Cursor-powered workflows at scale with non-human accounts for APIs and cloud agents.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Billing Groups

*[Billing groups](https://cursor.com/dashboard/members?subtab=billing-groups) allow Enterprise admins to understand and manage spend across groups of users. This functionality is useful for reporting, internal chargebacks, and budgeting.*

**Source:** https://cursor.com/docs/account/enterprise/billing-groups

[Billing groups](https://cursor.com/dashboard/members?subtab=billing-groups) allow Enterprise admins to understand and manage spend across groups of users. This functionality is useful for reporting, internal chargebacks, and budgeting.

For org-level cohorts across linked teams, see [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md).

#### Billing group architecture

Admins can assign each member to a billing group. Members can only be in one billing group at a time. Members not actively assigned in any other billing group are placed in a reserved `Unassigned` group.

All usage is attributed to the user's group at the time it occurs. Historical data does not change when users move between groups, though it can be reassigned only when a group is deleted. In that case, all of its usage is moved to the Unassigned group.

#### View billing groups

Enterprise admins can view billing groups in the web dashboard under the `Members & Groups` tab. This table shows each group, how it is configured, the number of members in it, and spend for the period.

![](https://cursor.com/docs-static/images/account/enterprise/billing-groups/billing-groups-view.png)

#### Create and add members to a billing group

Admins can create billing groups by clicking `Create Group`. After naming the group, there are four ways to assign members to that group:

1. **SCIM**: Sync the billing group with an existing [SCIM group](https://cursor.com/docs/account/teams/scim.md#scim).

2. **API**: Create groups and add members programmatically via the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#billing-groups).

3. **CSV**: Upload a CSV with group names and email addresses of members.

4. **Manual**: Click `Add Members` and manually select `Unassigned` members to be added.

Billing groups synced with SCIM cannot be edited via CSV, API, or manual UI changes. All member assignment for SCIM-synced groups must be handled via SCIM.

#### Move members between billing groups

Admins can move members from manual billing groups by clicking on the billing group and selecting `Move`.

- **SCIM**: When members are moved between SCIM groups in your identity provider, the billing group follows those changes automatically.
- **API**: Use the [add members](https://cursor.com/docs/account/teams/admin-api.md#add-members-to-group) and [remove members](https://cursor.com/docs/account/teams/admin-api.md#remove-members-from-group) endpoints to move members programmatically.

#### Rename a billing group

Billing groups can be renamed by clicking the gear button on the main menu, or by clicking `Rename` on the page for that specific billing group.

- **API**: Use the [update group](https://cursor.com/docs/account/teams/admin-api.md#update-group) endpoint to rename groups programmatically.

#### Delete a billing group

Billing groups can be deleted by clicking the gear button on the main menu, or by clicking `Delete` on the page for that specific billing group.

- **API**: Use the [delete group](https://cursor.com/docs/account/teams/admin-api.md#delete-group) endpoint to delete groups programmatically.

Deleting a billing group is a destructive operation; data cannot be recovered. All historic usage for deleted groups is assigned retroactively to the `Unassigned` group.

##### Billing groups are available on the Enterprise plan

Contact our team to learn about spend management and reporting.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Security and Privacy Hardening

*This page consolidates the security and privacy guidance spread across the Cursor docs into one reference, so teams configuring Cursor can review and apply the right controls without hunting through every page. Each item links to its source doc for the full detail.*

**Source:** https://cursor.com/docs/enterprise/security-hardening

This page consolidates the security and privacy guidance spread across the Cursor docs into one reference, so teams configuring Cursor can review and apply the right controls without hunting through every page. Each item links to its source doc for the full detail.

#### Shared responsibility

Cursor and your team share responsibility for a secure deployment. Cursor builds, secures, and operates the platform; you decide how to configure and adopt it for your environment. This page focuses on the controls you own. For Cursor's own posture, see the [Trust Center](https://trust.cursor.com/), [Security page](https://cursor.com/security), and [Data Use](https://cursor.com/data-use) policies.

- **Cursor handles** platform security, encryption, infrastructure, certifications, and the contractual commitments documented in the Trust Center.
- **You configure** identity, privacy enforcement, agent controls, extensibility trust, and monitoring, covered in the sections below.
- Layer controls for defense in depth: pair best-effort guardrails (Auto-review, allowlists, `.cursorignore`) with deterministic ones (approvals, hooks, sandboxing) rather than relying on a single layer.
- Most **enforcement** levers here (org-wide policies, MDM, SIEM streaming) are **Enterprise** features set in the [team dashboard](https://cursor.com/docs/account/teams/dashboard.md) or through MDM. Per-user controls such as `.cursorignore` and Run Mode defaults apply more broadly.

#### Admin quickstart

Do these first. Each links to its detail page. Other items for regulated orgs, like Cloud Agent retention windows, appear in the tables below.

1. Enforce **[Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#privacy-mode-enforcement)** org-wide so members can't disable Privacy Mode or its zero data retention guarantees for Cursor-routed models.
2. Set the org **[Run Mode policy](https://cursor.com/docs/agent/security/run-modes.md#run-mode)** to **Auto-review** (not Run Everything) and enable [sandboxing](https://cursor.com/docs/agent/security/run-modes.md#sandboxing).
3. Distribute **[hooks](https://cursor.com/docs/hooks.md#team-distribution)** for enforcement and logging across the team.
4. Apply **[network allowlisting](https://cursor.com/docs/enterprise/network-configuration.md#ip-allowlisting)** and exclude Cursor domains from [SSL inspection](https://cursor.com/docs/enterprise/network-configuration.md#ssl-inspection-and-dlp); set **[Cloud Agent network egress](https://cursor.com/docs/cloud-agent/security-network.md#network-access)** if you use Cloud Agents.
5. Set a **[Rules](https://cursor.com/docs/rules.md#team-rules)** baseline for steering, knowing rules are non-deterministic.
6. Govern **[plugins](https://cursor.com/docs/plugins.md)** and **[MCP servers](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-allowlist)** by reviewing what they install and approving trusted sources.
7. Add **[`.cursorignore`](https://cursor.com/docs/reference/ignore-file.md)** entries for secrets and regulated paths.
8. Lock identity with **[SSO](https://cursor.com/docs/account/teams/sso.md)**, **[SCIM](https://cursor.com/docs/account/teams/scim.md)**, and **[Allowed Team IDs](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-team-ids)** (MDM); restrict **[extensions](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-extensions)**, set an **[install cooldown](https://cursor.com/help/customization/extensions.md#marketplace-install-cooldown)** (and optional [signature verification](https://cursor.com/help/customization/extensions.md#extension-signature-verification)), and keep clients on a [supported version](https://cursor.com/docs/enterprise/deployment-patterns.md#minimum-versions).
9. Decide which **[models](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control)** your organization allows and restrict the rest; restrict **[personal API keys (BYOK)](https://cursor.com/docs/enterprise/model-and-integration-management.md#restrict-personal-api-keys-byok-controls)** if you rely on Cursor's ZDR agreements.
10. Periodically review and stream **[audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs)** to your SIEM.
11. For encryption with your own keys, enable **[CMEK](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#data-encryption)** when your compliance program requires it (embeddings and Cloud Agent data).

#### Identity and access

Control who signs in and on which device.

| Control                        | Recommendation                                                                                                                                                                                                  | Learn more                                                                                                                                                                                       |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SSO and SCIM**               | Centralize authentication and automate user deprovisioning.                                                                                                                                                     | [SSO](https://cursor.com/docs/account/teams/sso.md), [SCIM](https://cursor.com/docs/account/teams/scim.md)                                                                                       |
| **Allowed Team IDs**           | Block personal accounts on corporate devices via MDM so Privacy Mode always applies.                                                                                                                            | [Identity](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-team-ids)                                                                                                |
| **Allowed Extensions**         | Allowlist trusted publishers; any entry blocks the rest unless you add `"*": true`.                                                                                                                             | [Extensions](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-extensions)                                                                                            |
| **Extension install cooldown** | Defer extension installs and updates until a marketplace version has been public for a set number of hours (enforced fleet-wide), with optional signature verification, to blunt short-lived malicious uploads. | [Cooldown](https://cursor.com/help/customization/extensions.md#marketplace-install-cooldown), [Signatures](https://cursor.com/help/customization/extensions.md#extension-signature-verification) |
| **Supported version**          | Keep clients current and manage updates with the `UpdateMode` MDM policy.                                                                                                                                       | [Versions](https://cursor.com/docs/enterprise/deployment-patterns.md#minimum-versions)                                                                                                           |
| **Workspace Trust**            | Enforce through MDM so untrusted folders open in restricted mode. Restricted mode limits AI features; use it for truly untrusted trees, not day-to-day repos.                                                   | [Workspace Trust](https://cursor.com/docs/enterprise/identity-and-access-management.md#workspace-trust)                                                                                          |

#### Privacy and data

Control how your code and data are handled.

| Control                      | Recommendation                                                                                                                                                                                      | Learn more                                                                                                              |
| :--------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| **Privacy Mode**             | Enforce org-wide so members can't disable Privacy Mode or its ZDR commitments for Cursor-routed models; on by default for Enterprise. See exceptions under BYOK and models with provider retention. | [Privacy](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#privacy-mode-enforcement)                   |
| **Personal API keys (BYOK)** | Restrict them; with your own keys, zero data retention is subject to your own agreement with the model provider, not Cursor's.                                                                      | [BYOK](https://cursor.com/docs/enterprise/model-and-integration-management.md#restrict-personal-api-keys-byok-controls) |
| **CMEK**                     | Encrypt embeddings and Cloud Agent data with your own key when your compliance program requires customer-managed keys.                                                                              | [CMEK](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#data-encryption)                               |
| **Model access**             | Approve specific models for use by your organization. Non-ZDR models require admin approval.                                                                                                        | [Models](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control)                   |
| **Repository blocklist**     | Keep sensitive repos out of Cursor entirely.                                                                                                                                                        | [Blocklist](https://cursor.com/docs/enterprise/model-and-integration-management.md#git-repository-blocklist)            |
| **Protected Git Scopes**     | Lock your Git org or namespace so only your teams use those repos with Cloud Agents and Bugbot.                                                                                                     | [Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes)                   |

Also see [HIPAA BAA](https://cursor.com/docs/enterprise/baa.md) and [Cyber Safeguards](https://cursor.com/docs/account/enterprise/cyber-safeguards.md) when those apply to your deployment.

#### Data retention and deletion

You and your users have several ways to manage your data.

| Mechanism                             | What it covers                                                                                                                                           | How                                                                                                                                                                          |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Individual account deletion**       | That user's account and associated data, including indexed codebases; removed within 30 days. Does not by itself complete enterprise tenant offboarding. | Dashboard → Advanced Account Settings → Delete Account ([guide](https://cursor.com/help/account-and-billing/delete-account.md))                                              |
| **Data subject requests**             | Personal Data access, correction, or deletion requests (DSAR).                                                                                           | Email [hi@cursor.com](mailto:hi@cursor.com) to exercise privacy rights ([Privacy Policy](https://cursor.com/privacy))                                                        |
| **Shared chats and canvases**         | Published share links.                                                                                                                                   | Delete from the dashboard ([shared chats](https://cursor.com/dashboard/shared-chats), [shared canvases](https://cursor.com/dashboard/shared-canvases))                       |
| **Cloud Agent deletion**              | An agent's conversation transcript and artifacts, on demand.                                                                                             | [Delete Agent API](https://cursor.com/docs/cloud-agent/api/endpoints.md#delete-an-agent-permanently)                                                                         |
| **Automatic expiry**                  | Indexed codebases (6 weeks inactivity); Cloud Agent snapshots (90 days inactivity).                                                                      | Automatic, no action needed ([indexing](https://cursor.com/docs/agent/tools/search.md), [snapshots](https://cursor.com/docs/cloud-agent/security-network.md#data-retention)) |
| **Enterprise retention windows**      | Cap Cloud Agent data retention (Indefinite or 90 days; custom windows in early access).                                                                  | [Cloud Agent retention](https://cursor.com/docs/cloud-agent/security-network.md#cloud-agent-retention-policies); contact sales                                               |
| **Contract termination (Enterprise)** | Return or deletion of personal data for the enterprise engagement.                                                                                       | Governed by the [DPA](https://cursor.com/terms/dpa); coordinate with your account team                                                                                       |

#### Agent runtime and deterministic controls

The hard boundaries on what agents can do. Steering belongs with these, never instead of them.

| Control                        | Recommendation                                                                                                                                                                  | Learn more                                                                                                                                                                                                |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Auto-review (Run Mode)**     | Prefer it over Run Everything; it runs allowlisted calls, sandboxes shell commands when it can, and routes the rest through a best-effort classifier, so combine it with hooks. | [Run Modes](https://cursor.com/docs/agent/security/run-modes.md#run-mode), [Sandboxing](https://cursor.com/docs/agent/security/run-modes.md#sandboxing)                                                   |
| **Network allowlisting**       | Allowlist `*.cursor.sh` and set per-server MCP network policy; exclude Cursor domains from SSL inspection so users don't disable security to "make it work."                    | [Network](https://cursor.com/docs/enterprise/network-configuration.md#ip-allowlisting), [MCP network](https://cursor.com/docs/enterprise/model-and-integration-management.md#per-server-network-controls) |
| **Cloud Agent network egress** | Restrict Cloud Agents' outbound access with Default + allowlist or Allowlist-only modes; Enterprise admins can lock the policy org-wide.                                        | [Cloud Agent network](https://cursor.com/docs/cloud-agent/security-network.md#network-access)                                                                                                             |
| **Private connectivity**       | Reach private source control through PrivateLink or Cloudflare Tunnel, and align Cursor traffic with your endpoint security (AV/EDR/DLP).                                       | [Connectivity](https://cursor.com/docs/enterprise/private-connectivity.md), [Endpoint](https://cursor.com/docs/enterprise/endpoint-security.md)                                                           |
| **Hooks**                      | Enforce and observe at agent lifecycle points (block commands, scrub secrets, audit); distribute by MDM or cloud and set `failClosed` for critical hooks.                       | [Hooks](https://cursor.com/docs/hooks.md#team-distribution)                                                                                                                                               |
| **Integrate your own tools**   | Call your SIEM, DLP, allowlist, or policy APIs from hooks instead of relying only on defaults.                                                                                  | [Examples](https://cursor.com/docs/enterprise/llm-safety-and-controls.md#enforcement-hooks), [Partners](https://cursor.com/docs/hooks.md#partner-integrations)                                            |
| **`.cursorignore`**            | Block agent read and context for secrets and regulated trees; terminal and MCP tools can't honor it, so pair with approvals and file permissions.                               | [Ignore files](https://cursor.com/docs/reference/ignore-file.md)                                                                                                                                          |
| **Other protections**          | Keep Browser, File-Deletion, External-File, and `.cursor` directory protection enabled so risky actions still require approval.                                                 | [Protections](https://cursor.com/docs/agent/security/run-modes.md#other-protections), [.cursor](https://cursor.com/docs/enterprise/llm-safety-and-controls.md#cursor-directory-protection)                |

#### Steering and extensibility

Guidance and add-ons shape behavior and expand capability. Both are non-deterministic and are trust decisions.

| Control     | Recommendation                                                                                                                        | Learn more                                                                                                                                                                |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Rules**   | Steer behavior org-wide with Team Rules, but treat them as suggestions and pair them with the deterministic controls above.           | [Rules](https://cursor.com/docs/rules.md#team-rules)                                                                                                                      |
| **Plugins** | A plugin can bundle MCP servers, skills, subagents, rules, and hooks, so review what it installs and favor private team marketplaces. | [Plugins](https://cursor.com/docs/plugins.md), [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security.md)                               |
| **MCP**     | Approve servers with the allowlist, restrict per-server tools, and apply network modes; review each server before enabling.           | [MCP allowlist](https://cursor.com/docs/enterprise/model-and-integration-management.md#mcp-allowlist), [Security](https://cursor.com/docs/mcp.md#security-considerations) |

#### Monitor and respond

Review output, verify controls, and keep an audit trail.

| Practice                   | Recommendation                                                                                    | Learn more                                                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------ |
| **Pre-production review**  | Have Bugbot and Security Agents review Cursor-generated code before it ships to production.       | [Bugbot](https://cursor.com/docs/bugbot.md), [Security Agents](https://cursor.com/docs/security-agents.md)          |
| **Audit logs**             | Periodically review them and stream to SIEM, webhooks, or S3 for authentication and admin events. | [Compliance](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs)                            |
| **Compliance logging**     | Use hooks to capture development-activity metadata beyond Cursor's audit logs.                    | [Hooks logging](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#using-hooks-for-compliance-logging) |
| **Responsible disclosure** | Report vulnerabilities to [security-reports@cursor.com](mailto:security-reports@cursor.com).      | [Disclosure](https://cursor.com/docs/agent/security.md#responsible-disclosure)                                      |

#### Further reading

Background and product context. The docs linked throughout this page are the authority for each control.

- [Governing agent autonomy with Auto-review](https://cursor.com/blog/agent-autonomy-auto-review)
- [Implementing a secure sandbox for local agents](https://cursor.com/blog/agent-sandboxing)
- [Hooks for security and platform teams](https://cursor.com/blog/hooks-partners)

#### Platform commitments

The controls on this page describe how to configure your own environment. They complement Cursor's platform security and contractual commitments:

- [Trust Center](https://trust.cursor.com/) for certifications, security architecture, and subprocessors
- [Master Services Agreement](https://cursor.com/terms/msa) and [Data Processing Agreement](https://cursor.com/terms/dpa) for contractual and data-protection terms

Subscribe in the [Trust Center](https://trust.cursor.com/) to get notified when [subprocessors](https://trust.cursor.com/subprocessors) or Cursor's security posture change. Cursor sends a confirmation email to the address you enter, and you must verify it before updates start arriving.

##### Harden Cursor for your organization

Contact our team to enable org-wide enforcement, CMEK, and SIEM streaming.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cursor Blame

*Understanding how AI contributed to your codebase helps with review, compliance, and debugging. This page covers how Cursor Blame surfaces AI versus human authorship in git history.*

**Source:** https://cursor.com/docs/integrations/cursor-blame

Understanding how AI contributed to your codebase helps with review, compliance, and debugging. This page covers how Cursor Blame surfaces AI versus human authorship in git history.

#### Overview

Cursor Blame extends traditional git blame with AI attribution, so you can see what was AI-generated versus human-written. Available on the [Enterprise plan](https://cursor.com/contact-sales?source=docs-cursor-blame), it helps you understand the origin of each line when you review or revisit code:

- **Tab**: Code generated or accepted from Cursor's Tab suggestions
- **Agent**: Code generated by Agent, with model attribution
- **Human**: Code written directly by developers

Hover over AI-attributed lines to see conversation summaries. Click to open the full commit view with detailed AI attribution.

#### How it works

Cursor Blame analyzes committed code to determine AI attribution. When you view a file or commit, it retrieves attribution data that identifies which lines came from AI assistance, which models were used, and the conversations that produced them.

##### AI attribution

See at a glance which lines came from AI assistance and which were written manually.

##### Model tracking

Agent-generated code shows which model produced it, helping you understand AI tool usage across your codebase.

##### Conversation context

View summaries of the conversations that produced AI-generated code, with links to the full commit details.

##### Contribution breakdown

See percentage attribution for each contributor (AI models and human) in the commit view.

#### Using Cursor Blame

##### Enabling Cursor Blame

Cursor Blame is disabled at the team level by default. A team admin can enable it for all team members in the [Team settings](https://cursor.com/dashboard/settings).

##### Line annotations

1. Open the Command Palette (Cmd+Shift+P) and search for "Cursor Blame: Toggle editor decorations"

**In-editor ghost text** displays:

- **Author**: The team member who committed the change
- **Subject**: The commit message
- **Time**: When the change was made (relative time)

**Hover over the ghost text** to see:

- Author with AI co-authorship indicator
- Conversation summary (for AI-attributed lines)
- Commit statistics (files, additions, deletions)

**Open the commit view** to see:

- Full AI contribution breakdown by source
- Percentage attribution for Composer, each Agent model, and human edits
- Related conversations with summaries

##### File blame view

1. Open a file in the editor
2. Right-click and select **Cursor Blame > Toggle file blame** from the context menu, or use the Command Palette (Cmd+Shift+P) and search for "Cursor Blame: Open File Blame"
3. The file blame view shows attribution alongside each line

#### Privacy considerations

Cursor Blame caches attribution data locally for performance. When you view files and commits, data is fetched from Cursor's servers. Conversation summaries are retrieved on-demand and show brief descriptions rather than full conversation history.

#### Requirements

- Enterprise plan
- Git repository with Cursor-tracked changes

##### Get Cursor Blame on Enterprise

Talk to our team about enabling AI-aware git blame for your organization.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---
