# Cursor Documentation — Complete Guide (Part 2: Cloud Agents, Integrations, and SDK)

> **NotebookLM ingestion note:** This is 2 of 3 companion files covering the official Cursor documentation. Upload all 3 parts (plus the index file, if provided) as sources in the same NotebookLM notebook to build a complete learning plan. Each page below is a cleaned, self-contained section with its original source URL cited.

- **Source:** https://cursor.com/docs (official Cursor documentation)
- **Pages in this file:** 26
- **Total pages across all parts:** 101
- **Date compiled:** 2026-07-18

## Table of Contents

- [Cloud Agents](#cloud-agents)
  - [Cloud Agents](#cloud-agents-2)
  - [Cloud Environment Setup](#cloud-environment-setup)
  - [Capabilities](#capabilities)
  - [Best Practices](#best-practices)
  - [Automations](#automations)
  - [Cursor for iOS](#cursor-for-ios)
  - [Bugbot](#bugbot)
  - [Security Agents](#security-agents)
  - [Approval Agents](#approval-agents)
  - [Security & Network](#security-network)
  - [Cloud Agents settings](#cloud-agents-settings)
  - [Cloud Agents API](#cloud-agents-api)
- [Integrations](#integrations)
  - [Slack](#slack)
  - [Microsoft Teams](#microsoft-teams)
  - [Jira](#jira)
  - [Linear](#linear)
  - [Notion](#notion)
  - [GitHub](#github)
  - [GitLab](#gitlab)
  - [Azure DevOps](#azure-devops)
  - [Bitbucket](#bitbucket)
  - [JetBrains](#jetbrains)
  - [Xcode](#xcode)
  - [Deeplinks](#deeplinks)
- [SDK](#sdk)
  - [Cursor TypeScript SDK](#cursor-typescript-sdk)
  - [Cursor Python SDK](#cursor-python-sdk)

---
## Cloud Agents

### Cloud Agents

*Cloud agents use the same [agent fundamentals](https://cursor.com/learn/agents.md) but run in isolated VMs in the cloud with full development environments instead of on your local machine. The development environment is similar to the setup on your laptop: cloned repos, installed dependencies, secrets, startup commands, and network access.*

**Source:** https://cursor.com/docs/cloud-agent

Cloud agents use the same [agent fundamentals](https://cursor.com/learn/agents.md) but run in isolated VMs in the cloud with full development environments instead of on your local machine. The development environment is similar to the setup on your laptop: cloned repos, installed dependencies, secrets, startup commands, and network access.

Effective development environments give agents full context on your codebase and organization, so they can test and verify their work.

#### Why use Cloud Agents?

You can run as many agents as you want in parallel, and they do not require your local machine to be connected to the internet.

Because they have access to their own virtual machine, cloud agents can build, test, and interact with the changed software. They can also use computers to control the desktop and browser. Cloud agents support [MCP servers](https://cursor.com/docs/mcp.md), giving them access to external tools and data sources like databases, APIs, and third-party services.

Cloud agents can also run in multi-repo environments. Use one when a task spans separate frontend, backend, infrastructure, or shared-library repositories. The agent can inspect the full workspace, make coordinated changes, and open pull requests in the repos it changes.

#### How to access

Before anyone can start a cloud agent from a repository, a Cursor account admin needs to connect source control for the account. Set up [GitHub (Cloud and Enterprise Server)](https://cursor.com/docs/integrations/github.md), [GitLab (Cloud and Self-Hosted)](https://cursor.com/docs/integrations/gitlab.md), [Bitbucket Cloud](https://cursor.com/docs/integrations/bitbucket.md), or [Azure DevOps](https://cursor.com/docs/integrations/azure-devops.md).

You can kick off cloud agents from wherever you work:

1. **Cursor for iOS**: Start and manage agents from the [Cursor iOS app](https://cursor.com/docs/cloud-agent/mobile.md)
2. **Cursor Web**: Start and manage agents from [cursor.com/agents](https://cursor.com/agents) on any device
3. **Cursor Desktop**: Select **Cloud** in the dropdown under the agent input
4. **Slack**: Use the @cursor command to kick off an agent
5. **GitHub or Bitbucket**: Comment `@cursor` on a GitHub PR or issue, or on a Bitbucket PR, to kick off an agent
6. **Linear**: Use the @cursor command to kick off an agent
7. **API**: Use the API to kick off an agent

On **Android**, use [cursor.com/agents](https://cursor.com/agents) in Chrome
and tap **Install App** for a Progressive Web App (PWA). See [Cursor for
iOS](https://cursor.com/docs/cloud-agent/mobile.md) for the native iPhone app and more mobile
options.

##### Use Cursor in Slack

Learn more about setting up and using the Slack integration, including
triggering agents and receiving notifications.

#### How it works

##### Repository provider connection

Cloud agents clone your repo from GitHub, GitLab, Azure DevOps Services, or Bitbucket Cloud and work on a separate branch, then push changes to your repo for handoff.

You need read-write privileges to your repo and any dependent repos or submodules.

##### Environments

Agents are only as capable as the environments they run in. An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work.

Not setting up a development environment for your cloud agents is like not giving your engineers a computer. This is why environment setup is the most important step to improve the effectiveness of cloud agents. It lets cloud agents work like engineers do: write code, test and verify work, and ship software.

You can configure environments with agent-led setup, a saved snapshot, or a Dockerfile in `.cursor/environment.json`. See [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md) to get started. Each cloud agent then starts from an environment selected for the repo or multi-repo group.

The Cloud Agents dashboard shows which environment an agent used, along with environment details and version history. On the agent page, hover over the repository name at the top of the page to inspect the environment used for that run. See [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md) for configuration details.

##### Runtime and environment controls

Cursor manages VM provisioning, isolation, snapshots, startup, artifacts, and capacity for every Cloud Agent. You can add secrets, restrict outbound domains, connect to private networks with Tailscale or a similar client, and use private connectivity for supported source control paths.

See [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md) for the full set of environment and network controls. If you're weighing whether to self-host, see [why most teams start with Cursor Cloud](https://cursor.com/docs/cloud-agent/self-hosted.md).

#### Models

Cloud Agents use a curated selection of models. You can select the context window size for supported models.

#### MCP support

Cloud agents can use [MCP (Model Context Protocol)](https://cursor.com/docs/mcp.md) servers configured for your team. Add and manage MCP servers through the MCP dropdown in [cursor.com/agents](https://cursor.com/agents).

Both HTTP and stdio transports are supported. OAuth is supported for MCP servers that need it. See [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md) for setup details.

Cloud Agents also include a built-in [Cursor Cloud MCP](https://cursor.com/docs/cloud-agent/capabilities.md#cursor-cloud-mcp) for run diagnostics, including transcripts, environment details, and setup logs.

#### Hooks support

Cloud agents run command-based hooks from `.cursor/hooks.json` in your repository. On Enterprise plans, they also run team hooks and enterprise-managed hooks.

This keeps formatters, audit scripts, and policy checks active when work runs in the cloud. Supported hooks include tool and file hooks (`preToolUse`, `beforeShellExecution`, `afterFileEdit`), plus lifecycle hooks (`beforeSubmitPrompt`, `subagentStart` / `subagentStop`, `preCompact`, `afterAgentResponse` / `afterAgentThought`, and `stop`).

Hooks do not run during early exploratory turns in a read-only environment; they start once the agent has a writable environment. Some hooks are IDE-specific (Tab hooks, `workspaceOpen`). User-level hooks from `~/.cursor/hooks.json` are also not available since cloud VMs don't have access to your local home directory.

See [Hooks: Cloud agent support](https://cursor.com/docs/hooks.md#cloud-agent-support) for the full support matrix and details.

#### Artifacts and remote desktop control

Cloud agents produce merge-ready PRs with artifacts to demo their changes. You can also control the agent's remote desktop to use the modified software.

- **Artifacts**: Agents produce screenshots, videos, and logs so you can see exactly what changed and how the agent verified its work.
- **Remote desktop control**: Take control of the agent's desktop to test the software yourself in a full development environment without checking out the branch locally. Release control back to the agent for it to keep working.

See [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md) for details on artifacts, computer use, and remote desktop control.

#### Related pages

- Learn more about [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md).
- Learn more about [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md).
- Learn more about [Cloud agent security](https://cursor.com/docs/cloud-agent/security-network.md).
- Learn more about [Cloud agent settings](https://cursor.com/docs/cloud-agent/settings.md).

#### Billing

Cloud Agents are charged at API pricing for the selected [model](https://cursor.com/docs/models-and-pricing.md#model-pricing). You can select the context window size, and a larger context window can increase token usage and costs. You'll be asked to set a spend limit when you first start using them.

#### Troubleshooting

##### Agent runs are not starting

- Ensure you're logged in and have connected your GitHub, GitLab, Azure DevOps, or Bitbucket account.
- Check that you have the necessary repository permissions.
- You need to be on a paid Cursor plan.

##### My secrets aren't available to the cloud agent

- Ensure you've added secrets in [cursor.com/dashboard/cloud-agents](https://cursor.com/dashboard/cloud-agents)
- Secrets are workspace/team-scoped; make sure you're using the correct account
- Try restarting the cloud agent after adding new secrets

##### Can't find the Secrets tab

- If you don't see it, ensure you have the necessary permissions

##### Do snapshots copy .env.local files?

Snapshots save your base environment configuration (installed packages, system dependencies, etc.).
If you include `.env.local` files during snapshot creation, they will be saved. However, using the Secrets tab
in Cursor Settings is the recommended approach for managing environment variables.

##### Slack integration not working

Verify that your workspace admin has installed the Cursor Slack app and that
you have the proper permissions.

#### Naming History

Cloud Agents were formerly called Background Agents.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cloud Environment Setup

*Cloud agents run on isolated Ubuntu machines. Configure the environment so the agent has the same repos, tools, dependencies, secrets, and network access a developer would use.*

**Source:** https://cursor.com/docs/cloud-agent/setup

Cloud agents run on isolated Ubuntu machines. Configure the environment so the agent has the same repos, tools, dependencies, secrets, and network access a developer would use.

Create a new environment in your [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).

#### What is a cloud agent environment?

The development environment for a cloud agent is similar to the setup on your laptop: cloned repos, installed dependencies, secrets, startup commands, and network access.

Effective development environments give agents full context on your codebase and organization, so they can test and verify their work.

![Cloud agent development environment architecture](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/cloud-agents-architecture-light.png)

#### Why does environment configuration matter?

Agents are only as capable as the environments they run in. An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work.

To take engineering tasks from start to finish, cloud agents need a configured development environment with all the repositories, tools, dependencies, and context to stay autonomous and productive.

Development environments also make agent sessions faster because cloud agents start with the tools installed instead of setting up from scratch every time.

Environment setup is the most important step to improve the effectiveness of your cloud agents.

#### Environment setup options

There are two main ways to configure the environment for your cloud agent:

1. Let Cursor's agent set up its own environment from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments). After the agent is done, you will have the option to create a snapshot of its virtual machine that can be reused for future agents.
2. Manually configure the environment with a Dockerfile. If you choose this option, you can specify the Dockerfile in a `.cursor/environment.json` file.

Both options generate an environment, and also allow you to specify an update command that will be run before the agent starts to ensure that its dependencies are up to date (e.g. `npm install`, `pip install`, etc.).

##### Multi-repo environments

Use a multi-repo environment when an agent needs to work across more than one repository. Select multiple repositories when you create the environment. Cursor clones each selected repo into the agent machine and reuses the environment for future agent runs and automations that use the same repo group.

Multi-repo environments are useful when your frontend, backend, infrastructure, or shared libraries live in separate repos. The agent can inspect the full workspace, make coordinated changes, run tests across repos, and open pull requests in the repos it changes.

You can see which environment is active, along with all past active versions, by visiting the environment's configuration page on the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).

##### Environment resolution order

Cursor resolves environment configuration by repository or repo group, using the first match:

1. `.cursor/environment.json` in the repository
2. A personal saved environment
3. A team saved environment

This gives you predictable defaults at the team level while still letting individual users override with a personal environment when a repo-level `.cursor/environment.json` is not present. User overrides are also useful to allow testing out a new environment configuration before rolling it out to the entire team.

##### Agent-driven setup (recommended)

Cursor can set up your dev environment in the cloud in less than 10 minutes. Start guided setup from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments) or from the [Agents Window](https://cursor.com/docs/agent/agents-window.md) in the Cursor desktop app.

You will be asked to connect your GitHub, GitLab, Azure DevOps, or Bitbucket account and select one or more repositories.

Then, you provide Cursor with the environment variables and secrets it will need to install dependencies and run the code.

As the agent works, you can watch its progress in a shared terminal session while it handles setup tasks like installing dependencies. After Cursor has installed dependencies and verified the code is working, you can save a snapshot of its virtual machine.

![Cloud environment setup in a shared terminal session](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/changelog/cloud-environment-setup.png)

The snapshot is reusable, so future cloud agents start up faster and can test changes by running your software. Commit the configuration to `.cursor/environment.json` so your whole team benefits.

##### Manual setup with Dockerfile (advanced)

For advanced cases, configure the environment with a Dockerfile:

- Create a Dockerfile to install system-level dependencies, use specific compiler versions, install debuggers, or switch the base OS image
- Do not `COPY` the full project; Cursor manages the workspace and checks out the correct commit
- Edit `.cursor/environment.json` directly to configure runtime settings
- Use build secrets for private package registries or build-time credentials

Here's an example `.cursor/environment.json` referencing a `.cursor/Dockerfile` (relative path) and a `custom_script.sh` install script:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

If your repo needs Docker, Tailscale, or Cloudflare Tunnel, see [Running Docker](https://cursor.com/docs/cloud-agent/setup.md#running-docker), [Running Tailscale](https://cursor.com/docs/cloud-agent/setup.md#running-tailscale), and [Running Cloudflare Tunnel](https://cursor.com/docs/cloud-agent/setup.md#running-cloudflare-tunnel) below.

You configure the environment with a Dockerfile; you do not get direct access to the remote machine.

Dockerfile builds use layer caching. When you change a Dockerfile, Cursor rebuilds the changed layers instead of rebuilding every layer from scratch.

##### Cursor-configured Dockerfiles (private beta)

For teams that do not want to write a Dockerfile from scratch, Cursor can configure one for you. During setup, Cursor inspects your repos, identifies tools and dependencies, and produces a Dockerfile-based environment configuration you can edit and version.

This flow is in private beta for Enterprise teams. To request access, contact your Cursor account representative or email [hi@cursor.com](mailto:hi@cursor.com) from your team admin account.

##### Computer Use Support for Dockerfile Repos

Computer use is supported for repos with Dockerfiles based on Debian/Ubuntu-based Linux distributions. If you require support for a different Linux distribution, please contact support.

##### Resource limits

Each cloud agent runs on a default VM profile with limited memory and CPU. If you are on an Enterprise plan and your repo needs more resources, contact support and we can increase limits for your workspace.

Self-serve custom resource configuration is coming soon.

#### Update command

When a new machine boots, Cursor starts from the base environment, then runs the `update` command (called `install` in `environment.json`).

For most repos, the `update` script is `npm install`, `bazel build`, or a similar dependency setup command.

##### Update script idempotency

The `update` script must be idempotent. It can run more than once, and it may run on partially cached state.

##### How caching works

After `update` completes, if it took more than a few seconds to run, Cursor will take an internal checkpoint snapshot and will attempt to start future cloud agents from this checkpoint.

This is why `update` commands like `pnpm install` usually lead to fast startup - if dependencies changed, the command only needs to do incremental work.

Caching is best effort; you may see slower startup times on infrequently used repositories.

##### Environment configuration recovery

Agents no longer hard fail when Cursor can recover from an environment configuration issue. Saved environments often start from a snapshot. If the requested snapshot cannot be used, Cursor falls back to the default base image and warns you.

Cursor falls back when:

- The snapshot expired after inactivity
- The snapshot is invalid or failed
- You do not have access to the snapshot

When fallback happens, Cursor keeps the rest of the environment configuration and swaps the image back to the default base image. The `update` command still runs, so dependency setup can repair the environment during startup.

The agent view shows **Environment ready (with warnings)** and a warning banner explaining what happened. The warning stays visible in the conversation as an environment configuration issue card. Open setup from the warning to inspect or repair the environment.

Cursor does not automatically switch to an older saved environment version. If you want to roll back the saved configuration, open the environment from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents), review **Version history**, and restore a previous version.

##### How to decide what to put in your `update` script

There is a tradeoff between caching work in `update` and doing setup on demand during a run.

Placing infrequently run or expensive commands (such as starting services or building docker images) in `update` can slow down startup time.

A practical pattern is to run basic cached dependency updates (such as `pnpm install`) in your `update` script, then [adding instructions in AGENTS.md](https://cursor.com/docs/cloud-agent/setup.md#add-cloud-specific-instructions-to-agentsmd) so the agent can figure out which commands it needs to run for each specific task.

#### Startup commands

After `install`, the machine starts and runs the `start` command, then any configured `terminals`. Use this to start processes that should stay alive while the agent runs.

You can skip `start` in many repos. If your environment depends on Docker, add `sudo service docker start` in `start`.

`terminals` are for app code processes. These terminals run in a `tmux` session shared by you and the agent.

#### Add cloud-specific instructions to `AGENTS.md`

Cloud agents read `AGENTS.md` files. We recommend adding a dedicated section for Cloud-only setup and testing instructions, with a title such as `Cursor Cloud specific instructions`.

If this section gets large, we recommend including references to other files that can contain detailed instructions for specific tasks.

See our [AGENTS.md docs](https://cursor.com/docs/rules.md#agentsmd) for more information.

#### Environment variables and secrets

In order to fully run and test code like a human developer, Cloud agents often need environment variables and secrets such as API keys and database credentials.

##### Recommended: use the Secrets tab in Cursor settings

The easiest way to manage secrets is through [cursor.com](https://cursor.com/dashboard/cloud-agents). These are exposed to the cloud agent as environment variables.

For more about the different types of secrets, see our [Secrets documentation](https://cursor.com/docs/cloud-agent/security-network.md#secret-protection).

##### Environment-scoped secrets

Use environment-scoped secrets when a credential should only be available to agents that use one environment. This is useful for multi-repo environments, staging credentials, or repository groups with different access needs.

Environment-scoped secrets apply to every repo in that environment. They are not available to other environments.

##### Sign-in credentials and 2FA

If your app requires login, add the same credentials you use locally as secrets, such as a username, email, and password.

If your login flow uses TOTP-based 2FA, add the TOTP secret, sometimes called the shared or root secret, as a secret too. The agent can generate the current 6-digit code with `oathtool --totp -b "$TOTP_SECRET"`.

##### Monorepos with multiple `.env` files

If your monorepo has multiple `.env.local` files:

- Add values from all `.env.local` files to the same Secrets tab
- Use unique variable names when keys overlap, such as `NEXTJS_*` and `CONVEX_*`
- Reference those variables from each app as needed

If you include `.env.local` files while taking a snapshot, they can be saved and available to cloud agents. The Secrets tab remains the recommended approach for security and management.

##### Using AWS IAM Roles

Cursor supports assuming customer-provided IAM roles for deeper integration with AWS. This allows you to grant specific AWS permissions to cloud agents without sharing long-lived credentials.

1. **Create the IAM role**: In your AWS account, create the IAM role that you'd like the cloud agent to assume, and note its ARN (e.g. `arn:aws:iam::123456789012:role/acmeRole`).

2. **Configure the IAM role secret**: Navigate to [Cursor Dashboard → Cloud Agents](https://cursor.com/dashboard?tab=cloud-agents), and add a user or team secret named `CURSOR_AWS_ASSUME_IAM_ROLE_ARN` set to the ARN of the IAM role you created.

3. **Generate an external ID**: A team admin must do this from the **Advanced** section of team settings. Navigate to [Cursor Dashboard → Settings → Advanced](https://cursor.com/dashboard?tab=settings) and find the External ID settings. If you don't see an external ID displayed, enter a placeholder value in the "AWS IAM Role ARN" field, click "Validate & Save", and reload the page. This will generate an external ID for your team (e.g. `cursor-xxx-yyy-zzz`).

4. **Configure IAM role trust policy**: In your AWS account, update the IAM role's trust policy to trust Cursor's role assumer. The trust policy should look like this:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCursorAssume",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::289469326074:role/roleAssumer"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "cursor-xxx-yyy-zzz"
        }
      }
    }
  ]
}
```

Replace `cursor-xxx-yyy-zzz` with the external ID generated for your team.

**Environment variables:**

When configured, Cursor sets these environment variables so AWS tooling uses the `cursor-cloud-agent` profile:

- `AWS_CONFIG_FILE` points to a Cursor-managed AWS config file
- `AWS_PROFILE` is set to `cursor-cloud-agent`
- `AWS_SDK_LOAD_CONFIG` is set to `1`

The AWS CLI and AWS SDKs that use the default credential chain pick up this profile automatically during setup commands and while the agent is running. You don't need to export `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN` yourself.

Cursor assumes the role with STS credentials that expire after 1 hour.
When the agent wakes, Cursor refreshes credentials that are missing, invalid, or within 15 minutes of expiration.

#### Configuration in code with environment.json

If you prefer to keep your environment configuration defined in code, you can commit a `.cursor/environment.json` to your repository.

Cloud agents will use the configuration at the commit they start from, so to test a new configuration, you can commit and push the change to a new branch, and start a cloud agent from that branch.

Sample `environment.json` using a snapshot-based config (the snapshot ID is accessible from the environments page of the dashboard):

```json
{
  "snapshot": "snapshot-20260212-00000000-0000-0000-0000-000000000000",
  "install": "npm install"
}
```

Here is a sample `.cursor/environment.json` referencing a `.cursor/Dockerfile` (relative path) and a `custom_script.sh` install script:

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "install": "pnpm install && ./custom_script.sh"
}
```

##### Important path behavior

The `dockerfile` and `context` paths in `build` are relative to `.cursor`. When
you omit `context`, it defaults to `.cursor`. The values `.`, `./`, and `..` are
special-cased to mean the repository root rather than `.cursor`, so to `COPY`
files that live in `.cursor` with bare filenames, omit `context`. The `install`
command runs from your project root.

The full schema is [defined here](https://www.cursor.com/schemas/environment.schema.json).

#### Running Docker

Cloud agents support Docker workflows. We use this internally for full-stack repos that run many services.

For simple setups, installing Docker is often enough. Commands like `docker run hello-world` usually work once Docker is installed and the daemon is running.

Docker has edge cases in Cloud Agents because it runs inside another container layer. Simple workflows usually work. More complex setups should start from the `fuse-overlayfs` and `iptables-legacy` configuration below.

For more complex Docker setups, use `fuse-overlayfs`, `iptables-legacy`, and make sure your cloud agent user can run Docker.

##### Recommended Dockerfile for complex Docker setups

```docker
########################################################
# DOCKER INSTALLATION
########################################################

# Install Docker
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl --retry 3 --retry-delay 5 -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y \
    docker-ce=5:28.5.2-1~ubuntu.24.04~noble \
    docker-ce-cli=5:28.5.2-1~ubuntu.24.04~noble \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y fuse-overlayfs && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /etc/docker && \
    printf '%s\n' '{' \
    '  "storage-driver": "fuse-overlayfs"' \
    '}' > /etc/docker/daemon.json
RUN apt-get update && apt-get install -y iptables && rm -rf /var/lib/apt/lists/*
RUN update-alternatives --set iptables /usr/sbin/iptables-legacy && \
    update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy

########################################################
# CONFIG UBUNTU USER
########################################################

# ensure no password authentication
RUN echo 'PasswordAuthentication no\nChallengeResponseAuthentication no\nUsePAM no' > /etc/ssh/sshd_config.d/disable_password_auth.conf

# Create non-root user (only if it doesn't exist)
RUN id -u ubuntu &>/dev/null || useradd -m -s /bin/bash ubuntu
# Create docker group if it doesn't exist and add ubuntu user to it
RUN groupadd -f docker && usermod -aG docker ubuntu
RUN usermod -aG sudo ubuntu
# Configure passwordless sudo for ubuntu user
RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu
# Set a password for ubuntu user
RUN echo "ubuntu:ubuntu" | chpasswd
```

#### Running Tailscale

Tailscale does not work in its default networking mode in Cloud agent VMs. Use userspace networking mode instead.

This lets the agent reach private services and data stores through your tailnet without exposing those services to the public internet.

Start `tailscaled` with:

```bash
tailscaled --tun=userspace-networking \
  --outbound-http-proxy-listen=localhost:1054 \
  --socks5-server=localhost:1055
```

Then export these proxy variables in the shell where you want traffic to flow through Tailscale:

```bash
export ALL_PROXY=socks5h://localhost:1055/
export HTTP_PROXY=http://localhost:1054/
export HTTPS_PROXY=http://localhost:1054/
```

After that, run your usual `tailscale up ...` flow.

If you want a working reference, some customers have used [`tailscale-orb`](https://circleci.com/developer/orbs/orb/orbiously/tailscale#commands-connect) successfully because its Docker mode follows this pattern.

Userspace networking does not let the VM appear as a tailnet exit node.

#### Running Cloudflare Tunnel

Cloudflare Tunnel works in Cloud Agent VMs because `cloudflared` runs in userspace.

Use this pattern when a Cloud Agent needs to reach a private HTTP service in a VPC or intranet:

- Install `cloudflared` in your environment Dockerfile or update script.
- Run a `cloudflared` connector inside your private network.
- Route an authenticated hostname, such as `vpc.example.com`, through the tunnel to the private origin.
- Add that hostname to the Cloud Agent network allowlist if your environment uses restricted egress.
- Store the Cloudflare Access service token values as Cursor Secrets. For example, use `CF_ACCESS_CLIENT_ID` and `CF_ACCESS_CLIENT_SECRET`.

The Cloud Agent can then call the private service over normal HTTPS with the `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers. The connector makes the outbound connection to Cloudflare and forwards the request to your private origin. Your services and data stores stay on your private network, and the connector does not need inbound ports open.

For private TCP services, such as databases, configure a Cloudflare TCP Access app and run `cloudflared access tcp` in your startup command. Point your app or test command at the local listener that `cloudflared` creates.

Keep tunnel tokens and Access service token secrets in Cursor Secrets, not in
your repository. Rotate them after testing if they were created for a proof of
concept.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Capabilities

*Each cloud agent runs in its own isolated VM with a full desktop environment. Agents can use a mouse and keyboard to control the desktop and browser, allowing them to interact with the software they build like a human developer.*

**Source:** https://cursor.com/docs/cloud-agent/capabilities

#### Computer use

Each cloud agent runs in its own isolated VM with a full desktop environment. Agents can use a mouse and keyboard to control the desktop and browser, allowing them to interact with the software they build like a human developer.

This means agents can start dev servers, open the app in a browser, click through UI flows, and verify their changes work before pushing a PR. Read more in the [announcement blog post](https://cursor.com/blog/agent-computer-use).

#### Demos and Artifacts

Agents create artifacts such as screenshots, videos, and log references to demonstrate their work. These artifacts are attached to the PR so you can quickly validate changes without checking out the branch locally.

##### Artifacts in GitHub

You can opt-in to have Cloud Agents embed artifacts directly into GitHub pull request descriptions by enabling the **Allow posting artifacts to GitHub** setting in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#my-pull-requests).

GitHub's [image proxy](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls) requires public URLs, so artifacts in PR descriptions use long, unguessable URLs that are viewable without authentication. For context, GitHub used public URLs for all issue and PR attachments until [May 2023](https://github.blog/changelog/2023-05-08-more-secure-private-attachments).

#### Remote desktop control

You can take control of the agent's remote desktop to interact with the software the agent is building. Hand control back to the agent at any time to let it keep working.

Cloud agents run in a remote VM that can be fully onboarded with your repo, dependencies, tooling, and setup scripts. This allows you to test changes directly in the agent's VM without checking out the branch on your local machine.

#### MCP tools

Cloud agents can use [MCP (Model Context Protocol)](https://cursor.com/docs/mcp.md) servers configured for your team. This gives agents access to external tools and data sources like databases, APIs, and third-party services during their runs.

Add and enable personal MCP servers through the MCP dropdown in [cursor.com/agents](https://cursor.com/agents). Team admins configure shared servers under **Dashboard -> Integrations & MCP**.

Admins can link shared Team MCP servers to the [Default team marketplace](https://cursor.com/docs/plugins.md#migrate-existing-team-mcps). Linking keeps the servers available to Cloud Agents and also makes them available for teammates to install and configure in the Agent Window, IDE, and CLI.

Cloud agents support OAuth for MCP servers that need it. OAuth is per-user, including for MCP servers shared at the team level.

##### Custom MCP servers

You can add custom MCP servers using either **HTTP** or **stdio** transport. SSE and `mcp-remote` are not supported.

MCP configurations are encrypted at rest. Sensitive fields are redacted and cannot be read back by any user after saving:

- **`env`** — environment variables for stdio servers
- **`headers`** — request headers for HTTP servers
- **`CLIENT_SECRET`** — OAuth client secret for HTTP servers

##### HTTP vs stdio

- **HTTP (recommended)** — server configurations are never present in the cloud agent's VM environment. The agent does not have access to refresh tokens, headers, or other credentials. Tool calls are proxied through the backend.
- **Stdio** — servers run inside the cloud agent's VM, so the agent has access to the server's configuration and environment variables. This is similar to how stdio MCPs work in the Cursor IDE.

Stdio servers depend on the VM environment to execute. We cannot verify that a stdio server will run successfully until a cloud agent is launched. We recommend using HTTP MCPs when possible, and configuring your [environment setup](https://cursor.com/docs/cloud-agent/setup.md) correctly if you use stdio servers.

##### Cursor Cloud MCP

The Cursor Cloud MCP is a built-in diagnostics server available during Cloud Agent runs. It lets an agent inspect the current run, browse related runs in the same environment, and fetch transcripts, diff metadata, environment details, and setup logs without manually collecting links and files.

Team admins can disable Cursor Cloud MCP for their team from **MCP Configuration** in [team settings](https://cursor.com/dashboard/settings). See [Team dashboard](https://cursor.com/docs/account/teams/dashboard.md#mcp-configuration) for more on MCP admin controls.

###### Access and permissions

Cloud Agent conversations can include prompts, code, tool output, and secrets. All tools enforce access checks on every request.

| Role       | What you can access                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Team admin | List and fetch details (including transcripts) for Cloud Agent runs across the team, for repositories and environments they already have access to |
| Non-admin  | Only your own runs and transcripts. You cannot view other team members' chats through this MCP                                                     |

Even when listing runs in a shared environment, non-admins only see agents they started or own. Service accounts follow the same rules as the user or team context they run under.

###### What you can inspect

| Category      | Examples                                                                                                                          |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| Current run   | Run ID, URL, repo, branch, model, owner, lifecycle status, and where the run was started (Cursor, Slack, GitHub, API, and others) |
| Related runs  | Other Cloud Agents in the same environment, or on the same repository when no saved environment is attached                       |
| Environment   | Environment version, full environment config, dashboard URL, and effective egress network policy                                  |
| Transcript    | Full user-agent conversation, including tool calls when available                                                                 |
| Diff metadata | Whether the agent changed code, how much changed, and whether it opened a PR                                                      |
| Setup logs    | Raw logs from environment setup and image-build steps                                                                             |

###### Tools

Depending on your MCP client, tool names may include a server prefix (for example, `cursor-cloud-run-info`). The underlying tools are:

| Tool                  | Purpose                                                                                                                                                  |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `run-info`            | Get the current run's identity, metadata, and URL. Start here.                                                                                           |
| `environment-info`    | Get the current run's environment version, config, dashboard URL, and effective egress policy.                                                           |
| `list-cloud-agents`   | Browse Cloud Agent runs visible to you in this environment. Filter by source, status, date, code changes, PR creation, and archived state.               |
| `batch-fetch-details` | Fetch details for specific run IDs (`bcId`s). Optionally include transcripts, diff metadata, setup logs, and environment info (up to 50 runs per batch). |
| `get-automation`      | Get an automation's details like name and owner from its ID.                                                                                             |

A typical diagnostics flow is `run-info` → `environment-info` → `list-cloud-agents` → `batch-fetch-details`.

#### Fixing CI Failures

Cloud Agents automatically try to fix CI failures in PRs they create. This currently supports GitHub Actions only.

Cloud Agents skip automatic CI follow-ups if:

- You've pushed a new commit to the branch; cloud agents do not auto-fix CI failures on human commits.
- You've sent a follow-up message to the agent.
- The same check is already failing on the base commit of the PR.
- The PR has already had 10 CI-failure follow-ups.

To disable this feature on all your personal Cloud Agents, go to [Cursor Dashboard → Cloud Agents → My Settings](https://cursor.com/dashboard/cloud-agents) and disable the "Automatically fix CI Failures" option.

To disable this feature on a specific Cloud Agent PR, you can comment `@cursor autofix off` on the PR. To re-enable it, comment `@cursor autofix on`.

If you want cloud agents to fix CI failures in your own PRs, you can simply ask them by tagging Cursor in a comment as normal. For example, `@cursor please fix the CI failures`, or `@cursor fix the CI lint check failure`.

Automatically fixing CI failures is currently only available on Teams; support for non-Teams accounts is coming soon. In the meantime, if you want similar behavior, you can ask the cloud agent explicitly to monitor and fix CI failures on the PR.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Best Practices

*Use these recommendations to get more reliable Cloud Agent runs.*

**Source:** https://cursor.com/docs/cloud-agent/best-practices

Use these recommendations to get more reliable Cloud Agent runs.

#### Set up the environment first

Use [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md) so that Cursor has its environment configured. Like a human developer, Cursor does better work if its environment is set up correctly.

#### Ensure the agent can access what it needs

Before running a Cloud Agent, verify these prerequisites:

- **Secrets**: Make sure the agent has access to required secrets (API keys, database credentials, etc.) through the [Secrets tab](https://cursor.com/dashboard/cloud-agents) in your dashboard.
- **Egress controls**: If you have [network access](https://cursor.com/docs/cloud-agent/security-network.md) restrictions enabled, ensure all URLs your local development requires are whitelisted.
- **Local testability**: Your repo should be set up to run well locally without requiring external services that cannot be reached from a VM. If it is hard for a human developer to test locally, it will also be hard for an agent.

#### Use skills and agents.md to configure your agent

If the cloud agent is having difficulty testing its changes, we recommend using [skills](https://cursor.com/docs/skills.md) and agents.md to configure your agent.

Think of the agent as a smart, but low-context human developer. The best way to make sure it does the right thing is to give it the context it needs to understand what to do.

For example, at Cursor our agents.md lists tips for running and debugging the most commonly used microservices in our mono-repo. We also have lots of skills about how to test and debug key services, each with clear instructions on when to use the skill.

The skills contain in-depth details, such as how to debug a specific microservice or how to set up a third-party dependency when needed for testing.

#### Use rules to enforce conventions

Cloud Agents can read and follow [Rules](https://cursor.com/docs/rules.md) at three levels:

- **User rules**: Set in Cursor Settings, these apply to your sessions across all repositories. Best for rules you only want to apply to you personally.
- **Team rules**: Set in the [Rules, Commands, Hooks dashboard](https://cursor.com/dashboard/team-content), these apply to all team members across every repository. Best for org-wide conventions.
- **Repo rules**: `.cursor/rules/*.mdc` files committed to the repository, these apply to all agents using that repository. Best for repo/project-specific conventions.

#### Give the agent the tools it needs

We have often found that agents are limited by the tools they have access to. We recommend using MCP and creating custom tools so that the agent has access to the same systems a human developer would.

#### Mold the tools to the agent

It is important to create tools that the agent is good at using. We recommend creating tools, and iterating based on observations of how the agent uses them.

For example, at Cursor we have created a custom CLI for the model to run micro-services in our codebase. We found that when running custom dev commands, e.g. from a package.json file, some models would forget arguments, or agents would get distracted by noisy build logs which human developers knew to ignore.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Automations

*Cursor Automations run [cloud agents](https://cursor.com/docs/cloud-agent.md) in the background, either on a schedule or in response to events from GitHub, GitLab, Slack, webhooks, Linear, and more.*

**Source:** https://cursor.com/docs/cloud-agent/automations

Cursor Automations run [cloud agents](https://cursor.com/docs/cloud-agent.md) in the background, either on a schedule or in response to events from GitHub, GitLab, Slack, webhooks, Linear, and more.

Automations can be used to automate tasks like [reviewing recent PR commits for bugs](https://cursor.com/marketplace/automations/find-bugs), [performing deep review for vulnerabilities](https://cursor.com/marketplace/automations/find-vulnerabilities), [triaging bugs in Slack](https://cursor.com/marketplace/automations/fix-slack-bugs), and [summarizing changes to your codebase on a schedule](https://cursor.com/marketplace/automations/daily-digest).

#### Getting started

Create a new automation in the [Agents Window](https://cursor.com/docs/agent/agents-window.md), at [cursor.com/automations](https://cursor.com/automations), with the `/automate` skill from a local agent session, or from a template in the [Cursor Marketplace](https://cursor.com/marketplace/automations).

The `/automate` skill lets you describe the workflow you want in plain language. Cursor configures the automation's triggers, instructions, and tools for you.

For any path:

1. Choose a trigger, e.g. every hour or when a pull request is opened.
2. Write a prompt with instructions for the automation.
3. Choose optional tools the agent is able to use, such as Send to Slack, Comment on Pull Request, or tools from MCP.
4. Choose whether the automation needs a repository, multiple repositories, or no repository at all.
5. Save and activate the automation.

#### Billing

Automations create cloud agents and are billed based on cloud agent usage. See [cloud agent pricing](https://cursor.com/docs/models-and-pricing.md#model-pricing) for details.

Automations use each model's maximum supported context window because they run as cloud agents. There is no context-window toggle.

How usage is billed depends on the automation's [permission scope](https://cursor.com/docs/cloud-agent/automations.md#permissions):

- **Team Owned**: Usage is billed to the team's usage pool. Automations execute under a shared team service account, so no individual user's usage is affected.
- **Private**: Usage is billed to the user who created the automation.
- **Team Visible**: Usage is billed to the user who created the automation, the same as Private.

#### Triggers

Triggers decide when an automation runs. An automation can have more than one trigger and is run when *any* trigger fires.

For certain triggers like Slack or cron schedules, Cursor defaults to not using a repository. If your automation should make code changes, specify which repository or repositories agents should work in. For source control triggers, specifying a repo or multiple repos is required.

##### Scheduled triggers

Scheduled triggers run on a recurring schedule. Choose from preset options or enter a cron expression for precise control.

Scheduled triggers may run with a delay but will not start before the indicated time.

##### Source control triggers

Source control triggers respond to pull request and push events from your connected Git provider: GitHub, GitLab, and Bitbucket Cloud. Connect the automation to one repository or a multi-repo environment.

Every connected provider supports the core pull request and push triggers:

- **Draft opened** - When a draft pull request is created.
- **Pull request opened** - When a non-draft PR is created or a draft is marked ready for review.
- **Pull request pushed** - When new commits are pushed to an existing PR.
- **Pull request merged** - When a PR is merged.
- **Push to branch** - When commits are pushed to a specific branch outside a pull request.
- **Comment added** - When someone leaves a top-level comment on a pull request.

GitHub supports the most triggers. GitLab and Bitbucket support the core triggers above, plus a few extras listed in their sections below.

###### GitHub triggers

GitHub is the reference provider and supports every source control trigger. Alongside the core triggers, it adds:

- **Pull request label changed** - When a specific label, or any label, is added to or removed from a pull request.
- **Issue label changed** - When a label is added to or removed from a non-PR issue.
- **CI completed** - When a GitHub check finishes on a pull request or branch.
- **Issue comment** - When a comment is made on a non-PR issue.
- **PR review comment** - When an inline comment is left on a pull request diff.
- **PR review submitted** - When a review is submitted as approved, changes requested, or commented.
- **Review thread updated** - When a review thread on a pull request is marked resolved or unresolved.
- **Workflow run completed** - When a GitHub Actions workflow run finishes on a pull request or branch.

The [Cursor Marketplace](https://cursor.com/marketplace/automations) includes templates for [triaging failed GitHub Actions](https://cursor.com/marketplace/automations/triage-github-workflow-failures) and [fixing pull request review comments](https://cursor.com/marketplace/automations/autofix-pr-review-comments).

###### GitLab triggers

Alongside the core triggers, GitLab adds:

- **Pull request label changed** - When a label is added to or removed from a merge request.
- **Pull request approved** - When a merge request is approved.

###### Bitbucket triggers

Bitbucket support covers Bitbucket Cloud (`bitbucket.org`) only. Bitbucket Server and Data Center are not supported. Alongside the core triggers, it adds:

- **Pull request approved** - When a pull request is approved.

Bitbucket Cloud has no pull request label or inline review-comment triggers.

Pull request triggers don't run on PRs opened from forks. These runs fail with a "Fork pull requests not supported" error because the branch only exists on the fork, and running external code with the repo's permissions isn't safe. The exception is **Pull request merged** triggers, which still run because they start from the merge commit. To work around this, push the branch to the repo itself and open the PR from there.

##### Slack triggers

Slack triggers respond to events from the [Cursor Slack integration](https://cursor.com/docs/integrations/slack.md).

Only public Slack channels are visible to Slack triggers at this time.

- **New message in channel** - When a message is sent to a connected Slack channel. Without a message filter, the trigger only fires on top-level channel messages. Add a keyword or regex filter if you want runs from threaded replies as well.
- **Emoji reaction** - When someone reacts to a Slack message with a specific emoji.
- **Channel created** - When a new public Slack channel is created in your workspace.

##### Webhook triggers

Webhook triggers create a private HTTP endpoint for your automation. POST to the endpoint to start a run. You can use webhooks to connect automations to internal systems, CI pipelines, monitoring tools, and more.

To retrieve the webhook URL, you must save the automation first, which will then generate a webhook URL to call and an API key for authentication.

##### Linear triggers

Linear triggers respond to events from the [Cursor Linear integration](https://cursor.com/docs/integrations/linear.md).

- **Issue created** - When a new issue is created.
- **Status changed** - When an issue's status changes.
- **End of cycle** - When a Linear cycle completes.

##### Sentry triggers

Sentry triggers run when error and issue events occur in your Sentry project. Use them to automatically investigate errors, identify root causes, and propose fixes. See the [Investigate Sentry issues](https://cursor.com/marketplace/automations/investigate-sentry-issues) marketplace template for a ready-made example.

- **Issue created** - When a new issue is created in Sentry.
- **Issue updated** - When an existing issue changes, such as a status or assignment update.
- **Any issue event** - Matches all issue event types.

##### PagerDuty triggers

PagerDuty triggers run on incident events and can be helpful to automatically triage or even resolve incidents.

- **Incident triggered** - When a new incident is created.
- **Incident acknowledged** - When an incident is acknowledged.
- **Incident resolved** - When an incident is resolved.
- **Any incident event** - Matches all incident event types.

#### Tools

Cursor Automations can have tools enabled for richer capabilities around GitHub, Slack, memory, MCP, and more. Automations also include the same base set of tools as other cloud agents. See [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md) for details.

##### Pull request creation

Repo-backed automations can open pull requests after making code changes requested by the automation prompt. This tool is enabled by default for every automation.

The pull request is opened against the repositories specified for the source control trigger. For other triggers, it uses the repositories specified by the environment.

##### Comment on pull request

Posts comments on a target pull request. Supports top-level review comments and inline code comments.

If you enable approvals, the agent can also approve, request changes, and dismiss reviews. Otherwise, it can only post comments.

##### Request reviewers

Requests reviewers on a target pull request. The agent can use `git`, memory, and other tools to identify domain experts.

##### Send to Slack

Sends messages to a Slack channel. You can target a specific channel or let the agent dynamically choose any channel.

When you allow any channel, Cursor also includes the read access needed for the agent to discover available public channels.

Note that the agent is granted read access to public channels that it can send messages to.

##### Read Slack channels

Gives the agent read-only access to list and read messages from public Slack channels.

Use this when the agent needs more context before it replies or opens a pull request.

##### MCP server

Connects an [MCP (Model Context Protocol)](https://cursor.com/docs/mcp.md) server so the agent can use external tools and data sources.

Connecting an MCP server gives the agent access to every tool exposed by that server. Only connect servers you trust with the permissions your automation needs.

##### Memories

Memories let the agent read and write persistent notes across runs for the same automation. Use this to build agents that remember and improve over time. Each memory is stored as a named entry (`MEMORIES.md` by default) that exists outside the agent's working filesystem.

Memories are enabled by default but can be disabled. Memories can be viewed and edited from the tool configuration UI.

Agents can delete outdated memory files during automation runs. You can also delete memory files from the tool configuration UI.

Memories persist across runs and should be used with caution if your automation handles untrusted input. Inputs may lead to misleading or malicious memories that unintentionally impact future automation runs.

##### Computer use

Computer use lets cloud agents kicked off by automations use a computer just like a developer would. That means automations can operate a browser, produce screenshots or recordings, or use your internal services. It is included by default for every automation.

To make sure computer use is effective, ensure that you've configured a development environment for your automation. You can then ask for a demo in your automation instructions when you want the agent to show its work. For example, tell the agent to include a short screen recording after it changes a user-facing flow.

#### Automation settings

##### Model

You can select which model the cloud agent uses for your automation.

##### Repositories

Choose whether the automation needs no repository, one repository, or a multi-repo environment.

The repository setting controls the codebase context for each run:

- **No repository**: The agent does not clone code. Use this for workflows that only need Slack, MCP, webhooks, Linear, or PagerDuty. It cannot edit code or open pull requests.
- **Single repository**: The agent works in one repository and branch. Use this when the automation should read, review, or change code in one codebase.
- **Multi-repo environment**: The agent works across the repositories in an environment. Use this when the task spans multiple codebases.

For certain triggers like Slack or cron schedules, Cursor defaults to not using a repository. If your automation should make code changes, specify which repository or repositories agents should work in.

For source control triggers, specifying a repo or multiple repos is required.

###### Single-repo automations

By default, an automation runs against one repository and branch. This is the right choice when the agent should read, review, or change code in a single codebase.

Source control triggers infer the repository from the pull request. For other triggers, choose the repository and branch in the automation settings.

###### Multi-repo automations

Use a multi-repo environment when an automation needs to work across multiple repositories. Select multiple repos when you configure the environment, or choose an existing one from your [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).

##### Permissions

Control who can view and manage the automation. The permission scope also determines how usage is [billed](https://cursor.com/docs/cloud-agent/automations.md#billing).

- **Private**: Only you can manage the automation. Team admins can view and disable the automation.
- **Team Visible**: Only you can manage the automation. Team members can view the automation, and team admins can disable the automation. It still runs with your auth.
- **Team Owned**: Team members can view the automation. Only team admins can manage the automation. It runs with the team's shared automations service account.

Promoting an automation from Private or Team Visible to Team Owned changes the identity it runs as. It stops using your auth and starts using the team's shared automations service account. If the automation uses webhook triggers, regenerate its webhook API key after the scope change. If it uses MCPs or other integrations that rely on personal OAuth credentials, make sure those are configured for the team's service account instead. Only team admins can promote an automation to Team Owned.

##### Identity

When an automation acts on external services, it uses the following identities:

- GitHub comments, review approvals, and reviewer requests run as `cursor`.
- Team-scoped automations open pull requests as `cursor`.
- Private automations open pull requests as your GitHub account.
- Slack messages are sent as the Cursor bot.

#### Writing prompts

Prompts define what the agent should do. Write them the same way you would write instructions for a cloud agent run.

Tips:

- Be specific about what the agent should check, change, or produce.
- Reference the actions you enabled - you can at-mention tools or informally mention their names.
- Include decision rules for what to do in different cases.
- Set a quality bar for when the agent should open a pull request, comment, or do nothing.
- Describe the output format you want.

#### Related

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cloud agents overview](https://cursor.com/docs/cloud-agent.md)
- [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Cloud agent pricing](https://cursor.com/docs/models-and-pricing.md#model-pricing)
- [Skills](https://cursor.com/docs/skills.md)
- [GitHub integration](https://cursor.com/docs/integrations/github.md)
- [GitLab integration](https://cursor.com/docs/integrations/gitlab.md)
- [Slack integration](https://cursor.com/docs/integrations/slack.md)
- [Microsoft Teams integration](https://cursor.com/docs/integrations/microsoft-teams.md)
- [Linear integration](https://cursor.com/docs/integrations/linear.md)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cursor for iOS

*Cursor for iOS is in beta. Features may change before general availability.*

**Source:** https://cursor.com/docs/cloud-agent/mobile

##### Beta

Cursor for iOS is in beta. Features may change before general availability.

Cursor for iOS is a native mobile app for controlling agents running [in the cloud](https://cursor.com/docs/cloud-agent.md) and on your local computer. Start agents, follow their work in real time, and review and merge their pull requests from your iPhone. It runs on the same backend as [cursor.com/agents](https://cursor.com/agents) and the desktop Agents Window, so the agents you start on mobile show up everywhere you work.

[https://apps.apple.com/app/cursor/id6767085653](https://apps.apple.com/app/cursor/id6767085653)

The app runs on iPhone with iOS 26.0 or later, in English.
Android is planned.

Cursor for iOS is available on the Pro, Pro+, Ultra, Teams, and Enterprise plans. Learn
more about [what's included](https://cursor.com/help/account-and-billing/pricing.md).

#### Getting started

##### Download the app

Get [Cursor from the App Store](https://apps.apple.com/app/cursor/id6767085653) on your
iPhone.

##### Open Cursor and sign in

Sign in with your Cursor account. If your organization requires SSO, you'll
sign in through it.

##### Choose a repository

Pick the repository and branch you want Cursor to work in.

##### Start directing agents

Send a task and supervise the agent as it works.

Once you're set up, put an agent to work. For example:

- Fix a bug or respond to an incident while you're away from your desk.
- Review and merge a teammate's pull request from your phone.
- Kick off a refactor or a new feature, then check back when the agent is done.
- Ask an agent to investigate a failing CI check.

#### What you can do

You get the full cloud agent workflow from your pocket, not a stripped-down chat box. The same machines, models, and review tools you use on the web come with you.

- **Run agents on cloud machines.** Pick a worker for each run: a Cloud machine, a [Self-Hosted Pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md), or one of [My Machines](https://cursor.com/docs/cloud-agent/my-machines.md). Agents work in full development environments, so they install dependencies, run tests, and verify their changes.
- **Use any model.** Choose any model available for cloud agents. Every run uses the model's maximum supported context window.
- **Let agents run long.** Start a task, lock your phone, and check back later. Agents keep working in the cloud whether or not your device stays connected.
- **Follow the work live.** Watch the chat stream as the agent codes, send follow-ups to a running agent, and tap a subagent card to read its child transcript.
- **Review and merge pull requests.** Read full diffs, commits, deployments, and review threads. Then merge with squash, mark ready, update the branch, toggle auto-merge, publish, close, or hand a failing check back with Fix with Agent.
- **Use your commands and automations.** Your slash commands, skills, and automations work the same on mobile as they do locally, in the CLI, and on the web.
- **Enter Design Mode.** Attach photos, camera shots, or files, then point, click, and draw on images or front-end components to give agents visual direction.
- **Use your voice.** Dictate instructions to agents for hands-free edits with live transcription.
- **Connect MCP tools.** Choose the [MCP](https://cursor.com/docs/mcp.md) servers a run should use at launch, including the Slack MCP, so agents reach the same external tools they use on the web.
- **Stay in the loop.** Get a push notification when an agent finishes a turn, and track up to eight agents at once with Live Activities on the lock screen and Dynamic Island.

The app is cache-first. It reads from local data so the inbox and conversations open fast, then syncs once your connection returns.

#### What lives on the web

The app focuses on directing and reviewing agents. It isn't an IDE, and it isn't an admin console. A few things stay on [cursor.com/agents](https://cursor.com/agents) or the [Cursor Dashboard](https://cursor.com/dashboard):

- **Editor, terminal, and file browser.** On mobile you see changed files in the diff view, not a full workspace.
- **Secrets and environments.** Configure [cloud agent environments](https://cursor.com/docs/cloud-agent/setup.md) and secrets on the web. Agents on mobile use what's already set up.
- **MCP server management.** Pick servers per run on mobile; add and manage them on the web.
- **Source control setup.** Connect or reconnect [GitHub](https://cursor.com/docs/integrations/github.md) and [GitLab](https://cursor.com/docs/integrations/gitlab.md) from the dashboard.
- **Automations, rules, and skills config.** Manage these on the web. Agents pick up whatever the repo already contains.
- **Admin, billing, and usage.** Web only.

#### Move between devices

Agents follow you across surfaces:

- **Desktop or web to mobile.** Agents you start anywhere appear in the mobile inbox automatically. From a local IDE session, push your work to a cloud agent first with Move to Cloud, or keep it on your computer and direct it from your phone with [Remote Control](https://cursor.com/docs/cloud-agent/mobile.md#remote-control).
- **Mobile to desktop.** Any agent you start on mobile shows up in the desktop Cloud Agents panel and at [cursor.com/agents](https://cursor.com/agents). Open it and keep going.
- **Direct your computer from your phone.** Hand a session running on your computer to the cloud with [Remote Control](https://cursor.com/docs/cloud-agent/mobile.md#remote-control), then keep directing it from your phone. The agent loop runs in the cloud while terminal commands, file edits, and tests run on your computer.

Agents started on mobile are tagged with `source: iosApp` so you can tell where they came from.

#### Remote Control

Remote Control lets you take an agent you're running on your computer and keep directing it from your phone. The agent loop moves to the cloud while its tools keep running on your machine, so it reads your files, runs your tests, and uses your local setup the same way it did on your desktop.

Remote Control and its settings are only available in the [Agents Window](https://cursor.com/docs/agent/agents-window.md).

##### Before you start

- **Use Cursor 3.9.8 or later.** Remote Control requires Cursor client version 3.9.8 or later on your computer. Older clients won't show the Remote Control setting under **Settings > Agents** or the `/remote-control` command.
- **Use a supported account.** Remote Control is available on Pro, Pro+, Ultra, Teams, and Enterprise plans for users with Cloud Agents access. See [what's included](https://cursor.com/help/account-and-billing/pricing.md).
- **Enable Remote Control in Cursor.** In the Agents Window, turn it on under **Settings > Agents** before handing off a session.
- **Enable it for your team.** On Teams and Enterprise plans, an admin must enable Remote Control from [Cursor Dashboard → Cloud Agents → Self-Hosted](https://cursor.com/dashboard/cloud-agents#self-hosted) before members can use it.
- **Allow cloud data storage.** Remote Control isn't available when your privacy settings disable cloud data storage.
- **Use a Git-backed workspace.** The workspace must have a Git remote. Local and Remote SSH workspaces are supported.
- **Keep your computer available.** Your computer must stay awake and online because tool calls run on it. You can turn on **Keep this computer awake** under **Settings > Agents** to prevent sleep while the computer is plugged in.

##### Hand off a session

##### Run /remote-control

In the agent's input on your computer, run `/remote-control`, then send your
next message. Cursor hands the session to a worker on your machine and makes
it controllable from your other devices.

##### Open the agent on your phone

The session shows up in the Cursor app inbox alongside your other desktop
agents. Tap in to pick up where you left off.

##### Keep directing it

Send follow-ups, watch the work stream live, and review the results from
your phone. Your computer keeps running the work.

##### How your code stays on your machine

Remote Control automatically manages a worker on your computer, with no separate setup required. The agent loop runs in Cursor's cloud, and every tool call (terminal commands, file edits, tests, and git) runs on your computer.

- Your repository, secrets, credentials, and build caches stay on your machine. Only tool results and the context the model needs cross to Cursor.
- Only you can control your agents. Cursor ties each session to your account and your machine, and rejects requests for agents you don't own.
- Cursor sends the conversation state and model context needed to continue the session when you enable Remote Control for the agent.

For the trust boundaries that apply when tool calls run on your computer, see [Security and network](https://cursor.com/docs/cloud-agent/security-network.md).

##### Current limitations

- **Git-backed workspaces only.** Remote Control requires a workspace with a Git remote.
- **Your computer must stay available.** Tool calls can't run while your computer is asleep or offline.

##### Team controls

Team and Enterprise admins control Remote Control access from [Cursor Dashboard → Cloud Agents → Self-Hosted](https://cursor.com/dashboard/cloud-agents#self-hosted). When an admin enables Remote Control, Cursor also enables the team's self-hosted worker access. When it's off, members can't enable Remote Control or hand local sessions to their other devices.

#### Availability

You can use the app on any plan that includes cloud agents: Pro, Pro+, Ultra, Teams, and Enterprise. If your organization requires SSO, you'll sign in through it first.

For HIPAA BAA details, including Eligible Services and implementation requirements, see [HIPAA Business Associate Agreements](https://cursor.com/docs/enterprise/baa.md).

Cursor for iOS relies on [Cloud Agents](https://cursor.com/docs/cloud-agent.md), which need cloud data storage to run. If you're on Privacy Mode (Legacy), switch to Privacy Mode before using the app. You won't be able to start agents on mobile until you do. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

When you try to use Cloud Agents, Cursor prompts you to opt in to Privacy Mode. Tap **Update**, then confirm **Switch to Privacy Mode** in the dialog. Your code still won't be used for training, but you can't switch back to Legacy Privacy Mode afterward. See [Security and network](https://cursor.com/docs/cloud-agent/security-network.md) for how Cloud Agents store and retain data.

#### Related pages

- [Cloud agents overview](https://cursor.com/docs/cloud-agent.md)
- [Cloud agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md)
- [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Security and network](https://cursor.com/docs/cloud-agent/security-network.md)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Bugbot

*Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.*

**Source:** https://cursor.com/docs/bugbot

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

[Bugbot leaving comments on a PR](https://cursor.com/docs-static/images/bugbot/bugbot-report-cropped.mp4)

#### How it works

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

- Runs **automatic reviews** on every PR update
- **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
- **Uses existing PR comments as context**: reads connected PR comments (top-level and inline) to avoid duplicate suggestions and build on prior feedback
- **Fix in Cursor** links open issues directly in Cursor
- **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

#### Setup

Connect your repositories through the Cursor dashboard to start using Bugbot.

- **GitHub** (including GitHub Enterprise Server): See the [GitHub integration page](https://cursor.com/docs/integrations/github.md)
- **GitLab** (including GitLab Self-Hosted): See the [GitLab integration page](https://cursor.com/docs/integrations/gitlab.md)
- **Bitbucket** (including Bitbucket Data Center): See the [Bitbucket integration page](https://cursor.com/docs/integrations/bitbucket.md)

After connecting, return to the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) to enable Bugbot on specific repositories.

#### CI check statuses

Bugbot publishes a status for each review run. On GitHub, this appears as a check named `Cursor Bugbot`. On Bitbucket, this appears as a build status with the key `cursor-bugbot`. The status uses these conclusions:

- `success`: Bugbot found no issues, and there are no unresolved Bugbot comments from earlier runs.
- `neutral`: Bugbot found issues, the run was cancelled by a newer commit, or Bugbot hit an internal error. This is the default conclusion when Bugbot reports findings.
- `failure`: Bugbot found issues and the check is configured to fail on unresolved issues.

If you use branch protection, require the Bugbot check or build status to make sure Bugbot runs before merge. Requiring the status alone does not block merges on findings because findings default to `neutral`. If fail-on-unresolved-issues behavior is available for your organization, enable it to make unresolved findings produce a failing status. Bugbot does not emit a `skipped` conclusion.

When Bugbot Autofix is enabled, GitHub may also show a separate `Cursor Bugbot Autofix` check. That check only uses `success` or `neutral`.

#### Configuration

##### Individual

##### Repository settings

Enable or disable Bugbot per repository from your installations list. Bugbot runs only on PRs you author.

##### Personal settings

- Run **only when mentioned** by commenting `cursor review` or `bugbot run`
- Run **only once** per PR, skipping subsequent commits

##### Team

##### Repository settings

Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

- Run **only once** per PR per installation, skipping subsequent commits

Bugbot runs for all contributors to enabled repositories, regardless of team membership.

##### Personal settings

Team members can override settings for their own PRs:

- Run **only when mentioned** by commenting `cursor review` or `bugbot run`
- Run **only once** per PR, skipping subsequent commits
- **Enable reviews on draft PRs** to include draft pull requests in automatic reviews

#### Analytics

![Bugbot dashboard](https://cursor.com/docs-static/images/bugbot/bugbot-dashboard.png)

#### API

Enterprise teams can use the Bugbot API to trigger reviews and retrieve per-review analytics. Create an API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api) and authenticate with [Basic Authentication](https://cursor.com/docs/api.md#basic-authentication).

##### Trigger a review

/bugbot/review

Queue a Bugbot review for a pull request or merge request. The request returns when the review is queued; the review runs asynchronously.

Requires an API key with `admin:*` scope. The endpoint is limited to 30 requests per minute per team.

Set `dryRun` to `true` to run the full analysis pipeline without posting review comments, inline comments, checks, or other SCM side effects. Dry-run reviews still persist findings and are billed like normal reviews. Retrieve them with `GET /analytics/team/bugbot-reviews`. Dry-run requests have an additional limit of 10 requests per minute per team.

###### Request Body

`prUrl` string (required)

Full GitHub pull request or GitLab merge request URL.

`dryRun` boolean (optional)

When `true`, run analysis and persist findings without posting anything to the SCM provider. Default: `false`.

```bash
curl --request POST \
  --url https://api.cursor.com/bugbot/review \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prUrl": "https://github.com/your-org/your-repo/pull/42"
  }'
```

```bash
curl --request POST \
  --url https://api.cursor.com/bugbot/review \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prUrl": "https://github.com/your-org/your-repo/pull/42",
    "dryRun": true
  }'
```

**Response:**

```json
{
  "outcome": "success",
  "message": "Bugbot review queued",
  "request_id": "6e0d261c-86a2-4383-89f0-9162c1c10662",
  "dry_run": false
}
```

A dry-run response uses `"message": "Bugbot dry-run review queued"` and `"dry_run": true`.

Save `request_id` so you can match the completed review in the analytics endpoint.

If Bugbot cannot review the pull request, the endpoint returns `400 Bad Request` with the reason:

```json
{
  "outcome": "error",
  "message": "Bugbot is disabled for this repository"
}
```

##### Review analytics

/analytics/team/bugbot-reviews

Return one item per completed Bugbot review, including the reviewed commit, findings count, billed cost, and per-finding resolution data.

Includes both posted reviews and dry-run reviews. Posted findings are identified by `comment_id` and `resolution_status`. Dry-run findings return `title`, `description`, and `locations` instead because nothing is posted to the SCM.

Requires an API key with `read:*` scope.

###### Query Parameters

`startDate` string (optional)

Start of the analytics range. Defaults to 7 days ago. See [Date Formats](https://cursor.com/docs/account/teams/analytics-api.md#date-formats).

`endDate` string (optional)

End of the analytics range. Defaults to now. See [Date Formats](https://cursor.com/docs/account/teams/analytics-api.md#date-formats).

`repo` string (optional)

Repository filter in `host/owner/repo` form. Protocol and `.git` suffix are optional.

`prNumber` number (optional)

Pull request or merge request number.

`page` number (optional)

Page number for pagination. Default: `1`.

`pageSize` number (optional)

Number of reviews per page. Default: `100`, max: `250`.

`dryRun` boolean (optional)

Filter to dry-run (`true`) or posted (`false`) reviews only.

```bash
curl --get https://api.cursor.com/analytics/team/bugbot-reviews \
  -u YOUR_API_KEY: \
  --data-urlencode 'startDate=2026-06-01' \
  --data-urlencode 'endDate=2026-06-29' \
  --data-urlencode 'repo=github.com/your-org/your-repo' \
  --data-urlencode 'prNumber=42' \
  --data-urlencode 'page=1' \
  --data-urlencode 'pageSize=100'
```

```bash
curl --get https://api.cursor.com/analytics/team/bugbot-reviews \
  -u YOUR_API_KEY: \
  --data-urlencode 'dryRun=true' \
  --data-urlencode 'repo=github.com/your-org/your-repo' \
  --data-urlencode 'prNumber=42'
```

**Response (posted review):**

```json
{
  "data": [
    {
      "request_id": "6e0d261c-86a2-4383-89f0-9162c1c10662",
      "timestamp": "2026-06-29T19:42:18.000Z",
      "repo": "github.com/your-org/your-repo",
      "repo_node_id": "R_kgDOABCDEF",
      "pr_number": 42,
      "commit_sha": "9f3c2a1b7d8e4f5061728394a5b6c7d8e9f0a1b2",
      "bugs_found": 2,
      "cost_cents": 42.5,
      "dry_run": false,
      "publication_status": "posted",
      "bugs": [
        {
          "comment_id": "2147483999",
          "resolution_status": "resolved",
          "severity": "high"
        },
        {
          "comment_id": "2147484000",
          "resolution_status": "unresolved",
          "severity": "medium"
        }
      ]
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalItems": 1,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "bugbot-reviews",
    "teamId": 12345,
    "startDate": "2026-06-01",
    "endDate": "2026-06-29",
    "repo": "github.com/your-org/your-repo",
    "prNumber": 42,
    "page": 1,
    "pageSize": 100
  }
}
```

**Response (dry-run review):**

```json
{
  "data": [
    {
      "request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "timestamp": "2026-06-29T20:15:03.000Z",
      "repo": "github.com/your-org/your-repo",
      "repo_node_id": "R_kgDOABCDEF",
      "pr_number": 42,
      "commit_sha": "9f3c2a1b7d8e4f5061728394a5b6c7d8e9f0a1b2",
      "bugs_found": 1,
      "cost_cents": null,
      "dry_run": true,
      "publication_status": "dry_run",
      "bugs": [
        {
          "comment_id": null,
          "resolution_status": null,
          "severity": "medium",
          "title": "Unbounded retry loop",
          "description": "retry() recurses without a ceiling.",
          "locations": [
            { "file": "src/net.ts", "start_line": 5, "end_line": 9 }
          ]
        }
      ]
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 100,
    "totalItems": 1,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  },
  "params": {
    "metric": "bugbot-reviews",
    "teamId": 12345,
    "startDate": "2026-06-01",
    "endDate": "2026-06-29",
    "repo": "github.com/your-org/your-repo",
    "prNumber": 42,
    "dryRun": true,
    "page": 1,
    "pageSize": 100
  }
}
```

`repo_node_id`, `pr_number`, `commit_sha`, `cost_cents`, `bugs[].comment_id`, `bugs[].resolution_status`, and `bugs[].severity` may be `null` when unavailable. `cost_cents` is `null` when the review is not billed separately. For dry-run reviews, `bugs[].title`, `bugs[].description`, and `bugs[].locations` carry the finding content. Dry-run findings have `comment_id: null` and `resolution_status: null` because nothing is posted to the SCM.

##### Trigger and retrieve a review

1. Call `POST /bugbot/review` with the pull request URL. Pass `"dryRun": true` to analyze without posting to the SCM.
2. Save the returned `request_id`.
3. Poll `GET /analytics/team/bugbot-reviews`, filtering by `repo` and `prNumber`. Use `dryRun=true` when you triggered a dry-run review.
4. Find the item whose `request_id` matches the trigger response.

Analytics may take a short time to become available after a review is queued.

#### Incremental reviews

By default, Bugbot reviews the full pull request diff on every push. Turn on **Incremental Review** from the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) to review only the changes since the previous Bugbot review.

![Incremental Review setting in the Bugbot dashboard](https://cursor.com/docs-static/images/bugbot/incremental-review-setting.png)

#### Effort Levels

Effort levels control how much time Bugbot spends reasoning during a review. Higher effort levels can find more bugs, but each review may take longer and take more up usage.

Choose from these effort levels:

- **Default**: Optimizes for efficiency and speed. Reviews are less expensive, but Bugbot may find fewer bugs.
- **High**: Spends more time reasoning. Reviews are more expensive and take longer, but Bugbot may find more bugs.
- **Custom**: Lets you describe when Bugbot should use longer and deeper reviews. Cursor dynamically sets effort levels based on your instructions.

Effort levels are available only for usage-based Bugbot plans.

#### Team rules

Team admins can create rules from the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) that apply to all repositories in the team. These rules are available to every enabled repository, making it easy to enforce organization-wide standards.

When Team Rules, repository rules, and project rule files all apply, Bugbot merges them. Order of application: Team Rules → repository rules (learned and manual) → project BUGBOT.md (including nested files) → User Rules.

#### Repository rules

##### Project rules

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```bash
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

##### Learned rules

In the [Bugbot dashboard](https://cursor.com/dashboard/bugbot/repository-rules), enable learning for your organizations and repositories.

Rules are generated automatically from your team's activity on GitHub for that repository or by manually backfilling from the history of the repository.

You can also teach Bugbot new rules inline by commenting `@cursor remember [fact]` on any PR. Bugbot saves the fact as a learned rule and applies it to future reviews.

Cursor will automatically enable or disable rules as it learns more about your team's activity over time.

| Field            | Description                                                                                                    |
| :--------------- | :------------------------------------------------------------------------------------------------------------- |
| **Name**         | Short title for the rule.                                                                                      |
| **Rule content** | The instructions Bugbot should follow (i.e. style gates, paths, or review expectations).                       |
| **Scoped paths** | Optional glob patterns such as `src/components/**`. Leave empty to apply the rule across the whole repository. |

##### Manual rules

In the [Bugbot dashboard](https://cursor.com/dashboard/bugbot/repository-rules), you can create manual rules for individual repositories.

| Field            | Description                                                                                                    |
| :--------------- | :------------------------------------------------------------------------------------------------------------- |
| **Name**         | Short title for the rule.                                                                                      |
| **Rule content** | The instructions Bugbot should follow (i.e. style gates, paths, or review expectations).                       |
| **Scoped paths** | Optional glob patterns such as `src/components/**`. Leave empty to apply the rule across the whole repository. |

##### Rule analytics

**Analytics** on a Bugbot rule show how it performs on real PRs:

| Metric              | Meaning                                                    |
| :------------------ | :--------------------------------------------------------- |
| **Issues found**    | Number of findings Bugbot reported that involve this rule. |
| **PRs reviewed**    | Number of pull requests where those findings appeared.     |
| **Accepted issues** | Number of findings your team accepted.                     |
| **Acceptance rate** | Percentage of findings that were accepted.                 |

##### Examples

##### Security: Flag any use of eval() or exec()

```text
If any changed file contains the string pattern /\beval\s*\(|\bexec\s*\(/i, then:
- Add a blocking Bug with title "Dangerous dynamic execution" and body:
  "Usage of eval/exec was found. Replace with safe alternatives or justify with a detailed comment and tests."
- Assign the Bug to the PR author.
- Apply label "security".
```

##### OSS licenses: Prevent importing disallowed licenses

```text
If the PR modifies dependency files (package.json, pnpm-lock.yaml, yarn.lock, requirements.txt, go.mod, Cargo.toml), then:
- Run the built-in License Scan.
- If any new or upgraded dependency has license in {GPL-2.0, GPL-3.0, AGPL-3.0}, then:
  - Add a blocking Bug titled "Disallowed license detected"
  - Include the offending package names, versions, and licenses in the Bug body
  - Apply labels "compliance" and "security"
```

##### Language standards: Flag React componentWillMount usage

```text
For files matching **/*.{js,jsx,ts,tsx} in React projects:
If a changed file contains /componentWillMount\s*\(/, then:
- Add a blocking Bug titled "Deprecated React lifecycle method"
- Body: "Replace componentWillMount with constructor or useEffect. See React docs."
- Suggest an autofix snippet that migrates side effects to useEffect.
```

##### Standards: Require tests for backend changes

```text
If the PR modifies files in {server/**, api/**, backend/**} and there are no changes in {**/*.test.*, **/__tests__/**, tests/**}, then:
- Add a blocking Bug titled "Missing tests for backend changes"
- Body: "This PR modifies backend code but includes no accompanying tests. Please add or update tests."
- Apply label "quality"
```

##### Style: Disallow TODO comments

```text
If any changed file contains /(?:^|\s)(TODO|FIXME)(?:\s*:|\s+)/, then:
- Add a non-blocking Bug titled "TODO/FIXME comment found"
- Body: "Replace TODO/FIXME with a tracked issue reference, e.g., `TODO(#1234): ...`, or remove it."
- If the TODO already references an issue pattern /#\d+|[A-Z]+-\d+/, mark the Bug as resolved automatically.
```

#### Run in your agent

Use the `/review-bugbot` or `/review` skills to run Bugbot from your agent before you push the code.

**What diff is reviewed:** By default, `/review-bugbot` reviews your branch changes: every change relative to the base branch, including committed and uncommitted changes. Ask it to review only your uncommitted changes when you want narrower feedback.

**Against which branch:** `/review-bugbot` compares against your default base branch. When your base branch isn't the default (such as `main`), tell the agent which branch to compare against or let it infer from the context.

![Running the /review-bugbot skill from the agent input](https://cursor.com/docs-static/images/bugbot/review-bugbot-skill.png)

##### Sync with your pull request

`/review-bugbot` reviews stay in sync with Bugbot on your connected SCM (GitHub, GitLab, or Bitbucket).

Under the hood, `/review-bugbot` stores the [patch ID](https://git-scm.com/docs/git-patch-id) of the reviewed diff. When Bugbot on your SCM sees a diff with the same patch ID, it skips the review and leaves a comment noting it already reviewed that diff.

A common use case: run `/review-bugbot`, then open a pull request with the same diff, and Bugbot recognizes the review and skips the remote PR review.

`/review` and `/review-bugbot` are available in Cursor 3.7+ and at [cursor.com/agents](https://cursor.com/agents). CLI support is coming soon.

#### Autofix

Bugbot Autofix automatically spawns a [Cloud Agent](https://cursor.com/docs/cloud-agent.md#overview) to fix bugs found during PR reviews.

##### How it works

When Bugbot finds bugs during a PR review, it can automatically:

1. Spawn a Cloud Agent to analyze and fix the reported issues
2. Push fixes to the existing branch or a new branch (depending on your settings)
3. Post a comment on the original PR with the results

![Bugbot Autofix comment on a PR](https://cursor.com/docs-static/images/bugbot/bugbot-autofix-comment.png)

##### Configuration

Configure autofix behavior from the [Bugbot dashboard](https://cursor.com/dashboard/bugbot).

##### Individual

Individual users can configure their autofix preference in their personal Bugbot settings:

- **Use Installation Default** — Follow your organization's settings
- **Off** — autofix is disabled; use manual "Fix in Cursor" or "Fix in Web" links
- **Create New Branch** (Recommended) — Push fixes to a new branch
- **Commit to Existing Branch** — Push fixes to your branch (max 3 attempts per PR to prevent loops)

User settings override team defaults for your own PRs.

##### Team

Team admins can set a default autofix mode for all team members in a GitHub organization:

- **Off** — autofix is disabled by default
- **Create New Branch** (Recommended) — Push fixes to a new branch for team members
- **Commit to Existing Branch** — Push fixes directly to the PR branch (max 3 attempts per PR to prevent loops)

Individual team members can override these defaults in their personal settings.

Autofix uses your **Default agent model** from [Settings → Models](https://cursor.com/dashboard/settings). If you haven't set a personal model preference, autofix falls back to your team's default model (if you're on a team) or the system default.

##### Requirements

Autofix requires:

- [On-demand usage](https://cursor.com/docs/models-and-pricing.md) pricing enabled
- Storage enabled (not in Legacy Privacy Mode)

##### Billing

Autofix uses Cloud Agent credits and is billed at your plan rates. Cloud Agent billing follows your existing [pricing plan](https://cursor.com/docs/models-and-pricing.md).

#### MCP support

Bugbot is integrated with your [MCP servers](https://cursor.com/docs/mcp.md) so your AI tools can interact with Bugbot directly. Use the MCP server to provide additional tools to guide Bugbot's review process.

To get started:

1. Follow the [MCP documentation](https://cursor.com/docs/mcp.md) for MCP server setup instructions.
2. Add the tools to Bugbot in the [Bugbot dashboard](https://cursor.com/dashboard/bugbot).

MCP support is available on Team and Enterprise plans only.

#### Admin Configuration API

Team admins can use the Bugbot Admin API to manage repositories and control which users can use Bugbot. Use it to automate repository management, enable Bugbot across multiple repositories, or integrate user provisioning with internal tools.

##### Authentication

All endpoints require a team Admin API Key passed as a Bearer token:

```bash
Authorization: Bearer $API_KEY
```

To create an API key:

1. Visit [API Keys in the Cursor dashboard](https://cursor.com/dashboard/api)
2. Click **New API Key**
3. Save the API key

All endpoints are rate-limited to 60 requests per minute per team.

##### Enabling or disabling repositories

Use the `/bugbot/repo/update` endpoint to toggle Bugbot on or off for a repository:

```bash
curl -X POST https://api.cursor.com/bugbot/repo/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "repoUrl": "https://github.com/your-org/your-repo",
    "enabled": true,
    "manualTriggerOnly": false
  }'
```

**Parameters:**

- `repoUrl` (string, required): The full URL of the repository
- `enabled` (boolean, required): `true` to enable Bugbot, `false` to disable it
- `manualTriggerOnly` (boolean, optional): When `true`, Bugbot won't run automatically on PR updates for this repository. Manual triggers, such as commenting `cursor review` or `bugbot run`, still work.

The dashboard UI may take a moment to reflect changes made through the API due to caching. The API response shows the current state in the database.

##### Listing repositories

Use the `/bugbot/repos` endpoint to list all repositories with their Bugbot settings for your team:

```bash
curl https://api.cursor.com/bugbot/repos \
  -H "Authorization: Bearer $API_KEY"
```

The response includes each repository's enabled status, manual-only setting, and timestamps.

##### Managing user access

Use the `/bugbot/user/update` endpoint to control which GitHub, GitLab, or Bitbucket users can use your team's Bugbot licenses. Enterprises use this to integrate Bugbot provisioning with internal access-request tools.

###### Prerequisites

Before calling this endpoint, enable an allowlist or blocklist mode in your [team Bugbot settings](https://cursor.com/dashboard/bugbot):

- **Allowlist mode ("Only...")**: Only users on the list can use Bugbot
- **Blocklist mode ("Everyone but...")**: All users can use Bugbot except those on the list

If neither mode is enabled, the API returns an error.

###### Adding or removing a user

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "octocat",
    "allow": true
  }'
```

**Parameters:**

- `username` (string, required): The GitHub, GitLab, or Bitbucket username (case-insensitive)
- `allow` (boolean, required): Whether to grant or revoke access

How `allow` behaves depends on the active mode:

| Mode      | `allow: true`                                | `allow: false`                             |
| --------- | -------------------------------------------- | ------------------------------------------ |
| Allowlist | Adds user to list (can use Bugbot)           | Removes user from list (cannot use Bugbot) |
| Blocklist | Removes user from blocklist (can use Bugbot) | Adds user to blocklist (cannot use Bugbot) |

**Response:**

```json
{
  "outcome": "success",
  "message": "Updated team-level allowlist for @octocat",
  "updatedTeamSettings": true,
  "updatedInstallations": 0
}
```

The allowlist is stored at the team level and applies across all GitHub, GitLab, and Bitbucket installations owned by that team. Usernames are normalized to lowercase.

###### Example: provisioning users through an internal tool

Connect this API to an internal access-request portal. When an employee requests Bugbot access, the portal calls the API to add them. When they leave or lose access, it calls the API to remove them.

**Grant access:**

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-scm-username", "allow": true}'
```

**Revoke access:**

```bash
curl -X POST https://api.cursor.com/bugbot/user/update \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "employee-scm-username", "allow": false}'
```

#### Pricing

Bugbot uses usage-based billing.

Bugbot pricing changed with the May 2026 pricing update. See the [announcement blog post](https://cursor.com/blog/may-2026-bugbot-changes) for background. If you're still on the old seat-based plan, see [legacy Bugbot pricing](https://cursor.com/docs/bugbot/legacy-pricing.md).

##### Billing

##### Individuals

##### Usage-based billing

Bugbot includes:

- Reviews on all PRs across your repositories
- Access to Bugbot rules
- The ability to set the effort level Bugbot uses for reviews

Bugbot first consumes your included usage, then bills additional reviews through on-demand spend. See the [pricing page](https://cursor.com/pricing#bugbot) for current rates.

##### Getting started

Subscribe through your account settings.

##### Teams

##### Usage-based billing

Bugbot Teams includes:

- Code reviews on all PRs
- Analytics and reporting dashboard
- The ability to set the effort level Bugbot uses for reviews
- Advanced rules and settings

Bugbot Teams bills from on-demand spend. See the [pricing page](https://cursor.com/pricing#bugbot) for current rates.

##### Getting started

Subscribe through your team dashboard to enable billing.

#### Troubleshooting

If Bugbot isn't working:

1. **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2. **Check permissions** to verify Bugbot has repository access
3. **Verify installation** to confirm your repository provider integration is installed and enabled

Include the request ID from verbose mode when reporting issues.

#### FAQ

##### Does Bugbot read PR comments?

Yes. Bugbot reads both top-level and inline pull request comments from connected providers and includes them as context during reviews. This helps avoid duplicate suggestions and allows Bugbot to build on prior feedback from reviewers.

##### Is Bugbot privacy-mode compliant?

Yes, Bugbot follows the same privacy compliance as Cursor and processes data identically to other Cursor requests.

##### What happens when I use all included Bugbot usage?

When you use all included Bugbot usage, additional Bugbot reviews bill from on-demand spend.

##### How do I give Bugbot access to a self-hosted source control instance?

See the setup and networking guides on the respective integration pages:

- [GitHub Enterprise Server](https://cursor.com/docs/integrations/github.md#setup)
- [GitLab Self-Hosted](https://cursor.com/docs/integrations/gitlab.md#setup)
- [Bitbucket Data Center](https://cursor.com/docs/integrations/bitbucket.md#setup)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Security Agents

*Security Agents scan your code for security bugs, risky patterns, and vulnerabilities.*

**Source:** https://cursor.com/docs/security-agents

Security Agents scan your code for security bugs, risky patterns, and vulnerabilities.

#### How it works

Security Agents include two Cursor-managed agent types:

- **Security Reviewer** checks pull requests before they merge. Use it to catch vulnerabilities during code review.
- **Vulnerability Scanner** scans your codebase at rest. Use it to find pre-existing vulnerabilities, long-standing issues, and problems missed during PR review.

Both agent types run on the Automations platform and require Cloud Agents.

#### Setup

To configure Security Agents, open the [Security Agents Dashboard](https://cursor.com/dashboard/security-agents) and create your first agent.

##### Triggers

**Security Reviewer agents** support Git-based Automations triggers, including pull request and merge request events. Use these triggers to run security checks when code changes.

![Security Reviewer Git-based trigger configuration](https://cursor.com/docs-static/images/security-review/triggers.png)

**Vulnerability Scanner agents** support cron-based triggers. Use these triggers to scan your codebase on a recurring schedule, independent of pull request activity.

![Vulnerability Scanner cron trigger configuration](https://cursor.com/docs-static/images/security-review/vulnerability-scanner-triggers.png)

##### Security Checks

Both agent types include built-in security checks. Enable or disable individual checks based on what you want each agent to review.

##### Custom instructions

Use custom instructions to give each agent more context. You can describe the types of issues to prioritize, explain project-specific security expectations, or define how the agent should behave.

##### Tools and MCPs

Both agent types support tools and MCPs. Each agent needs at least one tool or MCP to run.

Use tools and MCPs to connect Security Agents to the systems where your team tracks security work.

- Send vulnerabilities to a Slack channel, issue tracker, or another connected system.
- Add custom instructions that explain when and how the agent should use each MCP.
- Give the agent extra context from tools or MCPs before it reports a finding.

##### Environment Setup

Security Agents run on Cloud Agents.

You can use Cursor's cloud with no additional setup.

#### Run in your agent

Use the `/review-security` or `/review` skills to run the Security Agent from your agent before you push the code.

**What diff is reviewed:** By default, `/review-security` reviews your branch changes: every change relative to the base branch, including committed and uncommitted changes. Ask it to review only your uncommitted changes when you want narrower feedback.

**Against which branch:** `/review-security` compares against your default base branch. When your base branch isn't the default (such as `main`), tell the agent which branch to compare against or let it infer from the context.

![Running the /review-security skill from the agent input](https://cursor.com/docs-static/images/security-review/review-security-skill.png)

`/review` and `/review-security` are available in Cursor 3.7+ and at [cursor.com/agents](https://cursor.com/agents). CLI support is coming soon.

#### Billing

Security Agents are billed at the team usage level:

- Usage is charged to the team's usage pool.
- Agents run under a shared team service account, so they don't affect any individual user's usage.

#### Analytics

Security Agents track three key metrics across agent runs:

- **Vulnerabilities found**: the number of security findings reported by agents.
- **Issues fixed**: the number of findings that were resolved after they were reported.
- **Resolution rate**: the percentage of reported findings that were fixed.

To determine whether an issue was fixed, Cursor uses LLMs to review incremental diffs and assess whether the flagged issue was resolved.

#### Viewing Runs

Every agent run is tracked in the dashboard. Use the run history to see when an agent ran, which tools it used, its final status, and how long it took.

Open a run to inspect the underlying Cloud Agent for more detail about what the agent did.

![Security Agents recent runs dashboard](https://cursor.com/docs-static/images/security-review/recent-runs.png)


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Approval Agents

*Approval Agents auto-approve pull requests and assigns reviewers.*

**Source:** https://cursor.com/docs/approval-agents

Approval Agents auto-approve pull requests and assigns reviewers.

#### How it works

Approval agents run on top of your pull requests. They approve PRs when your criteria are met, or routes PRs to reviewers when more review is needed.

These agents do not replace a full code review. They use configured instructions, approval policy files, AI review agent findings, and risk thresholds to decide whether approval is safe.

Get started by configuring in the [Approval Agents dashboard](https://cursor.com/dashboard/approval-agents).

#### Core capabilities

##### Auto-approval

Approval Agents can auto-approve pull requests when your approval criteria are met.

Use approval criteria to describe the conditions a PR must meet before the agent approves it. The agent also considers applicable policy files, risk settings, AI reviewer findings, and the current review state.

##### Reviewer assignment

Approval Agents can assign reviewers to pull requests when more review is needed.

Use reviewer assignment to describe the conditions a PR must meet before the agent assigns reviewers. The agent also considers applicable policy files, risk settings, AI reviewer findings, and the current review state.

#### Core features

##### AI reviewer awareness

Approval Agents can use findings from other Cursor review systems:

- **Bugbot Review Context** utilizes Bugbot findings in the approval decision.
- **Security Review Context** utilizes Security Agent findings in the approval decision.

When these contexts are enabled, the agent waits for the relevant agentic reviewer checks to finish and uses their findings as approval signals.

If Bugbot or Security Agents report findings that need human review, the Approval Agent will not approve the PR.

Security Agents require a team or enterprise plan.

##### Risk scoring

Approval Agents can classify a PR by risk and enforce a maximum approval threshold.

- **Use Risk Score** enables risk classification which can be customized further with prompting.
- **Maximum Risk Threshold** sets the highest risk level the agent may approve.

If a PR exceeds the configured threshold, the agent will not approve it.

##### Approval policy files

Approval Agents can discover repository policy files and apply them before deciding whether to approve.

For each changed file, the agent checks the file's directory and each ancestor directory for this exact filename:

```text
APPROVAL_POLICY.md
```

Only exact basename matches are trusted. Files such as `POLICY.md`, `approval_policy.md`, `APPROVAL_POLICY.md.bak`, and `team_APPROVAL_POLICY.md` are ignored during directory policy discovery.

The closest applicable `APPROVAL_POLICY.md` has the highest priority for files under that directory. Ancestor policies still apply unless they conflict with a more specific policy.

##### Routing policies

Approval Agents also check for a top-level routing file:

```text
.cursor/approval-policies/ROUTING.md
```

`ROUTING.md` is a YAML list of product entries. Each entry contains:

- `product`: the product or area name.
- `boundary`: a semantic boundary or explicit repository-relative path or glob.
- `policies`: policy prompt pointers, either explicit file paths or semantic descriptions.

If `ROUTING.md` is missing, directory-based `APPROVAL_POLICY.md` discovery still runs. Missing routing does not weaken policy discovery.

##### Policy precedence

Applicable approval policy prompts override generic approval criteria, risk thresholds, reviewer-selection guidance, custom approval instructions, and the default automated-review posture.

If policies conflict, the agent follows the most specific policy. If specificity is unclear, it follows the stricter instruction and avoids auto-approval.

If a PR changes an approval policy, routing file, routed policy file, or reviewer-specific policy file, the agent does not use the changed content to relax review requirements for that same PR. It uses the base-branch version when available, or requires human review when the base version cannot be determined.

#### Setup

To configure Approval Agents, open the [Approval Agents Dashboard](https://cursor.com/dashboard/approval-agents) and create your first agent.

##### Create an agent

Choose **New Agent**, or use the onboarding card to create a **Pull Request Approver**.

New agents start with default pull request triggers and approval behavior. You can then tune triggers, approval criteria, reviewer routing, AI context, and notification tools.

##### Configure triggers

Triggers decide when the agent runs. Approval Agents support pull request events such as:

- **PR opened** runs the agent when a pull request is created.
- **PR pushed / updated** runs the agent when new commits are pushed to an existing PR.
- **PR commented** runs the agent when a comment matching a regex is posted on an existing PR.

Triggers can be scoped to repositories or organizations. For team-owned repositories, team admins can configure broader team scopes.

##### Configure review signals

In **Configuration**, choose which signals the agent should use:

- **Use Bugbot Review Context**
- **Use Security Review Context**
- **Use Risk Score**
- **Maximum Risk for Approval**

Use these signals to decide whether the agent should rely on AI reviewer output, security findings, and risk thresholds before approving.

##### Write a custom prompt

Use the **Custom Prompt** to add approval criteria for your team. You can describe local review expectations, examples of PRs that are safe to approve, or cases that require human review.

Policy files still take precedence over the custom prompt for applicable files.

If the custom prompt is not set, the agent will use the default Cursor managed criteria.

##### Configure tools and MCPs

The agent must have at least one primary action enabled:

- **Approve PR**
- **Request Reviewers**

Optional integrations can include:

- Slack notifications.
- Microsoft Teams notifications.
- MCP servers for additional tool access.

Use the custom prompt to guide how the agent should use MCP tools.

##### Save and enable

After configuring, save the agent. Existing agents can be enabled or disabled from the detail page.

Team members without admin permission can view Approval Agents but cannot edit them.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Security & Network

*Cloud Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).*

**Source:** https://cursor.com/docs/cloud-agent/security-network

Cloud Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

**Privacy Mode (Legacy)** is not supported. Legacy privacy mode blocks cloud
data storage, and Cloud Agents need to store code and environment data in the
cloud while they run. Switch to Privacy Mode from [Dashboard → Cloud
Agents](https://cursor.com/dashboard/cloud-agents) before using Cloud Agents.

#### Secret protection

Secrets provided to Cloud Agents are encrypted at rest and in transit. They are not visible to anyone other than the Cloud Agent user.

Secrets can be set as Environment Variables, Runtime Secrets, or Build Secrets.

##### Environment Variables

Secrets set with type `Environment Variable` are visible to the cloud agent. These are best used for non-sensitive configuration that is helpful for the agent to view, such as flags or public URLs. They are still encrypted at rest and in transit as with other secret types.

##### Runtime secrets

Previously, Runtime Secrets were called Redacted Secrets.

Secrets set with type `Runtime Secret` are still loaded as environment variables, but their contents are redacted from the agent's tool call results, chat transcript, commits, and commit messages, and replaced with the placeholder string `[REDACTED]`. These are best used for sensitive credentials that should not be exposed to the agent and should never be committed to the repository.

Because Runtime Secrets still function internally as environment variables, while they are not shown to the agent, they are still visible to users interacting with the agent's environment via the Terminal.

##### Build secrets

Secrets set with type `Build Secret` are only available to the [Docker build process](https://cursor.com/docs/cloud-agent/security-network.md#manual-setup-with-dockerfile-advanced) (if you have configured one) and are not exposed to the running agent's environment. These are best used for private package registries or build-time credentials that should not be exposed to the agent.

In order to securely use a Build Secret within your Dockerfile, reference them from a `RUN` step using a [Docker secret mount](https://docs.docker.com/build/building/secrets/#secret-mounts), for example:

```docker
RUN --mount=type=secret,id=MY_TOKEN,env=MY_TOKEN,required=true \
    ./scripts/install-private-deps.sh
```

#### Signed commits

Cloud Agents sign every commit with a HSM-backed Ed25519 key. On GitHub and GitLab, these commits display a "Verified" badge so your team can confirm the commit came from Cursor.

This works automatically for all Cloud Agents. No setup is required.

If your repository enforces branch protection rules that require signed commits, Cloud Agent PRs satisfy those rules without extra configuration.

#### Protected Git Scopes

Team admins can lock a Git organization to your Cursor organization so only your teams can start Cloud Agents on its repositories. See [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes).

#### What you should know

1. Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes.
2. Your code runs inside our AWS infrastructure in isolated VMs and is stored on VM disks while the agent is accessible.
3. The agent has internet access by default. You can configure [network egress controls](https://cursor.com/docs/cloud-agent/security-network.md#network-access) for users, teams, and saved environments to restrict the domains the agent can access.
4. The agent auto-runs all terminal commands, letting it iterate on tests. This differs from the foreground agent, which requires user approval for every command. Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. See [OpenAI's explanation about risks of prompt injection for cloud agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. If privacy mode is disabled, we collect prompts and dev environments to improve the product.
6. If you disable privacy mode when starting a cloud agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes.

#### Data retention

Cloud Agents store two types of data for every run:

- **Conversation history.** The prompts, model responses, tool calls, and demo artifacts that make up the agent's transcript. This is the data you see when you open an agent on the web or from a desktop client.
- **Environment snapshots.** Encrypted point-in-time copies of the virtual machine disk. Snapshots let you customize VM environments and allow agents to start or resume without recloning the repository or running the setup again.

Conversation history is kept indefinitely by default so you can revisit and resume past runs. Environment snapshots are stored for a maximum of **90 days** of inactivity. Each time an agent starts or resumes from a snapshot, its expiry extends for another 90 days. Once a snapshot goes unused for 90 days, it's deleted automatically, regardless of plan or policy.

You can use the [Delete Agent API](https://cursor.com/docs/cloud-agent/api/endpoints.md#delete-an-agent-permanently) to explicitly delete a cloud agent's conversation history. This endpoint removes the conversation transcript and its artifacts. It doesn't delete environment snapshots, which can't be deleted on demand and instead follow the retention window above.

##### Cloud agent retention policies

Custom retention windows are in early access for select Enterprise teams. [Contact sales](https://cursor.com/contact-sales?source=docs-cloud-agent-retention) to request access.

Enterprise team admins can cap how long the team's Cloud Agent data is kept from **Team Settings** on the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents). The available windows are **Indefinite** and **90 days**.

When you set the policy to **90 days**:

- A background job deletes conversations older than the retention policy window.
- Environment snapshots continue to follow the rolling 90-day inactivity window described above.
- The policy applies to every agent run the team owns, including runs from saved environments and the [API](https://cursor.com/docs/cloud-agent/api/v0.md).

Switching back to **Indefinite** stops further conversation deletions but doesn't restore data that's already been removed.

#### Network access

Control which network resources your Cloud Agents can reach. These settings are available on the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents) for individual users, saved environments, and team admins.

##### Private network access

Cloud Agents do not need to run on your hardware to reach private resources. For services in a VPC or intranet, use Tailscale userspace networking, Cloudflare Tunnel, or a similar private-network client in the Cloud Agent environment. See [Running Tailscale](https://cursor.com/docs/cloud-agent/setup.md#running-tailscale) and [Running Cloudflare Tunnel](https://cursor.com/docs/cloud-agent/setup.md#running-cloudflare-tunnel) for setup notes.

With either Tailscale or Cloudflare Tunnel, your private services do not need to accept inbound traffic from the public internet. The agent connects through an authenticated network path, while the service stays on your private network.

Cloudflare Tunnel is a good fit when the agent can reach the private service through an authenticated HTTPS hostname. A connector in your network dials out to Cloudflare, and the Cloud Agent calls that hostname like any other external URL. You can protect the hostname with Cloudflare Access service tokens, store the token values as Cursor Secrets, and add the hostname to your Cloud Agent allowlist.

For TCP targets such as private databases, use a tunnel client that exposes a local TCP listener in the agent environment. The agent then connects to `localhost`, while the tunnel forwards traffic to the private origin.

For private GitHub Enterprise Server, GitLab Enterprise, source control APIs, and related webhook traffic, Enterprise teams can use [private connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) with AWS PrivateLink or Cloudflare Tunnel.

##### Access modes

Three modes control outbound network access for Cloud Agents:

| Mode                         | Behavior                                                                                                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Allow all network access** | Cloud Agents can reach any external host. No domain restrictions apply.                                                                                             |
| **Default + allowlist**      | Cloud Agents can reach the [default domains](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist) plus any domains you add to your allowlist. |
| **Allowlist only**           | Cloud Agents can only reach the domains you explicitly add to your allowlist.                                                                                       |

Even in **Allowlist only** mode, a small set of domains remain accessible so Cloud Agents can function. These include Cursor's own services and source control management (SCM) providers.

##### Artifact uploads

Cloud Agents upload [artifacts](https://cursor.com/docs/cloud-agent/capabilities.md#demos-and-artifacts) (screenshots, videos, and log references shown on PRs) to `cloud-agent-artifacts.s3.us-east-1.amazonaws.com`.

If you use **Default + allowlist** or **Allowlist only**, add the exact host to your allowlist so artifact uploads succeed. Don't broaden the entry to `*.s3.us-east-1.amazonaws.com`: the wildcard opens egress to every bucket in the region and creates an exfiltration path for a prompt-injected agent. Blocking the host disables uploads; agent sessions and other tool calls keep working.

##### User-level settings

Individual users can configure their network access mode from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents) under the **Security** header. Your user-level setting applies to all Cloud Agents you create.

When you select a mode that includes an allowlist (**Default + allowlist** or **Allowlist only**), an allowlist configuration section appears below the setting where you can add your custom domains.

##### Environment-level settings

Saved environments can have their own network access mode and allowlist. Use environment-level settings when one repo or repo group needs stricter egress than the rest of your team.

For example, you can keep a production-adjacent environment on **Allowlist only** while leaving a less sensitive environment on **Default + allowlist**. Agents that use the stricter environment inherit those restrictions.

Environment-level settings include two inheritance options:

| Mode                                         | Behavior                                                                                  |
| :------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **Inherit settings**                         | Uses the applicable user or team network access setting.                                  |
| **Inherit settings + environment allowlist** | Uses the applicable user or team setting and adds domains from the environment allowlist. |

You can also set an environment directly to **Allow all network access**, **Default + allowlist**, or **Allowlist only**.

##### Team-level settings

Team admins can set a default network access mode for the entire team from the same dashboard. The team-level allowlist is the same allowlist that admins configure for the [sandbox default network allowlist](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist). There is no separate allowlist to manage; one allowlist controls both Cloud Agent network access and the sandbox defaults.

When a team-level setting exists:

- If an environment defines its own mode, the **environment setting applies** to agents that use that environment.
- If an environment inherits settings and a user has configured their own setting, the **user setting takes precedence**.
- If neither the environment nor the user has configured a setting, the **team default applies**.

##### Locking the setting (Enterprise)

Locking is available for Enterprise teams only.

Enterprise team admins can lock the network access setting using the **Lock Network Access Policy** option. When locked:

- The team-level setting applies to every member, regardless of their individual preference.
- Users cannot override the locked setting from their own dashboard.

This gives admins full control over Cloud Agent network access across the organization.

##### Relationship to sandbox network policy

The "Default" domains in the **Default + allowlist** mode are the same [default network allowlist](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist) used by the desktop Agent's sandbox. The team-level allowlist is also shared: when an admin configures an allowlist on the dashboard, it applies to both Cloud Agent network access and the [sandbox network policy](https://cursor.com/docs/reference/sandbox.md).

#### Egress IP ranges

Cloud Agents make network connections from specific IP address ranges when accessing external services, APIs, or repositories.

##### API endpoint

The IP ranges are available via a [JSON API endpoint](https://cursor.com/docs/ips.json):

```bash
curl https://cursor.com/docs/ips.json
```

###### Response format

```json
{
  "version": 1,
  "modified": "2025-09-24T16:00:00.000Z",
  "cloudAgents": {
    "us3p": ["100.26.13.169/32", "34.195.201.10/32", "..."],
    "us4p": ["54.184.235.255/32", "35.167.37.158/32", "..."],
    "us5p": ["3.12.82.200/32", "52.14.104.140/32", "..."]
  },
  "gitEgressProxy": ["184.73.225.134/32", "3.209.66.12/32", "52.44.113.131/32"]
}
```

- **version**: Schema version number for the API response
- **modified**: ISO 8601 timestamp of when the IP ranges were last updated
- **cloudAgents**: Object containing IP ranges, keyed by cluster
- **gitEgressProxy**: IP addresses used by the [git egress proxy](https://cursor.com/docs/cloud-agent/security-network.md#git-egress-proxy-and-ip-allow-list)

IP ranges published in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). You can use an online conversion tool to convert from CIDR notation to IP address ranges if needed.

##### Using the IP ranges

These published IP ranges may be used by Cloud Agents to:

- Clone and push to remote repositories (unless using the [git egress proxy](https://cursor.com/docs/integrations/github.md#ip-allow-list-configuration))
- Download packages and dependencies
- Make API calls to external services
- Access web resources during agent execution

If your organization uses firewall rules or IP allowlists to control network access, you may need to allowlist these IP ranges to ensure Cloud Agents can properly access your services.

**Important considerations:**

- We make changes to our IP addresses from time to time for scaling and operational needs.
- We do not recommend allowlisting by IP address as your primary security mechanism.
- If you must use these IP ranges, we strongly encourage regular monitoring of the JSON API endpoint.

##### Git egress proxy and IP allow list

Cursor supports a similar but distinct feature to [use a git egress proxy for IP allow lists](https://cursor.com/docs/integrations/github.md#ip-allow-list-configuration). This proxy routes all git traffic through a narrower set of IPs and works across all git hosts, including GitHub, GitLab, Azure DevOps, and Bitbucket.

For git hosts specifically, we recommend the IP allow list configuration described in the link above, as it integrates directly with the Cursor GitHub app.

If you need to add the proxy IPs directly to an allowlist, use these addresses:

```text
184.73.225.134
3.209.66.12
52.44.113.131
```

##### Cursor Review IPs

If your team uses Cloud Agents alongside [Cursor Review](https://cursor.com/docs/review.md), allowlist these additional IPs on top of the git egress proxy IPs above:

```text
34.192.39.182
50.16.106.255
44.217.29.124
3.223.245.201
54.164.185.10
34.194.133.23
35.170.116.221
```

These IP addresses are stable. If the list ever changes, teams using IP allow
lists will get advance notice before any address is added or removed.

Enterprise customers with private GitHub Enterprise Server or GitLab Enterprise deployments can use [private connectivity options](https://cursor.com/docs/enterprise/private-connectivity.md), so Cloud Agents and Bugbot can access private source control systems.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cloud Agents settings

*Workspace admins can configure Cloud Agents from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents).*

**Source:** https://cursor.com/docs/cloud-agent/settings

Workspace admins can configure Cloud Agents from the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents).

#### Environment management

The **Environments** view lists the saved environments available to your team. Environments can be scoped to one repo or to a group of repos.

Open an environment to review:

- The repositories it applies to
- Whether it uses a snapshot or `.cursor/environment.json`
- The update script that runs before an agent starts
- Runtime secrets and build secrets
- Network access settings
- Version history and setup runs

Use **Update with Agent** when you want Cursor to inspect the current environment and propose a new setup. Use **New Setup Run** when you want Cursor to start setting up the environment fresh. Use **Restore** from version history to make a prior environment version active again.

#### Default settings

- **Default model** – the model used when a run does not specify one. Pick any model available for cloud agents.
- **Default repository** – when empty, agents ask the user to choose a repo. Supplying a repo here lets users skip that step.
- **Base branch** – the branch agents fork from when creating pull requests. Leave blank to use the repository’s default branch.

#### Network access settings

Control which network resources Cloud Agents can reach. User and team settings support three modes:

- **Allow all network access** – no domain restrictions.
- **Default + allowlist** – the [default domains](https://cursor.com/docs/agent/tools/terminal.md#default-network-allowlist) plus any domains you add.
- **Allowlist only** – only domains you explicitly add.

Users, team admins, and environment owners can configure network access. Environment-level settings can inherit user or team policy, add an environment allowlist, or define their own access mode. See [Network Access](https://cursor.com/docs/cloud-agent/security-network.md) for full details.

#### Security settings

All security options require admin privileges.

- **Display agent summary** – controls whether Cursor shows the agent's file-diff images and code snippets. Disable this if you prefer not to expose file paths or code in the sidebar.
- **Display agent summary in external channels** – extends the previous toggle to Slack or any external channel you've connected.
- **Team follow-ups** – controls whether team members can send follow-up messages to cloud agents created by other users on the team. See [team follow-ups](https://cursor.com/docs/cloud-agent/settings.md#team-follow-ups) below.

#### Team feature settings

Team admins can enable or disable these features for their team:

- **Long running agents** – controls whether team members can run agents for extended durations. Admins can enable or restrict this capability at the team level.
- **Computer use** – controls whether agents can use computer interaction capabilities (available to enterprise teams only).

Changes save instantly and affect new agents immediately.

##### Team follow-ups

Team members can send follow-up messages to cloud agents created by other users on the same team. This is useful when a teammate starts an agent and you need to course-correct, add context, or continue the work while they're unavailable.

Team admins control this behavior from the [Cloud Agents security settings](https://cursor.com/dashboard/cloud-agents) with three options:

| Setting                   | Behavior                                                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Disabled**              | Only the original creator can send follow-ups to their agent. No team follow-ups are allowed.                                                                                              |
| **Service accounts only** | Team members can send follow-ups to agents created by a [service account](https://cursor.com/docs/account/enterprise/service-accounts.md), but not to agents created by other human users. |
| **All**                   | Any team member can send follow-ups to any agent on the team, regardless of who created it.                                                                                                |

##### Lateral movement and secret exposure

Enabling team follow-ups means a user can influence the execution of a cloud agent that runs with *another user's* secrets and credentials. A follow-up message can instruct the agent to read environment variables, print secrets to logs, push credentials to an external endpoint, or perform actions using the original creator's access tokens.

A team member with limited permissions could escalate their access by directing an agent that holds a more privileged user's secrets. Treat this setting with the same care you would give shared SSH keys or service credentials.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cloud Agents API

*The Cloud Agents API v1 is in public beta. APIs may change before general*

**Source:** https://cursor.com/docs/cloud-agent/api/endpoints

##### Public beta

The Cloud Agents API v1 is in public beta. APIs may change before general
availability.

The Cloud Agents API lets you programmatically launch and manage cloud agents that work on your repositories.

- The Cloud Agents API accepts both [Basic and Bearer authentication](https://cursor.com/docs/api.md#authentication). Generate a user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api), or use a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md).
- For details on authentication methods, rate limits, and best practices, see the [API Overview](https://cursor.com/docs/api.md).
- View the full [OpenAPI specification](https://cursor.com/docs-static/cloud-agents-openapi.yaml) for detailed schemas and examples.
- Webhooks are coming soon. The legacy [v0 API](https://cursor.com/docs/cloud-agent/api/v0.md) still supports them — see [Webhooks](https://cursor.com/docs/cloud-agent/api/webhooks.md).

##### Migrating from v0?

This API splits work into a durable agent plus per-prompt runs, replacing the flatter v0 surface. The legacy [v0 reference](https://cursor.com/docs/cloud-agent/api/v0.md) remains available.

#### Endpoints

##### Create An Agent

/v1/agents

Create a Cloud Agent and immediately enqueue its initial run. The response returns both the durable `agent` and the initial `run`.

###### Request Body

`prompt` object (required)

The task prompt for the agent, including optional images.

`prompt.text` string (required)

The instruction text for the agent.

`prompt.images` array (optional)

Image inputs for the prompt. Each entry must include either `data` (base64-encoded bytes with a required `mimeType`) or `url` (an http or https URL that Cursor fetches). Maximum 5 images, 15 MB each. Supported MIME types: `image/png`, `image/jpeg`, `image/gif`, `image/webp`.

`model` object (optional)

Model selection. Omit this field to use the configured default. When omitted, Cursor resolves your user default model, then your team default model, then a system default.

`model.id` string (required if `model` provided)

An explicit model ID returned by `GET /v1/models` (for example, `claude-4-sonnet-thinking`).

`model.params` array (optional)

Per-model parameters to apply to the run, such as reasoning effort or context window size. Each item has an `id` and `value`. Use only parameters supported by the selected model — call `GET /v1/models` to discover the valid `id`/`params` combinations.

`name` string (optional)

Display name for the agent. Maximum 100 characters. When omitted, Cursor auto-derives a name from the prompt.

`env` object (optional)

Execution environment target. Use a named `cloud` environment, or route to a self-hosted `pool` or `machine`. Mutually exclusive with explicit `repos` when selecting a named Cursor-hosted environment.

`env.type` string (required if `env` provided)

Execution environment type. `cloud` uses Cursor-hosted VMs; `pool` and `machine` route to self-hosted workers.

`env.name` string (optional)

Named Cursor-hosted environment, self-hosted pool, or self-hosted machine name.

`repos` array (optional)

Repository configuration. Mutually exclusive with a named cloud environment. Omit both `repos` and `env` to start a no-repo agent. Maximum 20 repositories.

`repos[0].url` string (required)

GitHub repository URL (for example, `https://github.com/your-org/your-repo`). Required on every repo entry, including when `prUrl` is provided.

`repos[0].startingRef` string (optional)

Branch name or commit SHA to use as the starting point. Ignored when `prUrl` is provided.

`repos[0].prUrl` string (optional)

GitHub pull request URL. When provided, the agent works on this PR's repository and branches; `startingRef` is ignored. `url` must still be set on the same `repos` entry.

`workOnCurrentBranch` boolean (optional, default: false)

When `false` (the default), Cursor pushes commits to a new auto-generated branch (`cursor/...`) based on `repos[0].startingRef` (or the PR base ref when `prUrl` is set). When `true`, Cursor pushes directly to that starting ref — for a non-PR create, that's the branch you passed in `startingRef`; for a `prUrl` create, that's the PR's head branch. The branch the agent pushed shows up in the agent's `git.branches[]`.

`autoCreatePR` boolean (optional)

Whether Cursor should open a pull request when the run completes.

`skipReviewerRequest` boolean (optional)

Whether to skip requesting the user as a reviewer when Cursor opens a PR. Only applies when `autoCreatePR` is `true`.

`envVars` object (optional)

Session-scoped environment variables for the cloud agent. Values are encrypted at rest, injected into the agent's shell, and deleted with the agent. Maximum 50 entries; names up to 255 bytes (can't start with `CURSOR_`), values up to 4096 bytes. Cannot be combined with a client-supplied `agentId`.

**Beta:** `envVars` is rolling out. If it isn't enabled for your account yet, the field is silently ignored on create rather than failing the request — verify the values are present by inspecting the agent shell on a first run before relying on them in production.

`mcpServers` array (optional)

Inline MCP server definitions available to the agent. Maximum 50 servers. Remote servers support `headers` or OAuth `auth`; stdio servers run inside the cloud VM and can receive `env`. Server names must be unique.

`mcpServers[0].name` string (required)

The MCP server name exposed to the agent.

`mcpServers[0].type` string (optional)

Transport type: `http`, `sse`, or `stdio`. Defaults to `http` for remote servers with `url`, and `stdio` for servers with `command`.

`mcpServers[0].url` string (required for remote MCP)

HTTP or HTTPS URL for a remote MCP server. URLs with username or password are not allowed.

`mcpServers[0].command` string (required for stdio MCP)

Command to start a stdio MCP server inside the cloud agent VM. Use `args` and `env` for arguments and runtime secrets.

`customSubagents` array (optional)

Define custom subagents the main agent can delegate to during the run. Maximum 20 subagents. Each entry requires `name`, `description`, and `prompt`, plus an optional `model` (model ID string, `ModelSelection` object, or `"inherit"`). Names must be unique and cannot collide with built-ins (`explore`, `debug`, `shell`, `computerUse`, etc.).

`mode` string (optional, default: agent)

Initial conversation mode for the agent's first run. `plan` explores and drafts a plan before coding ([Plan mode](https://cursor.com/help/ai-features/plan-mode.md)); `agent` implements changes directly.

`agentId` string (optional)

Client-supplied agent identifier in the form `bc-<uuid>`. Useful for idempotent create flows — re-POSTing the same `agentId` returns `409 agent_id_conflict` rather than creating a duplicate. Cannot be combined with `envVars`; omit `agentId` so the server mints one when you need session secrets.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Add a README with setup instructions"
    },
    "model": {
      "id": "composer-2",
      "params": [
        { "id": "fast", "value": "true" }
      ]
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-repo",
        "startingRef": "main"
      }
    ],
    "mcpServers": [
      {
        "name": "linear",
        "type": "http",
        "url": "https://mcp.linear.app/sse",
        "headers": {
          "Authorization": "Bearer YOUR_LINEAR_API_KEY"
        }
      },
      {
        "name": "github",
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN"
        }
      }
    ],
    "autoCreatePR": true
  }'
```

**Response:**

```json
{
  "agent": {
    "id": "bc-00000000-0000-0000-0000-000000000001",
    "name": "Add README with setup instructions",
    "status": "ACTIVE",
    "env": {
      "type": "cloud"
    },
    "repos": [
      {
        "url": "https://github.com/your-org/your-repo",
        "startingRef": "main"
      }
    ],
    "workOnCurrentBranch": false,
    "autoCreatePR": true,
    "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
    "createdAt": "2026-04-13T18:30:00.000Z",
    "updatedAt": "2026-04-13T18:30:00.000Z",
    "latestRunId": "run-00000000-0000-0000-0000-000000000001"
  },
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000001",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:30:00.000Z",
    "updatedAt": "2026-04-13T18:30:00.000Z"
  }
}
```

##### List Agents

/v1/agents

List agents for the authenticated user, newest first.

###### Query Parameters

`limit` number (optional)

Number of agents to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

`prUrl` string (optional)

Filter agents by GitHub pull request URL.

`includeArchived` boolean (optional, default: true)

Whether to include archived agents in the response.

List items only include the durable identity fields. Call `GET /v1/agents/{id}` to load the full record (`repos`, `workOnCurrentBranch`, `autoCreatePR`, etc.).

`nextCursor` is **omitted** from the response when there are no more pages — it is not returned as `null`. Treat its absence as "no more results".

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents?limit=20' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "bc-00000000-0000-0000-0000-000000000001",
      "name": "Add README with setup instructions",
      "status": "ACTIVE",
      "env": {
        "type": "cloud"
      },
      "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
      "createdAt": "2026-04-13T18:30:00.000Z",
      "updatedAt": "2026-04-13T18:45:00.000Z",
      "latestRunId": "run-00000000-0000-0000-0000-000000000001"
    }
  ],
  "nextCursor": "bc-00000000-0000-0000-0000-000000000002"
}
```

##### Get An Agent

/v1/agents/

Retrieve durable metadata for an agent. Execution status lives on runs — fetch `latestRunId` and call [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run) to read run state.

###### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001",
  "name": "Add README with setup instructions",
  "status": "ACTIVE",
  "env": {
    "type": "cloud"
  },
  "repos": [
    {
      "url": "https://github.com/your-org/your-repo",
      "startingRef": "main"
    }
  ],
  "workOnCurrentBranch": false,
  "autoCreatePR": true,
  "url": "https://cursor.com/agents/bc-00000000-0000-0000-0000-000000000001",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:30:00.000Z",
  "latestRunId": "run-00000000-0000-0000-0000-000000000001"
}
```

##### Create A Run

/v1/agents//runs

Send a follow-up prompt to an existing active agent. The new run uses the agent's current conversation and workspace state.

Only one run can be active per agent. Calling this while another run is `CREATING` or `RUNNING` returns `409 agent_busy`. Wait for the existing run to terminate, or cancel it.

###### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

###### Request Body

`prompt` object (required)

The follow-up prompt, including optional images.

`prompt.text` string (required)

The follow-up instruction text.

`prompt.images` array (optional)

Image inputs for the follow-up. Each entry must include either `data` (base64-encoded bytes with a required `mimeType`) or `url`. Maximum 5 images, 15 MB each. Supported MIME types: `image/png`, `image/jpeg`, `image/gif`, `image/webp`.

`mcpServers` array (optional)

Inline MCP server definitions for this follow-up run. When provided, these replace any create-time inline MCP servers for this run. Omit to keep the agent's current MCP configuration.

`mode` string (optional)

Conversation mode override for this follow-up run: `agent` or `plan`. Omit to keep the conversation's current mode from prior runs.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs \
  -u YOUR_API_KEY: \
  --header 'Content-Type: application/json' \
  --data '{
    "prompt": {
      "text": "Also add troubleshooting steps"
    },
    "mcpServers": [
      {
        "name": "docs",
        "type": "http",
        "url": "https://example.com/mcp"
      }
    ]
  }'
```

**Response:**

```json
{
  "run": {
    "id": "run-00000000-0000-0000-0000-000000000002",
    "agentId": "bc-00000000-0000-0000-0000-000000000001",
    "status": "CREATING",
    "createdAt": "2026-04-13T18:50:00.000Z",
    "updatedAt": "2026-04-13T18:50:00.000Z"
  }
}
```

##### List Runs

/v1/agents//runs

List runs for an agent, newest first.

###### Path Parameters

`id` string

Unique identifier for the agent.

###### Query Parameters

`limit` number (optional)

Number of runs to return. Default: 20, Max: 100.

`cursor` string (optional)

Pagination cursor from `nextCursor` on the previous response.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs?limit=20' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "run-00000000-0000-0000-0000-000000000002",
      "agentId": "bc-00000000-0000-0000-0000-000000000001",
      "status": "RUNNING",
      "createdAt": "2026-04-13T18:50:00.000Z",
      "updatedAt": "2026-04-13T18:51:00.000Z",
      "git": {
        "branches": [
          {
            "repoUrl": "github.com/your-org/your-repo",
            "branch": "cursor/add-readme-a1b2"
          }
        ]
      }
    }
  ]
}
```

##### Get A Run

/v1/agents//runs/

Retrieve status, timestamps, and (for terminal runs) the final result, duration, and pushed branches for a specific run.

###### Path Parameters

`id` string

Unique identifier for the agent.

`runId` string

Unique identifier for the run (for example, `run-00000000-0000-0000-0000-000000000001`).

###### Response Fields

The base run fields (`id`, `agentId`, `status`, `createdAt`, `updatedAt`) are always present. The following are populated as soon as data is available:

`durationMs` integer (terminal runs)

Wall-clock duration of the run in milliseconds, computed once the run reaches `FINISHED`, `ERROR`, `CANCELLED`, or `EXPIRED`.

`result` string (terminal runs)

Final assistant reply text for a terminated run.

`git` object (when a branch has been pushed)

The agent's current pushed branches and pull requests. `git.branches[]` contains `{ repoUrl, branch?, prUrl? }` entries — one per branch the agent has pushed (stacked agents produce multiple).

**Per-agent state, not per-run.** Every run on the same agent returns the same `git` snapshot. Use the agent's `latestRunId` or the SSE stream to attribute work to a specific run.

`repoUrl` is returned without the scheme (for example, `github.com/your-org/your-repo`) — different from request `repos[].url`, which keeps the `https://` prefix.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "run-00000000-0000-0000-0000-000000000001",
  "agentId": "bc-00000000-0000-0000-0000-000000000001",
  "status": "FINISHED",
  "createdAt": "2026-04-13T18:30:00.000Z",
  "updatedAt": "2026-04-13T18:45:00.000Z",
  "durationMs": 12357,
  "result": "Added README.md with installation instructions and usage examples.",
  "git": {
    "branches": [
      {
        "repoUrl": "github.com/your-org/your-repo",
        "branch": "cursor/add-readme-a1b2",
        "prUrl": "https://github.com/your-org/your-repo/pull/123"
      }
    ]
  }
}
```

##### Stream A Run

/v1/agents//runs//stream

Stream Server-Sent Events (SSE) for one run. The stream is scoped to the requested run and does not replay prior runs.

###### Event types

- `status` — run status update. Payload: `{ runId, status }`.
- `assistant` — assistant text delta. Payload: `{ text }`.
- `thinking` — thinking text delta. Payload: `{ text }`.
- `tool_call` — tool call status update. Payload: `{ callId, name, status, args?, result?, truncated? }`.
- `interaction_update` — optional richer event emitted alongside the simplified events above. Payload matches the `InteractionUpdate` shape consumed by the [TypeScript SDK](https://cursor.com/docs/sdk/typescript.md), with subtypes like `text-delta`, `tool-call-started` / `tool-call-completed`, `step-started` / `step-completed`, and `turn-ended`. If you only need plain text and tool calls, handle the simplified events and ignore `interaction_update`. If you want the full SDK-shape stream, handle `interaction_update` and ignore the simplified events.
- `heartbeat` — keepalive event. Payload: `{}`.
- `result` — terminal run status. Payload: `{ runId, status, text?, durationMs?, git? }`. `text` is the final assistant reply, `durationMs` is the wall-clock run duration in milliseconds, and `git` mirrors `Run.git` (the agent's current pushed branches, not just this run's).
- `error` — stream error. Payload: `{ code, message }`.
- `done` — stream complete. Payload: `{}`.

###### Tool call payloads

`tool_call` events use a stable envelope around tool-specific inputs and outputs:

```typescript
type JsonValue =
  | string
  | number
  | boolean
  | null
  | JsonValue[]
  | { [key: string]: JsonValue };

interface ToolCallEventData {
  callId: string;
  name: string;
  status: "running" | "completed";
  args?: JsonValue;
  result?: JsonValue;
  truncated?: {
    args?: true;
    result?: true;
  };
}
```

`callId` identifies one tool invocation across updates. `name` is the public tool name, such as `read_file`, `run_terminal_cmd`, or `mcp`. `args` and `result` are tool-specific JSON values. If `args` or `result` is too large to include in the stream, Cursor omits that field and sets the matching `truncated` flag.

###### Resuming a stream

Most events include an `id` line — an opaque string you should not parse (current format looks like `1713033006000-0`, but treat it as opaque). The leading `status` event has no `id` — it is a sticky framing event that is re-sent at the top of every reconnect.

To resume after a disconnect, reconnect with `Last-Event-ID` set to the most recent received event id. The event id must belong to the requested run; otherwise the request returns `400 invalid_last_event_id`. After a successful resume, expect another `status` event before the resumed range begins.

###### Retention

Stream responses include the `X-Cursor-Stream-Retention-Seconds` header. After the retention window elapses, this endpoint may return `410 stream_expired`. Treat that as a signal to read terminal state via [Get A Run](https://cursor.com/docs/cloud-agent/api/endpoints.md#get-a-run) instead of retrying the stream.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001/stream \
  -u YOUR_API_KEY: \
  --header 'Accept: text/event-stream'
```

**Example stream:**

```text
event: status
data: {"runId":"run-00000000-0000-0000-0000-000000000001","status":"RUNNING"}

id: 1713033000000-0
event: assistant
data: {"text":"I'll update the README now."}

id: 1713033005000-0
event: tool_call
data: {"callId":"call-1","name":"read_file","status":"running","args":{"path":"README.md"}}

id: 1713033006000-0
event: tool_call
data: {"callId":"call-1","name":"read_file","status":"completed","args":{"path":"README.md"},"result":{"success":{"content":"# Project","totalLines":1,"fileSize":9,"path":"README.md"}}}

id: 1713033010000-0
event: result
data: {"runId":"run-00000000-0000-0000-0000-000000000001","status":"FINISHED","text":"Added README.md with installation instructions.","durationMs":12357,"git":{"branches":[{"repoUrl":"github.com/your-org/your-repo","branch":"cursor/add-readme-a1b2"}]}}

id: 1713033010000-0
event: done
data: {}
```

##### Cancel A Run

/v1/agents//runs//cancel

Cancel the active run for an agent. Cancellation is terminal — the run transitions to `CANCELLED` and cannot be resumed. To continue the conversation, create a new run on the same agent.

Cancelling a run that is already in a terminal state, or one that was never active, returns `409 run_not_cancellable`.

###### Path Parameters

`id` string

Unique identifier for the agent.

`runId` string

Unique identifier for the run to cancel.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/runs/run-00000000-0000-0000-0000-000000000001/cancel \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "run-00000000-0000-0000-0000-000000000001"
}
```

##### Get Agent Usage

/v1/agents//usage

Retrieve token usage for an agent, broken down per run. The response totals usage across every run on the agent and lists usage for each individual run. Token usage matches the `tokenUsage` reported by the team [usage events](https://cursor.com/docs/account/teams/admin-api.md#get-usage-events-data) endpoint.

###### Path Parameters

`id` string

Unique identifier for the agent (for example, `bc-00000000-0000-0000-0000-000000000001`).

###### Query Parameters

`runId` string (optional)

Scope the response to a single run (for example, `run-00000000-0000-0000-0000-000000000001`). Omit to return usage for every run on the agent. An unknown `runId` returns `404 run_not_found`.

###### Response Fields

`totalUsage` object

Token usage summed across the returned runs. Contains the same fields as each run's `usage` object.

`runs` array

Per-run usage, one entry per run (or a single entry when `runId` is set). Each object contains:

- `id` string - Run identifier (for example, `run-00000000-0000-0000-0000-000000000001`).
- `usageUuid` string (optional) - Internal usage identifier for the run. Omitted when the run has no recorded usage yet.
- `usage` object - Token usage for this run:
  - `inputTokens` number - Input tokens consumed.
  - `outputTokens` number - Output tokens generated.
  - `cacheWriteTokens` number - Tokens written to cache.
  - `cacheReadTokens` number - Tokens read from cache.
  - `totalTokens` number - Sum of the four token counts above.

Runs without any recorded token usage report zeros across all fields. A run that hasn't produced usage yet still appears in `runs` so you can track it over time.

```bash
# All runs on the agent
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/usage \
  -u YOUR_API_KEY:

# A single run
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/usage?runId=run-00000000-0000-0000-0000-000000000001' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "totalUsage": {
    "inputTokens": 12480,
    "outputTokens": 3110,
    "cacheWriteTokens": 18200,
    "cacheReadTokens": 42600,
    "totalTokens": 76390
  },
  "runs": [
    {
      "id": "run-00000000-0000-0000-0000-000000000002",
      "usageUuid": "00000000-0000-0000-0000-000000000002",
      "usage": {
        "inputTokens": 6320,
        "outputTokens": 1450,
        "cacheWriteTokens": 7100,
        "cacheReadTokens": 21300,
        "totalTokens": 36170
      }
    },
    {
      "id": "run-00000000-0000-0000-0000-000000000001",
      "usageUuid": "00000000-0000-0000-0000-000000000001",
      "usage": {
        "inputTokens": 6160,
        "outputTokens": 1660,
        "cacheWriteTokens": 11100,
        "cacheReadTokens": 21300,
        "totalTokens": 40220
      }
    }
  ]
}
```

#### Artifacts

Artifacts are agent-scoped because the workspace persists across runs.

##### List Artifacts

/v1/agents//artifacts

List artifacts produced by an agent. Each artifact's `path` is relative to the workspace's `artifacts/` directory.

Pass the `path` value returned here directly to [Download An Artifact](https://cursor.com/docs/cloud-agent/api/endpoints.md#download-an-artifact). v1 paths are relative; absolute v0 paths (`/opt/cursor/artifacts/...`) are not accepted.

###### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/artifacts \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "path": "artifacts/screenshot.png",
      "sizeBytes": 12345,
      "updatedAt": "2026-04-13T18:45:00.000Z"
    }
  ]
}
```

##### Download An Artifact

/v1/agents//artifacts/download

Retrieve a temporary 15-minute presigned S3 URL for a specific artifact.

###### Path Parameters

`id` string

Unique identifier for the agent.

###### Query Parameters

`path` string

Relative artifact path returned by [List Artifacts](https://cursor.com/docs/cloud-agent/api/endpoints.md#list-artifacts) (for example, `artifacts/screenshot.png`). Must be under `artifacts/`.

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/artifacts/download?path=artifacts/screenshot.png' \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "url": "https://cloud-agent-artifacts.s3.us-east-1.amazonaws.com/...",
  "expiresAt": "2026-04-13T19:00:00.000Z"
}
```

#### Agent Lifecycle

##### Archive An Agent

/v1/agents//archive

Archive an agent. Archived agents remain readable but cannot accept new runs until unarchived. Use this for reversible "soft delete" flows.

Archive is idempotent — re-archiving an already-archived agent returns `200` with no change. You don't need to check current state before calling.

###### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/archive \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

##### Unarchive An Agent

/v1/agents//unarchive

Unarchive an agent so it can accept new runs again.

Unarchive is idempotent — calling it on an already-active agent returns `200` with no change.

###### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request POST \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001/unarchive \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

##### Delete An Agent Permanently

/v1/agents/

Permanently delete an agent. This action is irreversible. Use [Archive](https://cursor.com/docs/cloud-agent/api/endpoints.md#archive-an-agent) for reversible removal.

###### Path Parameters

`id` string

Unique identifier for the agent.

```bash
curl --request DELETE \
  --url https://api.cursor.com/v1/agents/bc-00000000-0000-0000-0000-000000000001 \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "id": "bc-00000000-0000-0000-0000-000000000001"
}
```

#### Worker Tokens

##### Create A User-Scoped Worker Token

/v1/sub-tokens

Create a one-hour user-scoped token for a self-hosted worker to run as an active team member.

Requires an agent-scoped team service account API key. User-scoped tokens can't mint other user-scoped tokens.

The returned token expires after 1 hour and cannot refresh itself. Mint a new token with the service account API key when you need to refresh a running worker.

###### Request Body

Specify exactly one of the following to identify the target user:

`forUserEmail` string (optional)

Active team member email. Case-insensitive.

`forUserId` integer (optional)

Active team member's numeric Cursor user ID.

By email:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/sub-tokens \
  --header "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "forUserEmail": "alice@company.com"
  }'
```

By user ID:

```bash
curl --request POST \
  --url https://api.cursor.com/v1/sub-tokens \
  --header "Authorization: Bearer $CURSOR_SERVICE_ACCOUNT_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "forUserId": 42
  }'
```

**Response:**

```json
{
  "accessToken": "eyJ...",
  "expiresAt": "2026-04-24T19:00:00.000Z",
  "userId": 42,
  "teamId": 456
}
```

#### Fleet Management

Monitor pool worker utilization and build autoscaling against self-hosted Cloud Agent pools.

Authenticate with the pool's service account API key via Basic auth or Bearer token. Other API key types are rejected.

##### List Workers

/v0/private-workers

List self-hosted pool workers for the authenticated service account's team, newest first.

###### Query Parameters

`status` string (optional, default: `all`)

Filter by worker status. One of `all`, `in_use`, or `idle`.

`limit` integer (optional, default: 50)

Results per page. Range: 1 to 100.

`nextPageToken` string (optional)

Pagination cursor from the previous response.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers?status=idle&limit=50" \
  -u "$CURSOR_API_KEY:"
```

##### Get Fleet Summary

/v0/private-workers/summary

Return connected and in-use worker counts for the authenticated user and their team. Use this to trigger scaling decisions when utilization is high.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

**Example scaling check:**

```typescript
const summary = await response.json();
const team = summary.teamSummary;
if (team && team.totalConnected > 0) {
  const utilization = team.inUse / team.totalConnected;
  if (utilization >= 0.9) {
    // Scale up: provision additional workers
  }
}
```

##### Get Worker By ID

/v0/private-workers/

Retrieve a single self-hosted pool worker by its ID.

###### Path Parameters

`id` string

Unique identifier for the worker (for example, `pw_123`).

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pw_123" \
  -u "$CURSOR_API_KEY:"
```

##### List Pending Pool Requests

/v0/private-workers/pending-requests

List self-hosted pool requests that have not been assigned to a worker yet. Use this endpoint to scale capacity when users are waiting for an available pool worker.

This endpoint requires a service account API key. It returns requests for the key's team and excludes My Machines requests. If the key is scoped to specific repositories, pass `repository`; the repository must be in the key's allowed scope.

###### Query Parameters

`limit` number (optional)

Number of pending requests to return. Default: 50, Max: 100.

`pageToken` string (optional)

Pagination cursor from the previous response.

`repository` string (optional)

Filter by repository URL. Required for repo-scoped service account API keys.

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/pending-requests?limit=50&repository=https%3A%2F%2Fgithub.com%2Facme%2Fpayments-service" \
  -u "$CURSOR_API_KEY:"
```

**Response:**

```json
{
  "requests": [
    {
      "id": "bc-00000000-0000-0000-0000-000000000002",
      "userId": 321,
      "serviceAccountId": "sa_abc123",
      "repoOwner": "acme",
      "repoName": "payments-service",
      "repoUrl": "https://github.com/acme/payments-service",
      "labels": [
        { "key": "repo", "value": "acme/payments-service" },
        { "key": "pool", "value": "gpu" },
        { "key": "env", "value": "production" }
      ],
      "createdAtMs": 1737306880000
    }
  ],
  "nextPageToken": "eyJjcmVhdGVkQXRNcyI6MTczNzMwNjg4MDAwMH0="
}
```

`repoUrl` omits embedded credentials when the original repository URL includes userinfo.

#### Metadata Endpoints

##### API Key Info

/v1/me

Retrieve information about the API key being used for authentication.

###### Response Fields

`apiKeyName` string

Display name of the API key.

`createdAt` string

When the API key was created (ISO 8601).

`userId` integer (user-scoped keys)

Numeric Cursor user ID of the API key's owner. Omitted for service-account / team API keys, which aren't tied to a specific user.

`userEmail` string (user-scoped keys)

Email address of the API key's owner.

`userFirstName`, `userLastName` string (user-scoped keys)

First and last name of the API key's owner, when populated.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/me \
  -u YOUR_API_KEY:
```

**Response (user-scoped key):**

```json
{
  "apiKeyName": "Production API Key",
  "userId": 42,
  "createdAt": "2026-04-13T18:30:00.000Z",
  "userEmail": "developer@example.com",
  "userFirstName": "Alex",
  "userLastName": "Rivera"
}
```

**Response (service-account key):**

```json
{
  "apiKeyName": "Production Service Account",
  "createdAt": "2026-04-13T18:30:00.000Z"
}
```

##### List Models

/v1/models

Returns the recommended models you can pass to the `model.id` field on [Create An Agent](https://cursor.com/docs/cloud-agent/api/endpoints.md#create-an-agent), along with the parameters and variants each model accepts. Model parameters use the same `model.params` shape as the [TypeScript SDK ModelSelection](https://cursor.com/docs/sdk/typescript.md#modelselection).

To use the configured default model, omit `model` from the request body entirely. Cursor resolves your user default model, then your team default model, then a system default.

###### Response Fields

Each item in `items` describes one model:

`id` string

Pass this value as `model.id` when creating an agent.

`displayName` string

Human-readable name shown in the Cursor UI.

`description` string (optional)

Short description of the model.

`aliases` array (optional)

Alternate IDs that resolve to the same model (for example, `composer-latest`).

`parameters` array (optional)

Per-model parameter definitions. Each entry has an `id`, optional `displayName`, and a `values` array of permitted `{ value, displayName? }` entries. Use these to populate `model.params` on the create request.

`variants` array (optional)

Concrete `id`+`params` combinations the model accepts. Each entry has a `params` array (which may be empty), a `displayName`, an optional `description`, and an optional `isDefault` flag.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/models \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "id": "composer-2",
      "displayName": "Composer 2",
      "aliases": ["composer-latest", "composer"],
      "parameters": [
        {
          "id": "fast",
          "displayName": "Fast",
          "values": [
            { "value": "false" },
            { "value": "true", "displayName": "Fast" }
          ]
        }
      ],
      "variants": [
        {
          "params": [{ "id": "fast", "value": "true" }],
          "displayName": "Composer 2",
          "isDefault": true
        },
        {
          "params": [{ "id": "fast", "value": "false" }],
          "displayName": "Composer 2"
        }
      ]
    },
    {
      "id": "claude-4.6-sonnet-thinking",
      "displayName": "Claude 4.6 Sonnet (Thinking)",
      "variants": [
        {
          "params": [],
          "displayName": "Claude 4.6 Sonnet (Thinking)",
          "isDefault": true
        }
      ]
    }
  ]
}
```

##### List GitHub Repositories

/v1/repositories

List GitHub repositories accessible to the authenticated user through Cursor's GitHub App installation.

**This endpoint has very strict rate limits.**

Limit requests to **1 / user / minute**, and **30 / user / hour.**

This request can take tens of seconds to respond for users with access to many repositories.

Make sure to handle this information not being available gracefully.

```bash
curl --request GET \
  --url https://api.cursor.com/v1/repositories \
  -u YOUR_API_KEY:
```

**Response:**

```json
{
  "items": [
    {
      "url": "https://github.com/your-org/your-repo"
    }
  ]
}
```


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---

## Integrations

### Slack

*With Cursor's integration for Slack, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on your tasks directly from Slack by mentioning `@cursor` with a prompt.*

**Source:** https://cursor.com/docs/integrations/slack

With Cursor's integration for Slack, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on your tasks directly from Slack by mentioning `@cursor` with a prompt.

[Media](https://cursor.com/docs-static/images/cloud-agent/slack/slack-agent.mp4)

#### Get started

##### Installation

1. Go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)

2. Click *Connect* next to Slack or go to [installation page](https://cursor.com/api/install-slack-app) from here

3. You'll be prompted to install the Cursor app for Slack in your workspace.

4. After installing in Slack, you'll be redirected back to Cursor to finalize setup

   1. Connect a repository provider (if not already connected) and pick a default repository
   2. Enable usage-based pricing
   3. Confirm privacy settings

5. Start using Cloud Agents in Slack by mentioning `@cursor`

#### How to use

Mention `@cursor` and give your prompt. Cursor tries to detect a repository, model, base branch, or named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md) from your message. It also uses your recent agent activity when selecting a repository.

For a named environment, include its name in your prompt. For example: `@Cursor use the Platform environment to update the shared API`.

##### Commands

Run `@Cursor help` for an up-to-date command list.

| Command                      | Description                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------- |
| `@Cursor [prompt]`           | Start a Cloud Agent. In threads with existing agents, adds followup instructions       |
| `@Cursor settings`           | Configure defaults and channel's default repository                                    |
| `@Cursor [options] [prompt]` | Set the target, model, branch, PR behavior, worker, or output channel for a run        |
| `@Cursor agent [prompt]`     | Force create a new agent in a thread (e.g. `@Cursor start a new agent to fix billing`) |
| `@Cursor list my agents`     | Show your running agents                                                               |

###### Options

Customize Cloud Agent behavior with these options:

| Option                | Description                                                                                                              | Natural language example       | Inline example      |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------- | :----------------------------- | :------------------ |
| `repo`                | Use a specific repository                                                                                                | `in acme/backend`              | `repo=acme/backend` |
| `env` / `environment` | Use a named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md)                                      | `use the Platform environment` | `env=Platform`      |
| `branch`              | Use a specific base branch                                                                                               | `work from the dev branch`     | `branch=dev`        |
| `model`               | Use a specific model                                                                                                     | `with opus`                    | `model=opus`        |
| `autopr`              | Enable or disable automatic PR creation                                                                                  | Inline option required         | `autopr=false`      |
| `worker` / `machine`  | Run on a named [My Machine](https://cursor.com/docs/cloud-agent/my-machines.md#trigger-this-machine-from-a-chat-surface) | Inline option required         | `worker=my-devbox`  |
| `pool`                | Run on a named [self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md#triggering-pool-agents)        | Inline option required         | `pool=gpu`          |
| `self_hosted`         | Run on your team's self-hosted pool                                                                                      | Inline option required         | `self_hosted=true`  |
| `channel`             | Post agent updates in another channel you and Cursor can access                                                          | Inline option required         | `channel=#eng-bots` |

###### Syntax formats

Natural:

```bash
@Cursor with opus, fix the login bug in backend-api
```

Inline:

```bash
@Cursor env=Platform branch=dev model=opus autopr=false Fix the login bug
```

Use quotes for environment names with spaces:

```bash
@Cursor env="Platform Services" Update the shared API
```

###### Option precedence

When combining options:

- **Explicit values** override defaults
- **Later values** override earlier ones if duplicated
- **Inline options** take precedence over settings modal defaults
- **`env`** takes precedence over `repo` when both are present

The bot parses options from anywhere in the message, allowing natural command writing.

###### Using thread context

Cloud Agents understand and use context from existing thread discussions. Useful when your team discusses an issue and you want the agent to implement the solution based on that conversation.

Cloud Agents read the entire thread for context when invoked,
understanding and implementing solutions based on the team's discussion.

###### When to use force commands

**When do I need `@Cursor agent`?**

In threads with existing agents, `@Cursor [prompt]` adds followup instructions (only works if you own the agent). To launch a separate agent, use `@Cursor agent [prompt]`, or ask in natural language:

```bash
@Cursor start a new agent to refactor billing
```

Phrases like "create a new agent", "launch a fresh agent", or "new agent please" work the same way.

**When do I need `Add follow-up` (from context menu)?**

Use the context menu (⋯) on an agent's response for followup instructions. Useful when multiple agents exist in a thread and you need to specify which one to follow up on.

##### Status updates & handoff

When Cloud Agent runs, you first get an option to *Open in Cursor*.

![Open in Cursor button in Slack](https://cursor.com/docs-static/images/cloud-agent/slack/slack-open-in-cursor.png)

When Cloud Agent completes, you get a notification in Slack and an option to view the created PR in GitHub.

![View PR in GitHub in Slack](https://cursor.com/docs-static/images/cloud-agent/slack/slack-view-pr.png)

##### Managing agents

To see all running agents, run `@Cursor list my agents`.

Manage Cloud Agents using the context menu by clicking the three dots (⋯) on any agent message.

![Slack agent context menu](https://cursor.com/docs-static/images/cloud-agent/slack/slack-context-menu.png)

Available options:

- **Add follow-up**: Add instructions to an existing agent
- **Delete**: Stop and archive the Cloud Agent
- **View request ID**: View unique request ID for troubleshooting (include when contacting support)
- **Give feedback**: Provide feedback about agent performance

#### Configuration

Manage default settings and privacy options from [Dashboard → Cloud Agents](https://www.cursor.com/dashboard/cloud-agents).

##### Settings

###### Default Model

Used when no model is specified in your message. See [settings](https://www.cursor.com/dashboard/cloud-agents) for available options.

###### Repository Selection

Cursor automatically selects the right repository based on:

1. **Your message content** — Repository names or keywords in your prompt
2. **Recent agent activity** — Repositories you've used recently
3. **Routing rules** — Custom keyword-to-repo mappings (see below)
4. **Default repository** — Fallback when no match is found

To use a specific repository, include its name in your message. For example: `@Cursor in mobile-app, fix the login bug`.

###### Base Branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch (often `main`)

##### Channel Settings

Configure default settings at the channel level using `@Cursor settings`. These settings are per team and override your personal defaults for that channel.

Channel settings only apply to public channels.

Particularly useful when:

- Different channels work on different repositories
- Teams want consistent settings across all members

To configure channel settings:

1. Run `@Cursor settings` in the desired channel
2. Set the default repository for that channel
3. All team members using Cloud Agents in that channel use these defaults

Channel settings take precedence over personal defaults but can be overridden
by mentioning a specific repo in your message.

##### Routing Rules

Routing rules let you define keywords that automatically map to a target. When your message contains a keyword, Cursor routes the agent to the associated repository or [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md). Environments can bundle multiple repositories, so one keyword can start an agent with every repo it needs already configured.

###### Setting up routing rules

1. Go to [Dashboard → Cloud Agents](https://www.cursor.com/dashboard/cloud-agents)
2. Find the **Routing Rules** section
3. Add keyword-to-target mappings, pointing each keyword at a repository or an environment

###### Example rules

| Keyword    | Target                  |
| :--------- | :---------------------- |
| `frontend` | `acme/web-app`          |
| `mobile`   | `acme/mobile-app`       |
| `api`      | `acme/backend-services` |
| `platform` | `Platform` environment  |

With these rules configured:

- `@Cursor fix the frontend nav bug` → routes to `acme/web-app`
- `@Cursor update the mobile onboarding flow` → routes to `acme/mobile-app`
- `@Cursor add a migration across the platform` → starts in the `Platform` environment, with all its repos ready

Targeting an environment is useful for multi-repo environments. Learn how to
configure one in the [cloud agent docs](https://cursor.com/docs/cloud-agent/setup.md), including
[multi-repo environments](https://cursor.com/docs/cloud-agent/setup.md#multi-repo-environments).

###### How routing works

Cursor evaluates your message in this order:

1. **Your message content** — Repository names or keywords in your prompt
2. **Recent agent activity** — Repositories you've used recently
3. **Routing rules** — Custom keyword-to-target mappings (repository or environment)
4. **Channel default** — The repository set for this channel
5. **Default repository** — Fallback when no match is found

##### Privacy

Cloud Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard/cloud-agents).

Privacy Mode (Legacy) is not supported. Cloud Agents require temporary
code storage while running.

###### Display Agent Summary

Display agent summaries and diff images. May contain file paths or code snippets. Can be turned On/Off.

###### Display Agent Summary in External Channels

For Slack Connect with other workspaces or channels with external members like Guests, choose to display agent summaries in external channels.

#### Permissions

Cursor requests these Slack permissions for Cloud Agents to work within your workspace:

| Permission          | Description                                                                         |
| :------------------ | :---------------------------------------------------------------------------------- |
| `app_mentions:read` | Detects @mentions to start Cloud Agents and respond to requests                     |
| `channels:history`  | Reads previous messages in threads for context when adding follow-up instructions   |
| `channels:join`     | Automatically joins public channels when invited or requested                       |
| `channels:read`     | Accesses channel metadata (IDs and names) to post replies and updates               |
| `chat:write`        | Sends status updates, completion notifications, and PR links when agents finish     |
| `files:read`        | Downloads shared files (logs, screenshots, code samples) for additional context     |
| `files:write`       | Uploads visual summaries of agent changes for quick review                          |
| `groups:history`    | Reads previous messages in private channels for context in multi-turn conversations |
| `groups:read`       | Accesses private channel metadata to post responses and maintain conversation flow  |
| `im:history`        | Accesses direct message history for context in continued conversations              |
| `im:read`           | Reads DM metadata to identify participants and maintain proper threading            |
| `im:write`          | Initiates direct messages for private notifications or individual communication     |
| `mpim:history`      | Accesses group DM history for multi-participant conversations                       |
| `mpim:read`         | Reads group DM metadata to address participants and ensure proper delivery          |
| `reactions:read`    | Observes emoji reactions for user feedback and status signals                       |
| `reactions:write`   | Adds emoji reactions to mark status - ⏳ for running, ✅ for completed, ❌ for failed  |
| `team:read`         | Identifies workspace details to separate installations and apply settings           |
| `users:read`        | Matches Slack users with Cursor accounts for permissions and secure access          |

#### Disclaimer

Cursor can make mistakes. Please double-check code and responses.

#### Privacy Policy

For information about how Cursor collects, uses, and protects your data, see our [Privacy Policy](https://cursor.com/privacy).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Microsoft Teams

*With Cursor's integration for Microsoft Teams, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on tasks directly from Microsoft Teams by mentioning `@Cursor` with a prompt.*

**Source:** https://cursor.com/docs/integrations/microsoft-teams

With Cursor's integration for Microsoft Teams, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on tasks directly from Microsoft Teams by mentioning `@Cursor` with a prompt.

#### Get started

##### Installation

1. Go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)

2. Click *Connect* next to Microsoft Teams or go to the [Microsoft Marketplace listing](https://marketplace.microsoft.com/en-us/product/WA200010720)

3. Install the Cursor app in your Microsoft Teams workspace

4. After installing in Microsoft Teams, you'll be redirected back to Cursor to finalize setup

   1. Connect GitHub, GitLab, Azure DevOps, or Bitbucket, if you haven't connected a repository provider yet
   2. Enable usage-based pricing
   3. Confirm privacy settings

5. Start using Cloud Agents in Microsoft Teams by mentioning `@Cursor`

#### How to use

Mention `@Cursor` and give your prompt. Cursor automatically picks the right repository, model, base branch, or named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md) based on your message, the thread context, and your recent agent activity.

To use a specific repository, include its name in your message:

- `@Cursor in cursor-app, fix the login bug`
- `@Cursor fix the auth issue in backend-api`

To use a specific model, mention it in your message:

- `@Cursor with opus, fix the login bug`
- `@Cursor use gpt-5.2 to refactor the auth module`

To use a named environment, mention it in your message or add `env=<name>`:

- `@Cursor use the Platform environment to update the shared API`
- `@Cursor env=Platform update the shared API`
- `@Cursor env="Platform Services" update the shared API`

##### Commands

Run `@Cursor help` for an up-to-date command list.

| Command                      | Description                                                                               |
| :--------------------------- | :---------------------------------------------------------------------------------------- |
| `@Cursor [prompt]`           | Start a Cloud Agent. In channel threads with existing agents, adds follow-up instructions |
| `@Cursor help`               | Show setup and usage help                                                                 |
| `@Cursor unlink`             | Disconnect your Cursor account from Microsoft Teams                                       |
| `@Cursor disconnect`         | Disconnect your Cursor account from Microsoft Teams                                       |
| `@Cursor [options] [prompt]` | Set the repository, environment, branch, or model for a run                               |

###### Options

Customize Cloud Agent behavior with these options:

| Option                | Description                                                                         | Natural language example       | Inline example            |
| :-------------------- | :---------------------------------------------------------------------------------- | :----------------------------- | :------------------------ |
| `repo`                | Use a specific repository                                                           | `in acme/web-app`              | `repo=acme/web-app`       |
| `env` / `environment` | Use a named [cloud agent environment](https://cursor.com/docs/cloud-agent/setup.md) | `use the Platform environment` | `env="Platform Services"` |
| `branch`              | Use a specific base branch                                                          | `work from the main branch`    | `branch=main`             |
| `model`               | Use a specific model                                                                | `with opus`                    | `model=opus`              |

###### Syntax formats

Natural:

```bash
@Cursor with opus, fix the login bug in backend-api
```

Inline:

```bash
@Cursor env="Platform Services" branch=dev model=opus Fix the login bug
```

###### Option precedence

When combining options:

- **Explicit values** override defaults
- **Inline options** override model and repository values inferred from your message
- **Dashboard settings** apply when no value is specified or inferred
- **`env`** takes precedence over `repo` when both are present

The bot parses options from anywhere in the message, allowing natural command writing.

###### Using thread context

Cloud Agents understand and use context from existing Microsoft Teams discussions. This is useful when your team discusses an issue and you want the agent to make the code change based on that conversation.

Cloud Agents read the relevant thread or chat context when invoked,
understanding and acting on your team's discussion.

###### Follow-up instructions

In channel threads, reply in the agent's thread with another `@Cursor` mention to add follow-up instructions.

In personal chats and group chats, continue the conversation from Cursor using *Open in Web* or *Open in Desktop*.

##### Status updates & handoff

When Cloud Agent starts, Microsoft Teams shows a launch card with the selected repository, model, and branch. The card includes options to *Open in Web*, *Open in Desktop*, and *Switch repository*.

When Cloud Agent completes, you get a Microsoft Teams notification with the result. If the agent opened a pull request, the card includes an option to view the PR.

##### Managing agents

Manage Cloud Agents using actions on the Microsoft Teams cards.

Available options:

- **Add follow-up**: Add instructions to an existing agent from a channel thread
- **Switch repository**: Relaunch the same request against a different repository
- **Delete**: Stop and archive the Cloud Agent
- **Open in Web**: Continue in the web interface
- **Open in Desktop**: Continue in Cursor
- **Update settings**: Manage your Cloud Agent defaults
- **Give feedback**: Send feedback about agent performance

#### Configuration

Manage default settings and privacy options from [Dashboard -> Cloud Agents](https://www.cursor.com/dashboard/cloud-agents).

##### Settings

###### Default model

Used when no model is specified in your message. See [settings](https://www.cursor.com/dashboard/cloud-agents) for available options.

###### Repository selection

Cursor automatically selects the right repository based on:

1. **Your message content**: repository names or keywords in your prompt
2. **Recent agent activity**: repositories you've used recently
3. **Default repository**: fallback when no match is found

To use a specific repository, include its name in your message. For example: `@Cursor in mobile-app, fix the login bug`.

###### Base branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch, often `main`.

##### Routing behavior

Cursor evaluates your Microsoft Teams message in this order:

1. **Explicit options**: `repo`, `env`, `branch`, and `model` values in your prompt
2. **Your message content**: repository names, model names, or branch names in your prompt
3. **Recent agent activity**: repositories you've used recently
4. **Default repository**: fallback when no match is found

##### Privacy

Cloud Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard/cloud-agents).

Privacy Mode (Legacy) is not supported. Cloud Agents require temporary
code storage while running.

###### Display agent summary

Display agent summaries and diff images. They may contain file paths or code snippets. You can turn this on or off.

#### Permissions

Cursor requests these Microsoft Teams permissions for Cloud Agents to work in your workspace:

| Permission                   | Description                                                         |
| :--------------------------- | :------------------------------------------------------------------ |
| `identity`                   | Identifies the Microsoft Teams user starting or managing an agent   |
| `messageTeamMembers`         | Sends direct messages for setup, account linking, and notifications |
| `ChannelMessage.Read.Group`  | Reads channel messages and replies for thread context               |
| `ChatMessage.Read.Chat`      | Reads personal and group chat messages for conversation context     |
| `ChannelSettings.Read.Group` | Reads channel metadata, including channel names and descriptions    |
| `TeamSettings.Read.Group`    | Reads team metadata, including team names and descriptions          |

The Cursor app supports personal chats, team channels, and group chats in Microsoft Teams.

#### Disclaimer

Cursor can make mistakes. Please double-check code and responses.

#### Privacy Policy

For information about how Cursor collects, uses, and protects your data, see our [Privacy Policy](https://cursor.com/privacy).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Jira

*With Cursor's integration for Jira, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on Jira work items by assigning them to Cursor or mentioning `@Cursor` in Jira.*

**Source:** https://cursor.com/docs/integrations/jira

With Cursor's integration for Jira, you can use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) to work on Jira work items by assigning them to Cursor or mentioning `@Cursor` in Jira.

#### Get started

##### Requirements

Before you install the Jira integration, make sure you have:

- Jira Commercial Cloud with Rovo enabled
- Admin access to the Jira site where you want to install the app
- Cursor admin access to the team you want to connect
- GitHub, GitLab, Azure DevOps, or Bitbucket connected to Cursor for repository access and pull requests

The Cursor Jira integration is currently available only on Cursor Teams and
Enterprise plans.

The Cursor Jira integration is not currently supported in Atlassian HIPAA or
FedRAMP (including Government Cloud) instances.

##### Installation

1. As a Cursor admin, go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)

2. Click *Connect* next to Jira

3. Continue to the Cursor app listing in the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/3903220956/cursor)

4. Click *Get it now*

5. Select the Jira site where you want to install Cursor and click *Review*

6. Review the app, then click *Get it now*

7. Once installation completes, you should be dropped into the Cursor Jira app configuration page. Wait a few minutes for Atlassian to notify us of the installation, and then click the *Connect to Cursor* button.

8. Connect the Jira site to your Cursor team

   - If you want to enable user-level authentication (which gives team members more visibility and control over their agents) instead of running agents with a service account, flip the *Require individual authentication* toggle.

9. Complete any remaining Cloud Agent setup in Cursor:

   - Connect GitHub, GitLab, Azure DevOps, or Bitbucket
   - Enable usage-based pricing
   - Confirm privacy settings
   - Choose a default repository, model, and base branch (under Cloud Agents settings in the Cursor Dashboard)

10. Return to Jira and start using Cursor from a work item

    - If you enabled user-level authentication, each user will need to do more set up below

##### Authentication mode

You can choose how Jira authenticates Cloud Agents on the Cursor Jira integration admin dashboard by enabling the *Require individual authentication* toggle.

| Mode                           | How it works                                     | Settings used                                                                                                                                              |
| :----------------------------- | :----------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service account authentication | Cloud Agents run under a service account.        | Uses only the team's Cloud Agent settings for routing, models, repositories, and defaults.                                                                 |
| User-level authentication      | Runs all Cloud Agents under each user's account. | Uses each user's Cloud Agent settings for routing, models, repositories, and defaults. Also allows users to find their running agents under their account. |

To connect each user:

1. Kick off an agent on a Jira work item
2. A prompt will appear to connect the account
3. Follow the link to connect the Jira account to a Cursor account associated with the team
4. Complete any remaining Cloud Agent setup in Cursor:
   - Connect GitHub, GitLab, Azure DevOps, or Bitbucket if you haven't connected a repository provider yet
   - Choose a default repository, model, and base branch (under *My Settings* Cloud Agents settings in the Cursor Dashboard)

#### How to use

Open a Jira work item and then assign it to Cursor or mention `@Cursor` in a comment. Cursor uses the work item title, description, comments, and available repository settings to start a Cloud Agent.

You can ask Cursor to fix bugs, add features, update tests, or investigate a task described in the work item.

##### Delegating work items

Assign a Jira work item to Cursor when the ticket already describes the task clearly.

1. Open the Jira work item
2. Click the assignee field
3. Select Cursor
4. Review the Cloud Agent that starts from the work item

##### Mentioning Cursor

Mention `@Cursor` in a Jira comment when you want to add specific instructions. You can include a repository, branch, or model in the same comment.

Examples:

- `@Cursor please investigate this regression`
- `@Cursor repo=acme/backend branch=release fix this before the release cut`
- `@Cursor model=gpt-5.6-sol and update the related tests`

##### Follow-up instructions

Open Rovo chat from the Jira work item to continue the conversation with Cursor.

##### Status updates and handoff

When a Cloud Agent starts, Jira shows agent status on the work item. Cursor posts progress while it works and returns a summary when the task completes.

If Cursor opens a pull request, the completion update links to the PR for review.

#### Configuration

Manage default settings and privacy options from [Dashboard -> Cloud Agents](https://www.cursor.com/dashboard/cloud-agents) under *Team Settings* or *My Settings*.

##### Settings

###### Default model

Used when no model is specified in the Jira work item or comment. See [settings](https://www.cursor.com/dashboard/cloud-agents) for available options.

###### Repository selection

Cursor selects the repository based on:

1. **Explicit values**: `repo`, `branch`, or `model` values in the Jira comment or work item
2. **Work item content**: repository names, service names, or keywords in the title, description, and comments
3. **Routing rules**: [custom keyword-to-repository mappings](https://cursor.com/docs/integrations/jira.md#routing-rules)
4. **Recent agent activity**: repositories you've used recently
5. **Default repository**: fallback when no match is found

To use a specific repository, include it in your comment. For example: `@Cursor repo=acme/mobile-app fix the login bug`. Your team service account or user account (depending on the mode you have turned on) *must* have access to this repo or else the attempt to kick off a Cloud Agent will fail.

###### Base branch

Starting branch for Cloud Agent. Leave blank to use the repository's default branch (recommended).

###### Branch prefix

Prefix for branch names created by Cloud Agents.

##### Options

Customize Cloud Agent behavior while using mentions with `@Cursor` with these options:

| Option   | Description         | Example             |
| :------- | :------------------ | :------------------ |
| `repo`   | Specify repository  | `repo=acme/web-app` |
| `branch` | Specify base branch | `branch=main`       |
| `model`  | Specify model       | `model=opus`        |

##### Routing rules

Routing rules let you define keywords that automatically map to specific repositories. When a Jira work item or comment contains specific keywords, Cursor routes the Cloud Agent to the associated repository.

Routing rules are the way you can tell the agent which projects, work items, key words, and other data should decide which repositories are used for which work items.

###### Setting up routing rules

1. Go to [Dashboard -> Cloud Agents](https://www.cursor.com/dashboard/cloud-agents)
2. Find the **Routing Rules** section
3. Add keyword-to-repository mappings

###### Example rules

| Keyword    | Repository              |
| :--------- | :---------------------- |
| `frontend` | `acme/web-app`          |
| `mobile`   | `acme/mobile-app`       |
| `api`      | `acme/backend-services` |
| `docs`     | `acme/documentation`    |

With these rules configured:

- A work item titled `Fix the frontend nav bug` routes to `acme/web-app`
- A comment saying `@Cursor update the mobile onboarding flow` routes to `acme/mobile-app`
- A comment saying `@Cursor add rate limiting to the api` routes to `acme/backend-services`

###### How routing works

Cursor evaluates Jira work items and comments in this order:

1. **Explicit values**: `repo`, `branch`, or `model` values in the Jira comment or work item
2. **Work item content**: repository names, service names, or keywords in the title, description, and comments
3. **Routing rules**: custom keyword-to-repository mappings
4. **Recent agent activity**: repositories you've used recently
5. **Default repository**: fallback when no match is found

##### Privacy

Cloud Agents support Privacy Mode.

Read more about [Privacy Mode](https://www.cursor.com/privacy-overview) or manage your [privacy settings](https://www.cursor.com/dashboard/cloud-agents).

Privacy Mode (Legacy) is not supported. Cloud Agents require temporary code
storage while running.

#### Permissions

During installation, Jira shows the permissions requested by the Cursor app. Cursor uses these permissions to:

- Identify the Jira user starting or managing a Cloud Agent
- Read work item fields, descriptions, comments, and related context
- Post status updates, completion summaries, and pull request links
- Receive events when work items are assigned to Cursor or mention `@Cursor`

Review the permission prompt in Atlassian Marketplace before installing the app.

#### FAQ

##### Which Jira sites are supported?

The Cursor Jira integration supports Atlassian commercial cloud sites with Rovo enabled. Atlassian HIPAA, FedRAMP, and Government Cloud instances are not supported.

##### Do I need usage-based billing?

Yes. Cloud Agents require usage-based billing. Enable usage-based billing while completing Cloud Agent setup in Cursor.

##### Who can install the Jira integration?

A user that is both a Jira admin and Cursor team admin will need to do the initial setup.

##### Do users need to connect their own Cursor accounts?

It depends on the authentication mode you choose. Service account authentication runs all Cloud Agents under a service account and uses team settings. User-level authentication connects each Jira user to Cursor, lets users find their running Cloud Agents from Jira in their Cursor dashboard, and uses each user's settings for routing, models, repositories, and defaults.

##### What else needs to be set up before Cursor can create PRs?

Connect GitHub, GitLab, Azure DevOps, or Bitbucket to Cursor and make sure Cloud Agent settings include the repositories, models, and base branches your team wants to use.

##### How do users continue a conversation with Cursor?

Open Rovo chat from the Jira work item to continue the conversation with Cursor. Alternately, open the Cloud Agent in Cursor and continue the conversation there.

#### Disclaimer

Cursor can make mistakes. Please double-check code and responses.

#### Privacy Policy

For information about how Cursor collects, uses, and protects your data, see our [Privacy Policy](https://cursor.com/privacy).


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Linear

*Use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) directly from Linear by delegating issues to Cursor or mentioning `@Cursor` in comments.*

**Source:** https://cursor.com/docs/integrations/linear

Use [Cloud Agents](https://cursor.com/docs/cloud-agent.md) directly from Linear by delegating issues to Cursor or mentioning `@Cursor` in comments.

[Media](https://cursor.com/docs-static/images/integrations/linear/linear-agent.mp4)

#### Get started

##### Installation

You must be a Cursor admin to connect the Linear integration. Other team
settings are available to non-admin members.

1. Go to [Cursor integrations](https://www.cursor.com/dashboard/integrations)
2. Click *Connect* next to Linear
3. Connect your Linear workspace and select team
4. Click *Authorize*
5. Complete any remaining Cloud Agent setup in Cursor:
   - Connect a repository provider and select a default repository
   - Enable usage-based pricing
   - Confirm privacy settings

##### Account linking

First use prompts account linking between Cursor and Linear. A repository provider connection is required for PR creation.

#### How to use

Delegate issues to Cursor or mention `@Cursor` in comments. Cursor analyzes issues and filters out non-development work automatically.

##### Delegating issues

1. Open Linear issue
2. Click assignee field
3. Select "Cursor"

![Delegating an issue to Cursor in Linear](https://cursor.com/docs-static/images/integrations/linear/linear-delegate.png)

##### Mentioning Cursor

Mention `@Cursor` in a comment to assign a new agent or provide additional instructions, for example: `@Cursor fix the authentication bug described above`.

#### Workflow

Cloud Agents show real-time status in Linear and create PRs automatically when complete. Track progress in [Cursor dashboard](https://www.cursor.com/dashboard/cloud-agents).

![Cloud Agent status updates in Linear](https://cursor.com/docs-static/images/integrations/linear/linear-activity.png)

##### Follow-up instructions

You can respond in the agent session and it'll get sent as a follow-up to the agent. Simply mention `@Cursor` in a Linear comment to provide additional guidance to a running Cloud Agent.

#### Configuration

Configure Cloud Agent settings from [Dashboard → Cloud Agents](https://www.cursor.com/dashboard/cloud-agents).

| Setting                | Location         | Description                                               |
| :--------------------- | :--------------- | :-------------------------------------------------------- |
| **Default Repository** | Cursor Dashboard | Primary repository when no project repository configured  |
| **Default Model**      | Cursor Dashboard | AI model for Cloud Agents                                 |
| **Base Branch**        | Cursor Dashboard | Branch to create PRs from (typically `main` or `develop`) |

##### Configuration options

You can configure Cloud Agent behavior using several methods:

**Issue description or comments**: Use `[key=value]` syntax, for example:

- `@cursor please fix [repo=anysphere/everysphere]`
- `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue labels**: Use parent-child label structure where the parent label is the configuration key and the child label is the value.

**Project labels**: Same parent-child structure as issue labels, applied at the project level.

Supported configuration keys:

- `repo`: Specify target repository (e.g., `owner/repository`)
- `branch`: Specify base branch for PR creation
- `model`: Specify AI model to use

##### Repository selection

Cursor determines which repository to work on using this priority order:

1. **Issue description/comments**: `[repo=owner/repository]` syntax in issue text or comments
2. **Issue labels**: Repository labels attached to the specific Linear issue
3. **Project labels**: Repository labels attached to the Linear project
4. **Default repository**: Repository specified in Cursor dashboard settings

###### Setting up repository labels

To create repository labels in Linear:

1. Go to **Settings** in your Linear workspace
2. Click **Labels**
3. Click **New group**
4. Name the group "repo" (case insensitive - must be exactly "repo", not "Repository" or other variations)
5. Within that group, create labels for each repository using the format `owner/repo`

These labels can then be assigned to issues or projects to specify which repository the Cloud Agent should work on.

![Configuring repository labels in Linear](https://cursor.com/docs-static/images/integrations/linear/linear-project-labels.png)

#### Advanced features

##### Triage rules (Advanced)

Set up automation rules in Linear to automatically delegate issues to Cursor:

1. Go to Linear project settings
2. Navigate to triage rules
3. Create rules that automatically:
   - Add specific labels
   - Assign issues to Cursor
   - Trigger Cloud Agents based on conditions

Triage rules are an advanced feature with some current limitations. Linear
requires a human assignee for rules to fire, though this requirement may be
removed in future updates.

##### Getting help

Check [agent activity](https://www.cursor.com/dashboard/cloud-agents) and include request IDs when contacting support.

#### Feedback

Share feedback through Linear comments or your Cursor dashboard support channels.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Notion

*Connect Cursor to Notion so you can delegate specs, tasks, and comments to agents. Because the integration is built on the Cursor SDK, every agent uses the same runtime, harness, and models that power Cursor.*

**Source:** https://cursor.com/docs/integrations/notion

Connect Cursor to Notion so you can delegate specs, tasks, and comments to agents. Because the integration is built on the Cursor SDK, every agent uses the same runtime, harness, and models that power Cursor.

Setup, chat, @mentions, and task assignment happen in Notion. Cursor runs the agent in a secure, sandboxed [Cloud Agent](https://cursor.com/docs/cloud-agent.md) VM, so it keeps working in the background while you handle other work.

See Notion's full docs [here](https://www.notion.com/help/connect-cursor-to-notion).

Cursor in Notion is in beta and is available to all Cursor users with Notion Business or Enterprise plans.

#### Get started

##### Requirements

Before you connect Cursor in Notion, make sure you have:

- GitHub connected to your Cursor account, used for repository access and pull requests
- A Cursor User API Key, which you create during setup

Cursor usage in Notion is billed through your existing account and is available at no extra cost.

##### Installation

1. In Notion, go to Agents in the sidebar → New Agent → Cursor.
2. Pick a starting point for your agent:

- Start with a default template: Templates for common tasks (like Code Q\&A and Bug Triage) help you customize Cursor for specific workflows.
- Start from scratch: Set up your own instructions, triggers, and connections with the standard Cursor harness.

3. Create or take your Cursor API key from your [dashboard](https://cursor.com/dashboard/api) and enter it into Notion.
4. Add the pages, databases, and Notion spaces your agent needs, such as your engineering task database and spec pages.
5. Save the agent and start working.

Cursor is now connected and your agent can write code and open pull requests from tasks or agent chat.

##### Permissions

1. The connection is tied to your personal API key. This means Cursor access and activity are linked to your individual Cursor account, not the whole workspace. Learn more →
2. Repos, environment, and connections come from your Cursor agent setup. Configure these in your Cursor dashboard.
3. Each Cursor agent can only access content you have shared in Notion. Permissions are set per agent in Notion and are not inherited from whoever starts a run.

#### How to use

Bring Cursor to your task boards, spec docs, and other context that already live in Notion.

If you try to use Cursor in a workspace where it does not have permissions, you should set a pop up to give it access.

##### Mention the agent

Start from a spec doc or page. Leave a comment and @-mention Cursor. Ask it to build the spec, refine the plan, or answer a question.

Cursor replies in comments. Click **View chat** to open the full conversation.

The first time you mention the agent on a page, approve page access when prompted.

Example prompts:

- "Make a plan for this spec. Wait for approval."
- "Review this doc and flag anything unclear."
- "Turn this into a checklist of concrete tasks and then open PRs for each."

##### Assign a task

On a task database or board, assign a task to Cursor. The agent will:

- Update task status as it works
- Post progress as comments
- Link to any pages or PRs it creates

#### Troubleshooting

##### The agent can't access a page or database

- Confirm the page or database is listed in **Tools & access**, not only referenced in instructions.
- Confirm the page isn't restricted to a group the agent doesn't belong to.
- If the page is private, share it with the agent directly.

##### GitHub connection fails or the agent can't push

- Confirm the token has **Contents: read/write** and **Pull requests: read/write** scopes.
- Check whether SSO or org approval is required in your GitHub organization.
- Confirm the default repository in your setup is correct.
- Regenerate the token if it expired, then reconnect.

##### The agent didn't fire when I @mentioned it

- Confirm the **agent mentioned** trigger is on.
- Mention the agent in a **comment** rather than in page body text. Comments are most reliable.
- Confirm the agent has access to the page you mentioned it on.

#### FAQ

##### How does billing work?

Cursor usage in Notion is billed through your existing Cursor account, the same way [Cloud Agent](https://cursor.com/docs/cloud-agent.md) usage is billed. It's available to all Cursor users at no extra cost. You'll also need a Notion Business or Enterprise plan.

##### Where can I view Cursor activity?

Results appear in Notion on the page or task where the agent ran. You can also find your chat sessions in the agent view in Notion, or in Cursor.

##### Do Cursor runs kicked off from Notion respect zero data retention (ZDR)?

Yes. Agent runs respect your existing privacy settings in Cursor.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GitHub

*The Cursor GitHub app connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).*

**Source:** https://cursor.com/docs/integrations/github

The Cursor GitHub app connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

#### Setup

##### GitHub.com

Requires Cursor admin access and GitHub org admin access.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to GitHub (or **Manage Connections** if already connected)
3. Choose **All repositories** or **Selected repositories**
4. Return to the dashboard to configure features on your repositories

[GitHub setup](https://cursor.com/docs-static/images/bugbot/bugbot-install.mp4)

To disconnect your GitHub account, return to the integrations dashboard and click **Disconnect Account**.

##### GitHub Enterprise Server

##### Prerequisites

- Running a supported version of GitHub Enterprise Server (v3.8 or later recommended)
- Admin privileges on your GHES instance
- Cursor team admin access (required to see the GitHub Enterprise registration option in the dashboard)

##### Networking

GHES requires secure inbound access from Cursor and outbound access for webhook notifications.

###### IP whitelisting (recommended)

Add these IP addresses to your allowlist:

```text
184.73.225.134
3.209.66.12
52.44.113.131
34.192.39.182
50.16.106.255
44.217.29.124
3.223.245.201
54.164.185.10
34.194.133.23
35.170.116.221
```

For other connection options beyond IP whitelisting, see [Advanced networking](https://cursor.com/docs/integrations/github.md#advanced-networking).

###### Proxy requirements

If you run a proxy in front of GHES, make sure it allows Cursor's GitHub App integration to use authenticated GitHub REST and GraphQL APIs. Cursor uses these APIs during app setup and after webhook delivery to resolve repository identity, inspect pull request state, read checks and reviews, and update prior Bugbot output.

The proxy should allow authenticated GitHub API requests from Cursor without blocking or rewriting them.

##### Register the Cursor Enterprise App

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations). In the **Source Control** section, find the **GitHub Enterprise** row (listed under GitHub) and click **Manage apps**.
2. Enter the **base URL** of your GHES instance (e.g., `https://git.yourcompany.com`)
3. Enter the name of the **Organization** that will own the application
   - This should be your company's Organization inside your GHES installation
   - You need administrator privileges for this Organization
   - Other Organizations can access the app once registered
   - Leave blank to use your user account (not recommended)
4. Click **Register**
5. Choose a name for the Cursor Enterprise Application (default recommended)
6. The app will appear under your available GitHub Apps in your GHES instance
7. Return to the dashboard to configure features on your repositories

#### IP allow list configuration

If your organization uses GitHub's IP allow list feature to restrict access to your repositories, Cursor can be configured to use a hosted egress proxy with a narrow set of IPs.

Before configuring IP allowlists, contact [hi@cursor.com](mailto:hi@cursor.com) to enable this feature for your team. This is required for either configuration method below.

##### Enable IP allow list configuration for installed GitHub Apps (recommended)

The Cursor GitHub app has the IP list already pre-configured. You can enable the allowlist for installed apps to automatically inherit this list. This is the **recommended approach**, as it allows us to update the list and your organization receives updates automatically.

To enable this:

1. Go to your organization's Security settings
2. Navigate to IP allow list settings
3. Check **"Allow access by GitHub Apps"**

For detailed instructions, see [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

##### Add IPs directly to your allowlist

If your organization uses IdP-defined allowlists in GitHub or otherwise cannot use the pre-configured allowlist, add the proxy IPs listed in [Git egress proxy and IP allow list](https://cursor.com/docs/cloud-agent/security-network.md#git-egress-proxy-and-ip-allow-list).

#### Advanced networking

Self-hosted instances support multiple connection methods beyond IP whitelisting. For setup details and supported private networking options, see [Private Connectivity](https://cursor.com/docs/enterprise/private-connectivity.md).

##### AWS PrivateLink

Available for Enterprise customers. Use AWS PrivateLink when your GitHub Enterprise Server is in AWS or can sit behind an AWS Network Load Balancer. PrivateLink can cover Cursor accessing GHES and, when needed, GHES sending webhooks back to Cursor without public internet egress.

**Best for:** AWS-hosted GHES instances and teams that want private VPC endpoint connectivity

**Security:** HTTPS encryption, AWS PrivateLink, VPC endpoint policies, service account access tokens

**Drawbacks:** Requires coordination with Cursor and AWS endpoint service setup.

##### Cloudflare Tunnel

Available for Enterprise customers. Use Cloudflare Tunnel when AWS PrivateLink is not practical or when you need an outbound-only deployment model. Your network runs `cloudflared`, and Cursor provides the tunnel hostname and token.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, Cloudflare Tunnel, service account access tokens

**Drawbacks:** Requires running and maintaining `cloudflared` in your environment.

#### Permissions

The GitHub app requests the following permissions to support Cursor features:

| Permission                         | Purpose                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| **Repository access**              | Clone your code and create working branches                                  |
| **Pull requests**                  | Create PRs and leave review comments                                         |
| **Issues**                         | Track bugs and tasks discovered during reviews                               |
| **Checks and statuses**            | Report on code quality and test results                                      |
| **Actions and workflows**          | Monitor CI/CD pipelines and trigger CI re-runs from pull requests            |
| **Administration**                 | Read branch protection and required check rules to determine PR mergeability |
| **Custom repository roles**        | Determine user access levels so the correct merge and review options appear  |
| **Organization custom properties** | Surface organization-defined repository metadata in filtering                |

All permissions follow the principle of least privilege.

#### Protected Git Scopes

Lock your GitHub organization to your Cursor organization so only your teams can use its repositories with Cloud Agents, automations, and Bugbot. Protecting a scope requires GitHub organization owner or admin access. See [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes).

#### Troubleshooting

##### Agent can't access repository

- Install the GitHub app with repository access
- Check repository permissions for private repos
- Verify your GitHub account permissions

##### Permission denied for pull requests

- Grant the app write access to pull requests
- Check branch protection rules
- Reinstall if the app installation expired

##### App not visible in GitHub settings

- Check if installed at organization level
- Reinstall from [github.com/apps/cursor](https://github.com/apps/cursor)
- Contact support if installation is corrupted

#### Next steps

Once your GitHub integration is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) — automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) — AI agents that run in the cloud on your repositories


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### GitLab

*The GitLab integration connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).*

**Source:** https://cursor.com/docs/integrations/gitlab

The GitLab integration connects your repositories so you can use features like [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md).

#### Setup

##### GitLab.com

Requires Cursor admin access and GitLab maintainer access.

GitLab integration requires a **paid GitLab plan** (Premium or Ultimate). Project access tokens, which are required for this integration, are not available on GitLab Free.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to GitLab (or **Manage Connections** if already connected)
3. Follow the GitLab installation flow
4. Back on the Integrations tab, click **Manage** next to your GitLab connection and select **Sync Repos**
5. Return to the dashboard to configure features on your repositories

[GitLab setup](https://cursor.com/docs-static/images/bugbot/bugbot-gitlab.mp4)

To disconnect your GitLab account, return to the integrations dashboard and click **Disconnect Account**.

##### GitLab Self-Hosted

GitLab integration requires a **paid GitLab plan** (Premium or Ultimate). Project access tokens, which are required for this integration, are not available on GitLab Free.

GitLab Self-Hosted requires a [Teams](https://cursor.com/docs/account/teams/pricing.md) or [Enterprise](https://cursor.com/docs/enterprise.md) plan.

##### Networking

- GitLab self-hosted requires secure inbound access from Cursor and outbound access for webhook notifications.
- You need admin privileges on your GitLab instance to create the application.

###### IP whitelisting (recommended)

Add these IP addresses to your allowlist:

```text
184.73.225.134
3.209.66.12
52.44.113.131
```

For other connection options beyond IP whitelisting, see [Advanced networking](https://cursor.com/docs/integrations/gitlab.md#advanced-networking).

##### Create GitLab application

1. In your GitLab instance, create a new application (Instance level preferred)
2. Set the redirect URI to `https://cursor.com/gitlab-connected`
3. Configure the application:
   - **Trusted**: `true`
   - **Confidential**: `true`
   - **Scopes**: `api` and `write_repository`
4. After creation, you'll receive an **Application ID** and **Secret**

##### Register with Cursor

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations) → **Advanced** → **GitLab Self-Hosted**
2. Enter your GitLab instance **hostname**
3. Paste the **Application ID** and **Secret**
4. Click **Register**
5. Select your GitLab instance from the dropdown
6. Click **Connect** to complete the installation
7. Back on the Integrations tab, click **Manage** next to your GitLab connection and select **Sync Repos**
8. Return to the dashboard to configure features on your repositories

#### Advanced networking

Self-hosted instances support multiple connection methods beyond IP whitelisting.

##### AWS PrivateLink or Cloudflare Tunnel

Available for Enterprise customers. Allow Cursor to access your instance over a private network connection. See [Private Connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) or [contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-private-network) for setup.

**Best for:** Instances behind a firewall on a private network, including AWS-hosted instances and environments that can run `cloudflared`

**Security:** HTTPS encryption, AWS PrivateLink, Cloudflare Tunnel, VPC allowlisting, service account access tokens

**Drawbacks:** Requires coordination with Cursor. Google Private Service Connect is not currently supported.

##### Reverse Proxy Tunnel

Available for Enterprise customers. Run a reverse proxy tunnel on-premises that establishes a long-lived websocket connection to Cursor's servers. Network requests are forwarded through to your instance. Requires no inbound network access. [Contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-on-prem-proxy) for setup.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, service account access tokens

**Drawbacks:** Introduces additional complexity, maintenance requirements, and potential security considerations compared to more direct connection methods

#### Protected Git Scopes

Lock your GitLab group or namespace to your Cursor organization so only your teams can use its repositories with Cloud Agents, automations, and Bugbot. Protecting a scope requires the GitLab Owner role. See [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes).

#### Next steps

Once your GitLab integration is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) — automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) — AI agents that run in the cloud on your repositories


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Azure DevOps

*The Azure DevOps integration connects Azure DevOps Services repositories so Cursor can clone your code, work on branches, and open pull requests from [Cloud Agents](https://cursor.com/docs/cloud-agent.md).*

**Source:** https://cursor.com/docs/integrations/azure-devops

The Azure DevOps integration connects Azure DevOps Services repositories so Cursor can clone your code, work on branches, and open pull requests from [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

The Azure DevOps integration is in public beta. It supports Azure DevOps Services at `dev.azure.com`. Azure DevOps Server is not supported.

#### Supported features

Azure DevOps works with [Cloud Agents](https://cursor.com/docs/cloud-agent.md) only. Cloud Agents can clone your code, work on branches, and open pull requests.

The following features don't support Azure DevOps yet:

- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Bugbot](https://cursor.com/docs/bugbot.md) and Bugbot autofix
- [Security Agents](https://cursor.com/docs/security-agents.md), including Security Reviewer and Vulnerability Scanner

These features work with [GitHub](https://cursor.com/docs/integrations/github.md) today. Azure DevOps support is on the roadmap.

#### Setup

Requires access to the Azure DevOps organizations and repositories you want to use with Cursor.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to Azure DevOps
3. Sign in with the Microsoft account you use for Azure DevOps
4. Review the Microsoft Entra OAuth consent screen and approve access
5. Return to Cursor and select repositories from your Azure DevOps organizations
6. Configure Cloud Agents on the repositories you want Cursor to use

To disconnect your Azure DevOps account, return to the integrations dashboard and click **Disconnect Account**.

#### Repository URLs

Cursor supports Azure DevOps Services repository URLs in this format:

```text
https://dev.azure.com/{organization}/{project}/_git/{repository}
```

Azure DevOps uses an organization, project, and repository hierarchy. Cursor shows repositories as `{project}/{repository}` under the Azure DevOps organization.

If your organization still uses a `*.visualstudio.com` URL, open the repository in Azure DevOps and copy the `dev.azure.com` URL before adding it to Cursor.

#### Permissions

Cursor connects to Azure DevOps through Microsoft Entra OAuth. The connection lets Cursor:

| Access                         | Purpose                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------ |
| **Organizations and projects** | List the Azure DevOps organizations, projects, and repositories you can access |
| **Code repositories**          | Clone repositories and create working branches                                 |
| **Pull requests**              | Open, update, and merge pull requests created by Cloud Agents                  |

#### Troubleshooting

##### I don't see my Azure DevOps repository

- Confirm the repository is hosted on Azure DevOps Services at `dev.azure.com`.
- Confirm the Microsoft account you connected has access to the organization, project, and repository.
- Reconnect Azure DevOps from the integrations dashboard if your Microsoft access changed.

##### Cloud Agent can't open a pull request

- Confirm the selected Azure DevOps repository is connected in Cursor.
- Check that your Azure DevOps account can create branches and pull requests in the target repository.
- Check branch policies if the target branch blocks pull request creation or updates.

##### Repository URL is rejected

Use the `dev.azure.com` repository URL from Azure DevOps. Cursor does not accept Azure DevOps Server URLs for this integration.

#### Next steps

Once your Azure DevOps integration is connected, configure the features that use it:

- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) - AI agents that run in the cloud on your repositories
- [Cloud Agent setup](https://cursor.com/docs/cloud-agent/setup.md) - saved environments, multi-repo setup, secrets, and Dockerfiles


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Bitbucket

*Connect Bitbucket Cloud repositories to [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md). Connect Bitbucket Data Center repositories to Bugbot.*

**Source:** https://cursor.com/docs/integrations/bitbucket

Connect Bitbucket Cloud repositories to [Cloud Agents](https://cursor.com/docs/cloud-agent.md) and [Bugbot](https://cursor.com/docs/bugbot.md). Connect Bitbucket Data Center repositories to Bugbot.

#### Setup

##### Bitbucket Cloud

The Bitbucket Cloud integration is in public beta. It supports repositories on `bitbucket.org`.

Bitbucket Cloud setup has two parts, and each part requires a different role:

- Each developer connects their Bitbucket account so Cursor can clone repositories, push branches, and open pull requests as that user.
- A Bitbucket workspace admin installs the Cursor app so Bugbot and Cloud Agent status comments can appear as Cursor. Linking the installed app to your Cursor team requires a Cursor team admin with access to the Bitbucket workspace.

##### Connect your Bitbucket account

Requires access to the Bitbucket workspace repositories you want to use.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Click **Connect** next to Bitbucket
3. Authorize Cursor in Bitbucket
4. Return to the dashboard and confirm the integration shows **Connected**

[Bitbucket setup](https://cursor.com/docs-static/images/bitbucket/bitbucket-demo.mp4)

Each person who starts Cloud Agents or opens pull requests from Cursor should connect their own Bitbucket account.

##### Install the Cursor app in Bitbucket

A Bitbucket workspace admin must install the Cursor app for the workspace. This gives Cursor a stable app identity for repository events, Bugbot review comments, inline comments, and status updates.

Steps 1 through 4 require a Bitbucket workspace admin. Steps 5 and 6 require a Cursor team admin with access to the Bitbucket workspace. If one person handles the full setup, they need both roles.

1. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
2. Find Bitbucket and open the manage menu
3. Click **Install Cursor app**
4. Install the app in your Bitbucket workspace
5. In Bitbucket workspace settings, under **Forge Apps**, select **Cursor**
6. Click **Connect to Cursor** and choose the Cursor team to link

When the workspace is linked, the dashboard shows the Cursor app installed for that Bitbucket workspace.

Bitbucket can take a few minutes to notify Cursor after app installation. If Cursor cannot find the workspace right away, wait and try the link step again.

##### How Cursor uses Bitbucket Cloud identities

Cursor uses different Bitbucket identities for different actions:

| Action                                                       | Bitbucket identity           |
| ------------------------------------------------------------ | ---------------------------- |
| Bugbot summary comments, inline comments, and build statuses | Cursor app                   |
| Cloud Agent progress comments on pull requests               | Cursor app                   |
| Git clone, branch push, commits, and pull request creation   | The connected Bitbucket user |

Pull requests opened by Cloud Agents are attributed to the person who started the agent. Bugbot output appears from Cursor when the workspace app is installed.

##### Permissions

The Bitbucket Cloud integration asks for permissions needed to support Cloud Agents and Bugbot:

| Permission             | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| **Account**            | Identify the connected Bitbucket user      |
| **Repositories**       | List, clone, and read repository content   |
| **Pull requests**      | Read pull request diffs and metadata       |
| **Pull request write** | Create pull requests and post comments     |
| **Webhooks**           | Receive repository and pull request events |

##### Disconnect Bitbucket Cloud

Disconnecting Bitbucket Cloud has two separate effects:

- **Disconnect account** removes your personal Bitbucket OAuth connection from Cursor.
- **Disconnect Cursor app** unlinks the Bitbucket workspace from your Cursor team. The app can remain installed in Bitbucket until a workspace admin removes it there.

To fully stop app events from the workspace, uninstall the Cursor app from Bitbucket workspace settings.

##### Bitbucket Data Center

Bitbucket Data Center requires a [Teams](https://cursor.com/docs/account/teams/pricing.md) or [Enterprise](https://cursor.com/docs/enterprise.md) plan. It supports Bugbot. Cloud Agents are not supported.

##### Prerequisites

- Cursor team admin access
- A dedicated Bitbucket Data Center service account
- An HTTP access token for the service account
- Repository admin access for the service account on each repository you want to use with Bugbot

The service account reads repositories and pull requests, manages webhooks, and posts Bugbot comments and build statuses.

##### Networking

Cursor needs HTTPS access to your Bitbucket Data Center instance for API requests and Git clones. Your instance also needs outbound HTTPS access to send webhook notifications to Cursor.

###### IP allowlisting (recommended)

Add these Cursor IP addresses to your inbound allowlist:

```text
184.73.225.134
3.209.66.12
52.44.113.131
```

If Cursor should use a load balancer or API hostname that differs from the repository clone hostname, enter it as the external host during registration.

For instances without public inbound access, see [Advanced networking](https://cursor.com/docs/integrations/bitbucket.md#advanced-networking).

##### Register with Cursor

1. Create an HTTP access token for the Bitbucket service account
2. Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations)
3. Open **Advanced**, then select **Bitbucket Data Center**
4. Enter the **Bitbucket Hostname** used in repository clone URLs
5. If API traffic uses a different hostname, enter it as the **External Host**
6. Enter the **Service Account Token**
7. Click **Register**
8. Return to the [Bugbot dashboard](https://cursor.com/dashboard/bugbot) to enable Bugbot on repositories from the instance

Cursor uses the service account identity for Bugbot review comments, inline findings, webhooks, and build statuses.

##### Disconnect Bitbucket Data Center

Go to [Integrations in the dashboard](https://cursor.com/dashboard/integrations), open the Bitbucket Data Center configuration page, and delete the registered instance. Revoke the service account token in Bitbucket Data Center after removing the instance from Cursor.

#### Advanced networking

Bitbucket Data Center supports private connection methods for instances that cannot accept traffic from the public internet.

##### AWS PrivateLink or Cloudflare Tunnel

Available for Enterprise customers. Allow Cursor to access your instance over a private network connection. See [Private Connectivity](https://cursor.com/docs/enterprise/private-connectivity.md) or [contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-private-network) for setup.

**Best for:** Instances behind a firewall, including AWS-hosted instances and environments that can run `cloudflared`

**Security:** HTTPS encryption, AWS PrivateLink, Cloudflare Tunnel, VPC allowlisting, service account access tokens

**Drawbacks:** Requires coordination with Cursor. Google Private Service Connect is not currently supported.

##### Reverse Proxy Tunnel

Available for Enterprise customers. Run a reverse proxy tunnel on-premises that establishes an outbound connection to Cursor. Network requests are forwarded through the tunnel, so the Bitbucket instance does not need public inbound access. [Contact your Cursor representative](https://cursor.com/contact-sales?source=docs-bugbot-on-prem-proxy) for setup.

**Best for:** Environments without inbound network access

**Security:** HTTPS encryption, service account access tokens

**Drawbacks:** Introduces additional complexity, maintenance requirements, and potential security considerations compared to more direct connection methods

#### Troubleshooting

##### Cursor cannot find my Bitbucket workspace

Bitbucket app installation events can take a few minutes to sync. Wait and retry the **Connect to Cursor** step from Bitbucket workspace settings.

##### I installed the Cursor app but cannot link it to my Cursor team

- Confirm you are a Cursor team admin. Installing the app requires a Bitbucket workspace admin, but linking the workspace to a Cursor team requires a Cursor team admin.
- Confirm your Bitbucket user has access to the workspace you are linking.

##### Bugbot comments do not appear as Cursor

Install the Cursor app in the Bitbucket workspace and link it to your Cursor team. A personal Bitbucket connection alone is not enough for Cursor app comments.

##### Cloud Agent cannot access a Bitbucket repository

- Connect your personal Bitbucket account from the integrations dashboard.
- Confirm your Bitbucket user has read-write access to the repository.
- Confirm the repository is on Bitbucket Cloud at `bitbucket.org`.

##### Cursor cannot list my Bitbucket Data Center repositories

- Confirm the service account token is active.
- Confirm the service account can access the repositories.
- Confirm Cursor can reach the instance hostname or configured external host over HTTPS.

##### I cannot enable Bugbot on a Bitbucket Data Center repository

- Confirm you are a Cursor team admin.
- Confirm the registered instance has a service account token.
- Confirm the service account has repository admin access.

#### Next steps

Once Bitbucket is connected, configure the features that use it:

- [Bugbot](https://cursor.com/docs/bugbot.md) - automated PR reviews that catch bugs and security issues
- [Cloud Agents](https://cursor.com/docs/cloud-agent.md) - AI agents for Bitbucket Cloud repositories


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### JetBrains

*Use Cursor's AI agent in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs through the [Agent Client Protocol](https://agentclientprotocol.com/) (ACP).*

**Source:** https://cursor.com/docs/integrations/jetbrains

Use Cursor's AI agent in IntelliJ IDEA, PyCharm, WebStorm, and other JetBrains IDEs through the [Agent Client Protocol](https://agentclientprotocol.com/) (ACP).

ACP lets you stay in your JetBrains IDE while Cursor handles agent-driven development. You get access to frontier models from OpenAI, Anthropic, Google, and Cursor.

#### Prerequisites

- A paid [Cursor plan](https://cursor.com/docs/models-and-pricing.md)
- A JetBrains IDE with the [AI Assistant](https://plugins.jetbrains.com/plugin/22282-ai-assistant) plugin enabled (2025.1+)

#### Get started

##### Open the AI Chat plugin

Open the AI Chat panel in your JetBrains IDE. You can find it in the right sidebar or through **View** > **Tool Windows** > **AI Chat**.

##### Install Cursor from the ACP registry

In the AI Chat panel, open the agent provider list and select **Add Agent from Registry**. Search for **Cursor** and install it.

##### Authenticate

After installing, select Cursor as your agent provider.

##### Start coding

Send a prompt in the AI Chat panel. Cursor's agent reads your project, edits files, runs terminal commands, and creates code directly in your JetBrains IDE.

#### What you get

Cursor ACP in JetBrains IDEs provides many of the same agent capabilities available across other Cursor surfaces.

- **Model selection** — Choose from [frontier models](https://cursor.com/docs/models-and-pricing.md) suited to your task. Different models handle different kinds of work better; switch between them as needed.
- **File editing** — The agent reads and writes files in your project, with changes reflected in your JetBrains editor.
- **Terminal commands** — The agent runs shell commands in the IDE's integrated terminal.

#### How it works

Cursor ACP uses the [Agent Client Protocol](https://agentclientprotocol.com/), an open standard for connecting AI agents to IDEs. Your JetBrains IDE acts as the ACP client, and Cursor's agent acts as the server.

When you send a prompt, the AI Chat plugin forwards it to Cursor's agent through ACP. The agent processes your request, reads your project files, and streams edits and terminal commands back to the IDE.

#### Pricing

Cursor ACP uses the same usage-based pricing as your Cursor subscription. See [pricing](https://cursor.com/docs/models-and-pricing.md) for details.

#### Related

##### ACP reference

Full ACP protocol details, transport, and client examples

##### Models

Available models and their capabilities


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Xcode

*Xcode 26.3+ exposes a built-in [MCP](https://cursor.com/docs/mcp.md) server that gives Cursor direct access to your Xcode projects. Cursor's agent can read and edit files, trigger builds, run tests, capture SwiftUI previews, and search Apple's documentation; all without leaving your editor.*

**Source:** https://cursor.com/docs/integrations/xcode

Xcode 26.3+ exposes a built-in [MCP](https://cursor.com/docs/mcp.md) server that gives Cursor direct access to your Xcode projects. Cursor's agent can read and edit files, trigger builds, run tests, capture SwiftUI previews, and search Apple's documentation; all without leaving your editor.

This works through `xcrun mcpbridge`, a binary Apple ships with Xcode that translates MCP protocol messages into Xcode's internal XPC layer. You configure it once, and Cursor treats Xcode's 20 built-in tools like any other MCP server.

#### Prerequisites

- macOS with Xcode 26.3 or later installed
- A paid [Cursor plan](https://cursor.com/docs/models-and-pricing.md)
- An Xcode project open in Xcode (Xcode must be running)

##### Enable MCP in Xcode

Before Cursor can connect, turn on Xcode's MCP bridge:

##### Open Xcode settings

Go to **Xcode > Settings > Intelligence**.

##### Enable MCP

Under **Model Context Protocol**, toggle **Xcode Tools** on.

#### Set up Cursor

Pick whichever method suits your workflow.

##### Option 1: MCP settings UI

##### Open MCP settings

Go to **Cursor Settings > Features > MCP**.

##### Add the server

Click **Add New MCP Server**. Set the transport to **stdio**, name it `xcode-tools`, and enter `xcrun mcpbridge` as the command.

##### Option 2: `mcp.json`

Add an entry to your [MCP config file](https://cursor.com/docs/mcp.md#configuration-locations):

```json title="~/.cursor/mcp.json"
{
  "mcpServers": {
    "xcode-tools": {
      "command": "xcrun",
      "args": ["mcpbridge"]
    }
  }
}
```

##### Option 3: Cursor CLI

If you use the [Cursor CLI](https://cursor.com/docs/cli/overview.md), register the server from your terminal:

```bash
agent mcp add xcode-tools -- xcrun mcpbridge
```

The CLI shares the same MCP config as the editor, so the server appears in both.

#### Available tools

Xcode exposes 20 MCP tools across five categories:

##### File operations

- **XcodeRead** - Read file contents (up to 600 lines per call, with offset/limit for larger files)
- **XcodeWrite** - Create or overwrite files
- **XcodeUpdate** - Apply targeted edits to existing files
- **XcodeGrep** - Search file contents with regex
- **XcodeGlob** - Find files by pattern
- **XcodeLS** - List directory contents
- **XcodeMakeDir** - Create directories
- **XcodeRM** - Remove files or directories
- **XcodeMV** - Move or rename files

##### Build and test

- **BuildProject** - Build the active scheme
- **GetBuildLog** - Retrieve build logs, filterable by severity, regex, or file glob
- **RunAllTests** - Run the full test suite
- **RunSomeTests** - Run specific test classes or methods
- **GetTestList** - List available tests

##### Diagnostics

- **XcodeListNavigatorIssues** - Show warnings and errors from the Issue Navigator
- **XcodeRefreshCodeIssuesInFile** - Re-check a file for code issues

##### Intelligence

- **RenderPreview** - Capture a screenshot of a SwiftUI preview
- **DocumentationSearch** - Semantic search across Apple's documentation and WWDC transcripts
- **ExecuteSnippet** - Run a Swift code snippet

##### Workspace

- **XcodeListWindows** - List open Xcode windows and tabs

#### Example workflow

A typical Cursor + Xcode workflow looks like this:

1. Open your project in both Cursor and Xcode
2. Ask Cursor's agent to add a feature or fix a bug
3. The agent uses **XcodeRead** and **XcodeGrep** to understand your code
4. It edits files with **XcodeWrite** or **XcodeUpdate**
5. It runs **BuildProject** to check for errors, reads results with **GetBuildLog**
6. It runs tests with **RunSomeTests** to verify the change
7. It captures a SwiftUI preview with **RenderPreview** to confirm the UI

You stay in Cursor the whole time. Xcode handles compilation, testing, and previews in the background.

#### Cursor CLI with Xcode

The [Cursor CLI](https://cursor.com/docs/cli/overview.md) also works with Xcode's MCP tools. This is useful for headless workflows, CI pipelines, or terminal-first developers.

```bash
# Run agent with Xcode tools available
agent "Add unit tests for the NetworkManager class"
```

The agent picks up the `xcode-tools` MCP server from your config and uses the same tools available in the editor.

#### Troubleshooting

##### Cursor can't find the xcode-tools server

Make sure Xcode is running with a project open. The `xcrun mcpbridge` process needs an active Xcode session to communicate with.

##### Tools show errors about missing tabIdentifier

Some Xcode MCP tools need a workspace context. Confirm you have a project or workspace open in Xcode, not an empty window.

##### Build or test tools time out

Large projects take longer to build. Check Xcode's build progress directly. The MCP bridge waits for Xcode's response, so timeouts usually mean the underlying operation is still running.

##### MCP toggle missing in Xcode settings

You need Xcode 26.3 or later. Check your version under **Xcode > About Xcode** and update through the Mac App Store or [Apple Developer downloads](https://developer.apple.com/download/).

##### xcrun: error: unable to find utility "mcpbridge"

Your system is pointed at Command Line Tools instead of the full Xcode installation. Fix this by running:

```bash
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
```

Then confirm the bridge is available:

```bash
xcrun --find mcpbridge
```

This should return a file path, not an error. Once it does, open Xcode with your project, go to **Settings > Intelligence > Model Context Protocol**, and enable **Allow external agents**. Then toggle the Xcode MCP server back on in Cursor settings. You should see a permission dialog in Xcode confirming the connection.

#### Related

##### MCP overview

Complete MCP guide with setup, configuration, and authentication

##### iOS & macOS (Swift)

Swift development workflow with Cursor, Sweetpad, and Xcode Build Server

##### Cursor CLI

Use Cursor's agent from the terminal

##### CLI MCP commands

Manage MCP servers from the command line


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Deeplinks

*Deeplinks allow you to share prompts, commands, and rules with others, enabling collaboration and knowledge sharing across teams and communities.*

**Source:** https://cursor.com/docs/reference/deeplinks

Deeplinks allow you to share prompts, commands, and rules with others, enabling collaboration and knowledge sharing across teams and communities.

Links can also be opened via [cursor.com](https://cursor.com). Append the path and url params to the end of the url, for example: [cursor.com/link/prompt?text=...](https://cursor.com/link/prompt?text=Research+and+find+one+bug+in+this+codebase)

Always review your prompts and commands before sharing to ensure they don't contain sensitive information like API keys, passwords, or proprietary code.

#### Prompts

Share prompts that others can use to get started quickly with specific tasks or workflows. When someone clicks a prompt deeplink, it opens Cursor with the prompt pre-filled in the chat. The user must review and confirm the prompt before it gets executed. Deeplinks never trigger automatic execution.

Research and find one bug in this codebase

##### Playground

##### TypeScript

```typescript
const IS_WEB = false; // Set to true for web format

function generatePromptDeeplink(promptText: string): string {
  const baseUrl = IS_WEB
    ? 'https://cursor.com/link/prompt'
    : 'cursor://anysphere.cursor-deeplink/prompt';
  const url = new URL(baseUrl);
  url.searchParams.set('text', promptText);
  return url.toString();
}

const deeplink = generatePromptDeeplink("Create a React component for user authentication");
console.log(deeplink);
```

##### Python

```python
from urllib.parse import urlencode, urlparse, urlunparse

IS_WEB = False  # Set to True for web format

def generate_prompt_deeplink(prompt_text: str) -> str:
    base_url = "https://cursor.com/link/prompt" if IS_WEB else "cursor://anysphere.cursor-deeplink/prompt"
    params = {"text": prompt_text}
    query_string = urlencode(params)
    return f"{base_url}?{query_string}"

deeplink = generate_prompt_deeplink("Create a React component for user authentication")
print(deeplink)
```

#### Commands

Share commands that others can execute directly in their Cursor environment. Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory. When someone clicks a command deeplink, it opens Cursor and creates a new command with the specified name and content. The user must review and confirm the command before it gets executed.

debug-api

Add console.log statements to debug API responses

##### Playground

##### TypeScript

```typescript
const IS_WEB = false; // Set to true for web format

function generateCommandDeeplink(commandName: string, commandContent: string): string {
  const baseUrl = IS_WEB
    ? 'https://cursor.com/link/command'
    : 'cursor://anysphere.cursor-deeplink/command';
  const url = new URL(baseUrl);
  url.searchParams.set('name', commandName);
  url.searchParams.set('text', commandContent);
  return url.toString();
}

const deeplink = generateCommandDeeplink("debug-api", "Add console.log statements to debug API responses");
console.log(deeplink);
```

##### Python

```python
from urllib.parse import urlencode, urlparse, urlunparse

IS_WEB = False  # Set to True for web format

def generate_command_deeplink(command_name: str, command_content: str) -> str:
    base_url = "https://cursor.com/link/command" if IS_WEB else "cursor://anysphere.cursor-deeplink/command"
    params = {"name": command_name, "text": command_content}
    query_string = urlencode(params)
    return f"{base_url}?{query_string}"

deeplink = generate_command_deeplink("debug-api", "Add console.log statements to debug API responses")
print(deeplink)
```

#### Rules

Share rules that others can add to their Cursor environment. Rule deeplinks allow you to share custom rules defined in your `.cursor/rules` directory. When someone clicks a rule deeplink, it opens Cursor and creates a new rule with the specified name and content. The user must review and confirm the rule before it gets added.

typescript-strict

Always use strict TypeScript types and avoid 'any'

##### Playground

##### TypeScript

```typescript
const IS_WEB = false; // Set to true for web format

function generateRuleDeeplink(ruleName: string, ruleContent: string): string {
  const baseUrl = IS_WEB
    ? 'https://cursor.com/link/rule'
    : 'cursor://anysphere.cursor-deeplink/rule';
  const url = new URL(baseUrl);
  url.searchParams.set('name', ruleName);
  url.searchParams.set('text', ruleContent);
  return url.toString();
}

const deeplink = generateRuleDeeplink("typescript-strict", "Always use strict TypeScript types and avoid 'any'");
console.log(deeplink);
```

##### Python

```python
from urllib.parse import urlencode, urlparse, urlunparse

IS_WEB = False  # Set to True for web format

def generate_rule_deeplink(rule_name: str, rule_content: str) -> str:
    base_url = "https://cursor.com/link/rule" if IS_WEB else "cursor://anysphere.cursor-deeplink/rule"
    params = {"name": rule_name, "text": rule_content}
    query_string = urlencode(params)
    return f"{base_url}?{query_string}"

deeplink = generate_rule_deeplink("typescript-strict", "Always use strict TypeScript types and avoid 'any'")
print(deeplink)
```

#### FAQ

##### What is the maximum length for deeplink URLs?

Deeplink URLs have a maximum length of 8,000 characters. When generating deeplinks programmatically, ensure your content doesn't exceed this limit when URL-encoded. The interactive generators above will show you the current URL length and remaining characters as you type.

##### How do I use deeplinks on the web instead of in the Cursor app?

You can swap the deeplink protocol for web links by changing the base URL from `cursor://anysphere.cursor-deeplink/` to `https://cursor.com/link/`. For example:

```text
cursor://anysphere.cursor-deeplink/prompt?text=Hello%20world
```

```text
https://cursor.com/link/prompt?text=Hello%20world
```

Web links will redirect users to cursor.com where they can open the deeplink in their browser or copy it to use in Cursor.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---

## SDK

### Cursor TypeScript SDK

*The `@cursor/sdk` package lets you call Cursor's agent from your own code. The same agent that runs in the Cursor IDE, CLI, and web app is now scriptable from TypeScript. Run the `/sdk` skill inside Cursor to get started.*

**Source:** https://cursor.com/docs/sdk/typescript

The `@cursor/sdk` package lets you call Cursor's agent from your own code. The same agent that runs in the Cursor IDE, CLI, and web app is now scriptable from TypeScript. Run the `/sdk` skill inside Cursor to get started.

##### Cookbook

End-to-end examples live in the [Cursor
Cookbook](https://github.com/cursor/cookbook): a [SDK
quickstart](https://github.com/cursor/cookbook/tree/main/sdk/quickstart), an
[app-builder prototyping
tool](https://github.com/cursor/cookbook/tree/main/sdk/app-builder), a [kanban
board for cloud
agents](https://github.com/cursor/cookbook/tree/main/sdk/agent-kanban), and a
[coding-agent
CLI](https://github.com/cursor/cookbook/tree/main/sdk/coding-agent-cli). Good
starting points for CI auto-fix bots, bug triage workers, code-review passes,
embedded in-product agents, and orchestrators.

#### Overview

The SDK wraps local and cloud runtimes behind one interface. You write the same code regardless of where the agent runs.

| Runtime                   | What it does                                                           | When to use                                                                                                                |
| :------------------------ | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Local**                 | Runs the agent loop inline in your Node process. Files come from disk. | Dev scripts and CI checks against a working tree.                                                                          |
| **Cloud (Cursor-hosted)** | Runs in an isolated VM with your repo cloned in. Cursor runs the VMs.  | When the caller doesn't have the repo, you want many agents in parallel, or runs need to survive the caller disconnecting. |

##### Local means local agent loop, not local model

"Local" describes where the agent loop and filesystem access run, not where
the model runs. All inference goes through Cursor's hosted models in both
modes. Local mode keeps your files on your machine; cloud mode runs in a
Cursor environment. The model itself is hosted in either case.

Runtime is picked by which key you pass to `Agent.create()` (`local` or `cloud`). Use the same `CURSOR_API_KEY` for either.

For the REST API, see the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md).

#### Authentication

Set `CURSOR_API_KEY` (or pass `apiKey`) before creating an agent.

The SDK accepts user API keys and service account API keys for both local and cloud runs. Team Admin API keys are not yet supported.

- **User API key** from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api)
- **Service account API key** from [Team settings](https://cursor.com/dashboard/team-settings). See [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)

```bash
export CURSOR_API_KEY="your-key"
```

#### Usage and billing

SDK runs follow the same pricing, request pools, and Privacy Mode rules as runs from the IDE and Cloud Agents. Spend shows up in your team's [usage dashboard](https://cursor.com/dashboard/usage) under the SDK tag.

Service account API keys bill to the team that owns the service account. User API keys bill to that user's plan.

To read per-run token counts in code, see [Token usage](https://cursor.com/docs/sdk/typescript.md#token-usage).

#### Core concepts

| Concept        | Description                                                                                                        |
| :------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Agent**      | Durable container that holds conversation state, workspace config, and settings. Survives across multiple prompts. |
| **Run**        | One prompt submission. Owns its own stream, status, result, and cancellation.                                      |
| **SDKMessage** | Normalized stream events emitted during a run. Same shape across all runtimes.                                     |

#### Installation

```bash
npm install @cursor/sdk
```

The package name starts with `@`. The bare `cursor/sdk` doesn't exist on npm.

##### Runtime support

The SDK requires Node.js 22.13 or later. It ships per-platform `@cursor/sdk-<os>-<arch>` binaries for sandboxing and ripgrep, so it is a Node-first package.

Importing `@cursor/sdk` does not eagerly load the local agent stack. The local executor loads on the first local `acquire`, so cloud-only and type-only consumers don't pay the local import cost. The first local agent in a process pays a one-time import, then the module stays cached.

The current package, `@cursor/sdk@1.0.23`, publishes self-contained `.d.ts` files, so types resolve without pulling in unpublished workspace packages. After upgrading, re-run your typecheck. Stream types such as `TurnEndedUpdate` resolve to real types instead of `any`.

#### Quick start

The fastest way in: a local agent against your current working tree, streaming events as they come in. Cloud setup is in [Creating agents](https://cursor.com/docs/sdk/typescript.md#creating-agents) below.

```typescript
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: { cwd: process.cwd() },
});

const run = await agent.send("Summarize what this repository does");

for await (const event of run.stream()) {
  console.log(event);
}
```

Each event is a discriminated `SDKMessage`. [Streaming](https://cursor.com/docs/sdk/typescript.md#streaming) shows how to extract assistant text, handle tool calls, and clean up with `await using`. For a one-shot prompt (create, run, dispose), see [Agent.prompt()](https://cursor.com/docs/sdk/typescript.md#agentprompt).

##### Quickstart approves tool calls automatically

The default local agent runs tool calls (shell, edit, write, etc.) without
asking for approval; there's no human-in-the-loop prompt in headless mode. To
gate tool calls, configure [hooks](https://cursor.com/docs/sdk/typescript.md#hooks) (such as `beforeShellExecution` or
`preToolUse`) or run with [`local.sandboxOptions.enabled:
  true`](https://cursor.com/docs/sdk/typescript.md#sandbox-options).

#### Creating agents

```typescript
function Agent.create(options: AgentOptions): Promise<SDKAgent>;
```

`Agent.create()` validates options and returns a handle immediately. Pass either `local` or `cloud` to pick a runtime.

```typescript
// Local agent
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: { cwd: "/path/to/repo" },
});

// Cloud agent
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo", startingRef: "main" }],
    autoCreatePR: true,
  },
});
```

`agent.agentId` is populated immediately. Local agents get an `agent-<uuid>` ID; cloud agents get a `bc-<uuid>` ID.

Cloud agents started by the SDK are filtered out of the default agent list. To
view them in Cursor Web or a Cursor window, click **Filter > Source > SDK**.

##### Session environment variables

For cloud agents, pass `cloud.envVars` when a run needs short-lived credentials or other values that should live only with that agent.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo" }],
    envVars: {
      STAGING_API_TOKEN: process.env.STAGING_API_TOKEN!,
    },
  },
});
```

These values are encrypted at rest, injected into the cloud agent's shell, and deleted with the agent. `envVars` can't be used with a caller-supplied `agentId`; omit `agentId` and read the server-minted ID from `agent.agentId`. Variable names can't start with `CURSOR_`.

For values that should only exist during a single run, pass them on `agent.send()` instead. See [Per-run environment variables](https://cursor.com/docs/sdk/typescript.md#per-run-environment-variables).

##### Model parameters

Use `model.params` to pass per-model options such as reasoning effort. Parameter ids and values vary by model. Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/typescript.md#cursormodelslist) to discover supported parameters and preset variants for your account.

On legacy request-based plans, Cursor enables [Max Mode](https://cursor.com/help/ai-features/max-mode.md) automatically when the selected model requires it.

##### Composer 2 reroutes to Composer 2.5

Composer 2 is retired. SDK requests that still pass `composer-2` or
`composer-2-fast` are rerouted to Composer 2.5 at auth time, so existing
scripts keep working. If you relied on the `composer-2-fast` variant, confirm
the fast behavior still matches what you expect.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: {
    id: "composer-2.5",
    params: [{ id: "fast", value: "true" }],
  },
  local: { cwd: process.cwd() },
});
```

##### SDKAgent

The handle returned by `Agent.create()` and `Agent.resume()`.

```typescript
interface SDKAgent {
  readonly agentId: string;
  readonly model: ModelSelection | undefined;

  send(message: string | SDKUserMessage, options?: SendOptions): Promise<Run>;
  close(): void;
  reload(): Promise<void>;
  [Symbol.asyncDispose](): Promise<void>;

  listArtifacts(): Promise<SDKArtifact[]>;
  downloadArtifact(path: string): Promise<Buffer>;
}
```

| Member                  | Description                                                                                                                                                                  |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agentId`               | Stable agent identifier. `agent-<uuid>` for local, `bc-<uuid>` for cloud.                                                                                                    |
| `model`                 | Current model selection. Updates after every successful `send({ model })`. `undefined` until something sets it (including resumed agents whose caller did not pass `model`). |
| `send`                  | Start a new run with the given prompt. Returns a `Run` handle.                                                                                                               |
| `close`                 | Begin disposal without awaiting. Fire-and-forget.                                                                                                                            |
| `reload`                | Re-read filesystem config (hooks, project MCP, subagents) without disposing.                                                                                                 |
| `[Symbol.asyncDispose]` | Async disposal. Pair with `await using` for automatic cleanup.                                                                                                               |
| `listArtifacts`         | List files produced by the agent (cloud only; local returns empty).                                                                                                          |
| `downloadArtifact`      | Download a file by path (cloud only; local throws).                                                                                                                          |

##### Agent.prompt()

```typescript
function Agent.prompt(message: string, options?: AgentOptions): Promise<RunResult>;
```

One-shot convenience: creates an agent, sends a single prompt, waits for the run to finish, and disposes.

```typescript
const result = await Agent.prompt("What does the auth middleware do?", {
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: { cwd: process.cwd() },
});
```

#### Sending messages

Each `agent.send()` returns a `Run`. The agent retains conversation context across runs; the run is the unit of work for one prompt.

##### Run

```typescript
type RunStatus = "running" | "finished" | "error" | "cancelled";
type RunOperation = "stream" | "wait" | "cancel" | "conversation";

interface Run {
  readonly id: string;
  readonly requestId?: string;
  readonly agentId: string;
  readonly status: RunStatus;
  readonly result?: string;
  readonly error?: RunError;
  readonly model?: ModelSelection;
  readonly durationMs?: number;
  readonly usage?: TokenUsage;
  readonly git?: RunGitInfo;
  readonly createdAt?: number;

  stream(): AsyncGenerator<SDKMessage, void>;
  wait(): Promise<RunResult>;
  cancel(): Promise<void>;
  conversation(): Promise<ConversationTurn[]>;

  supports(operation: RunOperation): boolean;
  unsupportedReason(operation: RunOperation): string | undefined;
  onDidChangeStatus(listener: (status: RunStatus) => void): () => void;
}

interface RunGitInfo {
  branches: Array<{ repoUrl: string; branch?: string; prUrl?: string }>;
}

interface RunError {
  message: string;
  code?: string;
}

interface TokenUsage {
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  cacheWriteTokens: number;
  totalTokens: number;
  reasoningTokens?: number;
}

interface RunResult {
  id: string;
  requestId?: string;
  status: "finished" | "error" | "cancelled";
  result?: string;
  error?: RunError;
  model?: ModelSelection;
  durationMs?: number;
  usage?: TokenUsage;
  git?: RunGitInfo;
}
```

##### Streaming

```typescript
const run = await agent.send("Find the bug in src/auth.ts");

for await (const event of run.stream()) {
  switch (event.type) {
    case "assistant":
      for (const block of event.message.content) {
        if (block.type === "text") process.stdout.write(block.text);
      }
      break;
    case "thinking":
      process.stdout.write(event.text);
      break;
    case "tool_call":
      console.log(`[tool] ${event.name}: ${event.status}`);
      break;
    case "status":
      console.log(`[status] ${event.status}`);
      break;
  }
}

// Follow-up on the same agent. Conversation state from the previous
// run is loaded automatically.
const run2 = await agent.send("Fix it and add a regression test");
await run2.wait();
```

To send images alongside text:

```typescript
const run = await agent.send({
  text: "What's in this screenshot?",
  images: [{ data: base64Png, mimeType: "image/png" }],
});
```

##### Waiting without streaming

```typescript
const result = await run.wait();

console.log(result.status);      // "finished" | "error" | "cancelled"
console.log(result.result);      // final assistant text, if any
console.log(result.error);       // { message, code? } when the run failed
console.log(result.model);       // resolved ModelSelection used for this run
console.log(result.durationMs);
console.log(result.usage);       // cumulative TokenUsage, or undefined if unavailable
console.log(result.git);         // { branches: [{ repoUrl, branch?, prUrl? }] } on cloud
```

The final assistant text is on `result.result` as a string. There's no `text`, `message`, `messages`, or `content` field to dig through. If you need the per-step transcript instead, call `run.conversation()` for a structured `ConversationTurn[]` view:

```typescript
const result = await run.wait();
const finalText = result.result ?? "";

const turns = await run.conversation();
const lastAssistant = turns
  .flatMap((t) => (t.type === "agentConversationTurn" ? t.turn.steps : []))
  .filter((s) => s.type === "assistantMessage")
  .at(-1);

console.log(lastAssistant?.message.text);
```

##### Cancelling a run

```typescript
await run.cancel();
```

Cancels the run. The status moves to `"cancelled"`, the live stream aborts, in-flight tool calls stop, and `run.wait()` resolves with `status: "cancelled"`. Partial output (assistant text written so far) stays on the Run object.

Cancel is supported on running local and cloud runs and is a no-op if the run already finished.

##### Reading run state

```typescript
console.log(run.status);  // "running" | "finished" | "error" | "cancelled"

const stop = run.onDidChangeStatus((status) => {
  console.log(`status changed to ${status}`);
});
// Call `stop()` to remove the listener.

// Structured per-turn view of the conversation accumulated in this run
const turns = await run.conversation();
```

`run.conversation()` returns the run's `ConversationTurn[]` (an agent turn with steps, or a shell turn with command and output). Use it to render or persist the run's structured history without subscribing to the live stream.

##### Token usage

Runs report token usage when the runtime provides it. Read the cumulative total from `run.usage` while the run is in flight, or from `result.usage` after `run.wait()`. Both hold a `TokenUsage` summed across every turn that reported usage, and both are `undefined` when no turn did (a cancelled run that never finished a turn, or a runtime that doesn't surface usage).

```typescript
interface TokenUsage {
  inputTokens: number;
  outputTokens: number;
  cacheReadTokens: number;
  cacheWriteTokens: number;
  totalTokens: number;
  reasoningTokens?: number;
}
```

| Field              | Description                                                                                       |
| :----------------- | :------------------------------------------------------------------------------------------------ |
| `inputTokens`      | Prompt tokens sent to the model.                                                                  |
| `outputTokens`     | Tokens generated by the model.                                                                    |
| `cacheReadTokens`  | Tokens served from the prompt cache.                                                              |
| `cacheWriteTokens` | Tokens written to the prompt cache.                                                               |
| `totalTokens`      | `inputTokens + outputTokens + cacheReadTokens + cacheWriteTokens`. Excludes `reasoningTokens`.    |
| `reasoningTokens`  | Reasoning tokens, a subset of `outputTokens`. Omitted when the model or runtime didn't report it. |

```typescript
const result = await run.wait();

if (result.usage) {
  console.log(`total: ${result.usage.totalTokens}`);
  console.log(`in: ${result.usage.inputTokens}, out: ${result.usage.outputTokens}`);
  console.log(
    `cache read/write: ${result.usage.cacheReadTokens}/${result.usage.cacheWriteTokens}`
  );
} else {
  console.log("no usage reported for this run");
}
```

`reasoningTokens` is already counted inside `outputTokens`, so `totalTokens` leaves it out to avoid double-counting.

For per-turn numbers as they stream, handle the `usage` [stream event](https://cursor.com/docs/sdk/typescript.md#stream-events) (`SDKUsageMessage`). It fires once at the end of each turn that reported usage and carries that turn's `TokenUsage`. `run.usage` and `result.usage` stay cumulative across the run.

```typescript
for await (const event of run.stream()) {
  if (event.type === "usage") {
    console.log(`turn used ${event.usage.totalTokens} tokens`);
  }
}
```

##### Run correlation with requestId

Every `agent.send()` gets a platform-generated UUID, exposed as `requestId` on both the `Run` and the `RunResult`. Use it to tie a script or CI run to backend logs, analytics, and support threads instead of guessing from `agentId` alone.

```typescript
const run = await agent.send("Audit the auth middleware");
console.log(run.requestId); // e.g. "6e0d261c-86a2-4383-89f0-9162c1c10662"

const result = await run.wait();
logger.info({ requestId: result.requestId }, "run finished");
```

`requestId` persists with the run, so it round-trips through the in-memory, SQLite, and JSONL [local stores](https://cursor.com/docs/sdk/typescript.md#local-agent-stores) and is set on cloud runs when the backend returns one. Log it alongside `error.requestId` from [errors](https://cursor.com/docs/sdk/typescript.md#errors) so a single identifier spans both success and failure paths.

##### Per-run model override

The `model` you pass to `agent.send()` overrides the agent's selection for that run, then becomes sticky: subsequent sends without an override continue to use the new model. To switch back, pass another `model` override or read the current selection from `agent.model`.

```typescript
const run = await agent.send("Plan the refactor", {
  model: { id: "composer-2.5", params: [{ id: "fast", value: "true" }] },
});

console.log(agent.model);  // updated to the override after the send succeeds
```

`run.model` and `result.model` reflect the selection that this specific run actually used and are immutable once the run starts.

##### Per-run environment variables

Cloud agents can also take environment variables for a single run. Pass `cloud.envVars` on `agent.send()` and the values are injected into the agent's shell for that run only — when the run finishes, they're removed from the VM and the next run doesn't see them. This is the right shape for credentials that rotate between turns, like a short-lived deploy token you mint right before asking the agent to use it.

```typescript
const run = await agent.send("Deploy the preview environment", {
  cloud: {
    envVars: {
      DEPLOY_TOKEN: await mintShortLivedToken(),
    },
  },
});
```

If a run-scoped variable has the same name as an agent-scoped one from [`cloud.envVars` on `Agent.create()`](https://cursor.com/docs/sdk/typescript.md#session-environment-variables), the run-scoped value wins for that run, then the agent-scoped value comes back on the next run.

Per-run variables work on the first send too. The SDK passes them along with agent creation, scoped to the initial run, so they aren't persisted on the agent. Like agent-scoped variables, they're encrypted at rest and names can't start with `CURSOR_`.

Per-run environment variables are cloud agents only, and they aren't available for agents running against public repositories. For local agents, the agent process inherits your own environment, so set variables on the process before calling `send()`.

##### Conversation mode

Pass `mode: "plan"` or `mode: "agent"` to control whether a run explores and plans first or implements changes directly. See [Plan mode](https://cursor.com/help/ai-features/plan-mode.md) for what plan mode does in the product.

Set `mode` on `Agent.create()` to seed the first run. On follow-up `agent.send()` calls, omit `mode` to keep the conversation's current mode, or pass `mode` to switch for that run only.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  mode: "plan",
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo" }],
  },
});

await (await agent.send("Design the auth refactor")).wait();
await (await agent.send("Looks good, start building", { mode: "agent" })).wait();
```

##### Streaming raw deltas

`run.stream()` yields normalized `SDKMessage` events. For lower-level updates (per-token text, tool-call args streaming in, thinking deltas, step boundaries), pass `onDelta` and `onStep` callbacks to `send()`:

```typescript
const run = await agent.send("Refactor the utils module", {
  onDelta: ({ update }) => {
    if (update.type === "text-delta") process.stdout.write(update.text);
    if (update.type === "thinking-delta") process.stdout.write(update.text);
  },
  onStep: ({ step }) => {
    console.log(`[step] ${step.type}`);
  },
});
```

The callbacks are awaited before the next update is processed, so you can apply backpressure. `InteractionUpdate` covers `text-delta`, `thinking-delta`, `thinking-completed`, `tool-call-started`, `tool-call-completed`, `partial-tool-call`, `token-delta`, `step-started`, `step-completed`, `turn-ended`, and a handful of summary and shell-output deltas.

##### Per-send options

| Property            | Type                                          | Description                                                                                                                                                                                                                                       |
| :------------------ | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`             | `ModelSelection`                              | Per-send model override. If omitted, uses `agent.model`. Sticky: a successful send updates `agent.model`.                                                                                                                                         |
| `mode`              | `"agent" \| "plan"`                           | Per-send conversation mode override. If omitted on follow-ups, keeps the conversation's current mode.                                                                                                                                             |
| `mcpServers`        | `Record<string, McpServerConfig>`             | Inline MCP server definitions. Fully replaces creation-time servers for this run.                                                                                                                                                                 |
| `onStep`            | `(args: { step }) => void \| Promise<void>`   | Callback after each completed conversation step (text, thinking, or tool batch).                                                                                                                                                                  |
| `onDelta`           | `(args: { update }) => void \| Promise<void>` | Callback per raw `InteractionUpdate`.                                                                                                                                                                                                             |
| `idempotencyKey`    | `string`                                      | Optional client-generated idempotency key for the send.                                                                                                                                                                                           |
| `cloud.envVars`     | `Record<string, string>`                      | Cloud agents only. [Per-run environment variables](https://cursor.com/docs/sdk/typescript.md#per-run-environment-variables) injected for this run and removed when it finishes. Overrides agent-scoped `cloud.envVars` by name for this run only. |
| `local.force`       | `boolean`                                     | Local agents only. Defaults to `false`. Expire a stuck active run before starting this message. Cloud returns `409 agent_busy` server-side, so no equivalent is needed.                                                                           |
| `local.customTools` | `Record<string, SDKCustomTool>`               | Local agents only. [Custom tools](https://cursor.com/docs/sdk/typescript.md#custom-tools) for this run. Replaces the agent's creation-time `local.customTools` for that run.                                                                      |

***

The next three sections are detailed reference for `SDKMessage`, `InteractionUpdate`, and `ConversationTurn`. Skim or skip on a first read; [Resuming agents](https://cursor.com/docs/sdk/typescript.md#resuming-agents) picks up the narrative.

#### Stream events

Events from `run.stream()`. Discriminate on `type`. All events include `agent_id` and `run_id`.

```typescript
type SDKMessage =
  | SDKSystemMessage
  | SDKUserMessageEvent
  | SDKAssistantMessage
  | SDKThinkingMessage
  | SDKToolUseMessage
  | SDKStatusMessage
  | SDKTaskMessage
  | SDKRequestMessage
  | SDKUsageMessage;
```

| `type`        | Description                                                                                      | Key fields                                                                      |
| :------------ | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| `"system"`    | Init metadata. Emitted once at the start of a run.                                               | `subtype?` (`"init"`), `model?`, `tools?`                                       |
| `"user"`      | Echo of the user prompt for this run.                                                            | `message.content: TextBlock[]`                                                  |
| `"assistant"` | Model text output.                                                                               | `message.content: (TextBlock \| ToolUseBlock)[]`                                |
| `"thinking"`  | Reasoning content.                                                                               | `text`, `thinking_duration_ms?`                                                 |
| `"tool_call"` | Tool invocation lifecycle. Emitted at start with `args`, then again on completion with `result`. | `call_id`, `name`, `status`, `args?`, `result?`, `truncated?`                   |
| `"status"`    | Cloud run lifecycle transitions.                                                                 | `status`, `message?`                                                            |
| `"task"`      | Task-level milestones and summaries.                                                             | `status?`, `text?`                                                              |
| `"request"`   | Awaiting user input or approval.                                                                 | `request_id`                                                                    |
| `"usage"`     | Per-turn token usage, emitted once at turn end when the runtime reported it.                     | `usage` ([`TokenUsage`](https://cursor.com/docs/sdk/typescript.md#token-usage)) |

Result data (final text, model, duration, cumulative token usage, git metadata) lives on the `Run` object after the stream completes. Use `run.wait()` to read it.

> **Tool call schema is not stable.** The `args` and `result` payloads on `tool_call` events reflect each tool's internal shape and can change as tools evolve. Tool names can also be renamed or replaced. Treat `args` and `result` as `unknown` and parse defensively. The event envelope (`type`, `call_id`, `name`, `status`) is stable.

##### Message types

```typescript
interface SDKSystemMessage {
  type: "system";
  subtype?: "init";
  agent_id: string;
  run_id: string;
  model?: ModelSelection;
  tools?: string[];
}

interface SDKUserMessageEvent {
  type: "user";
  agent_id: string;
  run_id: string;
  message: { role: "user"; content: TextBlock[] };
}

interface SDKAssistantMessage {
  type: "assistant";
  agent_id: string;
  run_id: string;
  message: {
    role: "assistant";
    content: Array<TextBlock | ToolUseBlock>;
  };
}

interface SDKThinkingMessage {
  type: "thinking";
  agent_id: string;
  run_id: string;
  text: string;
  thinking_duration_ms?: number;
}

interface SDKToolUseMessage {
  type: "tool_call";
  agent_id: string;
  run_id: string;
  call_id: string;
  name: string;
  status: "running" | "completed" | "error";
  args?: unknown;
  result?: unknown;
  truncated?: { args?: boolean; result?: boolean };
}

interface SDKStatusMessage {
  type: "status";
  agent_id: string;
  run_id: string;
  status: "CREATING" | "RUNNING" | "FINISHED" | "ERROR" | "CANCELLED" | "EXPIRED";
  message?: string;
}

interface SDKTaskMessage {
  type: "task";
  agent_id: string;
  run_id: string;
  status?: string;
  text?: string;
}

interface SDKRequestMessage {
  type: "request";
  agent_id: string;
  run_id: string;
  request_id: string;
}

interface SDKUsageMessage {
  type: "usage";
  agent_id: string;
  run_id: string;
  usage: TokenUsage;
}

interface TextBlock {
  type: "text";
  text: string;
}

interface ToolUseBlock {
  type: "tool_use";
  id: string;
  name: string;
  input: unknown;
}
```

`SDKToolUseMessage` is emitted twice for most tool calls: first with `status: "running"` and `args` populated, then again on completion with `status: "completed"` (or `"error"`) and `result` populated. `truncated` flags whether the SDK truncated `args` or `result` because the payload was too large.

`SDKStatusMessage` covers cloud-side lifecycle transitions. `CREATING` covers VM provisioning and repo cloning; `RUNNING` is the agent doing work; the rest are terminal.

`SDKUsageMessage` is emitted once at the end of each turn that reported token usage, carrying that turn's [`TokenUsage`](https://cursor.com/docs/sdk/typescript.md#token-usage). The cumulative total across turns stays on `run.usage` and `result.usage`. See [Token usage](https://cursor.com/docs/sdk/typescript.md#token-usage).

#### Interaction updates

`InteractionUpdate` is the raw delta type passed to the `onDelta` callback on `agent.send()`. Updates are finer-grained than `SDKMessage` events: text streams in token-by-token, tool calls report partial state as args accumulate, thinking arrives as it happens.

```typescript
type InteractionUpdate =
  | TextDeltaUpdate
  | ThinkingDeltaUpdate
  | ThinkingCompletedUpdate
  | ToolCallStartedUpdate
  | ToolCallCompletedUpdate
  | PartialToolCallUpdate
  | TokenDeltaUpdate
  | StepStartedUpdate
  | StepCompletedUpdate
  | TurnEndedUpdate
  | UserMessageAppendedUpdate
  | SummaryUpdate
  | SummaryStartedUpdate
  | SummaryCompletedUpdate
  | ShellOutputDeltaUpdate;
```

##### Update types

```typescript
interface TextDeltaUpdate {
  type: "text-delta";
  text: string;
}

interface ThinkingDeltaUpdate {
  type: "thinking-delta";
  text: string;
}

interface ThinkingCompletedUpdate {
  type: "thinking-completed";
  thinkingDurationMs: number;
}

interface ToolCallStartedUpdate {
  type: "tool-call-started";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface PartialToolCallUpdate {
  type: "partial-tool-call";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface ToolCallCompletedUpdate {
  type: "tool-call-completed";
  callId: string;
  toolCall: ToolCall;
  modelCallId: string;
}

interface TokenDeltaUpdate {
  type: "token-delta";
  tokens: number;
}

interface StepStartedUpdate {
  type: "step-started";
  stepId: number;
}

interface StepCompletedUpdate {
  type: "step-completed";
  stepId: number;
  stepDurationMs: number;
}

interface TurnEndedUpdate {
  type: "turn-ended";
  usage?: {
    inputTokens: number;
    outputTokens: number;
    cacheReadTokens: number;
    cacheWriteTokens: number;
    reasoningTokens?: number;
  };
}

interface UserMessageAppendedUpdate {
  type: "user-message-appended";
  userMessage: UserMessage;
}

interface SummaryUpdate {
  type: "summary";
  summary: string;
}

interface SummaryStartedUpdate {
  type: "summary-started";
}

interface SummaryCompletedUpdate {
  type: "summary-completed";
}

interface ShellOutputDeltaUpdate {
  type: "shell-output-delta";
  event: Record<string, unknown>;
}
```

`PartialToolCallUpdate` is emitted as the model streams arguments into a tool call before it commits. The same stability disclaimer that applies to `SDKToolUseMessage.args` applies here.

#### Conversation types

The structured per-turn view of a run, returned by `run.conversation()` and used in the `onStep` callback's argument.

```typescript
type ConversationTurn =
  | { type: "agentConversationTurn"; turn: AgentConversationTurn }
  | { type: "shellConversationTurn"; turn: ShellConversationTurn };

interface AgentConversationTurn {
  userMessage?: UserMessage;
  steps: ConversationStep[];
}

interface ShellConversationTurn {
  shellCommand?: ShellCommand;
  shellOutput?: ShellOutput;
}

type ConversationStep =
  | { type: "assistantMessage"; message: AssistantMessage }
  | { type: "toolCall"; message: ToolCall }
  | { type: "thinkingMessage"; message: ThinkingMessage };

interface AssistantMessage {
  text: string;
}

interface ThinkingMessage {
  text: string;
  thinkingDurationMs?: number;
}

interface UserMessage {
  text: string;
}

interface ShellCommand {
  command: string;
  workingDirectory?: string;
}

interface ShellOutput {
  stdout: string;
  stderr: string;
  exitCode: number;
}
```

`ToolCall` is a discriminated union over every built-in tool (shell, edit, read, write, glob, grep, ls, semSearch, mcp, task, and others). Its shape is internal-facing; see the [stability note](https://cursor.com/docs/sdk/typescript.md#stream-events) under Stream events.

#### Resuming agents

```typescript
function Agent.resume(agentId: string, options?: Partial<AgentOptions>): Promise<SDKAgent>;
```

Use `Agent.resume()` to reattach to an existing agent by ID. Common flows: reconnecting to a long-running cloud agent that was kicked off earlier, or continuing a conversation after the local process restarted. Runtime is auto-detected from the ID prefix (`bc-` is cloud, anything else is local).

```typescript
await using agent = await Agent.resume("bc-abc123", {
  apiKey: process.env.CURSOR_API_KEY!,
});

const run = await agent.send("Also update the changelog");
await run.wait();
```

`agent.model` is `undefined` on resume unless you pass `model` again. Inline `mcpServers` are not persisted across resume — they often carry secrets and live in memory only. Pass them again on resume, or use file-based MCP config (`.cursor/mcp.json` + `local.settingSources`) for servers that should survive.

#### Inspecting agents and runs

List, fetch, and reload past agents. List endpoints return `{ items, nextCursor? }` for cursor-based pagination.

##### Agent.list()

```typescript
function Agent.list(options?: ListAgentsOptions): Promise<ListResult<SDKAgentInfo>>;

type ListAgentsOptions = {
  limit?: number;
  cursor?: string;
} & (
  | { runtime?: undefined }
  | { runtime: "local"; cwd?: string; store?: LocalAgentStore }
  | {
      runtime: "cloud";
      prUrl?: string;
      includeArchived?: boolean;
      apiKey?: string;
    }
);
```

```typescript
const { items, nextCursor } = await Agent.list({
  runtime: "local",
  cwd: process.cwd(),
});
```

##### Agent.get()

```typescript
function Agent.get(agentId: string, options?: GetAgentOptions): Promise<SDKAgentInfo>;

interface GetAgentOptions {
  cwd?: string;       // local routing
  apiKey?: string;    // cloud routing
  store?: LocalAgentStore;
}
```

Runtime is auto-detected from the agent ID prefix (`bc-` → cloud, otherwise local).

##### Agent.listRuns()

```typescript
function Agent.listRuns(agentId: string, options?: ListRunsOptions): Promise<ListResult<Run>>;

type ListRunsOptions = {
  limit?: number;
  cursor?: string;
} & (
  | { runtime?: "local"; cwd?: string; store?: LocalAgentStore }
  | { runtime: "cloud"; apiKey?: string }
);
```

##### Agent.getRun()

```typescript
function Agent.getRun(runId: string, options?: GetRunOptions): Promise<Run>;

type GetRunOptions =
  | { runtime?: "local"; cwd?: string; store?: LocalAgentStore }
  | { runtime: "cloud"; agentId: string; apiKey?: string };
```

Cloud `getRun` requires the parent `agentId`.

##### Agent.cancelRun()

```typescript
function Agent.cancelRun(runId: string, options?: GetRunOptions): Promise<void>;
```

Cancels a run when you have its ID but do not have a `Run` handle.

##### Agent.messages.list()

```typescript
Agent.messages.list(
  agentId: string,
  options?: GetAgentMessagesOptions
): Promise<AgentMessage[]>;

interface GetAgentMessagesOptions {
  limit?: number;
  offset?: number;
  runtime?: "local";
  cwd?: string;
  store?: LocalAgentStore;
}
```

Returns the stored user and assistant messages for a local agent.

##### Cloud agent lifecycle

Cloud agents stay in your team's workspace until you archive or delete them. `Agent.list({ runtime: "cloud" })` hides archived agents by default; pass `includeArchived: true` to see them. Filter by `prUrl` to find the agent that opened a specific pull request.

```typescript
function Agent.archive(agentId: string, options?: AgentOperationOptions): Promise<void>;
function Agent.unarchive(agentId: string, options?: AgentOperationOptions): Promise<void>;
function Agent.delete(agentId: string, options?: AgentOperationOptions): Promise<void>;

interface AgentOperationOptions {
  cwd?: string;
  apiKey?: string;
  store?: LocalAgentStore;
}
```

```typescript
await Agent.archive(agentId);     // soft-delete; transcript stays readable
await Agent.unarchive(agentId);   // restore an archived agent
await Agent.delete(agentId);      // permanent; subsequent reads return 404
```

##### SDKAgentInfo

The metadata shape returned by `Agent.list()` and `Agent.get()`.

```typescript
type SDKAgentInfo = {
  agentId: string;
  name: string;
  summary: string;
  lastModified: number;
  status?: "running" | "finished" | "error";
  createdAt?: number;
  archived?: boolean;
} & (
  | { runtime?: undefined }
  | { runtime: "local"; cwd?: string }
  | {
      runtime: "cloud";
      env?: { type: "cloud" | "pool" | "machine"; name?: string };
      repos?: string[];
    }
);
```

#### The Cursor namespace

Account-level reads, catalog reads, and process-wide SDK configuration. The read methods take an optional `{ apiKey }` and otherwise fall back to `CURSOR_API_KEY`.

##### Cursor.configure()

```typescript
function Cursor.configure(options: CursorConfigureOptions): void;

interface CursorConfigureOptions {
  local?: {
    store?: LocalAgentStore | null;
    useHttp1ForAgent?: boolean | null;
  };
}
```

Set defaults for local agents that apply to later `Agent.*` calls. Fields on an individual call override these values; pass `null` to clear a previous default.

| Option                   | Description                                                                                                                                                                                                                                                             |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `local.store`            | Default [local agent store](https://cursor.com/docs/sdk/typescript.md#local-agent-stores) when a call omits `local.store`. The SDK uses on-disk SQLite through Node's `node:sqlite`. Use `JsonlLocalAgentStore` or another store when you want to avoid SQLite storage. |
| `local.useHttp1ForAgent` | Force local agent backend streams to use HTTP/1.1 with SSE instead of HTTP/2. Useful behind proxies or on fetch stacks that don't support HTTP/2.Bun defaults to HTTP/1.1 due to upstream HTTP/2 compatibility issues.                                                  |

```typescript
import { Cursor, JsonlLocalAgentStore } from "@cursor/sdk";

Cursor.configure({
  local: {
    store: new JsonlLocalAgentStore("/var/lib/cursor-agents"),
    useHttp1ForAgent: true,
  },
});
```

##### Cursor.me()

```typescript
function Cursor.me(options?: CursorRequestOptions): Promise<SDKUser>;

interface CursorRequestOptions {
  apiKey?: string;
}

interface SDKUser {
  apiKeyName: string;
  userId?: number;
  userEmail?: string;
  userFirstName?: string;
  userLastName?: string;
  createdAt: string;
}
```

##### Cursor.models.list()

```typescript
function Cursor.models.list(options?: CursorRequestOptions): Promise<SDKModel[]>;

type SDKModel = ModelListItem;

interface ModelListItem {
  id: string;
  displayName: string;
  description?: string;
  aliases?: string[];
  parameters?: ModelParameterDefinition[];
  variants?: ModelVariant[];
}

interface ModelParameterDefinition {
  id: string;
  displayName?: string;
  values: Array<{ value: string; displayName?: string }>;
}

interface ModelVariant {
  params: ModelParameterValue[];
  displayName: string;
  description?: string;
  isDefault?: boolean;
}
```

Use `Cursor.models.list()` to discover valid `model` ids and per-model `params` before calling `Agent.create()` or `agent.send()`. Parameters are model-specific. Common examples include reasoning effort.

```typescript
const models = await Cursor.models.list();
const composer = models.find((model) => model.id === "composer-2.5");

console.log(composer?.parameters);
// [
//   {
//     id: "fast",
//     displayName: "Fast",
//     values: [
//       { value: "false" },
//       { value: "true", displayName: "Fast" },
//     ],
//   },
// ]
```

Pass selected parameter values through `model.params`. Preset `variants` already contain valid `params`, so you can copy them into a model selection.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: {
    id: "composer-2.5",
    params: [{ id: "fast", value: "true" }],
  },
  local: { cwd: process.cwd() },
});
```

###### Best practices

- **Discover, don't hard-code.** Call `Cursor.models.list()` at startup (or once per process) and cache the result. Model ids and parameter shapes can change as new models ship.
- **Pass parameters explicitly when the model expects them.** A model whose `parameters` array is non-empty is a parameterized model. Send the params you want; otherwise the run uses each parameter's first allowed value, which may not match what you intend.
- **Resolve by capability, not id.** If you want "the current default in fast mode" rather than a specific model, look it up:

  ```typescript
  const models = await Cursor.models.list();
  const composer = models.find((m) => m.id === "composer-2.5");
  const fast = composer?.parameters?.find((p) => p.id === "fast");
  const fastValue = fast?.values.find((v) => v.value === "true")?.value;

  const model = composer
    ? {
        id: composer.id,
        params: fastValue ? [{ id: "fast", value: fastValue }] : undefined,
      }
    : { id: "auto" };
  ```

  Falling back to `{ id: "auto" }` when a target model isn't available keeps scripts working as the catalog evolves.

##### Cursor.repositories.list()

```typescript
function Cursor.repositories.list(options?: CursorRequestOptions): Promise<SDKRepository[]>;

interface SDKRepository {
  url: string;
}
```

Returns the GitHub repositories connected for the calling user's team. Cloud only.

#### Configuration sources at a glance

MCP servers, subagents, and hooks all resolve from a mix of inline options and on-disk config. The precedence is the same shape across the three: per-send inline > creation-time inline > project files > user files > team / dashboard config.

| Feature              | Inline option                                               | Local file (project)                                                       | Local file (user)                        | Cloud / dashboard                                                                      | Precedence                                                                                              |
| :------------------- | :---------------------------------------------------------- | :------------------------------------------------------------------------- | :--------------------------------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **MCP servers**      | `mcpServers` on `Agent.create()` and `agent.send()`         | `.cursor/mcp.json` (gated by `local.settingSources` including `"project"`) | `~/.cursor/mcp.json` (gated by `"user"`) | Servers configured at [cursor.com/agents](https://cursor.com/agents) (cloud only)      | Send > create > plugins > project > user (local); Send > create > dashboard (cloud)                     |
| **Subagents**        | `agents` on `Agent.create()`                                | `.cursor/agents/*.md` (frontmatter: `name`, `description`, `model?`)       | n/a                                      | Cloud picks up the same project files when the agent runs against the cloned repo      | Inline overrides file-based with the same name                                                          |
| **Hooks**            | None — file-based only                                      | `.cursor/hooks.json` (+ scripts)                                           | `~/.cursor/hooks.json`                   | Cloud runs project hooks. On Enterprise plans, also team and enterprise-managed hooks. | File-based; project layered with user / team / enterprise per [Hooks](https://cursor.com/docs/hooks.md) |
| **Settings sources** | `local.settingSources` selects which on-disk layers to load | `.cursor/`                                                                 | `~/.cursor/`                             | n/a                                                                                    | Cloud always loads `project` / `team` / `plugins` and ignores `local.settingSources`.                   |

Inline values are good for secrets that should never touch disk (per-run API keys, tenant-scoped tokens). File-based config is good for policy: hooks especially are a project boundary, not a per-run knob.

#### MCP servers

Agents can pick up MCP servers from several sources. Inline definitions in `Agent.create()` or `agent.send()` are the most common path. File-based and dashboard-managed configs are also supported.

##### What gets loaded

**Local agents** load servers from up to five sources, with first-match-wins precedence on conflicting names:

1. `mcpServers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcpServers` on `Agent.create()`. Used when no per-send override is provided.
3. Plugin servers, if `local.settingSources` includes `"plugins"`.
4. Project servers from `.cursor/mcp.json`, if `local.settingSources` includes `"project"`.
5. User servers from `~/.cursor/mcp.json`, if `local.settingSources` includes `"user"`.

Without `local.settingSources`, only inline servers are loaded. If a local MCP server requires OAuth login, the SDK can't prompt you to sign in. It only works if you've already signed in to that server from the Cursor app, in which case the SDK reuses that saved login.

**Cloud agents** load servers from:

1. `mcpServers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcpServers` on `Agent.create()`. Used when no per-send override is provided.
3. Your user and team MCP servers from [cursor.com/agents](https://cursor.com/agents).

If an inline server doesn't include `auth` or `headers` and you've previously authorized that server URL on cursor.com/agents, runs authenticated with a personal API token reuse those OAuth tokens automatically. Service account API keys cannot fall back to user auth as they are not associated with a user.

`local.settingSources` does not apply to cloud agents.

##### Local

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "auto" },
  local: { cwd: process.cwd() },
  mcpServers: {
    docs: {
      type: "http",
      url: "https://example.com/mcp",
      auth: {
        CLIENT_ID: "client-id",
        scopes: ["read", "write"],
      },
    },
    filesystem: {
      type: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-filesystem", process.cwd()],
      cwd: process.cwd(),
    },
  },
});
```

##### Cloud

Cloud agents can receive authenticated MCP configs inline too. Use HTTP auth when Cursor should proxy a remote MCP through the backend. Use stdio `env` when the server runs inside the cloud VM and reads credentials from environment variables.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  cloud: {
    repos: [{ url: "https://github.com/your-org/your-repo", startingRef: "main" }],
  },
  mcpServers: {
    linear: {
      type: "http",
      url: "https://mcp.linear.app/sse",
      headers: {
        Authorization: `Bearer ${process.env.LINEAR_API_KEY!}`,
      },
    },
    figma: {
      type: "http",
      url: "https://api.figma.com/mcp",
      auth: {
        CLIENT_ID: process.env.FIGMA_CLIENT_ID!,
        CLIENT_SECRET: process.env.FIGMA_CLIENT_SECRET!,
        scopes: ["file_content:read"],
      },
    },
    github: {
      type: "stdio",
      command: "npx",
      args: ["-y", "@modelcontextprotocol/server-github"],
      env: {
        GITHUB_TOKEN: process.env.GITHUB_TOKEN!,
      },
    },
  },
});
```

Use `headers` for static API keys or Bearer tokens — Cursor passes them through on every request. Use `auth` for OAuth-protected servers. For cloud, Cursor runs the OAuth flow once server-side and reuses the token across runs. Locally, the SDK can't open a browser to sign you in; it only reuses tokens you've already obtained by signing in through the Cursor app.

- HTTP `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted and do not enter the VM.
- Stdio `env` values are passed into the VM because the server runs there. Treat them like any other runtime secret.
- OAuth for MCP servers configured on cursor.com/agents stays per-user, even for team-level servers.

See [MCP](https://cursor.com/docs/mcp.md) for the full config format and [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools) for cloud-specific behavior.

#### Subagents

Define named subagents that the main agent spawns via the `Agent` tool. Pass them inline:

```typescript
const agent = await Agent.create({
  model: { id: "composer-2.5" },
  apiKey: process.env.CURSOR_API_KEY!,
  local: { cwd: process.cwd() },
  agents: {
    "code-reviewer": {
      description: "Expert code reviewer for quality and security.",
      prompt: "Review code for bugs, security issues, and proven approaches.",
      model: "inherit",
    },
    "test-writer": {
      description: "Writes tests for code changes.",
      prompt: "Write comprehensive tests for the given code.",
    },
  },
});
```

Subagents committed to the repo at `.cursor/agents/*.md` (with `name`, `description`, and optional `model` frontmatter) are also picked up. Inline definitions override file-based ones with the same name.

##### Nested subagents

Subagents can spawn their own subagents, within a nesting limit. When a subagent uses the `Agent` tool, the SDK hands it the same subagent executor the parent has, so a parent can delegate to a subagent that delegates further. Each level reaches the same set of named subagents and [custom tools](https://cursor.com/docs/sdk/typescript.md#custom-tools). The top-level agent and its direct subagents can launch subagents, but a subagent launched by another subagent can't launch further ones.

#### Custom tools

Custom tools let you expose your own functions to the agent without standing up a separate MCP server. Pass them on `local.customTools` and the SDK registers them as an MCP server named `custom-user-tools`. The agent discovers and calls them through the same MCP path as any other server, under the same [permission gate](https://cursor.com/docs/agent/tools/terminal.md#run-mode). Custom tools reach [subagents](https://cursor.com/docs/sdk/typescript.md#subagents) (including nested ones) too.

Custom tools are local agents only. Passing `local.customTools` to a cloud agent throws a `ConfigurationError`.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: {
    cwd: process.cwd(),
    customTools: {
      get_deployment_status: {
        description: "Look up the current deployment status for a service.",
        inputSchema: {
          type: "object",
          properties: {
            service: { type: "string", description: "Service name" },
          },
          required: ["service"],
        },
        async execute({ service }) {
          const res = await fetch(`https://deploys.internal/api/${service}`);
          const body = await res.json();
          return `Service ${service} is ${body.status} (build ${body.build}).`;
        },
      },
    },
  },
});

await agent.send("Is the checkout service deployed yet?").then((r) => r.wait());
```

Set custom tools once on `Agent.create()` to apply them to every run, or pass `local.customTools` on a single `agent.send()` to replace them for that run.

```typescript
await agent.send("Roll forward if the canary is healthy", {
  local: {
    customTools: {
      promote_canary: {
        description: "Promote the current canary build to production.",
        async execute() {
          await promoteCanary();
          return { content: [{ type: "text", text: "Promoted." }] };
        },
      },
    },
  },
});
```

##### Tool definition

```typescript
interface SDKCustomTool {
  description?: string;
  inputSchema?: Record<string, SDKJsonValue>;
  execute: (
    args: Record<string, SDKJsonValue>,
    context: SDKCustomToolContext
  ) => SDKCustomToolResult | Promise<SDKCustomToolResult>;
}

interface SDKCustomToolContext {
  toolCallId?: string;
}
```

| Field         | Description                                                                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `description` | Shown to the model so it knows when to call the tool. Defaults to an empty string.                                                             |
| `inputSchema` | JSON Schema for the arguments. Defaults to an open object that accepts any properties.                                                         |
| `execute`     | Your callback. Receives the parsed `args` and a `context` with the `toolCallId`. Runs in your process, so it can reach anything your code can. |

##### Tool results

`execute` can return a plain string, any JSON value, or a structured envelope. The map key is the tool name the model calls.

```typescript
type SDKCustomToolResult =
  | string
  | SDKJsonValue
  | {
      content: SDKCustomToolContent[];
      isError?: boolean;
      structuredContent?: Record<string, SDKJsonValue>;
    };

type SDKCustomToolContent =
  | { type: "text"; text: string }
  | { type: "image"; data: string; mimeType?: string };
```

- Return a string for plain text output.
- Return any JSON value to send it back as text; objects also populate `structuredContent`.
- Return the envelope for full control: mix text and base64 image `content`, set `isError: true` to report a failure, or attach `structuredContent` for the model to parse. Throwing from `execute` is also reported back to the agent as a tool error.

#### Hooks

Hooks are file-based only. There is no programmatic hook callback. Hooks are a project policy boundary, not a per-run knob.

- **Local:** Add `.cursor/hooks.json` to the repo passed as `local.cwd`, or add `~/.cursor/hooks.json` for user-level hooks.
- **Cloud:** Commit `.cursor/hooks.json` and its scripts to the repo passed in `cloud.repos`. SDK-created cloud agents load project hooks automatically. On Enterprise plans, they also run team hooks and enterprise-managed hooks.

See [Hooks](https://cursor.com/docs/hooks.md) for the configuration format and [Cloud Agents hooks support](https://cursor.com/docs/cloud-agent.md#hooks-support) for cloud behavior.

#### Sandbox options

Local agents run with `local.sandboxOptions.enabled: false` by default. The agent can read and write the working directory, execute shell commands, and reach the network without restriction. There's no human-in-the-loop approval flow in headless SDK runs, so a sandbox-by-default would either block legitimate tool calls silently or require a callback that doesn't fit a script.

When you enable the sandbox, the SDK constrains every shell tool call and shell-spawned process:

- **Filesystem** — Writes are limited to the working directory (`local.cwd`) and a small set of allowed paths. Reads outside the workspace are blocked.
- **Shell** — Commands run inside a platform sandbox (`bubblewrap` on Linux, `seatbelt` on macOS, the bundled `@cursor/sdk-<os>-<arch>` helper). Privileged operations are denied.
- **Network** — Outbound network is denied by default. To allow specific hosts, drop a `.cursor/sandbox.json` in the workspace listing the allowed hosts. The SDK reads the same per-user policy at `~/.cursor/sandbox.json` if present.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: {
    cwd: process.cwd(),
    sandboxOptions: { enabled: true },
  },
});
```

If sandboxing isn't supported on the host (older Linux without `bubblewrap`, missing helper binary), the SDK throws a `ConfigurationError` with a message that names the missing dependency. Disable `sandboxOptions.enabled` or run in cloud mode to recover.

Cloud runs always execute inside an isolated VM, so `sandboxOptions` doesn't apply.

#### Auto-review

By default a local agent runs every tool call without restriction, since headless runs have no human to approve them. Set `local.autoReview: true` to route local tool calls through [Auto-review](https://cursor.com/docs/agent/tools/terminal.md#run-mode) instead, the same classifier the IDE uses to allow or block Shell, MCP, and Fetch calls based on safety and how well each call matches the run's intent.

```typescript
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: {
    cwd: process.cwd(),
    autoReview: true,
  },
});
```

Auto-review needs the classifier enabled on the connected backend; when it isn't available, runs fall back to the default behavior. Because there's no interactive approval in a headless run, a call the classifier blocks is denied rather than escalated, and the agent gets the block reason and can try another approach. Steer the classifier with a `permissions.json` `autoRun` block in the workspace, the same as in the IDE. See [permissions.json](https://cursor.com/docs/reference/permissions.md) for the format.

Auto-review is local agents only. Cloud runs already execute in an isolated VM. The classifier is best-effort convenience, not a security boundary; combine it with [`sandboxOptions`](https://cursor.com/docs/sdk/typescript.md#sandbox-options) or an [allowlist](https://cursor.com/docs/agent/tools/terminal.md#run-mode) for strict control.

#### Artifacts

List and download files from the agent's workspace.

```typescript
interface SDKArtifact {
  path: string;
  sizeBytes: number;
  updatedAt: string;
}
```

```typescript
const artifacts: SDKArtifact[] = await agent.listArtifacts();

for (const artifact of artifacts) {
  console.log(artifact.path, artifact.sizeBytes);
}

const buffer = await agent.downloadArtifact(artifacts[0].path);
```

Artifact support is runtime-dependent. Local SDK agents currently return no artifacts and throw for `downloadArtifact`.

#### Resource management

Always dispose agents when done. The cleanest pattern is `await using`:

```typescript
await using agent = await Agent.create({ /* ... */ });
// disposed automatically when the block exits
```

To dispose explicitly:

```typescript
await agent[Symbol.asyncDispose]();
```

`agent.close()` is the documented way to start disposal without awaiting. `Symbol.asyncDispose` works (`await using` is built on it) but `close()` is the path you should reach for in code that doesn't use the `await using` syntax. `agent.reload()` picks up filesystem config changes (hooks, project MCP, subagents) without disposing.

#### Agent lifecycle

##### Reattach to an existing agent

`Agent.resume(agentId)` returns a fresh handle to an agent that already exists. The runtime is auto-detected from the ID prefix (`bc-` is cloud, anything else is local), and conversation state is loaded from the cloud (cloud) or the local checkpoint store (local). This is how you continue work after a process restart, or how a different worker picks up an agent another process started.

```typescript
const agent = await Agent.resume("bc-abc123", {
  apiKey: process.env.CURSOR_API_KEY!,
});

const run = await agent.send("Apply the suggested fix");
const result = await run.wait();
```

If the run was already running when you reattached, `Agent.getRun(runId, { runtime: "cloud", agentId })` (or the local equivalent) returns a `Run` you can `stream()`, `wait()`, or `cancel()` against.

##### Conversation context

Local agents persist conversation state in a checkpoint store. By default this is on-disk SQLite under your home directory; swap it for JSONL or a custom backend with [`local.store`](https://cursor.com/docs/sdk/typescript.md#local-agent-stores). Each call to `agent.send()` loads the latest checkpoint for that agent and passes it to the model, so follow-ups see the same context the previous run finished with. The store survives process restarts, which means `Agent.resume(agentId)` from a brand-new process picks up where the previous one left off.

Cloud agents persist state server-side. Reattaching from anywhere returns the same conversation.

A few things that look like context loss but aren't:

- A new `Agent.create()` always starts a fresh agent with a new `agentId`. To continue an existing conversation, capture `agent.agentId` from the first call and use `Agent.resume(agentId)` later.
- `Agent.prompt()` creates, runs, and disposes in one shot. There's no second turn; that's the contract.
- Inline `mcpServers` aren't persisted across `Agent.resume()` because they often carry secrets. Pass them again on resume, or use file-based MCP config.

##### Dispatcher pattern

A dispatcher owns a pool of agents and hands work to them as it arrives. The shape is straightforward: keep a map of `agentId` to long-lived `SDKAgent`, route incoming prompts by some key (user, repo, ticket), and `Agent.resume()` from disk if a process restart wiped the in-memory map.

```typescript
import { Agent, type SDKAgent } from "@cursor/sdk";

const agents = new Map<string, SDKAgent>();

async function getAgent(key: string, savedId?: string): Promise<SDKAgent> {
  const existing = agents.get(key);
  if (existing) return existing;

  const agent = savedId
    ? await Agent.resume(savedId, {
        apiKey: process.env.CURSOR_API_KEY!,
      })
    : await Agent.create({
        apiKey: process.env.CURSOR_API_KEY!,
        model: { id: "composer-2.5" },
        local: { cwd: process.cwd() },
      });

  agents.set(key, agent);
  return agent;
}

async function handleMessage(key: string, prompt: string, savedId?: string) {
  const agent = await getAgent(key, savedId);
  const run = await agent.send(prompt);
  return run.wait();
}
```

Cloud SSE streams retain backlog for a window after the run starts, so a dispatcher that streams to many subscribers can call `run.stream()` from each subscriber without losing earlier events. For really long-running cloud runs, dispatchers usually fan out to `run.wait()` and let subscribers poll `run.conversation()` if they need the structured transcript.

#### Local agent stores

Local agents persist agent metadata, conversation checkpoints, runs, and run events to disk so that follow-ups and `Agent.resume()` survive process restarts. By default the SDK uses `SqliteLocalAgentStore`, an on-disk SQLite store under a state root in your home directory. You can swap in a different backend with `local.store`.

The SDK ships two backends and lets you bring your own:

| Store                    | Import               | When to use                                                                                                          |
| :----------------------- | :------------------- | :------------------------------------------------------------------------------------------------------------------- |
| `SqliteLocalAgentStore`  | `@cursor/sdk/sqlite` | On-disk SQLite under the workspace state root.                                                                       |
| `JsonlLocalAgentStore`   | `@cursor/sdk`        | Portable newline-delimited JSON (NDJSON) files under a directory you choose. Easy to inspect, copy, and diff.        |
| Custom `LocalAgentStore` | Your code            | Persist to anything: in-memory, Redis, Postgres, or a hosted database. Implement the interface or compose substores. |

Cloud agents persist server-side, so `local.store` applies to local agents only.

##### JSONL store

`JsonlLocalAgentStore` writes four NDJSON files (`agents.ndjson`, `runs.ndjson`, `run_events.ndjson`, `checkpoints.ndjson`) under the directory you pass. Construct one and pass it on `local.store`.

```typescript
import { Agent, JsonlLocalAgentStore } from "@cursor/sdk";

const store = new JsonlLocalAgentStore("/var/lib/cursor-agents");

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: { cwd: process.cwd(), store },
});
```

Pass the same store instance on `Agent.resume()` and on the local list and get APIs (`Agent.list`, `Agent.get`, `Agent.listRuns`, `Agent.getRun`) so they read the same data.

##### Set a process-wide default

To avoid threading a store through every call, set a default once with [`Cursor.configure()`](https://cursor.com/docs/sdk/typescript.md#cursorconfigure). Per-call `local.store` still wins when you pass it.

```typescript
import { Cursor, JsonlLocalAgentStore } from "@cursor/sdk";

Cursor.configure({ local: { store: new JsonlLocalAgentStore("/var/lib/cursor-agents") } });

// Later calls use the configured store unless they pass their own.
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2.5" },
  local: { cwd: process.cwd() },
});
```

Pass `store: null` to `Cursor.configure({ local: { store: null } })` to clear a previous default and return to the SDK's default local store selection.

##### Custom stores

To persist somewhere else (a shared Postgres, Redis, or an in-memory map for tests), implement `LocalAgentStore`. It's four substores, each a small CRUD surface the SDK calls:

```typescript
interface LocalAgentStore {
  readonly agents: LocalAgentStoreAgents;         // agent metadata rows
  readonly checkpoints: LocalAgentStoreCheckpoints; // content-addressed conversation blobs
  readonly runs: LocalAgentStoreRuns;             // run rows
  readonly runEvents: LocalAgentStoreRunEvents;   // append-only run event log
}
```

Implement the interface directly, or build each substore separately and combine them with `composeLocalAgentStore`:

```typescript
import { composeLocalAgentStore } from "@cursor/sdk";

const store = composeLocalAgentStore({
  agents: myAgentsTable,
  checkpoints: myCheckpointBlobs,
  runs: myRunsTable,
  runEvents: myRunEventLog,
});
```

The substores mirror the default SQLite tables: `agents` holds one row per agent (with a slim `latestCheckpoint.rootBlobId` pointer), `checkpoints` holds the content-addressed conversation blobs those pointers reference, `runs` holds one row per run, and `runEvents` is the append-only stream log. Catalog substores paginate with an opaque `cursor` / `nextCursor`; the run event log resumes with an exclusive `afterOffset` / `nextOffset`. See the exported `LocalAgentStore`, `LocalAgentDocument`, `LocalAgentRunDocument`, and related types for the exact shapes.

#### Configuration reference

##### AgentOptions

| Property         | Type                              | Default                                                             | Description                                                                                                                                |
| :--------------- | :-------------------------------- | :------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `model`          | `ModelSelection`                  | Required for local; cloud falls back to the server-resolved default | Model to use. See [`ModelSelection`](https://cursor.com/docs/sdk/typescript.md#modelselection).                                            |
| `apiKey`         | `string`                          | `CURSOR_API_KEY` env                                                | User API key or service account key. Team Admin keys are not yet supported.                                                                |
| `name`           | `string`                          | Auto-generated                                                      | Human-readable agent name surfaced as `title` in `Agent.list()` / `Agent.get()`.                                                           |
| `local`          | `LocalAgentOptions`               |                                                                     | Local agent config. See [`LocalAgentOptions`](https://cursor.com/docs/sdk/typescript.md#localagentoptions).                                |
| `cloud`          | `CloudOptions`                    |                                                                     | Cloud agent config.                                                                                                                        |
| `mcpServers`     | `Record<string, McpServerConfig>` |                                                                     | Inline MCP server definitions.                                                                                                             |
| `agents`         | `Record<string, AgentDefinition>` |                                                                     | Subagent definitions.                                                                                                                      |
| `agentId`        | `string`                          | Auto-generated                                                      | Durable agent ID. Pass to keep a stable ID across invocations.                                                                             |
| `idempotencyKey` | `string`                          | Auto-generated for cloud                                            | Optional client-generated idempotency key. Cloud only.                                                                                     |
| `mode`           | `"agent" \| "plan"`               | `"agent"`                                                           | Initial conversation mode for the agent's first run. See [Conversation mode](https://cursor.com/docs/sdk/typescript.md#conversation-mode). |

##### LocalAgentOptions

Config for local agents, passed as `local` on `Agent.create()`. Also exported as a standalone type for `Partial<LocalAgentOptions>`.

| Property             | Type                            | Default              | Description                                                                                                               |
| :------------------- | :------------------------------ | :------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| `cwd`                | `string \| string[]`            |                      | Workspace path or paths.                                                                                                  |
| `settingSources`     | `SettingSource[]`               |                      | Ambient settings layers to load: `"project"`, `"user"`, `"team"`, `"mdm"`, `"plugins"`, or `"all"`.                       |
| `sandboxOptions`     | `{ enabled: boolean }`          | `{ enabled: false }` | [Sandbox](https://cursor.com/docs/sdk/typescript.md#sandbox-options) config.                                              |
| `autoReview`         | `boolean`                       | `false`              | Route local tool calls through [Auto-review](https://cursor.com/docs/sdk/typescript.md#auto-review).                      |
| `customTools`        | `Record<string, SDKCustomTool>` |                      | [Custom tools](https://cursor.com/docs/sdk/typescript.md#custom-tools) exposed as the `custom-user-tools` MCP server.     |
| `store`              | `LocalAgentStore`               | SDK default store    | [Local agent store](https://cursor.com/docs/sdk/typescript.md#local-agent-stores) backing persistence.                    |
| `enableAgentRetries` | `boolean`                       | `true`               | Enable transport and stall auto-retry for local agent runs. Set `false` to surface transport errors on the first failure. |

##### CloudOptions

| Property              | Type                                                                                                        | Default             | Description                                                                                                                                                                                                                                                                                                                                          |
| :-------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `env`                 | `{ type: "cloud"; name?: string } \| { type: "pool"; name?: string } \| { type: "machine"; name?: string }` | `{ type: "cloud" }` | Execution environment target. `cloud` uses Cursor-hosted VMs; set `name` to use a saved Cursor-hosted environment. `pool` and `machine` route to self-hosted workers you run. Omit `repos` and leave `env` at the default for a no-repo agent with an empty workspace. Named Cursor-hosted environments and explicit `repos` are mutually exclusive. |
| `repos`               | `Array<{ url: string; startingRef?: string; prUrl?: string }>`                                              |                     | Repositories to clone into the VM. Pass one entry for a single-repo agent, or up to 20 for a multi-repo agent. Mutually exclusive with a named `env.name` for Cursor-hosted environments. Pass `prUrl` to attach the agent to an existing PR.                                                                                                        |
| `workOnCurrentBranch` | `boolean`                                                                                                   | `false`             | Push commits to the existing branch instead of a new one.                                                                                                                                                                                                                                                                                            |
| `autoCreatePR`        | `boolean`                                                                                                   | `false`             | Open a PR when the run finishes.                                                                                                                                                                                                                                                                                                                     |
| `skipReviewerRequest` | `boolean`                                                                                                   | `false`             | Skip requesting the calling user as a reviewer on the PR.                                                                                                                                                                                                                                                                                            |

##### AgentDefinition

| Property      | Type                                               | Default     | Description                                                                                     |
| :------------ | :------------------------------------------------- | :---------- | :---------------------------------------------------------------------------------------------- |
| `description` | `string`                                           | *required*  | When to use this subagent. Shown to the parent agent so it knows when to spawn.                 |
| `prompt`      | `string`                                           | *required*  | System prompt for the subagent.                                                                 |
| `model`       | `ModelSelection \| "inherit"`                      | `"inherit"` | Model override. Pass `"inherit"` to use the parent's selection.                                 |
| `mcpServers`  | `Array<string \| Record<string, McpServerConfig>>` |             | MCP servers available to this subagent. Names reference servers from the parent's `mcpServers`. |

##### ModelSelection

```typescript
interface ModelSelection {
  id: string;
  params?: ModelParameterValue[];
}

interface ModelParameterValue {
  id: string;
  value: string;
}
```

`id` is the model identifier (for example, `"composer-2.5"`). `params` carries per-model parameters such as reasoning effort. Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/typescript.md#cursormodelslist) to discover valid ids, parameter definitions, and preset variants for your account.

##### McpServerConfig

```typescript
type McpServerConfig =
  // stdio
  | {
      type?: "stdio";
      command: string;
      args?: string[];
      env?: Record<string, string>;
      cwd?: string;       // local only; cloud rejects this field
    }
  // HTTP / SSE
  | {
      type?: "http" | "sse";
      url: string;
      headers?: Record<string, string>;   // passed through; Authorization here works
      auth?: {
        CLIENT_ID: string;
        CLIENT_SECRET?: string;
        scopes?: string[];
      };
    };
```

For HTTP servers running in the cloud, `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted before the VM sees them. For stdio servers in the cloud, `env` values are passed into the VM (treat them like any runtime secret).

##### SDKUserMessage

```typescript
interface SDKUserMessage {
  text: string;
  images?: SDKImage[];
}
```

The structured form of `agent.send()`'s message argument. Use it to send images alongside text.

##### SDKImage

```typescript
type SDKImage =
  | { url: string; dimension?: SDKImageDimension }
  | { data: string; mimeType: string; dimension?: SDKImageDimension };

interface SDKImageDimension {
  width: number;
  height: number;
}
```

Pass either a remote `url` or base64 `data` with a `mimeType`.

##### SettingSource

```typescript
type SettingSource =
  | "project"
  | "user"
  | "team"
  | "mdm"
  | "plugins"
  | "all";
```

Controls which on-disk settings layers a local agent loads. Cloud agents always load `project` / `team` / `plugins` and ignore this field.

| Value       | Source                                  |
| :---------- | :-------------------------------------- |
| `"project"` | `.cursor/` in the workspace             |
| `"user"`    | `~/.cursor/`                            |
| `"team"`    | Team settings synced from the dashboard |
| `"mdm"`     | MDM-managed enterprise settings         |
| `"plugins"` | Plugin-provided settings                |
| `"all"`     | Shorthand for all of the above          |

##### ListResult

```typescript
interface ListResult<T> {
  items: T[];
  nextCursor?: string;
}
```

Returned by `Agent.list()` and `Agent.listRuns()`. `nextCursor` is absent when there are no more pages.

#### Errors

All SDK errors extend `CursorSdkError` (re-exported as `CursorAgentError` for backwards compatibility). Use `isRetryable` to drive retry logic, and `code` / `status` / `requestId` for diagnostics.

```typescript
class CursorSdkError extends Error {
  readonly isRetryable: boolean;
  readonly code?: string;       // stable SDK / backend code
  readonly status?: number;     // HTTP status if available
  readonly cause?: unknown;     // wrapped underlying error
  readonly endpoint?: string;
  readonly requestId?: string;
  readonly operation?: string;  // SDK operation that produced the error
}
```

| Error class                    | Typical message                                               | Likely cause                                                                                                               | Recommended fix                                                                                                                                                                                                 |
| :----------------------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AuthenticationError`          | "Invalid API key"                                             | Missing or wrong `CURSOR_API_KEY`, expired token, or admin disabled the key.                                               | Generate a new key from [API Keys](https://cursor.com/dashboard/api) (user) or [Team settings](https://cursor.com/dashboard/team-settings) (service account). Confirm the key has permission for the operation. |
| `RateLimitError`               | "Rate limit exceeded" or "Usage limit exceeded"               | Burst limit or monthly usage cap.                                                                                          | Back off using exponential delay (the SDK reports `isRetryable: true` for transient cases). For monthly cap, raise the plan's [usage limit](https://cursor.com/docs/account/usage.md).                          |
| `ConfigurationError`           | "Bad model name", "API key not supported", "File unsupported" | Invalid `model.id`, missing required `params`, unsupported file in a tool call, or an admin policy blocking the request.   | Call `Cursor.models.list()` to confirm the id and params. Check repo / file paths exist.                                                                                                                        |
| `AgentBusyError`               | "Agent is busy"                                               | Sending a follow-up while the same cloud agent already has a run in `CREATING` or `RUNNING` state.                         | Wait for the active run to finish, cancel it, or poll `Agent.listRuns()` before sending again.                                                                                                                  |
| `IntegrationNotConnectedError` | "\[provider] integration is not connected"                    | Creating a cloud agent for a repo whose SCM provider isn't connected to your Cursor team.                                  | Open `error.helpUrl` to reconnect the provider, then retry.                                                                                                                                                     |
| `NetworkError`                 | "Service unavailable", "Timeout"                              | Transient backend issue, network partition, or deadline exceeded.                                                          | Retry with backoff. Inspect `error.requestId` if you need to file a support ticket.                                                                                                                             |
| `UnsupportedRunOperationError` | "Operation "stream" is not supported on this runtime"         | Calling a `Run` method the current runtime can't satisfy (e.g. streaming on a re-fetched local run that already finished). | Guard with `run.supports(operation)` / `run.unsupportedReason(operation)` first.                                                                                                                                |
| `AgentNotFoundError`           | "Agent not found"                                             | The requested agent does not exist or is not visible under the resolved local workspace.                                   | Check the agent ID, `cwd`, and `local.store`.                                                                                                                                                                   |
| `UnknownAgentError`            | Server-defined message                                        | Unclassified backend or runtime error.                                                                                     | Inspect `error.code` and `error.cause` for the underlying detail.                                                                                                                                               |

##### Check error.helpUrl

Some errors carry a one-click resolution link. The most common is
`IntegrationNotConnectedError`, but more error types may add `helpUrl` over
time. When you catch an error, log `error.helpUrl` if present and surface it
to the user.

##### IntegrationNotConnectedError

```typescript
class IntegrationNotConnectedError extends ConfigurationError {
  readonly provider: string;   // e.g. "github", "gitlab", "azuredevops"
  readonly helpUrl: string;    // dashboard link to reconnect
}
```

The default error message doesn't include `helpUrl`, so log it explicitly:

```typescript
import { Agent, IntegrationNotConnectedError } from "@cursor/sdk";

try {
  await Agent.create({
    apiKey: process.env.CURSOR_API_KEY!,
    cloud: {
      repos: [{ url: "https://github.com/your-org/private-repo" }],
    },
  });
} catch (err) {
  if (err instanceof IntegrationNotConnectedError) {
    console.error(err.provider, err.helpUrl);
  }
}
```

##### AgentBusyError

```typescript
class AgentBusyError extends CursorAgentError {}
```

`isRetryable` is `false` for `agent_busy`. Retrying immediately will keep failing until the active run reaches a terminal status or you cancel it. Other `409` responses, such as `agent_archived`, throw `ConfigurationError` instead.

Wait for the active run to finish, cancel it with `run.cancel()`, or poll `Agent.listRuns()` before sending again:

```typescript
import { Agent, AgentBusyError } from "@cursor/sdk";

const agent = await Agent.resume("bc-00000000-0000-0000-0000-000000000001");

try {
  await agent.send({ text: "Also add tests for the auth middleware." });
} catch (err) {
  if (err instanceof AgentBusyError) {
    const runs = await Agent.listRuns(agent.agentId, { runtime: "cloud", limit: 1 });
    const active = runs.items[0];
    if (active?.status === "running") {
      await active.cancel();
    }
    await agent.send({ text: "Also add tests for the auth middleware." });
    return;
  }
  throw err;
}
```

Local agents do not return `agent_busy`. Use `send({ local: { force: true } })` to expire a stuck local run before starting a new one.

##### UnsupportedRunOperationError

```typescript
class UnsupportedRunOperationError extends ConfigurationError {
  readonly operation: RunOperation;
}
```

Thrown when a `Run` operation isn't available on the current runtime. Use `run.supports(operation)` and `run.unsupportedReason(operation)` to check before calling.

#### Known limitations

- Inline `mcpServers` are not persisted across `Agent.resume()`. Pass them again on resume if needed.
- Custom tools (`local.customTools`), Auto-review (`local.autoReview`), and custom stores (`local.store`) are local agents only. Cloud agents reject `local.customTools` and persist server-side.
- Artifact download is not implemented for local agents (`agent.listArtifacts()` returns an empty list and `agent.downloadArtifact()` throws).
- `local.settingSources` (and the file-based MCP / subagent paths it gates) does not apply to cloud agents. Cloud always loads `project` / `team` / `plugins`.
- Hooks are file-based only (`.cursor/hooks.json`). No programmatic callbacks.
- The SDK doesn't auto-discover credentials from a local Cursor app installation. Set `CURSOR_API_KEY` (or pass `apiKey`) explicitly.
- Local mode requires Node.js 22.13 or later and platform sandbox-helper support. `SqliteLocalAgentStore` uses Node's `node:sqlite`; switch to `JsonlLocalAgentStore` or a custom `local.store` to avoid SQLite storage.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

### Cursor Python SDK

*The `cursor-sdk` package lets you call Cursor's agent from your own Python code. The same agent that runs in the Cursor IDE, CLI, and web app is scriptable from Python with sync and async clients, typed dataclasses, and ordinary iteration for streams and pages. Run the `/sdk` skill inside Cursor to get started.*

**Source:** https://cursor.com/docs/sdk/python

The `cursor-sdk` package lets you call Cursor's agent from your own Python code. The same agent that runs in the Cursor IDE, CLI, and web app is scriptable from Python with sync and async clients, typed dataclasses, and ordinary iteration for streams and pages. Run the `/sdk` skill inside Cursor to get started.

For the REST API, see the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md).

#### Overview

The SDK wraps local and cloud runtimes behind one interface. You write the same code regardless of where the agent runs.

| Runtime                   | What it does                                                          | When to use                                                                                                                |
| :------------------------ | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Local**                 | Runs the agent against local files on disk.                           | Dev scripts and CI checks against a working tree.                                                                          |
| **Cloud (Cursor-hosted)** | Runs in an isolated VM with your repo cloned in. Cursor runs the VMs. | When the caller doesn't have the repo, you want many agents in parallel, or runs need to survive the caller disconnecting. |

Set the runtime by passing `local` or `cloud` to `Agent.create()`.

#### Authentication

Set `CURSOR_API_KEY` or pass `api_key` before creating an agent.

The SDK accepts user API keys and service account API keys for both local and cloud runs. Team Admin API keys are not yet supported.

- **User API key** from [Cursor Dashboard -> API Keys](https://cursor.com/dashboard/api)
- **Service account API key** from [Team settings](https://cursor.com/dashboard/team-settings). See [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md)

```bash
export CURSOR_API_KEY="your-key"
```

#### Usage and billing

SDK runs follow the same pricing, request pools, and Privacy Mode rules as runs from the IDE and Cloud Agents. Spend shows up in your team's [usage dashboard](https://cursor.com/dashboard/usage) under the SDK tag.

To read per-run token counts in code, see [Token usage](https://cursor.com/docs/sdk/python.md#token-usage).

#### Core concepts

| Concept          | Description                                                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Agent**        | Durable handle that holds conversation state, workspace config, model selection, and settings. Survives across multiple prompts. |
| **Run**          | One prompt submission. Owns its own stream, status, result, conversation, and cancellation.                                      |
| **SDKMessage**   | Typed stream message yielded during a run. Same shape across local and cloud runtimes.                                           |
| **CursorClient** | Explicit client for lifecycle control, custom HTTP options, or multiple workspaces in one process. `Client` is an alias.         |
| **AsyncClient**  | Async-mirror client. Required for all async operations.                                                                          |

#### Installation

```bash
pip install cursor-sdk
```

Requires Python 3.10 or later.

#### Quick start

```python
import os

from cursor_sdk import Agent, LocalAgentOptions

with Agent.create(
    model="composer-2.5",
    api_key="crsr_key",
    local=LocalAgentOptions(cwd=os.getcwd()),
) as agent:
    print(agent.send("Summarize what this repository does").text())
```

[Stream events](https://cursor.com/docs/sdk/python.md#stream-events) shows how to extract assistant text, handle tool calls, and read run state. For a one-shot prompt (create, run, finish), see [`Agent.prompt()`](https://cursor.com/docs/sdk/python.md#agentprompt).

##### Cloud quick start

The Python SDK has native support for Cursor's cloud agents. You can list connected repositories, start an agent against one of them, wait for the run, and review the final result.

```python
from cursor_sdk import Agent, CloudAgentOptions, CloudRepository

with Agent.create(
    model="composer-2.5",
    api_key="crsr_key",
    cloud=CloudAgentOptions(
        repos=[CloudRepository(url="https://github.com/your-org/your-repo", starting_ref="main")],
        auto_create_pr=True,
    ),
) as agent:
    print(agent.send("Add structured logging to the auth middleware").text())
```

Cloud agents started by the SDK are filtered out of the default agent list. To view them in Cursor Web or the Cursor agents window, click **Filter > Source > SDK**.

#### Async usage

The async client mirrors the sync surface and is recommended for servers, bots, and concurrent agent orchestration. `AsyncAgent`, `AsyncClient`, `AsyncRun`, and `AsyncCursor` are exported from both `cursor_sdk` and `cursor_sdk.asyncio`.

```python
import asyncio
import os

from cursor_sdk import AsyncClient, LocalAgentOptions

async def main():
    async with await AsyncClient.launch_bridge(workspace=os.getcwd()) as client:
        async with await client.agents.create(
            model="composer-2.5",
            api_key="crsr_key",
            local=LocalAgentOptions(cwd=os.getcwd()),
        ) as agent:
            run = await agent.send("Summarize what this repository does")
            print(await run.text())

asyncio.run(main())
```

There is no global async default client. Instantiate `AsyncClient` explicitly, or use `AsyncClient.launch_bridge(...)` as an async context manager, so each event loop owns its own client. Do not mix sync and async clients in the same code path.

| Sync                      | Async                               |
| :------------------------ | :---------------------------------- |
| `CursorClient` / `Client` | `AsyncClient` / `AsyncCursorClient` |
| `Agent`                   | `AsyncAgent`                        |
| `Run`                     | `AsyncRun`                          |
| `Cursor`                  | `AsyncCursor`                       |
| `ListResult`              | `AsyncListResult`                   |
| `DefaultHttpxClient`      | `DefaultAsyncHttpxClient`           |

#### Creating agents

`Agent.create()` validates options and returns a handle immediately. Pass either `local` or `cloud` to pick a runtime.

```python
from cursor_sdk import Agent, CloudAgentOptions, CloudRepository, LocalAgentOptions

agent = Agent.create(
    model="composer-2.5",
    local=LocalAgentOptions(cwd="."),
)

cloud_agent = Agent.create(
    model="composer-2.5",
    cloud=CloudAgentOptions(
        repos=[CloudRepository(url="https://github.com/your-org/your-repo", starting_ref="main")],
        auto_create_pr=True,
    ),
)
```

`agent.agent_id` is populated immediately. Local agents get an `agent-<uuid>` ID; cloud agents get a `bc-<uuid>` ID. `agent.model` is a typed `ModelSelection`, so `agent.model.id` and `agent.model.params` work directly.

Cloud agents started by the SDK are filtered out of the default agent list. To
view them in Cursor Web or a Cursor agent window, click **Filter > Source > SDK**.

##### Session environment variables

For cloud agents, pass `env_vars` when a run needs short-lived credentials or other values that should live only with that agent.

```python
agent = Agent.create(
    model="composer-2.5",
    cloud=CloudAgentOptions(
        repos=[CloudRepository(url="https://github.com/your-org/your-repo")],
        env_vars={
            "STAGING_API_TOKEN": os.environ["STAGING_API_TOKEN"],
        },
    ),
)
```

These values are encrypted at rest, injected into the cloud agent's shell, and deleted with the agent. `env_vars` can't be used with a caller-supplied `agent_id`; omit `agent_id` and read the server-minted ID from `agent.agent_id`. Variable names can't start with `CURSOR_`.

For values that should only exist during a single run, pass them on `agent.send()` instead. See [Per-run environment variables](https://cursor.com/docs/sdk/python.md#per-run-environment-variables).

##### Model parameters

Use `ModelSelection.params` to pass per-model options such as reasoning effort. Parameter IDs and values vary by model. Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/python.md#the-cursor-namespace) to discover supported parameters and preset variants for your account.

```python
from cursor_sdk import Agent, LocalAgentOptions, ModelParameterValue, ModelSelection

agent = Agent.create(
    model=ModelSelection(
        id="composer-2.5",
        params=[ModelParameterValue(id="fast", value="true")],
    ),
    local=LocalAgentOptions(cwd="."),
)
```

Use [`Cursor.models.list()`](https://cursor.com/docs/sdk/python.md#the-cursor-namespace) to discover the parameter IDs and preset variants for a given model.

##### Raw dictionaries

Typed dataclasses are preferred for application code because IDE autocomplete and type checking work better. The SDK also accepts plain dictionaries for short scripts or externally supplied JSON. Snake-case keys are normalized.

```python
from cursor_sdk import Agent

with Agent.create(
    {
        "api_key": "crsr_key",
        "model": {"id": "composer-2.5"},
        "local": {"cwd": "."},
    }
) as agent:
    ...
```

#### Agent

The handle returned by `Agent.create()`, `Agent.resume()`, `client.agents.create()`, and `client.agents.resume()`.

```python
class Agent:
    agent_id: str
    model: ModelSelection | None
    client: CursorClient

    def send(
        self,
        message: str | Mapping[str, Any] | UserMessage,
        options: SendOptions | Mapping[str, Any] | None = None,
        *,
        idempotency_key: str | None = None,
    ) -> Run: ...

    def reload(self) -> None: ...
    def close(self) -> None: ...

    def list_messages(
        self, options: Mapping[str, Any] | None = None
    ) -> list[AgentMessage]: ...
    def list_artifacts(self) -> list[SDKArtifact]: ...
    def download_artifact(self, path: str) -> bytes: ...

    def archive(self, options: Mapping[str, Any] | None = None) -> None: ...
    def unarchive(self, options: Mapping[str, Any] | None = None) -> None: ...
    def delete(self, options: Mapping[str, Any] | None = None) -> None: ...
```

| Member                             | Description                                                                           |
| :--------------------------------- | :------------------------------------------------------------------------------------ |
| `agent_id`                         | Stable agent identifier. `agent-<uuid>` for local, `bc-<uuid>` for cloud.             |
| `model`                            | Current typed model selection. Updates after a successful send with a model override. |
| `send`                             | Start a new run with the given prompt. Returns a `Run` handle.                        |
| `reload`                           | Re-read filesystem config (hooks, project MCP, subagents) without disposing.          |
| `close`                            | Close the agent and release resources.                                                |
| `list_messages`                    | List message history for the agent.                                                   |
| `list_artifacts`                   | List files produced by the agent (cloud only; local returns empty).                   |
| `download_artifact`                | Download a file by path (cloud only; local raises).                                   |
| `archive` / `unarchive` / `delete` | Manage cloud agent lifecycle.                                                         |

Use a context manager for automatic cleanup:

```python
with Agent.create(model="composer-2.5", local=LocalAgentOptions(cwd=".")) as agent:
    print(agent.send("Explain this repository").text())
```

When you use the sync `Agent.*` or `Cursor.*` helpers without passing `client=`, the SDK starts or reuses a module-level default client. It is closed automatically at process exit, and you can close it explicitly:

```python
from cursor_sdk import close_default_client

close_default_client()
```

##### Agent.prompt()

```python
Agent.prompt(
    message: str | Mapping[str, Any] | UserMessage,
    options: AgentOptions | Mapping[str, Any] | None = None,
    *,
    client: CursorClient | None = None,
) -> RunResult
```

One-shot convenience: creates an agent, sends a single prompt, waits for the run to finish, and disposes.

```python
from cursor_sdk import Agent, AgentOptions, LocalAgentOptions

result = Agent.prompt(
    "What does the auth middleware do?",
    AgentOptions(model="composer-2.5", local=LocalAgentOptions(cwd=".")),
)
print(result.result)
```

Async equivalent (assumes you already have an `AsyncClient` open):

```python
from cursor_sdk import AgentOptions, AsyncAgent, LocalAgentOptions

result = await AsyncAgent.prompt(
    "What does the auth middleware do?",
    AgentOptions(model="composer-2.5", local=LocalAgentOptions(cwd=".")),
    client=client,
)
```

#### CursorClient

Use `CursorClient` when you want explicit lifecycle control, a custom bridge endpoint, custom HTTP options, or multiple workspaces in one process. `Client` remains available as an alias.

```python
from cursor_sdk import CursorClient, LocalAgentOptions

with CursorClient.launch_bridge(workspace=".") as client:
    with client.agents.create(
        model="composer-2.5",
        api_key="crsr_key",
        local=LocalAgentOptions(cwd="."),
    ) as agent:
        print(agent.send("Summarize what this repository does").text())
```

##### Resources

Explicit clients expose resource namespaces:

| Resource       | Sync method examples                                                             | Async method examples                                              |
| :------------- | :------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| `agents`       | `client.agents.create(...)`, `client.agents.list(...)`, `client.agents.get(...)` | `await client.agents.create(...)`, `await client.agents.list(...)` |
| `models`       | `client.models.list()`                                                           | `await client.models.list()`                                       |
| `repositories` | `client.repositories.list()`                                                     | `await client.repositories.list()`                                 |

Top-level methods such as `client.create_agent(...)` and `client.list_agents(...)` remain available, but resource namespaces are the preferred shape for application code.

##### Custom HTTP clients

Both sync and async clients accept a custom `httpx` client for proxies, transports, and other advanced HTTP configuration:

```python
from cursor_sdk import CursorClient, DefaultHttpxClient

with CursorClient.launch_bridge(
    workspace=".",
    http_client=DefaultHttpxClient(proxy="http://proxy.example.com"),
) as client:
    ...
```

```python
from cursor_sdk import AsyncClient, DefaultAsyncHttpxClient

async with await AsyncClient.launch_bridge(
    workspace=".",
    http_client=DefaultAsyncHttpxClient(proxy="http://proxy.example.com"),
) as client:
    ...
```

`DefaultHttpxClient` and `DefaultAsyncHttpxClient` keep the SDK's default timeout and redirect behavior. Plain `httpx.Client` and `httpx.AsyncClient` use httpx defaults instead.

##### Connecting to a running bridge

If you already have a bridge endpoint (for example, a sidecar managed by your platform), use `connect(...)` to attach without spawning a new process:

```python
from cursor_sdk import CursorClient, LocalAgentOptions

with CursorClient.connect(
    base_url="http://127.0.0.1:8765",
    auth_token="bridge_token",
) as client:
    with client.agents.create(
        model="composer-2.5",
        api_key="crsr_key",
        local=LocalAgentOptions(cwd="."),
    ) as agent:
        ...
```

Async equivalent uses `AsyncClient.connect(...)` and `await client.aclose()`. Both forms default to `allow_api_key_env_fallback=False`; pass `api_key=` on each call or opt into env fallback when constructing the client.

##### Configuring timeouts and retries

Both clients expose `with_options(...)`, which returns a shallow copy that shares connection settings and overrides defaults:

```python
short = client.with_options(timeout=5.0, max_retries=2)
agent = short.agents.create(model="composer-2.5", local=LocalAgentOptions(cwd="."))
```

Async equivalent:

```python
short_async = async_client.with_options(timeout=5.0, max_retries=2)
agent = await short_async.agents.create(model="composer-2.5", local=LocalAgentOptions(cwd="."))
```

#### Sending messages

Each `agent.send()` returns a `Run`. Each `await async_agent.send()` returns an `AsyncRun`. The agent retains conversation context across runs; the run is the unit of work for one prompt.

```python
print(agent.send("Find the bug in src/auth.py").text())

# Same agent, full conversation context is preserved.
print(agent.send("Fix it and add a regression test").text())
```

Async equivalent:

```python
run = await agent.send("Find the bug in src/auth.py")
print(await run.text())

run = await agent.send("Fix it and add a regression test")
print(await run.text())
```

To send images alongside text:

```python
run = agent.send(
    {
        "text": "What's in this screenshot?",
        "images": [{"data": base64_png, "mime_type": "image/png"}],
    }
)
```

You can also use helper dataclasses. `SDKImage.from_file(path)` reads from disk and handles base64 encoding for you:

```python
from cursor_sdk import SDKImage, UserMessage

run = agent.send(
    UserMessage(
        text="What's in this screenshot?",
        images=[SDKImage.from_file("screenshot.png")],
    )
)
```

`SDKImage.data_image(base64_data, mime_type)` and `SDKImage.url_image(url)` are also available for callers that already have encoded bytes or a remote URL.

##### Run

```python
class Run:
    id: str
    agent_id: str
    status: str  # "running" | "finished" | "error" | "cancelled" | "expired"
    result: str
    model: ModelSelection | None
    duration_ms: int
    git: RunGitInfo | None
    created_at: str | None
    usage: TokenUsage | None  # cumulative; property on the live handle

    def messages(self) -> Iterator[SDKMessage]: ...
    def events(self) -> Iterator[RunStreamEvent]: ...
    def iter_text(self) -> Iterator[str]: ...
    def text(self) -> str: ...
    def wait(self) -> RunResult: ...
    def cancel(self) -> None: ...
    def conversation(self) -> list[ConversationTurn]: ...
    def conversation_json(self) -> str: ...
    def observe(self, *, after_offset: str | None = None) -> Iterator[RunStreamEvent]: ...

    def supports(self, operation: str) -> bool: ...
    def unsupported_reason(self, operation: str) -> str | None: ...
    def on_did_change_status(
        self, listener: Callable[[str], None]
    ) -> Callable[[], None]: ...
```

`run.stream()` is an alias for `run.messages()`. Iterating `run` directly yields `RunStreamEvent` envelopes, the same as `run.events()`.

`AsyncRun` exposes the same state fields, including `usage`. Methods that do I/O are async: `async for message in run.messages()`, `async for event in run.events()`, `async for text in run.iter_text()`, `await run.text()`, `await run.wait()`, `await run.cancel()`, `await run.conversation()`, `await run.conversation_json()`, and `async for event in run.observe()`.

##### Streaming

```python
run = agent.send("Find the bug in src/auth.py")

for message in run.messages():
    if message.type == "assistant":
        for block in message.message.content:
            if block.type == "text":
                print(block.text, end="")
    elif message.type == "thinking":
        print(message.text, end="")
    elif message.type == "tool_call":
        print(f"[tool] {message.name}: {message.status}")
    elif message.type == "status":
        print(f"[status] {message.status}")
    elif message.type == "usage":
        print(f"[usage] turn total={message.usage.total_tokens}")
```

A run stream is consumable once. `run.messages()`, `run.events()`, and `run.iter_text()` all draw from the same underlying stream and advance it. Once the stream completes, the run holds the terminal result (`run.result`, `run.status`, `run.usage`, `run.git`, ...). Call `run.wait()` to drain any remaining events and return the typed `RunResult`.

##### Waiting without streaming

```python
result = run.wait()

print(result.status)       # "finished" | "error" | "cancelled" | "expired"
print(result.result)       # final assistant text, if any
print(result.model)        # resolved ModelSelection used for this run
print(result.duration_ms)
print(result.usage)        # cumulative TokenUsage, or None if unavailable
print(result.git)          # RunGitInfo on cloud
```

Async equivalent:

```python
result = await run.wait()
```

##### Token usage

Runs report token usage when the runtime provides it. Read the cumulative total from `run.usage` on the live handle (while streaming or after `wait()`), or from `result.usage` on the `RunResult` returned by `run.wait()`. Both hold a `TokenUsage` summed across every turn that reported usage, and both are `None` when no turn did—for example a cancelled run that never finished a turn, a runtime that doesn't surface usage, or a detached cloud snapshot that hasn't reconciled usage yet.

```python
@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    total_tokens: int
    reasoning_tokens: int | None = None
```

| Field                | Description                                                                                           |
| :------------------- | :---------------------------------------------------------------------------------------------------- |
| `input_tokens`       | Prompt tokens sent to the model.                                                                      |
| `output_tokens`      | Tokens generated by the model.                                                                        |
| `cache_read_tokens`  | Tokens served from the prompt cache.                                                                  |
| `cache_write_tokens` | Tokens written to the prompt cache.                                                                   |
| `total_tokens`       | `input_tokens + output_tokens + cache_read_tokens + cache_write_tokens`. Excludes `reasoning_tokens`. |
| `reasoning_tokens`   | Reasoning tokens, a subset of `output_tokens`. `None` when the model or runtime didn't report it.     |

```python
result = run.wait()

if result.usage is not None:
    print(f"total: {result.usage.total_tokens}")
    print(f"in: {result.usage.input_tokens}, out: {result.usage.output_tokens}")
    print(
        f"cache read/write: {result.usage.cache_read_tokens}/{result.usage.cache_write_tokens}"
    )
else:
    print("no usage reported for this run")
```

`reasoning_tokens` is already counted inside `output_tokens`, so `total_tokens` leaves it out to avoid double-counting.

For per-turn numbers as they stream, handle the `usage` [stream event](https://cursor.com/docs/sdk/python.md#stream-events) (`SDKUsageMessage`). It fires once at the end of each turn that reported usage and carries that turn's `TokenUsage`. `run.usage` and `result.usage` stay cumulative across the run. After stream turns, the handle prefers those summed totals; otherwise it uses usage from `wait()` or from a `get_run` / `list_runs` snapshot when the bridge supplies it.

```python
for message in run.messages():
    if message.type == "usage":
        print(f"turn used {message.usage.total_tokens} tokens")

# Or after wait / without consuming messages yourself:
result = run.wait()
print(run.usage, result.usage)
```

Async equivalent: `async for message in run.messages()` and `await run.wait()`. `run.usage` is still a sync property on `AsyncRun`.

`TokenUsage` is exported from `cursor_sdk` (plus `to_token_usage` / `sum_token_usage` for advanced callers). Wire JSON is camelCase (`inputTokens`, …); the Python dataclasses use snake\_case.

##### Reading text output

`iter_text()` yields assistant text as it streams. `text()` returns the final terminal text, blocking on `wait()` if the run is still running.

```python
for chunk in run.iter_text():
    print(chunk, end="")

final_text = run.text()
```

Async equivalent:

```python
async for chunk in run.iter_text():
    print(chunk, end="")

final_text = await run.text()
```

##### Cancelling a run

```python
run.cancel()
```

Async equivalent:

```python
await run.cancel()
```

`run.cancel()` requests cancellation of an active run. The status moves to `"cancelled"`, the live stream stops, in-flight tool calls stop, and `run.wait()` resolves with `status: "cancelled"`. Partial output (assistant text written so far) stays on the `Run` object.

Cancelling a run that is already terminal (`"finished"`, `"error"`, `"cancelled"`, `"expired"`) raises `UnsupportedRunOperationError`. Guard with `run.status` when in doubt:

```python
if run.status == "running":
    run.cancel()
```

##### Reading run state

```python
print(run.id)
print(run.status)  # "running" | "finished" | "error" | "cancelled" | "expired"

stop = run.on_did_change_status(lambda status: print(f"status changed to {status}"))
stop()  # remove the listener

turns = run.conversation()
```

`run.conversation()` returns a typed `list[ConversationTurn]`. Use it to render or persist structured history without subscribing to the live stream. `run.conversation_json()` returns the raw JSON string.

For async runs, use `await run.conversation()` and `await run.conversation_json()`.

##### Per-run model override

The `model` you pass to `agent.send()` overrides the agent's selection for that run, then becomes sticky: subsequent sends without an override continue to use the new model. To switch back, pass another `model` override or read the current selection from `agent.model`.

```python
from cursor_sdk import ModelParameterValue, ModelSelection, SendOptions

run = agent.send(
    "Plan the refactor",
    SendOptions(
        model=ModelSelection(
            id="composer-2.5",
            params=[ModelParameterValue(id="fast", value="true")],
        ),
    ),
)
```

`run.model` and `result.model` reflect the selection this run used and are immutable once the run starts.

##### Per-run environment variables

Cloud agents can also take environment variables for a single run. Pass `cloud.env_vars` in `SendOptions` and the values are injected into the agent's shell for that run only — when the run finishes, they're removed from the VM and the next run doesn't see them. This is the right shape for credentials that rotate between turns, like a short-lived deploy token you mint right before asking the agent to use it.

```python
from cursor_sdk import CloudSendOptions, SendOptions

run = agent.send(
    "Deploy the preview environment",
    SendOptions(
        cloud=CloudSendOptions(env_vars={"DEPLOY_TOKEN": mint_short_lived_token()}),
    ),
)
```

If a run-scoped variable has the same name as an agent-scoped one from [`env_vars` on `CloudAgentOptions`](https://cursor.com/docs/sdk/python.md#session-environment-variables), the run-scoped value wins for that run, then the agent-scoped value comes back on the next run.

Per-run variables work on the first send too. The SDK passes them along with agent creation, scoped to the initial run, so they aren't persisted on the agent. Like agent-scoped variables, they're encrypted at rest and names can't start with `CURSOR_`.

Per-run environment variables are cloud agents only, and they aren't available for agents running against public repositories. For local agents, the agent process inherits your own environment, so set variables on the process before calling `send()`.

##### Conversation mode

Pass `mode="plan"` or `mode="agent"` to control whether a run explores and plans first or implements changes directly. See [Plan mode](https://cursor.com/help/ai-features/plan-mode.md) for what plan mode does in the product.

Set `mode` in `AgentOptions` passed to `Agent.create()` to seed the first run. On follow-up `agent.send()` calls, omit `mode` to keep the conversation's current mode, or pass `mode` to switch for that run only.

```python
from cursor_sdk import Agent, AgentOptions, CloudAgentOptions, CloudRepository, SendOptions

with Agent.create(
    AgentOptions(
        model="composer-2.5",
        mode="plan",
        cloud=CloudAgentOptions(
            repos=[CloudRepository(url="https://github.com/your-org/your-repo")],
        ),
    )
) as agent:
    agent.send("Design the auth refactor").wait()
    agent.send(
        "Looks good, start building",
        SendOptions(mode="agent"),
    ).wait()
```

##### Streaming raw deltas

Pass `on_delta` and `on_step` callbacks in `SendOptions` for lower-level updates. Sync callbacks are called inline. Async callbacks may be sync or async; awaitable return values are awaited before the next event is processed.

```python
from cursor_sdk import SendOptions

def on_delta(update):
    if update.type in ("text-delta", "thinking-delta"):
        print(update.text, end="")

run = agent.send(
    "Refactor the utils module",
    SendOptions(on_delta=on_delta, on_step=lambda step: print(f"[step] {step.type}")),
)
run.wait()
```

The concrete update and step subclasses live in `cursor_sdk.events`:

```python
from cursor_sdk.events import TextDeltaUpdate, ToolCallStartedUpdate

if isinstance(update, TextDeltaUpdate):
    print(update.text)
```

They remain importable from `cursor_sdk` for backward compatibility, but new code should import from `cursor_sdk.events`.

##### SendOptions

| Property          | Type                                         | Description                                                                                                                                                                                                                              |
| :---------------- | :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`           | `str \| ModelSelection \| Mapping[str, Any]` | Per-send model override. If omitted, uses `agent.model`. Sticky after a successful send.                                                                                                                                                 |
| `mode`            | `"agent" \| "plan"`                          | Per-send conversation mode override. If omitted on follow-ups, keeps the conversation's current mode.                                                                                                                                    |
| `mcp_servers`     | `Mapping[str, McpServerConfig]`              | Inline MCP server definitions. Fully replaces creation-time servers for this run.                                                                                                                                                        |
| `cloud.env_vars`  | `Mapping[str, str]`                          | Cloud agents only. [Per-run environment variables](https://cursor.com/docs/sdk/python.md#per-run-environment-variables) injected for this run and removed when it finishes. Overrides agent-scoped `env_vars` by name for this run only. |
| `local.force`     | `bool`                                       | Local agents only. Defaults to `False`. Expire a stuck active run before starting this message. Cloud returns `409 agent_busy` server-side, so no equivalent is needed.                                                                  |
| `idempotency_key` | `str`                                        | Optional client-generated idempotency key for the send.                                                                                                                                                                                  |
| `on_step`         | `Callable[[ConversationStep], Any]`          | Callback after each completed conversation step (text, thinking, or tool batch).                                                                                                                                                         |
| `on_delta`        | `Callable[[InteractionUpdate], Any]`         | Callback per raw `InteractionUpdate`.                                                                                                                                                                                                    |

***

The next three sections are detailed reference for `SDKMessage`, `InteractionUpdate`, and `ConversationTurn`. Skim or skip on a first read; [Resuming agents](https://cursor.com/docs/sdk/python.md#resuming-agents) picks up the narrative.

#### Stream events

`run.messages()` yields typed SDK message dataclasses. Discriminate on `message.type`. All messages include `agent_id` and `run_id` when the runtime provides them.

```python
SDKMessage = (
    SDKSystemMessage
    | SDKUserMessageEvent
    | SDKAssistantMessage
    | SDKThinkingMessage
    | SDKToolUseMessage
    | SDKStatusMessage
    | SDKTaskMessage
    | SDKRequestMessage
    | SDKUsageMessage
    | Mapping[str, Any]
)
```

| `type`        | Dataclass             | Key fields                                                                  |
| :------------ | :-------------------- | :-------------------------------------------------------------------------- |
| `"system"`    | `SDKSystemMessage`    | `subtype`, `model`, `tools`                                                 |
| `"user"`      | `SDKUserMessageEvent` | `message.content`                                                           |
| `"assistant"` | `SDKAssistantMessage` | `message.content` with `TextBlock` and `ToolUseBlock` values                |
| `"thinking"`  | `SDKThinkingMessage`  | `text`, `thinking_duration_ms`                                              |
| `"tool_call"` | `SDKToolUseMessage`   | `call_id`, `name`, `status`, `args`, `result`, `truncated`                  |
| `"status"`    | `SDKStatusMessage`    | `status`, `message`                                                         |
| `"task"`      | `SDKTaskMessage`      | `status`, `text`                                                            |
| `"request"`   | `SDKRequestMessage`   | `request_id`                                                                |
| `"usage"`     | `SDKUsageMessage`     | `usage` ([`TokenUsage`](https://cursor.com/docs/sdk/python.md#token-usage)) |

`SDKToolUseMessage` is emitted twice for most tool calls: first with `status="running"` and `args` populated, then again on completion with `status="completed"` (or `"error"`) and `result` populated. `truncated` flags whether the SDK truncated `args` or `result` because the payload was too large.

`SDKUsageMessage` is emitted once at the end of each turn that reported token usage, carrying that turn's [`TokenUsage`](https://cursor.com/docs/sdk/python.md#token-usage). The cumulative total across turns stays on `run.usage` and `result.usage`. See [Token usage](https://cursor.com/docs/sdk/python.md#token-usage).

```python
@dataclass(frozen=True)
class SDKUsageMessage:
    type: Literal["usage"]
    agent_id: str
    run_id: str
    usage: TokenUsage
```

Result data (final text, model, duration, cumulative token usage, git metadata) lives on the `Run` object after the stream completes. Use `run.wait()` to read it, including `result.usage` when the runtime reported it.

> **Tool call schema is not stable.** The `args` and `result` payloads on `tool_call` events reflect each tool's internal shape and can change as tools evolve. Tool names can also be renamed or replaced. Treat `args` and `result` as untyped data and parse defensively. The event envelope (`type`, `call_id`, `name`, `status`) is stable.

`run.events()` yields lower-level `RunStreamEvent` envelopes. Use it when you need offsets, terminal result envelopes, or raw interaction updates:

```python
for event in run.events():
    print(event.kind, event.offset)
```

#### Interaction updates

`InteractionUpdate` is the raw delta type passed to the `on_delta` callback on `agent.send()`. Updates are finer-grained than `SDKMessage` events: text streams in token-by-token and tool calls report partial state as args accumulate.

```python
InteractionUpdate = (
    TextDeltaUpdate
    | ThinkingDeltaUpdate
    | ThinkingCompletedUpdate
    | ToolCallStartedUpdate
    | ToolCallCompletedUpdate
    | PartialToolCallUpdate
    | TokenDeltaUpdate
    | StepStartedUpdate
    | StepCompletedUpdate
    | TurnEndedUpdate
    | UserMessageAppendedUpdate
    | SummaryUpdate
    | SummaryStartedUpdate
    | SummaryCompletedUpdate
    | ShellOutputDeltaUpdate
    | UnknownInteractionUpdate
    | Mapping[str, Any]
)
```

`PartialToolCallUpdate` is emitted as the model streams arguments into a tool call before it commits. The same stability disclaimer that applies to `SDKToolUseMessage.args` applies here.

#### Conversation types

The structured per-turn view of a run, returned by `run.conversation()`. Each item is a wrapper that carries the turn `type` discriminator alongside the typed payload in `turn`.

```python
@dataclass(frozen=True)
class ConversationTurn:
    type: str  # "agentConversationTurn" | "shellConversationTurn"
    turn: AgentConversationTurn | ShellConversationTurn | Mapping[str, Any]

@dataclass(frozen=True)
class AgentConversationTurn:
    user_message: Mapping[str, Any] | None = None
    steps: Sequence[ConversationStep] = ()

@dataclass(frozen=True)
class ShellConversationTurn:
    shell_command: ShellCommand | None = None
    shell_output: ShellOutput | None = None

ConversationStep = (
    AssistantConversationStep
    | ToolCallConversationStep
    | ThinkingConversationStep
    | Mapping[str, Any]
)
```

Discriminate on `turn.type` and read the payload through `turn.turn`:

```python
for turn in run.conversation():
    if turn.type == "agentConversationTurn":
        for step in turn.turn.steps:
            print(step.type)
    elif turn.type == "shellConversationTurn":
        print(turn.turn.shell_command, turn.turn.shell_output)
```

`run.conversation()` from `on_step` callbacks fires per `ConversationStep`, not per turn. Tool-call conversation steps carry a `Mapping[str, Any]` payload. Treat tool-call payload details as untyped data; see the [stability note](https://cursor.com/docs/sdk/python.md#stream-events) under Stream events.

#### Resuming agents

```python
Agent.resume(
    agent_id: str,
    options: AgentOptions | Mapping[str, Any] | None = None,
    *,
    client: CursorClient | None = None,
) -> Agent
```

Use `Agent.resume()` or `client.agents.resume()` to reattach to an existing agent by ID. Common flows: reconnecting to a long-running cloud agent that was kicked off earlier, or continuing a conversation after the local process restarted. Runtime is auto-detected from the ID prefix (`bc-` is cloud, anything else is local).

```python
agent = Agent.resume("bc-abc123")
run = agent.send("Also update the changelog")
run.wait()
```

Async equivalent:

```python
agent = await client.agents.resume("bc-abc123")
run = await agent.send("Also update the changelog")
await run.wait()
```

`agent.model` is `None` on resume unless you pass `model` again. Inline MCP servers are not persisted across resume; they often carry secrets and live in memory only. Pass them again on resume, or use file-based MCP config (`.cursor/mcp.json` plus `local.setting_sources`) for servers that should survive.

When you resume a cloud agent through a caller-supplied bridge (`CursorClient.connect(...)` or `AsyncClient.connect(...)`), the SDK requires an explicit `api_key` so the bridge can authenticate downstream agent calls. Pass it through `AgentOptions`:

```python
from cursor_sdk import AgentOptions

agent = Agent.resume(
    "bc-abc123",
    AgentOptions(api_key="crsr_key"),
    client=client,
)
```

##### Local persistence

Local agents persist conversation state and run metadata through the bridge, so follow-ups and `Agent.resume()` survive a process restart. The bridge keeps this under a per-workspace state root on disk by default. Cloud agents persist server-side, so resuming a cloud agent from anywhere returns the same conversation.

Local persistence is workspace-scoped. When the bridge runs as a long-lived sidecar or subprocess, give it the same workspace as the agent so local list, get, and resume calls resolve the right agents. Set it once on the client and pass `cwd` to the local list and get calls:

```python
from cursor_sdk import CursorClient

with CursorClient.launch_bridge(workspace="/path/to/repo") as client:
    agents = client.agents.list(runtime="local", cwd="/path/to/repo")
    info = client.agents.get(agents.items[0].agent_id, cwd="/path/to/repo")
```

#### Inspecting agents and runs

Use `CursorClient` for list, get, and pagination APIs.

```python
from cursor_sdk import CursorClient

with CursorClient.launch_bridge(workspace=".") as client:
    agents = client.agents.list(runtime="local", cwd=".")

    for agent_info in agents.auto_paging_iter():
        print(agent_info.agent_id)

    info = client.agents.get(agents.items[0].agent_id)
    runs = client.agents.list_runs(info.agent_id)
    run = client.agents.get_run(runs.items[0].id)
```

Async equivalent:

```python
agents = await client.agents.list(runtime="local", cwd=".")

async for agent_info in agents.auto_paging_iter():
    print(agent_info.agent_id)

info = await client.agents.get(agents.items[0].agent_id)
runs = await client.agents.list_runs(info.agent_id)
run = await client.agents.get_run(runs.items[0].id)
```

Use `agent.list_messages()` on an agent handle to read message history. `Agent.messages.list(agent_id)` is a typed-attribute convenience for the same call when you only have an ID.

List endpoints return `ListResult[T]`. Use `.items` and `.next_cursor` directly, iterate the current page with `for item in page`, or iterate all pages with `.auto_paging_iter()`. Async list endpoints return `AsyncListResult[T]`; `async for item in page` walks the current page, and `async for item in page.auto_paging_iter()` walks every page in the result set.

##### SDKAgentInfo

The metadata shape returned by `Agent.list()`, `Agent.get()`, `client.agents.list()`, and `client.agents.get()`.

```python
@dataclass(frozen=True)
class SDKAgentInfo:
    agent_id: str
    name: str
    summary: str
    last_modified: str | None = None
    status: str | None = None  # "running" | "finished" | "error"
    created_at: str | None = None
    archived: bool = False
    runtime: Literal["local", "cloud"] | None = None
    cwd: str = ""
    env: CloudEnvironment | None = None
    repos: Sequence[str] = ()
```

##### Cloud agent lifecycle

Cloud agents stay in your team's workspace until you archive or delete them. `client.agents.list(runtime="cloud")` hides archived agents by default; pass `include_archived=True` to see them. Filter by `pr_url` to find the agent that opened a specific pull request.

```python
# By ID, no agent handle required:
Agent.archive(agent_id)
Agent.unarchive(agent_id)
Agent.delete(agent_id)

# Through an explicit client:
client.agents.archive(agent_id)
client.agents.unarchive(agent_id)
client.agents.delete(agent_id)

# On an existing agent handle:
agent.archive()
agent.unarchive()
agent.delete()
```

`archive` soft-deletes the agent so the transcript stays readable. `unarchive` restores it. `delete` is permanent; subsequent reads return `NotFoundError`.

Async lifecycle methods use the same names and are awaitable.

#### The Cursor namespace

Account-level and catalog reads. Sync methods take optional `api_key` and otherwise fall back to `CURSOR_API_KEY`.

```python
from cursor_sdk import Cursor

me = Cursor.me()
models = Cursor.models.list()
repositories = Cursor.repositories.list()
```

Explicit-client equivalent:

```python
me = client.me()
models = client.models.list()
repositories = client.repositories.list()
```

Async equivalent:

```python
from cursor_sdk import AsyncCursor

me = await AsyncCursor.me(client=client)
models = await AsyncCursor.models.list(client=client)
repositories = await AsyncCursor.repositories.list(client=client)
```

Use `Cursor.models.list()` to discover valid model IDs and per-model parameters before calling `Agent.create()` or `agent.send()`. Parameters are model-specific. Common examples are reasoning effort and context window size.

```python
models = Cursor.models.list()
composer = next((model for model in models if model.id == "composer-2.5"), None)

print(composer.parameters if composer else [])
# [
#   ModelParameterDefinition(
#       id="fast",
#       display_name="Fast",
#       values=(
#           ModelParameterDefinitionValue(value="false"),
#           ModelParameterDefinitionValue(value="true", display_name="Fast"),
#       ),
#   ),
# ]
```

Preset `variants` on each `SDKModel` already contain valid `params`, so you can copy them into a `ModelSelection`.

`Cursor.repositories.list()` returns the SCM repositories (GitHub, GitLab, Bitbucket, Azure DevOps, depending on what's connected) available for cloud agents on the calling account or team. Each item exposes a `url`. Use these to populate `CloudAgentOptions.repos`.

#### MCP servers

Agents can pick up MCP servers from inline definitions, project/user settings, plugins, and dashboard-managed configuration depending on the runtime.

```python
from cursor_sdk import (
    Agent,
    AgentOptions,
    HttpMcpServerConfig,
    LocalAgentOptions,
    McpAuth,
    StdioMcpServerConfig,
)

agent = Agent.create(
    AgentOptions(
        model="composer-2.5",
        local=LocalAgentOptions(cwd="."),
        mcp_servers={
            "docs": HttpMcpServerConfig(
                url="https://example.com/mcp",
                auth=McpAuth(client_id="client-id", scopes=["read", "write"]),
            ),
            "filesystem": StdioMcpServerConfig(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-filesystem", "."],
            ),
        },
    )
)
```

Flat dictionaries (`{"type": "http", "url": ...}` and `{"type": "stdio", "command": ...}`) are also accepted as a quick-script convenience.

##### What gets loaded

**Local agents** load servers from up to five sources, with first-match-wins precedence on conflicting names:

1. `mcp_servers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcp_servers` on `Agent.create()`. Used when no per-send override is provided.
3. Plugin servers, if `local.setting_sources` includes `"plugins"`.
4. Project servers from `.cursor/mcp.json`, if `local.setting_sources` includes `"project"`.
5. User servers from `~/.cursor/mcp.json`, if `local.setting_sources` includes `"user"`.

Without `local.setting_sources`, only inline servers are loaded. If a local MCP server requires OAuth login, the SDK can reuse a saved login from the Cursor app, but it cannot open a browser to sign you in.

**Cloud agents** load servers from:

1. `mcp_servers` on `agent.send()`. Fully replaces creation-time servers for that run (not merged).
2. `mcp_servers` on `Agent.create()`. Used when no per-send override is provided.
3. Your user and team MCP servers from [cursor.com/agents](https://cursor.com/agents).

If an inline server doesn't include `auth` or `headers` and you've previously authorized that server URL on cursor.com/agents, runs authenticated with a personal API token reuse those OAuth tokens automatically. Service account API keys cannot fall back to user auth as they are not associated with a user.

`local.setting_sources` does not apply to cloud agents.

##### Cloud

Cloud agents accept authenticated MCP configs inline too. Cloud MCP supports HTTP and stdio transports. Use HTTP `headers` for static API keys or Bearer tokens. Use HTTP `auth` for OAuth-protected servers. Use stdio `env` when the server runs inside the cloud VM and reads credentials from environment variables.

```python
from cursor_sdk import (
    Agent,
    AgentOptions,
    CloudAgentOptions,
    CloudRepository,
    HttpMcpServerConfig,
    StdioMcpServerConfig,
)

agent = Agent.create(
    AgentOptions(
        model="composer-2.5",
        cloud=CloudAgentOptions(
            repos=[CloudRepository(url="https://github.com/your-org/your-repo")],
        ),
        mcp_servers={
            "linear": HttpMcpServerConfig(
                url="https://mcp.linear.app/mcp",
                headers={"Authorization": "Bearer linear_pat_xxx"},
            ),
            "github": StdioMcpServerConfig(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-github"],
                env={"GITHUB_TOKEN": "ghp_xxx"},
            ),
        },
    )
)
```

- HTTP `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted and do not enter the VM.
- Stdio `env` values are passed into the VM because the server runs there. Treat them like any other runtime secret.
- OAuth for MCP servers configured on cursor.com/agents stays per-user, even for team-level servers.

See [MCP](https://cursor.com/docs/mcp.md) for the full config format and [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools) for cloud-specific behavior.

#### Subagents

Define named subagents that the main agent can spawn via the `Agent` tool. Pass them inline:

```python
from cursor_sdk import Agent, AgentDefinition, AgentOptions, LocalAgentOptions

agent = Agent.create(
    AgentOptions(
        model="composer-2.5",
        local=LocalAgentOptions(cwd="."),
        agents={
            "code-reviewer": AgentDefinition(
                description="Expert code reviewer for quality and security.",
                prompt="Review code for bugs, security issues, and proven approaches.",
                model="inherit",
            ),
            "test-writer": AgentDefinition(
                description="Writes tests for code changes.",
                prompt="Write comprehensive tests for the given code.",
            ),
        },
    )
)
```

Subagents committed to the repo at `.cursor/agents/*.md` (with `name`, `description`, and optional `model` frontmatter) are also picked up. Inline definitions override file-based ones with the same name.

##### Nested subagents

Subagents can spawn their own subagents, within a nesting limit. When a subagent uses the `Agent` tool, it reaches the same subagent executor the parent has, so a parent can delegate to a subagent that delegates further. Each level sees the same set of named subagents. The top-level agent and its direct subagents can launch subagents, but a subagent launched by another subagent can't launch further ones.

#### Custom tools

Custom tools let you expose Python functions to local agents without standing up a separate MCP server. Pass them on `LocalAgentOptions.custom_tools`.

```python
from cursor_sdk import Agent, CustomTool, CustomToolContext, LocalAgentOptions

def get_deployment_status(args, context: CustomToolContext):
    service = args["service"]
    return f"Service {service} is healthy."

with Agent.create(
    model="composer-2.5",
    local=LocalAgentOptions(
        cwd=".",
        custom_tools={
            "get_deployment_status": CustomTool(
                description="Look up the current deployment status for a service.",
                input_schema={
                    "type": "object",
                    "properties": {
                        "service": {"type": "string", "description": "Service name"},
                    },
                    "required": ["service"],
                },
                execute=get_deployment_status,
            ),
        },
    ),
) as agent:
    agent.send("Is the checkout service healthy?").wait()
```

`execute` receives the parsed arguments and a `CustomToolContext` with `tool_call_id` when available. It can return a string, a JSON-compatible value, or a mapping with a `content` list. Custom tools are local agents only.

#### Hooks

Hooks are file-based only. There is no programmatic hook callback. Hooks are a project policy boundary, not a per-run knob.

- **Local:** Add `.cursor/hooks.json` to the repo passed as `local.cwd`, or add `~/.cursor/hooks.json` for user-level hooks.
- **Cloud:** Commit `.cursor/hooks.json` and its scripts to the repo passed in `cloud.repos`. SDK-created cloud agents load project hooks automatically. On Enterprise plans, they also run team hooks and enterprise-managed hooks.

See [Hooks](https://cursor.com/docs/hooks.md) for the configuration format and [Cloud Agents hooks support](https://cursor.com/docs/cloud-agent.md#hooks-support) for cloud behavior.

#### Artifacts

List and download files from the agent's workspace.

```python
@dataclass(frozen=True)
class SDKArtifact:
    path: str
    size_bytes: int = 0
    updated_at: str = ""
```

```python
from pathlib import Path

artifacts = agent.list_artifacts()

for artifact in artifacts:
    print(artifact.path, artifact.size_bytes)

# Download a single artifact to disk.
content = agent.download_artifact(artifacts[0].path)
Path("review.md").write_bytes(content)
```

Async agents expose `await agent.list_artifacts()` and `await agent.download_artifact(path)`.

Artifact support is runtime-dependent. Local SDK agents return an empty list from `list_artifacts()` and raise from `download_artifact()`.

#### Resource management

Always close agents when done. The cleanest sync pattern is a context manager:

```python
from cursor_sdk import Agent, LocalAgentOptions

with Agent.create(model="composer-2.5", local=LocalAgentOptions(cwd=".")) as agent:
    agent.send("Summarize the repository").wait()
```

To dispose explicitly:

```python
agent.close()
```

Async agents and clients support async context managers and `await` cleanup:

```python
from cursor_sdk import AsyncClient, LocalAgentOptions

async with await AsyncClient.launch_bridge(workspace=".") as client:
    async with await client.agents.create(
        model="composer-2.5",
        local=LocalAgentOptions(cwd="."),
    ) as agent:
        run = await agent.send("Summarize the repository")
        await run.wait()
```

To dispose explicitly:

```python
await agent.close()
await client.aclose()
```

The module-level sync default client is closed automatically at process exit. Long-running processes can close and reset it explicitly:

```python
from cursor_sdk import close_default_client

close_default_client()
```

#### Configuration reference

The Python SDK accepts helper dataclasses and raw dictionaries. Dataclasses use Python `snake_case` fields and are preferred for application code.

##### AgentOptions

| Property          | Type                                                 | Default                                                             | Description                                                                                                                            |
| :---------------- | :--------------------------------------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| `model`           | `str \| ModelSelection \| Mapping[str, Any]`         | Required for local; cloud falls back to the server-resolved default | Model to use. See [`ModelSelection`](https://cursor.com/docs/sdk/python.md#modelselection).                                            |
| `api_key`         | `str`                                                | `CURSOR_API_KEY` env                                                | User API key or service account key. Team Admin keys are not yet supported.                                                            |
| `name`            | `str`                                                | Auto-generated                                                      | Human-readable agent name surfaced in `client.agents.list()` / `client.agents.get()`.                                                  |
| `local`           | `LocalAgentOptions \| Mapping[str, Any]`             | `None`                                                              | Local agent config. Pass to create a local agent.                                                                                      |
| `cloud`           | `CloudAgentOptions \| Mapping[str, Any]`             | `None`                                                              | Cloud agent config. Pass to create a cloud agent.                                                                                      |
| `mcp_servers`     | `Mapping[str, McpServerConfig]`                      | `None`                                                              | Inline MCP server definitions.                                                                                                         |
| `agents`          | `Mapping[str, AgentDefinition \| Mapping[str, Any]]` | `None`                                                              | Subagent definitions.                                                                                                                  |
| `agent_id`        | `str`                                                | Auto-generated                                                      | Durable agent ID. Pass to keep a stable ID across invocations.                                                                         |
| `idempotency_key` | `str`                                                | Auto-generated for cloud                                            | Optional client-generated idempotency key. Cloud only.                                                                                 |
| `mode`            | `"agent" \| "plan"`                                  | `"agent"`                                                           | Initial conversation mode for the agent's first run. See [Conversation mode](https://cursor.com/docs/sdk/python.md#conversation-mode). |

##### LocalAgentOptions

| Property          | Type                                                 | Default | Description                                                                                 |
| :---------------- | :--------------------------------------------------- | :------ | :------------------------------------------------------------------------------------------ |
| `cwd`             | `str \| os.PathLike \| Sequence[str \| os.PathLike]` | `None`  | Workspace path or paths.                                                                    |
| `setting_sources` | `Sequence[SettingSource]`                            | `None`  | Ambient settings layers: `"project"`, `"user"`, `"team"`, `"mdm"`, `"plugins"`, or `"all"`. |
| `sandbox_options` | `SandboxOptions \| Mapping[str, Any]`                | `None`  | Local sandbox options.                                                                      |
| `store`           | `LocalAgentStoreConfig \| Mapping[str, Any]`         | `None`  | Local store config passed to the bridge.                                                    |
| `auto_review`     | `bool`                                               | `None`  | Route local tool calls through Auto-review when the connected backend supports it.          |
| `custom_tools`    | `Mapping[str, CustomTool \| Mapping[str, Any]]`      | `None`  | [Custom tools](https://cursor.com/docs/sdk/python.md#custom-tools) exposed to local agents. |

##### CloudAgentOptions

| Property                 | Type                                             | Default             | Description                                                                                                                                                                                |
| :----------------------- | :----------------------------------------------- | :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `env`                    | `CloudEnvironment \| Mapping[str, Any]`          | `{ type: "cloud" }` | Execution environment. `cloud` uses Cursor-hosted VMs; `pool` and `machine` target self-hosted workers you run.                                                                            |
| `repos`                  | `Sequence[CloudRepository \| Mapping[str, Any]]` | `None`              | Repositories to clone into the VM. Omit `repos` and leave `env` at the default for a no-repo agent with an empty workspace. Pass `pr_url` on a repo to attach the agent to an existing PR. |
| `work_on_current_branch` | `bool`                                           | `False`             | Push commits to the existing branch instead of a new one.                                                                                                                                  |
| `auto_create_pr`         | `bool`                                           | `False`             | Open a PR when the run finishes.                                                                                                                                                           |
| `skip_reviewer_request`  | `bool`                                           | `False`             | Skip requesting the calling user as a reviewer on the PR.                                                                                                                                  |
| `env_vars`               | `Mapping[str, str]`                              | `None`              | Session-scoped environment variables for cloud agents.                                                                                                                                     |

##### AgentDefinition

| Property      | Type                                                             | Default     | Description                                                                                      |
| :------------ | :--------------------------------------------------------------- | :---------- | :----------------------------------------------------------------------------------------------- |
| `description` | `str`                                                            | *required*  | When to use this subagent. Shown to the parent agent so it knows when to spawn.                  |
| `prompt`      | `str`                                                            | *required*  | System prompt for the subagent.                                                                  |
| `model`       | `str \| ModelSelection \| Mapping[str, Any] \| "inherit"`        | `"inherit"` | Model override. Pass `"inherit"` to use the parent's selection.                                  |
| `mcp_servers` | `Sequence[str \| AgentDefinitionMcpServer \| Mapping[str, Any]]` | `None`      | MCP servers available to this subagent. Names reference servers from the parent's `mcp_servers`. |

##### CustomTool

```python
@dataclass
class CustomTool:
    execute: Callable[[Mapping[str, Any], CustomToolContext], Any]
    description: str | None = None
    input_schema: Mapping[str, Any] | None = None

class CustomToolContext:
    tool_call_id: str | None = None
```

##### ModelSelection

```python
@dataclass(frozen=True)
class ModelSelection:
    id: str
    params: Sequence[ModelParameterValue] = ()

@dataclass(frozen=True)
class ModelParameterValue:
    id: str
    value: str
```

`id` is the model identifier (for example, `"composer-2.5"`). `params` carries per-model parameters such as reasoning effort. Use `Cursor.models.list()` to discover valid IDs, parameter definitions, and preset variants for your account.

##### McpServerConfig

```python
McpServerConfig = (
    HttpMcpServerConfig
    | SseMcpServerConfig
    | StdioMcpServerConfig
    | Mapping[str, Any]
)

@dataclass(frozen=True)
class HttpMcpServerConfig:
    url: str
    type: Literal["http", "sse"] | str = "http"
    headers: Mapping[str, str] | None = None
    auth: McpAuth | Mapping[str, Any] | None = None

@dataclass(frozen=True)
class SseMcpServerConfig(HttpMcpServerConfig):
    type: Literal["sse"] = "sse"

@dataclass(frozen=True)
class StdioMcpServerConfig:
    command: str
    args: Sequence[str] | None = None
    env: Mapping[str, str] | None = None
    cwd: str | os.PathLike | None = None  # local only; cloud rejects this field

@dataclass(frozen=True)
class McpAuth:
    client_id: str
    client_secret: str | None = None
    scopes: Sequence[str] = ()
```

For HTTP servers running in the cloud, `headers` and `auth` are handled by Cursor's backend. Sensitive fields are redacted before the VM sees them. For stdio servers in the cloud, `env` values are passed into the VM (treat them like any runtime secret).

##### UserMessage

```python
@dataclass(frozen=True)
class UserMessage:
    text: str
    images: Sequence[SDKImage | Mapping[str, Any]] | None = None
```

The structured form of `agent.send()`'s message argument. Use it to send images alongside text.

##### SDKImage

```python
@dataclass(frozen=True)
class SDKImage:
    url: str | None = None
    data: str | None = None
    mime_type: str | None = None
    dimension: SDKImageDimension | Mapping[str, Any] | None = None

    @classmethod
    def from_url(cls, url: str, dimension=None) -> SDKImage: ...

    @classmethod
    def from_data(cls, data: bytes | str, mime_type: str, dimension=None) -> SDKImage: ...

    @classmethod
    def url_image(cls, url: str, dimension=None) -> SDKImage: ...

    @classmethod
    def data_image(cls, data: str, mime_type: str, dimension=None) -> SDKImage: ...

    @classmethod
    def from_file(cls, path, *, mime_type=None, dimension=None) -> SDKImage: ...
```

Pass either a remote `url` or base64 `data` with a `mime_type`. `from_data()` accepts bytes or a base64 string. `from_file()` reads a file from disk and base64-encodes it.

##### SettingSource

```python
SettingSource = Literal["project", "user", "team", "mdm", "plugins", "all"]
```

Controls which on-disk settings layers a local agent loads. Cloud agents always load `project`, `team`, and `plugins` and ignore this field.

| Value       | Source                                  |
| :---------- | :-------------------------------------- |
| `"project"` | `.cursor/` in the workspace             |
| `"user"`    | `~/.cursor/`                            |
| `"team"`    | Team settings synced from the dashboard |
| `"mdm"`     | MDM-managed enterprise settings         |
| `"plugins"` | Plugin-provided settings                |
| `"all"`     | Shorthand for all of the above          |

##### ListResult

```python
@dataclass(frozen=True)
class ListResult(Generic[T]):
    items: list[T]
    next_cursor: str = ""

    def to_dict(self) -> dict[str, Any]: ...
    def has_next_page(self) -> bool: ...
    def next_page_info(self) -> dict[str, str]: ...
    def get_next_page(self) -> ListResult[T]: ...
    def auto_paging_iter(self) -> Iterator[T]: ...
```

Returned by `client.agents.list()`, `client.agents.list_runs()`, and `Agent.list()`. `next_cursor` is empty when there are no more pages. Async list endpoints return `AsyncListResult[T]` with awaitable equivalents.

#### Errors

All SDK errors extend `CursorAgentError`. `CursorSDKError` is the backward-compatible alias root for older callers. Use `is_retryable` and `retry_after` to drive retry logic.

```python
class CursorAgentError(Exception):
    message: str
    code: str | None
    status: int | None
    status_code: int | None
    details: list[Mapping[str, Any]]
    is_retryable: bool
    cause: BaseException | None
    request_id: str | None
    headers: Mapping[str, str]
    retry_after: str | None
```

| Error                          | When                                                                                                                    |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| `AuthenticationError`          | Invalid API key or not logged in.                                                                                       |
| `PermissionDeniedError`        | Authenticated caller does not have permission for the requested operation.                                              |
| `RateLimitError`               | Too many requests or usage limits exceeded.                                                                             |
| `ConfigurationError`           | Invalid model, missing required configuration, or bad request parameters.                                               |
| `AgentBusyError`               | Sending a follow-up while the agent already has a run in `CREATING` or `RUNNING` state (HTTP `409`, code `agent_busy`). |
| `BadRequestError`              | Request is malformed.                                                                                                   |
| `IntegrationNotConnectedError` | Creating a cloud agent for a repo whose SCM provider is not connected.                                                  |
| `NetworkError`                 | Service unavailable or network failure.                                                                                 |
| `APITimeoutError`              | Request timed out.                                                                                                      |
| `InternalServerError`          | Cursor service returned a server error.                                                                                 |
| `NotFoundError`                | Requested resource was not found.                                                                                       |
| `UnknownAgentError`            | Agent was not found or cannot be read.                                                                                  |
| `UnsupportedRunOperationError` | Run operation is not supported for the current run state.                                                               |

##### Retrying with backoff

`is_retryable` and `retry_after` drive caller-side retry logic. `retry_after` is an HTTP-style string (seconds, or an HTTP date) supplied by the server when it's set.

```python
import time

from cursor_sdk import Agent, AgentOptions, CursorAgentError, LocalAgentOptions, RateLimitError

for attempt in range(3):
    try:
        result = Agent.prompt(
            "Audit the auth middleware for missing input validation",
            AgentOptions(model="composer-2.5", local=LocalAgentOptions(cwd=".")),
        )
        break
    except RateLimitError as err:
        time.sleep(float(err.retry_after) if err.retry_after else 2**attempt)
    except CursorAgentError as err:
        if not err.is_retryable:
            raise
        time.sleep(2**attempt)
```

Every `CursorAgentError` includes `request_id` when the server returned one. Log it whenever you surface an error so support has a handle on the failure.

##### IntegrationNotConnectedError

```python
class IntegrationNotConnectedError(ConfigurationError):
    provider: str   # e.g. "github", "gitlab", "azuredevops"
    help_url: str   # dashboard link to reconnect
```

Use `help_url` to point the user at the right reconnect flow. New providers may be added without an SDK release.

##### AgentBusyError

Cloud agents allow only one active run at a time. `AgentBusyError` is raised when you call `agent.send()` (or otherwise create a run) while another run on the same agent is still `CREATING` or `RUNNING`.

`is_retryable` is `False`. Retrying immediately will keep failing until the active run reaches a terminal status or you cancel it. Other `409` responses, such as `agent_archived`, raise `ConfigurationError` instead.

Wait for the active run to finish, cancel it with `run.cancel()`, or poll `Agent.list_runs()` before sending again:

```python
from cursor_sdk import Agent, AgentBusyError

agent = Agent.resume("bc-00000000-0000-0000-0000-000000000001")

try:
    agent.send("Also add tests for the auth middleware.")
except AgentBusyError:
    runs = Agent.list_runs(agent.agent_id, {"runtime": "cloud", "limit": 1})
    active = runs.items[0] if runs.items else None
    if active is not None and active.status == "running":
        active.cancel()
    agent.send("Also add tests for the auth middleware.")
```

Local agents do not raise `AgentBusyError`. Pass `local={"force": True}` on `send()` to expire a stuck local run before starting a new one.

##### UnsupportedRunOperationError

```python
class UnsupportedRunOperationError(ConfigurationError):
    operation: str
```

Raised when a `Run` operation is not allowed on the current run. The most common case is `run.cancel()` on a run that's already terminal.

`run.supports(operation)` and `run.unsupported_reason(operation)` report SDK-level capability for an operation name (`"stream"`, `"wait"`, `"cancel"`, `"conversation"`) and do not check run state. Read `run.status` to guard state-sensitive calls.

#### Troubleshooting

Set `CURSOR_SDK_LOG=debug` (or `info`) to attach a stderr handler to the SDK's own logger. The SDK only configures its own `cursor_sdk` logger, so this won't interfere with the host application's logging setup.

```bash
CURSOR_SDK_LOG=debug python my_script.py
```

The bundled bridge binary is installed as `cursor-sdk-bridge` on PATH alongside the package. Run it directly to confirm the build shipped with your wheel:

```bash
cursor-sdk-bridge --help
```

#### Known limitations

- Tool-call payload schemas are intentionally not strongly typed.
- Inline MCP servers are not persisted across `Agent.resume()`. Pass them again on resume if needed.
- Custom tools (`local.custom_tools`) are local agents only.
- Artifact download is not implemented for local agents.
- `local.setting_sources` (and the file-based MCP and subagent paths it gates) does not apply to cloud agents. Cloud always loads `project`, `team`, and `plugins`.
- Hooks are file-based only (`.cursor/hooks.json`). No programmatic callbacks.


---

#### Sitemap

[Overview of all docs pages](https://cursor.com/llms.txt)

---
