# Magic Patterns — Complete Documentation Guide

> Scraped and cleaned from the official Magic Patterns documentation for offline reference and use in NotebookLM.
> Source: https://www.magicpatterns.com/docs/documentation/get-started/introduction
> Total pages: 91
> Compiled: 2026-07-18

---

## Table of Contents

- **Get Started**
  - [Multiple Pages](#multiple-pages)
  - [Import from Website](#import-from-website)
  - [Copy Code as Prompt](#copy-code-as-prompt)
  - [Credits and Plans](#credits-and-plans)
  - [Host on a Custom Domain](#host-on-a-custom-domain)
  - [Download Design as Code](#download-design-as-code)
  - [Common Questions](#common-questions)
  - [Export to Figma](#export-to-figma)
  - [Welcome](#welcome)
  - [Support](#support)
  - [Sync with Github](#sync-with-github)
- **Core Guide**
  - [Building Your First Prototype](#building-your-first-prototype)
  - [Design Systems](#design-systems)
  - [Engineering Handoff](#engineering-handoff)
  - [Importing from Figma](#importing-from-figma)
  - [Improving Your Prompts](#improving-your-prompts)
  - [Introduction](#introduction)
  - [Team Workflows and Sharing](#team-workflows-and-sharing)
- **Editor**
  - [Forking](#forking)
  - [How to Prompt](#how-to-prompt)
  - [Merging Designs](#merging-designs)
  - [Plan Mode](#plan-mode)
  - [Sharing Designs](#sharing-designs)
  - [Templates](#templates)
- **Projects & Canvas**
  - [Creating your first screen](#creating-your-first-screen)
  - [Using the Canvas](#using-the-canvas)
  - [Sharing designs](#sharing-designs)
  - [Navigating](#navigating)
  - [Using Prompt Templates](#using-prompt-templates)
  - [Linking Screens Together](#linking-screens-together)
  - [Using References](#using-references)
- **Design Systems**
  - [Colors](#colors)
  - [Components](#components)
  - [Rules](#rules)
  - [Skills](#skills)
  - [Typography and Icons](#typography-and-icons)
  - [Figma](#figma)
  - [GitHub](#github)
  - [Local Code Folder](#local-code-folder)
  - [NPM Package](#npm-package)
  - [Overview](#overview)
  - [Prompting](#prompting)
  - [Getting Started](#getting-started)
  - [Converting Design Systems](#converting-design-systems)
  - [Detaching Components](#detaching-components)
- **Importing**
  - [Connect to GitHub](#connect-to-github)
  - [Import from Figma](#import-from-figma)
- **Features**
  - [MCP Tools & Workflows](#mcp-tools-workflows)
  - [Overview of MCP](#overview-of-mcp)
  - [Features](#features)
- **Connectors**
  - [Connectors](#connectors)
- **Integrations**
  - [Anthropic](#anthropic)
  - [Collecting Feedback](#collecting-feedback)
  - [EmailJS](#emailjs)
  - [Google Analytics](#google-analytics)
  - [Google Sheets](#google-sheets)
  - [LinkedIn](#linkedin)
  - [Meta Pixel](#meta-pixel)
  - [OpenAI](#openai)
  - [Overview](#overview)
  - [PostHog](#posthog)
  - [Shopify](#shopify)
- **Collaboration**
  - [Inline Comments](#inline-comments)
  - [Live Multiplayer](#live-multiplayer)
  - [Team Workspaces](#team-workspaces)
- **Publishing**
  - [Website Metadata](#website-metadata)
  - [Password Protection](#password-protection)
  - [Custom Publish URL](#custom-publish-url)
- **Exporting**
  - [Integration Skill for AI Agents](#integration-skill-for-ai-agents)
  - [Overview of exporting](#overview-of-exporting)
- **Enterprise**
  - [Not Receiving a Login Code](#not-receiving-a-login-code)
  - [Enterprises](#enterprises)
  - [Security](#security)
  - [SSO, SCIM & Domain Setup](#sso-scim-domain-setup)
- **Troubleshooting**
  - [Troubleshooting](#troubleshooting)
- **Tutorials**
  - [Video Tutorials](#video-tutorials)
- **Changelog / Feature Releases**
  - [Changelog](#changelog)
- **API Reference**
  - [Create a new artifact](#create-a-new-artifact)
  - [Create a design](#create-a-design)
  - [Get the active artifact](#get-the-active-artifact)
  - [Read recent message history](#read-recent-message-history)
  - [Get design status](#get-design-status)
  - [List version history](#list-version-history)
  - [Getting Started](#getting-started)
  - [Health check](#health-check)
  - [List design systems](#list-design-systems)
  - [Publish an artifact](#publish-an-artifact)
  - [Read artifact files](#read-artifact-files)
  - [Resolve a Magic Patterns URL to an editor ID](#resolve-a-magic-patterns-url-to-an-editor-id)
  - [Send a prompt](#send-a-prompt)
  - [Write artifact files](#write-artifact-files)

---

## Get Started

### Multiple Pages
*Build multi-page designs with real routes and dynamic navigation*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/adding-pages

> 💡 **Tip:**
> Every Magic Patterns design is a website under the hood, so it can have as
>   many pages as you want!

#### Creating Interactive Designs

Magic Patterns supports multiple pages within one "design", so the AI can show different views.

If you want the view to exist as a separate page with its own URL path, such as `/settings`, you need to specify that route in your prompt. This tells the system to create a distinct page that reflects real routing behavior and can be accessed independently.

Pages in a design are defined by route paths. When your design is published, these paths become part of your live URL structure. For example, a settings page at `/settings` would be accessible at `www.yourdomain.com/settings`. This lets you simulate full application flows and structure your design around real navigation logic without needing to split across separate files.

#### Creating a New Page

To create a new page in your design, you simply need to describe it in your prompt. You should include the route path, what should be on the page, and how it should be accessed.

```Example Sample Routing Prompt theme={null}
Add a /settings route. The gear icon should take me to that page. The settings page should have a form with input boxes for name, email, and password.
```

#### Screens Tab

> 💡 **Tip:**
> Use Screens when you have many pages and want to edit one without clicking
>   through.


![The Screens view in Magic Patterns showing all pages of a design at once](https://cdn.magicpatterns.com/uploads/fzxBmL3wf1yooi8DWjjkDk/Screens.png)

The Screens tab sits next to Preview and Code at the top of the editor. It shows every view in your design on one canvas.

##### How to use Screens

1. Open your design in the editor.
2. Click the Screens tab.

> 💡 **Tip:**
> Double-click a screen to focus it before you prompt. You can also say "this
>   page" or "the settings screen". Magic Patterns is also "context-aware" and
>   will know which screen you are referring to if you are looking at it.

##### Commenting and Text Annotations on Screens

The Layers sidebar on the left lists every screen in your design and all of your layers. Screens can sit inside "Sections", so related pages stay grouped on the canvas.


![Screens view with the Layers sidebar, sections grouping screens, and a text annotation on the canvas](https://cdn.magicpatterns.com/uploads/jTHsuy4W8JyfRhXNMWvrGA/Ready_for_Dev.png)

* Use the text tool in the bottom toolbar to add free-form notes on the canvas, such as handoff notes like "Ready for Dev."
* Create sections from the toolbar or Layers sidebar, then drag screens into them to keep flows grouped.

> 💡 **Tip:**
> Sections help you organize. Magic Patterns will also intelligently group
>   screens into sections for you.

For more info about comments, see [Inline Comments](/documentation/collaboration/inline-comments).

#### Video Guide

Creating multiple pages is a topic is covered in our video lesson [Improving Your Prompts](/documentation/guide/improving-your-prompts).

### Import from Website
*Get inspiration from any website, then edit with AI*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/chrome-extension

#### Import via URL (Recommended)

With [Agent Mode](/documentation/feature-releases/changelog#2025-12-03), you can now import any website by simply sharing its URL in your prompt. The agent browses the page, captures its design, and uses it as context.

**How it works:**

1. Start a new design or open an existing project
2. In the prompt, include a URL like: `Clone airbnb.com` or `Make a landing page like stripe.com`
3. The agent automatically browses the website and uses it as design inspiration


![Importing a website via URL](https://cdn.magicpatterns.com/static/agent-mode/BrowseWebsite.gif)

This is the fastest way to get design inspiration from any public website.

***

#### Chrome Extension

For more advanced use cases, our [Chrome Extension](https://www.magicpatterns.com/extension) lets you import any website into Magic Patterns — including **localhost** and **authenticated pages** that the agent can't browse directly.

##### When to use the Chrome Extension

* **Localhost** — Import designs from your local development server
* **Authenticated pages** — Import pages behind a login
* **Individual components** — Select and import specific parts of a page, not just the whole thing
* **Storybook** — Import your Storybook components directly

##### Import from Storybook

Storybook is simply a website, so you can use our Chrome Extension to import your Storybook components into Magic Patterns! Simply go to your Storybook and select the preview of the component you want to import. [Install it now](https://www.magicpatterns.com/extension).

#### Chrome Extension Examples

Here's some real examples if you're curious what the final output looks like:

* [Components from Storybook](https://www.magicpatterns.com/imported/50957edf-db98-4931-b860-b1a918b6a33e)
* [Hacker News](https://www.magicpatterns.com/imported/82c60aab-2c36-4ce7-8ad5-b4698d5959e8)
* [Claude Welcome Screen](https://www.magicpatterns.com/imported/aebeaf31-bf7a-477e-bc47-9f79bea61a61)

### Copy Code as Prompt
*Take your Magic Patterns design from idea to production using AI code editors*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/copy-code-as-prompt

#### From Idea to Production in Minutes

One of Magic Patterns' most popular features is the **"Copy code as prompt"**, which enables customers to bring their AI-generated designs into production codebases seamlessly.

##### Why This Workflow is So Powerful

By default, Magic Patterns generates clean, vanilla React code that's ready to use ready to be consumed by tools like Cursor or Claude Code that know your codebase well.

##### How It Works


**Generate Your Design**

    Use Magic Patterns to create your UI components or full pages using natural
    language prompts. Magic Patterns will generate clean, production-ready React
    code.


**Copy Code as Prompt**

    Click the **"Copy code as prompt"** in the export menu. This copies your
    generated code in a format optimized for AI code editors.

![image](https://cdn.magicpatterns.com/assets/copy-code-as-prompt.png)


**Paste into Cursor, Claude Code, or the IDE of your choice**

    Open your project in Cursor, Claude Code, or any AI-powered editor. Paste
    the code and ask the AI to integrate it into your codebase.

> 💡 **Tip:**
> **Having trouble getting the generated code to fit smoothly?** Try using a
>       [Design System with Rules](/documentation/design-systems/editing/rules) to match
>       your codebase conventions. For best results, consider tweaking your IDE's
>       "rules" as well. For example, in Cursor, you can add rules to help it
>       better understand the AI output.

##### Need Help?

Join our community to see how other developers are using this workflow:


- **[Join our Slack](https://www.magicpatterns.com/join-slack-community)** — Share tips and get help from the community


- **[Watch Tutorials](https://www.youtube.com/@magicpatterns)** — See real-world examples of this workflow

### Credits and Plans
*Learn how plans, credits, on-demand usage, and billing work in Magic Patterns.*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/credits-and-billing

Magic Patterns is a subscription-based service with a free tier and several paid plans. Paid plans unlock additional features and include monthly credits that renew automatically. Credits power AI generation features.

#### Plans


- **Starter** — For hobbyists with light use to explore Magic Patterns.


- **Business** — For professionals & product teams building with Magic Patterns.


- **Enterprise** — For large orgs looking to replace their legacy workflows and become AI-native.

##### Plans are by Workspace

By default, everyone works inside a workspace: you always have at least one of your own, and you can join or create more.

Plans in Magic Patterns are applied **at the workspace level**, not to your account as a whole. Billing, credits, and plan features belong to whichever workspace you are using.

You can be a member of multiple workspaces—some may be on paid plans while others are on the free tier. Open the **workspace selector** in the sidebar, choose another workspace, and you switch context; the selector also shows which plan each workspace is on.

![Free vs paid workspace plans](https://cdn.magicpatterns.com/uploads/eSALr9amf929MMkoNoK8Zm/plans-are-by-workspaces.png)

|                                                                              | **Free**    | **Starter**         | **Business**   | **Enterprise** |
| :--------------------------------------------------------------------------- | :---------- | :------------------ | :------------- | :------------- |
| **Price**                                                                    | \$0/seat/mo | \$20/seat/mo        | \$100/seat/mo  | Custom         |
| **Annual price**                                                             | \$0/seat/mo | \$17/seat/mo        | \$85/seat/mo   | Custom         |
| **Monthly credits**                                                          | 100         | 1,000               | 5,000          | Custom         |
| **[Team workspace](/documentation/collaboration/team-workspaces)**           |             | Up to 10 paid seats | 11+ paid seats | 11+ paid seats |
| **[On-Demand Usage](#on-demand-usage)**                                      |             | ✓                   | ✓              | ✓              |
| **[Design systems](/documentation/design-systems/overview)**                 |             | ✓                   | ✓              | ✓              |
| **[No watermark](/documentation/publishing/metadata)**                       |             | ✓                   | ✓              | ✓              |
| **[GitHub sync](/documentation/get-started/sync-to-github)**                 |             | ✓                   | ✓              | ✓              |
| **[Magic Patterns MCP](/documentation/features/mcp-server/overview)**        |             | ✓                   | ✓              | ✓              |
| **Centralized billing**                                                      |             | ✓                   | ✓              | ✓              |
| **Faster AI models**                                                         |             |                     | ✓              | ✓              |
| **[Self-serve SSO](/documentation/enterprise/sso-scim-setup)**               |             |                     | ✓              | ✓              |
| **[User roles & permissions](/documentation/collaboration/team-workspaces)** |             |                     | ✓              | ✓              |
| **Usage reporting**                                                          |             |                     | ✓              | ✓              |
| **Shared credit pooling**                                                    |             |                     |                | ✓              |
| **[SCIM & audit logs](/documentation/enterprise/sso-scim-setup)**            |             |                     |                | ✓              |
| **Technical account manager**                                                |             |                     |                | ✓              |
| **Priority support**                                                         |             |                     |                | ✓              |
| **Custom contracts**                                                         |             |                     |                | ✓              |
| **Flexible invoicing**                                                       |             |                     |                | ✓              |

***

#### Credits

> 💡 **Tip:**
> Features like "Fix with AI" and all non-AI actions (e.g., manual edits,
>   exports, sharing) do not consume credits. Only direct AI generations count.

Credits are consumed when you use AI generation features. Cost scales with the complexity of the task.

##### Predictability

We researched credit usage across many real designs so you can estimate session costs before you start. The table below shows average credits by how many iterations a design goes through.

| Versions | Avg credits | Avg credits/version |
| -------- | ----------: | ------------------: |
| 1        |          27 |                  27 |
| 2–3      |          66 |                  28 |
| 4–5      |         107 |                  24 |
| 6–10     |         179 |                  24 |
| 11–20    |         340 |                  23 |
| 21–50    |         641 |                  20 |
| 51–100   |         975 |                  14 |
| 100+     |       2,500 |                  11 |

A single generation costs roughly **25 credits**. A small prototype with 6–10 iterations lands around **180 credits**, and a larger project with 21–50 iterations averages about **600 credits**. The more you iterate, the cheaper each additional version becomes: longer sessions consist mostly of small, incremental edits rather than full regenerations.

These numbers reflect usage with Claude Opus 4.6 (a highly capable, higher-cost model). Model choice affects credit spend, but cheaper is not always less: a weaker model that needs several retries to get a change right can cost more than a capable model that gets it right the first time. See [Choosing the Right Model](#choosing-the-right-model).

##### Viewing Credit Consumption

> 💡 **Tip:**
> There's no way to predict exactly how many credits a request will use before
>   it runs: it depends on the complexity of the task and the model's response.
>   The best approach is to make targeted, specific changes when possible,
>   especially when using faster models.

After each AI generation, you can see exactly how many credits were consumed and which model was used. The summary appears at the bottom of the AI response in the chat, showing credits used, tool calls, lines changed, and the model used—helping you understand usage in real time.

![Credit spend per prompt and model used](https://cdn.magicpatterns.com/uploads/1SdtMkkV4bEHmCcdgHzWrc/credits-used.png)

##### Choosing the Right Model

You can select which AI model to use for each generation using the model picker. Different models have different strengths and credit costs: hover over each option to see how they compare.

![Model Picker](https://cdn.magicpatterns.com/uploads/ix4iL7te4QLwrzHRwNvqFZ/model-picker.png)

**We highly recommend Auto.** Auto automatically picks the best model for your task and consistently produces the highest-quality results. If you are not sure which model to use, use Auto. It is the right default for almost everything.

**For complex or high-stakes work, GPT-5.6 is an excellent choice.** It handles sophisticated UI problems, larger creative tasks, and multi-step changes with strong reliability.

> ⚠️ **Warning:**
> **Cheaper is not always cheaper.** Faster, lower-cost models are tempting
>   because they use fewer credits per generation, but they tend to produce
>   lower-quality results. When a weaker model gets a change wrong, you end up
>   re-prompting, regenerating, and cleaning up its output, which burns **more**
>   credits overall than using a capable model once. Reaching for the cheapest
>   option to save credits frequently costs you more.

The key is matching the model to the task, and defaulting to Auto when in doubt.

##### Managing Conversation Context

Each follow-up prompt carries the earlier conversation along as context, which adds to the credits a generation uses. Magic Patterns manages this context automatically, so you usually don't need to think about it. If you want more control, two commands let you trim the context yourself:

* **`/Clear`** — resets the current conversation context without needing to fork the design. Use it when you start an unrelated task on the same design.
* **`/Summarize`** — condenses the conversation so far, preserving the important details while freeing up context.

Both keep the context smaller, which keeps the agent focused and lowers per-generation credit costs. See [How to Prompt](/documentation/editor/how-to-prompt) for the full command list.

##### Monthly Refresh Cycle

* **Monthly plans:** Credits renew when your invoice is paid (when Stripe successfully charges your payment method).
* **Annual plans:** Credits renew at 2:00 AM UTC on the day after your billing date. The exact local time depends on your timezone (e.g., \~7:00 PM PST or 2:00 AM the next day in London).
* Subscription changes are captured and applied before credits refresh.

##### Credit Rollover

We believe rollovers are only fair! Unused monthly credits roll over to the next month and expire after 1 month.

***

#### On-Demand Usage

![On-demand usage settings](https://cdn.magicpatterns.com/uploads/g1EkK1tVefn8PMk2gs6wpu/new-on-demand-feature.png)

On-Demand Usage lets you keep generating after your monthly credits run out, with pay-as-you-go billing. It is only available on paid plans (Starter, Business, Enterprise).

##### How it works

1. Be on a paid plan (Starter, Business, or Enterprise).
2. Go to [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription), click Manage Plan, and enable On-Demand Usage.
3. When your monthly credits run out, you keep generating. Each additional credit costs \$0.02 with pay-as-you-go billing on your next invoice.

##### Budget Alerts

> 💡 **Tip:**
> Any usage beyond your monthly credit limit will be billed at a fixed
>   per-credit rate with pay-as-you-go billing. No plan upgrades required. You can
>   additionally set up budget limits and alert thresholds to make sure you stay
>   within your budget.

![Budget limit settings](https://cdn.magicpatterns.com/static/docs/budget-limit-on-demand-usage.png)

If you're on a paid plan with On-Demand Usage enabled, you can set budget limits and alert thresholds at [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription). When your on-demand spending reaches an alert threshold, Magic Patterns shows a banner in the editor near the chat prompt with a link to manage your budget; you can dismiss the banner after you have reviewed it.

***

#### Billing

##### Where to manage billing

![Subscription and billing settings](https://cdn.magicpatterns.com/uploads/g1EkK1tVefn8PMk2gs6wpu/new-on-demand-feature.png)

Go to [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription) to manage your plan, enable On-Demand Usage, set spending limits, and download invoices. This page works for both workspace and individual plans.

##### Invoices

Download past invoices as PDF from [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription).

***

#### Teams

##### Team workspace tiers

All paid members must be on the same plan tier. If your workspace has 11 or more paid seats, it requires the Business or Enterprise plan. Free seats can always be added to any workspace at no cost.

##### Managing your team

Go to [magicpatterns.com/settings/team](https://www.magicpatterns.com/settings/team) to add or remove seats, manage team members, and upgrade or downgrade users. Use this if you're an admin managing your workspace. For more details on setting up and managing team workspaces, see the [Team Workspaces](/documentation/collaboration/team-workspaces) page.

***

#### FAQ


**Can I switch plans anytime?**

    Yes. Upgrades are immediate with prorated billing. Downgrades take effect at
    your next billing cycle.


**What counts as a credit?**

    Any AI generation action: prompting, agent mode, component generation. Cost
    scales with complexity (input/output tokens). "Fix" commands and manual
    edits are free. Most designs use around 30–100 credits total.


**Do credits expire?**

    Rolled-over credits expire one month after they're added.


**What happens to my projects if I downgrade or cancel?**

    Projects and code are never deleted. You lose access to plan-specific
    features but can still view, edit, and export your work.


**Can I get a refund?**

    Contact [support@magicpatterns.com](mailto:support@magicpatterns.com) for
    refund requests.


**How do I download invoices?**

    Download past invoices from
    [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription).


**Can I set a spending limit on On-Demand Usage?**

    Yes, if you're on a paid plan with [On-Demand Usage](#on-demand-usage)
    enabled. Set budget limits and alert thresholds at
    [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription).

### Host on a Custom Domain
*Connect your own domain to your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/custom-domain

> 💡 **Tip:**
> Don't own a domain yet? Use a [Custom Publish
>   URL](/documentation/publishing/publish-url) to publish instantly without any
>   setup.

#### How to Connect Your Domain

##### First, buy your domain

You must own your domain, usually purchased from a domain registrar. There are many domain registrars, but examples include: Namecheap, GoDaddy, Squarespace, Cloudflare, etc.

Once you own your domain:


**Click the Share button**

    Click the Share button at the top of the editor.


![Share button location](https://cdn.magicpatterns.com/uploads/76cgXyEJT44j7XbeLX88Fz/share-button.png)




**Open the Publish modal**

    In the Share menu, open the Publish modal.


![Publish modal](https://cdn.magicpatterns.com/uploads/q3C7SdUup4UVNmw56tjiNA/publish-modal.png)




**Add a custom domain**

    At the bottom of the Publish modal, click "Add a custom domain".


![Custom domain section](https://cdn.magicpatterns.com/uploads/4msL3sjhiRDRppoZcTFPZU/custom-domain.png)




**Add your DNS records**

    Go to your domain registrar (GoDaddy, Namecheap, Cloudflare, etc.) and find DNS settings (usually under "DNS Management" or "Advanced DNS").

    Follow the instructions below for your domain type:

    **For a root domain** (`example.com`):

> ⚠️ **Warning:**
> First, delete ALL existing A records for your domain. If you skip this step, your domain won't work.

    Add an A record with these settings:

    | TYPE | NAME | VALUE           |
    | ---- | ---- | --------------- |
    | A    | @    | 149.248.202.188 |

    The @ symbol means "root domain". In some registrars (like Wix), "@" is entered as a blank space.

    **For a subdomain** (`www.example.com`, `blog.example.com`):

    Add a CNAME record with these settings:

    | TYPE  | NAME | VALUE             |
    | ----- | ---- | ----------------- |
    | CNAME | www  | magicpatterns.dev |

    Replace `www` with your subdomain. For example, use `blog` for `blog.example.com` or `app` for `app.example.com`.

    In other words, if you want to connect `blog.example.com`, you would add:

    | TYPE  | NAME | VALUE             |
    | ----- | ---- | ----------------- |
    | CNAME | blog | magicpatterns.dev |


**Wait for DNS Propagation**

    DNS changes can take 5 minutes to 48 hours to propagate globally.

    **Check if it's ready:**

    * **For root domains:** Go to [whatsmydns.net/A](https://www.whatsmydns.net/?t=A), enter your domain, and check that it shows `149.248.202.188`
    * **For subdomains:** Go to [whatsmydns.net/CNAME](https://www.whatsmydns.net/?t=CNAME), enter your subdomain, and check that it shows `magicpatterns.dev`


**Connect Domain in Magic Patterns**

    Once DNS has propagated:

    1. Enter your domain name in Magic Patterns (e.g., `example.com` or `www.example.com`)
    2. Click "I have added DNS records"
    3. Wait for verification

    **Root Domain:**


![Root domain DNS settings](https://cdn.magicpatterns.com/static/docs/root-domain.png)

    **Subdomain:**


![Subdomain DNS settings](https://cdn.magicpatterns.com/static/docs/subdomain.png)




**Manage your published site**

    Once verified, you can manage your settings by clicking on the Publish button again.

    From here, you can also publish another version of your design.

#### Connecting Multiple Domains

You can connect multiple domains to the same project. For example, you might want both:

* `example.com` (root domain)
* `www.example.com` (subdomain)

Simply add both DNS records and connect each domain in Magic Patterns using the "+" button in the Publish panel.


![Multiple domains](https://cdn.magicpatterns.com/uploads/61QMTCc551n4itVTRJdf7h/multiple-domains.png)

#### FAQ and Troubleshooting

Be sure to refresh or try a different browser or device if you just published your domain! Your browser will cache old versions!


**My domain isn't working after 24 hours. What should I check?**

    Check these common issues:

    1. **For root domains:** Did you delete ALL old A records? (most common issue)
    2. Check your DNS at whatsmydns.net:
       * For root domains: [Check A record](https://www.whatsmydns.net/?t=A) — should show `149.248.202.188`
       * For subdomains: [Check CNAME record](https://www.whatsmydns.net/?t=CNAME) — should show `magicpatterns.dev`
       * If it shows something different or "No record found", your DNS isn't set up correctly
    3. Wait another few hours if changes were recent


**My subdomain (www, blog, etc.) doesn't work**

    Make sure you added a CNAME record (not an A record) for your subdomain:

    | TYPE  | NAME | VALUE             |
    | ----- | ---- | ----------------- |
    | CNAME | www  | magicpatterns.dev |

    Replace `www` with your subdomain (e.g., `blog`, `app`, `portfolio`).

    You can verify it's set up correctly at [whatsmydns.net/CNAME](https://www.whatsmydns.net/?t=CNAME) by entering your subdomain.


**When should I use an A record vs a CNAME record?**

    * Use an **A record** for root domains (`example.com`) - Use a **CNAME
      record** for subdomains (`www.example.com`, `blog.example.com`) The Publish
      panel in Magic Patterns will show you exactly which record type to use based
      on whether you select "Root Domain" or "Subdomain".


**Which DNS providers work with Magic Patterns?**

    Magic Patterns works with ALL DNS providers including GoDaddy, Namecheap,
    Cloudflare, Google Domains, Squarespace, Wix, and any other provider.


**How long does DNS propagation take?**

    DNS propagation typically takes between 30 minutes and 48 hours, depending on
    your DNS provider and various internet factors. Most domains are verified
    within a few hours.


**How do I disconnect my custom domain?**

    You can disconnect your custom domain by clicking on the domain in the Publish
    panel and selecting "Disconnect".


**Will my site have HTTPS?**

    Yes! We automatically provision SSL certificates for all custom domains to
    ensure your site is secure.


**How do I remove the 'Built with Magic Patterns' badge?**

    [Upgrade to a paid plan](https://www.magicpatterns.com/dashboard?dl=billing)
    to remove the "Built with Magic Patterns" badge under the Metadata tab in the
    Publish panel.


**Why am I still seeing the old version of my site?**

    Your browser is likely caching the old version of your site. Try clearing your cache or opening it in incognito mode to see the latest updates.

### Download Design as Code
*To download a `.zip` of all the code, click the Export button in the top right corner of the screen*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/download-code

![Download Code](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/exporting/images/download-code.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=24192935b10def6bd71aaa6bcb739fd6)

### Common Questions
*Frequently Asked Questions about Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/faq

**What is Magic Patterns?**

    Magic Patterns generates a functional web application that matches your existing product and allows you to explore new ideas in minutes. We offer features like using your own [design system](/documentation/design-systems/overview) and existing designs, sharing with teammates, password protection, and more.


**How do customers use Magic Patterns?**

    We support large enterprises and fast-moving startups. Check out our [customer showcase](https://www.magicpatterns.com/customers) to see how our users are using Magic Patterns.
    For example, read how [Luthor is winning more deals](https://www.magicpatterns.com/customers/luthor) by creating demos with our Chrome Extension.


**Do you have SOC 2?**

    Yes, we support many enterprises and are SOC 2 and ISO 27001 compliant. You can access our reports in our [Trust Center](https://trust.magicpatterns.com/).


**How can I cancel my plan?**

    {`You can cancel your plan at any time. Once logged in, navigate to the "Billing & Subscription" option in the account dropdown (by clicking on your profile picture) and then click "Manage." If you need any help, please do not hesitate to contact us at support@magicpatterns.com. We want you to have a good experience!`}


**How do credits refresh and how can I check my balance?**

    Credits renew automatically each month. On monthly plans, renewal happens when
    your invoice is paid. On annual plans, renewal happens at 2:00 AM UTC on the
    day after your billing date (e.g., \~7:00 PM PST if you're in San Francisco).
    For more details on credit timing and how to view your credits history, see
    our [Credits and Billing
    guide](/documentation/get-started/credits-and-billing).


**Which models do you use?**

    We use Anthropic's Claude models (Sonnet 4.6, Opus 4.8, and Fable 5),
    Google's Gemini models, and OpenAI's GPT models (GPT 5.4 mini) to generate
    designs.


**What counts as a credit?**

    Credits are consumed when you use AI generation features (prompting, agent
    mode, component generation). Cost scales with complexity. "Fix with AI" and
    manual edits do not consume credits. See our [Credits and Billing
    guide](/documentation/get-started/credits-and-billing) for details.


**Where is data stored?**

    Data is stored in the United States. Specifically, our primary database is
    hosted on AWS. We are a Delaware C-corp, based in San Francisco, California,
    United States.


**What's the difference between Components and Designs?**

    Designs are individual projects you create (like a landing page). Components
    are reusable UI elements (like a custom button used on that landing page) that
    are part of a [design system](/documentation/design-systems/overview). Design
    Systems are collections of styling rules and components that ensure
    consistency across your designs (like "Acme Design System").


**How do I set up a custom domain?**

    Every Magic Patterns design is a website, so you can host it on any domain you
    own! See our [Custom Domain guide](/documentation/get-started/custom-domain)
    for full instructions.


**How do I use custom components in my designs?**

    There are two ways:  1. **Automatic**: Create a [Design
    System](/documentation/design-systems/overview) and add your components to it.
    When you create designs using that Design System, components are used
    automatically.  2. **Manual**: Type `@ComponentName` in any design to
    reference a specific component.   [Learn more about using
    components](/documentation/design-systems/editing/components)


**What is your #1 tip for getting accurate results?**

    Use [Select
    Mode](/documentation/editor/how-to-prompt#select-mode-and-visual-edit)!


**The AI keeps making the same mistake. What do I do?**

    Try the [/Debug skill](/documentation/editor/how-to-prompt#debug) and
    check out our [Troubleshooting guide](/documentation/troubleshooting/overview)


**How do I access the Canvas, so that I can organize all my designs?**

    There are two ways: 1. From an existing design: Click the button next to the
    title in the top nav bar and select "Add to Canvas" 2. From the dashboard:
    Click the "Canvas" tab to see all your canvases.   [Learn more
    about your Magic Patterns Canvas](/documentation/projects/getting-started)!


**I asked for a change but don't see it on my design. Why?**

    The AI likely made the change, but it's not "hooked up" or it's on a different
    page. Quick fix: Ask the AI: "I don't see my changes. Can you explain what you
    did and where I should look?" Common reasons include: the AI created a new
    page but didn't link a button to it, the change is on a different route or
    it's in a modal or hidden state you need to trigger. [Learn more
    troubleshooting
    tips](/documentation/troubleshooting/overview#i-dont-see-my-changes).


**What does 'Fork' mean and how do I use it?**

    Fork means create a copy of your design. It's great for new ideas or
    collaboration! [Learn more about forking](/documentation/editor/forking)!


**I'm interested in your API. What's your API pricing?**

    For the [Magic Patterns API](/api/getting-started), usage draws
    from your normal Magic Patterns credit balance — the same credits the web app
    and MCP use. There is no separate API subscription.

### Export to Figma
*Generate designs and then export them to Figma*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/figma-plugin

##### Steps

You can export your Magic Patterns design to Figma within seconds.


**Generate a design and click on export in the top right corner. Then 'Export to Figma'.**

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/images/figma/1.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=16b002ccfc8d919eafbfbbf861f0d7c2)


**Once it's done preparing, click 'Copy' to copy the data onto your clipboard.**

![image](https://cdn.magicpatterns.com/uploads/88wZdYLJkx3dKusBmDTi3M/export-to-figma-copy.png)



> 💡 **Tip:**
> You can also use the hotkey "Option + F" to export to Figma.

#### Exporting Tips

##### Export a Design for Mobile

Magic Patterns designs are generally responsive by default. To export the mobile view to Figma:

1. First, switch to mobile view in Magic Patterns by clicking the device selector in the top bar and choosing **iPhone 17 / 17 Pro** (or your preferred mobile device)
2. Then export to Figma as normal by clicking "Export to Figma" in the menu

![image](https://cdn.magicpatterns.com/assets/Mobile-Figma.gif)

> ⚠️ **Warning:**
> **Important:** Always set the view you want to export BEFORE exporting.
>   Whatever you see in Magic Patterns is what will be exported to Figma.

##### Exporting Different States

Magic Patterns captures a static snapshot of what you currently see when you export to Figma. This means:

* For different screens: Navigate to the specific screen in your prototype first, then export
* For dropdown menus or modals: Open the menu/modal in Magic Patterns, then export
* For hover states or interactions: Trigger the state you want to capture, then export
* For responsive designs: Switch to the device size you want (mobile, tablet, desktop), then export

> 💡 **Tip:**
> **Remember:** What you see is what you get. If you want to export a menu in
>   its open state, make sure it's open before clicking export.

##### Exporting Multiple Designs into Figma

You can export multiple screens at once by using the canvas feature:

#### Troubleshooting

##### Why Designs Lose Interactivity in Figma

When you export from Magic Patterns to Figma, the design is converted into a static snapshot of the current code. Magic Patterns is powered by code, which allows for interactivity such as routing, hover states, and dynamic behavior. Figma, on the other hand, uses a visual data model based on vector graphics and layout primitives.

As a result, interactivity does not carry over. You’ll retain layout, styling, and structure, but the design will behave as a static series of “Figma layers” rather than an interactive interface.

##### Output Is Not What You Expect

If you're struggling with the Figma export or the output doesn't match what you see in Magic Patterns, you can try using [html.to.design](https://www.figma.com/community/plugin/1159123024924461424/html-to-design) as an alternative. It's a Figma plugin that converts any webpage into Figma layers, and can sometimes produce better results depending on your use case.


**Get your Publish URL**

    Use the Publish button in the editor to get a live URL for your design. See
    [Publish URL](/documentation/publishing/publish-url) for details.





#### Video Guide

This topic is covered in our video lesson [Figma Imports](/documentation/guide/figma-imports).

### Welcome
*Magic Patterns is an AI design tool for product teams. Use it to create prototypes using your real design system, handoff to engineering, and speed up your software development lifecycle.*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/introduction

#### Who Magic Patterns is for

* **Product managers** — Keep work anchored to your [design system](/documentation/design-systems/overview) while you ship interactive prototypes quickly, gate previews with [password protection](/documentation/publishing/password-protection), and reuse flows from [templates](/documentation/editor/templates).
* **Designers** — Build on the [canvas](/documentation/projects/getting-started) with your [design system](/documentation/design-systems/overview), and [import from Figma](/documentation/importing/import-from-figma) to stay aligned with your design files.
* **Engineers** — Connect Magic Patterns to your toolchain with the [MCP server](/documentation/features/mcp-server/overview) and [our tools](/documentation/features/mcp-server/available_tools) for roundtrip design and code.
* **Marketing, sales, website builders** — [Share](/documentation/editor/sharing) polished previews with customers and stakeholders, including [published URLs](/documentation/publishing/publish-url) and [hosting on a custom domain](/documentation/get-started/custom-domain).

#### Getting Started

Open [magicpatterns.com](https://www.magicpatterns.com/), describe the screen or flow you want, and refine from there. Upload a screenshot when you have one.

When you are ready to go deeper: read [how to prompt](/documentation/editor/how-to-prompt), using your real [design system](/documentation/design-systems/overview), [team workspaces](/documentation/collaboration/team-workspaces), and [engineering handoff with our MCP server](/documentation/features/mcp-server/overview) are all documented here.


- **[Credits and Plans](/documentation/get-started/credits-and-billing)** — Understand plans, credits, on-demand usage, and billing.


- **[How to Prompt](/documentation/editor/how-to-prompt)** — Write prompts that produce clearer UI and fewer rework cycles.


- **[Canvas](/documentation/projects/getting-started)** — Organize designs and collaborate in one place.


- **[Video Tutorials](/documentation/tutorials/video-tutorials)** — Watch walkthroughs and short tutorials at your own pace.

### Support
*How to get help with Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/support

We're here to help you get the most out of Magic Patterns! Support options vary by plan to ensure you get the right level of assistance.

#### Free Plan


**Email Support**

    Free users can reach out to our support team via email at
    [support@magicpatterns.com](mailto:support@magicpatterns.com). We aim to
    respond within 1-2 business days.


**In-App Chat**

    Use the chat widget in the bottom-right corner of the app to message our
    support team directly. We're available during business hours to help answer
    questions.


**Slack Community**

    Join our free [Slack
    community](https://www.magicpatterns.com/join-slack-community) to connect
    with other Magic Patterns users, share tips, ask questions, and get help
    from the community.

#### Business Plan


**All Free Plan Benefits**

    Business plan users have access to all support channels available on the
    Free plan, including email support, in-app chat, and the Slack community.


**Dedicated Slack or Microsoft Teams Channel**

    Business plan subscribers can request a dedicated Slack or Microsoft Teams
    channel for direct communication with the Magic Patterns team. This provides
    faster response times and personalized support for your team. **To request a
    channel:** 1. Go to **Settings** in your Magic Patterns dashboard 2.
    Navigate to the **Support** section 3. Enter your email and choose whether
    you'd like a Slack or Microsoft Teams channel Our team will set up your
    dedicated channel within 1 business day.

#### Enterprise Plan


**All Business Plan Benefits**

    Enterprise plan users have access to all support channels available on the Business plan.


**Dedicated Slack or Microsoft Teams Channel**

    Enterprise customers receive a dedicated Slack or Microsoft Teams channel for direct, real-time communication with our team. This channel is set up automatically as part of your onboarding.

    If you haven't received your channel invite yet, you can request one from **Settings > Support** in your dashboard.


**Priority Support**

    Enterprise customers receive priority support with faster response times and dedicated account management.


**Technical Account Manager**

    Enterprise customers can opt to have a dedicated Technical Account Manager (TAM) included as part of their plan. Your TAM serves as a strategic partner, helping with onboarding, best practices, technical guidance, and ongoing success with Magic Patterns.

    To request a Technical Account Manager, reach out to your account contact or email [support@magicpatterns.com](mailto:support@magicpatterns.com).

#### Quick Links


- **[Email Support](mailto:support@magicpatterns.com)** — Reach out via email for any questions or issues.


- **[Slack Community](https://www.magicpatterns.com/join-slack-community)** — Join our free community for tips and help.


- **[FAQ](/documentation/get-started/faq)** — Find answers to common questions.


- **[Troubleshooting](/documentation/troubleshooting/overview)** — Solve common issues with our guides.

### Sync with Github
*Generate designs and then sync them with Github*

**Source:** https://www.magicpatterns.com/docs/documentation/get-started/sync-to-github

> ℹ️ **Note:**
> Sync with Github requires a paid plan. [Upgrade
>   here](https://www.magicpatterns.com/dashboard?dl=billing).

Export your design to a Github code repository. This is a great way to either hand off a design to a developer or bring Magic Patterns designs into your code editor, like Cursor.

> ℹ️ **Info:**
> Sync with Github creates a **new repository** in your selected organization. You can then clone this repo and continue development in your preferred environment.

You'll be able to pull new changes from Github to continue working on them with Magic Patterns.

It is a two-way sync.

##### Steps

You can sync your Magic Patterns design to and from Github with a few easy steps.


**Open the Github panel**

    Generate a design and click on the Github icon at the top of the code tab.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/images/github/github-icon.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=aecca822405c9af1589996c616d766e1)


**Install Magic Patterns Github App**

    If it's your first time syncing to Github, you'll be asked to install the Magic
    Patterns Github app. Click 'Install Github App' to continue.


**Authorize the Magic Patterns Github App**

    Follow the instructions to install the app. Pick the organization where you
    want to create the new repository. The Github app will request the necessary
    permissions.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/images/github/install-and-authorize.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=5b93a2ae86e406268f0a63c7ea311705)


**Within Magic Patterns, chose a new repository name**

    Once the app is installed and authorized, you will automatically be
    brought back to Magic Patterns. In the Github panel, you will see the
    available organizations you can create the new repository in.

    Once you select an organization, the new repository will be created.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/images/github/pick-organization.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=1e276c87775f77eaf0b8a8cde2461da5)


**Two-way Sync**

    If you have many edits in Magic Patterns you want to sync new changes, simply click export to Github again in the top right corner and then "sync." Similarly, if you have many edits in Github you want to sync back to Magic Patterns, simply click "sync" in the Github panel.

![image](https://cdn.magicpatterns.com/assets/no-padding-github-sync.gif)

##### FAQ


**Can I export to a different code framework?**

    We currently support exporting to a React + Vite code template. More
    customizations are coming soon (let us know what you want to see). We chose
    React + Vite for its popularity.


**Will I lose my changes if I sync?**

    No! We keep every version you make in Magic Patterns, including when you
    pull a new version from Github.


**Can I make changes to the code in Cursor?**

    Yes! You can make changes to the code in Cursor and then push them to
    Github, which can then be synced back to Magic Patterns.


**I don't see my Github code in Magic Patterns.**

    In order to keep the code compatible in Magic Patterns, we strip out what we
    deem as unnecessary code. Please get in touch if you think this is a
    mistake!


---

## Core Guide

### Building Your First Prototype
*Visual edit, prompting, and the /Inspiration skill*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/building-your-first-prototype

In this video, you will learn how to get from an idea to a working prototype in Magic Patterns. Topics map to [How to Prompt](/documentation/editor/how-to-prompt) (Select Mode, Visual Edit, and skills including `/Inspiration`).

- **[Next: Improving Your Prompts](/documentation/guide/improving-your-prompts)** — Continue to lesson two and improve your prompts.

### Design Systems
*Overview of rules, typography, colors, components, and leveraging your real design system.*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/design-systems

In this lesson, you will learn how to keep prototypes on-brand by using components, tokens, and libraries so generated UI matches your product standards.

Set up your design system from the [design systems overview](/documentation/design-systems/overview): [Rules](/documentation/design-systems/editing/rules), [typography and icons](/documentation/design-systems/editing/typography-and-icons), [colors](/documentation/design-systems/editing/colors), and [components](/documentation/design-systems/editing/components).

Teams can connect a real React library by linking a [GitHub repo](/documentation/design-systems/importing/github) or an [NPM package](/documentation/design-systems/importing/npm-package) (for example NPM, GitHub Packages, or a manual bundle). See [importing your design system](/documentation/design-systems/importing/overview) for connecting your library and onboarding.

- **[Next: Team Workflows and Sharing](/documentation/guide/team-workflows-and-sharing)** — Continue to lesson five and collaborate with your team.

### Engineering Handoff
*Export, sync, and MCP for IDE and agent workflows*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/engineering-handoff

In this lesson, we cover the [MCP server](/documentation/features/mcp-server/overview), [available MCP tools](/documentation/features/mcp-server/available_tools)

See also [Connectors](/documentation/connectors/connectors) for external MCP context inside the product. For other export options, see the [exporting overview](/documentation/exporting/overview), [sync to GitHub](/documentation/get-started/sync-to-github), [download code](/documentation/get-started/download-code), and [copy code as prompt](/documentation/get-started/copy-code-as-prompt).

- **[Magic Patterns Features Overview](/documentation/features/overview)** — Explore all Magic Patterns features after the video series.

### Importing from Figma
*Bring in existing UI*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/figma-imports

In this lesson, you will learn how to bring existing designs into Magic Patterns so you can extend and prototype with AI instead of rebuilding from scratch, whether you start from screenshots, files, or a handoff from another tool. When your source frames live in Figma, use [import from Figma](/documentation/importing/import-from-figma). Keep generated UI aligned with your [design system](/documentation/design-systems/overview) and reusable [components](/documentation/design-systems/editing/components). When you are ready to show progress, use [sharing](/documentation/editor/sharing) and [publishing a custom URL](/documentation/publishing/publish-url).

- **[Next: Design Systems](/documentation/guide/design-systems)** — Continue to lesson four and use your design system.

### Improving Your Prompts
*Troubleshooting, routes, merging designs, and Rules for context*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/improving-your-prompts

In this lesson, you will learn how to refine your prompts so Magic Patterns. We cover specificity, structure, and iteration patterns that help the model understand your goals, plus [troubleshooting](/documentation/troubleshooting/overview), [how to prompt](/documentation/editor/how-to-prompt) in depth, [adding pages and routes](/documentation/get-started/adding-pages), [merging designs](/documentation/editor/merging-designs), and [Rules](/documentation/design-systems/editing/rules) so the AI keeps the right product context.

- **[Next: Figma Imports](/documentation/guide/figma-imports)** — Continue to lesson three and import from Figma.

### Introduction
*AI design with Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/introduction

Welcome to our video series! These short lessons walk you through prototyping with AI in Magic Patterns: from your first prompt to design systems, collaboration, and handoff to engineering. The series is taught by **Colin Matthews**.

1. [Building Your First Prototype](/documentation/guide/building-your-first-prototype)
2. [Improving Your Prompts](/documentation/guide/improving-your-prompts)
3. [Figma Imports](/documentation/guide/figma-imports)
4. [Design Systems](/documentation/guide/design-systems)
5. [Team Workflows and Sharing](/documentation/guide/team-workflows-and-sharing)
6. [Engineering Handoff](/documentation/guide/engineering-handoff)

### Team Workflows and Sharing
*Sharing, inline comments, and templates*

**Source:** https://www.magicpatterns.com/docs/documentation/guide/team-workflows-and-sharing

In this lesson, you will learn how to collaborate in Magic Patterns: sharing designs, gathering input, and keeping everyone aligned as the prototype evolves. We focus on [team workspaces](/documentation/collaboration/team-workspaces), [inline comments](/documentation/collaboration/inline-comments), [templates](/documentation/editor/templates), and [sharing](/documentation/editor/sharing).

- **[Next: Engineering Handoff](/documentation/guide/engineering-handoff)** — Continue to lesson six and hand off to engineering.


---

## Editor

### Forking
*Use forking for debugging, collaboration, and to explore new ideas*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/forking

#### What is Forking?

**Fork = Create a copy of your design.**

Forking a design in Magic Patterns creates a new copy that works independently from the original. This is helpful when you want to:

* Explore new ideas without affecting your "main" design
* Create layout or flow variations
* Build on someone else's work without making changes to the original version.
* Debug issues by returning to a working version

#### How to Guides

##### How to Fork an Existing Design

You can fork any Design you own or one shared with you. Open the design you want to fork.

**Option 1: Fork from the title dropdown**

Click the dropdown next to the file name and select **Fork**.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/project-fork-from-name.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=34a322ced705f4d0dc4fc4d3182d3c2b)

**Option 2: Fork from the Export menu**

Click the **Export** button in the top right corner and choose **Fork** from the menu.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/project-fork-from-export.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=0046a554fedecdec36f95d777c5643b7)

A new design will open in a separate tab. It will be titled “[Original Project Name] - Forked” by default, but you can rename it anytime. You are free to edit the fork however you like.

> 💡 **Tip:**
> Want a clean slate? Forking clears your chat history and resets the AI
>   context.

##### How to Fork from an Older Version

One of the most powerful features of forking is the ability to fork from a specific version of your design. This is particularly useful for debugging and cleaning up your AI context.

![image](https://cdn.magicpatterns.com/uploads/6mb9fCkkmeQZDDkZkTBV9m/restore-this-version.png)

How to fork from a previous version:

1. Open the design you want to fork
2. Click on the versions dropdown
3. Click on the specific version you want to fork from
4. Once viewing that version, click the fork button (from title dropdown or Export menu)
5. A new design will be created based on that exact version

**Why fork from an older version:**

> ℹ️ **Note:**
> When you fork from an older version, the chat history from after that version
>   will not be included. You get a clean context window starting from that point.

* Debug issues: If your design broke after recent changes, fork from the last working version and start fresh
* Clean AI context: After many chat interactions, the AI context can get cluttered. Forking from a clean version gives you a fresh start with all the work intact
* Explore alternative paths: Try a different approach from a specific point without losing your current progress
* Recover from mistakes: If you went down the wrong path for several iterations, jump back to where things were working

#### Other Ways to Fork

##### How to Fork from a Canvas

1. Hover over the design you want to fork.
2. Right-click on it to open the context menu.
3. Select **Fork Current Design**.

This creates a new project based on the selected design only, without affecting the rest of the original canvas.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/fork-design-from-canvas.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=71a13cd29c419a037f16cd0cb22959c8)

##### How to Fork from our Community Catalog

You can also fork designs from the [ Community Catalog ](https://www.magicpatterns.com/catalog), which contains a curated library of public templates and designs.

After selecting a design, click **Edit in Chat ->** in the top right corner of the preview.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/forking-from-catalog.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=33ac7b775d8e62b98fe20a5d9f1bb59e)

This creates a new design preloaded with the selected project, ready for you to customize and build upon.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/design-after-forking.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=08b8c1e206832d1d168067ceb97bdd36)

### How to Prompt
*Prompt like a pro with Magic Patterns.*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/how-to-prompt

#### General Tips

* **Our biggest tip is to be SPECIFIC.** [Select Mode](/documentation/editor/how-to-prompt#select-mode-and-visual-edit) helps because providing "context" to the AI is key to getting accurate results.
  Remember that the AI cannot read your mind.
* Getting an error? Use the `/Debug` skill.
* Attach screenshots when creating designs
* Use ChatGPT to generate a prompt for you. The more specific the better.
* Don't see any changes? Ask the AI to explain what it did. Switch to `/Ask` mode. For example, It might have made a new page but didn't link a button to it.

#### Select Mode and Visual Edit

> 💡 **Tip:**
> Selecting specific elements with "Select Mode" is the most important feature
>   for getting accurate results.

Select Mode lets you click on specific elements in your design to tell the AI exactly what you want to change.

**How to use Select Mode:**

1. Toggle on Select Mode from the bottom-left corner of the chat
2. Click any element in your design (button, text, image, etc.)
3. This will open the Visual Edit panel.
4. By default, the "context" of what you have selected will be added to the chat.
5. Optional: edit visual properties manually in the panel and then click "Save."

> 💡 **Tip:**
> You can quickly toggle Select Mode with **⌥ + S**.

##### When to use Select Mode

* When the AI is changing the wrong thing
* When working with complex, multi-section designs

#### Adding Context to a Prompt

##### Attaching Files

You can attach images and `.md` files to a prompt — both when starting a new design from the dashboard and from the editor chat bar. Drop in a screenshot, PRD, spec, or notes doc and the agent reads it as first-class context.

> 💡 **Tip:**
> Attaching a screenshot as a starting point is highly recommended — the models
>   are great at recreating designs from images.

* Uploaded markdown files are saved alongside your design as `docs/*.md`, so they stay attached to the artifact and are available on every follow-up prompt.

##### Other Magic Patterns Designs

Want to merge designs? You can simply paste Magic Patterns links directly into your prompt. See more in the [Merging Designs](/documentation/editor/merging-designs) guide.



#### Chat Modes, Commands, and Integrations

Type `/` in the chat input to open the menu. You can also use Chat Modes and Skills straight from the dashboard initial prompt to kick off a new design.

![image](https://cdn.magicpatterns.com/uploads/bVeCue4HZM4381ADRm9LuQ/CleanShot_2026-04-30_at_18.31.372x.png)

##### Chat Modes

Chat modes change how the AI responds to your next message and stay active until you switch them.

###### `/Ask`

Chat with the AI without generating code (great for planning or asking questions). Uses credits.

###### `/Plan`

Plan a change with the AI before it edits your design. The agent asks a few clarifying questions, drafts a structured plan you can edit, and only writes code once you approve it. Useful for larger changes when you want to align on the approach first. Uses credits.

[Read the full Plan Mode guide.](/documentation/editor/plan-mode)

##### Default Skills

Skills are powerful default prompts that help you work more efficiently. You can also add your own custom Skills.

###### `/Debug`

If the AI is in a doom loop or not following instructions, the `/Debug` skill uses a special prompt template to help debug the issue effectively.

###### `/Inspiration`

Generates 4 different design variations to explore options.

###### `/Polish`

Cleans up your design with better spacing, alignment, and visual hierarchy.

##### Managing Context

Magic Patterns manages your conversation context automatically, but these commands give you more control. Smaller context keeps the agent focused and lowers per-generation credit costs. See [Credits and Billing](/documentation/get-started/credits-and-billing#credits) for how context affects credits.

###### `/Summarize`

Condenses the conversation so far, preserving the important details while freeing up context.

###### `/Clear`

Resets the current conversation context without needing to fork the design. Useful when you start an unrelated task on the same design.

##### Integrations

The `/` menu also gives you access to your [Integrations](/documentation/integrations/overview), so you can pull in services like OpenAI, Anthropic, or Feedback collection without leaving the chat.

#### Using Version History

> 💡 **Tip:**
> One of the most powerful features of Magic Patterns is version control. It's
>   instantaneous because Magic Patterns is frontend-only.

##### Reverting to a previous design

To go back to a previous design, click an older artifact card or select a version from the versions dropdown to preview it. Previewing lets you inspect an older version without changing the active version.

To make the previewed design active again, click **Restore this version**. Restoring creates a new latest version from the selected design, so future prompts continue from that restored version.

> 💡 **Tip:**
> If you send a prompt while previewing an older version, Magic Patterns will ask
>   you to confirm before restoring it as the active version.

![image](https://cdn.magicpatterns.com/uploads/631ap5uowPsy6QyHdNQm4x/version-dropdown.png)

* Thumbs down opens an optional comment box so you can tell us exactly what went wrong.
* Every rating is logged with the full conversation context so we can reproduce and fix the issue.

#### Prompting Dos and Don'ts

| ❌ Don't                                                                              | ✅ Do                                                                                                                                                                   |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Don't** be unclear: `checklist with 4 sections with 3 tasks each showing progress` | **Do** be specific: `four sections with 3 checkboxes each. There should be a progress bar for each section that changes according to the number of checkboxes checked` |
| **Don't** omit component names: `a box for checks in a list in screen thing`         | **Do** use component names: `Three checkboxes in a list in a modal`                                                                                                    |
| **Don't** upload lengthy PRDs expecting perfect results                              | **Do** break down large changes into smaller, focused updates                                                                                                          |
| **Don't** give broad instructions like "make the page cleaner"                       | **Do** use the `/Polish` skill                                                                                                                                         |
| **Don't** keep prompting when results become inconsistent                            | **Do** fork your chat, roll back to a previous version, or ask the AI to reflect on what's going wrong                                                                 |

> 💡 **Tip:**
> Use a screenshot to recreate an existing design. Provide styling rules by
>   creating a [design system](/documentation/design-systems/overview).

#### Taking your design to a codebase

When you're ready to bring a design into a production codebase with an AI editor, add the [Integration Skill](/documentation/exporting/integration-skill) to Cursor or Claude Code. It teaches the agent to treat the Magic Patterns output as a design spec and adapt it to your codebase's components, tokens, and conventions — instead of pasting the prototype verbatim.

#### How to use Existing Styles

Read [key concepts](/documentation/get-started/introduction#key-features) to learn more about Design Systems and components.

1. The models have become quite good! Try uploading a screenshot of the design you want to use as a starting point.
2. Do you have an existing component library? You can [create a Design System](/documentation/design-systems/overview) to organize your reusable components and ensure consistent usage across all your designs.
3. Use [Rules](/documentation/design-systems/editing/rules) to configure default styles like "always use #228B22 as my primary button color."

#### Video Guide

How to prompt is covered in our video lesson [Building Your First Prototype](/documentation/guide/building-your-first-prototype).

### Merging Designs
*Combine multiple designs into one*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/merging-designs

#### Option 1: Cross-Project Referencing (Recommended)



The fastest way to pull content from another design is to reference it directly in your prompt. This works from both the dashboard prompt bar and the editor chat bar.

There are two ways to do this:

* **Type `@`** to pick a standalone Design or a Design System.
* **Paste a design URL** to reference any design directly, including a design inside a canvas.

For example, with an `@` mention:


![@ menu showing Design Systems and Designs in the prompt bar](https://cdn.magicpatterns.com/uploads/qGZBv6vKfP8xuwSYCf6HpT/CleanShot_2026-05-13_at_14.00.482x.png)

```
Grab the pricing table from @My Pricing Page and add it to my landing page
```

Or with a pasted URL:

```
Pull the pricing table from https://www.magicpatterns.com/s/123?page=0&nodeIds=456 and add it here
```

or

```
Grab my dashboard from https://www.magicpatterns.com/c/789 from this design
```

You can only reference designs you have access to.

#### Option 2: Prompt to Link the Designs Together

All Magic Patterns designs are websites, so you can always just link designs together.

Let's say you have two designs, Design A and Design B. Perhaps they are separate pages and you want to link them together.

First, navigate to Design A and get its publish link from the share button. The URL is something like `https://project-design-a.magicpatterns.app`

![image](https://mintcdn.com/magicpatterns/o5W2EDtDFhU9Oi6b/documentation/editor/images/merging-designs/url-reference-1.png?fit=max&auto=format&n=o5W2EDtDFhU9Oi6b&q=85&s=5aecda43ea2e1320970eb012eda912c6)

Now, in Design B, perhaps you want to make a button that links to Design A. So, you can prompt something like:

```
Please make the button link to this URL...
```

In this example, you'd likely use [Select Mode](/documentation/editor/how-to-prompt#select-mode-and-visual-edit) to be specific about the button you want to link to and prompt something like:

```
Please make the pricing button link to this URL: https://project-design-a.magicpatterns.app
```

![image](https://mintcdn.com/magicpatterns/o5W2EDtDFhU9Oi6b/documentation/editor/images/merging-designs/url-reference-3.png?fit=max&auto=format&n=o5W2EDtDFhU9Oi6b&q=85&s=71c75ea3396443b8ae1c7aa34fa32307)

#### Option 3: Copy Code as Prompt

> ⚠️ **Warning:**
> This method may hit prompt size limits if you're trying to merge very large
>   designs. But you can always select specific elements using [Select
>   Mode](/documentation/editor/how-to-prompt#select-mode) to get the code.

Navigate to the design — let's say Design A — that contains the content you want to merge into another design, Design B.

Use the [Copy Code as Prompt](/documentation/get-started/copy-code-as-prompt) feature to get the code from Design A.

![image](https://mintcdn.com/magicpatterns/o5W2EDtDFhU9Oi6b/documentation/editor/images/merging-designs/code-as-prompt-1.png?fit=max&auto=format&n=o5W2EDtDFhU9Oi6b&q=85&s=55a6aa15b8771ccf9f0008a1a3e32d5d)

In Design B where you want to add the content, paste the code with a specific instruction like:

```
Add an About Us page using this code: [paste the code here]
```

![image](https://mintcdn.com/magicpatterns/o5W2EDtDFhU9Oi6b/documentation/editor/images/merging-designs/code-as-prompt-2.png?fit=max&auto=format&n=o5W2EDtDFhU9Oi6b&q=85&s=f3917a1b959a27c33be3e0669b26771f)

### Plan Mode
*Brainstorm and align on a change with the agent before any code is written.*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/plan-mode

`/Plan` is a chat mode that turns the agent into a planning partner. Instead of jumping straight into editing your design, the agent asks a couple of clarifying questions, drafts a short plan you can edit, and only writes code once you approve it.

> ℹ️ **Note:**
> Plan Mode uses credits because the AI is actively reasoning about your design.

Use it for larger changes, or any time you want to align on the approach (with yourself or a teammate) before the agent starts modifying files.


![Plan Mode in Magic Patterns](https://cdn.magicpatterns.com/uploads/eD6u3UVEcFc5qaD5zvFziu/CleanShot_2026-05-06_at_18.26.122x.png)

#### How it works


**Pick Plan from the slash menu**

    Type `/` in the chat input (in the dashboard or the editor) and select **Plan**.


**Answer a quick question or two**

    The agent usually replies with 1 to 3 multiple-choice questions to narrow down the request. The first option is the agent's recommendation. You can also dismiss the questions if you want the agent to go ahead with its best guess.


**Review the plan**

    A plan editor opens over the design preview and streams in a short markdown plan with sections like **Summary**, **What You'll See**, and **User Flow**. Edit anything you want directly. Changes are auto-saved.


**Hit Build**

    Click **Build with Auto** at the bottom of the plan editor (or pick a specific model from the dropdown). The agent switches out of Plan mode and starts implementing the plan.

#### Read more


- **[How to Prompt](/documentation/editor/how-to-prompt)** — Tips, chat modes, skills, and prompting do's and don'ts.

### Sharing Designs
*How to share Magic Patterns designs*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/sharing

There are two ways to share your designs:

1. [Share](#share) — Control who has access, get comments on your design, collaborate with teammates
2. [Publish](#publish) — The pure website without the Magic Patterns toolbar, mostly commonly used for use cases that require actual control of what's "live"

#### Share

> 💡 **Tip:**
> **Best practice**: use the share link by default! The share link can be made
>   public by clicking on "Who Has Access" > "Anyone with Link"

Click on the Share button in the editor navbar when you want to control who has access, collaborate with teammates or get feedback. The share link supports [inline commenting](/documentation/collaboration/inline-comments).

To share, click **Share** in the editor navbar. The share panel lets you:

* Control who has access to the design
* Share the link with teammates
* Enable [inline commenting](/documentation/collaboration/inline-comments)

![image](https://cdn.magicpatterns.com/uploads/hLz5mzwxDWRcge45n1sdQz/share-panel.png)

#### Publish

Use Publish when you want to control the version you are sharing. Publishing is often used in conjunction with [using a custom publish URL](/documentation/publishing/publish-url) or [hosting on a custom domain](/documentation/get-started/custom-domain).


**Click on Publish**

    Click **Publish** in the editor navbar. Here you can configure metadata
    (favicon, social preview) and enable password protection.

![image](https://cdn.magicpatterns.com/uploads/kV83K7vkAgjg5Pf2DnB1kQ/publish.png)


**Grab the live link or create a custom publish link**

    Copy the live link to share your published site, or set a custom website
    address and connect your own domain. Read more about [using a custom publish
    URL](/documentation/publishing/publish-url) or [hosting on a custom
    domain](/documentation/get-started/custom-domain).

![image](https://cdn.magicpatterns.com/uploads/id8BzV6gcJYJeL9VvmDnDp/publishing.png)

##### The Default "Live" URL

By default, every Magic Patterns design comes with a "live" URL. This is the URL that is always updated and does not include the Magic Patterns toolbar.

You can get to this link by either going to:

* [The Publish panel](/documentation/editor/sharing#publish)
* Clicking the "Open in new window" button in the editor navbar

![image](https://cdn.magicpatterns.com/uploads/b938P49wieMrFBQthDWQmF/view-in-new-window.png)

#### Live multiplayer

Once your teammates open the share link, you'll see their avatars in the editor toolbar and the chat thread, generations, and preview update for everyone in real time. On the [Canvas](/documentation/projects/getting-started) you'll also see live cursors and shared selections.

[Learn more about Live Multiplayer.](/documentation/collaboration/live-multiplayer)

#### Collaborating on a Canvas

Read about sharing on the [Canvas](/documentation/projects/how-to-share) for more information.

#### Video Guide

This topic is covered in our video lesson [Figma Imports](/documentation/guide/figma-imports).

### Templates
*Organize and reuse your designs with Templates*

**Source:** https://www.magicpatterns.com/docs/documentation/editor/templates

#### What are Templates?

**Templates = Designs you can share with your team**

Example templates: Your company core dashboard homepage, settings page, etc

Templates help you organize your best designs and make them easy to reuse. Convert any design into a template, and it will appear in your Templates tab on the dashboard.

Templates are perfect for:

* Creating starting points
* Sharing reusable interactions with your team
* Standardizing common page types (landing pages, dashboards, forms, etc.)

#### How to Guides

##### How to Create a Template

![Publish Template](https://cdn.magicpatterns.com/static/marketing/Template.png)

1. Open the design you want to convert into a template
2. Click the dropdown next to the design name
3. Select **"Publish Template"** from the Actions menu

Your design is now a template and will appear in the Templates tab on your dashboard.

###### Share Templates with your workspace

1. Click **Share** in the top-right corner of the template.
2. Click **Invite Workspace**.

Once shared with the workspace, everyone included can see and fork the template under their "Templates" in the dashboard.

##### How to Fork from a Template

You can fork from templates in two ways:

**Option 1: Fork from the dashboard**

![Fork from dashboard](https://cdn.magicpatterns.com/uploads/qtA3t9vtnzDBenkyb9caDt/Templates.png)

1. Navigate to the Templates tab on your dashboard
2. Right-click on the template you want to fork
3. Select **"Fork"** from the context menu

**Option 2: Fork from inside the template**

![Fork from inside template](https://cdn.magicpatterns.com/static/marketing/Fork-2.png)

1. Open the template you want to fork
2. Click the dropdown next to the template name
3. Select **"Fork"** from the Actions menu

A new design will open in a separate tab. It will be titled "[Template Name] - Forked" by default, but you can rename it anytime. You are free to edit the fork however you like.

##### How to Unpublish a Template

![Unpublish Template](https://cdn.magicpatterns.com/static/marketing/Unpublish.png)

If you no longer want a design to appear as a template:

1. Open the template
2. Click the dropdown next to the template name
3. Select **"Unpublish Template"** from the Actions menu

The design will remain in your files but will no longer appear in the Templates tab.

#### Video Guide

This topic is covered in our video lesson [Team Workflows and Sharing](/documentation/guide/team-workflows-and-sharing).


---

## Projects & Canvas

### Creating your first screen
*Start from scratch or import an existing design*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/creating-new-screens

#### From Scratch


**Click the 'Add New' Button**


![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/projects/images/navigation-bar.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=b64b967384ab1e3665bb28df437a14a7)




**Describe your screen in the prompt input**

    Check out our [prompting guide](/documentation/editor/how-to-prompt) for tips on how to write a good prompt or our [prompting templates](/documentation/projects/prompt-templates) for example prompts.


**Click 'Generate'**

    A new screen will be generated based on your prompt.

#### From an existing non-Canvas design

If you have an existing design in Magic Patterns, you can use the import feature to convert it into a Canvas design.

* **List**: Select any existing design directly from your list of saved projects.

* **From URL**: Paste the URL of any Magic Patterns design to import it into the canvas.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/projects/images/import-list-vs-url.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=c7e5f78c2cf532c6268dd19e7769effc)

### Using the Canvas
*Use the Canvas to organize your designs*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/getting-started

#### Introduction to the Canvas

Learn about common workflows and how to get the most out of the Canvas.

#### Canvas Features

The Canvas in Magic Patterns allows you to collaborate with your team in realtime. It meant for organizing designs on a single page, like a bird's eye view of a product.

You can:

1. [Navigate](/documentation/projects/navigating) in realtime with your team, with [live cursors and shared selections](/documentation/collaboration/live-multiplayer).

2. [Import existing designs](/documentation/projects/creating-new-screens)

3. [Connect screens together](/documentation/projects/prototyping) and share the URL with customers or stakeholders.


![image](https://cdn.magicpatterns.com/uploads/dZ35s4dJKwZo7pNEeb13vN/canvas-designs.png)

#### How to Access the Canvas

There are two ways to access the Canvas:

1. **From an existing design:** Click the button next to the title in the top nav bar → select "Add to Canvas"

![image](https://cdn.magicpatterns.com/uploads/vyDLZZLqAPxXGRPytQDmnx/add-to-canvas-menu-in-editor.png)

2. **From the dashboard:** Click the "Canvas" tab to see all your canvases

![image](https://cdn.magicpatterns.com/uploads/nFTRZmo8tDYmY5TB1uhSjH/new-canvas-in-dash.png)

#### Examples

* [Fintech app](https://www.magicpatterns.com/s/oQuqgAQcAWhAGQmcBAeUBX?page=0)
* [Twitter clone](https://www.magicpatterns.com/s/toUgQRYEjMnH2SMTSCyhuE?page=0)

#### Read More


- **[Navigating the Canvas](/documentation/projects/navigating)** — Learn how to navigate the canvas with your team.


- **[Creating a New Screen](/documentation/projects/creating-new-screens)** — Learn how to create a new screen in the canvas.


- **[Live Multiplayer](/documentation/collaboration/live-multiplayer)** — See how live cursors and shared selections work on the canvas.

### Sharing designs
*How to share designs created in Magic Patterns canvases*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/how-to-share

#### Sharing Links

When you are in a canvas, you can share the design in two ways:

1. Right click on a screen, and click "Copy Link to Node" (your teammates will need to have access to the canvas to see the link).
2. Or, simply click on a screen, and click "Open share link in full page" (anyone with this link can view it.)

The open in new window option is accessible to anyone with the link. We
recommend inviting your teammates to the canvas via the share button if you
would like to keep it entirely private and using "copy link to node" instead.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/project-links.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=cc6c3264d406a85a035248ac40c769be)

##### Invite Team

You can invite your teammates by clicking on the Share button in the top right corner of the screen.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/project-sharing.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=8bba5eb3c35fd2db396d309bb80a31c6)

### Navigating
*Getting around the Magic Patterns canvas*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/navigating

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/projects/images/canvas-hotkeys.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=e31abe215e9c5489cd01ac495b4de97d)

#### Tools

The Magic Patterns canvas has three tools:

 **Select**: Use the select tool to click, drag, and
drag elements.

 **Pan**: Use the pan tool to move the canvas around.

 **Prototype**: Use the Prototype tool to connect elements
together.

You can switch between these modes by clicking the corresponding button in the navigation bar or using the `V`, `H`, and `P` hotkeys.

> 💡 **Tip:**
> Hold the `Space` key to temporarily switch to the pan tool.

#### Centering the Canvas

It can be easy to get lost in the canvas.

* Click on a screen's name in the side navigation bar to center the canvas on that screen
* Use the `Zoom to Fit` button to bring all screens on that current page into view

#### Reordering Folders and Chats

To move a chat from one folder to another, simply use your keyboard’s copy and paste commands. Select the chat you want to move, press `Cmd/Ctrl + C` to copy, navigate to the destination folder, and press `Cmd/Ctrl + V` to paste.

### Using Prompt Templates
*Example prompts within the canvas*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/prompt-templates

**For trying to get creative generations:**

> Here are your current instructions: **YOUR INSTRUCTIONS**. Carefully consider various options for how to design this following best UI/UX options. Be creative and consider multiple angles, but only implement the best one.

**For overall cleaning up:**

> Carefully re-analyze the page. Adjust the font size and the layout if necessary (but try to keep it as close to the current layout as possible) to achieve the maximum professional and aesthetic look on all viewport sizes

**Generating a new screen in a flow:**

> Create the new step in this onboarding flow following **Reference #**. Specifically, design the next screen after the user clicks the Continue button.

### Linking Screens Together
*Link together screens and get an embeddable prototype*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/prototyping

On the canvas you can link screens together and get a
"playable" app using "Prototype Mode."

> 💡 **Tip:**
> You can make a **single** chat highly interactive with multiple
>   pages, and therefore no need for prototype mode.
>   But we offer this feature for linking together large designs because once designs
>   get very large it can be hard for the AI to add new pages.


![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/projects/images/prototype-linking-example.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=db15f99cf0f9b2835626453a8819eb23)

#### Prototyping Tutorial

#### How to link screens

1. Enter prototype mode either through the tool selector in the bottom bar or use the keyboard shortcut `P`
2. Hover over the element in the screen you want to link. It should turn blue. Click that element.
3. Click the screen you want to connect that element to.
4. You should see a toast in the bottom right pop up "Linking screens..."
5. Once your screens are linked, you should see an arrow connecting those two screens.

#### Playing your prototype

To play your prototype, select the screen you want to start on. Next, click the "Play" button in the top toolbar.

This will open up a separate window with your prototype.

#### Unlinking screens

To unlink screens, select the screen you want to remove links from. Click the "Unlink" button in the top toolbar.

> ℹ️ **Note:**
> Make sure you have the screen selected first before trying to unlink!

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/images/unlink.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=dde72cbcaaab4c8a64fd3e85ef82b5f6)

### Using References
*References are a way to add context to your prompts*

**Source:** https://www.magicpatterns.com/docs/documentation/projects/using-references

> ⚠️ **Warning:**
> References are great when the designs you referencing are small and simple,
>   and not recommended when they are very complex. Instead, we recommend using
>   screenshots or components.

References are recommended in the following scenarios:

* You want to generate a new screen based off an existing screen
* You want to keep a design consistent across multiple screens
* You want to modify an existing design
* You want to merge or combine multiple designs

#### How to use a reference

To use a reference, select the screen you want to reference and click the `Reference` button in the bottom action bar.

##### Multiple References

You can select multiple screens to reference by holding down the `shift` key while selecting screens or by dragging your selection around multiple screens.


![Reference Button](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/documentation/projects/images/reference-in-bar.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=967d1355de9a59a65cd1d5869324a92c)

For more examples, check out our [prompt templates](/documentation/projects/prompt-templates).

##### Prompting with references

You can directly address references in your prompts by referring them to `Reference #`. For example, an example prompt for combining two screens
would look like this:

> Recreate Reference 2 but use Reference 1 as theming and styling inspiration. Keep the layout of Reference 2 the exact same. Only use colors from Reference 1.

##### Under the hood

Behind the scenes, we are simply passing in the code to each of the screens along with your new prompt. As a result, you still have ultimate flexibility
in your prompt. We have future plans to add more sophisticated reference modes to make prompting even easier.


---

## Design Systems

### Colors
*Define your color palette for AI generation and Visual Edit*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/editing/colors

The Colors page lets you define your color palette inside your Design System: your primary, secondary, accent, and any other colors your brand uses. Once defined, these colors are available across the platform in generated code and in the [Visual Edit](/documentation/editor/how-to-prompt) color picker. This keeps your styling consistent without having to re-specify colors every time.


![Colors page in a Design System](https://cdn.magicpatterns.com/uploads/s1u2Vn3kY2aKAyjtLyxMgZ/CleanShot_2026-04-30_at_11.42.032x.png)

To add a color, click **+ Add** and give it a name. Click any color swatch to open the color picker, or type a hex value directly.

#### Why set up colors?

##### Consistent AI Generation

When you generate a design or [component](/documentation/design-systems/editing/components) with a [Design System](/documentation/design-systems/overview) that has colors set up, the AI will use your palette in the generated code. This means your colors end up in every new design without having to specify them in every prompt.

##### Visual Edit

When you select an element in [Visual Edit](/documentation/editor/how-to-prompt), the color picker shows a "Design System" section with your defined colors. This lets you apply colors from your palette directly to any element.


![Design System colors in the Visual Edit color picker](https://cdn.magicpatterns.com/uploads/wHNGeKqpqmFkk2TG6YZh5B/CleanShot_2026-04-30_at_13.10.212x.png)

#### Importing Colors

You can bulk-import color tokens into your Design System from a `.csv` file or a Figma `.json` variable export. This is the fastest way to bring an existing palette into Magic Patterns without manually adding each color.


![Design System Color Import Flow](https://cdn.magicpatterns.com/uploads/dFCtQpduz3E9hAWCpmDUxJ/CleanShot_2026-04-30_at_13.12.41.png)

> 💡 **Tip:**
> You can upload multiple files at once. For example, upload a light-mode and a
>   dark-mode export and Magic Patterns will let you assign each group to the
>   correct mode during review.

##### Importing from CSV

Your CSV file should have two columns: a **token name** and a **color value**. The first row can be a header or you can start with data directly.

Accepted header names for the **name column**: `name`, `key`, `token`, `variable`.

Accepted header names for the **value column**: `value`, `color`, `hex`, `code`.

Color values can be hex (`#FF0000`), rgb (`rgb(255, 0, 0)`), or hsl (`hsl(0, 100%, 50%)`).

```csv theme={null}
token,hex
color.blue.10,#DDF3FC
color.blue.20,#BBE7F9
color.blue.30,#98DBF7
color.gray.10,#F2F2F2
color.gray.20,#EBEBEB
```

Dotted or hyphenated names like `color.blue.10` or `background-primary` are automatically converted to readable labels (e.g. "Color Blue 10", "Background Primary") during import.

##### Importing from Figma Variables

Follow these steps to export your color variables from Figma as a JSON file that Magic Patterns can read.


**Open the Variables Panel**

    In Figma, go to **View > Panels > Toggle Variables** to open the variables panel.


![Figma Variables Panel](https://cdn.magicpatterns.com/uploads/4nV7AwcHzanPzH4zsuVyuw/figma-variables.png)




**Export a Collection**

    Right-click on the collection you want to export and select **Export modes**. This will export all variables in that collection.


![Figma Export Modes](https://cdn.magicpatterns.com/uploads/11kqLn6S24VCUwmDsd5Kx8/figma-export-modes.png)




**Unzip Multi-Mode Exports**

    If your collection has multiple modes (e.g. Light and Dark), Figma will download a `.zip` file. Unzip it to find separate `.json` files for each mode, so that you can upload them all into the color import flow.

##### Importing into your Design System

Once you have your files ready:


**Tap on 'Import from File'**

    Go to your Design System's **Colors** page and click the **Import from
    File** button. You can find it in the empty state or next to the **Add**
    button in the color table.


**Upload your files**

    Drag and drop your `.csv` or `.json` files, or click to browse. You can
    upload up to 7 files at once.


**Review and assign modes**

    Magic Patterns parses your files into color groups. For each group you can
    toggle it on or off and assign it to **Light** or **Dark** mode.


**Import**

    Click **Import** to add the colors to your Design System. If you already
    have colors defined, you will be asked to confirm before they are replaced.

> ⚠️ **Warning:**
> Importing colors **replaces** all existing color tokens in your Design System.
>   Make sure you are ready before confirming.

#### What's Next?


- **[Rules](/documentation/design-systems/editing/rules)** — Define spacing, visual rules, and brand guidelines for the AI.


- **[Typography and Icons](/documentation/design-systems/editing/typography-and-icons)** — Manage font groups and icons in your Design System.

### Components
*Reuse your custom components in your designs*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/editing/components

Components are like lego bricks. You can reuse them in your designs. Example components are buttons, cards, and modals.

All of your components live inside a [Design System](/documentation/design-systems/overview) and are managed together in a single, unified editor. You chat with the Design System as a whole to add, edit, and refine one or many components at a time, then publish a new version of the Design System when you're ready.

> 💡 **Tip:**
> Do you work with an existing design system? You can [import it from
>   Figma](/documentation/design-systems/importing/figma) or [link a GitHub
>   repo](/documentation/design-systems/importing/github) to bring your components
>   into Magic Patterns.

#### Creating a New Component

Components live inside [Design Systems](/documentation/design-systems/overview). To create a new component, you simply ask the agent for it from the Design System chat.


**Open your Design System**

    From the dashboard, navigate to [**Design Systems**](/documentation/design-systems/overview) and open the Design
    System where you want to add the component.


![image](https://cdn.magicpatterns.com/uploads/8hSQJbDdAU9qkDdDX1NkoZ/CleanShot_2026-04-30_at_11.41.422x.png)




**Go to the Components page**

    Inside your [Design System](/documentation/design-systems/overview), open the **Components** page. It shows the component list on the left, the selected component's preview/code in the middle, and the unified chat on the right.


![image](https://cdn.magicpatterns.com/uploads/cfvY3b5TVStnNB8HdPUYYf/CleanShot_2026-04-30_at_11.42.562x.png)




**Ask the agent to create your component**

    In the chat, describe the component you want. You can attach a screenshot, paste a Figma frame, or describe it in plain English.

    ```text theme={null}
    Add a PricingCard component with three tiers and a featured highlight on the middle tier.
    ```

    The agent creates the component, adds it to your Design System, and shows it in the preview. You can keep iterating in the same chat that edits every other part of your Design System.

We recommend being specific and using screenshots as references when possible for the best results.

#### Editing Components

Everything inside a Design System (components, typography, colors, icons, spacing, rules) is edited from a single chat that lives with the Design System. The chat is available on every tab in the Design System and operates on the **whole** Design System, not just the tab you're on.

You can:

* **Edit one component**: tag it with `@` or refer to it by name. *"Make `@Button` rounder and add a destructive variant."*
* **Edit several at once**: *"Update `@Card`, `@Modal`, and `@Toast` to use a 12px border radius."*
* **Make universal updates**: *"Tighten the spacing scale across the whole system"* or *"switch the primary color to indigo and update every component that uses it."*
* **Update typography or colors from any tab**: ask in the chat and the agent updates the relevant tokens and the components that depend on them.

The chat history lives on the Design System, so you (and your teammates) can see exactly how the Design System has evolved over time.

#### Versioning & Publishing

Versions are tracked at the **Design System level**. The version selector in the top-right of the editor shows your current version (e.g. `v1.2`), and you can revert to a prior version from the same dropdown.

When you publish a new version of your Design System, a modal appears letting you choose which existing designs to upgrade to that version. This lets you roll out a batch of changes (across many components, tokens, or rules) to all your designs in one step.


![image](https://cdn.magicpatterns.com/uploads/c5D91uHadZ2nr7jgoe9tmz/CleanShot_2026-04-30_at_14.08.01.png)


![image](https://cdn.magicpatterns.com/uploads/vkmaDG23NWrCa9ovHivWiC/CleanShot_2026-04-30_at_14.08.38.png)

#### Using Components

There are two ways to use components from your Design System in designs:

##### Automatic Usage with Design Systems

When you create a [Design System](/documentation/design-systems/overview) and add components to it, the AI will automatically use those components when generating designs. You don't need to manually reference them. Just select your Design System when creating a new design.

- **[Learn about Design Systems](/documentation/design-systems/overview)** — Set up a Design System with your components for automatic usage across all designs.

##### Manual Reference with @

You can also explicitly reference components in your prompts using the `@` symbol. This is useful when you want to use a specific component or reference components from outside your current Design System.

How it works:

1. Start typing `@` in the chat
2. A component selector appears
3. Select the component you want
4. The component is added to your prompt


![image](https://cdn.magicpatterns.com/uploads/e1ZHQkaKciLdWXy76LkoKm/CleanShot_2026-04-30_at_12.47.16.png)

Example:

```
Create a pricing page using @PricingCard and @CTAButton
```

#### Deleting Components

> ⚠️ **Warning:**
> Deleting a component is permanent and cannot be undone!

You can also deprecate a component instead of deleting it, which means the AI will no longer use it in new designs.

1. Open your [Design System](/documentation/design-systems/overview) and find the component
2. Click the three dots next to the component name and select **Delete**
3. Confirm the deletion

![Delete a component from a Design System](https://cdn.magicpatterns.com/uploads/8AWRRJsMRR62CVmF3TNLWb/CleanShot_2026-04-30_at_11.43.032x.png)

### Rules
*Define default styling rules for consistent designs*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/editing/rules

Rules is where you define the general design rules and prompts that the AI uses when generating components and pages. If you are familiar with other AI tools, you can think of this as "default prompts" or "skills." Define it once, and every design follows your brand rules.


![image](https://cdn.magicpatterns.com/uploads/rwvpNLGHisVmRfnXw63BbQ/CleanShot_2026-04-30_at_11.42.252x.png)

#### Example Rules

> 💡 **Tip:**
> Upload your brand guidelines to ChatGPT and ask it to create Rules for Magic
>   Patterns!

Here's a well-structured Rules page:

```text theme={null}
You are designing for the Acme Inc company.

Acme Inc makes B2B SaaS and has users that do XYZ.

#### Brand
Voice: Professional but approachable

#### Visual Rules
- Border radius: 8px
- Shadows: subtle (0 1px 3px rgba(0,0,0,0.1))
- Spacing: 16px between sections
- Style: Clean, minimal, lots of whitespace
```

#### What's Next?


- **[Colors](/documentation/design-systems/editing/colors)** — Manage your brand color tokens visually with the Colors page.


- **[Typography and Icons](/documentation/design-systems/editing/typography-and-icons)** — Manage font groups and icons in your Design System.

### Skills
*Reusable instructions the AI activates when a task matches*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/editing/skills

Skills are reusable instruction packages that the AI can activate when a task matches their description. They extend what designs built with your [Design System](/documentation/design-systems/overview) can do, beyond the always-on guidance in [Rules](/documentation/design-systems/editing/rules).

A skill is a `SKILL.md` package with a name and a description. The description tells the AI *when* to reach for the skill; the body holds the specialized instructions it should follow once activated. Unlike Rules (which apply to every generation), skills are pulled in only when they're relevant to what you're asking for.


![Skills in a Design System](https://cdn.magicpatterns.com/uploads/8hSQJbDdAU9qkDdDX1NkoZ/CleanShot_2026-04-30_at_11.41.422x.png)

#### Adding a Skill

Open your Design System and go to the **Skills** section. You have two options:

##### Create a new skill

Click **New Skill** to scaffold a `SKILL.md` package you can edit in place. Give it a clear name and a description that states exactly when the AI should use it, then write the instructions in the body.

> 💡 **Tip:**
> The description is the most important part. The AI matches the user's request
>   against it to decide whether to activate the skill, so be specific about the
>   scenarios it covers.

##### Install a skill

Click **Install Skill** and paste an install command. Only the `npx skills add <repo> --skill <name>` format is supported. Repos must be hosted on `github.com`, `gitlab.com`, or `bitbucket.org` (or use the GitHub `owner/repo` shorthand).

```bash theme={null}
npx skills add vercel-labs/agent-skills --skill frontend-design
```

#### Managing Skills

The Skills section lists every package in your Design System with its name and description. Open a skill to edit its files, or use the kebab menu to delete a package. Skills that fail validation are flagged as **Invalid** so you can fix the `SKILL.md` frontmatter.

Like everything else in a Design System, skills are versioned with the Design System, so changes roll out when you publish a new version.

### Typography and Icons
*Learn how to use custom fonts and icons in your Magic Patterns designs*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/editing/typography-and-icons

#### Typography

Magic Patterns supports custom fonts through the **Typography** section of your [Design System](/documentation/design-systems/overview). You can upload your own font files, choose a popular Google Font, or paste a web-hosted font URL. Every design created with that Design System will automatically use your specified fonts.

You can also reference any font by name directly in your prompts:

```Example Prompt theme={null}
Use Merriweather font from Google Fonts.
```

##### Managing Fonts in Your Design System

The Typography section lives inside your Design System and lets you create font groups for different use cases like headings, or body text


![Typography in Design Systems](https://cdn.magicpatterns.com/uploads/qe3dGXfetVTGPRSKSpP4XG/CleanShot_2026-04-30_at_11.41.492x.png)

To set up fonts in your Design System:

1. Open your Design System
2. Go to the **Typography** section
3. Click Add Font Group to create a new group
4. Choose your font source:
   * Upload your own custom font file
   * Pick a Google Font from [fonts.google.com](https://fonts.google.com)
   * Paste a link to any web-hosted font
5. Save your changes

Now every design you create with that Design System will automatically use your specified fonts.

##### Finding Google Fonts

To explore available fonts:

1. Visit [Google Fonts](https://fonts.google.com) to browse thousands of free fonts
2. Preview different fonts and styles
3. Note the font name (e.g., "Roboto", "Playfair Display")
4. Use that exact name when adding a Google Font group, or reference it directly in your prompt

#### Icons

Magic Patterns supports custom icons through the **Icons** section of your [Design System](/documentation/design-systems/overview). You can choose from popular icon libraries like Lucide, or import your own custom icons by uploading SVG files or providing URLs.


![Icons in Design Systems](https://cdn.magicpatterns.com/uploads/7GfrnL9Y2imEPXwrftgyJV/CleanShot_2026-04-30_at_11.42.102x.png)

##### Managing Icons in Your Design System

The Icons section lives inside your Design System and lets you choose between two modes:

1. **Icon Library** - Select from popular icon packages like Lucide React
2. **Manual Import** - Upload your own custom icons by providing SVG files or URLs

To set up icons in your Design System:

1. Open your Design System
2. Go to the **Icons** section
3. Choose your icon source:
   * Select an icon library from the dropdown (e.g., Lucide React)
   * Or switch to Manual Import to add custom icons
4. For manual imports, you can:
   * Drag and drop SVG files
   * Paste SVG code directly
   * Provide URLs to hosted icon files
5. Save your changes

Now every design you create with that Design System will have access to your specified icons.

### Figma
*Import frames and components from Figma into your Design System*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/figma

> ℹ️ **Note:**
> Looking to import a full Figma library? [Book a
>   call](https://cal.com/mp-daniel/30min) and our team will help. We are working
>   towards making this self-serve!

You can bring your Figma work into Magic Patterns to seed a Design System: import full frames as designs, or import individual Figma components as reusable [components](/documentation/design-systems/editing/components).

#### Connect your Figma account

Before importing, connect your Figma account to Magic Patterns. This enables both copy-paste and URL-based imports, and lets us use the **Figma MCP Server** to extract richer design data for higher-quality imports.

> ℹ️ **Note:**
> The Figma MCP Server is only available for `Dev` and `Full` Figma accounts.
>   `Free` and `Collab` accounts will still work but may have less precise
>   imports.

#### Import a component into your Design System


**Open your Design System and create a component**

    Go into your [Design System](/documentation/design-systems/overview), open the **Components** page, and click **Create Component**. Choose the **Import from Figma** tab.

![image](https://cdn.magicpatterns.com/static/docs/component-import-from-figma.png)


**Copy the link to a frame in Figma**

    Select a frame or component in Figma, right click and choose **Copy as → Copy link to selection** (or press `CMD + L`).


**Paste the link and import**

    Paste the link into the import dialog, confirm the preview looks right, choose your library, and click **Import**.

> ℹ️ **Note:**
> You can import **one frame at a time**. Import from Figma won't always produce
>   a pixel-perfect frame, because every Magic Patterns design is code-first and
>   interactive, whereas Figma frames are not.

#### Learn more

- **[Import from Figma](/documentation/importing/import-from-figma)** — The full guide to importing designs and components from Figma, including copy-paste and URL imports.

### GitHub
*Link a GitHub repository to import components and styles*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/github

Linking a GitHub repository lets Magic Patterns read your component source directly, so generated designs use your real code and import paths. This is the fastest way to seed a Design System when your components already live in a repo.

#### Connect your GitHub account

Before you can link a repo, connect your GitHub account so Magic Patterns can read the repository and browse its folders. When you open the **Link GitHub** connector, you'll be prompted to connect if you haven't already.

> ℹ️ **Note:**
> We only need read access. Magic Patterns reads the repository to import your
>   components and styles; it does not write to your repo.

#### Link a repository


**Open the GitHub connector**

    From your Design System, open the linked-sources panel (during onboarding, or later from **Access & Settings**) and choose **Link GitHub**.


**Pick or paste a repository**

    If your account is connected, start typing to autocomplete from the repositories Magic Patterns can see. You can also paste a repository URL directly:

    ```
    https://github.com/your-org/your-repo
    ```


**Choose subfolders (optional)**

    Once the repo resolves, you can browse its folders and select specific subfolders to import. For large repos, selecting a subfolder (for example the folder that holds your components) is required so we only scan the relevant code.


**Link**

    Click **Link** to attach the repository. Magic Patterns scans it and proposes the components, colors, and tokens it finds for you to review.

> 💡 **Tip:**
> You can paste a `/tree/<branch>/<path>` folder URL or a `/blob/...` file URL
>   and Magic Patterns will pre-select that subfolder for you.

#### What's Next?


- **[NPM Package](/documentation/design-systems/importing/npm-package)** — Connect a published component library instead of (or alongside) a repo.


- **[Importing overview](/documentation/design-systems/importing/overview)** — See every way to bring an existing design system into Magic Patterns.

### Local Code Folder
*Upload a zipped export of your component library from your machine*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/local-code-folder

If your component library lives on your machine rather than in a connected repo, you can upload it directly. Magic Patterns reads your component source so generated designs use your real code and import paths.

#### Upload your code


**Open the Local Code connector**

    From your Design System, open the linked-sources panel (during onboarding, or later from **Access & Settings**) and choose **Link Local Code**.


**Add your zipped export**

    Drag and drop, or click to browse for, a zipped export of your component library. Supported formats are `.zip`, `.tar.gz`, and `.tgz`. You can add more than one file.


**Choose subfolders (optional)**

    After a file uploads, you can browse its contents and select specific subfolders to import (for example the folder that holds your components) so we only scan the relevant code.


**Done**

    Once your uploads finish, continue. Magic Patterns scans the code and proposes the components, colors, and tokens it finds for you to review.

> 💡 **Tip:**
> Linking [GitHub](/documentation/design-systems/importing/github) instead keeps
>   your Design System in sync with a repo you already maintain. Use a local
>   upload when the code isn't in a repository Magic Patterns can reach.

#### What's Next?


- **[GitHub](/documentation/design-systems/importing/github)** — Link a repository to import components and styles straight from your code.


- **[Importing overview](/documentation/design-systems/importing/overview)** — See every way to bring an existing design system into Magic Patterns.

### NPM Package
*Connect your published React component library so the AI uses your real code*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/npm-package

> ℹ️ **Note:**
> [Book a call](https://cal.com/mp-daniel/30min) and our team will help set this
>   up. We are working towards making this self-serve!

Connecting a published component library brings your existing React components into Magic Patterns. After everything is connected, the AI will:

* Use your actual component code in generated designs
* Respect your component APIs, props, and variants
* Generate code with correct import paths
* Stay consistent with your design system

> ℹ️ **Info:**
> Everything on this page is guidance, not a checklist. We work with you during
>   onboarding and adapt to how your team already ships components. For example,
>   we have connected teams using the public NPM registry, private NPM, and GitHub
>   Packages (an npm-compatible registry with a read-only token and `.npmrc`
>   scoped to your organization). Prefer working from a repository instead? See
>   [linking GitHub](/documentation/design-systems/importing/github).

#### What we need

To import your components, we need two things:

1. **Component code**: either via an NPM package plus access token, or a zip or tar bundle you send manually. This lets us render the components in the Magic Patterns editor and ensures visual parity.
2. **Component documentation**: either via Storybook or a custom MCP. This serves as context for the AI to understand your components and when to use each one.

NPM, GitHub Packages, and other private registries are different ways to host and version the same package artifact; a zip, tar, or `npm pack` tarball you send manually fills the same role.

#### Package structure

We recommend keeping Storybook files next to your component sources so documentation stays close to the code and is easier for the AI to relate to usage.

```
my-design-system/
├── package.json
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.stories.tsx    # Storybook file
│   │   │   └── index.ts
│   │   ├── Card/
│   │   │   ├── Card.tsx
│   │   │   ├── Card.stories.tsx
│   │   │   └── index.ts
│   │   └── index.ts                  # Re-exports all components
│   └── index.ts                      # Main entry point
└── dist/                             # Compiled output
```


- **React Components** — Your code must be written in React.

#### Ways to share


**Tab: Registry token**

    If your package is on a private registry (NPM, GitHub Packages, or another npm-compatible host), share a read-only access token.

    ```bash theme={null}
    # Generate a read-only token
    npm token create --read-only
    ```

    Share this token securely with your Magic Patterns contact.


**Tab: Manual Bundle**

    You can also send a zip or tar bundle of your component library.

    ```bash theme={null}
    # Create a tarball of your package
    npm pack
    ```

    That produces a `.tgz` file you can send to us directly.

#### Documentation best practices

Good documentation helps the AI understand not only what your components do, but when to use them.

> ⚠️ **Warning:**
> Listing props alone is not enough. The AI needs context about when to pick one
>   component or variant over another.

##### Usage guidance

For each component, cover:

* Purpose: what problem the component solves
* When to use: which scenarios should lead to this component
* When not to use: anti-patterns or wrong fits
* Variants: when each variant is appropriate

```tsx theme={null}
/**
 * Button component for user actions.
 *
 * @usage
 * - Use `primary` variant for the main call-to-action on a page
 * - Use `secondary` variant for less important actions
 * - Use `destructive` variant only for delete/remove actions
 * - Use `ghost` variant for tertiary actions or in toolbars
 *
 * @when-not-to-use
 * - Do not use Button for navigation; use Link instead
 * - Do not use multiple primary buttons in the same section
 */
export const Button = ({ variant, size, children, ...props }) => {
  // ...
}
```

#### Working with multiple packages

Many design systems split across packages that depend on each other. Magic Patterns supports that layout.


- **Monorepo** — Multiple packages in one repository (for example Yarn workspaces, Turborepo, or Nx)


- **Multi-Repo** — Separate repositories for packages that depend on each other

If packages depend on each other, we account for that when syncing:

```
@mycompany/tokens        # Design tokens (colors, spacing, etc.)
@mycompany/primitives    # Low-level components (Box, Text, etc.)
@mycompany/components    # High-level components (Card, Modal, etc.)
```

The AI can:

* Import from the correct package
* Use shared tokens in a consistent way
* Respect your component layering

For multiple packages, plan to share:

1. Package list: every package that belongs to the design system
2. Dependency graph: how those packages relate
3. Access tokens: credentials for each private package when needed

> 💡 **Tip:**
> In a monorepo, one access token often covers every package in the workspace.

Generated code can then follow your structure:

```tsx theme={null}
import { colors, spacing } from '@mycompany/tokens'
import { Box, Text } from '@mycompany/primitives'
import { Card, Button } from '@mycompany/components'

export const PricingCard = () => {
  return (

-

Premium Plan
 Get Started

  )
}
```

#### Next steps

- **[Schedule a call](https://cal.com/mp-daniel/30min)** — Book time to plan connecting your real component library with your team.

### Overview
*Bring an existing design system into Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/overview

If you already have a design system, you don't have to rebuild it from scratch. Magic Patterns can pull your existing components, tokens, and styles from the sources you already use, so generated designs match your product from day one.

You can start a Design System empty and build it up in the dashboard (see [Getting Started](/documentation/design-systems/overview)), or seed it by linking one or more of the sources below.

#### Ways to import


- **[GitHub](/documentation/design-systems/importing/github)** — Link a repository and pull components and styles straight from your code.


- **[Local Code Folder](/documentation/design-systems/importing/local-code-folder)** — Upload a zipped export of your component library from your machine.


- **[NPM Package](/documentation/design-systems/importing/npm-package)** — Connect a published React component library so the AI uses your real code.


- **[Figma](/documentation/design-systems/importing/figma)** — Import frames and components from a Figma file.


- **[Your website](/documentation/design-systems/importing/overview)** — Match colors, fonts, and styles from a live website.

#### How linking works

When you create a Design System, you can link sources during onboarding (or later, from **Access & Settings**). After you link a source, Magic Patterns scans it and proposes the components, colors, typography, and tokens it finds. You review what gets imported before it lands in your Design System.

> 💡 **Tip:**
> You can link more than one source. For higher-quality results, pair a visual
>   source like your website or a Figma file with a code source like GitHub so the
>   AI has both the look and the real implementation.

#### Connecting your real engineering design system

Enterprise teams often want generated UI to match a real engineering handoff: the same React components and import paths your product ships with, not only visual parity. That flow is **not fully self-serve** because every codebase has nuances (build configs, token formats, export conventions) that benefit from a guided setup.

- **[Schedule a call](https://cal.com/mp-daniel/30min)** — Book time to plan connecting your real component library with your team.

See [customer case studies](https://www.magicpatterns.com/customers) for examples of teams that ship from their real design system.

### Prompting
*Describe or paste references in chat to build your Design System*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/importing/prompting

You don't have to import anything to get started. From the Design System chat, you can describe what you want in plain English and the agent builds it for you, adding components, colors, typography, and tokens to your Design System as you go.

#### Ways to prompt

* **Describe it**: Tell the agent what you're building. *"Create a Button, Card, and Modal that all share a 12px border radius and our brand blue."*
* **Paste an image**: Drop in a screenshot or reference image and ask the agent to match it. Great for recreating an existing UI or working from a mockup.
* **Paste a Figma frame**: Copy a frame in Figma (`⌘C`) and paste it into the chat to seed components from your designs.
* **Reference what exists**: Mention components by name with `@` to build on or refine pieces you've already added.

> 💡 **Tip:**
> Be specific and include references where you can. A short description plus a
>   screenshot usually produces a much closer result than words alone.

#### How it works

The chat lives with your Design System and operates on the **whole** system, so you can add several things at once or refine many components in a single message. Keep iterating in the same chat, then publish a new version when you're ready.

- **[Editing your Design System](/documentation/design-systems/editing/components)** — Learn how to chat with your Design System to add, edit, version, and publish components.

### Getting Started
*Set up your design system in Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/overview

A Design System is your team's single source of truth for styling and components. Our Design Systems feature is what makes Magic Patterns fundamentally different from other AI tools.

Once you have your design system set up, it ensures every design follows the same visual rules and uses
the same building blocks.


![image](https://cdn.magicpatterns.com/uploads/8hSQJbDdAU9qkDdDX1NkoZ/CleanShot_2026-04-30_at_11.41.422x.png)

You can build a Design System from scratch in the dashboard, or seed it from tools you already use by [importing](/documentation/design-systems/importing/overview) from GitHub, an NPM package, Figma, or your website.

#### What's Inside a Design System

| Concept                | Purpose                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Components**         | Browse and manage reusable UI building blocks used across your designs             |
| **Typography & Icons** | Manage font groups and icon sets used across your designs                          |
| **Colors**             | Visually manage your brand color tokens, with dark mode and token references       |
| **Rules**              | Default styling rules (spacing, visual style, brand voice) applied to every design |
| **Skills**             | Reusable instructions the AI activates when a task matches their description       |
| **Access & Settings**  | Manage sharing, permissions, and other Design System configuration                 |

#### Getting Started


**Create a Design System**

    From your dashboard, click **Design Systems** → **Create a design system**. You can also go directly to [magicpatterns.com/design-systems](https://www.magicpatterns.com/design-systems).


![image](https://cdn.magicpatterns.com/uploads/7cHAwSGA6HjVBZ76eEwf4y/CleanShot_2026-04-30_at_11.46.142x.png)




**Import your existing sources (optional)**

    Already have a design system? Link [GitHub](/documentation/design-systems/importing/github), an [NPM package](/documentation/design-systems/importing/npm-package), [Figma](/documentation/design-systems/importing/figma), or your website to seed components, colors, and tokens. See the [importing overview](/documentation/design-systems/importing/overview).


**Add your Rules**

    Define your spacing, visual style, and brand guidelines. This acts as a default prompt for all designs. For those familiar with other AI tools, you can think of this as "default prompts" or "skills" that are applied to the context of all designs.


![image](https://cdn.magicpatterns.com/uploads/hRBEYP6dnTaSQGa6pTn8Eu/CleanShot_2026-04-30_at_11.42.252x.png)




**Set up Typography and Icons**

    Go to **Typography** to manage font groups (custom fonts, Google Fonts, or font URLs) and **Icons** to pick an icon library or upload your own.


![Typography in Design Systems](https://cdn.magicpatterns.com/uploads/qe3dGXfetVTGPRSKSpP4XG/CleanShot_2026-04-30_at_11.41.492x.png)




**Define your Colors**

    Open the Colors page to set up your brand palette with colors like Primary, Secondary, Accent, and more.


![image](https://cdn.magicpatterns.com/uploads/s1u2Vn3kY2aKAyjtLyxMgZ/CleanShot_2026-04-30_at_11.42.032x.png)




**Add Components**

    Create or import reusable components. The AI will use them automatically when generating designs.

> 💡 **Tip:**
> You can add or refine many components at once from the same chat. For example:
>       *"Add a Button, Card, and Modal that all share a 12px border radius."*



![image](https://cdn.magicpatterns.com/uploads/rUwMAYMxidhESmkVdmp2X2/CleanShot_2026-04-30_at_11.41.422x.png)



#### Editing your Design System

Once your Design System is set up, you keep evolving it from one place: a single chat that lives with the Design System. The chat is available on every tab (Components, Typography, Colors, etc.) and operates on the **whole** Design System.

You can edit one component, several at once, or make universal updates like changing a color token or tightening the spacing scale system-wide. Versioning and publishing also happen at the Design System level.

- **[Editing components and your Design System](/documentation/design-systems/editing/components)** — Learn how to chat with your Design System to add, edit, version, and publish components.

#### How to Use It

When creating a new design, select your Design System from the dropdown. The AI will automatically:

* Apply your Rules
* Use your color tokens from the Colors page
* Use your Typography font groups and icons
* Use components from your Design System when appropriate


![image](https://cdn.magicpatterns.com/uploads/gEGikpBACanWPwk24wyagV/CleanShot_2026-04-30_at_12.47.16.png)

> 💡 **Tip:**
> You don't have to pick it every time. The dropdown remembers your last-used
>   Design System and pre-selects it on every new design. Once you create a design
>   with a Design System other than Base, that one becomes your default and is
>   applied automatically on the next new design (and the one after that).

You can also reference specific components with `@`:

```
Create a pricing page using @PricingCard and @CTAButton
```

#### Controlling Access

1. Open your Design System
2. Click **Access & Settings** in the left sidebar
3. In the **Access & Permissions** section, enter one or more emails (comma-separated) and click **Invite**

By default, anyone in your workspace can access the Design System with **Can write** permissions. You can adjust each teammate's role from the **Who has access** list.

Teammates can then use the Design System, browse components, and add new ones (based on permissions).


![image](https://cdn.magicpatterns.com/uploads/k4m68vrxiEvio4XUUgVdbr/CleanShot_2026-04-30_at_11.42.352x.png)

#### Learn More


- **[Importing your Design System](/documentation/design-systems/importing/overview)** — Bring an existing design system in from GitHub, NPM, Figma, or your website.


- **[Colors](/documentation/design-systems/editing/colors)** — Visually manage your brand color tokens with dark mode and references.


- **[Rules](/documentation/design-systems/editing/rules)** — Write effective styling rules with examples and naming tips.


- **[Using Components](/documentation/design-systems/editing/components)** — Create, edit, and manage components in your Design System.


- **[Converting Design Systems](/documentation/design-systems/using/converting-design-systems)** — Switch a design from one Design System to another.


- **[Typography and Icons](/documentation/design-systems/editing/typography-and-icons)** — Manage font groups and icons in your Design System.

#### Video Guide

This topic is covered in our video lesson [Design Systems](/documentation/guide/design-systems).

### Converting Design Systems
*Switch a design from one Design System to another*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/using/converting-design-systems

#### Overview

Converting Design Systems allows you to take any existing design and convert it to use a different [Design System](/documentation/design-systems/overview). The AI attempts to rewrite your code to match the new Design System's styling and components while keeping the same views and functionality.

#### When to Convert

This feature is helpful when you want to:

* Switch [Design Systems](/documentation/design-systems/overview): move a design from one Design System to another
* Apply a new brand: update an existing design to match a newly created [Design System](/documentation/design-systems/overview)
* Explore variations: see how your design looks with different styling rules
* Standardize old designs: bring legacy designs up to date with your current [Design System](/documentation/design-systems/overview)

#### How to Convert


![image](https://cdn.magicpatterns.com/static/docs/convert.gif)


**Open the design you want to convert**

    Navigate to the design you want to change the Design System for in the
    editor.


**Click Convert in the dropdown**

    Click the **Convert** button in the top bar of the editor. This opens the
    [Design System](/documentation/design-systems/overview) conversion dialog.


**Choose your target Design System**

    Select the [Design System](/documentation/design-systems/overview) you want
    to convert to from the dropdown menu.


**Review the conversion**

    A new design will be generated in a separate tab with your design migrated
    to the new [Design System](/documentation/design-systems/overview). The
    original design remains unchanged.

### Detaching Components
*Detach components from your Design System to create one-off customizations*

**Source:** https://www.magicpatterns.com/docs/documentation/design-systems/using/detaching-components

#### Detach Components Tutorial

> ℹ️ **Note:**
> Use the "detach components" option sparingly when you need one-off
>   customizations that do not need to sync with the main design system.

While we recommend editing components directly to keep your design system consistent, there may be cases where you want more flexibility. For those situations, you can enable a preference to automatically detach components when adding them from a library. This setting can be found under Settings > [Preferences](https://www.magicpatterns.com/settings#preferences) > Automatically Detach Components.

Detaching gives you a raw instance of the component, allowing the AI to modify specific parts. However, it also breaks the link to the original component, so updates to the library version will not carry over.

Think of your components as the "lego bricks" of your app. You might use detach when:

1. You want the AI to edit the component directly
2. You are ok with the component not syncing with the main design system
3. You need to link screens together in the canvas (components are not currently supported in prototyping mode)

In most instances, you likely might be better off editing the instance of the component directly.


![image](https://cdn.magicpatterns.com/uploads/cHKwWPTSREGFZUcMKAKGSW/CleanShot_2026-04-30_at_13.15.29.png)


---

## Importing

### Connect to GitHub
*Attach a GitHub repository to your design so the agent builds with your real code*

**Source:** https://www.magicpatterns.com/docs/documentation/importing/connect-github

Connecting a GitHub repository attaches it to your design as context, so the agent can read your codebase and build with your real components, styles, and patterns.

> ℹ️ **Note:**
> We only need read access. Magic Patterns reads the repository to ground your
>   designs in your code; it does not write to your repo. Connecting a repo here
>   attaches it to a single design, it does not import a
>   [Design System](/documentation/design-systems/overview).

#### Connect your GitHub account

The first time you connect a repo, you'll be prompted to connect your GitHub account so Magic Patterns can list your repositories and browse their folders. Once connected, your account stays linked for future designs.

#### Attach a repository


**Open the GitHub connector**

    In the editor prompt bar, open the **+** menu and choose **Connect Github**.


![Connect Github option in the prompt bar menu](https://cdn.magicpatterns.com/uploads/ptHymCasdf3cAvNVBCsKbY/step-1-import-github.png)




**Pick or paste a repository**

    Start typing to autocomplete from the repositories Magic Patterns can see, or paste a repository URL directly:

    ```
    https://github.com/your-org/your-repo
    ```


![Selecting a repository in the Connect GitHub dialog](https://cdn.magicpatterns.com/uploads/gbGZ8NTMtJHopCjHZDep5B/step-2-write-repo.png)




**Choose subfolders (optional)**

    Once the repo resolves, browse its folders and select the subfolders you want the agent to use — for example, the folder that holds your components. For large repos, narrowing to a subfolder keeps the agent focused on the relevant code.


**Attach**

    Click to attach the repository. It appears as a chip above the prompt bar, and the agent can read it while building.


![Attached repository shown as a chip above the prompt bar](https://cdn.magicpatterns.com/uploads/jCjagJYk1eMokb6r5HHYnN/step-3-connected-github.png)



> 💡 **Tip:**
> You can paste a `/tree/<branch>/<path>` folder URL or a `/blob/...` file URL
>   and Magic Patterns will pre-select that subfolder for you.

#### Managing attached repos

* **Edit subfolders.** Click a chip to change which subfolders that repository uses.
* **Remove.** Remove a chip to detach the repo. Recently removed repos are offered as one-click **existing connection** shortcuts (with their saved subfolders) so re-attaching keeps your previous selection.

> ℹ️ **Note:**
> If a repo shows a connection issue, either GitHub isn't connected for your
>   account, or the repository was attached by someone else and you don't have
>   access to read it.

#### What's Next?


- **[Design Systems](/documentation/design-systems/overview)** — Link a repo permanently as a Design System to reuse components across designs.


- **[Connectors](/documentation/connectors/connectors)** — Pull context from your other tools, databases, and apps into your prompts.

### Import from Figma
*Import designs from Figma to Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/importing/import-from-figma

Import your Figma designs into Magic Patterns to turn them into interactive, code-first prototypes. Watch the video below to see how it works:

##### Connect Your Figma Account

Before importing, you'll need to connect your Figma account to Magic Patterns. This connection enables both copy-paste imports and URL-based imports.

![image](https://cdn.magicpatterns.com/uploads/h6yCNMciM47gbYzH6ZqKWy/Figma-Login.png)

When you connect your Figma account, we automatically use the **Figma MCP Server** to provide more precise imports by extracting detailed design information from your files.

**MCP** (Model Context Protocol) allows AI tools to communicate through a common interface. With MCP, we can access richer design data from Figma, resulting in better import quality.

> ℹ️ **Note:**
> The Figma MCP Server is only available for `Dev` and `Full` Figma accounts.
>   `Free` and `Collab` accounts will still work but may have less precise
>   imports.

##### Copy and Paste Import

The fastest way to import from Figma is to simply copy a frame or component in Figma and paste it directly into Magic Patterns. Once your Figma account is connected, Magic Patterns will automatically detect the pasted design and import it.

##### Import via URL

You can also import by pasting a Figma URL. This method works well when you want to share a specific frame link or import from a file you're not actively working in.

> ℹ️ **Note:**
> You can import **one frame at a time**. If you need to import multiple frames,
>   repeat the import process for each frame. Import from Figma won't always
>   generate a pixel-perfect frame. That's because every Magic Patterns design is
>   code-first and interactive, whereas Figma frames are not.


**Create a new design from the dashboard and click on the 'Import from Figma' button.**

![image](https://cdn.magicpatterns.com/static/docs/import-from-figma-design.png)

    You can also import Figma components as Magic Patterns [components](/documentation/design-systems/editing/components) by going into a [Design System](/documentation/design-systems/overview), clicking **Create Component**, and choosing the **Import from Figma** tab.

![image](https://cdn.magicpatterns.com/static/docs/component-import-from-figma.png)


**Copy the link to a frame in Figma.**

    Select a frame/component in Figma, right click and select 'Copy as' and then 'Copy link to selection'. CMD + L allows you highlight the link to the selection directly.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/importing/images/figma-frame-url.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=1c860fc6c9d764951021fd9ba17f4b8e)

    Select a frame/component in Figma and use "CMD + L" to get the URL.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/importing/images/figma-frame-url-shortcut.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=a62e3d7a8b71e30bb4780ea7bca501da)


**Paste the link into the Magic Patterns import dialog and click 'Next'**

![image](https://mintcdn.com/magicpatterns/oOL4DTirAmu4iVXf/documentation/importing/images/import-from-figma-url.png?fit=max&auto=format&n=oOL4DTirAmu4iVXf&q=85&s=6f43e466c06e345e2e14a02cfab42150)



#### Video Guide

This topic is covered in our video lesson [Figma Imports](/documentation/guide/figma-imports).


---

## Features

### MCP Tools & Workflows
*Tools available from the Magic Patterns MCP server and how to use them*

**Source:** https://www.magicpatterns.com/docs/documentation/features/mcp-server/available_tools

#### Workflows

There are four primary ways to use the Magic Patterns MCP tools.


- **Prompt-based** — Delegate creative work to Magic Patterns' AI. Send a natural language prompt and let the AI generate or update code.


- **Code-first** — Write code directly into artifacts. Create a working branch, edit files, and publish when done.


- **Design-system authoring** — Build a reusable design system by writing components, styling, and rules directly, then publish versioned releases.


- **Inspiration concepts** — Publish a shareable set of side-by-side design concepts, then fill in or revise each concept's content as you explore directions.

##### Workflow A — Prompt-based

**Starting from scratch:**

```
1. create_design(prompt, ...)         → kicks off AI generation
2. get_design_status(editorId)        → poll every 60s until isGenerating=false
```

**With an existing design:**

```
1. get_editor_id_from_url(url)        → resolve a Magic Patterns URL to an editorId
2. get_design_status(editorId)        → check current state before acting
3. send_prompt(editorId, prompt)      → send prompt (returns immediately)
4. get_design_status(editorId)        → poll every 60s until isGenerating=false
```

##### Workflow B — Code-first

```
1. create_design()                    → no prompt, creates blank design instantly
2. get_design_status(editorId)        → confirm active artifact is ready
3. create_new_artifact(artifactId, name)  → create a working branch
4. read_artifact_files(artifactId, fileNames) → read existing scaffolding
5. write_artifact_files(artifactId, files) → write one or more files at once
6. publish_artifact(artifactId, editorId)  → compile + activate
```

##### Workflow C — Design-system authoring

Author a reusable design system (components, styling, and rules) by writing files
directly. **You** write the code here — Magic Patterns does not generate it for you.
Load the `design_system_authoring_guide` prompt first for the full file contract.

```
1. list_design_systems()                      → find an existing design system ID, or…
2. create_design_system(name)                 → create a new blank design system
3. get_design_system(designSystemId)          → resolve active artifact + file list (always first)
4. read_design_system_files(designSystemId, fileNames) → read existing files before editing
5. write_design_system_files(designSystemId, files, baseArtifactId) → save files (permissive)
6. publish_design_system(designSystemId)       → publish an immutable version (strict)
```

##### Workflow D — Inspiration concepts

Publish a shareable `magicpatterns.com/inspiration/<id>` link that renders 4
design concepts side by side. The preferred flow declares placeholder concepts
first (so the link is publishable immediately), then streams each concept's
content in one at a time.

```
1. create_inspiration_document(title, files)     → declare concepts (with or without html), get the shareable URL
2. inspiration_add_variant(inspirationId, variantId, html) → fill in each placeholder concept
3. get_inspiration_document(inspirationId)        → read concepts back (e.g. to implement one)
4. inspiration_update_variant(inspirationId, variantId, html) → revise a single filled concept in place
5. inspiration_clear_variants(inspirationId)      → reset every concept back to a placeholder
```

> 💡 **Tip:**
> Slide decks share the design/artifact tooling: `create_slide_deck(prompt)`
>   kicks off AI generation just like `create_design`, then you poll
>   `get_design_status` the same way.

***

#### Important Guidance

> ⚠️ **Warning:**
> **Collaborative editing:** Magic Patterns is a collaborative editor — the user
>   can make changes in the UI at any time. Always call `get_design_status` before
>   starting new work to get the latest active artifact. Never assume state from a
>   previous call is still current.

> ⚠️ **Warning:**
> **Polling:** AI generation typically takes **2–10 minutes**. Poll
>   `get_design_status` no more frequently than **every 60 seconds**. Slow
>   generation is normal — do not treat it as an error.

> ⚠️ **Warning:**
> **Design systems — write vs. publish:** `write_design_system_files` is
>   *permissive* — it saves your files and returns `validationErrors` without
>   blocking, so you can build incrementally. `publish_design_system` is *strict*
>   — it refuses while any validation errors remain. Clear every
>   `validationErrors` entry before publishing. Design systems are also
>   collaborative: always call `get_design_system` first and pass its
>   `artifactId` as `baseArtifactId` on writes so concurrent edits are detected
>   (a 409 means re-read and retry).

***

#### General Tools

- `list_design_systems` (Tool): Lists the design systems available to the authenticated user. Returns both built-in presets (e.g. Base, Shadcn, MUI) and any custom design systems.

*Parameters:*
This tool takes no parameters.


*Returns:*
    Array of design systems, each with:

    * `id` — unique design system ID (pass to `create_design`)
    * `name` — human-readable name
    * `isReserved` — whether it is a built-in preset
    * `isActive` — whether this is the user's currently active design system

***

#### Design Tools

- `create_design` (Tool): Creates a new Magic Patterns design. This is the starting point for both workflows.

  * **With `prompt`**: Kicks off AI generation (long-running, 2–10 minutes). Poll `get_design_status` every 60s.
  * **Without `prompt`**: Creates a blank design with scaffold files (`App.tsx`, `index.tsx`, `index.css`, `tailwind.config.js`). Returns immediately.
  * **With `templateId`**: Forks an existing design first, then optionally applies the prompt to the fork.

*Parameters:*

- `name` (string): Optional name for the design. Defaults to "Untitled".


- `prompt` (string): Optional natural language prompt. If omitted, a blank design is created
      instantly.


- `imageUrls` (string[]): Optional image URLs as visual references (only used with prompt).


- `designSystemId` (string): Optional design system ID. Use `list_design_systems` to discover IDs.


- `designSystem` (string): Optional design system name (e.g. "Shadcn", "MUI"). Resolved
      case-insensitively. `designSystemId` takes precedence if both provided.


- `templateId` (string): Optional editor ID of an existing design to use as a template. The design
      is forked before any prompt is applied. You can find the editor ID in the
      design URL (`magicpatterns.com/c/<id>`) or resolve it with
      `get_editor_id_from_url`.


*Returns:*
    * `editorId` — the editor ID for subsequent operations - `editorUrl` — URL to
      edit the design - `previewUrl` — URL to preview the design -
      `activeArtifactId` — the currently active artifact ID - `availableFiles` —
      array of file paths


> ⚠️ **Warning:**
> This tool requires credits when used with a prompt.

- `create_slide_deck` (Tool): Creates a new Magic Patterns **slide deck** and kicks off AI generation. A slide deck is a 16:9, full-bleed, one-slide-at-a-time React presentation where each slide maps to a screen in the canvas.

  Unlike `create_design`, a `prompt` is **required** — there is no blank-deck path. Generation is long-running (2–10 minutes); poll `get_design_status` every 60s.

*Parameters:*

- `prompt` (string, required): Natural language description of the slide deck to generate (e.g. "A 10-slide
      startup pitch deck for a fintech company").


- `name` (string): Optional name for the slide deck. Defaults to "Untitled".


- `imageUrls` (string[]): Optional image URLs as visual references.


- `designSystemId` (string): Optional design system ID. Use `list_design_systems` to discover IDs.


- `designSystem` (string): Optional design system name (e.g. "Shadcn", "MUI"). Resolved
      case-insensitively. `designSystemId` takes precedence if both provided.


*Returns:*
    * `editorId` — the editor ID for subsequent operations
    * `editorUrl` — URL to edit the slide deck
    * `previewUrl` — URL to preview the slide deck
    * `activeArtifactId` — the currently active artifact ID
    * `availableFiles` — array of file paths


> ⚠️ **Warning:**
> Generation typically takes **2–10 minutes**. Poll `get_design_status` every 60 seconds until `isGenerating=false`. This tool requires credits.

- `get_editor_id_from_url` (Tool): Resolves a Magic Patterns URL to an editor ID.

*Parameters:*

- `url` (string, required): The Magic Patterns URL. Supported formats:

      * `magicpatterns.com/c/<id>`
      * `https://www.magicpatterns.com/c/<id>`
      * `project-<slug>.magicpatterns.app`
      * `magicpatterns.com/s/<canvasId>?nodeIds=<nodeId>`


*Returns:*
    * `editorId` — use with `get_design_status`, `send_prompt`, `get_artifact`, and other tools

- `get_design_status` (Tool): Gets the current status of a design: whether AI generation is active, the active artifact ID, and available files.

  **Always call this before starting new work** on an existing design — the user may have changed state since you last checked. Also used to poll for completion after `create_design` (with prompt) or `send_prompt`.

*Parameters:*

- `editorId` (string, required): The editor ID from `create_design` or `get_editor_id_from_url`.


*Returns:*
    * `isGenerating` — `true` if AI is still generating - `activeArtifactId` — the
      current active artifact ID - `availableFiles` — list of file names in the
      active artifact


> ℹ️ **Note:**
> When `isGenerating=true`, wait at least **60 seconds** before polling again. Generation can take up to 10 minutes.

- `send_prompt` (Tool): Sends a natural language prompt to the Magic Patterns AI for an existing design. Returns immediately with a request ID. The generation runs in the background.

*Parameters:*

- `editorId` (string, required): The editor ID of the design to update.


- `prompt` (string, required): A natural language description of what to create or change.


*Returns:*
    * `requestId` — identifier for this generation request


> ℹ️ **Note:**
> Check `get_design_status` first to ensure `isGenerating=false` before sending a prompt.

> ⚠️ **Warning:**
> Generation typically takes **2–10 minutes**. Poll `get_design_status` every 60 seconds until `isGenerating=false`. This tool requires credits.

- `read_recent_message_history` (Tool): Reads the recent chat item history for a design. Returns the last **10** items (user prompts, AI responses, artifact versions, edits). Use `skip` to paginate backwards.

  Code contents are omitted to keep the response concise — use `read_artifact_files` to read full file contents.

*Parameters:*

- `editorId` (string, required): The editor ID of the design.


- `skip` (number): Number of recent items to skip (for pagination). Defaults to 0.


*Returns:*
    * `items` — array of chat history items (id, role, app, content summary, timeCreated)
    * `hasMore` — whether older items exist

- `list_version_history` (Tool): Lists the artifact version history for a design. Returns the most recent **20** versions.

*Parameters:*

- `editorId` (string, required): The editor ID of the design.


- `skip` (number): Number of recent versions to skip (for pagination). Defaults to 0.


*Returns:*
    * `versions` — array of versions (artifactId, versionLabel, title, timeCreated)
    * `hasMore` — whether older versions exist

- `publish_artifact` (Tool): Compiles an artifact's source files and sets it as the active artifact for the design. This is the **final step** in the code-first workflow.

  1. Compiles all source files (bundling for preview)
  2. Sets the artifact as active (appears in editor and preview)
  3. Adds a version entry to the design timeline

*Parameters:*

- `artifactId` (string, required): The artifact ID to compile and publish.


- `editorId` (string, required): The editor ID of the design this artifact belongs to.


*Returns:*
    * `artifactId` — the published artifact ID
    * `compiledFiles` — list of compiled file names

***

#### Artifact Tools

- `get_artifact` (Tool): Gets the active artifact for a design, including its ID and list of files.

  Always call this (or `get_design_status`) to get the **latest** active artifact — do not rely on a previously cached artifact ID.

*Parameters:*

- `editorId` (string, required): The editor ID of the design.


*Returns:*
    * `artifactId` — the current active artifact ID
    * `files` — list of file names

- `create_new_artifact` (Tool): Creates a new artifact by cloning an existing one. The new artifact becomes the active artifact.

> ℹ️ **Note:**
> Call this **before** making file changes with `write_artifact_files` so the
>     user can revert to the previous artifact if needed. Always call
>     `get_design_status` or `get_artifact` first to get the current active artifact
>     ID.


*Parameters:*

- `artifactId` (string, required): The artifact ID to clone from (typically the active artifact).


- `name` (string, required): A name for this artifact version (shown in the design timeline).


*Returns:*
    * `artifactId` — the new artifact ID
    * `files` — list of file names cloned from the source

- `read_artifact_files` (Tool): Reads the contents of one or more files from an artifact.

> ℹ️ **Note:**
> Always read files **before** making changes with `write_artifact_files` so you
>     understand the current state.


*Parameters:*

- `artifactId` (string, required): The artifact ID to read files from.


- `fileNames` (string[], required): Array of file names/paths to read.


*Returns:*
    * `files` — array of `{ name, content }` for each matched file

- `write_artifact_files` (Tool): Creates or overwrites one or more files in an artifact. If a file exists, it is replaced. If it doesn't exist, it is created.

> ℹ️ **Note:**
> This only saves source files — it does **not** compile or publish. Call
>     `publish_artifact` after finishing all file changes.


*Parameters:*

- `artifactId` (string, required): The artifact ID to write files to.


- `files` (array, required): Array of files to write. Each entry has: - `fileName` — the file name/path
      (e.g. `App.tsx`, `utils/helpers.ts`) - `code` — the full file contents to
      write


*Returns:*
    * `files` — updated list of all file names in the artifact

***

#### Design System Tools

These tools let an agent author a Magic Patterns **design system** — a reusable,
versioned collection of components, styling, and rules — by writing files
directly. This is distinct from the design/artifact tools above: here **you**
write the code, rather than delegating to Magic Patterns' AI.

> 💡 **Tip:**
> Load the `design_system_authoring_guide` prompt before writing any files. It
>   documents the full file/folder contract (component trios, named-export rules,
>   `index.css` import order, allowed providers, and more).

A design system's writable files follow this structure:

* `components//index.tsx` — component source (PascalCase folder, **named exports only**)
* `components//.previews.tsx` — preview definitions (required per component)
* `components//Context.md` — AI/usage documentation (required per component)
* `index.css` — design system styles / Tailwind imports (editable, cannot be deleted)
* `tailwind.config.js` — Tailwind configuration (editable, cannot be deleted)
* `rules/<slug>.md` — design rules (`rules/setup.md` is the special "Setup" rule)

Shell / auto-generated files (root `index.tsx`, `library.ts`, `registry.ts`, etc.) are stripped automatically if sent.

- `get_design_system` (Tool): Resolves a design system's active artifact and lists its files. **Always call this first** — design systems are collaborative, so the active artifact ID can change between calls. Never reuse a cached `artifactId`.

*Parameters:*

- `designSystemId` (string, required): The design system ID (`ds-...`). Use `list_design_systems` to discover
      available design systems.


*Returns:*
    * `designSystemId` — the design system ID
    * `name` — human-readable name
    * `artifactId` — the current active artifact (pass as `baseArtifactId` to `write_design_system_files` to detect drift)
    * `files` — the persisted files (e.g. `components//*`, `index.css`, `tailwind.config.js`, `rules/*`)
    * `hasUnpublishedChanges` — whether the active artifact differs from the latest published version
    * `guide` — pointer to the `design_system_authoring_guide` prompt

- `read_design_system_files` (Tool): Reads the contents of one or more files from a design system's active artifact.

> ℹ️ **Note:**
> Call `get_design_system` first to discover available file names, and always
>     read files **before** editing them so you preserve current content.


*Parameters:*

- `designSystemId` (string, required): The design system ID (`ds-...`).


- `fileNames` (string[], required): Array of file names/paths to read (as listed by `get_design_system`).


*Returns:*
    * `files` — array of `{ name, content }` for each matched file

- `create_design_system` (Tool): Creates a new, blank design system owned by you and returns its ID and editor URL. Seeds an empty initial version so you can immediately write files into it.

> ℹ️ **Note:**
> This creates a **blank** design system. Forking from an existing design system
>     is not supported through the MCP. After creating, load the
>     `design_system_authoring_guide` prompt and write files with
>     `write_design_system_files`.


*Parameters:*

- `name` (string, required): The name of the new design system.


- `logo` (string): Optional logo URL. Defaults to a placeholder.


*Returns:*
    * `designSystemId` — the new design system ID
    * `name` — the design system name
    * `editorUrl` — URL to edit the design system

- `write_design_system_files` (Tool): Creates or overwrites files in a design system. Incoming files are merged onto the existing artifact (existing files are preserved), then compiled and activated immediately.

> ℹ️ **Note:**
> This tool is **permissive**: it saves your files and returns
>     `validationErrors` *without* blocking, so you can build incrementally. Fix all
>     validation errors before calling `publish_design_system`, which is strict.


*Parameters:*

- `designSystemId` (string, required): The design system ID (`ds-...`).


- `files` (array, required): Array of files to create or overwrite. Each entry has: - `fileName` — the
      file path (e.g. `components/Button/index.tsx`, `index.css`,
      `rules/setup.md`) - `content` — the full file contents to write


- `baseArtifactId` (string): The `artifactId` from `get_design_system`. If the active artifact has since
      changed, the write is rejected with a **409** so you can re-read and retry.


*Returns:*
    * `artifactId` — the new active artifact ID
    * `files` — updated list of all file names in the design system
    * `validationErrors` — non-blocking validation issues to fix before publishing

- `publish_design_system` (Tool): Publishes the design system's active artifact as a new immutable version.

> ℹ️ **Note:**
> This tool is **strict**: it refuses if the active artifact has validation
>     errors. Run `write_design_system_files` and clear all `validationErrors`
>     first. A breaking change (e.g. a removed component or prop) bumps the **major**
>     version; otherwise the **minor** version is incremented.


*Parameters:*

- `designSystemId` (string, required): The design system ID (`ds-...`).


*Returns:*
    * `version` — the new version (`{ major, minor }`)
    * `isBackwardsCompatible` — whether the version is backwards-compatible with the previously published version
    * `reason` — explanation when the change is breaking

***

#### Inspiration Tools

These tools publish and manage a Magic Patterns **inspiration document** — a
shareable `magicpatterns.com/inspiration/<id>` link that renders 4 design
**concepts** (variants) side by side. Each concept is a self-contained sketch
of a UI direction.

- `create_inspiration_document` (Tool): Creates an inspiration document and returns a shareable URL. Declare each concept's `name`/`description` **without** `html` to publish the link immediately, then stream each concept in with `inspiration_add_variant`. You may also pass `html` inline to publish concepts fully in one call.

*Parameters:*

- `title` (string): Short label for what the concepts explore (e.g. "Projects list empty state").


- `files` (array, required): 1–8 concepts, each with: - `name` — the concept name - `description` —
      one-line description of the direction - `html` — the full, self-contained
      concept content (omit to declare a placeholder to fill later)


- `repositoryUrl` (string): Optional GitHub repo URL the concepts were generated from (kept for context).


- `baseline` (object): Optional baseline the variants diverge from: `{ html, focus, sharedCopy,
                baselineStyle }` where `html` is a faithful recreation of the current UI's content.


*Returns:*
    * `id` — the inspiration document ID
    * `url` — the shareable URL (login may be required)
    * `variants` — array of `{ id, name }`; pass each `id` to `inspiration_add_variant`

- `inspiration_add_variant` (Tool): Fills in one placeholder concept with its content. The concept renders live on the shared page as soon as its content arrives; the document flips to "ready" once every concept is filled.

*Parameters:*

- `inspirationId` (string, required): The inspiration document ID from `create_inspiration_document`.


- `variantId` (string): The concept ID to fill. If omitted, the first still-empty concept is filled.


- `name` (string): Optional update to the concept's name.


- `description` (string): Optional update to the concept's design direction.


- `html` (string, required): The full, self-contained concept content (non-empty).


*Returns:*
    * `ok` — whether the concept was filled
    * `variantId` — the filled concept ID
    * `url` — the shareable URL

- `get_inspiration_document` (Tool): Loads an inspiration document by its ID. Use this to read concepts back — for example, to implement a specific concept ("Implement Concept B from inspiration `<id>`").

*Parameters:*

- `inspirationId` (string, required): The inspiration document ID (the `<id>` in `magicpatterns.com/inspiration/<id>`).


*Returns:*
    * `title`, `userPrompt` — the original request the concepts explore
    * `status` — `generating` while concepts are still being produced, else `ready`/`error`
    * `variants` — the concepts in order (Concept A = `variants[0]`, etc.), each with `{ id, name, description, implementationPrompt, html, status }`


> ℹ️ **Note:**
> A concept is only usable once its `status` is `ready`; a non-ready one has empty/partial `html`.

- `inspiration_update_variant` (Tool): Revises a single **already-filled** concept in place, replacing its content (and optionally its name/description). Use this to update a subset of concepts without touching the others.

*Parameters:*

- `inspirationId` (string, required): The inspiration document ID.


- `variantId` (string, required): The concept ID to revise (from `get_inspiration_document`). Targets an
      existing filled concept, unlike `inspiration_add_variant`.


- `name` (string): Optional update to the concept's name.


- `description` (string): Optional update to the concept's design direction.


- `html` (string, required): The full, self-contained concept content (non-empty).


*Returns:*
    * `ok` — whether the concept was updated
    * `variantId` — the revised concept ID
    * `url` — the shareable URL

- `inspiration_clear_variants` (Tool): Resets **every** concept back to an empty placeholder — dropping each concept's content and its pre-created "Iterate" room. Use this to replace all concepts with a fresh set of directions.

*Parameters:*

- `inspirationId` (string, required): The inspiration document ID.


*Returns:*
    * `ok` — whether the concepts were cleared
    * `url` — the shareable URL
    * `variants` — array of `{ id, name }`; each keeps its ID and name for refilling via `inspiration_add_variant`

#### Video Walkthrough

Getting existing code from your codebase into Magic Patterns:

### Overview of MCP
*Workflow to go roundtrip between design and code*

**Source:** https://www.magicpatterns.com/docs/documentation/features/mcp-server/overview

> ℹ️ **Note:**
> MCP integration requires a paid plan. [Upgrade
>   here](https://www.magicpatterns.com/dashboard?dl=billing).

The Magic Patterns MCP ("Model Context Protocol") can help you bring Magic Patterns designs into other AI tools like Cursor, Claude Code, Codex, or directly in Claude.ai. It can also be used to import existing layouts and designs from your codebase into Magic Patterns.

The MCP is a standardized way for connecting AI agents, like Magic Patterns, to other tools.

#### Connection Options


- **[Official Claude Connector](#official-claude-connector)** — One-click setup directly in Claude.ai


- **[Official Cursor Plugin](#official-cursor-plugin)** — One-click install from the Cursor Marketplace


- **[Custom MCP Setup](#custom-mcp-setup)** — Configure in Cursor, Claude Code, Codex, or other MCP clients


- **[API Key Authentication](#api-key-authentication)** — Authenticate with an API key instead of OAuth

***

#### Official Claude Connector

Magic Patterns is available as an official **Connector** directly in [Claude.ai](https://claude.ai/). This is the easiest way to get started - no configuration required.


**Open Claude.ai and navigate to Connectors**

    In Claude.ai, click on the Connectors icon or navigate to your integrations settings.


**Find Magic Patterns**

    Search for "Magic Patterns" in the available connectors and click to connect.


![Magic Patterns Connector in Claude.ai](https://cdn.magicpatterns.com/uploads/8BKaYASmYXx3oaQncgLUUg/connector.png)




**Authorize and start using**

    Complete the authorization flow, and you're ready to use Magic Patterns directly in Claude conversations.

***

#### Official Cursor Plugin

Magic Patterns is available as an official plugin in the Cursor Marketplace. This is the easiest way to use Magic Patterns from Cursor. Installing the plugin wires up the MCP server for you and bundles a set of skills that teach the agent Magic Patterns workflows.


![Magic Patterns plugin in the Cursor Marketplace](https://cdn.magicpatterns.com/uploads/7KcGbsmLko2u1XsmJJoagd/Magic-Patterns-Cursor-Plugin.png)


**Open the Cursor Marketplace**

    In Cursor, go to **Settings → Plugins** (or open the Marketplace) and search for **Magic Patterns**.


**Install the plugin**

    Click **Install**. The plugin registers the Magic Patterns MCP server automatically and adds the Magic Patterns skills.


**Authenticate and start building**

    Complete the OAuth flow to connect your Magic Patterns account, then prompt Cursor to prototype, generate inspiration with "/inspiration", upload local UI, or integrate a design.

The plugin bundles these skills:

| Skill                             | What it does                                                                                                                |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `prototype`                       | Prototype an idea in Magic Patterns, seeded from your local UI, then iterate into a live design and open it in the browser. |
| `inspiration`                     | Generate four bold, meaningfully-different design directions and publish a shareable comparison link.                       |
| `upload-to-magic-patterns`        | Port local UI into a hosted design, then return the editor link.                                                            |
| `integrate-magic-patterns-design` | Adapt a Magic Patterns design into your existing codebase as production code.                                               |

> 💡 **Tip:**
> The plugin is a **superset of the MCP**. It installs the same MCP server, but also ships skills the raw MCP can't, most notably `/inspiration`, which recreates a faithful baseline of your current UI and generates several distinct design directions as a shareable `magicpatterns.com/inspiration/<id>` link.

***

#### Custom MCP Setup

For tools like Cursor, Claude Code, or Codex, you can configure the Magic Patterns MCP server manually.

> 💡 **Tip:**
> For best results, also add the [Integration Skill](/documentation/exporting/integration-skill) to Cursor or Claude Code. It tells the agent to treat the design as a spec and adapt it to your codebase's components and conventions, rather than pasting the prototype verbatim.


**Tab: Cursor**


**Add to your MCP config**

        Create a `.cursor/mcp.json` in your project for project-specific tools. [Cursor instructions here](https://cursor.com/docs/context/mcp#configuration-locations).

        ```json theme={null}
        {
          "mcpServers": {
            "magic-patterns": {
              "url": "https://mcp.magicpatterns.com/mcp"
            }
          }
        }
        ```


**Verify MCP is enabled**

> ⚠️ **Warning:**
> **IMPORTANT:** If Cursor browses the web instead of using the MCP tools, it means it's not working!
>
>           Ensure the MCP is actually turned on and not globally ignored. You can check this in Cursor's settings. Check "magic-patterns" to on!
>
>
>
![Ensure MCP is enabled in Cursor settings](https://cdn.magicpatterns.com/uploads/cow4Qr9Xa7gNAqkGXMUb2U/Ensure-MCP-is-On.png)

>




**Reference your designs**

        Once connected, you can prompt Cursor to access a specific design. For example:

        ```
        Integrate this design: https://www.magicpatterns.com/c/abcd into my project
        ```



    ### Cursor Troubleshooting

> ⚠️ **Warning:**
> Ensure that all the Tools are enabled in Cursor's settings. Go to **Cursor >
>       Settings > Cursor Settings** > MCP & Tools



![Cursor Settings for MCP](https://cdn.magicpatterns.com/uploads/m8ueXcDq8dUxorbi9yzdV5/mcp-cursor-settings.png)




**Tab: Claude Code**


**Add Magic Patterns MCP**

        Run the following command to add the Magic Patterns MCP server:

        ```bash theme={null}
        claude mcp add --transport http magic-patterns https://mcp.magicpatterns.com/mcp
        ```


**Authenticate**

        Run `/mcp` inside Claude Code to trigger the OAuth authentication that enables the Magic Patterns Remote MCP Server.


**Reference your designs**

        Once connected, you can prompt Claude Code to access a specific design. For example:

        ```
        Integrate this design: https://www.magicpatterns.com/c/abcd into my project
        ```




**Tab: Codex**

> ℹ️ **Note:**
> Codex does not support OAuth, so you must authenticate with a [Magic Patterns API key](#api-key-authentication) passed as a custom header.



**Create an API key**

        Open [Settings → API Keys](https://www.magicpatterns.com/settings/api-keys) and click **Create Key**. Copy the key immediately — you can only see it once.


**Add a custom MCP in Codex**

        In Codex, go to **Settings → Plugins → MCP** and choose **Connect to a custom MCP**. Fill in the form:

        * **Name**: `magic-patterns`
        * **Type**: select **Streamable HTTP**
        * **URL**: `https://mcp.magicpatterns.com/mcp`

        Then add two custom headers:

        | Key               | Value                         |
        | ----------------- | ----------------------------- |
        | `Authorization`   | `Bearer mp_your_api_key_here` |
        | `x-mp-agent-name` | `codex`                       |

        The `Authorization` header authenticates you with your API key, and `x-mp-agent-name` identifies the agent for attribution in the Magic Patterns UI.


![Connect to a custom MCP form in Codex](https://mintcdn.com/magicpatterns/8weWbctTIu3dy8jZ/documentation/features/mcp-server/images/codex-custom-mcp.png?fit=max&auto=format&n=8weWbctTIu3dy8jZ&q=85&s=97b6bd6319291fe6e6f2a75c9ea85ce8)




**Save and reference your designs**

        Click **Save**. Once connected, you can prompt Codex to access a specific design. For example:

        ```
        Integrate this design: https://www.magicpatterns.com/c/abcd into my project
        ```




> 💡 **Tip:**
> If you'd rather not paste the key directly, store it in an environment variable and use Codex's **Bearer token env var** field (or **Headers from environment variables**) instead of a plain header.

##### Read-only mode

If you want to expose Magic Patterns to an AI client without granting permission to create, modify, or publish designs, point the client at the read-only endpoint `https://mcp.magicpatterns.com/mcp/readonly` instead of `https://mcp.magicpatterns.com/mcp`. The same OAuth flow and API keys work against both URLs.

Only the following tools are exposed on the read-only endpoint:

* `list_design_systems`
* `get_editor_id_from_url`
* `get_inspiration_document`
* `get_design_status`
* `read_recent_message_history`
* `list_version_history`
* `get_artifact`
* `read_artifact_files`
* `get_design_system`
* `read_design_system_files`

Destructive tools (`create_design`, `create_slide_deck`, `send_prompt`, `create_new_artifact`, `write_artifact_files`, `publish_artifact`, `create_design_system`, `write_design_system_files`, `publish_design_system`, `create_inspiration_document`, `inspiration_add_variant`, `inspiration_update_variant`, `inspiration_clear_variants`) are not registered on this endpoint, so the client cannot list or call them.


**Tab: Cursor**

    ```json theme={null}
    {
      "mcpServers": {
        "magic-patterns": {
          "url": "https://mcp.magicpatterns.com/mcp/readonly"
        }
      }
    }
    ```


**Tab: Claude Code**

    ```bash theme={null}
    claude mcp add --transport http magic-patterns https://mcp.magicpatterns.com/mcp/readonly
    ```


**Tab: Codex**

    Follow the [Codex setup](#custom-mcp-setup) as usual, but enter `https://mcp.magicpatterns.com/mcp/readonly` in the **URL** field instead.

***

#### API Key Authentication

If you prefer not to use OAuth, you can authenticate the MCP server with a Magic Patterns API key. This is useful for headless environments, CI, or any client where the interactive OAuth flow is impractical. The same API key also works for the [v3 REST API](/api/getting-started) and the legacy v2 API.


**Create an API key**

    Open [Settings → API Keys](https://www.magicpatterns.com/settings/api-keys) and click **Create Key**. Copy the key immediately — you can only see it once.


**Pass the key as a Bearer token**

    Configure the MCP server exactly as in [Custom MCP Setup](#custom-mcp-setup), but add an `Authorization: Bearer <your-api-key>` header. When a key is present, the OAuth flow is skipped entirely.


**Tab: Cursor**

        ```json theme={null}
        {
          "mcpServers": {
            "magic-patterns": {
              "url": "https://mcp.magicpatterns.com/mcp",
              "headers": {
                "Authorization": "Bearer mp_your_api_key_here"
              }
            }
          }
        }
        ```


**Tab: Claude Code**

        ```bash theme={null}
        claude mcp add --transport http magic-patterns https://mcp.magicpatterns.com/mcp \
          --header "Authorization: Bearer mp_your_api_key_here"
        ```


**Tab: Codex**

        Codex doesn't support OAuth, so the API key is the only way to connect. In **Settings → Plugins → MCP**, add a custom MCP with type **Streamable HTTP** and an `Authorization: Bearer mp_your_api_key_here` header. See the [Codex tab in Custom MCP Setup](#custom-mcp-setup) for the full walkthrough.




**(Optional) Identify your agent**

    Pass the `x-mp-agent-name` header to tag requests with your agent or integration name. This is optional but helps with attribution in the Magic Patterns UI.

You can also call the underlying REST endpoints directly (bypassing the MCP transport) with the API key in either the `Authorization: Bearer` or `x-mp-api-key` header:

```bash theme={null}
curl -X POST https://api.magicpatterns.com/mcp/design/create \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer mp_your_api_key_here" \
  -H "x-mp-agent-name: my-custom-agent" \
  -d '{"prompt": "A dashboard with a sidebar and chart"}'
```

> ℹ️ **Note:**
> API key authentication requires a paid plan. Usage is billed against your account's normal credits, the same as OAuth and the web app.

***

#### Next Steps


- **[Tools & Workflows](/documentation/features/mcp-server/available_tools)** — Explore the available MCP tools and learn common workflows for design-to-code and code-to-design.


- **[Integration Skill](/documentation/exporting/integration-skill)** — A drop-in skill that teaches your AI editor to adapt a Magic Patterns design into your codebase the right way.

### Features
*Explore all the features Magic Patterns has to offer*

**Source:** https://www.magicpatterns.com/docs/documentation/features/overview

For full sidebar navigation for design systems and team workflows, use the Design Systems and Team Collaboration tabs at the top of the docs.

#### Features

##### Design Systems


- **[Design Systems](/documentation/design-systems/overview)** — Create unified styling and reusable components for consistent designs.


- **[Components](/documentation/design-systems/editing/components)** — Build and manage reusable UI components in your Design System.


- **[Rules](/documentation/design-systems/editing/rules)** — Define default styling rules for consistent designs across your team.


- **[Colors](/documentation/design-systems/editing/colors)** — Define your color palette for AI generation and the Visual Edit color picker.


- **[Typography](/documentation/design-systems/editing/typography-and-icons)** — Manage font groups: upload custom fonts, Google Fonts, or font URLs.


- **[Icons](/documentation/design-systems/editing/typography-and-icons#icons)** — Manage icon libraries or import custom icons for your designs.

##### Visual Edit & Agent Mode


- **[Visual Edit](/documentation/editor/how-to-prompt)** — Select any element and edit its styles, text, and layout visually.


- **[Agent Mode](https://www.magicpatterns.com/blog/agent-mode)** — AI architecture with automatic model routing, website browsing, and context-aware generation.


- **[Plan Mode](/documentation/editor/plan-mode)** — Brainstorm and align on a plan with the agent before any code is written.

##### Import & Export


- **[Import from Website](/documentation/get-started/chrome-extension)** — Import designs from any website, including localhost.


- **[Import from Figma](/documentation/importing/import-from-figma)** — Bring your Figma designs into Magic Patterns.


- **[Sync with Github](/documentation/get-started/sync-to-github)** — Two-way sync between Magic Patterns and your Github repository.


- **[Download Code](/documentation/get-started/download-code)** — Download your design code as a zip file.


- **[Forking](/documentation/editor/forking)** — Create a copy of your design to explore new ideas.


- **[MCP Server](/documentation/features/mcp-server/overview)** — Connect your IDE or AI assistant to Magic Patterns via the Model Context Protocol.

##### Team Collaboration


- **[Team Workspaces](/documentation/collaboration/team-workspaces)** — Manage team members, share Design Systems and components, and centralize billing.


- **[Sharing Designs](/documentation/editor/sharing)** — Share your designs with team members and stakeholders.


- **[Live Multiplayer](/documentation/collaboration/live-multiplayer)** — Work on the same design or canvas with your team in real time.


- **[Inline Comments](/documentation/collaboration/inline-comments)** — Leave feedback directly on any element in a design.


- **[Canvases](/documentation/projects/how-to-share)** — Collaborate with your team in real-time.

##### Connectors


- **[Connectors](/documentation/connectors/connectors)** — Pull context from Notion, Linear, Granola, PostHog, and other connected tools into your designs.

##### Publishing


- **[Custom Publish URL](/documentation/publishing/publish-url)** — Publish instantly to a shareable Magic Patterns URL.


- **[Host on a Custom Domain](/documentation/get-started/custom-domain)** — Host your designs on your own custom domain.

##### Integrations


- **[OpenAI](/documentation/integrations/openai)** — Build AI-powered features using the OpenAI API.


- **[Google Sheets](/documentation/integrations/google-sheets)** — Read and write data from Google Sheets.


- **[Google Analytics](/documentation/integrations/google-analytics)** — Track page views and user behavior with Google Analytics.


- **[See All Integrations](/documentation/integrations/overview)** — Explore all supported third-party tools and services.


---

## Connectors

### Connectors
*Connect your tools, databases, and apps to Magic Patterns for more relevant AI responses.*

**Source:** https://www.magicpatterns.com/docs/documentation/connectors/connectors

#### What are Connectors?

Connectors let Magic Patterns work with your external tools, databases, and applications to give you more relevant responses. Powered by the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), connectors allow the AI assistant to pull in real context from the services you already use -- like meeting notes, project issues, or analytics data -- and incorporate it directly into your designs.

When a connector is enabled, the AI assistant can discover and call tools exposed by the connected service. For example, if you connect Granola, the assistant can pull your recent meeting notes and use them to inform a design.

#### Available Connectors

Magic Patterns ships with built-in support for the following services:

| Connector   | Description                                                              |
| ----------- | ------------------------------------------------------------------------ |
| **Granola** | Pull meeting notes and context into your designs.                        |
| **Notion**  | Pull pages, databases, and content from your Notion workspace.           |
| **Linear**  | Pull issues, projects, and roadmaps from Linear.                         |
| **Jira**    | Pull issues, sprints, and project context from Atlassian Jira.           |
| **Miro**    | Pull boards, frames, and visual context from Miro.                       |
| **Mobbin**  | Pull real-world UI screens, user flows, and design patterns from Mobbin. |

More connectors are being added regularly. You can also [add your own custom MCP server](#adding-a-custom-mcp-server).

#### Getting Started with Connectors

This walkthrough uses **Granola** as an example, but the steps are the same for any built-in connector.


**Open the Connectors Menu**

    In the editor, open the prompt bar dropdown and select the **Connectors** section. You will see a list of available connectors you can connect.


![Connectors menu in the prompt bar](https://cdn.magicpatterns.com/uploads/mD9fR7kytQYP8Ch6J6S5NB/pick-connector.png)




**Connect a Service**

    Click the connector you want to enable (e.g. Granola). An OAuth dialog will appear.


**Authorize Access**

    Click **Connect with OAuth**. A popup window will open asking you to sign in and authorize Magic Patterns to access your account. Once you approve, the popup will close and the connector will show as **Connected**.


![OAuth authorization flow for Granola](https://cdn.magicpatterns.com/uploads/g5y1JZmmGwMamJ5Bhwn7tH/granola-oauth.png)




**Use It in Your Prompts**

    Once connected, the AI assistant will automatically have access to the tools exposed by your connector. Just mention the data you need in your prompts and the assistant will pull it in:

    * "Pull my latest meeting notes from Granola and design a summary dashboard"
    * "What did we discuss in yesterday's standup? Use that to create a task board"

    The assistant handles the connector calls behind the scenes and incorporates the returned data into your design.

#### Managing Connectors


![Connectors settings page](https://cdn.magicpatterns.com/uploads/scRUd2jRLCHtG3WccKQgG2/connectors.png)

From the **Connectors** section in Settings, you can:

* Enable / Disable a connector using the toggle switch. Disabled connectors are not used by the AI assistant but remain connected.
* Re-authenticate a connector by clicking the refresh icon. This is useful if your access token has expired.
* Disconnect a connector by clicking the trash icon. This removes the connector and its stored credentials entirely.

You can also manage connectors from the **Connectors** submenu in the editor prompt bar.

#### Adding a Custom MCP Server

If your team runs a custom MCP server, you can connect it to Magic Patterns directly.


**Open Connector Settings**

    In the editor, open the prompt bar dropdown and select the Connectors
    section. At the bottom, click Manage Connectors to open the Connectors
    settings page.


**Click Add Custom Connector**

    On the Connectors settings page, click the Add Custom Connector button at
    the bottom of the list.


**Enter Server Details**

    Provide a Name (how it will appear in the UI) and the MCP Server URL (for
    example, [https://mcp.yourcompany.com/mcp](https://mcp.yourcompany.com/mcp)).


**Authenticate**

    After adding the connector, click Connect to begin the OAuth flow. Magic
    Patterns will automatically discover your server's OAuth endpoints via the
    standard well-known metadata endpoints.

> ⚠️ **Warning:**
> Only connect to MCP servers that you trust — Magic Patterns will be able to call any tools they expose. Your credentials are encrypted and never exposed to the frontend. Custom servers must support OAuth 2.0 and be publicly reachable.

#### How It Works

Connectors use the **Model Context Protocol (MCP)**, an open standard for connecting AI assistants to external data sources and tools.

1. When you connect a service, Magic Patterns performs OAuth 2.1 dynamic client registration with the MCP server's authorization server.
2. OAuth endpoints are discovered automatically via well-known metadata -- no manual configuration needed.
3. When the AI assistant needs data from a connector, it calls the MCP server's tools using the stored access token.
4. Tool results are returned to the assistant and incorporated into its response. You can expand any connector tool call in the chat to see the raw result.


---

## Integrations

### Anthropic
*Learn how to integrate Anthropic into your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/anthropic

#### Introduction to Anthropic

Want to build a chat app or AI assistant on Magic Patterns? You can use our Anthropic integration to create fully functional AI apps that leverage the latest Claude models from Anthropic.

#### Step by Step Tutorial


**Create an Anthropic Account**

    Create a new Anthropic account if you don't already have one at [console.anthropic.com](https://console.anthropic.com).


**Set up billing**

    **This is a required step:** You need to add a payment method and set up billing on your Anthropic account before you can use the API.

    Without billing configured, your API key will not work and API calls will fail.

    You can [set up billing here](https://console.anthropic.com/settings/billing).


**Create a new Anthropic API Key**

    Magic Patterns uses the Anthropic API to communicate with Anthropic's services.
    Your API key is sensitive and should be stored securely—never share it
    directly in prompts to Magic Patterns.

    You can [create a new API key here](https://console.anthropic.com/settings/keys).


**(Optional) Set a usage limit**

    We highly recommend setting a usage limit on your Anthropic account. This
    protects you from unexpected charges in case your API key is accidentally
    exposed or compromised.


**Enable the Anthropic Integration in Magic Patterns**

    Once you have your API key, enable the integration in Magic Patterns via the integrations section in the chatbar.

![Integrations in the chatbar](https://cdn.magicpatterns.com/uploads/bhuL6kJSi7iUbGQUw76eXj/integrations.png)


**Prompt Magic Patterns to use Anthropic**

    By default, Magic Patterns will not connect to Anthropic. Once the integration is enabled, you can
    prompt along the lines of "Connect this design to Anthropic" and Magic Patterns will then integrate your design.

> ⚠️ **Warning:**
> Once a design is connected to Anthropic, anyone you share the design or preview
>   link with will be able to use the AI features. This will consume your Anthropic
>   API credits.

### Collecting Feedback
*Gather structured feedback from external users on your prototypes*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/collecting-feedback

Magic Patterns lets you collect structured feedback directly through your shared designs. This is perfect for gathering insights from customers and other external stakeholders.

![Collecting feedback in Magic Patterns](https://cdn.magicpatterns.com/uploads/bhuL6kJSi7iUbGQUw76eXj/integrations.png)

#### Setting Up Feedback Collection


**Open the chatbar**

    Open the chatbar in your design and locate the integrations section.


**Enable external feedback collection**

    In the integrations section, click on "Collect Feedback," toggle it on, and
    configure your custom questions.


**Add custom questions**

    Create questions for your stakeholders to answer when they view your design.


**Share the Publish link**

    Send the preview link to your external stakeholders. They'll see your
    questions when viewing the design.


**Review feedback**

    View all collected feedback in the integrations panel by clicking on
    "Download Feedback."

#### Video Tutorial

> 💡 **Tip:**
> **This feature has moved to the chatbar.** In the video, you will see it under
>   Share, but currently you will find it in the **integrations section of the
>   chatbar**. Everything else is the same!

### EmailJS
*Learn how to integrate EmailJS to send emails directly from your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/emailjs

#### Introduction to EmailJS


  [
    EmailJS
  ](https://www.emailjs.com/)

  {` `}lets you send emails directly from client-side code. You can create
  dynamic templates and trigger emails with just a few lines of JavaScript.


#### Step by Step Tutorial

This tutorial walks you through setting up EmailJS to send emails directly from your Magic Patterns design with no database required.


**Create an EmailJS Account**

    Create an EmailJS account and connect your email service.

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/integrations/images/emailjs-email-services.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=60ecfaedc5b141cec6fd961cd294ad96)



**Go to EmailJS and create a free account.**

        Create a free EmailJS account.


**Add new email service.**

        Navigate to Email Services and click *Add New Service*.


**Choose your email provider.**

        Choose from services like Gmail, Outlook, or a custom SMTP server.





![image](https://cdn.magicpatterns.com/emailJS-content-2.gif)



**Go to the Email Templates section and create a new template.**

**Navigate to Code Editor and edit your content.**

        Click Edit Content and then Code Editor. We recommend replacing the body of the message with the following code, which is a placeholder that will be replaced with the content of the email:

        ```
        {{content}}
        ```

> 💡 **Tip:**
> Ask Magic Patterns to design an email template to customize the look and feel of your emails.




**Add your Domain**

    Go to *Account → Security* and add an approved domain for email sending (e.g. yourdomain.com).

![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/integrations/images/emailjs-domain.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=eec16c24091f60217032bf6583c37d15)


**Collect Required Credentials**

    * **EmailJS Public Key**: can be found under *Account → API Keys*.
    * **Service ID**: can be found under *Email Services*.
    * **Template ID**: can be found under *Email Templates → Settings*.


**Prompt Magic Patterns to integrate EmailJS**

    Use the Select tool to click on your call to action button if applicable. Then, enter the following prompt:

    ```
    Implement the "Try Beta" email sign up form using EmailJS to send an email.

    EmailJS Public Key: {{emailjs_public_key}}
    Service ID: {{service_id}}
    Template ID: {{template_id}}

    Inside my email template, it just takes a body with the parameter "{{content}}". Please just send me the user inputted email.
    ```

#### FAQ


**Can I use EmailJS for free?**

    EmailJS' Free plan offers 200 monthly emails a month.


**Can I customize the design of the emails I send?**

    You can design your own on Magic Patterns or use a open-source library like [React Email](https://react.email/) with templates.


**I have more questions about EmailJS.**

    Please visit the [EmailJS documentation](https://www.emailjs.com/docs) for more information.

### Google Analytics
*Learn how to integrate Google Analytics into your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/google-analytics

#### Step by Step Tutorial

Google Analytics helps you understand how people use your website or app.

For installing Google Analytics, we recommend prompting your code snippet using the [meta tag method](https://support.google.com/webmasters/answer/9008080?hl=en#meta_tag_verification).

```Example Installing Google Analytics Prompt theme={null}
Please help me implement Google Analytics using the react-ga4 package. Here is the snippet from Google:

<the code snippet from Google>
```

### Google Sheets
*Learn how to save submissions to Google Sheets from your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/google-sheets

#### Overview

Connect your design to Google Sheets to automatically save data. This is perfect for collecting emails, contact forms, waitlists, or anything that requires a very light database.

#### Step by Step Tutorial

##### 1. Get Your Custom Apps Script

First, switch to `/Ask` mode in Magic Patterns to ask what columns and Apps Script you need for your specific design:

Example Prompt:

```
I want to connect this design to Google Sheets to save form submissions.

What column headers should I add to my Google Sheet, and what Google Apps Script should I use to receive the data?

Please note my plan is to structure it like this:

const GOOGLE_SCRIPT_URL = 'TODO: I WILL PROVIDE YOU WITH THIS'

export async function submitToGoogleSheets(
  data: Record<string, any>,
): Promise<{ success: boolean; error?: string }> {
  try {
    const response = await fetch(GOOGLE_SCRIPT_URL, {
      method: 'POST',
      mode: 'no-cors', // Required for Google Apps Script
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })

    return { success: true }
  } catch (error) {
    console.error('Error submitting to Google Sheets:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
    }
  }
}
```


![Using /Ask mode to get your custom Apps Script](https://cdn.magicpatterns.com/static/docs/Gsheet-prompt1.png)

> 💡 **Tip:**
> The Magic Patterns AI will generally guide you on Step 2 and 3 after the
>   prompt from Step 1, but we have included the steps below for reference.

##### 2. Create Your Google Sheet

* Go to [sheets.google.com](https://sheets.google.com) and create a new sheet
* Add the column headers from Step 1 in the first row

##### 3. Set Up Google Apps Script

1. In your Google Sheet, go to **Extensions > Apps Script**
2. Paste the Apps Script code from step 1
3. Click **Deploy > New deployment**
4. Click the gear icon and choose **Web app**
5. Set "Execute as" to **Me**
6. Click **Deploy**
7. **IMPORTANT:** Set "Who has access" to Anyone
8. Authorize the app when prompted
9. Copy the **Web app URL** (looks like: `https://script.google.com/macros/s/.../exec`)


![Setting up the Web app deployment](https://cdn.magicpatterns.com/static/docs/Gsheet-webapp.png)

> 💡 **Tip:**
> IMPORTANT: Set "Who has access" to Anyone, otherwise you will likely get a
>   CORS error.

##### 4. Connect Your Design

Use this prompt in Magic Patterns, replacing the URL with your Web app URL from step 3:

Example Prompt:

```
[YOUR LINK FROM STEP 3]

Here is my Google Web app URL!
```


![Copying the Web app URL](https://cdn.magicpatterns.com/static/docs/Gsheet-url.png)

### LinkedIn
*Make your experience with Magic Patterns visible with LinkedIn Connected Accounts*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/linkedin

#### Why connect LinkedIn?

Connecting LinkedIn will highlight your experience with Magic Patterns on your LinkedIn profile. It's a
verified signal that shows you build with Magic Patterns, and it sits in the Connected Apps
section of your profile where anyone who visits can see it: recruiters, clients,
teammates.

#### How to connect


**Open your profile settings**

    Go to Settings, then Profile, then Connected Accounts, and find the LinkedIn
    card.


![The LinkedIn card in Settings → Profile → Connected Accounts, before connecting](https://cdn.magicpatterns.com/uploads/poBALjb2AVSg6PRVuEmK91/connect-to-linkedin-docs.png)




**Click Connect to LinkedIn**

    LinkedIn opens a window asking for your permission. We only ask for the one
    thing we need, which is permission to add your skill badge.


![The LinkedIn permission window showing the requested access](https://cdn.magicpatterns.com/uploads/fAEmbZcDSCZsiyo3pR8PEc/CleanShot_2026-06-04_at_14.56.16.png)




**Click Allow**

    That's it. Your badge is added to your LinkedIn profile automatically, and the
    card shows as connected.


![The LinkedIn card in Settings showing the connected state with a Disconnect button](https://cdn.magicpatterns.com/uploads/hvmAkGXnMckhTh6vmZaiQ9/CleanShot_2026-06-04_at_14.53.33.png)



#### Removing the badge

Changed your mind? Click Disconnect on the same LinkedIn card. We take the badge
off your LinkedIn profile right away and delete the connection on our side.

#### Your privacy


**What can Magic Patterns do on my LinkedIn?**

    Only one thing: add and later remove your Magic Patterns under Connected Accounts. You'll notice our permissions are tightly scoped; we
    can't read your messages, post on your behalf, or see your connections.


**Can I remove it later?**

    Yes, anytime. Hit Disconnect and the badge comes off your profile right away.


**The badge isn't showing up on my profile**

    It can take a moment to appear. If it still isn't there, try disconnecting
    and reconnecting. If that doesn't help, reach out to support at [support@magicpatterns.com](mailto:support@magicpatterns.com).

### Meta Pixel
*Learn how to integrate a Meta Pixel into your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/meta-pixel

#### Step by Step Tutorial

The Meta Pixel is a snippet of JavaScript code that loads a small library of functions you can use to track Facebook ad-driven visitor activity on your website.

For installing Meta Pixel, we recommend prompting your code snippet using the [base code method](https://developers.facebook.com/docs/meta-pixel/get-started#base-code).

```Example Installing Meta Pixel Prompt theme={null}
Please help me implement Meta Pixel. Here is the snippet from Meta:

Note: The pixel code is a placeholder code. You need to insert your own pixel code.

<!-- Facebook Pixel Code -->

<!-- End Facebook Pixel Code -->
```

### OpenAI
*Learn how to integrate OpenAI into your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/openai

#### Introduction to OpenAI

Want to build a chat app or AI assistant on Magic Patterns? You can use our OpenAI integration to create fully functional AI apps that leverage the latest models from OpenAI, the same company that build ChatGPT.


![OpenAI Integration](https://cdn.magicpatterns.com/static/marketing/openai-integration.gif)

#### Step by Step Tutorial


**Create an OpenAI Account**

    Create a new OpenAI account if you don't already have one.


**Set up billing**

    **This is a required step:** You need to add a payment method and set up billing on your OpenAI account before you can use the API.

    Without billing configured, your API key will not work and API calls will fail.

    You can [set up billing here](https://platform.openai.com/settings/organization/billing/overview).


**Create a new OpenAI API Key**

    Magic Patterns uses the OpenAI API to communicate with OpenAI's services.
    Your API key is sensitive and should be stored securely—never share it
    directly in prompts to Magic Patterns.

    You can [create a new API key here](https://platform.openai.com/api-keys).


**(Optional) Set a usage limit**

    We highly recommend setting a usage limit on your OpenAI account. This
    protects you from unexpected charges in case your API key is accidentally
    exposed or compromised.


**Enable the OpenAI Integration in Magic Patterns**

    Once you have your API key, enable the integration in Magic Patterns via the integrations section in the chatbar.

![OpenAI Integration in the chatbar](https://cdn.magicpatterns.com/uploads/9u92zsAsxWq3sopCfdpCoe/Open-ai-integration.png)


**Prompt Magic Patterns to use OpenAI**

    By default, Magic Patterns will not connect to OpenAI. Once the integration is enabled, you can
    prompt along the lines of "Connect this design to OpenAI" and Magic Patterns will then integrate your design.

> ⚠️ **Warning:**
> Once a design is connected to OpenAI, anyone you share the design or preview
>   link with will be able to use the AI features. This will consume your OpenAI
>   API credits.

### Overview
*Every third-party service Magic Patterns connects to*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/overview

Magic Patterns connects to the tools you already use for design, development, analytics, and collaboration.

You can access integrations from the chatbar within your design.

![Integrations in the chatbar](https://cdn.magicpatterns.com/uploads/kuq2RQ7CRV6vc9GcNruhae/integrations-chat-bar.png)

#### Design Tools


- **[Import from Figma](/documentation/importing/import-from-figma)** — Bring your Figma designs into Magic Patterns as editable code.


- **[Export to Figma](/documentation/get-started/figma-plugin)** — Export your designs to Figma for handoff or further design work.

#### Developer Tools


- **[Sync with GitHub](/documentation/get-started/sync-to-github)** — Two-way sync between Magic Patterns and your GitHub repository.


- **[MCP Server](/documentation/features/mcp-server/overview)** — Connect your IDE or AI assistant to Magic Patterns via the Model Context Protocol.

#### Connectors

Connectors let the AI assistant pull real context from external services into your designs. Connect via OAuth and the assistant handles the rest.


- **[Granola](/documentation/connectors/connectors)** — Pull meeting notes and context into your designs.


- **[Notion](/documentation/connectors/connectors)** — Pull pages, databases, and content from your Notion workspace.


- **[Linear](/documentation/connectors/connectors)** — Pull issues, projects, and roadmaps from Linear.


- **[PostHog](/documentation/connectors/connectors)** — Pull analytics, feature flags, and experiment data from PostHog.

You can also [add your own custom MCP server](/documentation/connectors/connectors#adding-a-custom-mcp-server) as a connector.

#### In-Design Services

These integrations work inside your published designs. Add API calls, analytics tracking, email forms, and more directly in your code.


- **[OpenAI](/documentation/integrations/openai)** — Build AI-powered features using the OpenAI API.


- **[Anthropic](/documentation/integrations/anthropic)** — Build AI-powered features using the Anthropic Claude API.


- **[Google Sheets](/documentation/integrations/google-sheets)** — Read and write data from Google Sheets.


- **[EmailJS](/documentation/integrations/emailjs)** — Send emails directly from your design without a backend.


- **[Collecting Feedback](/documentation/integrations/collecting-feedback)** — Gather structured feedback from external users on your prototypes.

#### E-commerce


- **[Shopify](/documentation/integrations/shopify)** — Create a landing page that links directly to your Shopify store and cart.

#### Connected Accounts


- **[Connect to LinkedIn](/documentation/integrations/linkedin)** — Highlight your experience with Magic Patterns on your LinkedIn profile.

#### Analytics


- **[Google Analytics](/documentation/integrations/google-analytics)** — Track page views and user behavior with Google Analytics.


- **[PostHog](/documentation/integrations/posthog)** — Track events and user behavior with PostHog.


- **[Meta Pixel](/documentation/integrations/meta-pixel)** — Track conversions and optimize ad campaigns with Meta Pixel.

### PostHog
*Learn how to integrate PostHog into your Magic Patterns design*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/posthog

#### Introduction to PostHog


  [
    PostHog
  ](https://www.posthog.com/)

  {` `}is an open-source product analytics platform that helps companies
  understand user behavior and improve their products. Track events, analyze
  user behavior, and make data-driven decisions.


#### Step by Step Tutorial

This tutorial walks you through setting up PostHog to capture analytics from your design directly.


**Create a PostHog Account**

    Create a new PostHog account if you don't already have one.

    Visit [PostHog signup](https://app.posthog.com/signup) to get started.


**Get Your Project Key and API Host**

    After creating your account, you'll need two pieces of information:

    * **Project Key**: Found in your project settings under *Project Settings → Project API Key*
    * **API Host**: Found in the same location, typically looks like `https://us.i.posthog.com` or `https://eu.i.posthog.com`

> 💡 **Tip:**
> The project key starts with `phc_` followed by a long string of characters.


**Prompt Magic Patterns to integrate PostHog**

    Use the following prompt to have Magic Patterns integrate PostHog into your design:

    ```
    Help me install PostHog using posthog-js

    Here is the project key: phc_YOUR_PROJECT_KEY_HERE

    Here is the PostHog host: https://us.i.posthog.com

    It should use PostHogProvider to wrap the app like this:

    import { PostHogProvider } from 'posthog-js/react'

    const options = {
      api_host: 'https://us.i.posthog.com',
      defaults: '2025-05-24',
    }



    ```

> ℹ️ **Note:**
> Replace the project key and API host with your actual values from Step 2.


**(Optional) Track Custom Events**

    Once PostHog is integrated, you can prompt Magic Patterns to track custom events:

    ```
    Add a PostHog event tracker when users click the "Sign Up" button.
    Track it as a "signup_button_clicked" event.
    ```

    Magic Patterns will use the PostHog `capture` method to track your custom events.

#### FAQ


**Is PostHog free to use?**

    PostHog offers a generous free tier with 1 million events per month. You can upgrade to paid plans as your usage grows.


**What kind of analytics can I track with PostHog?**

    PostHog automatically tracks page views and can track custom events like
    button clicks, form submissions, or any user interaction. It also supports
    feature flags, session recordings, and A/B testing.


**I have more questions about PostHog.**

    Please visit the [PostHog documentation](https://posthog.com/docs) for more information.

### Shopify
*Create a landing page in Magic Patterns that links directly to your Shopify store*

**Source:** https://www.magicpatterns.com/docs/documentation/integrations/shopify

This guide walks you through the full workflow: creating a landing page in Magic Patterns, hosting it on your own domain, and linking it to your Shopify store so visitors can buy your products directly.

This is a very common setup for businesses that already sell on Shopify and want a custom-designed landing page to drive traffic to their store.

**How it works:** your landing page lives on a subdomain (like `landing.yourbrand.com`) and when visitors click "Shop Now" or any product link, they go to your Shopify store on your root domain (`yourbrand.com`).

#### Step 1: Create Your Landing Page


**Sign in to Magic Patterns**

    Go to [magicpatterns.com](https://www.magicpatterns.com) and sign in or create a free account.


**Create a new design**

    Click **Create New Design** on your dashboard.


**Describe what you want**

    For example: *"Create a modern landing page for a skincare brand with a hero section, featured products, testimonials, and a footer."*

    You can also upload a screenshot of a landing page you like for inspiration. Just drag the image into the chat.


**Iterate on your design**

    Use the chat to make changes: *"Change the hero headline to 'Glow From Within'"* or *"Add a section showing our three best-selling products."*

    Keep going until you're happy with the design.

#### Step 2: Add Your Shopify Links

You can link your CTAs directly to a Shopify cart URL so that when someone clicks "Buy Now", the product is already in their cart. The link format is:

```
https://yourbrand.com/cart/VARIANT_ID:1
```

The `1` at the end is the quantity. Replace `VARIANT_ID` with the actual ID of the product variant you want to sell.

##### How to Find the Variant ID

1. Go to your Shopify admin panel (`yourbrand.myshopify.com/admin`).
2. Navigate to **Products** and click on the product you want to link.
3. If the product has variants (size, color, etc.), click on the specific variant.
4. The Variant ID is the number at the end of the URL in your browser's address bar: `admin/products/PRODUCT_ID/variants/VARIANT_ID`.

For example, if your variant ID is `41234567890123`, your cart link would be:

```
https://yourbrand.com/cart/41234567890123:1
```

Since most landing pages are built around a single product, the easiest approach is to update all buttons at once. Just type something like this in the chat:

*"Make all the CTAs on this page open this link in a new tab: [https://yourbrand.com/cart/41234567890123:1](https://yourbrand.com/cart/41234567890123:1)"*

#### Step 3: Publish Your Landing Page


**Publish your design**

    Click the **Publish** button at the top of the editor. Your design is now live on a free Magic Patterns URL (something like `project-abc123.magicpatterns.app`).


**Test your links**

    Open the link in a new browser tab and test that all your Shopify links work correctly.

At this point your landing page is live and working. If you're happy with the free URL, you're done. But most businesses want their own domain, so keep going.

#### Step 4: Set Up Your Domain

Most Shopify store owners already have their root domain (like `yourbrand.com`) pointing to their Shopify store. In that case, the recommended setup is:

| Domain                  | Points to                            |
| ----------------------- | ------------------------------------ |
| `yourbrand.com`         | Your Shopify store (keep this as-is) |
| `landing.yourbrand.com` | Your Magic Patterns landing page     |

> ℹ️ **Note:**
> We always recommend keeping your root domain pointed at Shopify and using a subdomain for your Magic Patterns landing page. Your Shopify store is your storefront and it should stay on the main domain for SEO and customer trust. The landing page works perfectly on a subdomain.

##### If You Don't Have a Domain Yet

Buy one from any registrar:

* [Namecheap](https://www.namecheap.com)
* [GoDaddy](https://www.godaddy.com)
* [Cloudflare Registrar](https://www.cloudflare.com/products/registrar)
* [Squarespace Domains](https://domains.squarespace.com)

Then point the root domain to your Shopify store (Shopify has [instructions for this](https://help.shopify.com/en/manual/domains/add-a-domain/connecting-domains)) and follow the steps below to connect a subdomain to Magic Patterns.

##### Connect a Subdomain to Magic Patterns


**Choose your subdomain**

    Pick a subdomain name. Common choices:

    * `landing.yourbrand.com`
    * `promo.yourbrand.com`
    * `go.yourbrand.com`


**Add a CNAME record in your DNS settings**

    Go to your domain registrar (or wherever your DNS is managed) and find the DNS settings. Add a CNAME record:

    | TYPE  | NAME    | VALUE             |
    | ----- | ------- | ----------------- |
    | CNAME | landing | magicpatterns.dev |

    Replace `landing` with whatever subdomain you chose.

> ⚠️ **Warning:**
> Do **not** change or delete the A record or CNAME for your root domain. That's what keeps your Shopify store working.


**Wait for DNS propagation**

    This can take anywhere from 5 minutes to 48 hours. Check the status at [whatsmydns.net/CNAME](https://www.whatsmydns.net/?t=CNAME). Enter your subdomain and look for `magicpatterns.dev` in the results.


**Connect the domain in Magic Patterns**

    1. Go back to your design in Magic Patterns and click the **Publish** button.
    2. Click **Add a custom domain**.
    3. Enter your subdomain (e.g. `landing.yourbrand.com`) and click **I have added DNS records**.
    4. Magic Patterns will verify the connection. Once verified, your landing page is live on your subdomain.

    We automatically set up SSL (HTTPS) for you, so your site is secure.

For more details on custom domains, see the [full custom domain guide](/documentation/get-started/custom-domain).

#### A Note About the Watermark

Designs published through Magic Patterns include a small "Built with Magic Patterns" badge. This badge is automatically hidden on any [paid plan](https://www.magicpatterns.com/dashboard?dl=billing). If you're on the free plan, the watermark will appear on your published site.

#### FAQ


**Can I use the same domain for both my landing page and Shopify store?**

    Not on the exact same domain. A domain can only point to one place. The recommended setup is:

    * **Root domain** (`yourbrand.com`) → Shopify store
    * **Subdomain** (`landing.yourbrand.com`) → Magic Patterns landing page

    This keeps your Shopify store on the main domain for SEO and customer trust, while your landing page lives on a subdomain.


**How do I find the Variant ID for a Shopify product?**

    1. Go to your Shopify admin → **Products** → click on the product.
    2. Click the specific variant (size, color, etc.).
    3. The Variant ID is the number at the end of the URL: `admin/products/PRODUCT_ID/variants/VARIANT_ID`.

    Use this ID to build a direct cart link: `https://yourbrand.com/cart/VARIANT_ID:1`


**Can I update my landing page after it's live?**

    Yes. Make changes in Magic Patterns and click **Publish** again. The update goes live immediately on your domain.


**Do I need to know how to code?**

    No. Magic Patterns generates all the code for you. You describe what you want in plain language.


**Can I add Google Analytics or Meta Pixel tracking to my landing page?**

    Yes. Magic Patterns supports [Google Analytics](/documentation/integrations/google-analytics), [PostHog](/documentation/integrations/posthog), and [Meta Pixel](/documentation/integrations/meta-pixel). You can add tracking directly in your design.


---

## Collaboration

### Inline Comments
*Leave feedback directly on specific elements in a design*

**Source:** https://www.magicpatterns.com/docs/documentation/collaboration/inline-comments

Inline comments let you leave feedback directly on specific elements in a design. This makes reviews faster, clearer, and easier to track across teammates and iterations.


![image](https://mintcdn.com/magicpatterns/r7WxSEN_k7EK12_1/documentation/collaboration/images/comments-full-sidebar.png?fit=max&auto=format&n=r7WxSEN_k7EK12_1&q=85&s=ed02512e5655ad070bf7238660dbae95)

#### Get your share link

To collect feedback, start by clicking on the Share button in the editor navbar.


**Open Share**

In the editor, click the Share button.


**Copy the Link**


![image](https://cdn.magicpatterns.com/uploads/hLz5mzwxDWRcge45n1sdQz/share-panel.png)




**Send it to your teammates**

    Anyone with the preview link can view the design and leave comments (if they
    have access).

#### Enter Comment Mode

##### From the editor

* Click the **comment** icon in the editor navbar to toggle Comment Mode.


![image](https://mintcdn.com/magicpatterns/r7WxSEN_k7EK12_1/documentation/collaboration/images/editor-room-comment-mode-button.png?fit=max&auto=format&n=r7WxSEN_k7EK12_1&q=85&s=4f0392593c64f7857fb056e2e7e6997d)

##### From the share link

* Open the preview link and click the **comment** icon to toggle Comment Mode.


![image](https://mintcdn.com/magicpatterns/r7WxSEN_k7EK12_1/documentation/collaboration/images/preview-link-comment-mode-button.png?fit=max&auto=format&n=r7WxSEN_k7EK12_1&q=85&s=2db7ee8a07ac32fa795578d15f67d755)

> 💡 **Tip:**
> You can quickly toggle Comment Mode with **C**. You can also
>   hide/show comment indicators with **H**.

#### Add an inline comment

Once Comment Mode is enabled:


**Click an element in the design**

    Tap on the specific UI element you want to comment on.


**Write your feedback**

    Add context, describe the issue, and include a suggestion if you can.


**Post the comment**

    Your comment appears as an indicator on the design and in the comments
    panel.

> ℹ️ **Note:**
> Comments are **tied to elements** in the design. If you resize
>   the screen and elements move, your comments stay anchored to the right
>   elements.


![image](https://mintcdn.com/magicpatterns/r7WxSEN_k7EK12_1/documentation/collaboration/images/adding-new-comment.png?fit=max&auto=format&n=r7WxSEN_k7EK12_1&q=85&s=c3a59016214210d6afb126ad4a05e3ad)

#### Commmon workflows:

* Async design reviews: Share a preview link, ask reviewers to leave comments directly on the relevant UI, and iterate without long meetings.
* Collecting feedback: Product, engineering, and stakeholders can comment on exactly what they mean—even if they're not editing the design.
* Bug or polish tracking: Use comments as a lightweight checklist while you refine the UI (resolve items as you address them).
* Version-aware feedback: Comments can be grouped by design version, so you can understand what feedback applies to which iteration.

#### Troubleshooting

> ⚠️ **Warning:**
> If you don't see comment indicators in the editor, make sure **comment mode**
>   is active (toggle it in the toolbar).

#### Video Guide

This topic is covered in our video lesson [Team Workflows and Sharing](/documentation/guide/team-workflows-and-sharing).

### Live Multiplayer
*Work on the same design or canvas with your team in real time.*

**Source:** https://www.magicpatterns.com/docs/documentation/collaboration/live-multiplayer

Magic Patterns is multiplayer everywhere, much like Figma. When you and a teammate open the same design or canvas, you both see who else is around and the page updates live as either of you (or the agent) makes changes.

#### In the design editor

You'll see your teammates' avatars in the toolbar, and the chat thread, generations, and design preview update for everyone at the same time. Read-only viewers can follow along and leave [inline comments](/documentation/collaboration/inline-comments).


![Two teammates on the same Magic Patterns design with synchronized chat and preview](https://cdn.magicpatterns.com/uploads/dgMseN8Su1c8ECNTnAV6Tn/multiplayer-design.gif)

#### On the canvas

The [Canvas](/documentation/projects/getting-started) goes a step further with live cursors. When a teammate selects a screen, it gets a colored outline matching their cursor color, so you can see exactly where each teammate is and what they're working on.


![Live cursors and selections on a shared Magic Patterns canvas](https://cdn.magicpatterns.com/uploads/bcYyKSV4yms73eHKNM8YJb/multiplayer.gif)

#### Who can join

Anyone with access to the design or canvas joins automatically when they open it. Set permissions through [Sharing Designs](/documentation/editor/sharing) and [Team Workspaces](/documentation/collaboration/team-workspaces).

### Team Workspaces
*Invite team members, manage your brand context, and configure workspace settings.*

**Source:** https://www.magicpatterns.com/docs/documentation/collaboration/team-workspaces

Team Workspaces give your team a shared place to work together, manage members, share Design Systems and components, and centralize billing.

#### Getting started

Go to [magicpatterns.com/settings/team](https://www.magicpatterns.com/settings/team) to manage your workspace. Only admins can manage the workspace; you can see who is the admin in the Team Members table under the Role column. You'll see:

* Team Members – Everyone in your workspace
* Subscription Plan – Your current plan (Starter, Business, or Enterprise)
* Billable Seats – How many paid seats you're paying for
* Available Seats – How many seats are free to assign

![Team Members table showing subscription overview and member list with Role column](https://cdn.magicpatterns.com/static/docs/team-members-table.png)

> 💡 **Tip:**
> You can invite unlimited team members. Free seats are included at no cost.
>   Only paid seats count toward your bill.

#### Understanding seats

A seat is a paid spot on your workspace plan. Each seat gets its own monthly credits and full access to generate designs. You pay for the number of seats you need.

* Paid seat – Full access, uses credits, counts toward your bill
* Free seat – In the workspace at no cost, 100 credits per month for generation

When you invite someone, they join with a Free seat by default. To give them full access, add a paid seat first (if needed), then assign it to them. Only admins can invite and manage members.

#### Workspace size and plans

Each plan has a limit on the number of paid seats:

* Starter: Up to 10 paid seats
* Business: 11 or more paid seats
* Enterprise: 10 paid seats minimum

If your workspace grows beyond 10 paid seats, you'll need to upgrade to Business or Enterprise. Free seats don't count toward this limit.

#### Common scenarios


**I need to add a teammate with full access**

    1. Go to [magicpatterns.com/settings/team](https://www.magicpatterns.com/settings/team)
    2. If you're out of seats, click Add more seats first and complete the payment
    3. Click Invite and enter their email
    4. Once they've joined, click the ... next to their name
    5. Click Upgrade to assign them a paid seat


**Someone left the team. I want to give their seat to someone else**

    Use Reassign Seat to move a paid seat from one person to another:

    1. Click the ... next to the member who is leaving
    2. Click Reassign Seat
    3. Select the team member who should receive the seat

    Credits already used on that seat transfer to the new member. The person who
    had the seat stays in the workspace but moves to a Free seat. The person
    receiving the seat gets it right away.


**I want to remove someone's seat but keep them in the workspace**

    Use Cancel Seat when you want to free up a seat but keep the person in the
    workspace:

    1. Click the ... next to the member
    2. Click Cancel Seat
    3. Their seat is marked for cancellation and frees up at the end of your
       billing cycle
    4. Until then, they keep full access. After the billing cycle ends, they
       remain in the workspace with a Free seat

    You cannot cancel your own seat. Use Manage Plan to change or cancel the
    workspace subscription instead.


**I need to remove someone from the workspace entirely**

    1. Click the ... next to the member
    2. Click Remove
    3. They are removed from the workspace


**I changed my mind about cancelling a seat**

    1. Click the ... next to the member whose seat is pending cancellation
    2. Click Undo Cancellation
    3. The seat stays active


**I'm out of seats. How do I add more?**

    1. Go to [magicpatterns.com/settings/team](https://www.magicpatterns.com/settings/team)
    2. Click Add more seats
    3. Choose how many seats you need
    4. Complete the payment

    Seats are prorated. You pay for the remainder of your billing cycle.


**I have too many seats. How do I reduce them?**

    Cancel seats for members who no longer need full access. Each cancelled seat
    frees up at the end of your billing cycle. You cannot reduce seats below the
    number of members who currently have active seats.


**I want to change our plan (upgrade or downgrade)**

    1. Go to [magicpatterns.com/settings/subscription](https://www.magicpatterns.com/settings/subscription) or [magicpatterns.com/settings/team](https://www.magicpatterns.com/settings/team)
    2. Click Manage Plan
    3. Select a new plan and complete the change in the payment portal

    See [Credits and Billing](/documentation/get-started/credits-and-billing)
    for how upgrades, downgrades, and prorating work.

#### When to use a Team Workspace

Team Workspaces work well when you:

* Work with multiple designers or developers on the same product
* Need a consistent brand across many pages or projects
* Share design systems, components, or templates
* Want one person to manage billing for the whole team

Once teammates are in the workspace, opening the same design or canvas puts you in a [live multiplayer session](/documentation/collaboration/live-multiplayer), with shared chat, generations, and (on the canvas) live cursors and shared selections.

#### Roles

* Admin – Can invite members, add seats, manage plans, upgrade or downgrade members, remove members, and change roles
* Member – Can use the workspace based on their seat; cannot manage billing or other members

#### Usage reporting

**Business** and **Enterprise** workspaces include Usage Reports at [magicpatterns.com/settings/usage-reports](https://www.magicpatterns.com/settings/usage-reports). There you can track workspace adoption, compare activity with a team leaderboard, and review time saved. Workspaces on other plans see an upgrade prompt until you move to Business or Enterprise.

![Unlock Usage Reporting modal on the Usage Reports dashboard](https://cdn.magicpatterns.com/uploads/jcHU4QviYhREXQAGjYWm5P/usage-report.png)

#### Moving files between workspaces

You can move designs between workspaces directly from the dashboard. Right-click on any file to see the option to move it to a different workspace.

![Right-click on a file to move it between workspaces](https://cdn.magicpatterns.com/uploads/cCfwJZdrt33DxMB91dGGDE/right-click-to-change-files.png)

This is useful when you need to:

* Transfer a design from your personal workspace to a team workspace
* Reorganize designs between different team workspaces
* Move completed work to a shared workspace for collaboration

#### SSO and SCIM

SSO, SCIM, and auto-join are available for team workspaces. SSO is self-serve
and available on Business plans and Enterprise plans. SCIM is available on
Enterprise plans. See [SSO and SCIM setup](/documentation/enterprise/sso-scim-setup)
for details.


---

## Publishing

### Website Metadata
*Customize your website metadata, such as your favicon and description*

**Source:** https://www.magicpatterns.com/docs/documentation/publishing/metadata

Once your design is published via a [Custom Publish URL](/documentation/publishing/publish-url) or your own [Custom Domain](/documentation/get-started/custom-domain), you can customize your website's metadata (title, description, favicon, social preview images).

##### Getting Started

To access the Metadata section, you need to either:

1. Publish your design with a [Custom Publish URL](/documentation/publishing/publish-url) (requires a paid plan), OR
2. Connect your design to a [Custom Domain](/documentation/get-started/custom-domain) (no paid plan required)

##### How to Update Metadata


**Click the Share button**

    Click the Share button at the top of the editor.


![Share button location](https://cdn.magicpatterns.com/uploads/76cgXyEJT44j7XbeLX88Fz/share-button.png)




**Edit your metadata**

    In the Publish modal, open the Metadata section. Here you can customize the metadata, such as favicons and descriptions.

    Click Save after making your changes.


![Editing website metadata](https://cdn.magicpatterns.com/uploads/s46hA3HtJ9k2pExUQLLsjj/website-metadata.png)



> 💡 **Tip:**
> Hide the 'Built with Magic Patterns' badge on a paid plan. paid plan. [Upgrade
>   here](https://www.magicpatterns.com/dashboard?dl=billing) to remove the badge
>   from your published websites.


![Built with Magic Patterns badge](https://cdn.magicpatterns.com/static/docs/built-with-mp-badge.png)

### Password Protection
*Restrict access to your published designs with password protection*

**Source:** https://www.magicpatterns.com/docs/documentation/publishing/password-protection

Password protection allows you to restrict access to your published designs.

#### How It Works

When password protection is enabled, anyone visiting your published design will see a password prompt. They will need to enter the correct password to view the site. This is useful for:

* Sharing work-in-progress designs with specific clients
* Restricting access to internal prototypes
* Protecting sensitive content before a public launch

#### How to Enable Password Protection


**Click the Share button**

    Click the **Share** button at the top of the editor, then open the **Privacy** section in the Publish modal.


![Privacy settings in Publish modal](https://cdn.magicpatterns.com/uploads/bJHaYJMuWVenr9zfQNKVaZ/password.png)




**Enable password protection**

    Toggle on **Require password for design preview**. A password input field will appear.


**Set your password**

    Enter your desired password and click **Save**. Your published design is now protected.

#### Removing Password Protection

To remove password protection:

1. Open the Publish panel and go to **Privacy**
2. Toggle off **Require password for design preview**

#### Notes

* Password protection applies to the published version of your design
* The password is not visible after it's been set—you'll need to set a new one if you forget it
* Password protection works with both [Custom Publish URLs](/documentation/publishing/publish-url) and [Custom Domains](/documentation/get-started/custom-domain)

### Custom Publish URL
*Publish your design to a custom Magic Patterns URL*

**Source:** https://www.magicpatterns.com/docs/documentation/publishing/publish-url

> ℹ️ **Note:**
> Custom Publish URLs require a paid plan. [Upgrade
>   here](https://www.magicpatterns.com/dashboard?dl=billing).

#### How It Works

By default, you are assigned a random website address hosted by Magic Patterns. But using the "Publish" button, you can assign a custom website address to your design.

For example, using our Custom Publish URL feature, if you want `my-portfolio` as your website address, your site will be live at `project-my-portfolio.magicpatterns.app`.

#### How to Publish to a Custom URL


**Click the Share button**

    Click the Share button at the top of the editor.


![Share button location](https://cdn.magicpatterns.com/uploads/76cgXyEJT44j7XbeLX88Fz/share-button.png)




**Enter your preferred website address (slug)**

    In the Publish modal, enter a name for your custom URL in the "Add Custom Publish URL" section.


![Publish modal](https://cdn.magicpatterns.com/uploads/q3C7SdUup4UVNmw56tjiNA/publish-modal.png)




**Click Publish**

    Your site will be live immediately. In the example screenshot, the URL is `project-mindfulnesscards.magicpatterns.app`

##### Changing Your Website Address

You can change your website address at any time by going back to the Publish panel and entering a new one.

#### Next Steps

Ready to use your own domain not on `*magicpatterns.app`? See [Host on a Custom Domain](/documentation/get-started/custom-domain) for instructions on connecting a domain you own.


---

## Exporting

### Integration Skill for AI Agents
*A drop-in skill that teaches Cursor or Claude Code how to adapt a Magic Patterns design into your production codebase.*

**Source:** https://www.magicpatterns.com/docs/documentation/exporting/integration-skill

When you bring a Magic Patterns design into your codebase — via the [MCP server](/documentation/features/mcp-server/overview), [Copy code as prompt](/documentation/get-started/copy-code-as-prompt), a [downloaded zip](/documentation/get-started/download-code), or a [GitHub sync](/documentation/get-started/sync-to-github) — the generated code is a **high-fidelity prototype**, not production code. This skill tells your AI coding agent to treat it that way: reproduce the *design*, not the literal code, and always prefer your codebase's existing components, tokens, and conventions.

> ℹ️ **Note:**
> Magic Patterns generates prototypes. The golden rule this skill encodes:
>   when the Magic Patterns code and your codebase disagree, **the codebase wins.**

#### Install the skill


**Tab: Claude Code**

    Save the skill to your project (or `~/.claude/skills/...` to make it global):

    ```bash theme={null}
    mkdir -p .claude/skills/integrate-magic-patterns-design
    # paste the SKILL.md below into:
    # .claude/skills/integrate-magic-patterns-design/SKILL.md
    ```

    Claude Code picks it up automatically and activates it when you share a Magic Patterns design or `magicpatterns.com` URL.


**Tab: Cursor**

    Add the skill as a project rule so Cursor applies it when integrating designs:

    ```bash theme={null}
    mkdir -p .cursor/rules
    # paste the SKILL.md below into:
    # .cursor/rules/integrate-magic-patterns-design.mdc
    ```


**Tab: Other AI editors**

    Any agent that supports custom instructions or skills works — paste the SKILL.md below into your tool's rules/skills configuration, or include it inline with your prompt when asking the agent to integrate a design.

#### The skill

Copy the contents below into your tool of choice.

```md theme={null}
---
name: integrate-magic-patterns-design
description: Adapt code generated by Magic Patterns (magicpatterns.com) into an existing codebase. Use when the user shares a Magic Patterns design, prototype, exported zip, "Copy Code as Prompt" output, or a magicpatterns.com URL and wants it implemented, integrated, or productionized in their project. Treats the Magic Patterns code as a design spec, not as code to copy verbatim.
---

### Integrate a Magic Patterns Design

Magic Patterns generates **prototypes**. The code you receive is a high-fidelity design spec — it shows layout, hierarchy, spacing rhythm, interactions, and intent. It is NOT meant to be pasted into a codebase as-is.

**The golden rule: when the Magic Patterns code and the target codebase disagree, the codebase wins.** Reproduce the *design*, not the exact code. Always prefer the codebase's existing components, design tokens, styling system, data layer, and conventions over the literal values in the prototype.

#### What Magic Patterns code looks like

Unless the design used a custom design system, expect:

- React 18 + TypeScript, styled with **Tailwind CSS v3** utility classes
- **lucide-react** icons, **framer-motion** animations, **react-router-dom** routing, **recharts** charts
- Named exports (`export function PricingSection`), flat or shallow file structure (`components/`, `pages/`, `utils/`)
- **Hardcoded mock data** — inline arrays/objects or a `utils/mockData.ts`
- Placeholder images as full URLs (often Unsplash)
- Stubbed interactivity: controlled inputs with local `useState`, `onSubmit` handlers that do nothing real, no API calls, no auth, no backend
- Zip/GitHub exports are wrapped in a standalone Vite project (`vite.config.ts`, `index.html`, `src/`)

Designs built on a design system preset (shadcn/ui, Chakra, Mantine, MUI) or a custom imported design system will use that library's components and theming instead of plain Tailwind.

#### Workflow

##### Step 1: Inventory the prototype

Read all the Magic Patterns files first. Identify:

- The actual design content: components, layout, screens, interactions, states (hover, empty, loading, error if present)
- Mock data shapes — these hint at the real data model the UI expects
- Which parts are scaffolding to discard (see checklist below)

**Discard checklist** — never port these:

- [ ] `index.tsx` / `index.html` / `vite.config.ts` / `tsconfig*.json` / `postcss.config.js` / `package.json` / `.eslintrc*` — Vite scaffolding; your project already has its own
- [ ] `tailwind.config.js` and `index.css` — merge any genuinely new tokens into your existing config instead of replacing it
- [ ] `canvas.manifest.js`, `useScreenInit.js` — Magic Patterns multi-screen plumbing; replace with your real router
- [ ] `ComponentPreview.tsx`, `components.config.json`, `context.md` — editor preview files
- [ ] `_designSystem/` folders and empty component stub files — precompiled design system bundles
- [ ] `data-id` props on elements — editor instrumentation
- [ ] `utils/mockData.ts` and inline mock data — replace with your real data layer

##### Step 2: Survey the target codebase

Before writing anything, learn how this codebase builds UI. Find:

1. **Framework and routing** — Next.js App Router? Pages Router? Remix? Plain Vite + react-router? Match its conventions for pages, layouts, links, and navigation.
2. **Component library** — Look for an existing `components/ui/`, design system package, or shared component folder. List the available primitives (Button, Input, Card, Dialog, Select, Badge, Table...).
3. **Styling system** — Tailwind (which version? v4 syntax differs from the v3 the prototype uses), CSS Modules, styled-components, vanilla-extract, a token system? Find the theme: colors, spacing, radii, typography, breakpoints.
4. **Icons** — Which icon library is already installed? Do not add lucide-react if the project uses something else.
5. **Data and state** — How does this codebase fetch data (React Query, SWR, server components, tRPC)? Where do types live? How are forms handled (react-hook-form, server actions)?
6. **Conventions** — Default vs named exports, file naming, folder placement, client/server component boundaries, i18n, accessibility patterns.

An effective shortcut: find an existing page or feature in the codebase that is similar in shape to the new design, and use it as the structural template.

##### Step 3: Map prototype pieces to codebase equivalents

For every element in the prototype, prefer replacement over porting:

| Prototype has | Do this |
|---|---|
| Hand-rolled `<button className="px-4 py-2 bg-blue-600...">` | Use the codebase's `` with the nearest variant |
| Hand-rolled inputs, selects, modals, dropdowns, tabs | Use the codebase's form/overlay primitives |
| Raw hex/arbitrary colors (`bg-[#4F46E5]`, `text-blue-600`) | Use the nearest semantic token (`bg-primary`, `text-accent`) |
| Exact pixel values (`w-[347px]`, `gap-[18px]`) | Snap to the codebase's spacing/sizing scale |
| Hardcoded font families and Google Font `@import`s | Use the project's existing typography setup |
| lucide-react icons | Use the project's icon library; pick the closest equivalent glyph |
| framer-motion animations | Keep only if framer-motion is already a dependency; otherwise use the project's animation approach or CSS transitions |
| `react-router-dom` routes and ``s | Use the framework's router and link component |
| Mock data arrays | Wire to the real data source; derive or reuse real types instead of the prototype's inline shapes |
| Unsplash/placeholder image URLs | Use real assets, or the project's placeholder/image component (`next/image`, etc.) |
| `useState`-only form handling | Use the codebase's form library and real submit/mutation logic |

Only port a component wholesale when the codebase genuinely has no equivalent — and when you do, restyle it with the project's tokens and put it where the codebase keeps shared components.

##### Step 4: Implement

- Build in the codebase's file structure, not the prototype's. The prototype's component *boundaries* (what's a section, what's a card, what's reusable) are usually worth keeping; its file paths are not.
- Preserve the design's intent: visual hierarchy, layout structure, relative spacing rhythm, responsive behavior, and interaction states. These are what the user approved in Magic Patterns.
- Treat exact values as approximations of that intent. "16px gap" means "one step of normal spacing", not literally `gap-[16px]` if the codebase's scale says `gap-4` or `var(--space-3)`.
- Add what prototypes always omit: real loading/error/empty states, accessibility (labels, focus management, keyboard handling) per the codebase's patterns, i18n if the project uses it, and real event handlers.
- Don't install new dependencies to match the prototype unless nothing in the codebase can do the job — and ask the user before adding any.

##### Step 5: Verify

1. Run the project's typecheck and linter; fix anything introduced.
2. Render the result and compare it against the Magic Patterns design for *intent*: same hierarchy, same layout, same interactions — expressed in this codebase's visual language. Pixel-for-pixel parity with the prototype is not the goal; consistency with the rest of the app is.
3. Confirm no prototype artifacts leaked in: no mock data, no `data-id` props, no stray Tailwind config, no unused new dependencies.

#### Common mistakes to avoid

- **Copying the prototype verbatim** and ending up with a page that looks different from the rest of the app. The most common and most costly failure.
- **Duplicating primitives** — shipping a second Button/Modal/Input that slightly differs from the existing one.
- **Importing the prototype's theme** — overwriting or forking `tailwind.config` / global CSS instead of mapping onto existing tokens.
- **Keeping mock data "for now"** — it gets shipped. Wire real data or clearly stub at the data-layer boundary, not inside components.
- **Matching arbitrary values exactly** (`w-[347px]`) instead of snapping to the design scale.
- **Adding lucide-react / framer-motion / react-router-dom** to a project that already has equivalents.
```

#### Related


- **[MCP Server](/documentation/features/mcp-server/overview)** — Pull designs directly into Cursor or Claude Code via MCP, then use this skill to integrate them.


- **[Copy code as prompt](/documentation/get-started/copy-code-as-prompt)** — Copy a design's code as a prompt for any AI editor.

### Overview of exporting
*Export your designs to Figma, sync back and forth with Github, or download your code.*

**Source:** https://www.magicpatterns.com/docs/documentation/exporting/overview

You've created an amazing design in Magic Patterns and you've already aligned with stakeholders. Now it's time to bring it into your development workflow or hand it off to an engineer. We offer several export options to fit your needs.


![Export options in Magic Patterns](https://cdn.magicpatterns.com/uploads/vV656i4VcuxNiLSJkAJsPz/handoff-to-eng.png)

#### Export options


- **[MCP Server](/documentation/features/mcp-server/overview)** — Integrate with AI coding tools like Cursor or Claude Code via MCP.


- **[Copy as prompt](/documentation/get-started/copy-code-as-prompt)** — Copy your design's code as a prompt to use in other AI tools.


- **[Integration Skill](/documentation/exporting/integration-skill)** — A drop-in skill that teaches Cursor or Claude Code to adapt a design into your codebase.


- **[Download code](/documentation/get-started/download-code)** — Download your design as a code package to use in any project.


- **[Sync with GitHub](/documentation/get-started/sync-to-github)** — Two-way sync with a GitHub repository. Creates a new repo and lets you push/pull changes between Magic Patterns and your codebase.


- **[Export to Figma](/documentation/get-started/figma-plugin)** — Send your design to Figma for further design work or handoff.

#### Common workflows

##### Handing off to an engineer

1. **MCP Server** - The most common workflow. Connect to Cursor or Claude Code and reference your designs directly in your IDE.
2. **Copy as prompt** - Copy your design's code to paste into other AI coding tools.

Whichever path you use, add the [Integration Skill](/documentation/exporting/integration-skill) to your AI editor so it adapts the design to your codebase's components and conventions instead of pasting the prototype verbatim.

3. **Download code** - Provide a zip file of the design code for engineers to integrate manually.
4. **Sync with GitHub** - Creates a new repository with your design code that engineers can clone and build upon.

##### Design handoff to Figma

Use the [Figma plugin](/documentation/get-started/figma-plugin) to export your design back to Figma for further refinement or stakeholder review.

#### Video Guide

This topic is covered in our video lesson [Engineering Handoff](/documentation/guide/engineering-handoff). For the MCP server, watch the [MCP overview video](https://www.youtube.com/watch?v=2QOc6vXftHo) (also embedded on the [MCP server overview](/documentation/features/mcp-server/overview)).


---

## Enterprise

### Not Receiving a Login Code
*Troubleshoot missing Magic Patterns login code emails*

**Source:** https://www.magicpatterns.com/docs/documentation/enterprise/email-deliverability

Magic Patterns sends a one-time code to your email address when you log in. If
the code does not arrive, follow the steps below.

#### Troubleshoot a missing code


**Confirm your email address**

    Check that you entered the correct email address on the login screen,
    including the domain name.


**Wait a few minutes**

    Delivery can occasionally be delayed by your email provider. Wait a few
    minutes before requesting a new code.


**Check spam and filtered folders**

    Search all folders for email from `auth.magicpatterns.com`, including spam,
    junk, promotions, quarantine, and other filtered folders.


**Ask your IT team to allowlist Magic Patterns**

    If you use a work email address, your company's mail gateway may be
    blocking the message. Ask your IT team to allowlist:

    * From domain: `auth.magicpatterns.com`
    * Envelope sender domain: `mail.auth.magicpatterns.com`

    Magic Patterns uses Amazon SES, which rotates sending IP addresses, so
    domain-based allowlisting is recommended.


**Use an individual mailbox**

    Avoid logging in with a Google Group, shared alias, or automatically
    forwarded address. These services can modify or filter the message before
    it reaches you. Use an individually owned mailbox when possible.

#### Information for IT teams

Authentication emails are sent from `auth.magicpatterns.com` through Amazon
SES. Direct messages are SPF, DKIM, and DMARC authenticated.

If the message is not delivered:

* Check gateway and quarantine logs for the recipient.
* Confirm `spf=pass`, `dkim=pass`, and `dmarc=pass` in the
  `Authentication-Results` header.
* Do not pin Amazon SES IP addresses or DKIM selectors because they can rotate.
* Check whether a forwarding rule, group footer, or subject prefix modified
  the message and invalidated DKIM.

#### Still unable to log in?

Contact [support@magicpatterns.com](mailto:support@magicpatterns.com) and
include the email address you are trying to use and the approximate time you requested the code

### Enterprises
*Overview of Magic Patterns for Enterprises*

**Source:** https://www.magicpatterns.com/docs/documentation/enterprise/overview

We are SOC 2 and ISO 27001 compliant.

Access our compliance reports in our [Trust Center](https://trust.magicpatterns.com/).

This section talks about the underlying mechanics of Magic Patterns, shedding light on the technology that powers our service, the architecture, and the measures we take to ensure data security.

> ℹ️ **Note:**
> Familiarity with this section isn't necessary for the use of Magic Patterns,
>   but we offer this information for those interested in the technical background
>   and for comprehensive security evaluations.

#### High-Level How Magic Patterns Works


**User prompt**

    You begin by entering a text prompt describing the user interface you
    envision. This could be as simple as "login page for an app" or as specific
    as detailed descriptions of elements and their behavior.


**Retrieve relevant context**

    Upon receiving your prompt, Magic Patterns retrieves the necessary context
    from its extensive library of design elements and systems. This process
    involves matching your description to the most appropriate UI components and
    layout patterns.


**Call relevant artificial intelligence model**

    The AI model is then engaged to interpret the prompt and context, generating
    a UI design. The model has been trained on a wide array of UI patterns and
    design principles, enabling it to produce high-quality, functional designs.
    Customer data is not used to train or improve any models.


**Show output**

    The final step is showing the output. The generated UI is rendered into a
    visual preview for your review and can be exported to code or to Figma,
    ready for implementation or further refinement.

#### Subprocessors

For comprehensive compliance information including SOC 2 reports, security policies, and more, visit our [Trust Center](https://trust.magicpatterns.com/).

| Vendor           | Nature and Purpose                                                                 | Security and Supplemental Measures                                                                               |
| ---------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Anthropic        | Anthropic is an AI safety and research company                                     | [https://trust.anthropic.com/](https://trust.anthropic.com/)                                                     |
| PostHog          | PostHog provides analytics and product insights                                    | [https://posthog.com/docs/privacy](https://posthog.com/docs/privacy)                                             |
| Sentry           | Sentry provides application performance monitoring and error tracking              | [https://sentry.io/security/](https://sentry.io/security/)                                                       |
| Cloudflare       | Cloudflare provides content delivery and security infrastructure                   | [https://www.cloudflare.com/trust-hub/](https://www.cloudflare.com/trust-hub/)                                   |
| MongoDB          | MongoDB is a database provider                                                     | [https://www.mongodb.com/products/capabilities/security](https://www.mongodb.com/products/capabilities/security) |
| Render           | Render is a platform-as-a-service (PaaS) used to host and run application services | [https://render.com/security](https://render.com/security)                                                       |
| Vercel           | Vercel is a platform-as-a-service (PaaS) used for frontend hosting and deployments | [https://vercel.com/security](https://vercel.com/security)                                                       |
| Google Workspace | Google Workspace is used for business productivity and internal collaboration      | [https://workspace.google.com/security/](https://workspace.google.com/security/)                                 |

- **[Security](/documentation/enterprise/security)** — Read about Magic Patterns' security measures and how we protect your data.

### Security
*Magic Patterns' security model includes many considerations and initiatives*

**Source:** https://www.magicpatterns.com/docs/documentation/enterprise/security

Given that customers of Magic Patterns may provide their code in order to best use Magic Patterns for legitimate business practices, the Magic Patterns security model is very important and held in the highest standard.
The goal of Magic Patterns' security model is to ensure the security and integrity of all of its managed data as well as all associated operations.

This means that data at rest and in transit must be secure from eavesdropping or tampering. All clients must be authenticated and authorized to access relevant data. Additionally, all interactions must be auditable and traced uniquely back to their source.

> ℹ️ **Note:**
> For detailed compliance reports, security policies, and audit documentation,
>   visit our [Trust Center](https://trust.magicpatterns.com/) where you can
>   access SOC 2 reports, compliance certifications, and comprehensive security
>   controls information.

#### Threat model

Magic Patterns' threat model spans communication, storage, response mechanisms, failover strategies, and more.

* Eavesdropping on communications: Magic Patterns ensures end-to-end encryption for all client interactions with the Magic Patterns API.
* Tampering with data (at rest or in transit): magic Patterns implements data integrity checks to detect tampering. If inconsistencies are found, Magic Patterns aborts transactions and raises alerts.
* Unauthorized access (lacking authentication/authorization): Magic Patterns mandates rigorous authentication and authorization checks for all inbound requests.
* Actions without accountability: Magic Patterns logs all project-level events, including policy updates, queries/mutations applied to secrets, and more. Every event is timestamped and information about actor, source (i.e. IP address, user-agent, etc.), and relevant metadata is included.
* Loss of service availability or secret data due to failures: Magic Patterns leverages the robust container orchestration capabilities of Render and the inherent high availability features of MongoDB to ensure resilience and fault tolerance. By deploying multiple replicas of Magic Patterns application on Render, operations can continue even if a single instance fails.
* Unrecognized suspicious activities: Magic Patterns monitors for any anomalous activities such as authentication attempts from previously unseen sources.

#### External threat overview

Magic Patterns's architecture consists of various systems:

* Magic Patterns API
* Storage backend
* Magic Patterns Web UI

The Magic Patterns API requires that the Magic Patterns Web UI are authenticated and authorized for every inbound request that accesses customer data.

The storage backend used by Magic Patterns is also untrusted by design. All sensitive data is encrypted either symmetrically with AES-256-GCM or asymmetrically with x25519-xsalsa20-poly1305 prior to entering the storage backend, depending on the context either on the client-side or server-side. Moreover, Magic Patterns communicates with the storage backend over TLS to provide an added layer of security.

#### Internal threat overview

Within Magic Patterns, a critical security concern is an attacker gaining access to sensitive data that they are not permitted to, especially if they already has some degree of access to the system. There are currently two authentication methods categories used by clients for where we apply robust authentication and authorization logic.

##### JWT

This token category is used by users and included in requests made from the Magic Patterns Web UI or elsewhere to the Magic Patterns API.

Each token is authenticated against the API and mapped to an existing user in Magic Patterns. If no existing user is found for the token, the request is rejected by the API. Each token assumes the permission set of the user that it is mapped to. For example, if a user corresponding to a token is not allowed access to a certain organization or code, then the token is also not be valid for any requests concerning those specific resources.

#### Infrastructure

##### High availability

Magic Patterns leverages the robust container orchestration capabilities of Render and the inherent high availability features of the storage backend (i.e. MongoDB) to ensure resilience and fault tolerance.

* Render: By deploying multiple replicas of Magic Patterns application on Render, operations continue even if a single instance fails. Render Services facilitate load balancing, effectively distributing traffic across your application’s instances and ensuring optimal performance.
* Storage backend: MongoDB supports replica sets, which provide data redundancy and automatic failover for the underlying database.
* If using [Magic Patterns](https://www.magicpatterns.com), data is stored in a Mongo Atlas cluster with storage autoscaling and cluster tier autoscaling enabled; as you'd expect, the cluster sits on a dedicated node.

Together, Render's self-healing mechanisms and MongoDB’s failover capabilities work to create a highly available and fault-tolerant application capable of recovering gracefully from unexpected failures.

##### Snapshots

A snapshot is a complete copy of data in the storage backend at a point in time.

If using Magic Patterns, snapshots of MongoDB databases are taken regularly; this can be enabled on your own storage backend as well.

#### Platform

##### Web application

Magic Patterns utilizes the latest HTTP security headers and employs a strict Content-Security-Policy to mitigate XSS.

JWT tokens are stored in browser memory and appended to outbound requests requiring authentication; refresh tokens are stored in `HttpOnly` cookies and included in future requests to `/api/token` for JWT token renewal.

##### User authentication

Magic Patterns supports authentication methods with Figma, Google, GitHub, and traditional email/password.

#### Employee data access

Whether or not Magic Patterns or your employees can access data in the Magic Patterns instance and/or storage backend depends on many factors how you use Magic Patterns:

Using Magic Patterns's managed service, [Magic Patterns](https://www.magicpatterns.com) means delegating data oversight and management to Magic Patterns. Under our policy controls, employees are only granted access to parts of infrastructure according to principle of least privilege; this is especially relevant to customer data which can only be accessed by executive management of Magic Patterns. Moreover, any changes to sensitive customer data is prohibited without explicit customer approval.

Please email [security@magicpatterns.com](mailto:security@magicpatterns.com) if you have any specific inquiries about employee data access policies.

#### Certifications

Magic Patterns is SOC 2 and ISO 27001 certified. Please visit our [Trust Center](https://trust.magicpatterns.com/) to request a copy of the report.

#### Additional resources

* Terms of Service: [https://www.magicpatterns.com/docs/documentation/legal/terms](https://www.magicpatterns.com/docs/documentation/legal/terms)
* Privacy Policy: [https://www.magicpatterns.com/docs/documentation/legal/privacy](https://www.magicpatterns.com/docs/documentation/legal/privacy)
* Trust Center: [https://trust.magicpatterns.com/](https://trust.magicpatterns.com/)

#### Get in touch

If you have any concerns about Magic Patterns or believe you have uncovered a vulnerability, please get in touch via the e-mail address [security@magicpatterns.com](mailto:security@magicpatterns.com). In the message, try to provide a description of the issue and ideally a way of reproducing it. The security team will get back to you as soon as possible.

### SSO, SCIM & Domain Setup
*Learn how to set up Single Sign-On (SSO), SCIM directory sync, and domain capture for your workspace*

**Source:** https://www.magicpatterns.com/docs/documentation/enterprise/sso-scim-setup

This guide explains how to set up enterprise authentication and user management features for your Magic Patterns workspace.

#### Single Sign-On (SSO)

Magic Patterns supports Single Sign-On (SSO), allowing your team to authenticate using your workspace's identity provider. SSO configuration is self-serve for Business and Enterprise accounts. Admins can configure it at [magicpatterns.com/settings/workspace](https://www.magicpatterns.com/settings/workspace).


**Configure your identity provider**

    Go to
    [magicpatterns.com/settings/workspace](https://www.magicpatterns.com/settings/workspace),
    click Configure SSO, and follow the setup instructions to connect your
    identity provider (such as Okta, Azure AD, Google Workspace, or others) to
    Magic Patterns.


**Test SSO login**

    Once configured, your team members can sign in to Magic Patterns using your
    workspace's SSO credentials.

#### SCIM / Directory Sync

Magic Patterns supports SCIM (System for Cross-domain Identity Management) for automatic user provisioning and directory synchronization for Enterprise customers.


**Enable SCIM**

    SCIM directory sync is also configured through WorkOS. When you set up SSO,
    you can also enable SCIM for automatic user management.


**Automatic user provisioning**

    Once SCIM is enabled, users from your directory will be automatically
    provisioned in Magic Patterns when they're added to your identity provider.


**User updates and deprovisioning**

    Changes to users in your directory (such as deactivation) will automatically
    sync to Magic Patterns.

#### Domain Capture / Auto Join

Domain capture automatically adds new users to your workspace when they sign up
to Magic Patterns with an email address from your workspace's domain.


**Contact support**

    To set up domain capture, edit the domain capture section of [your workspace
    settings](https://www.magicpatterns.com/workspace/settings#workspace-settings).


**Provide your domain**

    Input your workspace's email domain (e.g., `@yourcompany.com`).


**Domain configuration**

    If you have already verified your domain, you can add it to your workspace
    settings self-serve. Otherwise, you will be prompted to verify with our
    support team and we will assist.

> ℹ️ **Note:**
> Domain capture can be combined with SSO and SCIM for comprehensive user
>   management. Contact
>   [support@magicpatterns.com](mailto:support@magicpatterns.com) to discuss your
>   workspace's needs.


![Domain Capture](https://cdn.magicpatterns.com/uploads/4QbS2YwNHUMWgZFx9qoowb/domain-capture.png)

- **[Team Workspaces](/documentation/collaboration/team-workspaces)** — Learn more about managing team members and workspaces in Magic Patterns.


---

## Troubleshooting

### Troubleshooting
*Helpful tips for resolving issues*

**Source:** https://www.magicpatterns.com/docs/documentation/troubleshooting/overview

#### Features to Help You Troubleshoot

> ℹ️ **Note:**
> Fix with AI does not consume any credits.

##### Retry

If you didn't like what the AI generated, you can click the Retry button to have it try the same prompt again. Retrying a prompt will consume credits.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/documentation/troubleshooting/images/retry-message.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=c55c359c97f276eff05b777c31cde006)

##### Fix with AI

If you're experiencing an issue with your design in Magic Patterns, you can use the Fix with AI feature. This tool helps resolve problems automatically and does not consume any credits.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/documentation/troubleshooting/images/fixwithaibutton.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=da7428236b80e85aa1bd3f1189d521ad)

##### `/Debug` Skill

When you're stuck in a situation where the AI isn't following your instructions correctly, try using the `/Debug` skill in the chat. It plugs in a well-crafted prompt template along with your description of the issue that helps guide the AI toward debugging the issue effectively.

![image](https://mintcdn.com/magicpatterns/yhBxQxxixYmnt-5a/documentation/troubleshooting/images/debug.png?fit=max&auto=format&n=yhBxQxxixYmnt-5a&q=85&s=5a07cffaf763ba3839d087ca13679482)

***

#### Common Issues

##### "I Don't See My Changes"

###### Background

The AI likely *did* make the change you asked for, but:

* It's not "hooked up" (e.g., created a new page but didn't link a button to it)
* It's on a different page/route than you're looking at
* The element exists but isn't visible (hidden, off-screen, or in a different state)

###### Solution

Ask the AI to reflect on why you're not seeing the changes:

```Example Prompt theme={null}
I asked you to [describe your change] but I don't see it on the screen. Can you reflect on what you changed and where it is? Did you create a new page or component that I need to navigate to?
```

> 💡 **Tip:**
> The `/Ask` mode and `/Debug` skill can be powerful here too!

The AI might explain:

* "I created a new `/settings` route, but you need to click the gear icon to navigate there"
* "I added the feature to the mobile view, but you're looking at desktop"
* "I created a modal, but it only shows when you click the 'View Details' button"

###### Prevention Tips

1. **Be explicit about where changes should appear:**
   * Bad prompt: "Add a settings page"
   * Good prompt: "Add a /settings route and make the gear icon in the header link to it"

2. **Use [Select Mode](/documentation/editor/how-to-prompt#select-mode-and-visual-edit) to reference specific elements:**
   * Click the button that should trigger the change
   * Then prompt: "When I click X, ensure that it actually goes to [XYZ]."

3. **Ask the AI to confirm:**
   * Add to your prompt: "...and make sure it's visible on [XYZ]"

##### "I never see Fix with AI""

###### Background

If Fix with AI isn't appearing in your project, it's likely because your app is wrapped in a special thing called an `ErrorBoundary`. In frameworks like React, an ErrorBoundary catches errors and displays fallback UI. While useful for production, this behavior prevents unhandled exceptions from surfacing, which means the system doesn't recognize an error and won't trigger Fix with AI.

###### Solution

Remove or disable your error boundary by prompting the assistant to automatically make the change:

```Example Prompt theme={null}
Do not use an error boundary at all
```

###### Prevention Tips

* Avoid wrapping your entire app in an `ErrorBoundary` while prototyping
* If you need error handling, consider prompting the AI to add it only to specific components rather than the "entire App"

##### "I have to click A LOT every time to navigate through my screens"

###### Background

If you have a flow of *many* screens, you don't need to click through from the start every time. **Screens** shows every page of your design in a single bird's-eye view, and you can prompt against any of them directly.

###### Solution

Open the **Screens** tab at the top of your design. See [Screens](/documentation/get-started/adding-pages#screens) for details.


![The Screens view showing all pages of a design at once](https://cdn.magicpatterns.com/uploads/fzxBmL3wf1yooi8DWjjkDk/Screens.png)


---

## Tutorials

### Video Tutorials
*Watch how to use Magic Patterns to create designs*

**Source:** https://www.magicpatterns.com/docs/documentation/tutorials/video-tutorials

Subscribe on **[YouTube @magicpatterns](https://www.youtube.com/@magicpatterns)** for new walkthroughs and product updates. Follow us on **[LinkedIn](https://www.linkedin.com/company/magicpatterns)** and **[X @magicpatterns](https://x.com/magicpatterns)**.

#### Introducing Magic Patterns

#### Building Your First Prototype

#### Improving Your Prompts

#### Importing

#### Design Systems

#### Team Workflows and Sharing

#### Engineering Handoff

#### Build a Landing Page

#### Visual Edit

#### MCP Server

#### Canvas

#### Commenting

#### Internet Design to React Component


---

## Changelog / Feature Releases

### Changelog
*View the latest updates and releases on Magic Patterns*

**Source:** https://www.magicpatterns.com/docs/documentation/feature-releases/changelog

##### 2026-07-16 — Custom viewports

  ### Preview your designs at any custom viewport


![Custom viewport width and height inputs in the viewport panel](https://cdn.magicpatterns.com/uploads/aNa5tqc5AFG7MFkrLJ4oPS/custom-viewports.png)

  You can now set a custom viewport size in the preview. Enter any width and height in the viewport panel and hit Apply to test your design at the exact dimensions you need, alongside the built-in device presets.

##### 2026-07-15 — Transfer ownership

  ### Transfer ownership of a design


![Transfer ownership of a design to another member](https://cdn.magicpatterns.com/uploads/58bjndLJ5d5g5ffE3vWkzP/transfer-ownership.png)

  You can now transfer ownership of a design to another member of your workspace. Handy when a teammate takes over a project or when you want to hand off long-lived designs without losing history.

##### 2026-07-14 — Image generation

  ### Generate images right inside your designs


![Image generation in Magic Patterns](https://cdn.magicpatterns.com/uploads/9TyL2Dw3t3m8MSbAuUNF4W/Image-generation.png)

  The agent can now generate images and drop them straight into your designs, so mockups feel real instead of relying on gray placeholders. Powered by Nano Banana 2 Lite.

##### 2026-07-09 — GPT-5.6 models

  ### GPT-5.6 Sol and Terra are now available

  Magic Patterns now supports OpenAI's GPT-5.6 Sol and GPT-5.6 Terra in the model picker. Use Sol for flagship capability on complex workflows, or Terra for strong GPT-5.6 performance at a lower cost.

##### 2026-07-02 — Connect to GitHub

  ### Connect your GitHub repo for on-brand designs


![Connect a GitHub repository as a design source](https://cdn.magicpatterns.com/uploads/cWQLBcsAFTz5D7aWJ3bKHh/connect-github.png)

  You can now connect a GitHub repository as a design source. Point Magic Patterns at your repo and the agent will use your real codebase for context.

  Connect to Github through the + button on the prompt toolbar, connect your account, pick a repository, and build.

##### 2026-06-29 — Sonnet 5

  ### Announcing Claude Sonnet 5


![Claude Sonnet 5](https://cdn.magicpatterns.com/uploads/1fQXyPkXRS3ruk6z4Nk8QA/Sonnet_5.png)

  Magic Patterns now supports Anthropic's Claude Sonnet 5, their latest model, as a selectable option. It brings sharper reasoning and stronger design taste, so the agent plans more carefully and builds higher-quality UI.

##### 2026-06-29 — Web Access

  ### Your agent can now browse and search the web


![Web access — the agent can browse and search the web](https://cdn.magicpatterns.com/uploads/4iump1m5eQPV3xvv9QK5wF/web-search.png)

  Magic Patterns can now search the web and read pages and documentation while it works. That means it can pull in up-to-date information, reference third-party APIs, and ground designs in real sources instead of relying only on what it already knew.

  It's used sparingly and automatically: the agent reaches for the web only when something is genuinely current or external, and any sites it visits are tallied in the "Explored" steps in the chat.

##### 2026-06-24 — Download File

  ### Download File


![Download a file from the file tab](https://cdn.magicpatterns.com/uploads/ebhT67N2LHaq1B8Cb53xTH/Download-Code.png)

  You can now download any file by right-clicking on it in the file tab.

##### 2026-06-19 — Folders

  ### Organize your dashboard with Folders


![Organizing designs into folders on the dashboard](https://cdn.magicpatterns.com/uploads/mDv6gDh4CCJmCyzSMoZ9ZU/Folders-Magic-Patterns.png)

  You can now organize your designs into folders from the [Files dashboard](https://www.magicpatterns.com/dashboard/files).

  Folders are shareable, too: share one with your workspace

  [Create your first folder.](https://www.magicpatterns.com/dashboard/files)

##### 2026-06-18 — Unified Share panel

  ### Sharing and publishing, now in one place


![Unified Share panel — Collaborate tab](https://cdn.magicpatterns.com/uploads/wTNiXfjW8Uh5WkmbCsq6FG/new-collaborate-panel.png)

  Sharing and shipping used to live in two different buttons. We've merged them into a single **Share** panel, split across two tabs:

  **Collaborate**

  * Copy the editor link or invite teammates by email with write / read permissions
  * Manage access requests and share a clean preview link

  **Publish**

  * Set a custom URL, add password protection, and auto-publish your latest version
  * Edit site metadata (title, description, OG image) and connect a custom domain


![Unified Share panel — Publish tab](https://cdn.magicpatterns.com/uploads/9kUpYAWhWWTUUyRwoUcedg/new-publish-panel.png)

##### 2026-06-17 — Connect to LinkedIn

  ### Share your AI experience on LinkedIn


![Connect to LinkedIn](https://cdn.magicpatterns.com/uploads/piexBEp7vvSie4dtqtfNj6/connected-accounts-linkedin.png)

  Today, we're joining forces with LinkedIn to make it easier for you to showcase the work you've actually done, validated by the tools you use everyday to do it. As your work evolves, your profile and credibility evolves with it.

  Connect your LinkedIn to add Magic Patterns under "Connected apps" to your LinkedIn profile. It's a verified signal that shows you build with Magic Patterns, visible to recruiters, clients, and teammates.

  [Get started now.](https://www.magicpatterns.com/settings/profile?connect=linkedin)

##### 2026-06-16 — CSV File Support

  ### CSV File Support


![Attaching a CSV file in the chat bar](https://cdn.magicpatterns.com/uploads/tSYcr3EFzR5BePM4Sts3SQ/csv-upload.png)

  You can now attach `.csv` files to a prompt. Drop in a dataset and the agent uses it as first-class context for tables, charts, and data-driven UI.

##### 2026-06-15 — Improved Inspiration Mode

  ### Improved Inspiration Mode


![Inspiration Mode](https://cdn.magicpatterns.com/uploads/nw3xv6KYeJtrMpZ5ht5ZgY/inspiration.png)

  * Variants now displayed fullscreen in the preview
  * Concepts stream in live
  * 3x faster, you pick which one you want implemented

  [Read more about how to prompt.](/documentation/editor/how-to-prompt)

##### 2026-06-14 — Badges

  ### Badges on public profiles


![Badges on public profiles](https://cdn.magicpatterns.com/uploads/ccLoDzT8SXaSX6dL4SHPXe/Badges.png)

  Public profiles now include a Badges section celebrating milestones.

  Example badges:

  * Early User Badge
  * Ambassador Badge (learn more about the [Ambassador Program](https://www.magicpatterns.com/ambassadors))
  * Prompting milestones

  [Grab your handle](https://www.magicpatterns.com/settings/profile) to share your badges at `magicpatterns.com/profile/<handle>`.

##### 2026-06-11 — Context management

  ### Context Ring, 1M Context Window, /Clear, and /Summarize


![Context Ring](https://cdn.magicpatterns.com/uploads/gwgunUmkjv9UqTEZnR81V5/Context_Ring.png)

  Context Ring — see how full your chat's "memory" is. The Magic Patterns Agent will automatically manage context for you, but if you see the ring approaching 100%, you can leverage `/Summarize` and `/Clear` if you want more control.

  1M Context Window — a bigger context window to keep more of the conversation in memory, now available in the model picker. Will use more credits in longer conversations.

  **New Commands**

  * `/Summarize` — preserves important details while freeing up context
  * `/Clear` — resets the current conversation context without needing to fork the design

  A smaller context also keeps per-generation credit costs down.

  [Learn more about credits and plans.](/documentation/get-started/credits-and-billing#credits)

##### 2026-06-09 — Plan Mode improvements

  ### Plan Mode improvements


![Plan Mode improvements](https://cdn.magicpatterns.com/uploads/8v65cbeRpxZdJFp4TrSheY/Plan_Mode.png)

  We've improved our `/Plan` mode. Use /Plan when you have a larger change or want to align on the approach before any code is written. The agent asks a few clarifying questions, drafts a plan you can edit in the preview, and only starts building once you approve it.

  [Read more about Plan Mode.](/documentation/editor/plan-mode)

##### 2026-06-09 — Fable 5

  ### Introducing Fable 5


![Fable 5](https://cdn.magicpatterns.com/uploads/2vaKLuxUDXV5c72aCuoZzz/Fable_5.png)

  Fable 5 is now available in Magic Patterns. Claude's first Mythos model and the most powerful model available — pick it from the model picker for your next generation.

##### 2026-06-05 — Handles

  ### Introducing Handles


![Public profile page on Magic Patterns](https://cdn.magicpatterns.com/uploads/awsdEj9iA9U4ftoupw23K6/alex-handle.png)

  Claim your handle before someone else does, then share your Magic Patterns activity with the community.

  Public profiles are off by default. [Turn yours on in settings](https://www.magicpatterns.com/settings/profile) to share your activity heatmap at `magicpatterns.com/profile/<handle>`.

  Can you beat the top 4%? [Check out our CEO's profile.](https://www.magicpatterns.com/profile/alex)

##### 2026-06-01 — Per-screen viewports

  ### Per-screen viewports


![Per-screen viewport setting in Screens](https://cdn.magicpatterns.com/uploads/atVyUJidp4eXfYcJDQGnmd/Viewports_on_Screens.png)

  Screens now has per-screen viewport settings. Select one or multiple screens and switch between desktop, tablet, and mobile — or pick a specific device like iPhone 17 or iPad 13″.

  * **Viewport per screen** — set each screen to a different size right from the canvas.
  * **Cmd+A selects all** — quickly grab everything on the canvas.
  * **Export to Figma from the selection bar** — no need to open a menu.
  * **Smarter auto-layout** — layout now respects each screen's dimensions.

##### 2026-05-28 — Opus 4.8

  ### Opus 4.8


![Opus 4.8](https://cdn.magicpatterns.com/uploads/crfX9Th4PwwqW3iHYJGm1V/Opus_4.8.png)

  Opus 4.8 is now available in Magic Patterns. Pick it from the model picker for your next generation.

##### 2026-05-26 — Screens

  ### New "Screens" tab on every design



  A bird's-eye view of your design. The new **Screens** tab lays out every page side-by-side, so you can see and edit entire flows without clicking through.

  [Read more in the Multiple Pages guide.](/documentation/get-started/adding-pages#screens)

##### 2026-05-24 — Ambassador Program

  ### Ambassador Program


![Magic Patterns Ambassador Program](https://cdn.magicpatterns.com/uploads/4cBTypoJuGq4Cnkqz27XR8/Ambassadors.png)

  The Magic Patterns Ambassador Program is here. If you love sharing what you build with Magic Patterns, you can now apply to become an official ambassador and help grow the community.

  * **Share what you make** — get recognized for tutorials, demos, and content you create about Magic Patterns.
  * **Perks and early access** — ambassadors get credits, swag, and a first look at upcoming features.

  [Apply to become an ambassador.](https://www.magicpatterns.com/ambassadors)

##### 2026-05-23 — API v3

  ### API v3


![API v3](https://cdn.magicpatterns.com/uploads/rEnpkgBy8xBUSofebuTJa7/API-v3.png)

  The Magic Patterns API v3 is here. It gives you full programmatic access to design generation, iteration, file editing, and publishing — the same surface as the [MCP server](/documentation/features/mcp-server/overview), authenticated with a single key that works for both REST and MCP.

  * **Create and iterate on designs** — kick off generations, poll status, read and write artifact files, and publish changes from your own systems.
  * **Same credits, no separate subscription** — v3 usage draws from your normal Magic Patterns credit balance.

  [Get started with the v3 API.](https://www.magicpatterns.com/docs/api/getting-started)

##### 2026-05-21 — Resize designs on the canvas

  ### Resize Designs on the Canvas


![Arrows pointing at the resize handles on the right edge and bottom-right corner of a design on the canvas](https://cdn.magicpatterns.com/uploads/br53auqBQuMbNduV1QUnU1/CleanShot_2026-05-21_at_17.30.39.png)

  You can now drag to resize a design on the canvas. Useful for checking how a design looks at different aspect ratios, including custom devices like kiosks, watches, foldables, or other non-standard viewports.

  * Drag the right, bottom, or corner handle on a design to change its width and height.
  * Compare multiple sizes side by side on the same canvas.

##### 2026-05-13 — Reference other designs

  ### Reference Other Designs


![@ menu showing Design Systems and Designs in the prompt bar](https://cdn.magicpatterns.com/uploads/qGZBv6vKfP8xuwSYCf6HpT/CleanShot_2026-05-13_at_14.00.482x.png)

  Cross-referencing is here. You can now pull another design into your prompt for context, from both the dashboard prompt and the editor chat bar.

  * Type `@` to pick a Design or Design System.
  * You can also paste a design link directly into the prompt.
  * You can only reference designs you have access to.

  [Learn more in the Referencing Other Designs guide.](/documentation/editor/merging-designs#option-1-cross-project-referencing-recommended)

##### 2026-05-12 — Rate Agent Responses

  ### Rate Agent Responses


![Thumbs up and thumbs down buttons on an agent response](https://cdn.magicpatterns.com/uploads/kHAq1ExCK8oM3qDB24a2r7/thumbs-up-down.png)

  You can now give a thumbs up or thumbs down on every agent response. Your feedback is our roadmap — we review it regularly to find where the agent can do better.

  * Thumbs down opens an optional comment box so you can tell us exactly what went wrong.
  * Every rating is logged with the full conversation context so we can reproduce and fix the issue.

##### 2026-05-09 — Markdown File Support

  ### Markdown File Support


![Attaching a markdown file in the chat bar](https://cdn.magicpatterns.com/uploads/vzjZZWDptzEKdbNCHvktQ9/markdown-files.png)

  You can now attach `.md` files to a prompt — both when starting a new design and from the editor chat bar. Drop in a PRD, spec, or notes doc and the agent reads it as first-class context.

  * Uploaded files are saved alongside your design as `docs/*.md`, so they stay attached to the artifact and are available on every follow-up prompt.
  * Up to 2MB per file. Multiple docs per prompt are supported.

##### 2026-05-06 — Plan Mode

  ### Plan Mode


![Plan Mode in Magic Patterns](https://cdn.magicpatterns.com/uploads/eD6u3UVEcFc5qaD5zvFziu/CleanShot_2026-05-06_at_18.26.122x.png)

  `/Plan` is a new chat mode for when you want to align on the approach before any code is written.

  * The agent asks a few clarifying questions, then drafts a structured plan you can edit directly in the preview.
  * When you're happy with it, click Build to hand the plan to the agent.

  [Read the full Plan Mode guide.](/documentation/editor/plan-mode)

##### 2026-05-05 — Live Multiplayer

  ### Live Multiplayer


![Live multiplayer in Magic Patterns](https://cdn.magicpatterns.com/uploads/bcYyKSV4yms73eHKNM8YJb/multiplayer.gif)

  Magic Patterns has been multiplayer since day one. Open the same design or canvas as a teammate and everything stays in sync — edits, chat, generations, and the preview all update live.

  * Live cursors and selection outlines on the canvas.
  * Read-only viewers can follow along via share link and leave [inline comments](/documentation/collaboration/inline-comments).

  [Read more here.](/documentation/collaboration/live-multiplayer)

##### 2026-05-01 — Chat Modes and Skills

  ### Chat Modes and Skills


![Chat Modes and Skills in the / menu](https://cdn.magicpatterns.com/uploads/gSpZ9529cyWPTDFAVzv3GW/CleanShot_2026-04-30_at_14.23.22.png)

  You can now use Chat Modes and Skills straight from the dashboard initial prompt. Start a new design with `/Inspiration`, or kick off in `/Plan` mode before any code is written.

  In the editor, the `/` menu now organizes everything in one place:

  * Chat Modes: `/Ask` (formerly `/Discuss`) and `/Plan`.
  * Skills: `/Inspiration`, `/Debug`, and `/Polish` (previously called "Commands").

  [Learn more in our How to Prompt guide.](/documentation/editor/how-to-prompt#chat-modes-skills-and-integrations)

##### 2026-04-30 — New Component UI

  ### Components are now unified in a single editor


![New Component UI](https://cdn.magicpatterns.com/uploads/wajhKVhCs4bRVj4KSQXupc/CleanShot_2026-04-29_at_22.42.312x.png)

  If you want to make changes to the entire library at once you can now prompt it directly, e.g. "Update everything to be in my new primary color". This makes it easier to edit multiple components at once.

  Here to help with any questions — message [support@magicpatterns.com](mailto:support@magicpatterns.com).

##### 2026-04-23 — Agent 2.0

  ### Announcing Agent 2.0 and a new editor UI


![Agent 2.0](https://cdn.magicpatterns.com/uploads/mg1jGFGvDW1MJToeoxAEVM/agent20.gif)

  Agent 2.0 is here! 15% fewer credits, 10% faster time-to-first-token, and an 8% performance improvement.

  We've also rebuilt the editor from the ground up with a cleaner layout and faster performance. [Check it out on Product Hunt!](https://www.producthunt.com/products/magicpatterns?launch=magic-patterns-agent-2-0)

##### 2026-04-23 — Integrations moved to editor chatbar

  ### Integrations Moved to the Chat Bar


![Integrations menu in the chat bar](https://cdn.magicpatterns.com/uploads/kuq2RQ7CRV6vc9GcNruhae/integrations-chat-bar.png)

  Integrations now live in the chat bar, alongside Connectors and Skills. Open the menu to manage OpenAI, Anthropic, and Collect External Feedback without leaving the editor.

  Learn more about [integrations](/documentation/integrations/overview).

##### 2026-04-22 — View model credit usage

  ### View Model Usage and Credit Spend Per Prompt


![Credit spend per prompt](https://cdn.magicpatterns.com/uploads/hsdFtUWMi1NZFBJqbK5kkG/tool-text.png)

  You can now see exactly how many credits each prompt consumed and which model was used, directly in the chat interface.

  Learn more about [credits and plans](/documentation/get-started/credits-and-billing#viewing-credit-consumption).

##### 2026-04-21 — Code Editor Shortcuts in Editor

  ### New Code Editor Shortcuts


![Code editor keyboard shortcuts](https://cdn.magicpatterns.com/uploads/7dDk7pQZagsyZo7t3r5Am2/command-p.png)

  The code editor now supports new keyboard shortcuts for faster navigation:

  * **Cmd+Shift+F** (Search in Project) — Quickly search across all files in your design.
  * **Cmd+P** (Quick Open) — Jump to any file instantly by name.

##### 2026-04-20 — Copy Paste Directly to Figma

  ### Copy Paste Directly to Figma


![Export to Figma](https://cdn.magicpatterns.com/uploads/752kXjyHDSNZPaB6L9qa3a/export-to-figma.gif)

  Exporting your designs to Figma is now faster and more seamless than ever:

  * **No plugin required** — The Figma plugin is no longer needed. Export works natively without any installation.
  * **Direct copy-paste** — Copy your design from Magic Patterns and paste it directly into Figma.
  * **Higher-fidelity output** — Exports now render with improved accuracy, preserving more detail from your original design.

  [Learn more about exporting to Figma](/documentation/get-started/figma-plugin).

##### 2026-04-16 — Opus 4.7

  ### Opus 4.7


![Opus 4.7](https://cdn.magicpatterns.com/uploads/s6Agyx1hGMUU6YiAnZhTja/opus47.png)

  Opus 4.7 is now available in Magic Patterns. It brings two key improvements:

  * **Better vision** — Upload a screenshot to Magic Patterns and Opus 4.7 performs better relative to other models.
  * **Fewer errors** — Opus 4.7 tends to verify its output before finishing, resulting in more reliable generations.

##### 2026-04-15 — Move Files Between Workspaces

  ### Move Files Between Workspaces


![Move Files Between Workspaces](https://cdn.magicpatterns.com/uploads/cCfwJZdrt33DxMB91dGGDE/right-click-to-change-files.png)

  You can now right-click on any file in the dashboard to move it between workspaces. This makes it easy to reorganize your designs across different team workspaces without duplicating work.

  See [Team Workspaces](/documentation/collaboration/team-workspaces#moving-files-between-workspaces) for details.

##### 2026-04-14 — Usage Reports

  ### Usage Reports


![Usage Reports](https://cdn.magicpatterns.com/uploads/jcHU4QviYhREXQAGjYWm5P/usage-report.png)

  **Business** and **Enterprise** workspaces can open **Usage Reports** at [Settings → Usage Reports](https://www.magicpatterns.com/settings/usage-reports) to track adoption, compare activity on a team leaderboard, and review time saved. Other plans see an upgrade path to unlock reporting.

  See [Team Workspaces](/documentation/collaboration/team-workspaces#usage-reporting) for details.

##### 2026-04-10 — Skills

  ### Skills


![Skills](https://cdn.magicpatterns.com/uploads/4emZCwH7stZGrtRE1Bk49T/Skills.png)

  A simple, open format for giving the Magic Patterns agent new capabilities and expertise. Skills are folders of instructions, scripts, and resources that the agent can discover and load on demand to do real work more accurately and efficiently.

  Use Skills to capture procedural knowledge and company-, team-, or user-specific context in portable, version-controlled packages the agent can draw from based on the task it's working on.

  Access Skills at [Settings > Skills](https://www.magicpatterns.com/settings/skills).

##### 2026-04-09 — Spacing and Misc Tokens added to Design Systems

  ### Spacing and Misc Tokens added to Design Systems


![Spacing and Misc Tokens added to Design Systems](https://cdn.magicpatterns.com/uploads/fDZaUBePi6SjT6Gg6gpDmj/Spacing-and-misc.png)

  You can now define spacing and miscellaneous tokens directly in your Design System. This gives you more control over consistent spacing, sizing, and other design tokens across your team's designs.

##### 2026-03-28 — Improved Agent

  ### Improved Agent

  Our agent just got a significant upgrade across the board:

  * **18% less credits** — More efficient generations mean your credits go further.
  * **10% faster** — Reduced latency for quicker iterations.
  * **12% more intelligent** — Better understanding of your prompts and more accurate designs.

  In addition, our agent now has better context management + memory. It will remember
  past details better and handle long conversations more efficiently.

  Enabled by default across all models for all users!

##### 2026-03-26 — Anthropic Integration

  ### Anthropic Integration


![Anthropic Integration in the chatbar](https://cdn.magicpatterns.com/uploads/bhuL6kJSi7iUbGQUw76eXj/integrations.png)

  We noticed people like designing chatbots... Introducing our Anthropic integration! You can now use the Anthropic API directly in Magic Patterns. Use it to create a working chatbot or support other AI-powered features directly in your Magic Patterns design.

  Enable the integration from the integrations section in the chatbar. We also support [OpenAI](/documentation/integrations/openai) integration, so you can choose the AI provider that works best for you.

  Learn more about setting up the [Anthropic integration](/documentation/integrations/anthropic) or the [OpenAI integration](/documentation/integrations/openai) in our documentation.

##### 2026-03-25 — Model Picker

  ### Model Picker


![Model Picker](https://cdn.magicpatterns.com/uploads/ix4iL7te4QLwrzHRwNvqFZ/model-picker.png)

  You can now choose which AI model works best for you, depending on the task. Different models have different strengths: some are better for quick iterations, while others excel at complex design challenges.

  Hover over each model option to see how they compare, including credit usage per generation. This helps you make informed decisions about which model to use based on your current task.

##### 2026-03-24 — Cross-Project Referencing via MCP

  ### Cross-Project Referencing via Magic Patterns MCP

  You can now reference and merge designs across projects.

  This works out of the box by using the Magic Patterns MCP as a Connector *within Magic Patterns*.

  Simply connect the [Magic Patterns MCP](/documentation/features/mcp-server/overview) as a [Connector](/documentation/connectors/connectors), then share any Magic Patterns link in your prompts.

  Example prompt: "Use the Magic Patterns Connector/MCP to get the navigation bar from [https://www.magicpatterns.com/c/456](https://www.magicpatterns.com/c/456) and the settings panel from [https://www.magicpatterns.com/c/design-b](https://www.magicpatterns.com/c/design-b), then combine them into a single layout component"

  [Learn more about Merging Designs](/documentation/editor/merging-designs).

##### 2026-03-20 — New Plans, Credits, and On-Demand Usage

  ### New Plans, Credits, and On-Demand Usage

  Today we're introducing a new credit system, on-demand usage with pay-as-you-go billing, and restructured pricing plans.

  [Read the full details here](https://www.magicpatterns.com/blog/new-plans-and-pricing).


![New Plans](https://cdn.magicpatterns.com/uploads/s1QVVWDpnVFjJTMorANtt3/New-Plans.png)

##### 2026-03-19 — Icons in Design Systems

  ### Icons in Design Systems


![Icons in Design Systems](https://cdn.magicpatterns.com/uploads/qBtfHka8P8BNJc1xnjLG5a/add-icon-to-changelog.png)

  You can now manage custom icons directly in your Design System. Choose from popular icon libraries like Lucide, or import your own custom icons by uploading SVG files or providing URLs.

  Icons are a dedicated section in your [Design System](/documentation/design-systems/overview). Learn more about [using custom icons](/documentation/design-systems/editing/typography-and-icons#icons).

##### 2026-03-17 — New Credit System

  ### Reminder: New Credit System and Pricing Updates

  As shared earlier this month, we're introducing a new credit system, on-demand usage with pay-as-you-go billing, and restructured pricing plans. These changes take effect on **Friday, March 20, 2026**. Emails have been sent to all existing customers.

  For existing customers, you'll be automatically upgraded to a new equivalent plan at no additional cost. Your current pricing will be honored through June 30, 2026 or until your next renewal if you're on an annual plan.

  [Read the exciting new updates here](https://www.magicpatterns.com/blog/new-plans-and-pricing). If you have any questions, we're here to help. Feel free to reach out to our support team at [support@magicpatterns.com](mailto:support@magicpatterns.com) or use our in-app chat. We believe this will unlock a lot for our power users.

##### 2026-03-11 — Image Nodes in the Canvas

  ### Image Nodes in the Canvas


![Image Nodes in the Canvas](https://cdn.magicpatterns.com/uploads/3ncgXndDQGyrvB65nnRXAj/image-node.png)

  You can now drop in screenshots and images directly onto the canvas! This feature does not cost a credit because no AI is needed.

##### 2026-03-04 — Copy Paste from Figma

  ### Copy Paste from Figma

  Copy frames and components directly from Figma into Magic Patterns. Connect your Figma account, select any element in Figma, copy it, and paste it right into your design. No importing or exporting required.



  Thank you to Magic Patterns user [Steve Witmer](https://www.linkedin.com/feed/update/urn:li:activity:7435718701959540736/) for his help and [feedback](https://www.magicpatterns.com/docs/documentation/feature-releases/changelog#2026-02-25) with this change!

##### 2026-03-03 — Rename Versions

  ### Rename Versions


![Rename Versions](https://cdn.magicpatterns.com/uploads/su6NBdM2SXEiH3Cc7geCPA/Rename_Versions.png)

  You can now rename versions directly in the versions dropdown. Give your versions meaningful names to keep track of your design iterations.

##### 2026-03-03 — Fork in Preview Links

  ### Fork in Share Links


![Fork in Preview Links](https://cdn.magicpatterns.com/uploads/wFbRVpH5cUaK4DGDJ1qET4/Fork-in-preview.png)

  Anyone viewing your share link can now [fork](/documentation/editor/forking) your design directly from the preview. This makes it easy for teammates to create their own version of a shared design.

  [Learn more about sharing and preview links](/documentation/editor/sharing).

##### 2026-03-02 — New Pricing

  ### New Credit System and Pricing Updates on March 20, 2026

  We're introducing a new credit system, on-demand usage with pay-as-you-go billing, and restructured pricing plans. These changes take effect on **Friday, March 20, 2026**. Emails have been sent to all existing customers.

  For existing customers, you'll be automatically upgraded to a new equivalent plan at no additional cost. Your current pricing will be honored through June 30, 2026 or until your next renewal if you're on an annual plan.

  [Read the full details here](https://www.magicpatterns.com/blog/new-plans-and-pricing). If you have any questions, we're here to help. Feel free to reach out to our support team at [support@magicpatterns.com](mailto:support@magicpatterns.com) or use our in-app chat.

##### 2026-02-28 — New MCP Tools

  ### New MCP Tools

  Our MCP server now letting you specify which design system to use when creating designs programmatically.

  We've also added several new tools:

  * `list_design_systems` — Discover available design systems
  * `create_blank_design` — Create a new blank design with default scaffold files
  * `create_design` — Create a design from a natural language prompt
  * `create_new_artifact` — Clone the current artifact for safe editing
  * `read_files` / `write_files` / `edit_files` — Read and modify files in an artifact
  * `compile_artifact_changes` — Compile after making file changes
  * `update_design_from_prompt` — Update a design using natural language

  [Learn more about the MCP Server](/documentation/features/mcp-server/overview).

##### 2026-02-26 — Command K

  ### Command K



  Press `⌘K` (or `Ctrl+K` on Windows) to quickly access actions, navigate between designs, and search across your workspace. Command K gives you instant access to everything you need without leaving the keyboard.

##### 2026-02-25 — Submit feedback, get featured

  ### Submit Feedback and Get Featured

  We use Magic Patterns internally to build Magic Patterns.

  Submitting feedback here will spin up an internal Magic Patterns prototype for us to review and implement into our codebase. If shipped, we'll credit you here in the changelog. We're thankful for your feedback!


![Prompt submission improvements screenshot placeholder](https://cdn.magicpatterns.com/uploads/tGAqJgTqHEs3HWyUNVGbDN/submit-a-feedback-prompt-for-our-team.png)

##### 2026-02-24 — Brand Import for Design Systems

  ### Brand & Color Import for Design Systems


![Brand Import](https://cdn.magicpatterns.com/uploads/5pGNSV8rr3fXseaYx5KhUM/brand-import.gif)

  You can now import your brand, typography, color tokens directly into your Design System.

  Paste your website URL and Magic Patterns will automatically extract your brand's colors, fonts, and styles to populate your Design System.

##### 2026-02-19 — Color Tokens

  ### Color Tokens in Design Systems


![Color Tokens](https://cdn.magicpatterns.com/uploads/s3aFvV399BaX39EaLmoEMY/Colors.gif)

  You can now define and manage color tokens directly in your Design System.

  Your color tokens are also available in **Visual Edit**. When editing an element's colors, they appear in the color picker under **"On this design"** for quick selection.

##### 2026-02-18 — Official Claude Connector

  ### Official Claude Connector


![Official Claude Connector](https://cdn.magicpatterns.com/uploads/rNnx9V7JWK7dxuyKakUE29/1771516263016.jpg)

  Magic Patterns is now an official Claude connector! This recognition from Anthropic highlights our deep integration with Claude's capabilities, enabling seamless AI-powered UI generation directly within the Claude ecosystem.

##### 2026-02-16 — Connectors

  ### Connectors


![Connectors](https://cdn.magicpatterns.com/uploads/uozzmvhEAVeiV7EoVLSryP/Connectors.gif)

  Magic Patterns can now work with your external tools, databases, and applications to give you more relevant AI responses. Powered by the Model Context Protocol (MCP), connectors let the AI assistant pull in real context from the services you already use -- like meeting notes, project issues, or analytics data -- and incorporate it directly into your designs.

  Built-in support is available for **Granola**, **Notion**, **Linear**, and **PostHog**, with more coming soon. You can also add your own custom MCP server.

  For example: if you use Granola, you can now prompt the AI assistant to pull in your latest meeting notes and use them to inform a design.

  [Learn more in the Connectors documentation](/documentation/connectors/connectors).

##### 2026-02-10 — Typography in Design Systems

  ### Typography in Design Systems

  Generate designs that look like your font, automatically!

  Upload your custom font, choose a popular Google Font, or simply paste your font URL.

  Typography is a dedicated section in your [Design System](/documentation/design-systems/overview). Learn more about [using custom fonts](/documentation/design-systems/editing/typography-and-icons).


![Typography in Design Systems](https://cdn.magicpatterns.com/static/docs/typography.png)

##### 2026-02-08 — Emails sent when sharing

  ## Emails sent when sharing designs

  For a long time, users thought our system would send an email when they invited someone to a design. This is now "fixed." Emails are now sent when you invite someone. Thanks for your feedback!


![Improved Invite Email](https://cdn.magicpatterns.com/uploads/qHaioK4EtScgyJBYaqEak2/email-sending.png)

##### 2026-02-06 — Improved Dashboard Navigation

  ### Improved Dashboard Navigation

  We've refreshed the navigation on the dashboard for a cleaner, more intuitive experience.

##### 2026-02-05 — Opus 4.6 in Auto Mode

  ### Opus 4.6 Now Default in Auto

  "Auto" mode now uses Claude Opus 4.6 by default, unless your organization has disabled it.

##### 2026-02-04 — Design Systems

  ### Design Systems

  Design Systems are the new way to keep consistent styles, colors, typography, and components across your team's designs.

  Your existing presets and component libraries have been automatically migrated to Design Systems.


![Design Systems](https://cdn.magicpatterns.com/static/docs/design-systems.png)

  [Read more in our blog post](https://www.magicpatterns.com/blog/introducing-design-systems) or check out the [Design Systems documentation](/documentation/design-systems/overview).

##### 2026-01-31 — Visual Edit

  ### Visual Edit

  Sometimes, you don't need the AI. You're now in control: select any element in your design and edit it manually. Change text, colors, spacing, and other properties from the Visual Edit panel.

  This feature was in beta, but is now available to everyone.


![Visual Edit](https://cdn.magicpatterns.com/uploads/pCUQU5TXwkhDtHHwpkr5W7/visual-edit-screenshot.png)

##### 2026-01-28 — Queue Messages

  ### Queue Messages

  You can now queue multiple prompts while a generation is in progress. Each prompt is processed in order.

  Queued prompts appear below the input field. You can remove any queued prompt before it starts.


![Queue Messages](https://cdn.magicpatterns.com/static/docs/queue-messages.png)

##### 2026-01-21 — MUI Preset

  ### MUI Default Design System

  Generate components using our Material UI (MUI) Design System default

  **How it works:**

  * Tap the Design System Selector from the Dashboard
  * Select MUI

##### 2026-01-16 — Text Nodes in the Canvas

  ### Annotate Your Canvas

  Add text nodes directly to your canvas to describe user flows, label prototypes, and keep your workspace organized.

  **How it works:**

  * Click the text tool in the toolbar to add a text node anywhere on your canvas
  * Double-click to edit the text inline
  * Adjust font size, weight, and alignment using the floating controls
  * Drag to reposition or resize the text box to fit your layout

  Perfect for documenting design decisions, labeling prototype variations, or creating visual hierarchies across your projects.


![Text Nodes in the Canvas](https://cdn.magicpatterns.com/uploads/j2m6UsXbCyo4KQcdczBYmX/TextNodes.png)

##### 2026-01-12 — Collecting External Feedback

  ### Collect Feedback in the Chatbar

  We've moved the "Collect External Feedback" feature to the integrations section of the chatbar.

  You can enable external feedback collection on your designs from the integrations section in the chatbar.

  This adds a structured feedback form directly on your publish link. View more details in our [Collecting External Feedback](/documentation/integrations/collecting-feedback) documentation.

  Access it via the **integrations section in the chatbar → Collect External Feedback**.


![Collecting External Feedback in the chatbar](https://cdn.magicpatterns.com/uploads/bhuL6kJSi7iUbGQUw76eXj/integrations.png)

##### 2026-01-12 — Inline Preview Comments


![Inline Preview Comments](https://cdn.magicpatterns.com/static/docs/comments-in-preview.png)

  ### Inline Preview Comments

  Leave comments directly on your preview to collaborate with your team. Click anywhere on the design to start a conversation — perfect for gathering feedback without leaving the browser.

  We also refreshed the preview page with viewport controls, so you can see how your design looks across different screen sizes.

  Access it via **Share → Preview Link**.

##### 2026-01-04 — OAuth in MCP Server

  ### OAuth 2.0 Authentication for MCP Server

  Our MCP Server now supports OAuth 2.0 authentication. Simply connect and authorize through your browser — no more manually copying API keys into headers.

  This makes setup faster and keeps your credentials more secure.

##### 2025-12-24 — Updated Share & Publish Panels


![Updated Share Panel](https://cdn.magicpatterns.com/uploads/hLz5mzwxDWRcge45n1sdQz/share-panel.png)

  ### Updated Share & Publish Panels

  Sharing designs with teammates and publishing to the web are two of the most popular things you do with your prototypes.

  We gave both panels a UI & UX upgrade to make these workflows faster and more intuitive.

##### 2025-12-19 — Magic Patterns MCP Server


![Connect to Magic Patterns MCP](https://cdn.magicpatterns.com/static/docs/connect-to-mcp.png)

  ### Magic Patterns MCP Server

  Your favorite AI tools & agents can now connect to your Magic Patterns design via our MCP Server.

  One of our favorite new workflows is adding the Magic Patterns MCP to Cursor. When connected, you can simply
  tell Cursor the link to your Magic Patterns prototype and Cursor will automatically implement it
  in your codebase following your codebase's conventions.

  [Learn how to configure the MCP Server with your favorite tools here.](/documentation/features/mcp-server/overview)

##### 2025-12-12 — Video → UI


![Uploading a video](https://cdn.magicpatterns.com/static/docs/video-access.png)

  ### Uploading a Video

  Animate interactions, generate full user flows, debug issues, all from just uploading a single file.

  You can use a video when creating a new design or updating an existing one.

##### 2025-12-09 — Converting Presets


![Converting presets flow](https://cdn.magicpatterns.com/static/docs/convert.gif)

  ### Converting Presets

  You can now change the [preset](/documentation/get-started/presets) of an existing design to a different preset.

  Key benefits:

  * Change Presets: Switch between Wireframe, Shadcn, Chakra, Mantine, or your own Custom Presets without starting over.
  * Non-destructive: Creates a new version of your design, preserving your original generation.

  How to try it:

  * Open any design and click the "Convert" button in the top bar.
  * Choose a new preset (like switching between two of your custom presets with different design systems).
  * Watch as a new design is generated in a separate tab.

##### 2025-12-04 — Publishing

  ### Publishing to a Custom Website Address

  Publish your designs as live websites with a custom website address or your own domain.

  **Key features:**

  * **Custom Website Address:** Create shareable URLs like `project-alex.magicpatterns.app`
  * **Custom Domains:** Connect your own domain or subdomain.
  * **Multiple Domains:** Add multiple domains to the same design

  [Learn more about publishing and custom preview URLs](/documentation/publishing/publish-url).

##### 2025-12-03 — Agent Mode


![Agent Mode Examples](https://cdn.magicpatterns.com/static/agent-mode/AgentModeShowcaseGif.gif)

  ### Agent Mode

  Agent Mode is our new architecture designed specifically for rapid prototyping, creative inspiration, and building production interfaces.

  Read more about it's capabilities in [our blog post here](https://www.magicpatterns.com/blog/agent-mode).

##### 2025-11-14 — Device Frames


![Device Frames](https://cdn.magicpatterns.com/static/docs/device-frames.png)

  ### Device Frames

  For specific viewports, you can now display a device frame around your design. Currently, these are the supported device frames:

  * iPhone SE
  * iPad Pro

  More to come!

##### 2025-11-07 — Templates


![Templates](https://cdn.magicpatterns.com/static/marketing/Template.png)

  ### Templates

  Organize your reusable designs with Templates. Convert any design into a template and access them all from a dedicated tab in your dashboard.

  **How it works:**

  * Click the dropdown next to your design name and select "Publish Template"
  * All your templates appear in the Templates tab on your dashboard
  * Fork from any template to create a new design based on it
  * Unpublish templates anytime to remove them from the Templates tab

##### 2025-11-06 — Enhance Prompt


![Enhance Prompt](https://cdn.magicpatterns.com/static/marketing/Enhance-prompt.gif)

  ### Enhance Prompt

  Get better results with AI-powered prompt enhancement. Magic Patterns now helps you refine your prompts before generating.

  **How it works:**

  * Click the "Enhance this prompt" button in the prompt input field
  * AI automatically refines your prompt for clarity and specificity
  * Get higher-quality designs with more accurate results

##### 2025-10-17 — Figma Remote MCP

  ### Figma Remote MCP

  Importing from Figma got a massive upgrade. We now enrich frames and components with context from the Figma MCP automatically (you no longer need the Chrome extension + dekstop app).

  Read more about how we designed this feature in [our latest blog post](https://www.magicpatterns.com/blog/using-magic-patterns-to-design-magic-patterns).

  ### Upgraded Personal & Workspace Settings

  Our settings page was getting really long with all the features we've been shipping. We improved this page to help you better manage your team + customize your Magic Patterns experience.

  ### Refreshed documentation

  We made it easier to find the information you need. If you have any feedback on what documentation you'd like to see, we're all ears!

##### 2025-10-13 — OpenAI Integration


![OpenAI Integration](https://cdn.magicpatterns.com/uploads/9u92zsAsxWq3sopCfdpCoe/Open-ai-integration.png)

  ### OpenAI Integration

  You can now bring your own OpenAI API key to power AI generation in your designs and prototypes.

  **Key features:**

  * Input your OpenAI API key directly in the integrations section of the chatbar
  * Use AI-powered features with your own OpenAI account
  * API keys are automatically available across all your designs once configured

  Get your OpenAI API key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

  Learn more about the OpenAI integration in our [documentation](/documentation/integrations/openai).

##### 2025-10-06 — Upgrade Component Instances


![Upgrade Component Instances](https://cdn.magicpatterns.com/Upgrade-components.png)

  ### Upgrade Component Instances

  When you publish a new version of a component, you can now upgrade all instances across your designs in one place.

  **How it works:**

  * When you publish a new component version, a modal appears showing all designs that use that component
  * Select which designs you want to upgrade and click "Upgrade Instances" to update them all at once

##### 2025-09-19 — Sound Notifications

  ### Sound Notifications

  **Enabled by default for all users!**

  * Get a gentle chime when your design is ready
  * Multitask while Magic Patterns works in the background

  How to disable:

  1. Go to Settings > [Preferences](https://www.magicpatterns.com/settings#preferences) > Sound Notifications
  2. Toggle "Sound Notifications" off

##### 2025-09-12 — Credit Rollovers


![Credit History](https://mintcdn.com/magicpatterns/-6mEJ6LOnSDWyslO/images/credit_hist.png?fit=max&auto=format&n=-6mEJ6LOnSDWyslO&q=85&s=46d6f5cd9f5752dbbc93370b9137b361)

  ### Credit Rollovers

  * Credits now rollover month-over-month
  * See your credit history in [your settings](https://www.magicpatterns.com/settings#credit-history)

  Read more about this update [in our blog here](https://www.magicpatterns.com/blog/credit-rollovers).

  ### Closed beta

  Two new features are releasing under closed beta.

  * Agent Mode
  * Integration with Figma MCP

  If you're interested in testing either of these, reach out!

##### 2025-09-01 — Improved Import from Figma

  ### Improved Import from Figma

  * We've improved the Import from Figma to capture exact color values.

  ### Other Improvements & New Features

  * Improved Import from Figma
  * Dashboard QoL features (renaming files, performance improvements)
  * Editor QoL features (refresh preview, page dropdown, etc)
  * Fixed issues with Delete Element
  * Improved sync with GitHub reliability

##### 2025-08-15 — New Fast Model

  ### New Fast Model

  * "Fast" mode now runs on Claude Sonnet 4.
  * We've seen major improvements in debugging issues, listening to instructions, and solving unique challenges
  * We'd still recommend using "Best" for large UI changes or more "inspirational" guidance

  ### Improved Site Hosting

  * We migrated our site hosting infrastructure to a new system that loads previews 2x faster
  * Sites hosted through our custom domain feature will also be faster + more stable

  ### Other Improvements & New Features

  * Import from Figma is now in early access. Coming to everyone next week.
  * Default page routing
  * Convert between presets
  * Improved error handling for sync with Github
  * Fixed preview on canvas
  * Supporting more NPM packages

##### 2025-08-01 — Referral Program

  ### Referral Program

  * Earn credits by inviting your teammates and friends to Magic Patterns
  * Find your unique referral link on the Magic Patterns dashboard

  ### Other Improvements & New Features

  * Granular permissions on libraries
  * Automatic Detach Components preference
  * Support for Meta Pixels and Google Tags
  * General stability and error improvements
  * Improved login experience
  * Lots of bug fixes

##### 2025-07-01 — Shared with me

  ### Shared with me tab

  * We've added a new "Shared with me" section to the dashboard.
  * You can now see all the designs that have been shared with you.

  ### Other Improvements & New Features

  * Granular permissions on canvases
  * SAML SSO Authentication
  * Improved support chat interface
  * Better troubleshooting documentation
  * Automatic error detection + fixing
  * Improved dashboard loading performance
  * Better support for mock data via xlsx and csv files
  * Support for many more NPM packages
  * Ability to deprecate components
  * Ability to add additional context when creating a component

  ### Bug Fixes

  * Support for latest lucide icons
  * Easier site navigation in canvas
  * Fixed bug with versioning dropdown
  * Fixed issues of infinitely hanging generations
  * Fixed performance issues
  * Improved platform stability and handling for outages out of our control

##### 2025-06-01 — Granular Permissions

  ### Invite your team, set permissions, and control read/write access

  1. If you click the share button in the top-right corner of any design, you can now invite your team to collaborate on the design.
  2. You can also control who has access to the design.


![image](https://mintcdn.com/magicpatterns/dyhr1UMzzXl3NtrZ/documentation/editor/images/editor-sharing.png?fit=max&auto=format&n=dyhr1UMzzXl3NtrZ&q=85&s=695262cbdbd6ed2c255a6f70dfbe5751)

  Other updates:

  * Better error handling
  * Component source code included when possible in code export
  * Improved AI context handling
  * Ability to rename components
  * New /Debug and /Discuss commands

##### 2025-05-01 — New Dashboard and Custom Components

  ### "Chats" renamed to "Designs" and "Projects" renamed to "Canvas"

  1. We revamped our dashboard: [magicpatterns.com/dashboard](https://magicpatterns.com/dashboard)
  2. We renamed "Projects" to "Canvas"

  Users consistently referred to the infinite canvas as "the canvas." So, we renamed it. Naming is hard. Internally, we called it "Spaces," then settled on "Projects." But it got extra confusing when people referred to chats as "projects." We are listening to the community here and officially renamed it to "Canvas."

  More excitingly, we revamped the dashboard to show libraries and components.

  ## Custom components in public beta

  We're excited to announce components in public beta, read more here: [Custom Components](/documentation/custom-components/creating-a-library)

  1. **Custom components in public beta**
  2. **Thinking is exposed**
  3. **Improved preview image generation**

##### 2025-04-01 — Feedback Collection and Password Protection

  We're excited to announce two major features:

  1. **Structured feedback collection**
  2. **Password protection for shared designs**

  You can now gather feedback directly through Magic Patterns by configuring custom questions for stakeholders.

  Additionally, you can secure your shared prototypes with password protection to control who has access to your designs.



##### 2025-03-01 — Custom Domains and Improved Preview Links

  We're excited to several new features:

  1. **Custom domains**
  2. **Image upload improvements**
  3. **Preview links — more human-readable and shareable**
  4. **Lots and lots of bug fixes**

  Read more about custom domains here: [Custom domains](/documentation/get-started/custom-domain)

##### 2025-02-01 — Editor UI Refresh and Performance Improvements

  We're excited to several new features and improvements:

  1. **Refresh of our core editor UI**
  2. **Previews now load 5x faster**
  3. **Page routing**
  4. **Model Mode: Fast or Quality (Sonnet 3.5 vs 3.7)**
  5. **Moved our API product to our new infrastructure**
  6. **"Copy Prompt" feature/integration on 21st.dev**

##### 2025-01-01 — Workspaces

  We're excited to announce Workspaces and other improvements:

  1. **Workspaces**
  2. **Added diff-ing**
  3. **Ability to undo**

##### 2024-12-01 — API Product and Projects Released

  1. **API Product Released, read more here: [API](/documentation/api/getting-started)**
  2. **Release of infinite canvas, read more here: [canvas](/documentation/projects/getting-started)**


---

## API Reference

### Create a new artifact
*Creates a new artifact by cloning an existing one (typically the*

**Source:** https://www.magicpatterns.com/docs/api/create-artifact

currently active artifact). The new artifact becomes the active
artifact for the design and a new version entry is added to the
timeline.

Use this to create a safe working branch before writing files —
users can revert to the previous artifact if needed.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs/{editorId}/artifacts
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/artifacts:
    post:
      tags:
        - Artifacts
      summary: Create a new artifact
      description: |
        Creates a new artifact by cloning an existing one (typically the
        currently active artifact). The new artifact becomes the active
        artifact for the design and a new version entry is added to the
        timeline.

        Use this to create a safe working branch before writing files —
        users can revert to the previous artifact if needed.
      operationId: createArtifactV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sourceArtifactId
                - name
              properties:
                sourceArtifactId:
                  type: string
                  description: >-
                    The artifact ID to clone from (usually the current active
                    artifact).
                name:
                  type: string
                  description: >-
                    A name for this artifact version, shown in the design
                    timeline.
                  example: Header tweaks
      responses:
        '200':
          description: New artifact created and set as active.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ArtifactSummary'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
  schemas:
    ArtifactSummary:
      type: object
      properties:
        artifactId:
          type: string
        files:
          type: array
          items:
            type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Create a design
*Creates a new Magic Patterns design.*

**Source:** https://www.magicpatterns.com/docs/api/create-design

Behavior depends on the request:
- **With `prompt`**: kicks off AI generation in the background. The
  response returns immediately with `editorId`; poll
  `GET /v3/designs/{editorId}/status` until `isGenerating` is `false`.
  Generation typically takes 2–10 minutes.
- **Without `prompt`**: creates a blank design with scaffold files
  (App.tsx, index.tsx, index.css, tailwind.config.js) and returns
  immediately.
- **With `templateId`**: forks an existing design first, then optionally
  applies the prompt to the fork.

Generation calls bill credits from the authenticated user's normal
credit balance.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs:
    post:
      tags:
        - Designs
      summary: Create a design
      description: |
        Creates a new Magic Patterns design.

        Behavior depends on the request:
        - **With `prompt`**: kicks off AI generation in the background. The
          response returns immediately with `editorId`; poll
          `GET /v3/designs/{editorId}/status` until `isGenerating` is `false`.
          Generation typically takes 2–10 minutes.
        - **Without `prompt`**: creates a blank design with scaffold files
          (App.tsx, index.tsx, index.css, tailwind.config.js) and returns
          immediately.
        - **With `templateId`**: forks an existing design first, then optionally
          applies the prompt to the fork.

        Generation calls bill credits from the authenticated user's normal
        credit balance.
      operationId: createDesignV3
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDesignRequest'
      responses:
        '200':
          description: Design created. If generation is in flight, poll status.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateDesignResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '402':
          $ref: '#/components/responses/InsufficientCredits'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  schemas:
    CreateDesignRequest:
      type: object
      properties:
        name:
          type: string
          description: Optional name for the design. Defaults to "Untitled".
          example: Onboarding flow
        prompt:
          type: string
          description: |
            Optional natural-language prompt. If supplied, AI generation runs
            in the background and the caller must poll
            `GET /v3/designs/{editorId}/status`. If omitted, a blank design
            with scaffold files is created instantly.
          example: A login page with social sign-in.
        imageUrls:
          type: array
          description: >-
            Optional image URLs to use as visual references (only used with
            `prompt`).
          items:
            type: string
            format: uri
        designSystemId:
          type: string
          description: >-
            Optional ID of the design system to use. Discover IDs via `GET
            /v3/design-systems`.
        designSystem:
          type: string
          description: >-
            Optional design system name (e.g. "Shadcn"). Resolved
            case-insensitively. `designSystemId` takes precedence if both are
            provided.
        templateId:
          type: string
          description: >-
            Optional editor ID of an existing design to use as a template. The
            design is forked first, then any prompt is applied to the fork.
    CreateDesignResponse:
      type: object
      properties:
        editorId:
          type: string
          example: abc123
        editorUrl:
          type: string
          format: uri
          example: https://www.magicpatterns.com/c/abc123
        previewUrl:
          type: string
          format: uri
          nullable: true
          description: >-
            Live preview URL. Only populated once the first artifact has been
            compiled.
          example: https://project-onboarding-flow.magicpatterns.app
        activeArtifactId:
          type: string
          nullable: true
          description: >-
            The artifact created at design-creation time. Null until the first
            artifact is ready.
        availableFiles:
          type: array
          items:
            type: string
          description: >-
            File names in the active artifact. Empty while generation is still
            running.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InsufficientCredits:
      description: The authenticated user has run out of credits.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Get the active artifact
*Returns the design's currently active artifact — the one shown in the*

**Source:** https://www.magicpatterns.com/docs/api/get-active-artifact

editor and preview. Includes the artifact ID and the list of file
names in it.

Because the active artifact can change (the user may select a different
version in the UI, or AI generation may produce a new artifact),
always call this (or `GET /v3/designs/{editorId}/status`) to get the
latest active artifact before working with files.

#### OpenAPI

````yaml openapi-v3.yml get /v3/designs/{editorId}/active-artifact
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/active-artifact:
    get:
      tags:
        - Artifacts
      summary: Get the active artifact
      description: |
        Returns the design's currently active artifact — the one shown in the
        editor and preview. Includes the artifact ID and the list of file
        names in it.

        Because the active artifact can change (the user may select a different
        version in the UI, or AI generation may produce a new artifact),
        always call this (or `GET /v3/designs/{editorId}/status`) to get the
        latest active artifact before working with files.
      operationId: getActiveArtifactV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
      responses:
        '200':
          description: Active artifact summary.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ArtifactSummary'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
  schemas:
    ArtifactSummary:
      type: object
      properties:
        artifactId:
          type: string
        files:
          type: array
          items:
            type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Read recent message history
*Returns the last 10 chat items for a design (user prompts, AI*

**Source:** https://www.magicpatterns.com/docs/api/get-design-messages

responses, artifact versions, manual edits). Use `?skip=N` to paginate
backwards through older items. Page size is fixed at 10.

Because the editor is collaborative, the user (or other agents) may
have sent prompts or made changes between your tool calls. Use this
to stay in sync with the current state.

Code contents are omitted from chat items to keep the response small.
Use `POST /v3/designs/{editorId}/artifacts/{artifactId}/files/read`
to read full file contents.

#### OpenAPI

````yaml openapi-v3.yml get /v3/designs/{editorId}/messages
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/messages:
    get:
      tags:
        - Designs
      summary: Read recent message history
      description: |
        Returns the last 10 chat items for a design (user prompts, AI
        responses, artifact versions, manual edits). Use `?skip=N` to paginate
        backwards through older items. Page size is fixed at 10.

        Because the editor is collaborative, the user (or other agents) may
        have sent prompts or made changes between your tool calls. Use this
        to stay in sync with the current state.

        Code contents are omitted from chat items to keep the response small.
        Use `POST /v3/designs/{editorId}/artifacts/{artifactId}/files/read`
        to read full file contents.
      operationId: getDesignMessagesV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
        - $ref: '#/components/parameters/Skip'
      responses:
        '200':
          description: Paginated chat history.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatHistoryPage'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
    Skip:
      name: skip
      in: query
      required: false
      description: Number of most-recent items to skip (for pagination). Defaults to 0.
      schema:
        type: integer
        minimum: 0
        default: 0
  schemas:
    ChatHistoryPage:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/ChatHistoryItem'
        hasMore:
          type: boolean
          description: >-
            True if there are older items beyond this page. Paginate with
            `?skip=`.
    ChatHistoryItem:
      type: object
      properties:
        id:
          type: string
        role:
          type: string
          description: One of `user`, `assistant`, `app`.
          example: assistant
        app:
          type: string
          nullable: true
          description: Origin label for `app`-role items (e.g. `api`, `mcp`).
        content:
          type: array
          items: {}
          description: Item content blocks (summarized — code is omitted).
        timeCreated:
          type: integer
          description: Milliseconds since the Unix epoch.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Get design status
*Returns the current state of a design: whether AI generation is in*

**Source:** https://www.magicpatterns.com/docs/api/get-design-status

flight, the active artifact ID, and which files exist in that artifact.

Use this to poll after `POST /v3/designs` (with a prompt) or
`POST /v3/designs/{editorId}/prompts`. Poll no more than once every
60 seconds.

#### OpenAPI

````yaml openapi-v3.yml get /v3/designs/{editorId}/status
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/status:
    get:
      tags:
        - Designs
      summary: Get design status
      description: |
        Returns the current state of a design: whether AI generation is in
        flight, the active artifact ID, and which files exist in that artifact.

        Use this to poll after `POST /v3/designs` (with a prompt) or
        `POST /v3/designs/{editorId}/prompts`. Poll no more than once every
        60 seconds.
      operationId: getDesignStatusV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
      responses:
        '200':
          description: Current design status.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DesignStatus'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
  schemas:
    DesignStatus:
      type: object
      properties:
        isGenerating:
          type: boolean
          description: True while AI generation is in flight.
        activeArtifactId:
          type: string
          nullable: true
          description: The design's currently active artifact, or null if none.
        availableFiles:
          type: array
          items:
            type: string
          description: File names in the active artifact.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### List version history
*Returns the most recent 20 artifact versions for a design, with their*

**Source:** https://www.magicpatterns.com/docs/api/get-design-versions

artifact IDs, labels, and titles. Use `?skip=N` to paginate backwards.
Page size is fixed at 20.

Each version corresponds to a snapshot of the design's code at a point
in time. Use the returned `artifactId` with the artifact read/write
endpoints, or fork from it with `POST /v3/designs/{editorId}/artifacts`.

#### OpenAPI

````yaml openapi-v3.yml get /v3/designs/{editorId}/versions
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/versions:
    get:
      tags:
        - Designs
      summary: List version history
      description: |
        Returns the most recent 20 artifact versions for a design, with their
        artifact IDs, labels, and titles. Use `?skip=N` to paginate backwards.
        Page size is fixed at 20.

        Each version corresponds to a snapshot of the design's code at a point
        in time. Use the returned `artifactId` with the artifact read/write
        endpoints, or fork from it with `POST /v3/designs/{editorId}/artifacts`.
      operationId: getDesignVersionsV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
        - $ref: '#/components/parameters/Skip'
      responses:
        '200':
          description: Paginated version history.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VersionHistoryPage'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
    Skip:
      name: skip
      in: query
      required: false
      description: Number of most-recent items to skip (for pagination). Defaults to 0.
      schema:
        type: integer
        minimum: 0
        default: 0
  schemas:
    VersionHistoryPage:
      type: object
      properties:
        versions:
          type: array
          items:
            $ref: '#/components/schemas/VersionHistoryItem'
        hasMore:
          type: boolean
    VersionHistoryItem:
      type: object
      properties:
        artifactId:
          type: string
        versionLabel:
          type: string
          example: v3
        title:
          type: string
          example: Onboarding redesign
        timeCreated:
          type: integer
          nullable: true
          description: Milliseconds since the Unix epoch.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Getting Started
*Programmatic access to Magic Patterns with the v3 API*

**Source:** https://www.magicpatterns.com/docs/api/getting-started

The Magic Patterns API lets you create and iterate on designs programmatically — kicking off generations, polling status, reading and writing artifact files, and publishing changes — all from your own systems.

v3 is the current API surface. It mirrors the [Magic Patterns MCP server](/documentation/features/mcp-server/overview) endpoint-for-endpoint, so the same key works for both REST and MCP. You don't need to choose.

> ℹ️ **Note:**
> Already integrated against the legacy `/v2/pattern` endpoint? See the [v2 reference](/documentation/api/getting-started). v2 is being deprecated and will be removed in a future release — plan to migrate to v3 when convenient.

#### Authentication

All v3 endpoints require an API key in the `x-mp-api-key` header.


**Log in**

    Sign in (or create an account) at [magicpatterns.com](https://www.magicpatterns.com/).


**Create an API key**

    Open [Settings → API Keys](https://www.magicpatterns.com/settings/api-keys) and click **Create Key**. Copy the key immediately — you can only see it once.


**Send your first request**

    Use the key in the `x-mp-api-key` header on every request.

```bash theme={null}
curl https://api.magicpatterns.com/api/v3/health \
  -H "x-mp-api-key: mp_live_..."
```

A `200 OK` with `{"status":"ok"}` confirms your key is valid.

#### Billing

v3 usage draws from your normal Magic Patterns **credit balance** — the same credits the web app and MCP use. There is no separate API subscription.

* Free-tier accounts get free monthly credits and can call v3 up to that limit.
* Need more? Upgrade your plan or buy credit packs at [Settings → Billing & Subscription](https://www.magicpatterns.com/settings/subscription).
* When you run out, v3 calls that consume credits return `402 Payment Required`. Read endpoints continue to work.

#### Quickstart: create a design

This kicks off generation in the background, then polls until the design is ready.

```bash theme={null}
### 1. Create the design — returns immediately with an editorId.
curl https://api.magicpatterns.com/api/v3/designs \
  -H "x-mp-api-key: mp_live_..." \
  -H "Content-Type: application/json" \
  -d '{"prompt": "A landing page for a coffee shop"}'

### Response:
### { "editorId": "abc123", "editorUrl": "https://www.magicpatterns.com/c/abc123", ... }

### 2. Poll status until generation finishes. Wait at least 60 seconds between polls.
curl https://api.magicpatterns.com/api/v3/designs/abc123/status \
  -H "x-mp-api-key: mp_live_..."

### Response:
### { "isGenerating": false, "activeArtifactId": "...", "availableFiles": [...] }
```

Generation typically takes 2–10 minutes. **Don't poll more than once every 60 seconds.**

#### Asynchronous endpoints

Two endpoints kick off long-running work and return immediately:

* `POST /v3/designs` (when `prompt` is set)
* `POST /v3/designs/{editorId}/prompts`

Both return a `requestId` (or `editorId`) right away. To know when the work is done, poll `GET /v3/designs/{editorId}/status` until `isGenerating` is `false`.

There are no webhooks in v3 — polling is the only mechanism. We may add webhooks in a future release if customers ask.

#### Same key for MCP

The same API key authenticates the [Magic Patterns MCP server](/documentation/features/mcp-server/overview) — no separate OAuth login required. Configure the MCP server with an `Authorization: Bearer <your-api-key>` header (the MCP server also accepts `x-mp-api-key`), and the key works across both transports. See [API Key Authentication](/documentation/features/mcp-server/overview#api-key-authentication) for client config examples.

#### Common errors

| Status | Meaning                                                                                              |
| ------ | ---------------------------------------------------------------------------------------------------- |
| `400`  | Invalid input — check the request body and parameters.                                               |
| `401`  | Missing or invalid `x-mp-api-key`.                                                                   |
| `402`  | Out of credits. Top up at [Settings → Billing](https://www.magicpatterns.com/settings/subscription). |
| `403`  | The key's owner doesn't have access to the requested design or artifact.                             |
| `404`  | The design or artifact doesn't exist.                                                                |
| `422`  | Compilation failed on a `publish` call.                                                              |
| `500`  | Unexpected server error — logged on our side.                                                        |

All error responses are `application/json` with a single `error` field:

```json theme={null}
{ "error": "Insufficient credits. Please upgrade your plan or add credits." }
```

#### Rate limits

1000 generations per 10 hours per key. Contact us if you need a higher limit.

#### Next steps


- **[Browse endpoints](/api/health)** — Full API reference with request/response examples and a try-it widget.


- **[MCP server](/documentation/features/mcp-server/overview)** — Use the same key with our Model Context Protocol server.

### Health check
*Returns `200 OK` only when the supplied API key is valid and active.*

**Source:** https://www.magicpatterns.com/docs/api/health

Returns `401 Unauthorized` for invalid or missing keys. Use this to
verify your key and connectivity before making real requests.

#### OpenAPI

````yaml openapi-v3.yml get /v3/health
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/health:
    get:
      tags:
        - Health
      summary: Health check
      description: |
        Returns `200 OK` only when the supplied API key is valid and active.
        Returns `401 Unauthorized` for invalid or missing keys. Use this to
        verify your key and connectivity before making real requests.
      operationId: healthV3
      responses:
        '200':
          description: Key is valid and active.
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ok
        '401':
          $ref: '#/components/responses/Unauthorized'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### List design systems
*Returns every design system accessible to the authenticated user —*

**Source:** https://www.magicpatterns.com/docs/api/list-design-systems

both built-in (reserved) systems (e.g. Base, Shadcn, MUI) and any
custom systems the user owns or has been invited to.

Use the returned `id` as the `designSystemId` parameter when creating
new designs.

#### OpenAPI

````yaml openapi-v3.yml get /v3/design-systems
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/design-systems:
    get:
      tags:
        - Design Systems
      summary: List design systems
      description: |
        Returns every design system accessible to the authenticated user —
        both built-in (reserved) systems (e.g. Base, Shadcn, MUI) and any
        custom systems the user owns or has been invited to.

        Use the returned `id` as the `designSystemId` parameter when creating
        new designs.
      operationId: listDesignSystemsV3
      responses:
        '200':
          description: List of accessible design systems.
          content:
            application/json:
              schema:
                type: object
                properties:
                  designSystems:
                    type: array
                    items:
                      $ref: '#/components/schemas/DesignSystem'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  schemas:
    DesignSystem:
      type: object
      properties:
        id:
          type: string
          description: Pass this as `designSystemId` when creating a design.
          example: ds-9b80b54e-92b3-4b2f-8265-afe466ee8b75
        name:
          type: string
          example: Shadcn
        isReserved:
          type: boolean
          description: True for built-in design systems (Base, Shadcn, MUI, etc).
        isActive:
          type: boolean
          description: True for the user's currently selected default design system.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Publish an artifact
*Compiles the artifact's source files and sets it as the active*

**Source:** https://www.magicpatterns.com/docs/api/publish-artifact

artifact for the design. This is the final step in a code-first
workflow: after writing files, call this to make the changes visible
in the editor and live preview.

Returns `422 Unprocessable Entity` if compilation fails.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs/{editorId}/artifacts/{artifactId}/publish
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/artifacts/{artifactId}/publish:
    post:
      tags:
        - Artifacts
      summary: Publish an artifact
      description: |
        Compiles the artifact's source files and sets it as the active
        artifact for the design. This is the final step in a code-first
        workflow: after writing files, call this to make the changes visible
        in the editor and live preview.

        Returns `422 Unprocessable Entity` if compilation fails.
      operationId: publishArtifactV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
        - $ref: '#/components/parameters/ArtifactId'
      responses:
        '200':
          description: Compiled and activated.
          content:
            application/json:
              schema:
                type: object
                properties:
                  artifactId:
                    type: string
                  compiledFiles:
                    type: array
                    items:
                      type: string
                    description: File names that were emitted by the compiler.
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '422':
          description: Compilation failed.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
    ArtifactId:
      name: artifactId
      in: path
      required: true
      description: The artifact ID.
      schema:
        type: string
  responses:
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Read artifact files
*Returns the contents of one or more files in an artifact. Files that*

**Source:** https://www.magicpatterns.com/docs/api/read-artifact-files

don't exist in the artifact are simply omitted from the response.

This endpoint uses POST (with a request body) rather than GET (with a
query string) so file names containing `/`, commas, or other special
characters don't need URL encoding.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs/{editorId}/artifacts/{artifactId}/files/read
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/artifacts/{artifactId}/files/read:
    post:
      tags:
        - Artifacts
      summary: Read artifact files
      description: |
        Returns the contents of one or more files in an artifact. Files that
        don't exist in the artifact are simply omitted from the response.

        This endpoint uses POST (with a request body) rather than GET (with a
        query string) so file names containing `/`, commas, or other special
        characters don't need URL encoding.
      operationId: readArtifactFilesV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
        - $ref: '#/components/parameters/ArtifactId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - fileNames
              properties:
                fileNames:
                  type: array
                  description: The file names to read.
                  items:
                    type: string
                  example:
                    - App.tsx
                    - index.css
      responses:
        '200':
          description: Requested files.
          content:
            application/json:
              schema:
                type: object
                properties:
                  files:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          example: App.tsx
                        content:
                          type: string
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
    ArtifactId:
      name: artifactId
      in: path
      required: true
      description: The artifact ID.
      schema:
        type: string
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Resolve a Magic Patterns URL to an editor ID
*Given a Magic Patterns URL, returns the underlying `editorId`. Supports:*

**Source:** https://www.magicpatterns.com/docs/api/resolve-design-url

- Design URLs: `magicpatterns.com/c/<editorId>`
- Published URLs: `project-<slug>.magicpatterns.app`
- Canvas URLs: `magicpatterns.com/s/<canvasId>?nodeIds=<nodeId>`

Use this when a user shares a Magic Patterns link and you need the
`editorId` to call other endpoints.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs/resolve-url
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/resolve-url:
    post:
      tags:
        - Designs
      summary: Resolve a Magic Patterns URL to an editor ID
      description: |
        Given a Magic Patterns URL, returns the underlying `editorId`. Supports:

        - Design URLs: `magicpatterns.com/c/<editorId>`
        - Published URLs: `project-<slug>.magicpatterns.app`
        - Canvas URLs: `magicpatterns.com/s/<canvasId>?nodeIds=<nodeId>`

        Use this when a user shares a Magic Patterns link and you need the
        `editorId` to call other endpoints.
      operationId: resolveDesignUrlV3
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - url
              properties:
                url:
                  type: string
                  description: A Magic Patterns design / published / canvas URL.
                  example: https://www.magicpatterns.com/c/abc123
      responses:
        '200':
          description: Resolved editor ID.
          content:
            application/json:
              schema:
                type: object
                properties:
                  editorId:
                    type: string
                    example: abc123
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Send a prompt
*Sends a natural-language prompt to update an existing design. Returns*

**Source:** https://www.magicpatterns.com/docs/api/send-prompt

immediately with a `requestId`; the AI generation runs in the
background.

Poll `GET /v3/designs/{editorId}/status` until `isGenerating` is
`false`. Generation typically takes 2–10 minutes; do not poll more
than once every 60 seconds.

Before calling, check `GET /v3/designs/{editorId}/status` to confirm
the design isn't already generating.

Bills credits from the authenticated user's normal credit balance.

#### OpenAPI

````yaml openapi-v3.yml post /v3/designs/{editorId}/prompts
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/prompts:
    post:
      tags:
        - Designs
      summary: Send a prompt
      description: |
        Sends a natural-language prompt to update an existing design. Returns
        immediately with a `requestId`; the AI generation runs in the
        background.

        Poll `GET /v3/designs/{editorId}/status` until `isGenerating` is
        `false`. Generation typically takes 2–10 minutes; do not poll more
        than once every 60 seconds.

        Before calling, check `GET /v3/designs/{editorId}/status` to confirm
        the design isn't already generating.

        Bills credits from the authenticated user's normal credit balance.
      operationId: sendPromptV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - prompt
              properties:
                prompt:
                  type: string
                  description: Natural language description of the change to make.
                  example: Add a footer with three columns of links.
      responses:
        '200':
          description: Prompt accepted. Generation runs in the background.
          content:
            application/json:
              schema:
                type: object
                properties:
                  requestId:
                    type: string
                    description: Opaque identifier for this generation run.
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '402':
          $ref: '#/components/responses/InsufficientCredits'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InsufficientCredits:
      description: The authenticated user has run out of credits.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````

### Write artifact files
*Creates or overwrites one or more files in an artifact. Files that*

**Source:** https://www.magicpatterns.com/docs/api/write-artifact-files

already exist are replaced; new files are appended. Files not
mentioned in the request are left untouched.

This only updates source files — it does **not** compile or publish.
Call `POST /v3/designs/{editorId}/artifacts/{artifactId}/publish` when
you're done with all file changes to compile and set the artifact
active.

#### OpenAPI

````yaml openapi-v3.yml patch /v3/designs/{editorId}/artifacts/{artifactId}/files
openapi: 3.0.3
info:
  title: Magic Patterns API (v3)
  version: 3.0.0
  description: |
    The Magic Patterns API v3 provides programmatic access to design generation,
    iteration, and code-level editing. v3 mirrors the surface of the Magic
    Patterns MCP server — a single key authenticates both transports.

    v3 bills against your normal Magic Patterns credit balance. There is no
    separate API subscription. Free tier users can call v3 up to their credit
    limit, identical to web and MCP usage.

    For the legacy v2 single-shot creation endpoint (separate $99/mo plan),
    see the v2 reference.
servers:
  - url: https://api.magicpatterns.com/api
security:
  - ApiKeyAuth: []
tags:
  - name: Health
  - name: Design Systems
  - name: Designs
  - name: Artifacts
paths:
  /v3/designs/{editorId}/artifacts/{artifactId}/files:
    patch:
      tags:
        - Artifacts
      summary: Write artifact files
      description: |
        Creates or overwrites one or more files in an artifact. Files that
        already exist are replaced; new files are appended. Files not
        mentioned in the request are left untouched.

        This only updates source files — it does **not** compile or publish.
        Call `POST /v3/designs/{editorId}/artifacts/{artifactId}/publish` when
        you're done with all file changes to compile and set the artifact
        active.
      operationId: writeArtifactFilesV3
      parameters:
        - $ref: '#/components/parameters/EditorId'
        - $ref: '#/components/parameters/ArtifactId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - files
              properties:
                files:
                  type: array
                  minItems: 1
                  items:
                    type: object
                    required:
                      - fileName
                      - code
                    properties:
                      fileName:
                        type: string
                        example: App.tsx
                      code:
                        type: string
                        description: >-
                          Full file contents (replaces any existing content for
                          that file).
      responses:
        '200':
          description: >-
            Updated. Response lists all file names in the artifact after the
            write.
          content:
            application/json:
              schema:
                type: object
                properties:
                  files:
                    type: array
                    items:
                      type: string
                    example:
                      - App.tsx
                      - index.tsx
                      - index.css
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '403':
          $ref: '#/components/responses/Forbidden'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
components:
  parameters:
    EditorId:
      name: editorId
      in: path
      required: true
      description: The design's editor ID.
      schema:
        type: string
        example: abc123
    ArtifactId:
      name: artifactId
      in: path
      required: true
      description: The artifact ID.
      schema:
        type: string
  responses:
    BadRequest:
      description: Invalid or missing required input.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Missing or invalid API key.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: The caller does not have access to this resource.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    NotFound:
      description: The requested design or artifact does not exist.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Unexpected server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  schemas:
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Human-readable error message.
          example: You do not have access to this resource.
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-mp-api-key
      description: >
        Magic Patterns API key. The same key authenticates v3 REST and the

        MCP server. Create one at
        https://www.magicpatterns.com/settings/api-keys.

````
