# Dify Documentation — difyctl CLI Reference

*This document was scraped from the official Dify documentation and cleaned/reformatted for ingestion into NotebookLM (for building a learning plan). It is part of a multi-file set covering the full Dify docs guide.*

- **Source:** https://docs.dify.ai/en/home
- **Total pages in this file:** 20
- **Date scraped:** 2026-07-18

## Table of Contents

- **[difyctl CLI](#difyctl-cli)**
  - [Authenticate](#authenticate)
    - [Authenticate](#authenticate-1)
  - [Common Tasks](#common-tasks)
    - [Common Tasks](#common-tasks-1)
  - [Install](#install)
    - [Install difyctl](#install-difyctl)
  - [Integrate Agents](#integrate-agents)
    - [Authenticate Where Your Agent Runs](#authenticate-where-your-agent-runs)
    - [Handle Errors and Retries](#handle-errors-and-retries)
    - [Install the difyctl Skill](#install-the-difyctl-skill)
    - [Integrate Your Agents with Dify Apps](#integrate-your-agents-with-dify-apps)
  - [Overview](#overview)
    - [Overview](#overview-1)
  - [Quick Start](#quick-start)
    - [Quick Start](#quick-start-1)
  - [Reference](#reference)
    - [Apps](#apps)
    - [Auth and Contexts](#auth-and-contexts)
    - [Command Index](#command-index)
    - [Environment Variables](#environment-variables)
    - [Global Flags](#global-flags)
    - [Help](#help)
    - [Output Formats and Exit Codes](#output-formats-and-exit-codes)
    - [Skills](#skills)
    - [Version](#version)
    - [Workspaces](#workspaces)
  - [Troubleshooting](#troubleshooting)
    - [Troubleshooting](#troubleshooting-1)

---

## difyctl CLI

### Authenticate

#### Authenticate

*Sign in to your Dify host from the CLI, see where your token is stored, and manage your session*

**Source:** https://docs.dify.ai/en/cli/authenticate

Sign in to your Dify host from the CLI, see where your token is stored, and manage your session

You sign in through your browser, using the OAuth 2.0 device flow; `difyctl` never sees your password.

#### Sign In

  1. **Run the login command**
        Pass your Dify host's URL. For Dify Cloud, use `https://cloud.dify.ai`; on a self-hosted deployment, use the [console API URL](https://docs.dify.ai/en/self-host/deploy/configuration/environments#console_api_url).

        ```bash theme={null}
        difyctl auth login --host https://cloud.dify.ai
        ```

        `difyctl` prints a one-time code, opens the verification URL in your default browser, and waits:

        ```text theme={null}
        ! Copy this one-time code: WDJP-XKLM
          Open: https://cloud.dify.ai/device
        ```

        > **💡 Tip:**
>           To skip the auto-open, pass `--no-browser`.
>

        If no browser opens (normal over SSH and in headless sessions), open the URL yourself on any device.

  1. **Approve the sign-in in your browser**
        In the browser tab that opens, sign in with your Dify credentials and enter the one-time code.

        The code expires after 15 minutes. If it expired, re-run `difyctl auth login` to get a fresh one.

  1. **Confirm the session**
        Back in the terminal:

        ```text theme={null}
        ✓ Logged in to cloud.dify.ai as <your-email> (<your-name>)
          Workspace: <your-workspace>
        ```

        The second line is your workspace.

#### Sign In Again

If a command fails with `auth_expired` (exit code 4), the server has expired or revoked your session.

Run `difyctl auth login` again. You don't need to sign out first, and the new sign-in refreshes your stored token.

#### Check Who You're Signed In As

```bash theme={null}
difyctl auth whoami
```

```text theme={null}
<your-email> (<your-name>)
```

To read the identity from a script, add `--json`:

```bash theme={null}
difyctl auth whoami --json
```

You'll get the same fields as a JSON object, plus your account ID:

```json theme={null}
{"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","email":"<your-email>","name":"<your-name>"}
```

#### Sign Out

```bash theme={null}
difyctl auth logout
```

```text theme={null}
✓ Logged out of cloud.dify.ai
```

This revokes the session on the server and deletes the token and session entry from your machine. If the server-side revocation fails, your local credentials are cleared anyway.

#### Where Your Token Lives

Signing in stores an OAuth bearer token, recognizable by its `dfoa_` prefix. It represents you: whatever your account can do in your workspace, the token can do from the CLI.

`difyctl` keeps the token in your operating system's credential store when one is available: Keychain on macOS, Credential Manager on Windows, Secret Service on Linux. If no credential store responds, it falls back to a `tokens.yml` file with `0600` permissions in the `difyctl` config directory.

`difyctl` picks the store once when you sign in, and the session uses it from then on. Session metadata (hosts, accounts, workspaces) lives alongside the token in `hosts.yml`.

The config directory is `~/.config/difyctl` on macOS and Linux (Linux honors `XDG_CONFIG_HOME`) and `%APPDATA%\difyctl` on Windows. Set [`DIFY_CONFIG_DIR`](https://docs.dify.ai/en/cli/reference/environment-variables) to override it.

#### Troubleshooting

| Problem                                   | What to do                                                                                                                                                                                                                      |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The browser never opens                   | Copy the URL from the terminal and open it on any device.                                                                                                                                                                       |
| The host is rejected                      | Only `https://` hosts are accepted; a host without a scheme defaults to `https://`. For a plain `http://` host, or an `https://` host with a self-signed or invalid TLS certificate (local development only), add `--insecure`. |
| A later command fails with `auth_expired` | Your session expired or was revoked. [Sign in again](#sign-in-again).                                                                                                                                                           |

For everything else, see the full [Troubleshooting](https://docs.dify.ai/en/cli/troubleshooting) page.

### Common Tasks

#### Common Tasks

*Copy-paste commands for the difyctl tasks you'll run most often*

**Source:** https://docs.dify.ai/en/cli/common-tasks

Copy-paste commands for the difyctl tasks you'll run most often

All commands below assume you're [signed in](https://docs.dify.ai/en/cli/authenticate).

#### Send a Message

Send a message to a Chatbot, Chatflow, Agent, or Text Generator app by passing it as a positional argument to [`difyctl run app`](https://docs.dify.ai/en/cli/reference/apps#run-an-app). The reply prints to stdout.

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?"

# save just the reply to a file; hints and errors go to stderr, not stdout
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "Summarize this week's tickets" > reply.txt
```

#### Run a Workflow

Pass the inputs as a single JSON object with [`--inputs`](https://docs.dify.ai/en/cli/reference/apps#run-an-app) instead of a positional message. The outputs print to stdout as JSON.

```bash theme={null}
difyctl run app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --inputs '{"topic":"quarterly report"}'

# read large input sets from a file instead
difyctl run app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --inputs-file inputs.json
```

#### Find Your Apps

List the apps in your workspace with [`difyctl get app`](https://docs.dify.ai/en/cli/reference/apps#list-your-apps). Narrow the list with `--name` or `--mode`.

```bash theme={null}
difyctl get app

# filter by name substring or mode
difyctl get app --name report --mode workflow

# list apps from every workspace you belong to
difyctl get app -A
```

#### Stream a Long Response

Add [`--stream`](https://docs.dify.ai/en/cli/reference/apps#run-an-app) to print the response as it's generated instead of all at once at the end.

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "Draft a launch announcement" --stream
```

#### Continue a Conversation

Copy the conversation ID from the hint that follows each Chatbot or Chatflow reply, then pass it back with [`--conversation`](https://docs.dify.ai/en/cli/reference/apps#run-an-app) to continue the same conversation.

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?"
# hint: continue this conversation with --conversation 4f7d8c2a-9b1e-4c6d-8a3f-5e2b7c9d0a1f

difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "And on weekends?" --conversation 4f7d8c2a-9b1e-4c6d-8a3f-5e2b7c9d0a1f
```

#### Get JSON Output for Scripts

Add [`-o json`](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) to any command to get the raw response as pipe-friendly JSON.

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?" -o json | jq -r '.answer'

# extract fields from list output the same way
difyctl get app -o json | jq -r '.data[].id'

# get just the IDs, one per line, no jq needed
difyctl get app -o name
```

#### Switch Your Workspace **[Cloud]**

Change your active workspace with [`difyctl use workspace`](https://docs.dify.ai/en/cli/reference/workspaces#switch-your-workspace-cloud). List available workspaces with `get workspace`.

```bash theme={null}
difyctl get workspace

difyctl use workspace 9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c
# ✓ Switched to Marketing (9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c)

# one-off: run a single command against another workspace without switching
difyctl get app --workspace 9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c
```

#### Inspect an App's Inputs

Before running an unfamiliar app, check its app type and input schema with [`difyctl describe app`](https://docs.dify.ai/en/cli/reference/apps#inspect-an-app): names, types, and which inputs are required.

```bash theme={null}
difyctl describe app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b

# get the schema as JSON to build --inputs programmatically
difyctl describe app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b -o json
```

### Install

#### Install difyctl

*Install difyctl with a one-line script or a manual binary download*

**Source:** https://docs.dify.ai/en/cli/install

Install difyctl with a one-line script or a manual binary download

`difyctl` is a standalone binary with no runtime dependencies. The install script detects your platform, downloads the matching build from Dify's GitHub Releases, verifies its checksum, and puts the binary in place.

> **📝 Note:**
>   `difyctl` was introduced with Dify 1.15.0. Each build targets a specific Dify version, so install the one that matches your server (see `DIFY_VERSION` below).

#### Install

  1. **Run the Installer**
        `difyctl` ships a build with each Dify release, and the installer fetches the latest by default.

          **macOS / Linux:**

            Supported platforms: macOS and Linux, x64 and arm64.

            ```bash theme={null}
            curl -fsSL https://raw.githubusercontent.com/langgenius/dify/main/cli/scripts/install-cli.sh | sh
            ```

            The script installs to `~/.local/bin/difyctl` and tells you if that directory isn't on your `PATH`.

          **Windows:**

            Supported platform: x64.

            ```powershell theme={null}
            irm https://raw.githubusercontent.com/langgenius/dify/main/cli/scripts/install.ps1 | iex
            ```

            The script installs to `%LOCALAPPDATA%\difyctl\bin\difyctl.exe` and prints the command to add that directory to your `PATH` if it isn't already there.

          **Manual Download:**

            1. From [Dify's GitHub Releases](https://github.com/langgenius/dify/releases), pick the release that matches your server's Dify version and download two assets:

               * The binary for your platform (`difyctl-v`&lt;version&gt;`-`&lt;os&gt;`-<arch>`)
               * The checksum manifest (`difyctl-v`&lt;version&gt;`-checksums.txt`)

            2. Compute the binary's SHA-256 hash and compare it with the matching entry in the checksums file.

               If the values differ, the download is corrupted or was tampered with; delete it and download again.

                 ```bash macOS / Linux theme={null}
                 shasum -a 256 difyctl-v<version>-<os>-<arch>
                 ```

                 ```powershell Windows theme={null}
                 Get-FileHash difyctl-v<version>-windows-x64.exe
                 ```

            3. Put the binary on your `PATH`:

                 ```bash macOS / Linux theme={null}
                 chmod +x difyctl-v<version>-<os>-<arch>
                 mv difyctl-v<version>-<os>-<arch> ~/.local/bin/difyctl
                 ```

                 ```powershell Windows theme={null}
                 New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\difyctl\bin" | Out-Null
                 Move-Item difyctl-v<version>-windows-x64.exe "$env:LOCALAPPDATA\difyctl\bin\difyctl.exe"
                 ```

        > **💡 Tip:**
>           To customize the install, set any of these environment variables on the install command.
>
>           | Variable          | Description                                                                                                                                                                                                                                            | Example       |
>           | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
>           | `DIFY_VERSION`    | The Dify release tag to install `difyctl` from, matching a tag on [Dify's Releases](https://github.com/langgenius/dify/releases).

Defaults to the latest release; set it to your server's release tag when your server isn't on the latest. | `1.15.0`      |
>           | `DIFYCTL_VERSION` | Pin a specific `difyctl` build. Used only when `DIFY_VERSION` is unset.                                                                                                                                                                                | `0.1.0-alpha` |
>           | `DIFYCTL_PREFIX`  | The install directory (default `~/.local`). The binary lands in `/bin`.                                                                                                                                                                        | `/usr/local`  |
>
>           For example:
>
>
>             ```bash macOS / Linux theme={null}
>             curl -fsSL https://raw.githubusercontent.com/langgenius/dify/main/cli/scripts/install-cli.sh | DIFY_VERSION=1.15.0 sh
>             ```
>
>             ```powershell Windows theme={null}
>             # PowerShell has no inline form; this applies for the rest of your session
>             $env:DIFY_VERSION = "1.15.0"
>             irm https://raw.githubusercontent.com/langgenius/dify/main/cli/scripts/install.ps1 | iex
>             ```
>
>

  1. **Verify the Install**
        ```bash theme={null}
        difyctl version
        ```

        You should see a `Client:` block with the version and platform.

        If you get `command not found` instead, the install directory isn't on your `PATH`. Add it:

          ```bash macOS / Linux theme={null}
          # add to ~/.zshrc or ~/.bashrc; running it inline only lasts until the session ends
          export PATH="$HOME/.local/bin:$PATH"
          ```

          ```powershell Windows theme={null}
          [Environment]::SetEnvironmentVariable('PATH', "$env:LOCALAPPDATA\difyctl\bin;$env:PATH", 'User')
          ```

#### Update

To update `difyctl`, re-run the install script; it replaces the binary in place. To move to a specific Dify version, set `DIFY_VERSION` as above.

#### Uninstall

  ```bash macOS / Linux theme={null}
  rm ~/.local/bin/difyctl
  ```

  ```powershell Windows theme={null}
  Remove-Item -Recurse "$env:LOCALAPPDATA\difyctl"
  ```

To sign out before uninstalling, run [`difyctl auth logout`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#sign-out).

#### Next Steps

With `difyctl` installed, head to the [Quick Start](https://docs.dify.ai/en/cli/quick-start) to sign in and run your first app.

### Integrate Agents

#### Authenticate Where Your Agent Runs

*Put a difyctl session on the server or container where your agent runs, so it can call Dify apps unattended*

**Source:** https://docs.dify.ai/en/cli/integrate-agents/auth-for-agent-deployments

Put a difyctl session on the server or container where your agent runs, so it can call Dify apps unattended

Your agent never logs in. It reuses the `difyctl` session on the machine where it runs. How you get it there depends on the machine:

* **Your own machine**: [sign in](https://docs.dify.ai/en/cli/authenticate) and you're set.
* **A server or VM you can log into**: sign in on it (Option 1).
* **A container, CI runner, or prebaked image**: copy a session in (Option 2).

#### Option 1: Sign In on the Machine

Sign in on the target machine as the account the agent should act as. The agent inherits everything that account can reach.

For Dify Cloud, use `https://cloud.dify.ai` for `--host`; on a self-hosted deployment, use the [console API URL](https://docs.dify.ai/en/self-host/deploy/configuration/environments#console_api_url). Pass `--no-browser` when the machine has no browser:

```bash theme={null}
difyctl auth login --host https://cloud.dify.ai --no-browser
```

`difyctl` prints a one-time code and a verification URL. Open the URL on any device, sign in, and enter the code. The session is written to the machine the moment you approve. For the full walkthrough, see [Authenticate](https://docs.dify.ai/en/cli/authenticate#sign-in).

Confirm it landed:

```bash theme={null}
difyctl auth whoami
```

```text theme={null}
<your-email> (<your-name>)
```

#### Option 2: Copy a Session You Already Have

Use this when you can't sign in on the target itself, like a prebaked image or an ephemeral container.

  1. **Sign in on a machine without an OS keychain**
        Use a headless Linux server or a container. Without a keychain, `difyctl` saves the token to `tokens.yml` in the [config directory](https://docs.dify.ai/en/cli/authenticate#where-your-token-lives), making the entire directory portable.

        Before copying, confirm `tokens.yml` exists in the config directory (`~/.config/difyctl` by default). If it's missing, a keychain captured the token instead, and there's no supported way to export it. Sign in directly on the target with [Option 1](#option-1-sign-in-on-the-machine).

  1. **Copy the config directory to the target**
        After copying, point `difyctl` at it with [`DIFY_CONFIG_DIR`](https://docs.dify.ai/en/cli/reference/environment-variables). For a container, mount the directory at runtime instead of baking it into the image:

        ```bash theme={null}
        docker run \
          -v /path/to/difyctl-config:/config:ro \
          -e DIFY_CONFIG_DIR=/config \
          your-agent-image
        ```

        `tokens.yml` is a live credential. Keep its `0600` permissions and keep it out of images and version control. The mount is read-only because an agent that only runs apps never writes to the config directory.

#### When the Session Expires

A server-expired or revoked session surfaces as exit code 4 with `error.code` `auth_expired`. The agent can't recover on its own: a new session takes a person approving the sign-in, the same one-time-code step as Option 1.

So it should stop and surface the failure for a human to [sign in again](https://docs.dify.ai/en/cli/authenticate#sign-in-again), not retry. See [Handle Errors and Retries](https://docs.dify.ai/en/cli/integrate-agents/error-handling-and-retries-for-agents#branch-on-the-exit-code) for how to branch on it.

To revoke a session you suspect is compromised, run [`auth devices revoke`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#revoke-sessions) from any signed-in machine.

#### Handle Errors and Retries

*Make your agent fail safely on difyctl errors: branch on exit codes, parse the error, detect paused workflows, and retry only what's safe*

**Source:** https://docs.dify.ai/en/cli/integrate-agents/error-handling-and-retries-for-agents

Make your agent fail safely on difyctl errors: branch on exit codes, parse the error, detect paused workflows, and retry only what's safe

Your agent needs four pieces of failure logic to drive `difyctl` safely: read the right channel, branch on the exit code, treat a paused workflow as success, and retry only what's safe to retry.

#### Read the Right Channel

Run every programmatic invocation with `-o json`. The channel discipline is strict and you can build on it:

* **Success**: the payload is on stdout as parseable JSON with no ANSI codes, and stderr is empty.
* **Failure**: stdout is empty, and stderr is a structured JSON object. The entire trimmed stderr parses as JSON.
* **Paused**: a Workflow that stops for human input also exits `0` on the success channel, with `"status": "paused"` on stdout. [Treat it as success](#a-pause-is-success-not-an-error), not failure.

So the parse rule is: exit code first, then `JSON.parse(stdout)` on success and `JSON.parse(stderr)` on failure. See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes#errors) for the error object's fields and a full sample.

#### Branch on the Exit Code

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes#exit-codes) for the full exit-code table. For an agent, the branches that matter:

* **Exit `7`—rate limited**: The server returned a 429. Back off and retry.
* **Exit `4`—auth**: No session, or the session expired. Re-establish the session before doing anything else. Don't retry the same command as-is, which just burns calls. See [Authenticate Where Your Agent Runs](https://docs.dify.ai/en/cli/integrate-agents/auth-for-agent-deployments).
* **Exit `1`—generic or server error**: Network failure, server error, app not found, or an unknown flag or command. Parse the error object and inspect `error.code`. Don't blindly retry.
* **Exit `2`—invalid input**: The CLI rejected a value before any request went out: malformed `--inputs` JSON, a non-UUID app ID, or an out-of-range flag such as `--limit 0`. Fix the call; retrying it unchanged fails the same way.
* **A paused run is exit `0`**: A workflow that hit a human-input step exits `0` with `"status": "paused"` on stdout, not an error. It's [handled separately](#a-pause-is-success-not-an-error).

#### A Pause Is Success, Not an Error

A Workflow or Chatflow app with a human-input step pauses mid-run. The command exits `0` and reports the pause on stdout. There is nothing on stderr to catch. An agent that only checks exit codes will mistake the pause for a completed run, so the completion check must read the payload:

```python theme={null}
import json, subprocess

r = subprocess.run(
    ["difyctl", "run", "app", app_id, "--inputs", json.dumps(inputs), "-o", "json"],
    capture_output=True, text=True,
)
if r.returncode == 0:
    payload = json.loads(r.stdout)
    if payload.get("status") == "paused":
        # Success-with-pending: collect input, then resume with
        # payload["form_token"] and payload["workflow_run_id"].
        ...
```

See [When a Workflow Pauses](https://docs.dify.ai/en/cli/reference/apps#when-a-workflow-pauses) for the full paused payload, the resume command, and the expiry rules. A resumed run can pause again at a later step, so run the same check after every `resume app`.

#### Branch on `error.code`

The error object's `error.code` is a stable machine identifier: the same failure produces the same code across calls, so you write the branching logic once. Group your branches by recovery action rather than enumerating every code:

* **Re-authenticate, then retry**: `not_logged_in`, `auth_expired`. Both exit 4.
* **Retry with backoff**: `network_connection`, `server_5xx`. Transient infrastructure trouble.
* **Don't retry, inspect**: `server_4xx_other`. The server rejected the request: wrong app ID, bad inputs, or insufficient permissions. The `message` carries the server's reason.
* **Fix the invocation**: the usage codes that arrive with exit 2.

The error object also carries a human-readable `hint` with a suggested recovery action. Log it to speed up debugging.

When the failure came from the server, the error object may also include `error.server`, the server's own error body. Its `server.code` (for example `not_found`) distinguishes rejection reasons more finely than `server_4xx_other` if your loop needs that granularity.

#### Retry Deliberately

`difyctl` already retries idempotent requests (GET, PUT, DELETE) on transient failures with exponential backoff. See [Global Flags](https://docs.dify.ai/en/cli/reference/global-flags#http-retries) for the budget and the `--http-retry` override.

What it never retries automatically is POST, and that's the call that matters: every `run app` is a POST. When `run app` fails mid-flight, the CLI doesn't know whether the server already started executing, so by default it won't re-send.

The one opt-in is [`run app --retry-on-limit`](https://docs.dify.ai/en/cli/reference/apps#run-an-app), which retries specifically on a 429 with bounded backoff. It stays off by default because an app run isn't idempotent.

The same applies to your agent's logic: re-running a failed `run app` is a new execution, not a resume of the old one. For a Chatbot, that's usually acceptable (re-ask the question). For a Workflow with side effects, gate the retry on what the workflow does.

Keep agent-side retries for the transient errors above, cap the attempts, and log every retry decision. An agent that silently re-runs writes is the failure mode the [`effect` labels](https://docs.dify.ai/en/cli/reference/help#machine-readable-help) exist to prevent. Every command in `difyctl help -o json` is tagged `read`, `write`, or `destructive`, so your loop can gate auto-retry on the tag and never re-send a `write` blindly.

#### Install the difyctl Skill

*Give your coding agent access to your Dify apps by installing one skill file*

**Source:** https://docs.dify.ai/en/cli/integrate-agents/install-the-difyctl-skill

Give your coding agent access to your Dify apps by installing one skill file

Run [`difyctl skills install`](https://docs.dify.ai/en/cli/reference/skills#install-the-skill) to write a skill file for the coding agents on your machine. The agent picks it up and onboards itself from there.

The installed `SKILL.md` is a bootstrap, not a manual. It tells the agent the one thing that matters: run [`difyctl help -o json`](https://docs.dify.ai/en/cli/reference/help#machine-readable-help) and treat that output as the source of truth.

At runtime, the agent reads the full command surface from the installed `difyctl`.

#### When to Use the Skill

* Your agent runtime reads skills: Claude Code, Codex, OpenCode, Cursor, pi, or anything else that picks up `SKILL.md` files from a skill directory.
* The agent can run shell commands. The skill drives `difyctl` through the agent's shell tool.
* You want zero maintenance: the skill never goes stale, because it lists no commands.

If your runtime doesn't read skills, your agent can still drive `difyctl` directly by reading [`difyctl help -o json`](https://docs.dify.ai/en/cli/reference/help#machine-readable-help) at runtime.

#### Prerequisites

* [Install](https://docs.dify.ai/en/cli/install) `difyctl` and [sign in](https://docs.dify.ai/en/cli/authenticate) on the machine the agent runs on, so it can reuse your session. For a server or container, see [Authenticate Where Your Agent Runs](https://docs.dify.ai/en/cli/integrate-agents/auth-for-agent-deployments).
* Use a coding agent that reads skills and can run shell commands. A sandboxed agent with no shell access can't use the skill.
* Launch the agent at least once before installing, so its config directory exists for `difyctl skills install` to find.

#### Steps

  1. **Preview where the skill will land**
        Without `--yes`, the command is a dry run:

        ```bash theme={null}
        difyctl skills install
        ```

        ```text theme={null}
        Detected 1 agent: claude-code

        would write to claude-code: /Users/you/.claude/skills/difyctl/SKILL.md

        Re-run with --yes to write.
        Agent not listed? Install into its directory with `difyctl skills install <dir>`.
        ```

  1. **Write the skill**
        `--yes` writes to every detected agent. Pass `--agent <name>` to write to just one.

        ```bash theme={null}
        difyctl skills install --yes
        ```

        ```text theme={null}
        wrote /Users/you/.claude/skills/difyctl/SKILL.md
        ```

  1. **Start a fresh agent session**
        Start a new session so the agent indexes the skill it just received.

> **ℹ️ Info:**
>   See the [Skills reference page](https://docs.dify.ai/en/cli/reference/skills) for detection, target paths per agent, and the `--agent`, `--stdout`, and explicit-directory forms.

#### Test

The install prints the path it wrote; open that file to confirm the skill is there. Then check that the agent actually uses it:

1. **Discovery**: In a fresh session, ask the agent: *"What can you do with `difyctl`?"* A correctly onboarded agent runs `difyctl help -o json` and answers from its output rather than guessing commands.
2. **End to end**: Ask the agent to list your Dify apps and run one. Watch for `difyctl get app -o json` followed by a `describe`/`run` sequence with real IDs from the list.
3. **Pause handling**: If you have a Workflow or Chatflow app with a human-input step, ask the agent to run it. A paused run [exits 0 and reports `"status": "paused"` on stdout](https://docs.dify.ai/en/cli/reference/apps#when-a-workflow-pauses). The agent should recognize the pause and offer to resume, not report a failure or retry the run.

#### Troubleshooting

| Problem                                         | What to do                                                                                                                                                                                        |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The agent isn't detected                        | Its config directory (for example `~/.claude`) doesn't exist until the agent has run at least once. Launch it once, or target the directory explicitly with `difyctl skills install `&lt;dir&gt;` --yes`. |
| The skill is installed but the agent ignores it | Most agents index skills at session start, so start a new session. If it still doesn't load, point the installer at the directory your agent reads skills from.                                   |
| Commands fail with exit code 4                  | The agent has no session to reuse. Sign in on its machine first: see [Authenticate Where Your Agent Runs](https://docs.dify.ai/en/cli/integrate-agents/auth-for-agent-deployments).                                   |
| The skill is older than the CLI                 | The skill carries a version stamp and tells the agent to compare it against `difyctl version`. If they differ, re-run `difyctl skills install --yes` to overwrite it.                             |

For everything else, see the full [Troubleshooting](https://docs.dify.ai/en/cli/troubleshooting) page.

#### Integrate Your Agents with Dify Apps

*Call your Dify apps from any coding agent through difyctl, with no API to integrate or SDK to install*

**Source:** https://docs.dify.ai/en/cli/integrate-agents/overview

Call your Dify apps from any coding agent through difyctl, with no API to integrate or SDK to install

Your agent can call your Dify apps as tools. It runs `difyctl` as an ordinary subprocess and reads the JSON it prints back. `difyctl` describes itself, so the agent discovers your apps, runs them, and reads the results on its own.

#### What the Agent Does on Its Own

The agent drives a four-step loop, with no glue code from you:

1. **Discover** the apps in your workspace.
2. **Inspect** one to learn the inputs it expects.
3. **Run** it with those inputs.
4. **Parse** the JSON result.

The agent doesn't work from a hard-coded command list. `difyctl` describes itself through [`difyctl help -o json`](https://docs.dify.ai/en/cli/reference/help#machine-readable-help), and the agent reads that at runtime, so it always tracks the current CLI.

#### Before You Start: Sign In Where the Agent Runs

The agent doesn't log in. It runs `difyctl` and reuses whatever session exists on the machine where it runs, so get a session onto that machine first:

* **On your own machine**: a one-time browser [sign-in](https://docs.dify.ai/en/cli/authenticate).
* **On a server or in a container**: sign in on the machine, or copy a session onto it. See [Authenticate Where Your Agent Runs](https://docs.dify.ai/en/cli/integrate-agents/auth-for-agent-deployments) for details.

#### Onboard Your Agent

The agent learns `difyctl` from `difyctl help -o json`. Pointing it there is the only setup, and how depends on the agent:

* **Reads skills** (Claude Code, Codex, and similar): [install the `difyctl` skill](https://docs.dify.ai/en/cli/integrate-agents/install-the-difyctl-skill). One command writes a small file that points the agent at `difyctl help -o json`, and it onboards itself from there. No integration code.
* **Doesn't read skills**: point it there yourself. Add a line to the agent's system prompt or instructions, such as "to work with Dify, run `difyctl help -o json` and use the commands it lists." That's the hand-off the skill otherwise does for you.

### Overview

#### Overview

*Run your Dify apps from terminals, scripts, CI pipelines, and AI agents with the official Dify command-line interface `difyctl`*

**Source:** https://docs.dify.ai/en/cli/overview

Run your Dify apps from terminals, scripts, CI pipelines, and AI agents with the official Dify command-line interface `difyctl`

You build Dify apps in the browser, but the work that needs them often lives somewhere else: a shell script, a CI pipeline, an AI agent deciding which tool to call.

Dify CLI (difyctl) closes that gap: anything that can run a shell command can run your Dify apps.

#### What You Can Do

* Run any Dify app from your terminal and capture its output.
* List the apps in your workspace and inspect the inputs each one expects.
* Stream long responses live, or get structured JSON for scripting.
* Sign in once with OAuth, then automate without storing passwords or API keys in scripts.
* Let your AI agents discover and call your Dify apps as tools.

#### Get Started

First, [install `difyctl`](https://docs.dify.ai/en/cli/install). Then follow the [Quick Start](https://docs.dify.ai/en/cli/quick-start) to sign in and run your first app.

> **💡 Tip:**
>   Want an AI agent to run your Dify apps as tools? Once `difyctl` is installed, start with [Integrate Your Agents with Dify](https://docs.dify.ai/en/cli/integrate-agents/overview).

### Quick Start

#### Quick Start

*Run your first Dify app from the command line in under 5 minutes*

**Source:** https://docs.dify.ai/en/cli/quick-start

Run your first Dify app from the command line in under 5 minutes

Before you start, make sure `difyctl` is [installed](https://docs.dify.ai/en/cli/install).

#### Step 1: Sign In

1. Sign in to your Dify host.

   For Dify Cloud, use `https://cloud.dify.ai`; on a self-hosted deployment, use the [console API URL](https://docs.dify.ai/en/self-host/deploy/configuration/environments#console_api_url).

   ```bash theme={null}
   difyctl auth login --host https://cloud.dify.ai
   ```

   `difyctl` prints a one-time code and a verification URL, then waits:

   ```text theme={null}
   ! Copy this one-time code: WDJP-XKLM
     Open: https://cloud.dify.ai/device
   ```

2. Open the URL in a browser, enter the code, and sign in. Return to the terminal and you'll see:

   ```text theme={null}
   ✓ Logged in to cloud.dify.ai as <your-email> (<your-name>)
     Workspace: <your-workspace>
   ```

#### Step 2: Find Your App

List the apps in your workspace:

```bash theme={null}
difyctl get app
```

You should see something like this:

```text theme={null}
NAME          ID                                    MODE      UPDATED
Customer FAQ  0a1b2c3d-4e5f-6789-abcd-ef0123456789  chat      2026-06-08T03:14:27.521839
Daily Report  7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b  workflow  2026-06-05T22:41:09.812016
```

Copy the ID of the app you want to run. The examples below use the two IDs from this table.

#### Step 3: Run Your App

How you pass input depends on the app type.

  **Chatbot / Chatflow / Agent / Text Generator:**

    Pass your message as a positional argument:

    ```bash theme={null}
    difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?"
    ```

    The reply prints to stdout. For Chatbot, Chatflow, and Agent apps, a hint also prints to stderr so you can continue the same conversation later:

    ```text theme={null}
    Our business hours are Monday through Friday, 9am to 6pm PT.

    hint: continue this conversation with --conversation 4f7d8c2a-9b1e-4c6d-8a3f-5e2b7c9d0a1f
    ```

  **Workflow:**

    Pass inputs as a single JSON object with `--inputs`:

    ```bash theme={null}
    difyctl run app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --inputs '{"topic":"quarterly report","audience":"executives"}'
    ```

    The workflow's outputs print to stdout as JSON:

    ```json theme={null}
    {"summary":"Q3 revenue grew 14% YoY...","sections":["revenue","costs","outlook"]}
    ```

#### Next Steps

* **The everyday commands, copy-paste ready**: [Common Tasks](https://docs.dify.ai/en/cli/common-tasks)
* **Where your token lives and how sessions work**: [Authenticate](https://docs.dify.ai/en/cli/authenticate)
* **Everything else you can do with `difyctl`**: [Command Index](https://docs.dify.ai/en/cli/reference/command-index)

### Reference

#### Apps

*List, inspect, run, resume, export, and import your Dify apps from the CLI*

**Source:** https://docs.dify.ai/en/cli/reference/apps

List, inspect, run, resume, export, and import your Dify apps from the CLI

Every app task maps to one command, and all of them accept the [global flags](https://docs.dify.ai/en/cli/reference/global-flags).

* [`difyctl get app`](#list-your-apps) lists your apps
* [`describe app`](#inspect-an-app) shows one app's details and inputs
* [`run app`](#run-an-app) invokes one
* [`resume app`](#resume-a-paused-workflow) continues a workflow that [paused for human input](#when-a-workflow-pauses)
* [`export studio-app`](#export-an-app) / [`import studio-app`](#import-an-app) exports / imports apps as DSL files

#### List Your Apps

```text theme={null}
difyctl get app [app-id] [flags]
```

> **💡 Tip:**
>   For the everyday invocations, see [Find Your Apps](https://docs.dify.ai/en/cli/common-tasks#find-your-apps) in Common Tasks.

##### Arguments

* `[app-id]`: optional. The ID of one app to show. Omit it to list every app in your workspace.

##### Flags

| Flag                                        | Type    | Default          | Description                                                                                                                                                                                                       |
| :------------------------------------------ | :------ | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--name <substring>`                        | string  | none             | Filter to apps whose name contains this text.                                                                                                                                                                     |
| `--mode <mode>`                             | string  | none             | Filter by app type, named by its API mode: * `chat` (Chatbot)
* `advanced-chat` (Chatflow)
* `agent-chat` (Agent)
* `workflow` (Workflow)
* `completion` (Text Generator)
 |
| `--page <n>`                                | integer | `1`              | Page number.                                                                                                                                                                                                      |
| `--limit <n>`                               | integer | `20`             | Page size, 1 to 200. The flag wins, then [`DIFY_LIMIT`](https://docs.dify.ai/en/cli/reference/environment-variables).                                                                                                                 |
| `--workspace <id>` **[Cloud]**     | string  | active workspace | Run against another workspace for this invocation only.

For how `difyctl` resolves the workspace, see [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace).     |
| `-A, --all-workspaces` **[Cloud]** | boolean | `false`          | List apps across every workspace your token can see.                                                                                                                                                              |
| `-o `                               | string  | none             | Output format: `json`, `yaml`, `name`, or `wide`. Omit the flag for the default table.                                                                                                                            |

##### Examples

List the apps in your workspace:

```bash theme={null}
difyctl get app
```

List apps across every workspace you belong to:

```bash theme={null}
difyctl get app -A
```

Find Workflow apps whose name contains "report":

```bash theme={null}
difyctl get app --name report --mode workflow
```

Print app IDs only, one per line, for shell loops:

```bash theme={null}
difyctl get app -o name
```

##### Output

| Format               | What stdout gets                                                                                                                                                   |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| default              | An aligned table. The `MODE` column is each app's API mode name (see [`--mode`](#list-your-apps) for the mapping to app types).                                    |
| `-o wide`            | The table plus a `WORKSPACE` column.                                                                                                                               |
| `-o json`, `-o yaml` | A `data` array of the apps, plus the paging fields `page` (current page), `limit` (page size), `total` (apps matched), and `has_more` (whether more pages remain). |
| `-o name`            | The app IDs, one per line.                                                                                                                                         |

Default table:

```text theme={null}
NAME          ID                                    MODE      UPDATED
Customer FAQ  0a1b2c3d-4e5f-6789-abcd-ef0123456789  chat      2026-06-08T03:14:27.521839
Daily Report  7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b  workflow  2026-06-05T22:41:09.812016
```

##### Exit Codes

| Code | Meaning                                           |
| :--- | :------------------------------------------------ |
| `0`  | Success                                           |
| `1`  | Network or server error                           |
| `2`  | Usage error, such as a `--limit` outside 1 to 200 |
| `4`  | Authentication failure                            |
| `7`  | Rate limited (HTTP 429)                           |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Inspect an App

```text theme={null}
difyctl describe app <app-id> [flags]
```

`describe app` answers the question you have before running an unfamiliar app: what type of app is it, is its API enabled, and what inputs does it expect.

##### Arguments

* `<app-id>`: required. The ID of the app to inspect.

##### Flags

| Flag          | Type    | Default | Description                                                                                |
| :------------ | :------ | :------ | :----------------------------------------------------------------------------------------- |
| `--refresh`   | boolean | `false` | Bypass the local app-info cache and fetch fresh details. Use after an app was republished. |
| `-o ` | string  | `text`  | Output format: `json`, `yaml`, or `text`.                                                  |

##### Examples

Inspect an app before running it:

```bash theme={null}
difyctl describe app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b
```

Extract the input schema for building `--inputs` programmatically:

```bash theme={null}
difyctl describe app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b -o json | jq '.input_schema'
```

Re-fetch after republishing the app:

```bash theme={null}
difyctl describe app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --refresh
```

##### Output

| Format               | What stdout gets                                                                   |
| :------------------- | :--------------------------------------------------------------------------------- |
| default (`text`)     | An aligned field block, then the app's parameters (including the user input form). |
| `-o json`, `-o yaml` | Three top-level keys: `info`, `parameters`, and `input_schema` (detailed below).   |

Default text view:

```text theme={null}
Name:        Daily Report
ID:          7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b
Mode:        workflow
Updated:     2026-06-05T22:41:09.812016
Service API: true
Parameters:
  {
    "opening_statement": null,
    "suggested_questions": [],
    "user_input_form": [
      {
        "text-input": {
          "label": "topic",
          "variable": "topic",
          "required": true,
          "default": ""
        }
      }
    ],
    "file_upload": null,
    "system_parameters": {
      "file_size_limit": 15,
      "image_file_size_limit": 10,
      "audio_file_size_limit": 50,
      "video_file_size_limit": 100,
      "workflow_file_upload_limit": 10
    }
  }
```

A `Description:` row appears when the app has one, and an `Agent: true` row when the app is agentic.

Under `-o json`, the three keys are:

* `info` - the metadata fields shown above, from `Name` to `Service API`
* `parameters` - the parameters block shown above
* `input_schema` - a normalized list of the app's inputs, the field the `jq '.input_schema'` example reads

##### Exit Codes

| Code | Meaning                                          |
| :--- | :----------------------------------------------- |
| `0`  | Success                                          |
| `1`  | Network or server error, including app not found |
| `2`  | Usage error, including a non-UUID `<app-id>`     |
| `4`  | Authentication failure                           |
| `7`  | Rate limited (HTTP 429)                          |

#### Run an App

```text theme={null}
difyctl run app <app-id> [message] [flags]
```

`run app` is one command for all app types. The CLI reads the app's type and dispatches to the right endpoint. What changes is how you pass input and the response shape:

* **Chatbot, Chatflow, Agent**: take a positional message, print the reply to stdout, and print a conversation hint to stderr.
* **Text Generator**: takes a positional message and prints the completion to stdout. No conversational state, no hint.
* **Workflow**: takes a JSON object via `--inputs` and prints its outputs to stdout. A workflow whose output is a single string prints it raw. Anything else prints as compact JSON.

##### Arguments

* `<app-id>`: required. The ID of the app to run, from [`get app`](#list-your-apps).
* `[message]`: the user message, for Chatbot, Chatflow, Agent, and Text Generator apps. Workflow apps reject a positional message, so pass their inputs with `--inputs`.

##### Flags

| Flag                                    | Type               | Default          | Description                                                                                                                                                                                                   |
| :-------------------------------------- | :----------------- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--inputs <json>`                       | string             | none             | Input variables as one JSON object, e.g. `--inputs '{"topic":"Q3"}'`. Required for Workflow apps. Mutually exclusive with `--inputs-file`.                                                                    |
| `--inputs-file `                  | string             | none             | Read the inputs object from a JSON file instead.                                                                                                                                                              |
| `--file <key=value>`                    | string, repeatable | none             | Named file input. `key=@path` uploads a local file. `key=https://…` passes a remote URL without uploading. The key is the input variable name.                                                                |
| `--conversation <id>`                   | string             | none             | Continue an existing conversation. The ID comes from the stderr hint or the JSON response of an earlier run.                                                                                                  |
| `--workflow-id <id>`                    | string             | none             | Pin the run to a specific published workflow version. Workflow and Chatflow apps only.                                                                                                                        |
| `--stream`                              | boolean            | `false`          | Print the output live as it's generated, instead of all at once at the end.                                                                                                                                   |
| `--think`                               | boolean            | `false`          | Print the model's thinking to stderr when the model exposes it, whether as inline `` blocks or a separate reasoning stream.

Without this flag, that thinking is hidden.                     |
| `--retry-on-limit`                      | boolean            | `false`          | On a 429 rate limit, wait and retry the run instead of failing with exit `7`. Off by default, since a run isn't idempotent.                                                                                   |
| `--workspace <id>` **[Cloud]** | string             | active workspace | Run against another workspace for this invocation only.

For how `difyctl` resolves the workspace, see [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace). |
| `-o `                           | string             | `text`           | Output format: `json`, `yaml`, or `text`.                                                                                                                                                                     |

##### Examples

Send a message to a Chatbot, Chatflow, Agent, or Text Generator app:

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?"
```

Run a Workflow app with structured inputs:

```bash theme={null}
difyctl run app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --inputs '{"topic":"quarterly report","audience":"executives"}'
```

Attach a local file to a file-type input variable:

```bash theme={null}
difyctl run app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --inputs '{"topic":"contract review"}' --file document=@./contract.pdf
```

Continue an earlier conversation:

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "And on weekends?" --conversation 4f7d8c2a-9b1e-4c6d-8a3f-5e2b7c9d0a1f
```

Get the raw response as JSON for scripts and agents:

```bash theme={null}
difyctl run app 0a1b2c3d-4e5f-6789-abcd-ef0123456789 "What are your business hours?" -o json | jq -r '.answer'
```

##### Output

| Format               | What stdout gets                                                                                                                                               |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| default (`text`)     | The reply (Chatbot, Chatflow, Agent, Text Generator) or the workflow's output, as plain text.                                                                  |
| `-o json`, `-o yaml` | The full server payload, including `answer` and `conversation_id` for conversational apps, plus the model's reasoning under `metadata.reasoning` when present. |

The response body goes to stdout. Everything else (hints, progress, errors) goes to stderr, so piping and redirection stay clean. After a reply from a Chatbot, Chatflow, or Agent app, stderr carries the conversation hint:

```text theme={null}
hint: continue this conversation with --conversation 4f7d8c2a-9b1e-4c6d-8a3f-5e2b7c9d0a1f
```

With `--stream`, output prints incrementally as the server produces it. If a run fails with HTTP 422 right after an app was republished, the CLI clears its app-metadata cache and hints to run the command again.

Errors print to stderr. Under `-o json` they arrive as a structured JSON object with a stable `code` field. See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the error shape.

##### Exit Codes

| Code | Meaning                                                                                |
| :--- | :------------------------------------------------------------------------------------- |
| `0`  | Success, including a workflow that [paused for human input](#when-a-workflow-pauses)   |
| `1`  | Network or server error, including app not found                                       |
| `2`  | Usage error: invalid `--inputs` JSON, or a positional message passed to a Workflow app |
| `4`  | Authentication failure                                                                 |
| `7`  | Rate limited (HTTP 429)                                                                |

##### When a Workflow Pauses

Workflow and Chatflow apps can include human-input steps. When a run reaches one, it pauses instead of finishing: the command **exits 0** (a pause is not a failure), prints the pause to stdout, and prints a ready-to-run resume command to stderr:

```text theme={null}
! Workflow paused — input required
  Node:    Review draft
  Message: Approve the report before it is published.
  Actions: [approve] Approve  [reject] Reject
  Inputs:   - comment — Reviewer comment

! workflow paused — resume with:
  difyctl resume app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b k3J9mQ2xWv8pL5nR7tY4bA --workflow-run-id 8e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b --action approve
```

With `-o json`, stdout gets the pause as a JSON object instead:

```json theme={null}
{
  "status": "paused",
  "app_id": "7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b",
  "task_id": "c4a8e2f6-1b3d-4a5c-9e7f-2d8b6c0a4e1f",
  "workflow_run_id": "8e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b",
  "form_id": "5d9c3b7a-2e4f-4c6d-8b0a-1f3e5d7c9b2a",
  "node_id": "1749876543210",
  "node_title": "Review draft",
  "form_token": "k3J9mQ2xWv8pL5nR7tY4bA",
  "form_content": "Approve the report before it is published.",
  "inputs": [
    {
      "output_variable_name": "comment",
      "label": "Reviewer comment",
      "type": "text-input",
      "required": false
    }
  ],
  "actions": [
    { "id": "approve", "title": "Approve" },
    { "id": "reject", "title": "Reject" }
  ],
  "display_in_ui": true,
  "resolved_default_values": {},
  "expiration_time": 1781712000
}
```

For scripts and agents: a paused run and a completed run both exit 0, so don't branch on the exit code. Run workflows with `-o json` and check stdout for `"status": "paused"`. Three fields drive the resume: `form_token`, `workflow_run_id`, and (when the form offers more than one action) the action `id`. Forms expire at `expiration_time` (Unix epoch seconds).

When the workflow delivers its form through email or another external channel, `form_token` is `null` and the run can't be resumed from the CLI.

#### Resume a Paused Workflow

```text theme={null}
difyctl resume app <app-id>  --workflow-run-id <id> [flags]
```

`resume app` submits the form a paused workflow is waiting on, then attaches to the run and prints its output exactly like `run app`.

##### Arguments

* `<app-id>`: required. The `app_id` from the pause payload.
* ``: required. The `form_token` from the pause payload. Tokens are single-use, so resuming with an already-consumed token returns an error.

##### Flags

| Flag                     | Type    | Default       | Description                                                                                                                                                                               |
| :----------------------- | :------ | :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--workflow-run-id <id>` | string  | required      | The `workflow_run_id` from the pause payload.                                                                                                                                             |
| `--action <id>`          | string  | auto-selected | Which form action to take, by `id` from the pause payload's `actions`.

Optional when the form has exactly one action, required when it has several.                            |
| `--inputs <json>`        | string  | none          | Values for the form's inputs as one JSON object, keyed by each input's `output_variable_name`.

Mutually exclusive with `--inputs-file`.                                        |
| `--inputs-file `   | string  | none          | Read the form values from a JSON file instead.                                                                                                                                            |
| `--with-history`         | boolean | `false`       | Replay the output of already-executed nodes before attaching to the live stream.                                                                                                          |
| `--stream`               | boolean | `false`       | Print the output live as it's generated, instead of all at once at the end.                                                                                                               |
| `--think`                | boolean | `false`       | Print the model's thinking to stderr when the model exposes it, whether as inline `` blocks or a separate reasoning stream.

Without this flag, that thinking is hidden. |
| `-o `            | string  | `text`        | Output format: `json`, `yaml`, or `text`.                                                                                                                                                 |

##### Examples

Approve a single-action form, providing its input values:

```bash theme={null}
difyctl resume app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b k3J9mQ2xWv8pL5nR7tY4bA --workflow-run-id 8e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b --inputs '{"comment":"Looks good"}'
```

Pick an action when the form offers several:

```bash theme={null}
difyctl resume app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b k3J9mQ2xWv8pL5nR7tY4bA --workflow-run-id 8e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b --action reject --inputs '{"comment":"Numbers need a re-check"}'
```

Read the form values from a file:

```bash theme={null}
difyctl resume app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b k3J9mQ2xWv8pL5nR7tY4bA --workflow-run-id 8e1f2a3b-4c5d-6e7f-8a9b-0c1d2e3f4a5b --inputs-file form.json
```

##### Output

| Format               | What stdout gets                                                                           |
| :------------------- | :----------------------------------------------------------------------------------------- |
| default (`text`)     | The workflow's output as the run completes. stderr confirms the submission and the finish. |
| `-o json`, `-o yaml` | The run result as one document, just like `run app` (a pause payload if it pauses again).  |

In the default text output, stderr confirms the submission, the workflow's output prints to stdout as the run completes, and stderr confirms the finish:

```text theme={null}
✓ form submitted
  workflow execution resumed
✓ workflow finished
```

A resumed workflow can pause again at a later human-input node. You then get a new pause payload and resume again with the new token.

##### Exit Codes

| Code | Meaning                                                                                       |
| :--- | :-------------------------------------------------------------------------------------------- |
| `0`  | Success, including the run pausing again at a later node                                      |
| `1`  | Error, including a consumed form token, or omitting `--action` on a form with several actions |
| `2`  | Usage error                                                                                   |
| `4`  | Authentication failure                                                                        |
| `7`  | Rate limited (HTTP 429)                                                                       |

#### Export an App

```text theme={null}
difyctl export studio-app <app-id> [flags]
```

`export studio-app` writes the app's full definition as a DSL YAML document, for versioning, backup, or [importing](#import-an-app) elsewhere.

For Workflow and Chatflow apps, export returns the current draft, not the published version that `run app` executes. Use `--workflow-id` to export a specific published version instead. Chatbot, Agent, and Text Generator apps export the published version.

##### Arguments

* `<app-id>`: required. The ID of the app to export, from [`get app`](#list-your-apps).

##### Flags

| Flag                                    | Type    | Default          | Description                                                                                                                                                                                                   |
| :-------------------------------------- | :------ | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-o, --output `                   | string  | none             | Write the DSL to this file instead of stdout.

On this command, `-o` is the output file path, not the output-format selector.                                                                       |
| `--include-secret`                      | boolean | `false`          | Include encrypted secret values in the exported DSL.                                                                                                                                                          |
| `--workflow-id <id>`                    | string  | none             | Export a specific published workflow version by ID, instead of the default draft.

Workflow and Chatflow apps only.                                                                                 |
| `--workspace <id>` **[Cloud]** | string  | active workspace | Run against another workspace for this invocation only.

For how `difyctl` resolves the workspace, see [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace). |

##### Examples

Print an app's DSL to stdout:

```bash theme={null}
difyctl export studio-app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b
```

Write it to a file:

```bash theme={null}
difyctl export studio-app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --output ./daily-report.yaml
```

Export a specific published version:

```bash theme={null}
difyctl export studio-app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --workflow-id c7e4a1b9-3f82-4d6a-9e15-0b8c2d7f4a63
```

Export with secret values included:

```bash theme={null}
difyctl export studio-app 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b --include-secret
```

##### Output

The DSL YAML document prints to stdout: a `kind: app` header, a `version` field, and the full app definition. With `--output`, the same content is written to the file and stderr confirms it:

```text theme={null}
DSL written to ./daily-report.yaml
```

##### Exit Codes

| Code | Meaning                                          |
| :--- | :----------------------------------------------- |
| `0`  | Success                                          |
| `1`  | Network or server error, including app not found |
| `2`  | Usage error, including a missing `<app-id>`      |
| `4`  | Authentication failure                           |
| `7`  | Rate limited (HTTP 429)                          |

#### Import an App

```text theme={null}
difyctl import studio-app (--from-file  | --from-url <url>) [flags]
```

`import studio-app` creates an app from a DSL YAML document, or overwrites an existing one with `--app-id`.

For Workflow and Chatflow apps, it writes the definition to the app's draft. `run app` uses the published version, so publish the app in Dify after importing for the change to take effect.

##### Flags

| Flag                                    | Type   | Default          | Description                                                                                                                                                                                                   |
| :-------------------------------------- | :----- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-f, --from-file `                | string | none             | Import DSL from a local file. Exactly one of `--from-file` or `--from-url` is required.                                                                                                                       |
| `--from-url <url>`                      | string | none             | Import DSL from an HTTP(S) URL.                                                                                                                                                                               |
| `--name <name>`                         | string | from DSL         | Override the app name.                                                                                                                                                                                        |
| `--description <text>`                  | string | from DSL         | Override the app description.                                                                                                                                                                                 |
| `--app-id <id>`                         | string | none             | Overwrite an existing app instead of creating a new one.

Workflow and Chatflow apps only.                                                                                                          |
| `--icon-type <type>`                    | string | from DSL         | Override the icon type.                                                                                                                                                                                       |
| `--icon <icon>`                         | string | from DSL         | Override the icon.                                                                                                                                                                                            |
| `--icon-background <color>`             | string | from DSL         | Override the icon background color.                                                                                                                                                                           |
| `--workspace <id>` **[Cloud]** | string | active workspace | Import into another workspace for this invocation only.

For how `difyctl` resolves the workspace, see [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace). |

##### Examples

Import an app from a local DSL file:

```bash theme={null}
difyctl import studio-app --from-file ./daily-report.yaml
```

Import under a different name:

```bash theme={null}
difyctl import studio-app --from-file ./daily-report.yaml --name "Daily Report (staging)"
```

Overwrite an existing app with an updated DSL:

```bash theme={null}
difyctl import studio-app --from-file ./daily-report.yaml --app-id 7f3e9a2b-1c4d-4e8f-9a0b-2d5c8e1f4a7b
```

Import directly from a URL:

```bash theme={null}
difyctl import studio-app --from-url https://example.com/templates/daily-report.yaml
```

##### Output

All status lines go to stderr; stdout stays empty. On success, stderr reports the new app's ID:

```text theme={null}
Import completed: app 9b4f2c8e-6a1d-4e3f-b7a5-0c8d2e6f4a9b
```

If the DSL was written for a different DSL version, the CLI confirms it for you and notes both versions on stderr.

If the app depends on plugins that aren't installed in the workspace, stderr lists them under `Missing plugin dependencies` after the import. Install them before using the app.

##### Exit Codes

| Code | Meaning                                                                                  |
| :--- | :--------------------------------------------------------------------------------------- |
| `0`  | Success, including imports with warnings                                                 |
| `1`  | Error, including a missing or conflicting `--from-file`/`--from-url`, or a failed import |
| `2`  | Usage error, including a `--from-file` path that doesn't exist                           |
| `4`  | Authentication failure                                                                   |
| `7`  | Rate limited (HTTP 429)                                                                  |

#### Auth and Contexts

*Sign in, manage sessions, and switch between saved hosts and accounts*

**Source:** https://docs.dify.ai/en/cli/reference/auth-and-contexts

Sign in, manage sessions, and switch between saved hosts and accounts

`difyctl` can hold sign-ins for several Dify hosts and accounts at once. Each host and account pair is a context: its metadata lives in `hosts.yml` in the [config directory](https://docs.dify.ai/en/cli/reference/environment-variables), and its bearer token lives in your OS credential store (with a protected file fallback).

Each task maps to one command:

* [`difyctl auth login`](#sign-in) signs you in to a host
* [`auth whoami`](#check-your-active-identity) prints the identity you're signed in as
* [`auth list`](#list-your-saved-contexts) lists your saved contexts
* [`auth logout`](#sign-out) signs you out of the active host
* [`use host`](#switch-the-active-host) / [`use account`](#switch-the-active-account) switch the active context
* [`auth devices list`](#list-your-active-sessions) lists your active sessions
* [`auth devices revoke`](#revoke-sessions) revokes sessions you don't recognize

For the step-by-step sign-in walkthrough, see [Authenticate](https://docs.dify.ai/en/cli/authenticate).

#### Sign In

```text theme={null}
difyctl auth login [flags]
```

`auth login` runs the OAuth 2.0 device flow: it prints a one-time code and a verification URL, opens the URL in your browser, and waits for you to approve the sign-in there. The CLI never sees your password.

##### Flags

| Flag           | Type    | Default | Description                                                                                                                                                                                                                                                                                                                                                                                |
| :------------- | :------ | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--host <url>` | string  | none    | The Dify host to sign in to: * For Dify Cloud, use `https://cloud.dify.ai`.
* On self-hosted Dify, use the [console API URL](https://docs.dify.ai/en/self-host/deploy/configuration/environments#console_api_url).
A URL without a scheme gets `https://`.

In a terminal, omit it and enter your host; in a non-interactive session (script, CI, pipe), the flag is required. |
| `--no-browser` | boolean | false   | Don't auto-open the browser; print the verification URL only.                                                                                                                                                                                                                                                                                                                              |
| `--insecure`   | boolean | false   | Allow `http://` hosts, and accept `https://` hosts whose TLS certificate is self-signed or invalid (local development only).                                                                                                                                                                                                                                                               |

##### Examples

Sign in to your Dify host:

```bash theme={null}
difyctl auth login --host https://cloud.dify.ai
```

Sign in from an SSH session, opening the verification URL on another device:

```bash theme={null}
difyctl auth login --no-browser
```

##### Output

The code prompt goes to stderr, then a spinner waits for the browser-side approval:

```text theme={null}
! Copy this one-time code: WDJP-XKLM
  Open: https://cloud.dify.ai/device
```

On success, the confirmation goes to stdout:

```text theme={null}
✓ Logged in to cloud.dify.ai as <your-email> (<your-name>)
  Workspace: <your-workspace>
```

The `Workspace:` line is your default workspace.

Each sign-in also registers a server-side session, labeled `difyctl on <hostname>`. Run [`auth devices list`](#list-your-active-sessions) to see all your sessions. Signing in to a host you're already signed in to refreshes that context's stored token.

##### Exit Codes

| Code | Meaning                                                                                                                                                                                                                                         |
| :--- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`  | Signed in                                                                                                                                                                                                                                       |
| `1`  | Network or server error                                                                                                                                                                                                                         |
| `2`  | Usage error, such as a missing `--host` outside a terminal or a non-`https` host without `--insecure`                                                                                                                                           |
| `4`  | The sign-in was denied (`access_denied`), or the code expired before you approved it (`expired_token`)                                                                                                                                          |
| `6`  | A version mismatch: the server is too old for this `difyctl` (checked before the session is saved), or this `difyctl` is too old for the server (HTTP `426`). Also when the server has no device-flow sign-in endpoint (`unsupported_endpoint`) |
| `7`  | Rate limited (HTTP 429)                                                                                                                                                                                                                         |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Check Your Active Identity

```text theme={null}
difyctl auth whoami [flags]
```

`auth whoami` prints who the active context belongs to. It reads the stored context without contacting the server, so it answers "which identity is active", not "is the token still valid". It exits `0` even if the session has expired server-side.

##### Flags

| Flag     | Type    | Default | Description                               |
| :------- | :------ | :------ | :---------------------------------------- |
| `--json` | boolean | false   | Emit JSON instead of the plain-text line. |

##### Examples

```bash theme={null}
difyctl auth whoami
```

For scripts:

```bash theme={null}
difyctl auth whoami --json
```

##### Output

```text theme={null}
<your-email> (<your-name>)
```

The `--json` output is a single line with `id`, `email`, and `name`:

```json theme={null}
{"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","email":"<your-email>","name":"<your-name>"}
```

##### Exit Codes

| Code | Meaning                         |
| :--- | :------------------------------ |
| `0`  | An active context exists        |
| `4`  | Not signed in (`not_logged_in`) |

#### List Your Saved Contexts

```text theme={null}
difyctl auth list [flags]
```

`auth list` shows every stored host and account pair and marks the active one. Like `auth whoami`, it is purely local and never contacts the server.

##### Flags

| Flag          | Type   | Default | Description                                                                    |
| :------------ | :----- | :------ | :----------------------------------------------------------------------------- |
| `-o ` | string | none    | Output format: `json`, `yaml`, or `name`. Omit the flag for the default table. |

##### Examples

```bash theme={null}
difyctl auth list
```

##### Output

| Format               | What stdout gets                                                             |
| :------------------- | :--------------------------------------------------------------------------- |
| default              | A table of your contexts: host, account, and an active marker.               |
| `-o json`, `-o yaml` | A `contexts` array, each entry with `host`, `account`, `name`, and `active`. |
| `-o name`            | The account emails, one per line.                                            |

Default table:

```text theme={null}
HOST                    ACCOUNT                      ACTIVE
cloud.dify.ai           you@company.com (Your Name)  *
dify.internal.acme.com  you@acme.com (Your Name)
```

`-o json`:

```json theme={null}
{
  "contexts": [
    {
      "host": "cloud.dify.ai",
      "account": "you@company.com",
      "name": "Your Name",
      "active": true
    },
    {
      "host": "dify.internal.acme.com",
      "account": "you@acme.com",
      "name": "Your Name",
      "active": false
    }
  ]
}
```

##### Exit Codes

| Code | Meaning                                        |
| :--- | :--------------------------------------------- |
| `0`  | Success, including when no contexts are stored |
| `2`  | Usage error, such as an unsupported `-o` value |

#### Sign Out

```text theme={null}
difyctl auth logout
```

`auth logout` revokes the active context's session on the server, then deletes its token and `hosts.yml` entry from your machine. Other saved contexts are untouched.

The local cleanup always happens. If the server-side revoke fails, `difyctl` prints a warning on stderr and clears your credentials anyway.

The same applies when the token sits in an OS keychain that can't be read at sign-out (locked, or no desktop session): the revoke is skipped and the local cleanup still runs.

##### Flags

None.

##### Examples

```bash theme={null}
difyctl auth logout
```

##### Output

```text theme={null}
✓ Logged out of cloud.dify.ai
```

##### Exit Codes

| Code | Meaning                         |
| :--- | :------------------------------ |
| `0`  | Signed out                      |
| `4`  | Not signed in (`not_logged_in`) |

#### Switch the Active Host

```text theme={null}
difyctl use host [flags]
```

`use host` changes which stored host subsequent commands run against. It is local: it only re-points the active context among the sign-ins you already have. To add a new host, run [`auth login --host`](#sign-in) instead.

##### Flags

| Flag              | Type   | Default | Description                                                                                                                                                                                                                             |
| :---------------- | :----- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--domain <host>` | string | none    | The stored host to switch to, written as its bare domain (`cloud.dify.ai`), without a scheme.

In a terminal, omit it and pick from your stored hosts. In a non-interactive session (script, CI, pipe), the flag is required. |

##### Examples

Switch to a stored host by its domain:

```bash theme={null}
difyctl use host --domain dify.internal.acme.com
```

##### Output

On success, the new active host is confirmed:

```text theme={null}
✓ Active host is now dify.internal.acme.com
```

A domain you haven't signed into fails as a usage error that lists your known hosts.

##### Exit Codes

| Code | Meaning                                                                  |
| :--- | :----------------------------------------------------------------------- |
| `0`  | Switched                                                                 |
| `2`  | Usage error: an unknown host, or a missing `--domain` outside a terminal |
| `4`  | No stored sign-ins (`not_logged_in`)                                     |

#### Switch the Active Account

```text theme={null}
difyctl use account [flags]
```

`use account` changes which stored account is active on the current host. Like `use host`, it is local and only switches between sign-ins you already have.

##### Flags

| Flag              | Type   | Default | Description                                                                                                                                                            |
| :---------------- | :----- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--email <email>` | string | none    | The account to switch to.

In a terminal, omit it and pick from your stored accounts; in a non-interactive session (script, CI, pipe), the flag is required. |

##### Examples

Switch to another account on the active host:

```bash theme={null}
difyctl use account --email teammate-bot@company.com
```

##### Output

On success, the new active account is confirmed:

```text theme={null}
✓ Active account on cloud.dify.ai is now teammate-bot@company.com
```

An email that isn't stored on the active host fails as a usage error that lists your known accounts. An account whose stored token is gone (revoked, or cleared by a [session revoke](#revoke-sessions)) fails with a not-logged-in error and a hint to sign in again.

##### Exit Codes

| Code | Meaning                                                                    |
| :--- | :------------------------------------------------------------------------- |
| `0`  | Switched                                                                   |
| `2`  | Usage error: an unknown account, or a missing `--email` outside a terminal |
| `4`  | No stored sign-in on this host, or no credential for the chosen account    |

#### List Your Active Sessions

```text theme={null}
difyctl auth devices list [flags]
```

Every device-flow sign-in registers a server-side session, labeled `difyctl on <hostname>` by default. `auth devices list` shows the sessions active for your account so you can spot and [revoke](#revoke-sessions) ones you don't recognize.

##### Flags

| Flag          | Type    | Default | Description                                                                                       |
| :------------ | :------ | :------ | :------------------------------------------------------------------------------------------------ |
| `--json`      | boolean | false   | Emit JSON instead of the table.                                                                   |
| `--page <n>`  | integer | 1       | Page number.                                                                                      |
| `--limit <n>` | integer | 20      | Page size, 1 to 200. The flag wins, then [`DIFY_LIMIT`](https://docs.dify.ai/en/cli/reference/environment-variables). |

##### Examples

List the sessions active for your account:

```bash theme={null}
difyctl auth devices list
```

##### Output

```text theme={null}
DEVICE                        CREATED               LAST USED             CURRENT
difyctl on Yours-MacBook-Pro  2026-06-02T09:14:31Z  2026-06-11T08:02:17Z  *
difyctl on build-runner-3     2026-05-28T11:40:09Z  2026-06-10T22:51:44Z
```

The table marks the session your current sign-in uses with `*`. `LAST USED` is empty for a session you haven't used since signing in.

`--json` prints a single line of JSON: a `data` array with one entry per session, plus the paging fields `page`, `limit`, `total`, and `has_more`. Each entry carries `id`, `prefix`, `client_id`, `device_label`, `created_at`, `last_used_at`, and `expires_at`.

##### Exit Codes

| Code | Meaning                          |
| :--- | :------------------------------- |
| `0`  | Success                          |
| `1`  | Network or server error          |
| `2`  | Usage error, such as `--limit 0` |
| `4`  | Authentication failure           |
| `7`  | Rate limited (HTTP 429)          |

#### Revoke Sessions

```text theme={null}
difyctl auth devices revoke [<target>] [flags]
```

`auth devices revoke` ends sessions server-side. The target matches by exact label first, then by exact session ID, then by case-insensitive label substring. A target that matches more than one session fails with the candidates listed, so pass an exact ID to disambiguate.

In a terminal, `difyctl` first asks you to confirm; pass `-y`/`--yes` to skip the prompt. Outside a terminal (a script or pipe), it revokes without prompting.

If you revoke the session your current sign-in uses, `difyctl` also clears that context's local credentials: you are signed out on this machine.

##### Arguments

* `<target>`: a device label or session ID from [`auth devices list`](#list-your-active-sessions). Required unless `--all` is passed.

##### Flags

| Flag        | Type    | Default | Description                                  |
| :---------- | :------ | :------ | :------------------------------------------- |
| `--all`     | boolean | false   | Revoke every session except the current one. |
| `-y, --yes` | boolean | false   | Skip the confirmation prompt.                |

##### Examples

Revoke one session by its label:

```bash theme={null}
difyctl auth devices revoke "difyctl on build-runner-3"
```

Sign out everywhere else, keeping this machine's session:

```bash theme={null}
difyctl auth devices revoke --all
```

##### Output

On success, `difyctl` prints `✓ Revoked `&lt;N&gt;` session(s)`. A named target that matches nothing fails with `no session matches "`&lt;target&gt;`"`. `--all` with no other sessions prints `no sessions to revoke` and exits `0`.

##### Exit Codes

| Code | Meaning                                                                                                               |
| :--- | :-------------------------------------------------------------------------------------------------------------------- |
| `0`  | Revoked, or nothing to revoke under `--all`                                                                           |
| `1`  | Network or server error                                                                                               |
| `2`  | Usage error: no target and no `--all`, an ambiguous target, no matching session, or declining the confirmation prompt |
| `4`  | Authentication failure                                                                                                |
| `7`  | Rate limited (HTTP 429)                                                                                               |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Command Index

*Find any difyctl command by name, with a link to its full reference*

**Source:** https://docs.dify.ai/en/cli/reference/command-index

Find any difyctl command by name, with a link to its full reference

| Command                                                                                          | What it does                                               |
| :----------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| [`auth devices list`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#list-your-active-sessions)             | List the active sessions for your account.                 |
| [`auth devices revoke`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#revoke-sessions)                     | Revoke one session, or all but the current one.            |
| [`auth list`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#list-your-saved-contexts)                      | List your saved sign-in contexts.                          |
| [`auth login`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#sign-in)                                      | Sign in to a Dify host with the OAuth device flow.         |
| [`auth logout`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#sign-out)                                    | Sign out of the active host.                               |
| [`auth whoami`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#check-your-active-identity)                  | Print the identity you're signed in as.                    |
| [`describe app`](https://docs.dify.ai/en/cli/reference/apps#inspect-an-app)                                          | Inspect one app's metadata and inputs.                     |
| [`env list`](https://docs.dify.ai/en/cli/reference/environment-variables#see-whats-set)                              | List the environment variables difyctl recognizes.         |
| [`export studio-app`](https://docs.dify.ai/en/cli/reference/apps#export-an-app)                                      | Export a studio app's DSL configuration as YAML.           |
| [`get app`](https://docs.dify.ai/en/cli/reference/apps#list-your-apps)                                               | List apps, or look up one app.                             |
| [`get workspace`](https://docs.dify.ai/en/cli/reference/workspaces#list-your-workspaces)                             | List the workspaces you belong to.                         |
| [`help`](https://docs.dify.ai/en/cli/reference/help)                                                                 | Get help in the terminal, including machine-readable JSON. |
| [`import studio-app`](https://docs.dify.ai/en/cli/reference/apps#import-an-app)                                      | Import a studio app from a DSL file or URL.                |
| [`resume app`](https://docs.dify.ai/en/cli/reference/apps#resume-a-paused-workflow)                                  | Resume a paused workflow run.                              |
| [`run app`](https://docs.dify.ai/en/cli/reference/apps#run-an-app)                                                   | Run an app and print the response.                         |
| [`skills install`](https://docs.dify.ai/en/cli/reference/skills#install-the-skill)                                   | Install the difyctl skill into detected coding agents.     |
| [`use account`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#switch-the-active-account)                   | Switch the active account on the current host.             |
| [`use host`](https://docs.dify.ai/en/cli/reference/auth-and-contexts#switch-the-active-host)                         | Switch the active Dify host.                               |
| [`use workspace`](https://docs.dify.ai/en/cli/reference/workspaces#switch-your-workspace-cloud) **[Cloud]** | Switch your active workspace.                              |
| [`version`](https://docs.dify.ai/en/cli/reference/version)                                                           | Show client and server versions and compatibility.         |

[Global flags](https://docs.dify.ai/en/cli/reference/global-flags) work across commands.

For the output formats, errors, and exit codes, see [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes).

#### Environment Variables

*Set difyctl defaults for the current shell session with environment variables*

**Source:** https://docs.dify.ai/en/cli/reference/environment-variables

Set difyctl defaults for the current shell session with environment variables

Environment variables set defaults for the current shell session: every `difyctl` command you run in it picks them up. A command flag wins, then an environment variable. They're shell-scoped and last only as long as the session.

#### Variables difyctl Reads

| Variable             | What it controls                                                                                                                                                                        | Default                                                                                                       |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| `DIFY_CONFIG_DIR`    | Where `difyctl` keeps its configuration (`hosts.yml`).                                                                                                                                  | macOS and Linux: `~/.config/difyctl` (Linux honors `XDG_CONFIG_HOME`)

Windows: `%APPDATA%\difyctl` |
| `DIFY_LIMIT`         | Default page size, 1 to 200, for list commands (`get app`, `auth devices list`). The `--limit` flag wins, then this variable.                                                           | `20`                                                                                                          |
| `DIFY_WORKSPACE_ID`  | The workspace `difyctl` commands run against. Must be a UUID. See [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace) for the resolution order. | none                                                                                                          |
| `DIFYCTL_HTTP_RETRY` | Retry attempts for idempotent requests on transient failures (`0` disables retries). [`--http-retry`](https://docs.dify.ai/en/cli/reference/global-flags#http-retries) overrides it.                        | `3`                                                                                                           |

An invalid value fails as a usage error (exit code `2`) rather than being silently ignored, for example a non-UUID `DIFY_WORKSPACE_ID`.

> **ℹ️ Info:**
>   Only the variables above change `difyctl`'s behavior. The others reported by the `env list` command are recognized but currently have no effect.

#### See What's Set

```text theme={null}
difyctl env list [flags]
```

`env list` shows the current value of each `difyctl` environment variable in your shell. It reads only your local environment and never calls the server, so it works before you sign in.

##### Flags

| Flag     | Type    | Default | Description                                             |
| :------- | :------ | :------ | :------------------------------------------------------ |
| `--json` | boolean | `false` | Print the inventory as a JSON array instead of a table. |

> **📝 Note:**
>   `env list` takes `--json`, not the [`-o` global flag](https://docs.dify.ai/en/cli/reference/global-flags).

##### Examples

Check which variables are set in the current shell:

```bash theme={null}
difyctl env list
```

Get the same inventory as JSON:

```bash theme={null}
difyctl env list --json
```

##### Output

Unset variables show `<unset>`, and sensitive variables never print their value (only `<set>` or `<unset>`). With `DIFY_LIMIT=50` exported:

```text theme={null}
NAME                VALUE    DESCRIPTION
DIFY_CONFIG_DIR     <unset>  Override the config-dir resolution (precedes XDG_CONFIG_HOME on Linux).
DIFY_FORMAT         <unset>  Default output format for list commands (table | json | yaml | wide | name).
DIFY_HOST           <unset>  Default Dify host (overridden by --host).
DIFY_LIMIT          50       Default page size for list commands (1..200).
DIFY_NO_PROGRESS    <unset>  Suppress progress spinners. Truthy values: 1, true, yes.
DIFY_PLAIN          <unset>  Disable ANSI colors and decorative output. Truthy values: 1, true, yes.
DIFY_TOKEN          <unset>  Bearer token for non-interactive auth.
DIFY_WORKSPACE_ID   <unset>  Workspace ID used for difyctl commands.
DIFYCTL_HTTP_RETRY  <unset>  HTTP retry count for GET/PUT/DELETE. 0 disables. Overrides --http-retry flag.
```

`--json` prints a JSON array, one entry per variable, masked the same way:

```json theme={null}
[
  {
    "name": "DIFY_CONFIG_DIR",
    "description": "Override the config-dir resolution (precedes XDG_CONFIG_HOME on Linux).",
    "sensitive": false,
    "value": "<unset>"
  }
]
```

##### Exit Codes

| Code | Meaning |
| :--- | :------ |
| `0`  | Success |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Global Flags

*Use these flags across difyctl commands to control output format, verbosity, and retry behavior*

**Source:** https://docs.dify.ai/en/cli/reference/global-flags

Use these flags across difyctl commands to control output format, verbosity, and retry behavior

The flags below work across `difyctl` commands. `-v` and `-h` are universal, while `-o` and `--http-retry` are accepted by most but not all. Check a command's [reference](https://docs.dify.ai/en/cli/reference/command-index) for the flags it accepts.

| Flag                                      | What it does                                                          |
| :---------------------------------------- | :-------------------------------------------------------------------- |
| [`-o, --output `](#output-format) | Selects the output format: `json`, `yaml`, `name`, `wide`, or `text`. |
| [`-v, --verbose`](#verbose-mode)          | Turns on verbose diagnostics on stderr.                               |
| [`--http-retry <n>`](#http-retries)       | Sets the retry budget for idempotent requests.                        |
| [`-h, --help`](https://docs.dify.ai/en/cli/reference/help)    | Show the command's help instead of running it.                        |

> **📝 Note:**
>   Flags always follow the command: `difyctl get app -o json` works; `difyctl -o json get app` is read as an unknown command.

#### Output Format

To see which of the five formats a command supports, check its `--help` or the flags table on its reference page. If you repeat the flag, the last value wins.

`-o` also changes how failures render: under `-o json`, errors arrive as a machine-readable JSON object on stderr.

For the format schemas, defaults, and channel rules, see [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes).

> **📝 Note:**
>   On [`export studio-app`](https://docs.dify.ai/en/cli/reference/apps#export-an-app), `-o` is the output file path, not a format selector.

#### Verbose Mode

`-v` adds verbose HTTP logging to stderr and includes the `raw_response` field (the raw server response, bearer tokens redacted) in error output.

Use it when a request fails and the normal error doesn't explain why.

#### HTTP Retries

`difyctl` retries idempotent requests (GET, PUT, DELETE) on transient failures: network errors and HTTP 408, 413, 500, 502, 503, and 504 responses. POST requests are never retried. A 429 (rate limited) is handled separately and exits `7`, not retried by this budget.

The default budget is 3 attempts with exponential backoff (300 ms, doubling, capped at 30 s). Use `--http-retry 0` to disable retries.

The [`DIFYCTL_HTTP_RETRY`](https://docs.dify.ai/en/cli/reference/environment-variables) environment variable sets the same budget; if both are set, the flag takes priority.

#### `--workspace` Is Not Global **[Cloud]**

`--workspace <id>` is per-command: it appears on commands that target workspace data and applies to that invocation only.

For where the flag sits in the precedence chain (flag, environment variable, stored default), see [How difyctl Picks a Workspace](https://docs.dify.ai/en/cli/reference/workspaces#how-difyctl-picks-a-workspace).

#### Help

*Get help in the terminal with per-command docs, guide topics, and machine-readable JSON*

**Source:** https://docs.dify.ai/en/cli/reference/help

Get help in the terminal with per-command docs, guide topics, and machine-readable JSON

The `difyctl` help system covers four surfaces: the [top-level overview](#get-help), [per-command and group help](#help-for-one-command-or-group), [guide topics](#guide-topics), and a [machine-readable form](#machine-readable-help) of all of them. All help prints to stdout and exits `0`.

#### Get Help

Four invocations show the same top-level overview:

```bash theme={null}
difyctl
difyctl help
difyctl --help
difyctl -h
```

The overview lists every command with its one-liner, three getting-started examples, the [global flags](https://docs.dify.ai/en/cli/reference/global-flags), and the [guide topics](#guide-topics). For the same inventory with links into this reference, see the [Command Index](https://docs.dify.ai/en/cli/reference/command-index).

#### Help for One Command or Group

Append `--help` to any command, or put `help` in front of it:

```bash theme={null}
difyctl run app --help
difyctl help run app
```

Per-command help shows the command's description, usage line, arguments, flags with defaults, and examples.

Name a command group instead of a command to list the group's subcommands:

```bash theme={null}
difyctl auth --help
```

```text theme={null}
COMMANDS
  auth devices list    List active sessions for the current bearer
  auth devices revoke  Revoke one or all session devices
  auth list            List all authenticated contexts (host + account pairs)
  auth login           Sign in to Dify via OAuth device flow
  auth logout          Log out of the active Dify host
  auth whoami          Print the active subject's identity
```

A name that matches neither a command, a topic, nor a group fails with `unknown help topic: <name>`, suggestions, and exit code `1`.

#### Guide Topics

Long-form topics ship inside the CLI, read with `difyctl help <topic>`:

| Topic         | What it covers                                                    |
| :------------ | :---------------------------------------------------------------- |
| `account`     | Onboarding guidance.                                              |
| `environment` | The CLI's own descriptions of the `DIFY_*` environment variables. |
| `agent`       | The cross-command contract for agents driving `difyctl`.          |

These topics are built into the CLI. For which variables `difyctl` actually reads, see [Environment Variables](https://docs.dify.ai/en/cli/reference/environment-variables).

#### Machine-Readable Help

Every help surface accepts `-o json` and `-o yaml`. The top-level form emits the complete command surface in one document:

```bash theme={null}
difyctl help -o json
```

The document has four top-level keys:

* `bin`, `contract`: exit codes, output formats, the shape of error output, and cross-command rules
* `commands`: one descriptor per command
* `topics`: the available guide topics by name, with each topic's text read via `difyctl help <topic>`

Per-command help in JSON returns just that command's descriptor:

```bash theme={null}
difyctl auth whoami --help -o json
```

```json theme={null}
{
  "command": "auth whoami",
  "description": "Print the active subject's identity",
  "effect": "read",
  "args": [],
  "flags": [
    {
      "name": "json",
      "char": null,
      "type": "boolean",
      "default": false,
      "multiple": false,
      "options": null,
      "description": "emit JSON"
    }
  ],
  "examples": [
    "difyctl auth whoami",
    "difyctl auth whoami --json"
  ],
  "agentGuide": null
}
```

Each descriptor carries the command's arguments and flags with types and defaults, an `effect` label (`read`, `write`, or `destructive`), and an `agentGuide` string where one exists. This is how coding agents discover `difyctl`.

#### Exit Codes

| Code | Meaning                            |
| :--- | :--------------------------------- |
| `0`  | Help printed                       |
| `1`  | Unknown help topic or command name |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Output Formats and Exit Codes

*What each difyctl output format emits, how stdout and stderr split, how errors are structured, and what every exit code means*

**Source:** https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes

What each difyctl output format emits, how stdout and stderr split, how errors are structured, and what every exit code means

`difyctl` is built to be scripted: data goes to stdout while everything else goes to stderr, the [`-o` global flag](https://docs.dify.ai/en/cli/reference/global-flags) selects the output format, and failures exit with a predictable code.

#### Output Formats

`-o ` selects how a command renders its result on stdout. Each command supports a subset of the five formats, listed in its `--help` and the Flags table on its reference page.

| Format | What stdout gets                                                                                                                            |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `json` | The result as pretty-printed JSON (2-space indent). Unicode characters appear as-is, and null fields are an explicit `null`, never omitted. |
| `yaml` | The same data as YAML.                                                                                                                      |
| `name` | Bare resource IDs, one per line. Built for shell loops; no parsing needed.                                                                  |
| `wide` | The default table plus extra columns. For example, `get app -o wide` adds a `WORKSPACE` column.                                             |
| `text` | Human-readable text. The default for single-resource commands such as `describe app` and `run app`.                                         |

Without `-o`, list commands such as `get app` print an aligned text table and other commands print text.

The JSON shapes are stable: list commands such as `get app` print a JSON object with the rows in an array, and two runs of the same command return the same top-level structure. For a command's exact JSON shape, see its reference page.

#### Output Channels

| Channel | What lands there                                                                                                                |
| :------ | :------------------------------------------------------------------------------------------------------------------------------ |
| stdout  | Data: tables, JSON and YAML documents, IDs, run output, exported DSL                                                            |
| stderr  | Everything else: errors, hints, progress spinners, status lines such as `✓ form submitted`, and reasoning streamed by `--think` |

The rules worth scripting against:

* On failure, stdout stays empty. You never have to filter error text out of captured data.
* On success, `get` and `describe` commands leave stderr empty; `run app` and `resume app` may print hints there.
* Progress spinners appear only in a terminal, on stderr, and are suppressed under `-o json`, `-o yaml`, and `-o name`.
* Piped output carries no ANSI color codes.
* If the consumer of a pipe exits early (`difyctl get app -o name | head -2`), `difyctl` exits `0` rather than failing on the broken pipe.

#### Errors

Errors go to stderr. In the default human format, an error is a `code: message` line plus optional detail lines:

```text theme={null}
not_logged_in: not logged in
hint: run 'difyctl auth login'
```

When an HTTP request was involved, `request: `&lt;METHOD&gt;` <url>` and `http_status: <n>` lines follow.

When the server's reply carries Dify's standard error body, the header line shows the server's more specific code (`not_found`, `invalid_param`) instead of the CLI's transport-level code.

Per-field validation details follow as indented lines, and the server's hint appears when `difyctl` has none of its own.

Under `-o json`, the same error becomes a single-line JSON object on stderr:

```json theme={null}
{"error":{"code":"not_logged_in","message":"not logged in","hint":"run 'difyctl auth login'"}}
```

Only `-o json` switches error rendering: `-o yaml` failures print the human format.

| Field           | Present                                                        | Meaning                                                                                                                                                                                                                         |
| :-------------- | :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `code`          | always                                                         | Stable machine-readable error code. Branch on this, never on message text.                                                                                                                                                      |
| `message`       | always                                                         | Human-readable description.                                                                                                                                                                                                     |
| `hint`          | when known                                                     | The fastest fix, often a copy-pasteable command.                                                                                                                                                                                |
| `http_status`   | on HTTP failures                                               | Status code of the failed request.                                                                                                                                                                                              |
| `method`, `url` | on HTTP failures                                               | The request that failed.                                                                                                                                                                                                        |
| `raw_response`  | only with `-v`                                                 | The raw server response body, bearer tokens redacted.                                                                                                                                                                           |
| `server`        | on HTTP failures, when the reply is Dify's standard error body | The server's own error: `code`, `message`, `status`, plus optional `hint` and `details`. 

The top-level `code` stays the CLI's stable transport-level code; `server.code` carries the server's finer-grained reason. |

For what each code means and how to fix it, see [Troubleshooting](https://docs.dify.ai/en/cli/troubleshooting).

#### Exit Codes

| Code | Meaning                        | Examples                                                                                                                                                                                                                                                               |
| :--- | :----------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`  | Success                        | Also `--help`, `version`, and a workflow run that [paused for human input](#a-paused-workflow-run-exits-0).                                                                                                                                                            |
| `1`  | Generic failure                | Network and server errors (`network_connection`, `server_5xx`, `server_4xx_other`), unknown commands, unknown flags, an unreachable OS keychain (`keyring_unavailable`).                                                                                               |
| `2`  | Usage error                    | An invalid flag value (`-o table`, `--limit 0`), a missing argument, a non-UUID app or workspace ID, `--inputs` that isn't a JSON object.                                                                                                                              |
| `4`  | Authentication error           | `not_logged_in`, `auth_expired`, `token_expired`, `access_denied`.                                                                                                                                                                                                     |
| `6`  | Version or compatibility error | `version_skew` (the server is older than this `difyctl` supports, or the server rejected this `difyctl` as too old with HTTP 426), `unsupported_endpoint` (the server lacks an endpoint this build needs), or an unreadable config file (`config_schema_unsupported`). |
| `7`  | Rate limited                   | An HTTP 429 (`rate_limited`), kept distinct from `1` so a script can back off and retry.                                                                                                                                                                               |
| `64` | Compatibility gate failed      | Only [`version --check-compat`](https://docs.dify.ai/en/cli/reference/version#gate-scripts-on-compatibility): the server was not confirmed compatible.                                                                                                                                     |

One nuance for strict scripts: parser-level mistakes (an unknown command, an unknown flag, a flag missing its value) exit `1` with a plain-text message, while an invalid value for a known flag exits `2`.

##### A Paused Workflow Run Exits 0

A Workflow or Chatflow app can pause mid-run to collect human input. The pause is a successful outcome, not a failure: `run app` and `resume app` exit `0` and print a paused payload to stdout.

To detect a pause in a script or an agent, run with `-o json` and check stdout for `"status": "paused"`; don't branch on the exit code.

For the payload shape and the resume protocol, see [When a Workflow Pauses](https://docs.dify.ai/en/cli/reference/apps#when-a-workflow-pauses) on the Apps reference.

#### Skills

*Install the agent skill so coding agents can drive difyctl*

**Source:** https://docs.dify.ai/en/cli/reference/skills

Install the agent skill so coding agents can drive difyctl

[`skills install`](#install-the-skill) writes the `difyctl` skill (a `SKILL.md` file) into the skill directories of the coding agents on your machine.

The skill deliberately lists no commands: it points the agent at `difyctl help -o json` and lets it discover the live command surface itself.

See the [help reference](https://docs.dify.ai/en/cli/reference/help#machine-readable-help) for that discovery surface, and [Install the difyctl Skill](https://docs.dify.ai/en/cli/integrate-agents/install-the-difyctl-skill) for the full integration.

#### Install the Skill

```text theme={null}
difyctl skills install [dir] [flags]
```

This command is fully local: it needs no sign-in and never contacts a server.

##### Arguments

* `dir`: optional. Install into this single directory, bypassing agent detection. The skill lands at `<dir>/SKILL.md`. Cannot be combined with `--agent`.

##### Flags

| Flag        | Type               | Default | Description                                                                                                                                                                                                                                                                                                                                          |
| :---------- | :----------------- | :------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-y, --yes` | boolean            | `false` | Write the skill. Without it, the command is a dry run: it lists where the skill would land and writes nothing.                                                                                                                                                                                                                                       |
| `--agent`   | string, repeatable | none    | Restrict the install to specific detected agents, using the names from [Agent Detection](#agent-detection).

With no `--agent`, the skill installs into every detected agent. To install into several agents but not all, repeat the flag or pass a comma-separated list.

Naming an agent that isn't detected is a usage error. |
| `--stdout`  | boolean            | `false` | Print the skill to stdout and write nothing. Cannot be combined with `--yes`, `--agent`, or `dir`.                                                                                                                                                                                                                                                   |

##### Examples

Preview where the skill would be installed (dry run, the default):

```bash theme={null}
difyctl skills install
```

Install into every detected agent:

```bash theme={null}
difyctl skills install --yes
```

Install into one agent only:

```bash theme={null}
difyctl skills install --yes --agent claude-code
```

Install into several specific agents (repeat the flag or comma-separate):

```bash theme={null}
difyctl skills install --yes --agent claude-code --agent cursor
```

Install into an explicit directory, for an agent the CLI doesn't detect:

```bash theme={null}
difyctl skills install ./my-skills/difyctl --yes
```

Print the skill without writing anything:

```bash theme={null}
difyctl skills install --stdout
```

##### Agent Detection

Detection checks whether each agent's configuration directory exists. The CLI never probes `PATH` or launches anything. The skill is written to each agent's documented user-level skill location:

| Agent         | Detected when               | Skill lands in                               |
| :------------ | :-------------------------- | :------------------------------------------- |
| `claude-code` | `~/.claude` exists          | `~/.claude/skills/difyctl/SKILL.md`          |
| `codex`       | `~/.codex` exists           | `~/.agents/skills/difyctl/SKILL.md`          |
| `opencode`    | `~/.config/opencode` exists | `~/.config/opencode/skills/difyctl/SKILL.md` |
| `cursor`      | `~/.cursor` exists          | `~/.cursor/skills/difyctl/SKILL.md`          |
| `pi`          | `~/.pi` exists              | `~/.pi/agent/skills/difyctl/SKILL.md`        |

An agent that's installed but has never been launched may not have its configuration directory yet. Install into its skill directory explicitly with `difyctl skills install <dir>`.

##### Output

A dry run lists the detected agents and the target paths, then tells you how to proceed:

```text theme={null}
Detected 2 agents: claude-code, cursor

would write to claude-code: /Users/you/.claude/skills/difyctl/SKILL.md
would write to cursor: /Users/you/.cursor/skills/difyctl/SKILL.md

Re-run with --yes to write all, or --agent <name> to write only some.
Agent not listed? Install into its directory with `difyctl skills install <dir>`.
```

With `--yes`, each write is confirmed:

```text theme={null}
wrote /Users/you/.claude/skills/difyctl/SKILL.md
wrote /Users/you/.cursor/skills/difyctl/SKILL.md
```

When nothing is detected, the command explains the alternatives and exits 0:

```text theme={null}
No agents detected (looked for ~/.claude, ~/.codex, ~/.config/opencode, ~/.cursor, ~/.pi).
Install into a directory manually with `difyctl skills install <dir>`, or
print the skill with `difyctl skills install --stdout`.
```

The installed skill carries a version stamp matching the CLI that wrote it. Re-running `skills install --yes` after upgrading replaces the file with the current version. Re-running is always safe.

##### Exit Codes

| Code | Meaning                                                                                                                               |
| :--- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `0`  | Success, including a dry run and the nothing-detected case                                                                            |
| `1`  | Local failure, such as a target directory that isn't writable                                                                         |
| `2`  | Usage error: `--stdout` combined with a write option, `dir` combined with `--agent`, or `--agent` naming an agent that isn't detected |

#### Version

*Check your difyctl build and its compatibility with your Dify server*

**Source:** https://docs.dify.ai/en/cli/reference/version

Check your difyctl build and its compatibility with your Dify server

Run [`difyctl version`](#check-client-and-server-versions) to see which `difyctl` build you have and whether it works with your Dify server. It prints the client build, probes your active host, and reports a [compatibility verdict](#compatibility-verdicts).

In a script, [`--check-compat`](#gate-scripts-on-compatibility) turns that verdict into an exit code.

#### Check Client and Server Versions

```text theme={null}
difyctl version [flags]
```

##### Flags

| Flag             | Type    | Default | Description                                              |
| :--------------- | :------ | :------ | :------------------------------------------------------- |
| `--short`        | boolean | false   | Print only the client semver (no server probe) and exit. |
| `--client`       | boolean | false   | Skip the server probe, so the verdict reports `unknown`. |
| `--check-compat` | boolean | false   | Exit `64` unless the verdict is `compatible`.            |
| `-o `    | string  | text    | Output format: `text`, `json`, or `yaml`.                |

##### Examples

Print the full report:

```bash theme={null}
difyctl version
```

Print just the client version, for scripts and bug reports:

```bash theme={null}
difyctl version --short
```

##### Output

| Format               | What stdout gets                                                                                                                                                                                                                                                              |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| default (`text`)     | The full report: a `Client` block, a `Server` block, and a one-line `Compatibility` verdict. Builds on any channel other than `stable` append a warning recommending the stable channel.                                                                                      |
| `-o json`, `-o yaml` | The same report as three objects: * `client` (`version`, `commit`, `buildDate`, `channel`, `platform`, `arch`)
* `server` (`endpoint`, `reachable`, and on success `version` and `edition`)
* `compat` (`minDify`, `maxDify`, `status`, `detail`)
 |

The default `text` report:

```text theme={null}
Client:
  Version:   0.2.0-alpha (channel: alpha)
  Commit:    9f3c2ab (built 2026-06-05)
  Platform:  darwin/arm64
  Compat:    dify >=1.16.0, <=1.16.0

Server:
  Endpoint:  https://cloud.dify.ai
  Version:   1.16.0 (cloud)

Compatibility: ok — server 1.16.0 in [1.16.0, 1.16.0]
```

`--short` prints only the client semver:

```text theme={null}
0.2.0-alpha
```

`-o json`:

```json theme={null}
{
  "client": {
    "version": "0.2.0-alpha",
    "commit": "9f3c2ab",
    "buildDate": "2026-06-05",
    "channel": "alpha",
    "platform": "darwin",
    "arch": "arm64"
  },
  "server": {
    "endpoint": "https://cloud.dify.ai",
    "reachable": true,
    "version": "1.16.0",
    "edition": "CLOUD"
  },
  "compat": {
    "minDify": "1.16.0",
    "maxDify": "1.16.0",
    "status": "compatible",
    "detail": "server 1.16.0 in [1.16.0, 1.16.0]"
  }
}
```

This command exits `0` even when the server is unreachable or incompatible: the verdict is the report, not an error. Pass `--check-compat` (below) to turn it into an exit code. Other commands act on the verdict; see [How Commands React to an Incompatible Server](#how-commands-react-to-an-incompatible-server).

##### Exit Codes

| Code | Meaning                                                 |
| :--- | :------------------------------------------------------ |
| `0`  | Report printed, whatever the verdict                    |
| `64` | With `--check-compat`: the verdict was not `compatible` |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Compatibility Verdicts

`difyctl version` compares your build against the server's version and reports one of four verdicts. You don't need to be signed in, but you do need a stored host to probe.

The `text` report prints the **Shown as** label on its `Compatibility:` line; `-o json` reports the verdict name in `status`.

| Verdict      | Shown as                        | Meaning                                                                                                                                 |
| :----------- | :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| `compatible` | `ok`                            | The server version is inside the range this build supports.                                                                             |
| `too_old`    | `incompatible (server too old)` | The server is older than the minimum this build supports.                                                                               |
| `too_new`    | `incompatible (server too new)` | The server is newer than the maximum this build was tested against.                                                                     |
| `unknown`    | `unknown`                       | No verdict: no host configured, the server is unreachable, the probe was skipped with `--client`, or the server's version didn't parse. |

The `detail` field spells out the case, for example `server 1.14.0 is older than the minimum 1.16.0` or `server 1.16.0 in [1.16.0, 1.16.0]`.

#### How Commands React to an Incompatible Server

`difyctl version` only reports the verdict. Every command that contacts the server acts on it before running, so a `too_old` server stops those commands until you resolve the mismatch:

* **`too_old`**: the command stops with exit [`6`](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) before doing its work, and tells you to upgrade the Dify server to at least the minimum this build supports (or [install the `difyctl` that matches your server](https://docs.dify.ai/en/cli/install)).
* **`too_new`**: the command runs; in an interactive terminal with text output, it also prints a throttled one-line warning to stderr.
* **`unknown`**: the command runs; there is nothing to gate on.

A server that clears the minimum version (`compatible` or `too_new`) is cached for about an hour per host, so the block check isn't repeated on every command. A `too_old` server is never cached, so it's re-checked each time and starts working as soon as you upgrade it.

Signing in with [`auth login`](https://docs.dify.ai/en/cli/reference/auth-and-contexts) runs the same check before it stores a session, so a mismatch surfaces at sign-in rather than on your first command.

The checks run in both directions: the verdicts above are `difyctl` judging your server, and your server also judges `difyctl`.

If your client is older than the server accepts, the server rejects the request with HTTP `426` and `difyctl` exits `6` with an upgrade message. This is why upgrading your Dify server can break an older `difyctl`: the server refuses the old client, even though that client's own verdict on a newer server is only a warning.

So the reliable path is to keep `difyctl` matched to your server: a newer server is tolerated with a warning, but an older one is refused.

#### Gate Scripts on Compatibility

`--check-compat` makes the verdict scriptable: anything other than `compatible`, including every `unknown` case, exits `64`. `difyctl version` always probes the server live and never reads the compatibility cache, so a scripted gate reflects the current version; the flag only turns that verdict into an exit code.

The full report still goes to stdout in your chosen format, and the one-line reason goes to stderr, so `difyctl version -o json --check-compat | jq` works the same on both outcomes.

```bash theme={null}
difyctl version --check-compat || echo "difyctl and this Dify server are not a confirmed match"
```

Exit code `64` is specific to this flag. No other `difyctl` failure uses it.

#### Workspaces

*List your workspaces, switch the active one, and understand how difyctl resolves which workspace to use*

**Source:** https://docs.dify.ai/en/cli/reference/workspaces

List your workspaces, switch the active one, and understand how difyctl resolves which workspace to use

`difyctl` works in one active workspace at a time, taken from a flag, an environment variable, or your stored default. For the order those take priority, see [How difyctl Picks a Workspace](#how-difyctl-picks-a-workspace).

* [`difyctl get workspace`](#list-your-workspaces) lists the workspaces you belong to
* [`use workspace`](#switch-your-workspace-cloud) switches the active one **[Cloud]**

Both accept the [global flags](https://docs.dify.ai/en/cli/reference/global-flags).

#### List Your Workspaces

```text theme={null}
difyctl get workspace [flags]
```

##### Flags

| Flag          | Type   | Default | Description                                                                            |
| :------------ | :----- | :------ | :------------------------------------------------------------------------------------- |
| `-o ` | string | none    | Output format: `json`, `yaml`, `name`, or `wide`. Omit the flag for the default table. |

##### Examples

See your workspaces and which one is active:

```bash theme={null}
difyctl get workspace
```

Get the full list as JSON for scripts:

```bash theme={null}
difyctl get workspace -o json
```

Print workspace IDs only, one per line:

```bash theme={null}
difyctl get workspace -o name
```

##### Output

| Format               | What stdout gets                                                                                       |
| :------------------- | :----------------------------------------------------------------------------------------------------- |
| default              | An aligned table. `CURRENT` marks your active workspace with `*`, and `ROLE` is your role in each one. |
| `-o wide`            | The same columns. Workspaces have no wide-only columns.                                                |
| `-o json`, `-o yaml` | A `workspaces` array, each entry carrying `id`, `name`, `role`, `status`, and `current`.               |
| `-o name`            | The workspace IDs, one per line.                                                                       |

Default table:

```text theme={null}
ID                                    NAME       ROLE    STATUS  CURRENT
b4e8d2a6-7c3f-4a1e-9d5b-8f2c6e0a4d7b  Acme Team  owner   normal  *
9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c  Marketing  normal  normal
```

`-o json`:

```json theme={null}
{
  "workspaces": [
    {
      "id": "b4e8d2a6-7c3f-4a1e-9d5b-8f2c6e0a4d7b",
      "name": "Acme Team",
      "role": "owner",
      "status": "normal",
      "current": true
    },
    {
      "id": "9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c",
      "name": "Marketing",
      "role": "normal",
      "status": "normal",
      "current": false
    }
  ]
}
```

##### Exit Codes

| Code | Meaning                                        |
| :--- | :--------------------------------------------- |
| `0`  | Success                                        |
| `1`  | Network or server error                        |
| `2`  | Usage error, such as an unsupported `-o` value |
| `4`  | Authentication failure                         |
| `7`  | Rate limited (HTTP 429)                        |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### Switch Your Workspace **[Cloud]**

```text theme={null}
difyctl use workspace [workspace-id] [flags]
```

`use workspace` switches your active workspace on the server first, then updates the stored default in `hosts.yml`. If the switch fails (the workspace doesn't exist, or you're not a member), your local state is left untouched.

> **💡 Tip:**
>   For the everyday invocation, see [Switch Your Workspace](https://docs.dify.ai/en/cli/common-tasks#switch-your-workspace-cloud) in Common Tasks.

##### Arguments

* `workspace-id`: the workspace to switch to, from [`get workspace`](#list-your-workspaces). In a terminal, omit it to pick from your workspaces, the current one marked `*`. In a non-interactive session (script, CI, pipe), it's required.

##### Flags

Only the [global flags](https://docs.dify.ai/en/cli/reference/global-flags).

##### Examples

Pick interactively from your workspaces:

```bash theme={null}
difyctl use workspace
```

Or look up the target yourself, then switch by ID (the form that works in scripts):

```bash theme={null}
difyctl get workspace
difyctl use workspace 9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c
```

For a single command against another workspace, skip switching and pass `--workspace` instead:

```bash theme={null}
difyctl get app --workspace 9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c
```

##### Output

On success, the new active workspace is confirmed on stdout:

```text theme={null}
✓ Switched to Marketing (9c2f4e6a-8b1d-4f3e-a5c7-0d9e2b4f6a8c)
```

The switch persists: every subsequent command runs against the new workspace until you switch again.

##### Exit Codes

| Code | Meaning                                                                                  |
| :--- | :--------------------------------------------------------------------------------------- |
| `0`  | Success                                                                                  |
| `1`  | Workspace not found, or another server error                                             |
| `2`  | Usage error, such as omitting `workspace-id` where there's no terminal to pick in        |
| `4`  | Authentication failure, or no workspaces available when `use workspace` opens its picker |
| `7`  | Rate limited (HTTP 429)                                                                  |

See [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes) for the full scheme.

#### How difyctl Picks a Workspace

Apps live in exactly one workspace, so every command that targets one needs a workspace to run against. `difyctl` resolves it in this order, taking the first value it finds:

1. The `--workspace <id>` flag on the command itself. Applies to that invocation only.
2. The [`DIFY_WORKSPACE_ID`](https://docs.dify.ai/en/cli/reference/environment-variables) environment variable.
3. Your stored default, written to `hosts.yml` in the config directory when you sign in and updated by [`use workspace`](#switch-your-workspace-cloud).

If none of these yields a workspace, the command fails with exit code `2`.

Workspace IDs are UUIDs, so pass an ID from [`get workspace`](#list-your-workspaces), not a workspace name. A value that isn't a UUID fails as a usage error.

### Troubleshooting

#### Troubleshooting

*Fix common difyctl errors with their explanations, exit codes, and solutions*

**Source:** https://docs.dify.ai/en/cli/troubleshooting

Fix common difyctl errors with their explanations, exit codes, and solutions

When `difyctl` encounters an error, it writes a message to stderr. With `-o json` active, errors are also single-line JSON with a stable `code` field and an actionable `hint`.

For the full exit-code table and error object shape, see [Output Formats and Exit Codes](https://docs.dify.ai/en/cli/reference/output-formats-and-exit-codes).

#### Version Compatibility

##### `version_skew` (difyctl and the server don't match)

`difyctl` ships with each Dify release and is matched to a server version, so a version change on either side can leave the two out of sync. It surfaces in two ways, both exiting `6`:

* **Your Dify server was upgraded** and your existing `difyctl` is now too old. The server rejects it with HTTP `426` and prints an upgrade message.
* **Your `difyctl` is newer than your server**, so it stops before sending the request, reporting that the server is older than it supports.

1. Confirm it's a version mismatch:

   ```bash theme={null}
   difyctl version
   ```

   A `Compatibility: incompatible …` line, or an upgrade message, confirms it.

2. Reinstall `difyctl` so it matches your server: set `DIFY_VERSION` to your server's Dify release tag (or omit it if your server runs the latest release), then re-run the install script. See [Install](https://docs.dify.ai/en/cli/install) for details.

Exit code: `6`.

#### Authentication Errors

##### `auth_expired`

Your session has expired and `difyctl` can no longer make authenticated requests.

1. Re-authenticate:

   ```bash theme={null}
   difyctl auth login
   ```

2. Re-run the failed command.

Exit code: `4`.

##### `not_logged_in`

No active session exists for the requested host.

1. Sign in:

   ```bash theme={null}
   difyctl auth login --host <url>
   ```

2. Re-run the failed command.

Exit code: `4`.

##### `access_denied`

You denied the sign-in request, or canceled it before approving, so nothing was authorized.

Re-run and approve the request:

```bash theme={null}
difyctl auth login
```

Exit code: `4`.

#### App Errors

##### App not found (HTTP 404)

The App ID you specified doesn't exist or isn't accessible to your token. Surfaces as `server_4xx_other` with HTTP status 404.

1. List apps you can access:

   ```bash theme={null}
   difyctl get app
   ```

2. Verify the ID and re-run.

Exit code: `1`.

##### Service API disabled (HTTP 403 from server)

The app exists, but its Service API is turned off in the Dify console. The app owner must enable it. A 403 surfaces as `server_4xx_other`.

Exit code: `1`.

#### Workflow Errors

##### Workflow validation error (HTTP 422)

A Workflow app rejected your inputs. The error message lists which required inputs are missing or invalid.

1. Inspect the app's input schema:

   ```bash theme={null}
   difyctl describe app <id>
   ```

2. Update your `--inputs` JSON to match.

Exit code: `1`.

---
