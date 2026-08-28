# Gumloop Documentation — Complete Guide (Part 3: MCP Connector Nodes)

*This document was scraped and cleaned from Gumloop's official documentation for ingestion into NotebookLM as a learning-plan source. Custom UI components (callouts, cards, tabs, steps, accordions) have been converted to plain Markdown.*

- **Source:** https://docs.gumloop.com
- **Part:** 3 of 3 — Node Reference — MCP Connectors
- **Pages in this file:** 119 (of 420 total pages across the full guide)
- **Date scraped:** 2026-07-18

## Table of Contents

- [Node Reference — MCP Connectors](#node-reference-mcp-connectors)
  - [Affinity](#affinity)
  - [Ahrefs](#ahrefs)
  - [Airtable](#airtable)
  - [Apify](#apify)
  - [Apollo](#apollo)
  - [AppSheet](#appsheet)
  - [Asana](#asana)
  - [Ashby](#ashby)
  - [Attio](#attio)
  - [Basedash](#basedash)
  - [Beehiiv](#beehiiv)
  - [BigQuery](#bigquery)
  - [Bing Webmaster](#bing-webmaster)
  - [Box](#box)
  - [Brandfetch](#brandfetch)
  - [Cal.com](#calcom)
  - [Canva](#canva)
  - [Carta](#carta)
  - [Chorus](#chorus)
  - [Circleback](#circleback)
  - [ClickHouse](#clickhouse)
  - [ClickUp](#clickup)
  - [Cloudflare](#cloudflare)
  - [Confluence](#confluence)
  - [Cursor](#cursor)
  - [Custom MCP Servers](#custom-mcp-servers)
  - [Databricks](#databricks)
  - [Datadog](#datadog)
  - [Devin](#devin)
  - [Dropbox](#dropbox)
  - [Exa](#exa)
  - [Excel](#excel)
  - [Expensify](#expensify)
  - [Extend](#extend)
  - [Fal](#fal)
  - [Fathom](#fathom)
  - [Fellow](#fellow)
  - [Findymail](#findymail)
  - [Firecrawl](#firecrawl)
  - [Foreplay](#foreplay)
  - [Freshdesk](#freshdesk)
  - [Freshsales](#freshsales)
  - [Gamma](#gamma)
  - [GitHub](#github)
  - [Gmail](#gmail)
  - [Gong](#gong)
  - [Google Ads](#google-ads)
  - [Google Analytics](#google-analytics)
  - [Google Calendar](#google-calendar)
  - [Google Cloud Storage](#google-cloud-storage)
  - [Google DV360](#google-dv360)
  - [Google Docs](#google-docs)
  - [Google Drive](#google-drive)
  - [Google Maps](#google-maps)
  - [Google Meet](#google-meet)
  - [Google PageSpeed](#google-pagespeed)
  - [Google Search Console](#google-search-console)
  - [Google Sheets](#google-sheets)
  - [Google Slides](#google-slides)
  - [Google Tasks](#google-tasks)
  - [Granola](#granola)
  - [Greenhouse](#greenhouse)
  - [Gumloop](#gumloop)
  - [Hex](#hex)
  - [HubSpot](#hubspot)
  - [Incident.io](#incidentio)
  - [Instagram](#instagram)
  - [Intercom](#intercom)
  - [Ironclad](#ironclad)
  - [Jam](#jam)
  - [Jira](#jira)
  - [Klaviyo](#klaviyo)
  - [LaunchDarkly](#launchdarkly)
  - [Linear](#linear)
  - [Looker](#looker)
  - [Loops](#loops)
  - [Luma](#luma)
  - [Microsoft Teams](#microsoft-teams)
  - [Microsoft Word](#microsoft-word)
  - [Monday](#monday)
  - [NetSuite](#netsuite)
  - [Notion](#notion)
  - [Outlook](#outlook)
  - [Outlook Calendar](#outlook-calendar)
  - [Outreach](#outreach)
  - [PagerDuty](#pagerduty)
  - [Parallel](#parallel)
  - [Pipedrive](#pipedrive)
  - [PostgreSQL](#postgresql)
  - [Pylon](#pylon)
  - [QuickBooks](#quickbooks)
  - [Ramp](#ramp)
  - [Reddit](#reddit)
  - [Reducto](#reducto)
  - [Robinhood](#robinhood)
  - [Rocketlane](#rocketlane)
  - [Salesforce](#salesforce)
  - [Salesloft](#salesloft)
  - [Seismic](#seismic)
  - [Semrush](#semrush)
  - [Sentry](#sentry)
  - [Shopify](#shopify)
  - [Sigma Computing](#sigma-computing)
  - [Similarweb](#similarweb)
  - [Slack](#slack)
  - [Snowflake](#snowflake)
  - [Sprig](#sprig)
  - [Stripe](#stripe)
  - [Supabase](#supabase)
  - [Tableau](#tableau)
  - [TikTok](#tiktok)
  - [Trello](#trello)
  - [Vercel](#vercel)
  - [Webflow](#webflow)
  - [Workday](#workday)
  - [X (Twitter)](#x-twitter)
  - [YouTube](#youtube)
  - [Zendesk](#zendesk)
  - [Zoom](#zoom)

---

## Node Reference — MCP Connectors

### Affinity

*Manage your CRM relationships, deals, and notes with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/affinity

Manage your CRM relationships, deals, and notes with AI-powered automation.

Affinity is a relationship intelligence CRM built for dealmakers. The Affinity MCP server lets you search contacts, manage deals, update fields, and create notes using natural language.

#### What Can It Do?

* **Search and retrieve** people, organizations, opportunities, and notes
* **Create and update** contacts, companies, deals, and list entries
* **Manage custom fields** to keep data synced across your tools
* **Add notes** to track conversations and follow-ups

#### Where to Use It

##### In Agents (Recommended)

Add Affinity as a tool to any agent. The agent can then interact with your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Affinity tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search persons by email and return their name and company")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| **Get All Lists**           | Retrieve all lists you have access to                |
| **Get List**                | Get details for a specific list                      |
| **Get List Entries**        | Retrieve entries from a list with pagination         |
| **Get List Entry**          | Get details for a single list entry                  |
| **Create List Entry**       | Add a person, organization, or opportunity to a list |
| **Delete List Entry**       | Remove an entity from a list                         |
| **Get Fields**              | Retrieve all fields with optional filters            |
| **Get Field Values**        | Get field values for an entity                       |
| **Create Field Value**      | Create or update a field value                       |
| **Update Field Value**      | Update an existing field value                       |
| **Delete Field Value**      | Clear a field value                                  |
| **Search Persons**          | Search people in your database                       |
| **Get Person**              | Get details for a single person                      |
| **Create Person**           | Create a new person                                  |
| **Update Person**           | Update a person's information                        |
| **Delete Person**           | Delete a person                                      |
| **Get Person Fields**       | List global person fields                            |
| **Search Organizations**    | Search organizations                                 |
| **Get Organization**        | Get details for an organization                      |
| **Create Organization**     | Create a new organization                            |
| **Update Organization**     | Update an organization                               |
| **Delete Organization**     | Delete an organization                               |
| **Get Organization Fields** | List global organization fields                      |
| **Search Opportunities**    | Search deals/opportunities                           |
| **Get Opportunity**         | Get details for an opportunity                       |
| **Create Opportunity**      | Create a new opportunity                             |
| **Update Opportunity**      | Update an opportunity                                |
| **Delete Opportunity**      | Delete an opportunity                                |
| **Get Notes**               | Retrieve notes with filters                          |
| **Get Note**                | Get a specific note                                  |
| **Create Note**             | Create a new note                                    |
| **Update Note**             | Update an existing note                              |
| **Delete Note**             | Delete a note                                        |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find key contacts:**

```text
Find all people with "Partner" in their title at venture capital firms
```

**Track a new deal:**

```text
Create a new opportunity called "Series A - TechCo" and add it to the Active Pipeline list
```

**Update deal status:**

```text
Move the "Seed Round - StartupXYZ" opportunity to the Due Diligence stage
```

**Log a meeting:**

```text
Add a note to Sarah Chen at Sequoia: "Great intro call, interested in our ML approach. Follow up next week with deck."
```

**Get pipeline overview:**

```text
Show me all opportunities in the Negotiation stage with their associated organizations
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Be more specific with names or add context like "in list X" or "from organization Y"                                                       |
| Action not completing            | Check that you've authenticated and have the necessary permissions in Affinity                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., listing projects first, then querying). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find issues in the Marketing project" will automatically list projects, find the right ID, then query issues. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Affinity MCP server](https://www.gumloop.com/mcp/affinity) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Ahrefs

*Analyze backlinks, keywords, and SEO performance with AI-powered search marketing automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/ahrefs

Analyze backlinks, keywords, and SEO performance with AI-powered search marketing automation.

Ahrefs is a comprehensive SEO toolset for backlink analysis, keyword research, rank tracking, and site auditing. The Ahrefs MCP server lets you access SEO data and analytics using natural language.

#### What Can It Do?

* **Analyze backlinks and domains** with ratings, referring domains, and anchor text
* **Research keywords** with volume, difficulty, SERP data, and suggestions
* **Track rankings** across projects and competitors
* **Audit sites** for SEO issues and page content
* **Monitor brand mentions** in AI chatbot responses

#### Where to Use It

##### In Agents (Recommended)

Add Ahrefs as a tool to any agent. The agent can then analyze SEO data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Ahrefs tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get the domain rating for example.com")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Site Explorer

| Tool                            | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| **Domain Rating**               | Get domain rating for a domain                         |
| **Backlinks Stats**             | Get backlinks statistics for a domain or URL           |
| **Outlinks Stats**              | Get outlinks statistics for a domain or URL            |
| **Metrics**                     | Get comprehensive metrics for a domain or URL          |
| **Metrics By Country**          | Get metrics filtered by country for a domain or URL    |
| **Pages By Traffic**            | Get pages by traffic for a domain or URL               |
| **Domain Rating History**       | Get domain rating history for a domain                 |
| **URL Rating History**          | Get URL rating history for a URL                       |
| **Refdomains History**          | Get referring domains history for a domain or URL      |
| **Pages History**               | Get pages history for a domain or URL                  |
| **Metrics History**             | Get metrics history for a domain or URL                |
| **Keywords History**            | Get keywords history for a domain or URL               |
| **Total Search Volume History** | Get total search volume history for a domain or URL    |
| **Backlinks**                   | Get backlinks for a domain or URL                      |
| **Broken Backlinks**            | Get broken backlinks for a domain or URL               |
| **Refdomains**                  | Get referring domains for a domain or URL              |
| **Anchors**                     | Get anchor text for a domain or URL                    |
| **Organic Keywords**            | Get organic keywords for a domain or URL               |
| **Organic Competitors**         | Get organic competitors for a domain or URL            |
| **Top Pages**                   | Get top organic pages for a domain                     |
| **Paid Pages**                  | Get paid pages for a domain or URL                     |
| **Best By External Links**      | Get pages with the most external links                 |
| **Best By Internal Links**      | Get pages with the most internal links                 |
| **Linked Domains**              | Get domains that are linked from the target            |
| **Outgoing External Anchors**   | Get external anchor texts used in outgoing links       |
| **Outgoing Internal Anchors**   | Get internal anchor texts used in outgoing links       |
| **Batch Analysis**              | Batch analyze multiple URLs or domains for SEO metrics |

##### Keywords Explorer

| Tool                   | Description                                     |
| ---------------------- | ----------------------------------------------- |
| **Keywords Overview**  | Get metrics for keywords from Keywords Explorer |
| **Volume History**     | Get search volume history for a keyword         |
| **Volume By Country**  | Get search volume by country for a keyword      |
| **Matching Terms**     | Get matching terms for keywords                 |
| **Related Terms**      | Get related terms for keywords                  |
| **Search Suggestions** | Get search suggestions for keywords             |
| **SERP Overview**      | Get top SERP results for a keyword              |

##### Rank Tracker

| Tool                                  | Description                                              |
| ------------------------------------- | -------------------------------------------------------- |
| **Rank Tracker Overview**             | Get keyword rankings overview for a Rank Tracker project |
| **Rank Tracker Competitors Overview** | Get competitor rankings for a Rank Tracker project       |
| **Rank Tracker Competitors Pages**    | Get competitor pages for a Rank Tracker project          |
| **Rank Tracker Competitors Stats**    | Get competitor statistics for a Rank Tracker project     |
| **Rank Tracker SERP Overview**        | Get SERP overview for a tracked keyword in Rank Tracker  |

##### Site Audit

| Tool                         | Description                                 |
| ---------------------------- | ------------------------------------------- |
| **Site Audit Projects**      | List Site Audit projects with health scores |
| **Site Audit Issues**        | Get SEO issues found by Site Audit          |
| **Site Audit Page Content**  | Get page content from a Site Audit crawl    |
| **Site Audit Page Explorer** | Explore pages from a Site Audit crawl       |

##### Brand Radar

| Tool                                 | Description                                      |
| ------------------------------------ | ------------------------------------------------ |
| **Brand Radar AI Responses**         | Get AI chatbot responses mentioning brands       |
| **Brand Radar Cited Domains**        | Get domains cited in AI responses about brands   |
| **Brand Radar Cited Pages**          | Get pages cited in AI responses about brands     |
| **Brand Radar Impressions Overview** | Get brand impression statistics from AI chatbots |
| **Brand Radar Mentions Overview**    | Get brand mention statistics from AI chatbots    |
| **Brand Radar Impressions History**  | Get brand impressions over time from AI chatbots |
| **Brand Radar Mentions History**     | Get brand mentions over time from AI chatbots    |
| **Brand Radar SOV History**          | Get share of voice history from AI chatbots      |
| **Brand Radar SOV Overview**         | Get share of voice overview from AI chatbots     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check domain authority:**

```text
Get the domain rating for competitor.com
```

**Analyze backlinks:**

```text
Show me the backlink stats for our website example.com
```

**Research keywords:**

```text
Get keyword overview for "project management software"
```

**Find competitors:**

```text
Who are the organic competitors for example.com?
```

**Audit site health:**

```text
List all Site Audit projects and their health scores
```

**Track brand mentions:**

```text
Show AI chatbot responses that mention our brand
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use exact domain names without protocol (e.g., "example.com" not "[https://example.com](https://example.com)")                                   |
| Action not completing            | Check that you've authenticated with Ahrefs                                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., getting domain rating first, then backlinks). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                              |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Compare our backlink profile with competitor.com" will analyze both domains then present results. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Ahrefs MCP server](https://www.gumloop.com/mcp/ahrefs) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Airtable

*Search, create, and manage Airtable records with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/airtable

Search, create, and manage Airtable records with AI-powered automation.

Airtable is a flexible database platform that combines spreadsheet simplicity with database power. The Airtable MCP server lets you search, filter, create, and update records using natural language.

#### What Can It Do?

* **Retrieve records** with filters, sorts, and selected fields
* **Create and update** records to keep your tables current
* **Explore your workspace** by listing bases, tables, and schema
* **Manage structure** by creating and modifying fields
* **Manage comments** on records — create, update, and delete

#### Where to Use It

##### In Agents (Recommended)

Add Airtable as a tool to any agent. The agent can then interact with your bases conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Airtable tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List records from table X where status is Active")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool               | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| **List Records**   | Retrieve records with filtering, sorting, and field selection |
| **Create Records** | Create new records in a table                                 |
| **Update Records** | Update existing records                                       |
| **Get Record**     | Get a single record by ID                                     |
| **Delete Records** | Delete one or more records                                    |
| **List Bases**     | List all accessible bases                                     |
| **List Tables**    | List all tables in a base                                     |
| **Base Schema**    | Get detailed schema for all tables                            |
| **Create Table**   | Create a new table in a base with specified fields and types  |
| **Update Table**   | Update a table's name or description                          |
| **Create Field**   | Add a new field to a table                                    |
| **Update Field**   | Update a field's metadata                                     |
| **List Comments**  | List comments for a record                                    |
| **Create Comment** | Create a comment on a specific record                         |
| **Update Comment** | Update an existing comment on a record                        |
| **Delete Comment** | Delete a comment from a record                                |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Discover your workspace:**

```text
List all my Airtable bases and their tables
```

**Find specific records:**

```text
Get all records from the Projects table where Status is "In Progress"
```

**Create new data:**

```text
Add a new record to the Tasks table with Name "Review Q4 report" and Due Date "2024-12-15"
```

**Update records:**

```text
Update the record for "Project Alpha" to set Status to "Complete"
```

**Explore schema:**

```text
Show me all the fields in the Customers table and their types
```

**Add a comment:**

```text
Add a comment "Needs review" to the first record in the Tasks table
```

**Delete a comment:**

```text
Delete my last comment on the record for "Project Alpha"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                 |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Be more specific with table names and filter conditions                                                                                  |
| Action not completing            | Check that you've authenticated and have write permissions                                                                               |
| Unexpected results               | The agent may chain multiple tools (e.g., listing tables first, then querying). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                      |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find the project named Marketing Campaign" will automatically list bases, find the right table, then search for the record. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Airtable MCP server](https://www.gumloop.com/mcp/airtable) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Apify

*Discover and run web scraping Actors with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/apify

Discover and run web scraping Actors with AI-powered automation.

Apify is a platform for web scraping, data extraction, and automation. The Apify MCP server lets you search the Apify Store, run Actors and saved tasks, monitor runs, and retrieve results using natural language.

#### What Can It Do?

* **Search and discover Actors** in the Apify Store
* **Run Actors** synchronously or asynchronously with validated input
* **Manage saved tasks** for preconfigured Actor runs
* **Monitor run status** and retrieve logs
* **Read dataset results** from completed runs

#### Where to Use It

##### In Agents (Recommended)

Add Apify as a tool to any agent. The agent can then discover and run Actors conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Apify tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run a web scraper Actor on a URL")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Actor Discovery

| Tool                     | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Search Actors**        | Search runnable Actors in the Apify Store          |
| **Get Actor**            | Get Actor metadata and optionally its input schema |
| **Validate Actor Input** | Validate input for an Actor build before running   |

##### Running Actors

| Tool            | Description                                  |
| --------------- | -------------------------------------------- |
| **Run Actor**   | Run an Actor synchronously or asynchronously |
| **Get Run**     | Get Actor run status and metadata            |
| **Abort Run**   | Abort a running Actor run                    |
| **Get Run Log** | Get the log output from an Actor run         |

##### Saved Tasks

| Tool           | Description                                            |
| -------------- | ------------------------------------------------------ |
| **List Tasks** | List saved Apify Actor tasks                           |
| **Get Task**   | Get a saved Apify Actor task                           |
| **Run Task**   | Run a saved Actor task synchronously or asynchronously |

##### Results

| Tool                  | Description                     |
| --------------------- | ------------------------------- |
| **Get Dataset Items** | Get items from an Apify dataset |

> **Info:** The Gumloop-managed Apify key supports searching public Actors, reading public metadata, and running public limited-permission Actors synchronously. For full-permission Actors, async runs, saved tasks, run status, and dataset reads, connect your own Apify API key.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search for an Actor:**

```text
Find an Actor in the Apify Store that can scrape Google Maps reviews
```

**Run a scraper:**

```text
Run the web scraper Actor on https://example.com and return the results
```

**Check run status:**

```text
Check the status of my last Apify run
```

**Get results:**

```text
Get the dataset items from my completed Actor run
```

**Run a saved task:**

```text
Run my saved "Daily Product Scrape" task
```

#### Troubleshooting

| Issue                             | Solution                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| "Full-permission Actor" error     | Some Actors require your own Apify API key. Connect it in the integration settings                                  |
| Run stuck or timing out           | For long-running Actors, use async mode and check status with Get Run                                               |
| Agent not finding the right Actor | Use specific keywords or the Actor's full name from the Apify Store                                                 |
| Tool not available                | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Agents can chain tools together automatically. For example, asking "Scrape product data from this URL" will search for a suitable Actor, validate the input, run it, and return the results. Review the agent's reasoning if results seem off.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Apify MCP server](https://www.gumloop.com/mcp/apify) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Apollo

*Find, enrich, and track B2B contacts and companies with AI-powered prospecting.*

**Source:** https://docs.gumloop.com/nodes/mcp/apollo

Find, enrich, and track B2B contacts and companies with AI-powered prospecting.

Apollo is one of the world's largest B2B prospecting databases with 275M+ contacts and 73M+ companies. The Apollo MCP server lets you search prospects, enrich leads, and monitor companies using natural language.

#### What Can It Do?

* **Find prospects** with powerful filters for role, location, company, and keywords
* **Enrich leads** with fresh emails, titles, and firmographic data
* **Monitor companies** for job postings that signal buying intent
* **Search organizations** by industry, size, funding, and location

#### Where to Use It

##### In Agents (Recommended)

Add Apollo as a tool to any agent. The agent can then search and enrich prospects conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Apollo tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Find sales managers at SaaS companies in San Francisco")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                              | Description                                               |
| --------------------------------- | --------------------------------------------------------- |
| **People Search**                 | Find people by role, location, company, or keywords       |
| **Organization Search**           | Search companies by industry, size, location, and funding |
| **Enrich Person**                 | Get full profile data for a known email or person ID      |
| **Enrich Organization**           | Get firmographic data for a known domain or org ID        |
| **Get Organization Job Postings** | Retrieve current job listings for a company               |

#### Credit Costs

| Tool                          | Credits Per Use      |
| ----------------------------- | -------------------- |
| People Search                 | 3 credits per result |
| Organization Search           | 3 credits per result |
| Enrich Person                 | 3+ credits           |
| Enrich Organization           | 5 credits            |
| Get Organization Job Postings | 3 credits per result |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Prospect discovery:**

```text
Find 10 product managers at AI startups funded in the last 2 years
```

**Company research:**

```text
Search for cybersecurity companies with 50-200 employees in Austin
```

**Lead enrichment:**

```text
Get the full profile for john.smith@acme.com including their title and LinkedIn
```

**Hiring signals:**

```text
Show me the latest job postings from Stripe
```

**Targeted outreach:**

```text
Find VPs of Marketing at fintech companies in New York
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use more specific filters like job title, location, or company size                                                                                 |
| Action not completing            | Check that you've authenticated and have sufficient Apollo credits                                                                                  |
| Unexpected results               | The agent may chain multiple tools (e.g., searching companies first, then finding people). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find the CEO of companies that raised Series A last year" will search organizations first, then find people. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Apollo MCP server](https://www.gumloop.com/mcp/apollo) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### AppSheet

*Manage your AppSheet tables with AI-powered data operations.*

**Source:** https://docs.gumloop.com/nodes/mcp/appsheet

Manage your AppSheet tables with AI-powered data operations.

AppSheet is Google's no-code application platform that lets you build apps from spreadsheets and databases. The AppSheet MCP server lets you read, add, update, and delete rows using natural language.

#### What Can It Do?

* **Retrieve rows** from any table with filters and conditions
* **Add new rows** to keep your app data current
* **Update existing rows** to reflect changes from other systems
* **Delete rows** to clean up outdated records

#### Where to Use It

##### In Agents (Recommended)

Add AppSheet as a tool to any agent. The agent can then interact with your app's tables conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with AppSheet tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get all rows from Inventory where In Stock is true")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Setting Up AppSheet Credentials

Before using AppSheet, you need to enable API access in your app:

1. **Open Your AppSheet App**

   In the AppSheet editor, go to **Settings** → **Integrations**.

2. **Enable Cloud Services Access**

   Under **IN: from cloud services to your app**, toggle **Enable** to allow external services to communicate with your app.

3. **Copy Your App ID**

   Your **App Id** is displayed in the Integrations panel. Copy this value.

4. **Create an Access Key**

   Click **Create Application Access Key** to generate a new key. Copy the access key value.

5. **Add Credentials in Gumloop**

   Go to [Connectors page](https://www.gumloop.com/personal/connectors), add AppSheet, and enter your App ID and Access Key.

> **Warning:** Application Access Keys provide full access to your AppSheet app's data. Keep them secure and never share publicly.

#### Available Tools

| Tool            | Description                                      |
| --------------- | ------------------------------------------------ |
| **Get Rows**    | Retrieve rows from a table with optional filters |
| **Add Rows**    | Add new rows to a table                          |
| **Update Rows** | Update existing rows in a table                  |
| **Delete Rows** | Delete rows from a table                         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Retrieve records:**

```text
Get all rows from the Inventory table where In Stock is true
```

**Add new data:**

```text
Add a new contact: Name "Sarah Smith", Email "sarah@example.com", Company "Acme Corp"
```

**Update records:**

```text
Update the project PRJ-123 to set Status to "In Progress"
```

**Clean up data:**

```text
Delete all rows from the Logs table older than June 2024
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Include the app ID and exact table names in your request                                                                               |
| Action not completing            | Check that cloud services access is enabled and your access key is active                                                              |
| Unexpected results               | The agent may chain multiple tools (e.g., getting rows first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                    |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update all overdue tasks to high priority" will get the tasks first, then update them. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [AppSheet MCP server](https://www.gumloop.com/mcp/gappsheet) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Asana

*Manage projects, tasks, and teams with AI-powered work management.*

**Source:** https://docs.gumloop.com/nodes/mcp/asana

Manage projects, tasks, and teams with AI-powered work management.

Asana is a work management platform for organizing projects, tasks, and team collaboration. The Asana MCP server lets you create tasks, manage projects, and track work using natural language.

#### What Can It Do?

* **Create and update tasks** with assignees, due dates, tags, and custom fields
* **Retrieve tasks** by project, assignee, tag, or section
* **Manage project access** by adding or removing members and followers
* **Explore portfolios and sections** to keep stakeholders informed

#### Where to Use It

##### In Agents (Recommended)

Add Asana as a tool to any agent. The agent can then interact with your projects and tasks conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Asana tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a task in the Marketing project")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                             | Description                                                    |
| -------------------------------- | -------------------------------------------------------------- |
| **Get User Details**             | Get current user's details                                     |
| **List Projects**                | List accessible projects with filtering                        |
| **Get Project**                  | Get detailed project information                               |
| **Add/Remove Project Members**   | Manage project membership                                      |
| **Add/Remove Project Followers** | Manage project followers                                       |
| **List Tasks**                   | List tasks by project, tag, assignee, or section               |
| **Create Task**                  | Create a new task with assignee, due date, and custom fields   |
| **Get Task**                     | Get detailed task information                                  |
| **Update Task**                  | Update task properties including custom fields                 |
| **Delete Task**                  | Move a task to trash                                           |
| **Duplicate Task**               | Create a copy of a task                                        |
| **Create Subtask**               | Create a subtask under a parent task with custom field support |
| **Get Subtasks**                 | Get all subtasks of a task                                     |
| **Add/Remove Task Tags**         | Manage task tags                                               |
| **Add/Remove Task Followers**    | Manage task followers                                          |
| **Get Project Sections**         | Get all sections in a project                                  |
| **Get/Create Tags**              | Manage workspace tags                                          |
| **Get Portfolio**                | Get portfolio details                                          |
| **Get Portfolio Items**          | Get projects in a portfolio                                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a task:**

```text
Create a task "Review Q4 budget" in the Finance project, assign to sarah@company.com, due next Friday
```

**Find tasks:**

```text
Show me all tasks assigned to me that are due this week
```

**Update task status:**

```text
Mark the task "Prepare presentation" as complete
```

**Manage project access:**

```text
Add john@company.com as a member to the Product Launch project
```

**Get project overview:**

```text
List all sections in the Marketing Campaign project
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Be specific with project names or use "in workspace X" for clarity                                                                                   |
| Action not completing            | Check that you've authenticated and have permissions for the project                                                                                 |
| Unexpected results               | The agent may chain multiple tools (e.g., finding the project first, then creating a task). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                  |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a task in the Marketing project" will find the project ID first, then create the task. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Asana MCP server](https://www.gumloop.com/mcp/asana) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Ashby

*Streamline recruiting with AI-powered applicant tracking and scheduling.*

**Source:** https://docs.gumloop.com/nodes/mcp/ashby

Streamline recruiting with AI-powered applicant tracking and scheduling.

Ashby is a modern applicant tracking system (ATS) for recruiting teams. The Ashby MCP server lets you manage jobs, candidates, applications, and interview schedules using natural language.

#### What Can It Do?

* **Find and manage candidates** with search and filters
* **Create applications** and transfer them between jobs
* **Submit interview feedback** and review feedback form definitions
* **Read interview scorecards** and AI-generated criteria evaluations for applications
* **Download candidate files and interview transcripts** into Gumloop storage
* **View application history** and change application stages
* **Create and update interview schedules** with timing and participants
* **Manage interview plans, stages, and events** across jobs
* **Manage interviewer pools** with training requirements and roster updates
* **Create jobs, job postings, offers, and openings** end-to-end
* **Maintain job status** as roles open, pause, or close
* **Move applications** through stages with notes and tags
* **Read org-wide metadata** like departments, locations, sources, custom fields, archive reasons, and communication templates
* **Manage webhook subscriptions** for real-time event notifications

#### Where to Use It

##### In Agents (Recommended)

Add Ashby as a tool to any agent. The agent can then interact with your recruiting data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Ashby tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all open jobs in Engineering")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                                      | Description                                                           |
| ----------------------------------------- | --------------------------------------------------------------------- |
| **List/Get Users**                        | Search and get user details                                           |
| **List/Get Jobs**                         | Search jobs with filters                                              |
| **Update Job**                            | Update job properties                                                 |
| **Set Job Status**                        | Change job status (open/closed)                                       |
| **List/Get Candidates**                   | Search candidates                                                     |
| **Create Candidate**                      | Create a new candidate                                                |
| **Update Candidate**                      | Update candidate info                                                 |
| **Add Candidate Tag**                     | Tag a candidate                                                       |
| **Create Candidate Note**                 | Add a note to a candidate                                             |
| **List/Get Applications**                 | Search applications                                                   |
| **Update Application**                    | Update application properties                                         |
| **Change Application Stage**              | Move to a different stage                                             |
| **Change Application Source**             | Update the source                                                     |
| **List/Get Interviews**                   | Search interviews                                                     |
| **List/Get Interview Schedules**          | Get interview schedules                                               |
| **Create Interview Schedule**             | Schedule an interview                                                 |
| **Update Interview Schedule**             | Modify a schedule                                                     |
| **Cancel Interview Schedule**             | Cancel a schedule                                                     |
| **List/Get Interviewer Pools**            | Manage interviewer pools                                              |
| **Add User To Interviewer Pool**          | Add interviewers                                                      |
| **Create Interviewer Pool**               | Create a new interviewer pool                                         |
| **Update Interviewer Pool**               | Update an interviewer pool's title or training requirements           |
| **Create Application**                    | Create an application to consider a candidate for a job               |
| **Transfer Application**                  | Transfer an application to a different job                            |
| **List Application History**              | Get the stage transition history for an application                   |
| **Submit Application Feedback**           | Submit interview feedback for an application                          |
| **List Application Feedback**             | List interview scorecards and feedback submissions for an application |
| **List Application Criteria Evaluations** | List AI-generated criteria evaluations for an application             |
| **List Candidate Files**                  | List resume and attached files associated with a candidate            |
| **Download File**                         | Download a file or interview transcript from Ashby to Gumloop storage |
| **List Candidate Notes**                  | List all notes on a candidate with pagination                         |
| **Get Job Info**                          | Get detailed information about a specific job                         |
| **Get Job Interview Plan**                | Get the interview plan for a job including stages and activities      |
| **List Interview Plans**                  | List all interview plans with pagination                              |
| **List Interview Stages**                 | List all interview stages for a plan in order                         |
| **Get Interview Stage Info**              | Get detailed information about a specific interview stage             |
| **List Interview Stage Groups**           | List all interview stage groups with ordering                         |
| **List Interview Events**                 | List all interview events for a specific interview schedule           |
| **List Hiring Team Roles**                | List all available hiring team roles                                  |
| **List Archive Reasons**                  | List all archive reasons used when archiving applications             |
| **List Departments**                      | List all departments in the organization                              |
| **List Locations**                        | List all locations in the organization                                |
| **List Sources**                          | List all recruiting sources for candidate attribution                 |
| **List Custom Fields**                    | List all custom fields defined in the organization                    |
| **Set Custom Field Value**                | Set the value of a custom field on a candidate or application         |
| **List Communication Templates**          | List all email communication templates                                |
| **Create Job**                            | Create a new job posting                                              |
| **List Job Postings**                     | List all job postings with pagination                                 |
| **Get Job Posting Info**                  | Get detailed information about a specific job posting                 |
| **List Feedback Form Definitions**        | List all feedback form definitions for interview evaluations          |
| **Get Feedback Form Definition Info**     | Get detailed information about a specific feedback form definition    |
| **Create Offer**                          | Create a new offer for an application                                 |
| **Get Offer Info**                        | Get detailed information about a specific offer                       |
| **List Offers**                           | List all offers with pagination                                       |
| **List Openings**                         | List all job openings with pagination                                 |
| **Get Opening Info**                      | Get detailed information about a specific job opening                 |
| **Create Webhook Subscription**           | Create a webhook subscription for real-time event notifications       |
| **Delete Webhook Subscription**           | Delete a webhook subscription                                         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find open jobs:**

```text
List all open jobs in the Engineering department
```

**Search candidates:**

```text
Find candidates who applied for the Senior Engineer role
```

**Move an application:**

```text
Move Sarah Chen's application for Product Manager to the Interview stage
```

**Schedule an interview:**

```text
Schedule an interview for John Doe tomorrow at 2pm with the hiring manager
```

**Add a note:**

```text
Add a note to candidate Emily Wang: "Strong technical background, proceed to final round"
```

**Create an application:**

```text
Create an application for candidate Emily Wang for the Senior Engineer role
```

**Submit interview feedback:**

```text
Submit positive feedback for John Doe's Product Manager application using the "Technical Screen" form
```

**List openings and postings:**

```text
Show me all open openings and their active job postings in the Engineering department
```

**Check application history:**

```text
Show the stage transition history for Sarah Chen's Product Manager application
```

**Create an offer:**

```text
Create an offer for John Doe's Senior Engineer application starting next Monday
```

**Download a candidate's resume:**

```text
Download the resume for candidate Emily Wang and save it to my workspace
```

**Review interview feedback:**

```text
Show me all the interview scorecards and criteria evaluations for John Doe's Senior Engineer application
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific job titles or candidate names/emails                                                                                               |
| Action not completing            | Check that you've authenticated and have the necessary Ashby permissions                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., finding the candidate first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Move John's application to the next stage" will find the candidate and application first, then update the stage. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Ashby MCP server](https://www.gumloop.com/mcp/ashby) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Attio

*Manage contacts, companies, and relationships with AI-powered CRM automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/attio

Manage contacts, companies, and relationships with AI-powered CRM automation.

Attio is a modern relationship management platform that keeps contacts, companies, and interactions organized. The Attio MCP server lets you search, create, and update CRM records using natural language.

#### What Can It Do?

* **Search companies and people** with flexible filters
* **Read, create, and update** company and person records
* **Manage lists** by viewing entries or adding new records
* **Sync CRM data** with other tools in your workflows

#### Where to Use It

##### In Agents (Recommended)

Add Attio as a tool to any agent. The agent can then interact with your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Attio tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search companies in the fintech industry")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                 | Description                             |
| -------------------- | --------------------------------------- |
| **Search Companies** | Search companies with filtering options |
| **Read Company**     | Get details for a specific company      |
| **Create Company**   | Create a new company record             |
| **Update Company**   | Update fields on a company              |
| **Search People**    | Search people with flexible filters     |
| **Read Person**      | Get details for a specific person       |
| **Create Person**    | Add a new person to Attio               |
| **Update Person**    | Update fields on a person               |
| **List Lists**       | List all lists in your workspace        |
| **Read List**        | Read entries from a specific list       |
| **Add To List**      | Add a company or person to a list       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find a company:**

```text
Search for companies in the fintech industry headquartered in London
```

**Find prospects:**

```text
Find people with title "VP Sales" at SaaS companies in San Francisco
```

**Update a record:**

```text
Update DataCorp to set their industry to "AI/ML" and funding stage to "Series B"
```

**Add to a list:**

```text
Add NewDeal Inc to the Pipeline - Due Diligence list
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific filters like industry, location, or title                                                                                              |
| Action not completing            | Check that you've authenticated and have the necessary Attio permissions                                                                            |
| Unexpected results               | The agent may chain multiple tools (e.g., searching companies first, then finding people). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find the CEO of TechCorp" will search for the company first, then find people at that company. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Attio MCP server](https://www.gumloop.com/mcp/attio) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Basedash

*Create and manage Basedash charts, dashboards, and database insights.*

**Source:** https://docs.gumloop.com/nodes/mcp/basedash

Create and manage Basedash charts, dashboards, and database insights.

Basedash is the database management and visualization platform that makes it easy to create charts and dashboards from your data. The Basedash MCP server lets you create and manage charts, dashboards, and database insights using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Basedash. Authentication uses OAuth — just connect your Basedash account and start using it immediately.

#### What Can It Do?

* **Create charts** and visualizations from your data
* **Manage dashboards** and organize views
* **Access database insights** and query results

#### Where to Use It

##### In Agents (Recommended)

Add Basedash as a tool to any agent. The agent can then create visualizations and access your data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Basedash account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Basedash tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Basedash uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Basedash to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a chart:**

```text
Create a line chart showing signups per day for the last 30 days
```

**Manage dashboards:**

```text
List all dashboards and their charts
```

**Query data:**

```text
Show me the top 10 customers by revenue this quarter
```

#### Troubleshooting

| Issue               | Solution                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect      | Ensure you have an active Basedash account with database connections                                                |
| Chart not rendering | Check that the underlying data source is accessible                                                                 |
| Tool not available  | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Beehiiv

*Manage your newsletter with AI-powered publishing and subscriber automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/beehiiv

Manage your newsletter with AI-powered publishing and subscriber automation.

Beehiiv is a newsletter platform for creators and publishers. The Beehiiv MCP server lets you publish posts, manage subscribers, and organize your publication using natural language.

#### What Can It Do?

* **Publish and manage posts** automatically
* **Add and update subscribers** with tags and custom fields
* **Retrieve segments and tiers** for targeted campaigns
* **Sync newsletter data** with other tools for reporting

#### Where to Use It

##### In Agents (Recommended)

Add Beehiiv as a tool to any agent. The agent can then interact with your publication conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Beehiiv tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List the 10 most recent posts")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                               | Description                       |
| ---------------------------------- | --------------------------------- |
| **List Automations**               | List automations in a publication |
| **Create/List Custom Fields**      | Manage custom fields              |
| **Create Post**                    | Create a new post                 |
| **List Posts**                     | Retrieve posts from a publication |
| **Get Post**                       | Get a single post                 |
| **Delete Post**                    | Archive or delete a post          |
| **List Segments**                  | List segments for a publication   |
| **Get Segment**                    | Get segment details               |
| **List Segment Subscribers**       | List subscribers in a segment     |
| **Create Subscription**            | Add a new subscriber              |
| **List Subscriptions**             | List subscriptions                |
| **Get/Update/Delete Subscription** | Manage subscriptions              |
| **Add Subscription Tag**           | Tag a subscription                |
| **List/Create Tiers**              | Manage publication tiers          |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a post:**

```text
Create a draft post titled "Product Launch Recap" for my newsletter
```

**Add a subscriber:**

```text
Subscribe sarah@company.com to my newsletter with the Premium tier
```

**Find segment subscribers:**

```text
List all subscribers in the VIP Readers segment
```

**Tag a subscriber:**

```text
Add the "enterprise_customer" tag to cto@bigcorp.com
```

**List recent posts:**

```text
Show me the 10 most recent posts and their status
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific publication names or IDs                                                                                                          |
| Action not completing            | Check that you've authenticated with your Beehiiv API key                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a subscriber first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                            |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the subscription for [john@example.com](mailto:john@example.com) to Premium" will find the subscription first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Beehiiv MCP server](https://www.gumloop.com/mcp/beehiiv) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### BigQuery

*Query and explore your data warehouse with AI-powered SQL automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_bigquery

Query and explore your data warehouse with AI-powered SQL automation.

Google BigQuery is a serverless data warehouse for analytics at scale. The BigQuery MCP server lets you explore projects, inspect datasets, and run SQL using natural language.

#### What Can It Do?

* **Discover projects and datasets** you have access to
* **Inspect table metadata** including schema and row counts
* **Run SQL queries** and return structured results
* **Power data workflows** by chaining outputs to other tools

#### Where to Use It

##### In Agents (Recommended)

Add BigQuery as a tool to any agent. The agent can then query and explore your data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with BigQuery tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run this SQL query on my dataset")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

BigQuery supports two ways to connect your GCP credentials:

  - **Google OAuth (default)**: Sign in with your Google account. Quick to set up, but requires re-authentication when your GCP session-control window expires (typically every 1–24 hours, depending on your org's policy).

  - **Workload Identity Federation**: Keyless, token-based access. No daily reconnect, no stored secrets. Best for teams that need always-on BigQuery access without manual re-auth.

##### Setting up Workload Identity Federation (WIF)

WIF lets Gumloop mint short-lived access tokens by federating into your GCP project. There are no static keys or OAuth sessions to manage.

To set it up:

1. Create a workload identity pool and OIDC provider in your GCP project that trusts Gumloop's issuer (`https://api.gumloop.com`)
2. Create a target service account with the BigQuery permissions your team needs
3. Grant the pool permission to impersonate that service account
4. In Gumloop, go to your [Connectors page](https://www.gumloop.com/personal/connectors), click **Add Credential**, and select **BigQuery (Workload Identity)**
5. Enter three values: your **GCP Project Number**, the **Workload Identity Pool Resource Name** (this must be the full **provider** resource path, e.g. `projects/123456789012/locations/global/workloadIdentityPools/gumloop-pool/providers/gumloop-oidc`), and the **Target Service Account Email**

> **Tip:** Add the WIF credential at the **team** level so the whole team shares one keyless connection. Use a **personal** credential if you only need it for your own agents.

For the complete setup walkthrough (including exact `gcloud` commands), see the [BigQuery Workload Identity Federation guide](https://docs.gumloop.com/nodes/integrations/bigquery-workload-identity-federation).

##### FAQ

  
**Can I use OAuth and WIF at the same time?**

Yes. If you have both a standard BigQuery OAuth credential and a WIF credential, Gumloop will try your OAuth token first. If it's expired or missing, it will automatically fall back to your WIF credential. You don't need to choose one or the other.

  
**Do I need to change anything in my agents or workflows?**

No. WIF works transparently. Your agents and workflows continue to use BigQuery the same way. The only difference is how Gumloop authenticates behind the scenes.

  
**Why would I pick WIF over OAuth?**

If your GCP organization enforces short session-control windows (e.g., 1-hour reauth), OAuth credentials require frequent reconnection. WIF eliminates that. It's also the better choice for teams that prohibit static service-account key files.

#### Available Tools

| Tool                 | Description                           |
| -------------------- | ------------------------------------- |
| **List Project Ids** | List accessible Google Cloud projects |
| **List Dataset Ids** | List datasets in a project            |
| **List Table Ids**   | List tables in a dataset              |
| **Get Dataset Info** | Get dataset metadata                  |
| **Get Table Info**   | Get table schema and row count        |
| **Execute SQL**      | Run a SQL query and return results    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Discover projects:**

```text
List all Google Cloud projects I have access to
```

**Explore datasets:**

```text
List all datasets in my analytics project
```

**Run a query:**

```text
Run "SELECT * FROM sales WHERE region = 'West' LIMIT 100"
```

**Get table info:**

```text
Show me the schema and row count for the customers table
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Specify the project ID and dataset explicitly                                                                                              |
| Action not completing            | Check that you've authenticated and have BigQuery access                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., listing datasets first, then querying). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "What tables are in my analytics dataset?" will find the project and dataset first, then list tables. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [BigQuery MCP server](https://www.gumloop.com/mcp/gbigquery) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Bing Webmaster

*Manage your Bing Webmaster Tools with AI-powered SEO automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/bing_webmaster

Manage your Bing Webmaster Tools with AI-powered SEO automation.

Bing Webmaster Tools helps you monitor and optimize your site's presence in Bing search results. The Bing Webmaster MCP server lets you manage sites, submit URLs, pull search and crawl analytics, and monitor indexing using natural language.

#### What Can It Do?

* **Manage sites** — add, verify, and remove sites from your account
* **Submit URLs and content** — push URLs and page content to Bing for crawling and indexing
* **Analyze search traffic** — get query stats, page stats, rank and traffic trends
* **Research keywords** — get impression data and related keywords across Bing
* **Monitor indexing** — check URL index status, inbound links, and connected pages
* **Track crawl health** — view crawl stats, issues, and adjust crawl settings
* **Manage sitemaps** — list, submit, and remove sitemap feeds

#### Where to Use It

##### In Agents (Recommended)

Add Bing Webmaster as a tool to any agent. The agent can then manage your SEO and indexing conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Bing Webmaster tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get top search queries for my site")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Sites

| Tool            | Description                                     |
| --------------- | ----------------------------------------------- |
| **List Sites**  | List sites in your Bing Webmaster Tools account |
| **Add Site**    | Add a site to your account                      |
| **Verify Site** | Verify ownership of a site                      |
| **Remove Site** | Remove a site from your account                 |

##### URL Submission

| Tool                             | Description                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| **Submit URLs**                  | Submit one or more URLs to Bing for crawling and indexing        |
| **Submit Content**               | Submit a URL together with its page content to Bing for indexing |
| **Fetch URL**                    | Request that Bing fetch a specific URL                           |
| **Get URL Submission Quota**     | Get the remaining URL submission quota for a site                |
| **Get Content Submission Quota** | Get the remaining content submission quota for a site            |
| **List Fetched URLs**            | List URLs that have been fetched for a site                      |
| **Get Fetched URL Details**      | Get details for a single fetched URL                             |

##### Search Analytics & Keywords

| Tool                            | Description                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| **Get Query Stats**             | Get traffic statistics for a site's top search queries                    |
| **Get Page Stats**              | Get traffic statistics for a site's top pages                             |
| **Get Page Query Stats**        | Get the search queries driving traffic to a specific page                 |
| **Get Query Page Stats**        | Get the pages that rank for a specific search query                       |
| **Get Query Page Detail Stats** | Get detailed traffic statistics for a specific query and page combination |
| **Get Rank and Traffic Stats**  | Get overall rank and traffic statistics for a site over time              |
| **Get Keyword**                 | Get impression data for a keyword over a date range (Bing-wide)           |
| **Get Keyword Stats**           | Get historical impression statistics for a keyword (Bing-wide)            |
| **Get Related Keywords**        | Get keywords related to a query with impression data (Bing-wide)          |

##### URL Index, Traffic & Links

| Tool                              | Description                                                        |
| --------------------------------- | ------------------------------------------------------------------ |
| **Get URL Info**                  | Get index details for a single page                                |
| **Get URL Traffic Info**          | Get index traffic details for a single page                        |
| **Get Children URL Info**         | Get index details for the pages under a directory                  |
| **Get Children URL Traffic Info** | Get index traffic details for the pages under a directory          |
| **Get Link Counts**               | Get pages that have inbound links with their link counts           |
| **Get URL Links**                 | Get inbound links for a specific page                              |
| **List Connected Pages**          | List pages connected to the site (pages elsewhere that link to it) |
| **Add Connected Page**            | Register a page that links to the site as connected                |

##### Crawl & Feeds

| Tool                      | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| **Get Crawl Stats**       | Get crawl statistics for a site                              |
| **Get Crawl Issues**      | Get crawl issues detected for a site                         |
| **Get Crawl Settings**    | Get the crawl settings for a site                            |
| **Update Crawl Settings** | Update the crawl settings for a site                         |
| **List Feeds**            | List the sitemap feeds submitted for a site                  |
| **Get Feed Details**      | Get details for a sitemap feed, including its child sitemaps |
| **Submit Feed**           | Submit a sitemap feed for a site                             |
| **Remove Feed**           | Remove a sitemap feed from a site                            |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check search performance:**

```text
What are my top 10 search queries by clicks this month?
```

**Submit new content:**

```text
Submit these URLs for indexing: https://example.com/new-page, https://example.com/updated-post
```

**Monitor crawl health:**

```text
Are there any crawl issues on my site?
```

**Keyword research:**

```text
Get related keywords for "project management software" with impression data
```

**Check indexing status:**

```text
Is https://example.com/blog/new-post indexed by Bing?
```

**Manage sitemaps:**

```text
Submit my sitemap at https://example.com/sitemap.xml
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                     |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific site URLs when querying stats                                                                                                   |
| Action not completing            | Check that you've authenticated with Bing Webmaster Tools                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., listing sites first, then pulling stats). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                          |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Show me crawl issues and top queries for my site" will list your sites first, then pull the relevant data. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Bing Webmaster MCP server](https://www.gumloop.com/mcp/bing-webmaster) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Box

*Manage your cloud storage with AI-powered file and folder automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/box

Manage your cloud storage with AI-powered file and folder automation.

Box is a leading cloud content management and file sharing platform for businesses. The Box MCP server lets you search, manage, and access files and folders stored in your Box account using natural language.

#### What Can It Do?

* **Search files and folders** with advanced filtering by type, date, and content
* **Manage files** including upload, download, copy, move, and delete operations
* **Organize folders** by creating, listing, and managing folder structures
* **Share content** by creating shared links and adding collaborators
* **Manage users and groups** for enterprise collaboration

#### Where to Use It

##### In Agents (Recommended)

Add Box as a tool to any agent. The agent can then manage your cloud storage conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Box account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Box tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for PDF files in the Reports folder")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

Box uses OAuth 2.0 for authentication. When connecting your Box account, you'll be redirected to Box to authorize Gumloop to access your files and folders. The integration will automatically handle token refresh to maintain your connection.

#### Available Tools

##### Search

| Tool             | Description                                                             |
| ---------------- | ----------------------------------------------------------------------- |
| **Search Files** | Search for files, folders, and web links in Box with advanced filtering |

##### File Operations

| Tool            | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| **Get File**    | Get file metadata by ID, optionally download file content to workspace |
| **Upload File** | Upload a file from Gumloop workspace to Box                            |
| **Delete File** | Delete a file from Box                                                 |
| **Copy File**   | Copy a file to a destination folder                                    |
| **Move File**   | Move and optionally rename a file                                      |

##### Folder Operations

| Tool              | Description                        |
| ----------------- | ---------------------------------- |
| **List Files**    | List files and folders in a folder |
| **List Folders**  | List only folders in a folder      |
| **Get Folder**    | Get folder metadata by ID          |
| **Create Folder** | Create a new folder                |

##### User and Group Management

| Tool              | Description                      |
| ----------------- | -------------------------------- |
| **Search Users**  | List or search enterprise users  |
| **Search Groups** | List or search enterprise groups |

##### Sharing and Collaboration

| Tool                   | Description                                         |
| ---------------------- | --------------------------------------------------- |
| **Create Shared Link** | Create or update a shared link for a file or folder |
| **Add Collaborator**   | Add a collaborator to a file or folder              |
| **Update Tags**        | Add or remove tags on a file or folder              |

##### AI Tools

| Tool                      | Description                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **AI Ask**                | Ask a question about files or a Box Hub using Box AI                                   |
| **AI Extract**            | Extract metadata from files using a freeform prompt with Box AI                        |
| **AI Extract Structured** | Extract structured metadata from files using fields or a metadata template with Box AI |
| **AI Text Gen**           | Generate text based on file content using Box AI                                       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search for files:**

```text
Find all PDF files in my Box account that contain "quarterly report" in the name
```

**List folder contents:**

```text
Show me all files in the Marketing folder
```

**Upload a file:**

```text
Upload the sales_data.csv file to the Reports folder in Box
```

**Create a shared link:**

```text
Create a shared link for the Q4 presentation that expires in 7 days
```

**Move files:**

```text
Move all files from the Inbox folder to the Archive folder
```

**Add a collaborator:**

```text
Add john@company.com as an editor to the Project Alpha folder
```

#### Search Options

The search tool supports advanced filtering options:

* **Type**: Filter by `file`, `folder`, or `web_link`
* **Scope**: Search `user_content` (your files) or `enterprise_content` (requires admin)
* **File Extensions**: Filter by specific file types (e.g., `pdf`, `docx`, `xlsx`)
* **Ancestor Folders**: Limit search to specific folder IDs
* **Owner**: Filter by owner user IDs
* **Content Types**: Search within `name`, `description`, `file_content`, `comments`, or `tag`
* **Size Range**: Filter by file size in bytes
* **Date Ranges**: Filter by creation or modification date
* **Trash Content**: Include or exclude trashed items

#### Troubleshooting

| Issue                   | Solution                                                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding files | Use specific search terms and check folder permissions                                                                                 |
| Action not completing   | Check that you've authenticated with Box                                                                                               |
| Permission denied       | Ensure you have access to the file or folder                                                                                           |
| Upload failed           | Verify the file exists in your Gumloop workspace                                                                                       |
| Tool not available      | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                    |
| Unexpected results      | The agent may chain multiple tools (e.g., searching first, then downloading). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Download the latest sales report" will search for the file first, then download it. If results seem off, check the agent's step-by-step reasoning.

#### Working with Folder IDs

Many Box operations require folder IDs. Here are some tips:

* The root folder ID is always `0`
* Use "List Files" or "List Folders" to discover folder IDs
* Use "Search Files" to find specific files and their IDs
* Folder IDs are returned in the response when creating new folders

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Box MCP server](https://www.gumloop.com/mcp/box) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Brandfetch

*Look up brand assets, logos, colors, fonts, and company details for any company.*

**Source:** https://docs.gumloop.com/nodes/mcp/brandfetch

Look up brand assets, logos, colors, fonts, and company details for any company.

Brandfetch is a brand data platform that provides logos, colors, fonts, and company information for millions of brands. The Brandfetch MCP server lets you search for brands, retrieve detailed brand assets, and identify brands from payment transaction labels.

#### What Can It Do?

* **Search for brands by name** and get matching results with domains, icons, and brand IDs
* **Retrieve complete brand data** including logos (SVG, PNG), brand colors, fonts, company details, social links, industry classification, and financial identifiers — using a domain, brand ID, stock ticker, ISIN, or crypto symbol
* **Identify brands from transaction labels** by matching raw payment text (e.g., "STARBUCKS 1523 OMAHA NE") to brand data, useful for enriching financial records

#### Where to Use It

##### In Agents (Recommended)

Add Brandfetch as a tool to any agent. The agent can look up any brand's visual identity and company information conversationally.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Brandfetch account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Brandfetch tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get the logo and brand colors for Nike")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                                                                                                                                                                                                                                                                                                          | Credits |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Search Brands**      | Search for brands by name. Returns matching brands with their domain, icon, brand ID, and quality score.                                                                                                                                                                                                             | 5       |
| **Get Brand**          | Get complete brand data including logos, colors, fonts, company info, social links, industry, and financial identifiers. Accepts a domain (e.g., `nike.com`), brand ID, stock ticker (e.g., `NKE`), ISIN, or crypto symbol (e.g., `BTC`). You can optionally specify the identifier type to avoid naming collisions. | 30      |
| **Enrich Transaction** | Identify a brand from a raw payment transaction label (e.g., "STARBUCKS 1523 OMAHA NE"). Requires a country code. Returns the matched brand's full data including logos, colors, and company details.                                                                                                                | 30      |

##### What Brand Data Includes

The `get_brand` and `enrich_transaction` tools return rich brand data:

* **Logos** — Multiple formats (SVG, PNG) with light/dark theme variants
* **Colors** — Brand accent and primary colors with hex codes
* **Fonts** — Brand typography with font names and types (title, body)
* **Company info** — Employee count, founded year, industry classification, public/private status
* **Financial identifiers** — ISIN numbers and stock tickers for public companies
* **Location** — Headquarters city, country, and region
* **Social links** — Twitter, LinkedIn, and other social media URLs
* **Images** — Banner images and other brand imagery

#### Example Prompts

Use these with your agent or in the Agent Node:

**Look up a brand:**

```text
Get the logo, brand colors, and company details for Nike
```

**Search by name:**

```text
Search for brands matching "Spotify"
```

**Use a stock ticker:**

```text
Get the brand data for the company with ticker symbol AAPL
```

**Enrich a transaction:**

```text
Identify the brand from this transaction: "AMZN MKTP US*1A2B3C4D" in the US
```

**Get brand assets for design:**

```text
Get all logo variants and brand colors for stripe.com
```

#### Troubleshooting

| Issue                     | Solution                                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Brand not found           | Try searching by name first to find the correct domain or brand ID                                                                          |
| Identifier type collision | Use the `identifier_type` parameter to explicitly specify domain, ticker, isin, or crypto                                                   |
| No logo variants          | Not all brands have complete data. The `qualityScore` field indicates data completeness.                                                    |
| Authentication failed     | Verify your Brandfetch API key is connected and valid                                                                                       |
| Tool not available        | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                         |
| Unexpected results        | The agent may chain multiple tools (e.g., searching first, then fetching details). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the Nike logo" will search for Nike, find the right brand, then retrieve the full brand data with logo URLs. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Brandfetch MCP server](https://www.gumloop.com/mcp/brandfetch) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Cal.com

*Manage scheduling and bookings with AI-powered calendar automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/cal

Manage scheduling and bookings with AI-powered calendar automation.

Cal.com is an open-source scheduling platform for managing availability and bookings. The Cal MCP server lets you check availability, create bookings, and manage schedules using natural language.

#### What Can It Do?

* **Check availability** for event types over date ranges
* **Create and manage bookings** with timing and participants
* **Reschedule, confirm, or cancel** existing bookings
* **Retrieve schedules and event types** for automation

#### Where to Use It

##### In Agents (Recommended)

Add Cal.com as a tool to any agent. The agent can then interact with your calendar conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Cal.com tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get available time slots for next week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                                |
| ---------------------- | ------------------------------------------ |
| **Get Me**             | Get your Cal.com user profile              |
| **Get Event Types**    | List all event types                       |
| **Get Schedules**      | Get all schedules with working hours       |
| **Get Availability**   | Get available time slots for an event type |
| **Get Bookings**       | List bookings within a date range          |
| **Get Booking**        | Get a specific booking by ID               |
| **Create Booking**     | Create a new booking                       |
| **Reschedule Booking** | Move a booking to a new time               |
| **Confirm Booking**    | Confirm a pending booking                  |
| **Decline Booking**    | Decline a pending booking                  |
| **Cancel Booking**     | Cancel an existing booking                 |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check availability:**

```text
What time slots are available for a 30-minute meeting next week?
```

**Create a booking:**

```text
Book a meeting with john@example.com on Tuesday at 2pm
```

**Reschedule a meeting:**

```text
Move my meeting with Sarah to Thursday at 10am
```

**Get upcoming bookings:**

```text
Show me all my bookings for this week
```

**Cancel a booking:**

```text
Cancel my meeting tomorrow with the reason "scheduling conflict"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify the event type or date range clearly                                                                                                               |
| Action not completing            | Check that you've authenticated and the event type exists                                                                                                  |
| Unexpected results               | The agent may chain multiple tools (e.g., getting event types first, then checking availability). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Book a meeting" will find available slots first, then create the booking. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Cal.com MCP server](https://www.gumloop.com/mcp/cal) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Canva

*Design and manage Canva assets, designs, and brand content.*

**Source:** https://docs.gumloop.com/nodes/mcp/canva

Design and manage Canva assets, designs, and brand content.

Canva is the visual design platform for creating graphics, presentations, social media content, and more. The Canva MCP server lets you design and manage your assets and brand content using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Canva. Authentication uses OAuth — just connect your Canva account and start using it immediately.

#### What Can It Do?

* **Create and manage designs** across various formats
* **Access brand assets** like logos, colors, and fonts
* **Manage design content** and templates

#### Where to Use It

##### In Agents (Recommended)

Add Canva as a tool to any agent. The agent can then manage your design assets conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Canva account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Canva tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Canva uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Canva to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a design:**

```text
Create a new Instagram post design with our brand colors
```

**Manage assets:**

```text
Show me all my recent designs from this week
```

**Access brand kit:**

```text
What fonts and colors are in our brand kit?
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Canva account (Pro or Teams recommended)                                                  |
| Design not saving  | Check that you have edit permissions for the target folder                                                          |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Carta

*Manage your Carta cap table, equity, and stakeholders.*

**Source:** https://docs.gumloop.com/nodes/mcp/carta

Manage your Carta cap table, equity, and stakeholders.

Carta is the platform for managing equity, cap tables, and valuations. The Carta MCP server lets you manage your cap table, equity grants, and stakeholder information using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Carta. Authentication uses OAuth — just connect your Carta account and start using it immediately.

#### What Can It Do?

* **View cap table** information and ownership breakdowns
* **Manage equity** grants and vesting schedules
* **Access stakeholder** information and contacts

#### Where to Use It

##### In Agents (Recommended)

Add Carta as a tool to any agent. The agent can then access your equity data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Carta account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Carta tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Carta uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Carta to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**View cap table:**

```text
Show me the current ownership breakdown for my company
```

**Check equity:**

```text
What's the vesting schedule for the latest employee grants?
```

**Find stakeholders:**

```text
List all stakeholders with more than 1% ownership
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have admin or viewer access to your Carta company                                                        |
| Data not loading   | Check that your permissions include the requested data                                                              |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Chorus

*Access conversation intelligence and meeting insights with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/chorus

Access conversation intelligence and meeting insights with AI-powered automation.

Chorus is a conversation intelligence platform that records and analyzes sales calls. The Chorus MCP server lets you search meetings, review scorecards, and access conversation details using natural language.

#### What Can It Do?

* **Search recorded meetings** with filters for date, participants, and topics
* **Pull conversation details** for coaching and quality assurance
* **Review scorecards** by recipient, reviewer, or initiative
* **Discover playlists** for onboarding and training

#### Where to Use It

##### In Agents (Recommended)

Add Chorus as a tool to any agent. The agent can then search and analyze your conversation data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Chorus tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get meetings from last week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                  | Description                      |
| --------------------- | -------------------------------- |
| **Get Me**            | Get authenticated user details   |
| **Get Engagements**   | Search meetings with filtering   |
| **Delete Engagement** | Delete a specific engagement     |
| **Get Conversation**  | Fetch detailed conversation data |
| **Get Playlists**     | Fetch playlists with filtering   |
| **Get Scorecards**    | Fetch scorecards with filtering  |
| **Get Users**         | Fetch all users from Chorus      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find recent meetings:**

```text
Show me all meetings from last week with external participants
```

**Get conversation details:**

```text
Get the details for the meeting with Acme Corp including participants and duration
```

**Review scorecards:**

```text
Find scorecards for sarah@company.com submitted this month
```

**Discover playlists:**

```text
List training playlists owned by the sales team
```

**User directory:**

```text
Show me all users with their roles and team assignments
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific date ranges or participant names                                                                                                          |
| Action not completing            | Check that you've authenticated and have access to the recordings                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., searching engagements first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                    |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the details for the Acme meeting" will search for the engagement first, then fetch conversation details. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Chorus MCP server](https://www.gumloop.com/mcp/chorus) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Circleback

*Search and access your Circleback meeting notes and action items.*

**Source:** https://docs.gumloop.com/nodes/mcp/circleback

Search and access your Circleback meeting notes and action items.

Circleback is an AI meeting assistant that automatically records, transcribes, and summarizes meetings. The Circleback MCP server lets you search and access your meeting notes and action items using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Circleback. Authentication uses OAuth — just connect your Circleback account and start using it immediately.

#### What Can It Do?

* **Search meeting notes** by topic, date, or participant
* **Access action items** from your meetings
* **View meeting summaries** and key decisions

#### Where to Use It

##### In Agents (Recommended)

Add Circleback as a tool to any agent. The agent can then access your meeting history conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Circleback account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Circleback tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Circleback uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Circleback to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search notes:**

```text
Find meeting notes from last week about the product launch
```

**Get action items:**

```text
What are my outstanding action items from recent meetings?
```

**Review decisions:**

```text
What decisions were made in the board meeting on Monday?
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Circleback account                                                                        |
| No meetings found  | Check that Circleback has been joined to your meetings                                                              |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### ClickHouse

*Query ClickHouse Cloud and manage services, ClickPipes, and ClickStack observability with natural language.*

**Source:** https://docs.gumloop.com/nodes/mcp/clickhouse

Query ClickHouse Cloud and manage services, ClickPipes, and ClickStack observability with natural language.

ClickHouse Cloud is a serverless, columnar data warehouse for real-time analytics and observability. The ClickHouse MCP server lets you run SQL, manage services and backups, configure ClickPipes, track costs, and operate the ClickStack observability plane (dashboards, alerts, sources) using natural language.

#### What Can It Do?

* **Run SQL** against any ClickHouse Cloud service and return structured results
* **Manage services** by listing them, starting, or stopping on demand
* **Inspect backups** and backup schedules for each service
* **Manage ClickPipes** to monitor streaming ingestion jobs
* **Track organization costs** with daily billing and usage data
* **Operate ClickStack observability** with dashboards, alerts, and data sources

#### Where to Use It

##### In Agents (Recommended)

Add ClickHouse as a tool to any agent. The agent can then interact with your data and observability plane conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your ClickHouse Cloud API key

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with ClickHouse tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Query the events table for the last 24 hours")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

ClickHouse uses a **Key ID / Key Secret** API key pair plus a **database user and password** for SQL access.

1. In the ClickHouse Cloud console, go to **Organization Settings → API Keys → New API Key**
2. Assign a role that matches what you want the MCP to do (Developer for read-only, Admin for writes and lifecycle operations)
3. Copy the **Key ID** and **Key Secret** (the secret is shown once)
4. Get your **Database User** (defaults to `default`) and **Database Password** from **Service Settings** in the Cloud console

See [Managing API Keys](https://clickhouse.com/docs/cloud/manage/openapi) for full details.

#### Available Tools

| Tool                                 | Description                                                        |
| ------------------------------------ | ------------------------------------------------------------------ |
| **Execute Query**                    | Run a SQL query against a ClickHouse Cloud service                 |
| **List Organizations**               | List your Cloud organizations or fetch one by id                   |
| **List Services**                    | List services in an organization or fetch one by id                |
| **Update Service State**             | Start or stop a ClickHouse Cloud service                           |
| **List Service Backups**             | List backups for a service or fetch one by id                      |
| **Get Service Backup Configuration** | Get the backup schedule and retention for a service                |
| **List ClickPipes**                  | List ClickPipes on a service or fetch one by id                    |
| **Get Organization Cost**            | Retrieve daily billing and usage cost for an organization          |
| **List Dashboards**                  | List ClickStack dashboards on a service or fetch one by id         |
| **Create Dashboard**                 | Create a ClickStack dashboard                                      |
| **Update Dashboard**                 | Update a ClickStack dashboard                                      |
| **Delete Dashboard**                 | Delete a ClickStack dashboard                                      |
| **List Alerts**                      | List ClickStack alerts on a service or fetch one by id             |
| **Create Alert**                     | Create a ClickStack alert tied to a dashboard tile or saved search |
| **Update Alert**                     | Update a ClickStack alert                                          |
| **Delete Alert**                     | Delete a ClickStack alert                                          |
| **List Sources**                     | List ClickStack data sources configured on a service               |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Run a query:**

```text
Run "SELECT count() FROM events WHERE event_date = today()" on my production service
```

**List services:**

```text
Show me all ClickHouse services in my organization and their current state
```

**Start a service:**

```text
Start the "analytics-prod" service
```

**Check backups:**

```text
List the latest backups for the analytics-prod service and its backup retention policy
```

**Monitor ingestion:**

```text
List all ClickPipes on the analytics-prod service and flag any that are not running
```

**Track cost:**

```text
Show me the daily ClickHouse Cloud cost for my organization over the last 7 days
```

**Create an alert:**

```text
Create an alert on the "API Errors" dashboard tile that fires when errors exceed 100 per hour
```

#### Troubleshooting

| Issue                  | Solution                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failing | Verify the Key ID, Key Secret, and database credentials. The Key Secret is only shown once when created.            |
| Query returns no data  | Confirm you're targeting the right service and that the service is running. Use **List Services** first.            |
| Action not permitted   | Check that your API key role (Developer vs Admin) has the permissions the tool needs.                               |
| Tool not available     | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Start the analytics service and run a smoke-test query" will list services, start the right one, wait, and then run the query. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

### ClickUp

*Manage tasks, projects, and team collaboration with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/clickup

Manage tasks, projects, and team collaboration with AI-powered automation.

ClickUp is a project management platform that organizes tasks, projects, and collaboration in one place. The ClickUp MCP server lets you view, create, and update tasks, lists, and folders using natural language.

#### What Can It Do?

* **Retrieve workspaces, spaces, folders, lists, and tasks** without writing code
* **Create and update tasks** with assignees, due dates, and priorities
* **Add comments** to keep teammates informed
* **Manage project structure** by creating lists and folders

#### Where to Use It

##### In Agents (Recommended)

Add ClickUp as a tool to any agent. The agent can then interact with your projects conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with ClickUp tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get tasks from the Sprint 23 list")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                       | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| **Get Authenticated User** | Get current user details                                |
| **Get Workspaces**         | List all workspaces                                     |
| **Get Spaces**             | List spaces in a workspace                              |
| **Get Folders**            | List folders in a space                                 |
| **Get Lists**              | List lists in a folder or space                         |
| **Get Tasks**              | Retrieve tasks from a list with cursor-based pagination |
| **Get Task By Id**         | Get a single task                                       |
| **Create Task**            | Create a new task                                       |
| **Update Task**            | Update an existing task                                 |
| **Add Comment**            | Add a comment to a task                                 |
| **Create List**            | Create a list in a folder                               |
| **Create Folder**          | Create a folder in a space                              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Get tasks:**

```text
Show me all in-progress tasks from the Sprint 23 list
```

**Create a task:**

```text
Create a task "Review Q3 Budget" in the Finance Tasks list, due next Friday
```

**Update a task:**

```text
Mark the API Documentation task as complete
```

**Add a comment:**

```text
Add a comment to the Logo Redesign task: "Waiting on client approval"
```

**Explore structure:**

```text
List all folders in the Marketing space
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific list names or provide the workspace context                                                                                        |
| Action not completing            | Check that you've authenticated and have permissions for the workspace                                                                          |
| Unexpected results               | The agent may chain multiple tools (e.g., finding the list first, then getting tasks). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a task in the Marketing folder" will find the workspace, space, and folder first, then create the task. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [ClickUp MCP server](https://www.gumloop.com/mcp/clickup) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Cloudflare

*Manage your Cloudflare account, DNS, and Workers.*

**Source:** https://docs.gumloop.com/nodes/mcp/cloudflare

Manage your Cloudflare account, DNS, and Workers.

Cloudflare is a web infrastructure and security company providing CDN, DNS, DDoS protection, and serverless computing. The Cloudflare MCP server lets you manage your account, DNS records, and Workers using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Cloudflare. Authentication uses OAuth — just connect your Cloudflare account and start using it immediately.

#### What Can It Do?

* **Manage DNS records** across your domains
* **Configure Workers** and serverless functions
* **View account settings** and zone configurations
* **Monitor site performance** and security events

#### Where to Use It

##### In Agents (Recommended)

Add Cloudflare as a tool to any agent. The agent can then manage your infrastructure conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Cloudflare account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Cloudflare tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Cloudflare uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Cloudflare to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Manage DNS:**

```text
Add an A record for api.example.com pointing to 192.0.2.1
```

**Check Workers:**

```text
List all my deployed Cloudflare Workers
```

**View zones:**

```text
Show me the DNS records for my domain example.com
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have admin access to your Cloudflare account                                                             |
| Permission denied  | Check that the OAuth scope includes the resources you're trying to manage                                           |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Confluence

*Manage documentation and knowledge bases with AI-powered content automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/confluence

Manage documentation and knowledge bases with AI-powered content automation.

Confluence is Atlassian's collaboration platform for creating and organizing documentation. The Confluence MCP server lets you search pages, create content, and manage tasks using natural language.

#### What Can It Do?

* **Find pages and blog posts** with flexible filters
* **Create and update** pages and blog posts in specific spaces
* **List and manage tasks** including status updates
* **Upload, list, and manage attachments** on pages
* **Discover spaces** to target where to publish or search

#### Where to Use It

##### In Agents (Recommended)

Add Confluence as a tool to any agent. The agent can then interact with your documentation conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Confluence tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search pages in the Engineering space")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                  | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| **List Pages**        | Search pages with filtering options                           |
| **Get Page**          | Get a specific page by ID                                     |
| **Create Page**       | Create a new page in a space                                  |
| **Update Page**       | Update a page by ID                                           |
| **List Tasks**        | List tasks with filtering                                     |
| **Get Task**          | Get a specific task                                           |
| **Update Task**       | Update task status                                            |
| **List Blog Posts**   | Search blog posts                                             |
| **Get Blog Post**     | Get a specific blog post                                      |
| **Create Blog Post**  | Create a new blog post                                        |
| **Update Blog Post**  | Update a blog post                                            |
| **Get Spaces**        | List spaces with filtering                                    |
| **Get Database**      | Get a specific database                                       |
| **Upload Attachment** | Upload a file to a Confluence page as an attachment           |
| **List Attachments**  | List attachments with filtering options                       |
| **Get Attachment**    | Get attachment metadata by ID, optionally download to storage |
| **Delete Attachment** | Delete an attachment by ID                                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find pages:**

```text
Search for pages about "API documentation" in the Engineering space
```

**Create a page:**

```text
Create a new page titled "Q4 Planning" in the Product space
```

**Update a task:**

```text
Mark the task "Review architecture docs" as complete
```

**Discover spaces:**

```text
List all spaces I have access to
```

**Publish a blog post:**

```text
Create a blog post titled "Product Update - January" in the Company News space
```

**Upload an attachment:**

```text
Upload the file "report.pdf" to the Q4 Planning page
```

**List attachments:**

```text
Show me all attachments on page 12345
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific space names or search terms                                                                                                           |
| Action not completing            | Check that you've authenticated and have permissions for the space                                                                                 |
| Unexpected results               | The agent may chain multiple tools (e.g., finding the space first, then creating a page). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a page in the Marketing space" will find the space first, then create the page. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Confluence MCP server](https://www.gumloop.com/mcp/confluence) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Cursor

*Manage Cursor cloud agents to launch, monitor, and control AI coding agents on your repositories.*

**Source:** https://docs.gumloop.com/nodes/mcp/cursor

Manage Cursor cloud agents to launch, monitor, and control AI coding agents on your repositories.

Cursor is an AI-powered code editor. The Cursor MCP server lets you launch and manage cloud agents that work on your GitHub repositories using natural language.

#### What Can It Do?

* **Launch cloud agents** to work on GitHub repositories
* **Monitor agent status** and view conversation history
* **Send follow-up instructions** to running agents
* **Stop and delete agents** when done

#### Where to Use It

##### In Agents (Recommended)

Add Cursor as a tool to any agent. The agent can then interact with Cursor conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Cursor tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Launch an agent to fix the login bug")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                       | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| **List Agents**            | List all cloud agents for the authenticated user        |
| **Launch Agent**           | Launch a new cloud agent to work on a GitHub repository |
| **Get Agent**              | Get a cloud agent's status and results                  |
| **Get Agent Conversation** | Get a cloud agent's conversation history                |
| **Add Followup**           | Send a follow-up instruction to a running cloud agent   |
| **Stop Agent**             | Stop a running cloud agent                              |
| **Delete Agent**           | Permanently delete a cloud agent                        |
| **List Models**            | List available LLM models for cloud agents              |
| **List Repositories**      | List accessible GitHub repositories                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Launch an agent:**

```text
Launch a Cursor agent to refactor the auth module in my-repo
```

**Check status:**

```text
What's the status of my running Cursor agents?
```

**Send follow-up:**

```text
Tell my Cursor agent to also update the tests
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Cursor credentials and that you have the required permissions                                           |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Cursor MCP server](https://www.gumloop.com/mcp/cursor) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Custom MCP Servers

*Connect your own MCP servers to Gumloop for extended AI capabilities.*

**Source:** https://docs.gumloop.com/nodes/mcp/custom_mcp_servers

Connect your own MCP servers to Gumloop for extended AI capabilities.

Gumloop supports connecting to any [Model Context Protocol (MCP)](https://www.gumloop.com/blog/what-is-mcp-model-context-protocol-a-simple-guide) server. This lets you extend your agents and workflows with specialized tools, internal services, or any MCP-compatible API.

> **Info:** Gumloop already has **50+ pre-built MCP servers** for popular services like GitHub, Slack, Notion, HubSpot, and more. These work out of the box with agents and workflows. [Browse available integrations](https://docs.gumloop.com/nodes/mcp) before setting up a custom server.

#### Adding a Custom MCP Server

Setting up a custom MCP server takes just a few steps.

1. **Go to Connectors**

   Navigate to **Settings > [Connectors](https://www.gumloop.com/personal/connectors?provider=mcp%20server)** and search for "MCP Server" in the available integrations.

       *[Screenshot: Apps Available modal showing MCP Server option]*

2. **Enter the Server URL**

   Click **Add credential** and enter your MCP server's URL. The URL must use HTTPS.

       *[Screenshot: MCP Server URL entry dialog]*

3. **Configure Authentication**

   Fill in the server details:

       | Field                      | Description                                              | Required              |
       | -------------------------- | -------------------------------------------------------- | --------------------- |
       | **Label**                  | A unique name for this server (e.g., `slack-mcp-server`) | Yes                   |
       | **Access Token / API Key** | OAuth token or API key for authentication                | If required by server |
       | **Additional Header**      | Custom header in `Header-Name: value` format             | Optional              |

       *[Screenshot: MCP Server credential configuration]*

4. **Connect**

   Click **Connect** to save your credential. The server is now available to use in your agents and workflows.

> **Tip:** **Team vs Personal credentials**: Credentials can be stored at the personal level (only you can use them) or team level (shared with your team). Choose the appropriate scope when setting up. [Learn more about credentials here](https://docs.gumloop.com/core-concepts/credentials#personal-vs-team-connectors)

#### Requirements

Custom MCP servers must meet these requirements:

| Requirement       | Details                                           |
| ----------------- | ------------------------------------------------- |
| **Protocol**      | HTTPS only (HTTP not supported)                   |
| **Accessibility** | Must be publicly accessible on the internet       |
| **Transport**     | Streamable HTTP or Server-Sent Events (SSE)       |
| **Local servers** | Not supported (no STDIO or localhost connections) |

> **Warning:** **Local MCP servers won't work.** Your server must be deployed to a publicly accessible URL. Services like [Cloudflare Tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) or [ngrok](https://ngrok.com/) can expose local servers if needed.

##### Authentication Options

Gumloop supports multiple authentication methods:

* **Bearer tokens**: Standard OAuth/API key authentication. When you provide an **Access Token / API Key**, Gumloop sends it as an `Authorization: Bearer <token>` header with every request to your MCP server.
* **Custom headers**: For services requiring specific header formats. The **Additional Header** field accepts a single header in `Header-Name: value` format (e.g., `X-API-Key: my-secret-key`). This is useful for MCP servers that expect authentication in a non-standard header.
* **OAuth discovery**: Automatic OAuth flow discovery (RFC 8414) for compatible servers

#### Where You Can Use Custom MCP Servers

Once configured, your custom MCP servers can be used in two places: **Agents** and the **Ask AI node**.

##### Using MCP Servers with Agents

Agents offer the most flexible way to use custom MCP servers. The AI can discover all available tools and use them naturally in conversation.

1. **Open Agent Configuration**

   Go to your agent's settings and click **Add tools**.

2. **Select MCP Server**

   Choose **MCP Server** as the tool type and search for your configured server under the **Custom** tab.

       *[Screenshot: Selecting a custom MCP server in agent configuration]*

3. **Use Your Agent**

   Your agent now has access to all tools from the MCP server. It will automatically discover and use them based on conversation context.

**Why agents are more flexible:**

* **Conversational context**: The agent maintains conversation history and can use tools across multiple turns
* **Automatic tool selection**: The agent chooses the right tool based on your request
* **Multi-server support**: Connect multiple MCP servers and let the agent orchestrate between them
* **No workflow required**: Use immediately in chat, Slack, or embedded interfaces

##### Using MCP Servers with Ask AI Node

For deterministic workflows, you can connect MCP servers to the Ask AI node.

1. **Add Ask AI Node**

   Drag an Ask AI node onto your canvas.

2. **Enable MCP**

   Click **Show more options**, then toggle **Connect MCP Server?** to ON.

3. **Select Server(s)**

   Choose your configured MCP server(s) from the dropdown. You can select multiple servers.

       *[Screenshot: Enabling MCP in Ask AI Node]*

**When to use Ask AI node with MCP:**

* Building repeatable, production workflows
* Need specific tool calls as part of a larger automation
* Want to combine MCP tools with other Gumloop nodes

##### Comparison: Agents vs Ask AI Node

| Capability           | Agents                             | Ask AI Node                     |
| -------------------- | ---------------------------------- | ------------------------------- |
| **Flexibility**      | High: conversational, multi-turn   | Medium: single prompt execution |
| **Tool discovery**   | Automatic                          | Automatic                       |
| **Multi-server**     | Yes                                | Yes                             |
| **Best for**         | Interactive use, complex reasoning | Workflows, batch processing     |
| **Approval prompts** | Not available                      | Not available                   |

#### Model-Specific Differences

Custom MCP servers work across all models in Gumloop, but how they run depends on the provider:

| Model             | Provider  | How MCP Tools Run                               |
| ----------------- | --------- | ----------------------------------------------- |
| GPT-5.5           | OpenAI    | Native MCP                                      |
| GPT-5.4           | OpenAI    | Native MCP                                      |
| Claude 4.6 Sonnet | Anthropic | Native MCP                                      |
| Claude 4.5 Sonnet | Anthropic | Native MCP                                      |
| Gemini            | Google    | Backend connector (Gumloop executes tool calls) |
| Groq models       | Groq      | Backend connector (Gumloop executes tool calls) |

* **Native MCP**: The provider (OpenAI/Anthropic) connects directly to your MCP server and executes tools.
* **Backend connector (Gumloop executes tool calls)**: Gumloop connects to your server and presents tools as regular function calls; when invoked, Gumloop executes them and returns results to the model.

##### Header Handling by Model

| Execution Method                    | Bearer Token                            | Additional Header |
| ----------------------------------- | --------------------------------------- | ----------------- |
| **OpenAI (Native MCP)**             | Sent as `Authorization: Bearer <token>` | Sent as-is        |
| **Anthropic (Native MCP)**          | Sent as authorization token             | Not forwarded     |
| **Gemini/Groq (backend connector)** | Sent as `Authorization: Bearer <token>` | Sent as-is        |

> **Warning:** Anthropic models do not forward custom headers. If your MCP server relies on a custom header (e.g., `X-API-Key`), use the **Access Token / API Key** field with a Bearer token instead, or choose OpenAI, Gemini, or Groq.

#### Security Considerations

  
**Data sharing**

Information in your prompts may be sent to your MCP server. Be mindful of sensitive data and review your server's data handling policies.

  
**Direct tool access**

All tools exposed by your MCP server are immediately available to the AI. There are no approval prompts before tool execution. Use appropriate authorization scopes to limit access.

  
**Multi-server implications**

When using multiple MCP servers, consider that data retrieved from one server could be passed to another. Design your prompts accordingly.

#### Troubleshooting

| Issue                 | Solution                                                 |
| --------------------- | -------------------------------------------------------- |
| Cannot connect        | Verify URL is HTTPS and publicly accessible              |
| Authentication failed | Check token validity and expiration                      |
| Tools not appearing   | Ensure the server implements MCP tool discovery          |
| AI ignoring tools     | Be more explicit in your prompt about which tools to use |
| Timeout errors        | Server may be slow or unreachable. Check server status.  |

> **Tip:** **Test with discovery first.** Ask your agent or Ask AI node to "list available tools" to verify the connection is working before building complex workflows.

#### Further Reading

* [What is MCP? A Simple Guide](https://www.gumloop.com/blog/what-is-mcp-model-context-protocol-a-simple-guide)
* [Introducing MCP Workflows in Gumloop](https://www.gumloop.com/blog/introducing-mcp-workflows)
* [MCP Nodes Best Practices](https://www.gumloop.com/university/video/mcp-nodes-best-practices)

### Databricks

*Manage data engineering and ML operations with AI-powered workspace automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/databricks

Manage data engineering and ML operations with AI-powered workspace automation.

Databricks is a unified analytics platform for data engineering, data science, and machine learning. The Databricks MCP server lets you manage clusters, run jobs, execute SQL, and query ML endpoints using natural language.

#### What Can It Do?

* **Manage clusters** by listing, starting, and terminating on demand
* **Orchestrate jobs** by triggering runs and fetching outputs
* **Run SQL** on warehouses and return structured data
* **Query ML endpoints** and vector indexes for AI workflows

#### Where to Use It

##### In Agents (Recommended)

Add Databricks as a tool to any agent. The agent can then interact with your workspace conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Databricks tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all active clusters")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                             | Description                         |
| -------------------------------- | ----------------------------------- |
| **Get Me**                       | Get authenticated user information  |
| **List Clusters**                | List all pinned and active clusters |
| **Start Cluster**                | Start a terminated cluster          |
| **Terminate Cluster**            | Terminate a running cluster         |
| **List Jobs**                    | List jobs with pagination           |
| **Run Job**                      | Trigger a new job run               |
| **Manage Job Run**               | Cancel or delete a job run          |
| **Get Job Run Output**           | Get output from a job run           |
| **Execute SQL**                  | Run SQL on a warehouse              |
| **List Warehouses**              | List all SQL warehouses             |
| **Query Serving Endpoint**       | Query a model serving endpoint      |
| **List Serving Endpoints**       | List all serving endpoints          |
| **Query Vector Index**           | Query a vector index                |
| **List Vector Search Endpoints** | List vector search endpoints        |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Manage clusters:**

```text
List all my clusters and their current status
```

**Start compute:**

```text
Start the cluster named "analytics-cluster"
```

**Run a job:**

```text
Trigger the daily ETL job and return the run ID
```

**Execute SQL:**

```text
Run "SELECT * FROM sales WHERE region = 'West'" on the main warehouse
```

**Query ML endpoint:**

```text
Query the fraud-detection endpoint with this transaction data
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific cluster or job names                                                                                                         |
| Action not completing            | Check that you've authenticated and have the necessary workspace permissions                                                              |
| Unexpected results               | The agent may chain multiple tools (e.g., listing jobs first, then running one). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                       |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Run the ETL job" will find the job first, then trigger it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Databricks MCP server](https://www.gumloop.com/mcp/databricks) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Datadog

*Monitor your infrastructure with AI-powered observability and incident management.*

**Source:** https://docs.gumloop.com/nodes/mcp/datadog

Monitor your infrastructure with AI-powered observability and incident management.

Datadog is a comprehensive monitoring and analytics platform for cloud-scale infrastructure, applications, and logs. The Datadog MCP server lets you monitor infrastructure, query metrics, search logs, manage incidents, and control monitors using natural language.

#### What Can It Do?

* **Monitor management** including create, update, mute, and delete monitors
* **Query metrics** with timeseries data and aggregation
* **Search logs** with advanced filtering and time ranges
* **Incident management** for tracking and coordinating responses
* **Dashboard operations** including create, update, and view dashboards
* **Host management** including muting and listing infrastructure hosts
* **SLO tracking** for service level objectives
* **Synthetic monitoring** for proactive testing

#### Where to Use It

##### In Agents (Recommended)

Add Datadog as a tool to any agent. The agent can then monitor your infrastructure conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Enter your Datadog API credentials

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Datadog tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all monitors in alert state")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

Datadog uses API key authentication. When connecting your Datadog account, you'll need to provide:

* **API Key**: Your Datadog API key for authentication
* **Application Key**: Your Datadog Application key for authorization
* **Site**: Your Datadog site (e.g., `datadoghq.com`, `datadoghq.eu`, `us3.datadoghq.com`)

To create API and Application keys:

1. Log in to your Datadog account
2. Navigate to **Organization Settings** → **API Keys** to create an API key
3. Navigate to **Organization Settings** → **Application Keys** to create an Application key
4. Copy both keys and your site URL for use in Gumloop

> **Warning:** Keep your API and Application keys secure. These keys provide access to your Datadog account and should not be shared publicly.

#### Available Tools

##### Monitor Tools

| Tool               | Description                                                                 |
| ------------------ | --------------------------------------------------------------------------- |
| **List Monitors**  | List all monitors with filtering by name, tags, or status                   |
| **Get Monitor**    | Get detailed information about a specific monitor by ID                     |
| **Create Monitor** | Create a new monitor with specified type, query, and alerting configuration |
| **Update Monitor** | Update an existing monitor's configuration                                  |
| **Delete Monitor** | Delete a monitor by ID                                                      |
| **Mute Monitor**   | Mute a monitor to suppress notifications during maintenance                 |
| **Unmute Monitor** | Unmute a previously muted monitor to resume notifications                   |

##### Metrics Tools

| Tool              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| **Query Metrics** | Query timeseries metrics data with aggregation and grouping     |
| **List Metrics**  | List available metrics in your account to discover metric names |

##### Logs Tools

| Tool            | Description                                                           |
| --------------- | --------------------------------------------------------------------- |
| **Search Logs** | Search and retrieve log events with filtering by query and time range |

##### Incident Tools

| Tool                       | Description                                                              |
| -------------------------- | ------------------------------------------------------------------------ |
| **List Incidents**         | List incidents with optional filtering by state or query                 |
| **Get Incident**           | Get detailed information about a specific incident                       |
| **Create Incident**        | Create a new incident for tracking and coordination                      |
| **Update Incident**        | Update an existing incident's attributes like title, status, or severity |
| **Delete Incident**        | Delete an incident by ID                                                 |
| **List Incident Timeline** | Get the timeline of events for a specific incident                       |

##### Dashboard Tools

| Tool                 | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| **List Dashboards**  | List all dashboards with optional filtering                  |
| **Get Dashboard**    | Get detailed dashboard configuration by ID including widgets |
| **Create Dashboard** | Create a new dashboard with specified layout and widgets     |
| **Update Dashboard** | Update an existing dashboard's layout and widgets            |
| **Delete Dashboard** | Delete a dashboard from Datadog                              |

##### Host Tools

| Tool                | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| **List Hosts**      | List infrastructure hosts with filtering by name, tags, or criteria |
| **Get Host Totals** | Get the total count of active and up hosts                          |
| **Mute Host**       | Mute a host to suppress alerts during maintenance                   |
| **Unmute Host**     | Unmute a previously muted host to resume alerts                     |

##### Event Tools

| Tool             | Description                                              |
| ---------------- | -------------------------------------------------------- |
| **List Events**  | Query events by time range and optional filters          |
| **Get Event**    | Get detailed information about a specific event by ID    |
| **Create Event** | Post a new event to Datadog for tracking and correlation |

##### Downtime Tools

| Tool                | Description                                                 |
| ------------------- | ----------------------------------------------------------- |
| **List Downtimes**  | List all scheduled downtimes for maintenance windows        |
| **Get Downtime**    | Get detailed information about a specific downtime          |
| **Create Downtime** | Schedule a new downtime to mute monitors during maintenance |
| **Cancel Downtime** | Cancel a scheduled downtime to resume monitoring            |

##### SLO Tools

| Tool                | Description                                               |
| ------------------- | --------------------------------------------------------- |
| **List SLOs**       | List all Service Level Objectives with optional filtering |
| **Get SLO**         | Get detailed information about a specific SLO             |
| **Create SLO**      | Create a new Service Level Objective                      |
| **Update SLO**      | Update an existing SLO's configuration                    |
| **Delete SLO**      | Delete an SLO by ID                                       |
| **Get SLO History** | Get historical SLI data for an SLO                        |

##### Synthetics Tools

| Tool                  | Description                                              |
| --------------------- | -------------------------------------------------------- |
| **List Synthetics**   | List all synthetic monitoring tests                      |
| **Get Synthetic**     | Get detailed information about a specific synthetic test |
| **Create Synthetic**  | Create a new synthetic monitoring test                   |
| **Update Synthetic**  | Update an existing synthetic test                        |
| **Delete Synthetic**  | Delete synthetic tests by IDs                            |
| **Trigger Synthetic** | Manually trigger synthetic tests                         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List alerting monitors:**

```text
Show me all monitors that are currently in alert state
```

**Query metrics:**

```text
Get the average CPU usage across all hosts for the last hour
```

**Search logs:**

```text
Search for error logs in production from the last 30 minutes
```

**Create an incident:**

```text
Create a critical incident for the database outage affecting the checkout service
```

**Mute a monitor:**

```text
Mute the high CPU monitor for 2 hours during the deployment
```

**Check SLO status:**

```text
Show me the current status of all SLOs for the payment service
```

#### Troubleshooting

| Issue                 | Solution                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your API Key and Application Key are correct                                                                                               |
| Wrong site            | Make sure you're using the correct Datadog site (e.g., datadoghq.com vs datadoghq.eu)                                                             |
| Permission denied     | Ensure your Application Key has the necessary permissions                                                                                         |
| Monitor not found     | Check that the monitor ID is correct                                                                                                              |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |
| Unexpected results    | The agent may chain multiple tools (e.g., listing monitors first, then getting details). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Mute all monitors for the web service during maintenance" will list the monitors first, then mute each one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Datadog MCP server](https://www.gumloop.com/mcp/datadog) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Devin

*Manage AI coding sessions and engineering automation with natural language.*

**Source:** https://docs.gumloop.com/nodes/mcp/devin

Manage AI coding sessions and engineering automation with natural language.

Devin is an AI software engineer that can code, debug, and deploy. The Devin MCP server lets you create sessions, send messages, and manage organization resources using natural language.

#### What Can It Do?

* **Start coding sessions** with task prompts and track progress
* **Send messages** to ongoing sessions and fetch details
* **Organize work** with tags on sessions
* **Manage resources** like secrets and knowledge items

#### Where to Use It

##### In Agents (Recommended)

Add Devin as a tool to any agent. The agent can then interact with your coding sessions conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Devin tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a new coding session")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                            |
| ------------------------ | -------------------------------------- |
| **List Sessions**        | List all coding sessions               |
| **Create Session**       | Start a new session with a task prompt |
| **Get Session**          | Get details for a session              |
| **Send Session Message** | Send a message to a session            |
| **Terminate Session**    | End an active session                  |
| **Update Session Tags**  | Organize sessions with tags            |
| **List Secrets**         | List organization secrets              |
| **Create Secret**        | Create a new encrypted secret          |
| **Delete Secret**        | Remove a secret                        |
| **List Knowledge**       | List knowledge items and folders       |
| **Create Knowledge**     | Create a knowledge item                |
| **Update Knowledge**     | Update a knowledge item                |
| **Delete Knowledge**     | Remove a knowledge item                |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Start a coding session:**

```text
Create a new session to implement the user authentication feature
```

**Check session status:**

```text
Get the status of my active sessions
```

**Send instructions:**

```text
Tell the session to focus on writing unit tests first
```

**Organize work:**

```text
Tag the authentication session with "sprint-23" and "backend"
```

**Manage knowledge:**

```text
Create a knowledge item with our API documentation
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific session names or IDs                                                                                                                   |
| Action not completing            | Check that you've authenticated with your Devin API key                                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., listing sessions first, then sending a message). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Send a message to the auth session" will find the session first, then send the message. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Devin MCP server](https://www.gumloop.com/mcp/devin) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Dropbox

*Manage files, folders, sharing, and file requests with AI-powered cloud storage automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/dropbox

Manage files, folders, sharing, and file requests with AI-powered cloud storage automation.

Dropbox is a cloud storage and file sharing platform used by millions of individuals and teams. The Dropbox MCP server lets you manage files and folders, create shared links, collaborate with team members, and collect files via file requests using natural language.

#### What Can It Do?

* **Browse and manage files** — list, search, create, move, copy, and delete files and folders
* **Upload and download files** — transfer files between Gumloop and your Dropbox
* **Share content** — create shared links and share folders with specific users
* **Collect files** — create and manage file requests to gather files from anyone
* **Check account info** — view storage usage and account details

#### Where to Use It

##### In Agents (Recommended)

Add Dropbox as a tool to any agent. The agent can then manage your cloud storage conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Dropbox account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Dropbox tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Upload a file to Dropbox")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Files & Folders

| Tool                      | Description                                     |
| ------------------------- | ----------------------------------------------- |
| **List Folder**           | List files and folders in a Dropbox directory   |
| **Get File Metadata**     | Get metadata for a file or folder               |
| **Search Files**          | Search for files and folders by name or content |
| **Create Folder**         | Create a new folder                             |
| **Delete File Or Folder** | Delete a file or folder                         |
| **Move File Or Folder**   | Move or rename a file or folder                 |
| **Copy File Or Folder**   | Copy a file or folder                           |
| **Upload File**           | Upload a file from Gumloop storage to Dropbox   |
| **Download File**         | Download a file from Dropbox to Gumloop storage |
| **Get Temporary Link**    | Get a temporary direct download link for a file |
| **List Revisions**        | List the revision history of a file             |

##### Sharing

| Tool                    | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **Create Shared Link**  | Create a shared link for a file or folder                 |
| **List Shared Links**   | List shared links for a file, folder, or all shared links |
| **Share Folder**        | Share a folder with other users                           |
| **Add Folder Member**   | Add a member to a shared folder by email                  |
| **List Folder Members** | List members of a shared folder                           |
| **Share File**          | Share a file with specific users by email                 |

##### File Requests

| Tool                     | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Create File Request**  | Create a file request to collect files from anyone |
| **List File Requests**   | List all file requests owned by the current user   |
| **Get File Request**     | Get details of a specific file request             |
| **Delete File Requests** | Delete one or more file requests                   |

##### Account

| Tool                    | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| **Get Current Account** | Get information about the authenticated Dropbox user |
| **Get Space Usage**     | Get current storage space usage and allocation       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Browse files:**

```text
List all files in my /Projects/2026 folder
```

**Share a file:**

```text
Create a shared link for the file at /Reports/Q1-2026.pdf
```

**Upload content:**

```text
Upload the generated report to /Reports/ in my Dropbox
```

**Collect files from others:**

```text
Create a file request for client deliverables and send me the link
```

**Check storage:**

```text
How much Dropbox storage am I using?
```

#### Troubleshooting

| Issue               | Solution                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| File not found      | Use `List Folder` or `Search Files` to confirm the exact path                                                       |
| Upload failing      | Ensure the destination folder exists before uploading                                                               |
| Sharing not working | Verify the email addresses are correct and the users have Dropbox accounts                                          |
| Tool not available  | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Dropbox paths are case-sensitive and must start with `/`. Use `Search Files` to find the exact path of a file before moving or sharing it.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Dropbox MCP server](https://www.gumloop.com/mcp/dropbox) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Exa

*Search the web intelligently with AI-powered research and content extraction.*

**Source:** https://docs.gumloop.com/nodes/mcp/exa

Search the web intelligently with AI-powered research and content extraction.

Exa is an AI-powered search engine that finds high-quality web content with neural search. The Exa MCP server lets you search, extract content, find similar pages, and get citation-backed answers using natural language.

#### What Can It Do?

* **Search the web** with neural and keyword search for relevant results
* **Extract content** including full text, summaries, and metadata from URLs
* **Find similar pages** to broaden research coverage
* **Get answers** with citations from reliable web sources

#### Where to Use It

##### In Agents (Recommended)

Add Exa as a tool to any agent. The agent can then search and research conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Exa tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for AI startup funding news")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                                   |
| ------------------------ | --------------------------------------------- |
| **Search**               | Search the web with neural and keyword search |
| **Get Contents**         | Extract full page contents from URLs          |
| **Find Similar**         | Find similar pages to a source URL            |
| **Answer**               | Get LLM answers with citations                |
| **Create Research Task** | Start an async research task                  |
| **Get Research Task**    | Get status and results of research            |

#### Credit Costs

| Tool                     | Credits Per Use |
| ------------------------ | --------------- |
| Get Contents             | 3 per item      |
| Find Similar             | 5 per item      |
| Answer                   | 10 credits      |
| Create/Get Research Task | 5 credits each  |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search the web:**

```text
Find the top 10 articles about AI regulation in 2024
```

**Extract content:**

```text
Get the full content from this article URL
```

**Find related sources:**

```text
Find similar pages to this TechCrunch article
```

**Get an answer:**

```text
What are the latest developments in quantum computing? Include citations.
```

**Start research:**

```text
Research the competitive landscape for AI writing tools
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use more specific search terms or date filters                                                                                              |
| Action not completing            | Check that you've authenticated and have sufficient Exa credits                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then getting contents). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                         |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Research AI trends and summarize" will search, get contents, and synthesize. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Exa MCP server](https://www.gumloop.com/mcp/exa) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Excel

*Manage Microsoft 365 Excel workbooks with AI-powered spreadsheet automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/excel

Manage Microsoft 365 Excel workbooks with AI-powered spreadsheet automation.

Microsoft Excel in Microsoft 365 is a powerful spreadsheet application for data management and analysis. The Excel MCP server lets you read, write, and manage workbooks in OneDrive and SharePoint using natural language.

#### What Can It Do?

* **Create and search workbooks** in OneDrive and SharePoint, including SharePoint document libraries
* **Manage worksheets** by adding, listing, and updating
* **Read and write data** to cells, rows, and tables
* **Download workbooks** for sharing and backup

#### Where to Use It

##### In Agents (Recommended)

Add Excel as a tool to any agent. The agent can then interact with your spreadsheets conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Excel tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Read data from the Sales worksheet")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                             |
| ------------------------ | --------------------------------------- |
| **Create Workbook**      | Create a new Excel workbook             |
| **Search Workbooks**     | Search workbooks in OneDrive/SharePoint |
| **Download Workbook**    | Get a download URL                      |
| **List Worksheets**      | List all worksheets                     |
| **Add Worksheet**        | Add a new worksheet                     |
| **Read Worksheet**       | Read data from a range                  |
| **Update Cells**         | Update cell values                      |
| **Search Data**          | Get data from a range                   |
| **Add Row**              | Append a row                            |
| **Find Row**             | Find a row by value                     |
| **Find Or Create Row**   | Find or create a row                    |
| **Update Row**           | Update a row                            |
| **Delete Worksheet Row** | Delete a row                            |
| **List Tables**          | List all tables                         |
| **Get Table**            | Get table metadata                      |
| **Add Table**            | Create a table                          |
| **List Table Rows**      | List rows in a table                    |
| **Add Table Row**        | Add a row to a table                    |
| **Add Table Column**     | Add a column                            |
| **Update Table Column**  | Update column data                      |
| **Delete Table**         | Delete a table                          |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a workbook:**

```text
Create a new workbook called "Q4 Budget" in my OneDrive
```

**Read data:**

```text
Read the data from cells A1 to D50 in the Sales worksheet
```

**Update cells:**

```text
Update cell C10 to "Closed Won" in the Deals workbook
```

**Add data:**

```text
Add a new row with "Acme Inc", 25000, and "Pending" to the Sales table
```

**Find a record:**

```text
Find the row where Company Name is "TechCorp"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific workbook names or provide the OneDrive/SharePoint path                                                                              |
| Action not completing            | Check that you've authenticated with Microsoft 365 and have access to the file                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., listing worksheets first, then reading data). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                              |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the Acme row in the Sales table" will find the row first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Excel MCP server](https://www.gumloop.com/mcp/excel) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Expensify

*Automate expense management with AI-powered report exports and bulk expense creation.*

**Source:** https://docs.gumloop.com/nodes/mcp/expensify

Automate expense management with AI-powered report exports and bulk expense creation.

Expensify is an expense management platform for tracking receipts, reports, and corporate card transactions. The Expensify MCP server lets you export reports, reconcile transactions, and create expenses using natural language.

#### What Can It Do?

* **Export expense reports** in CSV, Excel, PDF, or XML formats
* **Reconcile card transactions** by exporting transaction data
* **Create expenses in bulk** with categories, tags, and custom fields
* **Get download links** for exported data

#### Where to Use It

##### In Agents (Recommended)

Add Expensify as a tool to any agent. The agent can then interact with your expense data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Expensify tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Export reports from last month")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

To use Expensify, generate API credentials:

1. Create an account at [expensify.com](https://www.expensify.com/)
2. Go to [Integrations](https://www.expensify.com/tools/integrations/)
3. Copy your partnerUserID and partnerUserSecret
4. Add them to your [Connectors page](https://www.gumloop.com/personal/connectors)

#### Available Tools

| Tool                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **Get Reports**           | Export reports in CSV, Excel, PDF, or XML        |
| **Get Card Transactions** | Export card transactions for reconciliation      |
| **Create Expenses**       | Create expenses in bulk with categories and tags |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Export reports:**

```text
Export expense reports from January 1 to January 31 as a CSV
```

**Get card transactions:**

```text
Export corporate card transactions for last month
```

**Create expenses:**

```text
Create an expense for $45.50 at Uber on January 15 in the Travel category
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Specify clear date ranges and report states                                                                                          |
| Action not completing            | Check that you've authenticated with your Expensify API credentials                                                                  |
| Unexpected results               | The agent may chain multiple tools (e.g., exporting first, then filtering). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                  |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get my Q4 expense summary" will export reports and calculate totals. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Expensify MCP server](https://www.gumloop.com/mcp/expensify) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Extend

*Process documents with AI-powered extraction, classification, and parsing.*

**Source:** https://docs.gumloop.com/nodes/mcp/extend

Process documents with AI-powered extraction, classification, and parsing.

Extend is a document processing platform that turns PDFs, images, and scans into structured data. The Extend MCP server lets you run processors, parse files, and manage document workflows using natural language.

#### What Can It Do?

* **Run document workflows** with files or text inputs
* **Parse files** into clean, chunked content for processing
* **Extract and classify** data from documents with processors
* **Monitor runs** with filtering and lifecycle management

#### Where to Use It

##### In Agents (Recommended)

Add Extend as a tool to any agent. The agent can then process documents conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Extend tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Parse this PDF to markdown")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                            | Description                               |
| ------------------------------- | ----------------------------------------- |
| **List Workflow Runs**          | List runs with filtering by status        |
| **Get Workflow Run**            | Get details of a specific run             |
| **Run Workflow**                | Run a workflow with files or text         |
| **Run Processor**               | Run extraction or classification          |
| **List Processor Runs**         | List processor runs with filtering        |
| **Get Processor Run**           | Get details of a processor run            |
| **Cancel/Delete Processor Run** | Manage processor runs                     |
| **Parse File**                  | Parse files to markdown or spatial format |
| **Get Parser Run**              | Get parser run status and results         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Run a workflow:**

```text
Run the invoice processing workflow on this PDF
```

**Parse a document:**

```text
Parse this PDF to markdown and return the text chunks
```

**Extract data:**

```text
Run the contract extraction processor on this document
```

**Check run status:**

```text
Get the status of my latest workflow runs
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific workflow or processor names                                                                                            |
| Action not completing            | Check that you've authenticated and the file URL is accessible                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., parsing first, then extracting). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Extract invoice details from this PDF" will parse the file first, then run the extractor. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Extend MCP server](https://www.gumloop.com/mcp/extend) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Fal

*Run AI models for image, video, audio, speech, and 3D generation using fal.ai.*

**Source:** https://docs.gumloop.com/nodes/mcp/fal

Run AI models for image, video, audio, speech, and 3D generation using fal.ai.

Fal is an AI inference platform that hosts hundreds of generative AI models. The Fal MCP server lets you search for models, inspect their schemas, submit inference jobs, and retrieve results across image, video, audio, speech, and 3D generation categories.

#### What Can It Do?

* **Search AI models** by category (text-to-image, text-to-video, text-to-audio, text-to-speech, text-to-3D)
* **Inspect model schemas** to understand accepted input parameters before running a model
* **Submit inference requests** that queue on fal.ai and return a request ID for polling
* **Poll for results** including generated images, videos, audio files, and 3D assets with download URLs

#### Where to Use It

##### In Agents (Recommended)

Add Fal as a tool to any agent. The agent can search for the right model, check its schema, submit a generation request, and poll for results conversationally.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Fal account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Fal tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Generate an image using fal-ai/flux/dev")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                 | Description                                                                                                                                                           | Credits            |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **Search Models**    | Search available fal.ai models by category (text-to-image, text-to-video, text-to-audio, text-to-speech, text-to-3D). Supports free-text filtering and result limits. | 3                  |
| **Get Model Schema** | Get the OpenAPI input/output schema for a specific model by endpoint ID. Use this before `run_model` to see what parameters the model accepts.                        | 3                  |
| **Run Model**        | Submit an inference request to fal.ai's queue. Returns a `request_id` for polling with `get_result`.                                                                  | Varies by category |
| **Get Result**       | Poll the status and result of a submitted request. Returns status (`IN_QUEUE`, `IN_PROGRESS`, `COMPLETED`) and the output when done.                                  | 3                  |

##### Run Model Credit Costs

The `run_model` tool cost depends on the model category:

| Category       | Credits |
| -------------- | ------- |
| Text to Image  | 24      |
| Text to Audio  | 12      |
| Text to Speech | 60      |
| Text to 3D     | 96      |
| Text to Video  | 2,400   |

#### How It Works — Asynchronous Generation

Fal does **not** return results instantly. It uses an asynchronous queue system, which means generation happens in the background and you retrieve the output separately once it's ready.

Here's the full flow:

1. **Search** for a model using `search_models` with a category like `text_to_image`
2. **Inspect** the model's accepted parameters using `get_model_schema`
3. **Submit** a request using `run_model` — this queues the job on fal.ai and immediately returns a `request_id`. The generation has started, but the result is **not available yet**.
4. **Wait and poll** using `get_result` with the `request_id`. The status will progress through `IN_QUEUE` → `IN_PROGRESS` → `COMPLETED`. You need to keep polling until the status reaches `COMPLETED`.
5. **Retrieve the output** — once `COMPLETED`, the response contains download URLs for the generated content (images, videos, audio, 3D assets).

> **Warning:** Generation is not real-time. After submitting a request, there is a waiting period while fal.ai processes the job. Image generation typically takes a few seconds, but video and 3D generation can take several minutes. The agent will submit the job, then poll periodically until the result is ready.

> **Info:** The download URLs returned in the result are temporary. Make sure to download or use the generated files promptly after retrieval.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a product hero image:**

```text
Generate a clean product photo of a pair of white sneakers on a marble surface with soft studio lighting
```

**Generate a social media video:**

```text
Create a 5-second animated video of a logo reveal with a dark background for my brand intro
```

**Create a voiceover for a demo:**

```text
Generate a professional voiceover saying "Welcome to our platform. Let's walk through the key features."
```

**Generate background music:**

```text
Create a 30-second upbeat lo-fi background track for a product walkthrough video
```

**Create a 3D asset:**

```text
Generate a 3D model of a minimalist desk lamp for use in a product render
```

**Batch-generate marketing visuals:**

```text
Generate 4 variations of a banner image showing a futuristic cityscape for our landing page A/B test
```

#### Troubleshooting

| Issue                  | Solution                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Model not found        | Verify the endpoint ID is correct by searching models first                                                         |
| Request still in queue | Video and 3D generation can take minutes. Keep polling with `get_result` until status is `COMPLETED`                |
| Model type mismatch    | Ensure the `model_type` parameter matches the model's actual category                                               |
| Authentication failed  | Verify your Fal API key is connected and valid                                                                      |
| Tool not available     | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Agents handle the full async workflow automatically. When you ask "Generate a product photo of sneakers," the agent will search for an image model, check its schema, submit the request, wait for it to finish processing, and then return the download URL — all without you needing to manage the polling yourself. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Fal MCP server](https://www.gumloop.com/mcp/fal) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Fathom

*Access meeting recordings, transcripts, and AI-generated summaries with automated notetaking.*

**Source:** https://docs.gumloop.com/nodes/mcp/fathom

Access meeting recordings, transcripts, and AI-generated summaries with automated notetaking.

Fathom is an AI-powered meeting assistant that records, transcribes, and summarizes meetings. The Fathom MCP server lets you list meetings, retrieve transcripts, and access AI-generated summaries using natural language.

#### What Can It Do?

* **List and filter meetings** by date, recorder, team, or invitee domains
* **Retrieve AI-generated summaries** for meeting recordings
* **Access full transcripts** with speaker attribution and timestamps
* **Manage teams and members** across your organization

#### Where to Use It

##### In Agents (Recommended)

Add Fathom as a tool to any agent. The agent can then interact with your meeting data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Fathom tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List meetings from last week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                         | Description                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| **List Meetings**            | List meetings with filtering by date, recorder, team, and invitee domains |
| **Get Recording Summary**    | Get the AI-generated summary for a meeting recording                      |
| **Get Recording Transcript** | Get the full transcript with speaker attribution and timestamps           |
| **List Teams**               | List all teams in the organization                                        |
| **List Team Members**        | List team members, optionally filtered by team name                       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find recent meetings:**

```text
List all meetings from last week recorded by the sales team
```

**Get a summary:**

```text
Get the AI summary from yesterday's product planning meeting
```

**Get a transcript:**

```text
Get the full transcript from the Q4 review meeting
```

**List teams:**

```text
Show me all teams in the organization
```

**Find team members:**

```text
List all members of the engineering team
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific date ranges or meeting titles                                                                                                          |
| Action not completing            | Check that you've authenticated with Fathom                                                                                                         |
| Unexpected results               | The agent may chain multiple tools (e.g., listing meetings first, then getting summaries). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Summarize last week's meetings" will list meetings, get summaries, and synthesize. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Fathom MCP server](https://www.gumloop.com/mcp/fathom) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Fellow

*Access meeting recordings, notes, and transcripts with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/fellow

Access meeting recordings, notes, and transcripts with AI-powered automation.

Fellow is a meeting productivity platform for notes, recordings, and action items. The Fellow MCP server lets you search recordings, retrieve transcripts, and access meeting notes using natural language.

#### What Can It Do?

* **List and search recordings** with date and keyword filters
* **Retrieve transcripts** for meeting analysis
* **Access meeting notes** with attendee information
* **Get workspace details** for governance and routing

#### Where to Use It

##### In Agents (Recommended)

Add Fellow as a tool to any agent. The agent can then interact with your meeting data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Fellow tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List recordings from last week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                | Description                              |
| ------------------- | ---------------------------------------- |
| **Get Me**          | Get user and workspace details           |
| **List Recordings** | List recordings with filtering           |
| **Get Recording**   | Get a specific recording with transcript |
| **List Notes**      | List meeting notes with filtering        |
| **Get Note**        | Get a specific note with content         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find recordings:**

```text
List all recordings from last week that mention "product launch"
```

**Get a transcript:**

```text
Get the transcript from the Q4 planning meeting
```

**Review notes:**

```text
Show me the notes from my meetings with the engineering team
```

**Workspace info:**

```text
Get my account and workspace details
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific date ranges or meeting titles                                                                                                              |
| Action not completing            | Check that you've authenticated with Fellow                                                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., listing recordings first, then getting transcripts). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                     |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Summarize last week's meetings" will list recordings, get transcripts, and synthesize. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Fellow MCP server](https://www.gumloop.com/mcp/fellow) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Findymail

*Find and verify professional emails with AI-powered lead discovery and enrichment.*

**Source:** https://docs.gumloop.com/nodes/mcp/findymail

Find and verify professional emails with AI-powered lead discovery and enrichment.

Findymail is an email finding and verification platform for B2B prospecting. The Findymail MCP server lets you find emails, verify addresses, enrich companies, discover employees, and search for leads using natural language.

#### What Can It Do?

* **Find emails** by name and domain, domain only, or LinkedIn URL
* **Verify email addresses** to check deliverability
* **Enrich companies** with firmographic data like size, industry, and domain
* **Find employees** at target companies by job title
* **Search leads** using AI-powered IntelliMatch with natural language queries
* **Find lookalike companies** similar to a seed company
* **Manage contact lists** to organize your prospects

#### Where to Use It

##### In Agents (Recommended)

Add Findymail as a tool to any agent. The agent can then find and verify emails conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Findymail tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Find the email for the CEO of gumloop.com")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                                                   |
| --------------------------- | ----------------------------------------------------------------------------- |
| **Find Email**              | Find a person's email address by name+domain, domain only, or LinkedIn URL    |
| **Verify Email**            | Verify if an email address is valid and deliverable                           |
| **Find Phone**              | Find a person's phone number from their LinkedIn profile URL                  |
| **Enrich Company**          | Get company details like size, industry, and domain from a company identifier |
| **Find Employees**          | Find employees at a company by website and job titles                         |
| **Reverse Email Lookup**    | Look up a person's profile and company info from their email address          |
| **List Contact Lists**      | List all saved contact lists                                                  |
| **Create Contact List**     | Create a new contact list                                                     |
| **Get Contacts**            | Get contacts saved in a specific list or all contacts                         |
| **Search Leads**            | Search for leads using AI-powered IntelliMatch with natural language queries  |
| **Get Lead Search Status**  | Check the status of an IntelliMatch lead search by its hash                   |
| **Get Lead Search Results** | Get paginated results from a completed IntelliMatch lead search               |
| **Search Lookalike**        | Find companies similar to a given company                                     |

#### Setting Up Credentials

Findymail uses API key authentication. You'll need to provide your Findymail API key to connect.

**To get your API key:**

1. Log in to your [Findymail Dashboard](https://app.findymail.com)
2. Navigate to your account settings or API section
3. Copy your API key

**To connect in Gumloop:**

1. Go to your [Connectors page](https://www.gumloop.com/personal/connectors)
2. Find Findymail and click **Connect**
3. Paste your API key when prompted

> **Info:** Your API key is stored securely and used to authenticate all Findymail API requests on your behalf. Each API call consumes credits from your Findymail account based on the action performed.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find an email:**

```text
Find the email address for Satya Nadella at Microsoft
```

**Verify an email:**

```text
Is john@company.com a valid email address?
```

**Enrich a company:**

```text
Get company details for gumloop.com
```

**Find employees:**

```text
Find the CEO and CTO at stripe.com
```

**Search for leads:**

```text
Find SaaS companies in San Francisco with 50-200 employees
```

**Find similar companies:**

```text
Find companies similar to stripe.com in the same country
```

**Reverse lookup:**

```text
Who is the person behind sarah@acme.com? Include their full profile.
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Provide specific names, domains, or LinkedIn URLs for accurate results                                                                                     |
| Action not completing            | Check that you've connected your Findymail API key and have sufficient credits                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a company first, then searching for employees). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                        |
| Lead search taking long          | IntelliMatch searches are asynchronous. Use **Get Lead Search Status** to poll progress, then **Get Lead Search Results** once complete.                   |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find the email for the VP of Sales at Acme Corp" will enrich the company first, then find the employee. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Findymail MCP server](https://www.gumloop.com/mcp/findymail) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Firecrawl

*Search, scrape, and map websites using Firecrawl's web data API.*

**Source:** https://docs.gumloop.com/nodes/mcp/firecrawl

Search, scrape, and map websites using Firecrawl's web data API.

Firecrawl is a web scraping API that turns websites into clean, structured data. The Firecrawl MCP server lets you search, scrape, crawl, and extract data from websites using natural language.

#### What Can It Do?

* **Search the web** with optional scraping and source filtering
* **Scrape single URLs** for content in markdown, HTML, or other formats
* **Map websites** to get all URLs ordered by relevance
* **Crawl entire sites** and extract content from multiple pages
* **Deep extract** data by autonomously navigating and exploring links
* **Interact with pages** using natural language prompts or browser code
* **Manage interactive browser sessions** for persistent browser automation

#### Where to Use It

##### In Agents (Recommended)

Add Firecrawl as a tool to any agent. The agent can then scrape and extract web data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Firecrawl tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Scrape this URL and get the content")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                         | Description                                                                                                                                          | Credits    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **Search**                   | Search the web and optionally scrape full page content. Returns results organized by source type (web, images, news).                                | 8 per item |
| **Scrape**                   | Scrape a single URL and extract content in various formats. Supports persistent profiles to reuse browser state across sessions.                     | 8          |
| **Map**                      | Get all URLs from a website. Returns a list of URLs ordered by relevance.                                                                            | 1          |
| **Crawl**                    | Crawl a website and extract content from multiple pages.                                                                                             | 40         |
| **Get Crawl Status**         | Get the status and results of a crawl job.                                                                                                           | 8 per item |
| **Batch Scrape**             | Scrape multiple URLs at once.                                                                                                                        | 40         |
| **Get Batch Scrape Status**  | Get the status and results of a batch scrape job.                                                                                                    | 8 per item |
| **Deep Extract**             | Autonomously navigate and extract data from websites based on a prompt. Unlike regular extract, this explores links and pages to find relevant data. | 120        |
| **Get Deep Extract Status**  | Get the status and results of a deep extract job.                                                                                                    | 3          |
| **Interact**                 | Interact with a previously scraped page using a natural language prompt or browser code.                                                             | 14         |
| **Stop Interact**            | Stop an interactive browser session to release resources.                                                                                            | 3          |
| **Create Interact Session**  | Start a standalone interactive browser session. Supports persistent profiles scoped per user.                                                        | 4          |
| **Execute Interact Session** | Run Playwright or agent-browser code in a standalone interact session.                                                                               | 4          |
| **Delete Interact Session**  | Stop a standalone interact session to release browser resources.                                                                                     | 3          |
| **List Interact Sessions**   | List standalone interact sessions, optionally filtered by status.                                                                                    | 3          |

> **Info:** The Gumloop-managed Firecrawl key supports searching, scraping, mapping, crawling, and extraction tools. Interactive browser tools — **Interact**, **Stop Interact**, **Create Interact Session**, **Execute Interact Session**, **Delete Interact Session**, and **List Interact Sessions** — require your own Firecrawl API key. Connect it in your [Connectors page](https://www.gumloop.com/personal/connectors).

#### Example Prompts

Use these with your agent or in the Agent Node:

**Scrape a page:**

```text
Scrape this URL and get the main content as markdown
```

**Search the web:**

```text
Search for "AI startup funding" and get the top 10 results
```

**Map a website:**

```text
Get all URLs from example.com
```

**Crawl a site:**

```text
Crawl example.com/blog with depth 2 and get all article content
```

**Deep extract:**

```text
Extract pricing information from this SaaS website, exploring all relevant pages
```

**Batch scrape:**

```text
Scrape these 5 URLs and get the main content from each
```

**Interactive browser session:**

```text
Create a browser session, navigate to example.com, and click the login button
```

#### Troubleshooting

| Issue                             | Solution                                                                                                                                        |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data  | Ensure the URL is publicly accessible                                                                                                           |
| Interactive tool requires API key | Interactive browser tools require your own Firecrawl API key. Connect it in your [Connectors page](https://www.gumloop.com/personal/connectors) |
| Action not completing             | Check that you've authenticated and have sufficient Firecrawl credits                                                                           |
| Unexpected results                | The agent may chain multiple tools (e.g., mapping first, then scraping). Review the agent's reasoning to understand its approach.               |
| Tool not available                | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get all blog posts from this site" will map the URLs first, then scrape each one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Firecrawl MCP server](https://www.gumloop.com/mcp/firecrawl) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Foreplay

*Research ads and competitor strategies with AI-powered creative intelligence.*

**Source:** https://docs.gumloop.com/nodes/mcp/foreplay

Research ads and competitor strategies with AI-powered creative intelligence.

Foreplay is an ad research platform with access to 100M+ live and historical ads. The Foreplay MCP server lets you search brands, discover ads, and pull analytics using natural language.

#### What Can It Do?

* **Search brands** by name or domain for detailed profiles
* **Discover ads** with filters for platform, format, niche, and date
* **Retrieve brand ads** with advanced filtering options
* **Pull analytics** including ad distribution and creative velocity

#### Where to Use It

##### In Agents (Recommended)

Add Foreplay as a tool to any agent. The agent can then research ads and competitors conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Foreplay tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for Nike ads on Facebook")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                         | Description                      |
| ---------------------------- | -------------------------------- |
| **Search Brands**            | Search brands by name or domain  |
| **Search And Filter Ads**    | Search ads with multiple filters |
| **Get Ads By Brand Or Page** | Get ads for a specific brand     |
| **Get Brand Analytics**      | Get ad distribution and velocity |
| **Get Ad Details**           | Get comprehensive ad details     |

#### Credit Costs

| Tool                     | Credits Per Use |
| ------------------------ | --------------- |
| Search Brands            | 3 per item      |
| Search And Filter Ads    | 3 per item      |
| Get Ads By Brand Or Page | 3 per item      |
| Get Brand Analytics      | 5 per item      |
| Get Ad Details           | 5 per item      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find a brand:**

```text
Search for Nike and get their brand profile
```

**Discover ads:**

```text
Find video ads about fitness on Facebook from the last 30 days
```

**Get brand ads:**

```text
Show me all of Glossier's Instagram ads from Q4
```

**Analyze a competitor:**

```text
Get analytics for Allbirds including their ad distribution by platform
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                      |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific brand names or domains                                                                                                           |
| Action not completing            | Check that you've authenticated and have sufficient Foreplay credits                                                                          |
| Unexpected results               | The agent may chain multiple tools (e.g., searching brands first, then getting ads). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                           |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Analyze Nike's ad strategy" will search the brand, get ads, and pull analytics. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Foreplay MCP server](https://www.gumloop.com/mcp/foreplay) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Freshdesk

*Manage support tickets, contacts, and knowledge base with AI-powered helpdesk automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/freshdesk

Manage support tickets, contacts, and knowledge base with AI-powered helpdesk automation.

Freshdesk is a cloud-based customer support platform for managing tickets, contacts, and self-service content. The Freshdesk MCP server lets you triage tickets, manage contacts and companies, work with the knowledge base, and orchestrate community forums using natural language.

#### What Can It Do?

* **Read, create, and triage tickets** with full lifecycle management
* **Manage contacts and companies** with search, merge, and bulk operations
* **Work with the knowledge base** to create and update solution articles
* **Orchestrate community forums** with topics and comments
* **Track time entries** on tickets
* **Handle attachments** with download to Gumloop storage

#### Where to Use It

##### In Agents (Recommended)

Add Freshdesk as a tool to any agent. The agent can then manage your helpdesk conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Freshdesk tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List open tickets assigned to me")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Tickets

| Tool               | Description                                                                      |
| ------------------ | -------------------------------------------------------------------------------- |
| **List Tickets**   | List tickets with filters, automatic pagination, and optional embedded relations |
| **Get Ticket**     | Get a single ticket by ID, optionally embedding related data                     |
| **Create Ticket**  | Create a new ticket                                                              |
| **Update Ticket**  | Update fields on an existing ticket                                              |
| **Delete Ticket**  | Soft-delete a ticket                                                             |
| **Search Tickets** | Search tickets using the Freshdesk filter DSL                                    |
| **Merge Tickets**  | Merge one or more secondary tickets into a primary ticket                        |
| **Forward Ticket** | Forward a ticket as a new outbound email                                         |
| **Restore Ticket** | Restore a previously soft-deleted ticket                                         |

##### Conversations

| Tool                    | Description                                  |
| ----------------------- | -------------------------------------------- |
| **List Conversations**  | List replies and notes on a ticket           |
| **Reply to Ticket**     | Post a public reply to a ticket              |
| **Add Note**            | Add a note (private by default) to a ticket  |
| **Update Conversation** | Update an existing conversation (notes only) |
| **Delete Conversation** | Delete a conversation (reply or note)        |

##### Watchers

| Tool                    | Description                                    |
| ----------------------- | ---------------------------------------------- |
| **List Watchers**       | List agents watching a ticket                  |
| **Add Watcher**         | Add an agent as a watcher on a ticket          |
| **Remove Self Watcher** | Remove the API caller from a ticket's watchers |

##### Attachments

| Tool                        | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| **List Ticket Attachments** | List attachments on a ticket by walking its conversations    |
| **Get Attachment**          | Download a ticket attachment and store it in Gumloop storage |

##### Contacts

| Tool                    | Description                                     |
| ----------------------- | ----------------------------------------------- |
| **List Contacts**       | List contacts with optional filters             |
| **Get Contact**         | Get a contact by ID                             |
| **Search Contacts**     | Search contacts using the Freshdesk filter DSL  |
| **Create Contact**      | Create a contact                                |
| **Update Contact**      | Update fields on a contact                      |
| **Delete Contact**      | Soft-delete a contact                           |
| **Hard Delete Contact** | Permanently delete a contact                    |
| **Merge Contacts**      | Merge secondary contacts into a primary contact |
| **Restore Contact**     | Restore a soft-deleted contact                  |

##### Companies

| Tool                 | Description                                     |
| -------------------- | ----------------------------------------------- |
| **List Companies**   | List companies with optional filters            |
| **Get Company**      | Get a company by ID                             |
| **Search Companies** | Search companies using the Freshdesk filter DSL |
| **Create Company**   | Create a company                                |
| **Update Company**   | Update fields on a company                      |
| **Delete Company**   | Delete a company                                |

##### Directory

| Tool                          | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| **List Agents**               | List agents with optional filters                       |
| **Get Agent**                 | Get an agent by ID                                      |
| **Get Current Agent**         | Get the agent associated with the authenticated API key |
| **List Groups**               | List agent groups                                       |
| **Get Group**                 | Get an agent group by ID                                |
| **List Skills**               | List agent skills                                       |
| **List Roles**                | List agent roles                                        |
| **List Products**             | List products                                           |
| **List Business Hours**       | List business hours configurations                      |
| **List SLA Policies**         | List SLA policies                                       |
| **List Ticket Fields**        | List ticket fields for schema discovery                 |
| **List Contact Fields**       | List contact fields for schema discovery                |
| **List Company Fields**       | List company fields for schema discovery                |
| **List CSAT Surveys**         | List customer satisfaction surveys                      |
| **List Satisfaction Ratings** | List customer satisfaction ratings across all surveys   |

##### Time Entries

| Tool                  | Description                             |
| --------------------- | --------------------------------------- |
| **List Time Entries** | List time entries with filters          |
| **Create Time Entry** | Create a time entry on a ticket         |
| **Update Time Entry** | Update a time entry                     |
| **Delete Time Entry** | Delete a time entry                     |
| **Toggle Timer**      | Start or stop the timer on a time entry |

##### Knowledge Base

| Tool                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| **List Solution Categories**     | List solution categories in the knowledge base |
| **Get Solution Category**        | Get a solution category by ID                  |
| **List Solution Folders**        | List folders inside a solution category        |
| **Get Solution Folder**          | Get a solution folder by ID                    |
| **List Solution Articles**       | List articles inside a solution folder         |
| **Get Solution Article**         | Get a solution article by ID                   |
| **Search Solutions**             | Full-text search across solution articles      |
| **Create Solution Article**      | Create a solution article                      |
| **Update Solution Article**      | Update a solution article                      |
| **Delete Solution Article**      | Delete a solution article                      |
| **List Canned Responses**        | List canned responses visible to the agent     |
| **Get Canned Response**          | Get a canned response by ID                    |
| **List Canned Response Folders** | List canned response folders                   |
| **Get Canned Response Folder**   | Get a canned response folder by ID             |

##### Forums

| Tool                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **List Forum Categories** | List forum categories                            |
| **Get Forum Category**    | Get a forum category by ID                       |
| **List Forums**           | List forums under a category                     |
| **Get Forum**             | Get a forum by ID                                |
| **List Forum Topics**     | List topics within a forum                       |
| **Get Forum Topic**       | Get a forum topic by ID                          |
| **Create Forum Topic**    | Create a new topic in a forum                    |
| **Update Forum Topic**    | Update a forum topic                             |
| **Delete Forum Topic**    | Delete a forum topic                             |
| **Follow Forum Topic**    | Subscribe a user to updates on a forum topic     |
| **Unfollow Forum Topic**  | Unsubscribe a user from updates on a forum topic |
| **List Topic Comments**   | List comments on a forum topic                   |
| **Create Forum Comment**  | Post a comment to a forum topic                  |
| **Update Forum Comment**  | Update a forum comment                           |
| **Delete Forum Comment**  | Delete a forum comment                           |

##### Threads (Pro+)

| Tool                      | Description                               |
| ------------------------- | ----------------------------------------- |
| **Get Thread**            | Get a collaboration thread by ID          |
| **Create Thread**         | Create a collaboration thread on a ticket |
| **Update Thread**         | Update a collaboration thread             |
| **Delete Thread**         | Delete a collaboration thread             |
| **Get Thread Message**    | Get a collaboration thread message by ID  |
| **Create Thread Message** | Post a message to a collaboration thread  |
| **Update Thread Message** | Update a collaboration thread message     |
| **Delete Thread Message** | Delete a collaboration thread message     |

##### Custom Objects (Enterprise)

| Tool                            | Description                            |
| ------------------------------- | -------------------------------------- |
| **List Custom Object Records**  | List records of a custom object schema |
| **Get Custom Object Record**    | Get a custom object record by ID       |
| **Create Custom Object Record** | Create a custom object record          |
| **Update Custom Object Record** | Update a custom object record          |
| **Delete Custom Object Record** | Delete a custom object record          |

##### Other

| Tool                            | Description                                    |
| ------------------------------- | ---------------------------------------------- |
| **Get Outbound Message Status** | Get the delivery status of an outbound message |
| **Get Job Status**              | Poll the status of an async Freshdesk job      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List open tickets:**

```text
Show me all open tickets assigned to the support team
```

**Triage a ticket:**

```text
Update ticket #1234 to high priority and assign it to the billing group
```

**Search for a contact:**

```text
Find the contact with email jane@acme.com
```

**Reply to a ticket:**

```text
Reply to ticket #5678 saying we've escalated the issue to engineering
```

**Search the knowledge base:**

```text
Search for articles about password reset
```

**Merge duplicate tickets:**

```text
Merge tickets #1001 and #1002 into ticket #1000
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific ticket IDs or exact email addresses                                                                                    |
| Action not completing            | Check that you've authenticated with Freshdesk                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Reply to the latest ticket from Acme" will search for the ticket first, then post the reply. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Freshdesk MCP server](https://www.gumloop.com/mcp/freshdesk) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Freshsales

*Manage your CRM with AI-powered sales automation for contacts, accounts, deals, and more.*

**Source:** https://docs.gumloop.com/nodes/mcp/freshsales

Manage your CRM with AI-powered sales automation for contacts, accounts, deals, and more.

Freshsales is a CRM platform built for sales teams to manage contacts, accounts, deals, and the full sales pipeline. The Freshsales MCP server lets you manage records, track activities, handle CPQ products and documents, and work with custom modules using natural language.

#### What Can It Do?

* **Manage contacts, accounts, and deals** with full CRUD, upsert, and bulk operations
* **Track sales activities** including tasks, appointments, calls, and notes
* **Handle CPQ products and documents** with pricing and deal associations
* **Work with marketing lists** for segmentation and outreach
* **Search and lookup records** across multiple entity types
* **Manage custom modules** with custom fields and records

#### Where to Use It

##### In Agents (Recommended)

Add Freshsales as a tool to any agent. The agent can then manage your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Freshsales tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List deals closing this month")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Contacts

| Tool                          | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| **List Contact Filters**      | List available contact views and filters                                   |
| **Create Contact**            | Create a contact using any current contact fields, including custom fields |
| **Get Contact**               | Get one contact by ID                                                      |
| **List Contacts**             | List contacts from a view with optional sorting and includes               |
| **Update Contact**            | Update a contact using any current contact fields                          |
| **Update Contact Team**       | Replace or update team members for a contact                               |
| **Upsert Contact**            | Create or update a contact using the upsert API                            |
| **Bulk Upsert Contacts**      | Bulk upsert contacts                                                       |
| **Bulk Assign Contact Owner** | Bulk assign contacts to an owner                                           |
| **Clone Contact**             | Clone a contact                                                            |
| **Delete Contact**            | Delete a contact                                                           |
| **Forget Contact**            | Permanently forget a contact                                               |
| **Bulk Delete Contacts**      | Bulk delete contacts                                                       |
| **List Contact Fields**       | List all contact fields, including custom fields                           |
| **List Contact Activities**   | List activities for one contact                                            |

##### Accounts

| Tool                     | Description                                           |
| ------------------------ | ----------------------------------------------------- |
| **List Account Filters** | List available account views and filters              |
| **Create Account**       | Create a sales account                                |
| **Get Account**          | Get one sales account by ID                           |
| **List Accounts**        | List sales accounts from a view                       |
| **Update Account**       | Update a sales account                                |
| **Update Account Team**  | Replace or update team members for a sales account    |
| **Upsert Account**       | Create or update a sales account using the upsert API |
| **Bulk Upsert Accounts** | Bulk upsert sales accounts                            |
| **Clone Account**        | Clone a sales account                                 |
| **Delete Account**       | Delete a sales account                                |
| **Forget Account**       | Permanently forget a sales account                    |
| **Bulk Delete Accounts** | Bulk delete sales accounts                            |
| **List Account Fields**  | List all account fields, including custom fields      |

##### Deals

| Tool                  | Description                                   |
| --------------------- | --------------------------------------------- |
| **List Deal Filters** | List available deal views and filters         |
| **Create Deal**       | Create a deal                                 |
| **Get Deal**          | Get one deal by ID                            |
| **List Deals**        | List deals from a view                        |
| **Update Deal**       | Update a deal                                 |
| **Update Deal Team**  | Replace or update team members for a deal     |
| **Upsert Deal**       | Create or update a deal using the upsert API  |
| **Bulk Upsert Deals** | Bulk upsert deals                             |
| **Clone Deal**        | Clone a deal                                  |
| **Delete Deal**       | Delete a deal                                 |
| **Forget Deal**       | Permanently forget a deal                     |
| **Bulk Delete Deals** | Bulk delete deals                             |
| **List Deal Fields**  | List all deal fields, including custom fields |

##### Marketing Lists

| Tool                                      | Description                                      |
| ----------------------------------------- | ------------------------------------------------ |
| **Create Marketing List**                 | Create a marketing list                          |
| **List Marketing Lists**                  | List marketing lists                             |
| **Update Marketing List**                 | Update a marketing list                          |
| **List Contacts in Marketing List**       | List contacts in a marketing list                |
| **Copy Contacts to Marketing List**       | Copy specific contacts into a marketing list     |
| **Remove Contacts from Marketing List**   | Remove contacts from a marketing list            |
| **Move Contacts Between Marketing Lists** | Move contacts from one marketing list to another |

##### Notes, Tasks, and Appointments

| Tool                   | Description                 |
| ---------------------- | --------------------------- |
| **Create Note**        | Create a note               |
| **Update Note**        | Update a note               |
| **Delete Note**        | Delete a note               |
| **Create Task**        | Create a task               |
| **Get Task**           | Get one task by ID          |
| **List Tasks**         | List tasks by filter        |
| **Update Task**        | Update a task               |
| **Mark Task Done**     | Mark a task as done         |
| **Delete Task**        | Delete a task               |
| **Create Appointment** | Create an appointment       |
| **Get Appointment**    | Get one appointment by ID   |
| **List Appointments**  | List appointments by filter |
| **Update Appointment** | Update an appointment       |
| **Delete Appointment** | Delete an appointment       |

##### Sales Activities

| Tool                           | Description                    |
| ------------------------------ | ------------------------------ |
| **Create Sales Activity**      | Create a sales activity        |
| **Get Sales Activity**         | Get one sales activity by ID   |
| **List Sales Activities**      | List sales activities          |
| **List Sales Activity Fields** | List all sales activity fields |
| **Update Sales Activity**      | Update a sales activity        |
| **Delete Sales Activity**      | Delete a sales activity        |

##### Search and Lookup

| Tool                      | Description                                |
| ------------------------- | ------------------------------------------ |
| **Search Records**        | Search records across selected entities    |
| **Lookup Records**        | Lookup records by one field and entity set |
| **Create Phone Call Log** | Create a manual phone call log             |

##### CPQ Products

| Tool                          | Description                      |
| ----------------------------- | -------------------------------- |
| **Create Product**            | Create a CPQ product             |
| **Get Product**               | Get one CPQ product by ID        |
| **Update Product**            | Update a CPQ product             |
| **Bulk Update Products**      | Bulk update CPQ products         |
| **Bulk Assign Product Owner** | Bulk assign CPQ product owners   |
| **Delete Product**            | Delete a CPQ product             |
| **Restore Product**           | Restore a deleted CPQ product    |
| **Bulk Delete Products**      | Bulk delete CPQ products         |
| **Bulk Restore Products**     | Bulk restore CPQ products        |
| **Add Product Prices**        | Add prices to a CPQ product      |
| **Update Product Prices**     | Update prices on a CPQ product   |
| **Delete Product Prices**     | Delete prices from a CPQ product |
| **Add Products to Deal**      | Set products on a deal           |
| **Update Products on Deal**   | Replace products on a deal       |
| **Delete Products from Deal** | Delete all products from a deal  |

##### CPQ Documents

| Tool                              | Description                             |
| --------------------------------- | --------------------------------------- |
| **Create Document**               | Create a CPQ document                   |
| **Get Document**                  | Get one CPQ document by ID              |
| **Update Document**               | Update a CPQ document                   |
| **Bulk Update Documents**         | Bulk update CPQ documents               |
| **Bulk Assign Document Owner**    | Bulk assign CPQ document owners         |
| **Delete Document**               | Delete a CPQ document                   |
| **Restore Document**              | Restore a deleted CPQ document          |
| **Bulk Delete Documents**         | Bulk delete CPQ documents               |
| **Bulk Restore Documents**        | Bulk restore CPQ documents              |
| **Forget Document**               | Permanently forget a CPQ document       |
| **Add Products to Document**      | Set products on a CPQ document          |
| **Update Products on Document**   | Replace products on a CPQ document      |
| **Delete Products from Document** | Delete all products from a CPQ document |
| **Get Related Products**          | Get related products for a CPQ document |

##### Files and Links

| Tool                             | Description                                                |
| -------------------------------- | ---------------------------------------------------------- |
| **Create File**                  | Upload a file to Freshsales and associate it with a record |
| **Create Link**                  | Create a document link and associate it with a record      |
| **List Contact Files and Links** | List files and links associated with a contact             |
| **Get Job Status**               | Get background job status by ID                            |

##### Custom Modules

| Tool                                  | Description                                           |
| ------------------------------------- | ----------------------------------------------------- |
| **Create Custom Module**              | Create a custom module                                |
| **Get Custom Module**                 | Get one custom module definition                      |
| **Update Custom Module**              | Update a custom module definition                     |
| **Delete Custom Module**              | Delete a custom module definition                     |
| **Create Custom Field**               | Create a field on a standard or custom module form    |
| **List Custom Module Fields**         | List forms and fields for a custom module entity type |
| **List Custom Module Filters**        | List available views and filters for a custom module  |
| **Create Custom Module Record**       | Create a record in a custom module                    |
| **Get Custom Module Record**          | Get one custom module record                          |
| **List Custom Module Records**        | List custom module records                            |
| **Update Custom Module Record**       | Update a custom module record                         |
| **Delete Custom Module Record**       | Delete a custom module record                         |
| **Forget Custom Module Record**       | Permanently forget a custom module record             |
| **Clone Custom Module Record**        | Clone a custom module record                          |
| **Bulk Delete Custom Module Records** | Bulk delete custom module records                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search contacts:**

```text
Find all contacts at Acme Corp
```

**Create a deal:**

```text
Create a deal called "Enterprise License" for $50,000 associated with the Acme account
```

**List tasks:**

```text
Show me all open tasks due this week
```

**Update a contact:**

```text
Update the contact with email john@acme.com to set the lifecycle stage to "customer"
```

**Manage marketing lists:**

```text
Add all contacts from the "Q4 Leads" list to the "Newsletter" marketing list
```

**Search across entities:**

```text
Search for "renewal" across contacts, deals, and accounts
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific names, emails, or record IDs                                                                                           |
| Action not completing            | Check that you've authenticated with Freshsales                                                                                     |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the Acme deal to closed-won" will find the deal first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Freshsales MCP server](https://www.gumloop.com/mcp/freshsales) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Gamma

*Create presentations, documents, and carousels with AI-powered content generation.*

**Source:** https://docs.gumloop.com/nodes/mcp/gamma

Create presentations, documents, and carousels with AI-powered content generation.

Gamma is a content creation platform that turns ideas into polished presentations, documents, and social carousels. The Gamma MCP server lets you create and retrieve content using natural language.

#### What Can It Do?

* **Create presentations** with customizable tone, imagery, and formatting
* **Generate documents** and one-pagers from outlines
* **Build social carousels** with consistent branding
* **Retrieve finished content** via shareable URLs

#### Where to Use It

##### In Agents (Recommended)

Add Gamma as a tool to any agent. The agent can then create and retrieve content conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Gamma tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a presentation about Q4 results")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool               | Description                                        |
| ------------------ | -------------------------------------------------- |
| **Create Gamma**   | Create presentations, documents, or social content |
| **Get Generation** | Check status and retrieve the finished URL         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a presentation:**

```text
Create a presentation about our Q4 results with a professional tone
```

**Create a document:**

```text
Create a one-page summary of our product features
```

**Create a carousel:**

```text
Create a social media carousel about productivity tips with 5 slides
```

**Check status:**

```text
Get the URL for my presentation once it's ready
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Be specific about the type of content (presentation, document, carousel)                                                      |
| Action not completing            | Check that you've authenticated with Gamma                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., creating then retrieving). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)           |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a presentation and share the link" will create the content first, then retrieve the URL. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Gamma MCP server](https://www.gumloop.com/mcp/gamma) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### GitHub

*Automate repositories, issues, PRs, and projects with AI-powered development workflows.*

**Source:** https://docs.gumloop.com/nodes/mcp/github

Automate repositories, issues, PRs, and projects with AI-powered development workflows.

GitHub is the world's leading code hosting platform for version control and collaboration. The GitHub MCP server lets you manage repositories, issues, pull requests, and projects using natural language.

#### What Can It Do?

* **Create and manage repositories** and branches on demand
* **Find and filter** issues, PRs, and commits for reporting
* **Organize projects** with fields and items
* **Inspect CI/CD logs** from GitHub Actions workflows and jobs
* **Automate releases** and collaborator management

#### Where to Use It

##### In Agents (Recommended)

Add GitHub as a tool to any agent. The agent can then interact with your repositories conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with GitHub tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List open issues in my repo")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                                           | Description                                                                            |
| ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Create/List/Search Repositories**            | Manage repositories                                                                    |
| **Get Contents**                               | Retrieve file or directory contents                                                    |
| **Create or Update File**                      | Create or update one or more files in a repository in a single commit                  |
| **List/Get Commits**                           | Access commit history                                                                  |
| **List/Search Issues**                         | Find and filter issues                                                                 |
| **Create/Update Issue**                        | Manage issues                                                                          |
| **Add Comment To Issue**                       | Comment on issues                                                                      |
| **List/Create Branches**                       | Manage branches                                                                        |
| **List/Get/Create/Update/Merge Pull Requests** | Manage PRs                                                                             |
| **Add Comment to Pull Request**                | Comment on PRs                                                                         |
| **List Pull Request Files**                    | View changed files in a PR                                                             |
| **List Pull Request Review Comments**          | List inline review comments on a PR (code-level comments on specific lines/files)      |
| **Request Pull Request Reviewers**             | Request reviews from users or teams                                                    |
| **List/Get Projects**                          | Access project boards                                                                  |
| **List/Create/Update/Delete Project Fields**   | Manage project fields                                                                  |
| **List/Add/Update/Delete Project Items**       | Manage project items                                                                   |
| **List/Get Tags and Releases**                 | Access releases                                                                        |
| **List/Add/Remove Collaborators**              | Manage access                                                                          |
| **List Labels, Milestones, Teams**             | Organization tools                                                                     |
| **List Deployments and Workflows**             | CI/CD access                                                                           |
| **List Workflow Runs**                         | List GitHub Actions workflow runs with optional filters (branch, status, event, actor) |
| **List Workflow Runs for Workflow**            | List GitHub Actions workflow runs for a specific workflow definition                   |
| **Get Workflow Run**                           | Get a specific GitHub Actions workflow run by its ID                                   |
| **List Workflow Jobs**                         | List jobs for a specific workflow run                                                  |
| **Get Job Logs**                               | Get plain-text logs for a workflow job, or download them to storage                    |
| **Get Workflow Run Logs**                      | Download the full log archive for a workflow run                                       |
| **Search Code**                                | Search across repositories                                                             |
| **List Vulnerability Alerts**                  | List Dependabot vulnerability alerts for a repository                                  |
| **Create Gist**                                | Create a new GitHub gist (public or secret) with one or more files                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search repositories:**

```text
Find repositories about "LLM chatbot" with more than 5000 stars
```

**Manage issues:**

```text
Create an issue in octocat/Hello-World titled "Bug: login fails"
```

**List pull requests:**

```text
Show me all open PRs in facebook/react
```

**Merge a pull request:**

```text
Merge PR #42 in my-org/my-repo using squash
```

**Request reviewers:**

```text
Request a review from @octocat on PR #15 in my-org/my-repo
```

**Get commit details:**

```text
Get the details of the latest commit in my repo
```

**Create or update files:**

```text
Create a README.md file in my-org/my-repo with the content "# My Project"
```

**Search code:**

```text
Search for "def get_queryset" in the Django repository
```

**Create a gist:**

```text
Create a secret gist called "debug notes" with a file notes.md containing my troubleshooting steps
```

**List vulnerability alerts:**

```text
List open Dependabot vulnerability alerts in my-org/my-repo
```

**View CI logs:**

```text
Show me the logs from the latest failed CI job in my-org/my-repo
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific repository names in owner/repo format                                                                                             |
| Action not completing            | Check that you've authenticated and have permissions for the repository                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a repo first, then listing issues). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                            |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create an issue in the marketing repo" will find the repository first, then create the issue. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [GitHub MCP server](https://www.gumloop.com/mcp/github) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Gmail

*Read, send, and organize emails with AI-powered inbox automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/gmail

Read, send, and organize emails with AI-powered inbox automation.

Gmail is Google's email service used by billions worldwide. The Gmail MCP server lets you search, read, send, and organize emails using natural language.

#### What Can It Do?

* **Search and read emails** with any filter, label, or timeframe
* **Send emails and replies** from within workflows
* **Manage drafts** — list, create, update, send, or delete drafts
* **Work with threads** — retrieve full email conversations
* **Organize your inbox** by starring, archiving, labeling, or batch-updating
* **Manage labels** — create, update, and delete custom labels
* **Send emails with file attachments** from Gumloop storage
* **Download attachments** for automated processing

#### Where to Use It

##### In Agents (Recommended)

Add Gmail as a tool to any agent. The agent can then interact with your inbox conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Gmail tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Find emails from Stripe about invoices")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description                                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Read Emails**         | Search and read emails (supports `body_format`: `text`, `html`, or `raw`)                                                 |
| **Send Email**          | Send new emails or replies (supports optional `sender` for Send As aliases and file attachments from Gumloop storage)     |
| **Update Email**        | Update labels (read/unread, folders)                                                                                      |
| **Create Draft**        | Prepare emails without sending (supports optional `sender` for Send As aliases and file attachments from Gumloop storage) |
| **List Drafts**         | List email drafts in the mailbox with optional search query                                                               |
| **Update Draft**        | Update an existing email draft with new content (supports file attachments from Gumloop storage)                          |
| **Delete Draft**        | Permanently delete an email draft                                                                                         |
| **Send Draft**          | Send an existing email draft                                                                                              |
| **Forward Email**       | Forward to other recipients (supports optional `sender` for Send As aliases)                                              |
| **Get Thread**          | Get a full email thread with all messages                                                                                 |
| **Create Label**        | Create new Gmail labels                                                                                                   |
| **Update Label**        | Update a label's name, colors, or visibility settings                                                                     |
| **Delete Label**        | Delete a custom Gmail label (system labels cannot be deleted)                                                             |
| **List Labels**         | List all Gmail labels with their IDs                                                                                      |
| **Archive Email**       | Move emails out of inbox                                                                                                  |
| **Trash Email**         | Move emails to trash                                                                                                      |
| **Star/Unstar Email**   | Manage starred emails                                                                                                     |
| **Batch Update Emails** | Modify labels on multiple emails at once                                                                                  |
| **Get Attachment**      | Download and access email attachments                                                                                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search emails:**

```text
Find emails from Stripe with "invoice" in the subject from this month
```

**Send an email:**

```text
Send an email to sarah@company.com about the project kickoff
```

**Organize inbox:**

```text
Archive all newsletters older than 30 days
```

**Download attachments:**

```text
Download the PDF attachments from the latest expense report email
```

**Send with attachments:**

```text
Send an email to john@company.com with the file "report.pdf" from my storage attached
```

**Create a draft:**

```text
Create a draft reply to the latest email from my manager
```

**Manage drafts:**

```text
List my recent drafts and send the one about the project proposal
```

**View a thread:**

```text
Show me the full conversation thread for the latest email from Sarah
```

**Batch update:**

```text
Add the "Reviewed" label to all emails from the hiring team this week
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                               |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific sender addresses or date ranges                                                                                           |
| Action not completing            | Check that you've authenticated with Gmail                                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then downloading). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                    |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Forward the invoice from Stripe to accounting" will find the email first, then forward it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Gmail MCP server](https://www.gumloop.com/mcp/gmail) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Gong

*Access sales call recordings, transcripts, and analytics with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/gong

Access sales call recordings, transcripts, and analytics with AI-powered automation.

Gong is a revenue intelligence platform that records and analyzes sales conversations. The Gong MCP server lets you search calls, retrieve transcripts, and access analytics using natural language.

#### What Can It Do?

* **Fetch calls and transcripts** for coaching and QA
* **Access scorecards and trackers** for performance insights
* **Manage Engage flows** to assign and track prospects in sequences
* **Manage users and workspaces** without manual API calls
* **Stream Gong data** to other tools for reporting

#### Where to Use It

##### In Agents (Recommended)

Add Gong as a tool to any agent. The agent can then search and analyze your sales data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Gong tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List calls from last week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                              | Description                                  |
| --------------------------------- | -------------------------------------------- |
| **List Calls**                    | List calls in a date range                   |
| **Get Call**                      | Get details for a specific call              |
| **Add Call**                      | Add a new call to Gong                       |
| **Get Call Transcript**           | Retrieve call transcripts                    |
| **Get Detailed Calls**            | Get calls with interaction metrics           |
| **List/Get Users**                | Access user data                             |
| **Get Answered Scorecards**       | Retrieve reviewed scorecards                 |
| **Get Interaction Stats**         | Get user interaction metrics                 |
| **Get Scorecards**                | List all scorecards                          |
| **Get Trackers**                  | Get keyword tracker details                  |
| **List Workspaces**               | List all workspaces                          |
| **List Library Folders**          | List library folders                         |
| **Get Folder Content**            | Get folder contents                          |
| **Manage Call Access**            | Control who can access calls                 |
| **List Flows**                    | List Gong Engage flows for a user            |
| **List Flow Folders**             | List Gong Engage flow folders for a user     |
| **List Prospect Flows**           | List Gong Engage flows assigned to prospects |
| **Assign Prospects to Flow**      | Assign prospects to a Gong Engage flow       |
| **Unassign Prospects from Flows** | Unassign prospects from Gong Engage flows    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List recent calls:**

```text
List all calls from last week with Acme Corp
```

**Get a transcript:**

```text
Get the transcript from the latest discovery call
```

**Check interaction stats:**

```text
Get interaction stats for Sarah for Q2 including talk ratio and empathy score
```

**Find scorecards:**

```text
Get answered scorecards from last month for the sales team
```

**List users:**

```text
List all users in the sales workspace with their roles
```

**List Engage flows:**

```text
List all Engage flows for sarah@company.com
```

**Assign prospects to a flow:**

```text
Assign prospect john@acme.com to the "SDR Outbound" Engage flow
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific date ranges or call IDs                                                                                                               |
| Action not completing            | Check that you've authenticated and have access to the workspace                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., listing calls first, then getting transcripts). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the transcript from the Acme call" will find the call first, then retrieve the transcript. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Gong MCP server](https://www.gumloop.com/mcp/gong) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Ads

*Manage campaigns, keywords, and performance with AI-powered advertising automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_ads

Manage campaigns, keywords, and performance with AI-powered advertising automation.

Google Ads is the world's largest digital advertising platform. The Google Ads MCP server lets you inspect, optimize, and update your campaigns using natural language.

#### What Can It Do?

* **Pull campaign performance** metrics including conversions, CTR, and cost per conversion
* **Analyze competitive positioning** with impression share metrics
* **Identify wasted spend** with low quality score keywords
* **Update campaign settings** and budgets without the UI
* **Track conversion value** across campaigns and asset groups
* **Export filtered data** to other tools for alerts

#### Where to Use It

##### In Agents (Recommended)

Add Google Ads as a tool to any agent. The agent can then interact with your advertising data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Ads tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List enabled campaigns with their performance")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                               | Description                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **List Campaigns**                 | Get campaigns with filters and metrics (includes conversions, CTR, cost per conversion, and conversion value) |
| **Get Campaign**                   | Get details for a single campaign with optional performance metrics                                           |
| **Update Campaign**                | Modify campaign settings                                                                                      |
| **List Asset Groups**              | Get asset groups with filters and performance metrics                                                         |
| **Get Asset Group**                | Get details for an asset group with optional metrics                                                          |
| **Update Asset Group**             | Modify asset group settings                                                                                   |
| **Get Account**                    | Get account-level information with optional metrics                                                           |
| **List Budgets**                   | List campaign budgets with amount, shared status, and usage details                                           |
| **Update Budget**                  | Update a campaign budget's daily amount, name, or delivery method                                             |
| **List Negative Keywords**         | List negative keywords                                                                                        |
| **Get Low Quality Score Keywords** | Find underperforming keywords                                                                                 |
| **Get Overspent Campaigns**        | Find campaigns over budget                                                                                    |
| **Get Competitive Metrics**        | Get impression share and lost impression share metrics for campaigns to analyze competitive positioning       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Campaign performance:**

```text
List all enabled campaigns with more than 1000 impressions from the last 30 days
```

**Budget optimization:**

```text
Find campaigns that exceeded their daily budget this week
```

**Keyword audit:**

```text
Get keywords with quality score below 4 in my search campaigns
```

**Update a campaign:**

```text
Pause the Black Friday campaign
```

**Account overview:**

```text
Get my account summary including total spend
```

**Competitive positioning:**

```text
Get impression share and lost impression share for my search campaigns this month
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific campaign names or IDs                                                                                                                 |
| Action not completing            | Check that you've authenticated and have account access                                                                                            |
| Unexpected results               | The agent may chain multiple tools (e.g., listing campaigns first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Pause the worst performing campaign" will list campaigns, identify the worst one, then pause it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Ads MCP server](https://www.gumloop.com/mcp/gads) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Analytics

*Run reports, manage GA4 properties, and send server-side events with AI-powered analytics automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_analytics

Run reports, manage GA4 properties, and send server-side events with AI-powered analytics automation.

Google Analytics 4 is Google's web and app analytics platform. The Google Analytics MCP server lets you run reports, manage accounts and properties, configure custom dimensions, metrics, and conversions, and send server-side events using natural language.

#### What Can It Do?

* **Run reports** for users, sessions, pageviews, and other metrics, including real-time data
* **Check report compatibility** to see which dimensions and metrics can be combined
* **Manage accounts and properties** including create, update, delete, and data retention settings
* **Configure data streams** for web, iOS, and Android
* **Manage custom dimensions, metrics, and conversion (key) events**
* **Link Google Ads and Firebase** projects to your GA4 properties
* **Export and download audiences** for downstream activation
* **Send server-side events** via the Measurement Protocol with auto-fetched API secrets

#### Where to Use It

##### In Agents (Recommended)

Add Google Analytics as a tool to any agent. The agent can then explore your analytics data and configuration conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Google account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Analytics tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run a 30-day report of users by country")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Reporting

| Tool                    | Description                                                                    |
| ----------------------- | ------------------------------------------------------------------------------ |
| **Run Report**          | Run 1-5 GA4 reports and get back users, sessions, pageviews, and other metrics |
| **Run Realtime Report** | Get real-time GA4 data for events in the last 30 minutes                       |
| **Check Compatibility** | Check which dimensions and metrics can be combined in a report                 |
| **Get Metadata**        | List all dimensions and metrics available for reports on a property            |
| **Run Access Report**   | See who accessed a GA4 account or property's data and when                     |

##### Audiences

| Tool                       | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| **Create Audience Export** | Start an export of users in a GA4 audience              |
| **List Audience Exports**  | List audience exports for a GA4 property                |
| **Get Audience Export**    | Check the status of a GA4 audience export               |
| **Query Audience Export**  | Download the users from a completed GA4 audience export |

##### Accounts

| Tool                                     | Description                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| **List Account Summaries**               | List your GA4 accounts along with the websites and apps tracked in each |
| **List Accounts**                        | List your GA4 accounts                                                  |
| **Get Account**                          | Get details of a GA4 account                                            |
| **Update Account**                       | Rename a GA4 account or change its region                               |
| **Delete Account**                       | Move a GA4 account to the trash                                         |
| **Get Account Data Sharing Settings**    | See how a GA4 account shares data with Google products and support      |
| **Search Account Change History Events** | See recent changes made in a GA4 account (who edited what)              |

##### Properties

| Tool                                 | Description                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| **List Properties**                  | List the websites and apps (properties) tracked in a GA4 account |
| **Get Property**                     | Get details of a GA4 property                                    |
| **Create Property**                  | Create a new GA4 property to track a website or app              |
| **Update Property**                  | Update a GA4 property's name, timezone, currency, or industry    |
| **Delete Property**                  | Move a GA4 property to the trash                                 |
| **Acknowledge User Data Collection** | Confirm Google's user-data-collection terms for a GA4 property   |
| **Get Data Retention Settings**      | See how long a GA4 property keeps user and event data            |
| **Update Data Retention Settings**   | Change how long a GA4 property keeps user and event data         |

##### Data Streams

| Tool                   | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **List Data Streams**  | List the web, iOS, and Android data streams for a GA4 property       |
| **Get Data Stream**    | Get details of a GA4 data stream                                     |
| **Create Data Stream** | Add a new website, iOS app, or Android app data stream to a property |
| **Update Data Stream** | Update a GA4 data stream's name or settings                          |
| **Delete Data Stream** | Delete a GA4 data stream                                             |

##### Custom Dimensions & Metrics

| Tool                        | Description                                                                      |
| --------------------------- | -------------------------------------------------------------------------------- |
| **List Custom Dimensions**  | List the custom dimensions defined on a GA4 property                             |
| **Get Custom Dimension**    | Get details of a GA4 custom dimension                                            |
| **Create Custom Dimension** | Create a custom dimension that captures an event parameter or user property      |
| **Update Custom Dimension** | Update or archive a GA4 custom dimension                                         |
| **List Custom Metrics**     | List the custom metrics defined on a GA4 property                                |
| **Get Custom Metric**       | Get details of a GA4 custom metric                                               |
| **Create Custom Metric**    | Create a custom metric from a numeric event parameter (currency, duration, etc.) |
| **Update Custom Metric**    | Update or archive a GA4 custom metric                                            |

##### Conversions (Key Events)

| Tool                 | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| **List Key Events**  | List the conversion events set up on a GA4 property         |
| **Get Key Event**    | Get details of a GA4 conversion event                       |
| **Create Key Event** | Mark an event as a conversion in GA4                        |
| **Update Key Event** | Update how a GA4 conversion is counted or its default value |
| **Delete Key Event** | Remove a conversion from GA4                                |

##### Product Links

| Tool                       | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| **List Google Ads Links**  | List the Google Ads accounts linked to a GA4 property       |
| **Create Google Ads Link** | Link a Google Ads account to a GA4 property                 |
| **Update Google Ads Link** | Change the ads-personalization setting on a Google Ads link |
| **Delete Google Ads Link** | Unlink a Google Ads account from a GA4 property             |
| **List Firebase Links**    | List the Firebase projects linked to a GA4 property         |
| **Create Firebase Link**   | Link a Firebase project to a GA4 property                   |
| **Delete Firebase Link**   | Unlink a Firebase project from a GA4 property               |

##### Measurement Protocol

| Tool                           | Description                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Measurement Protocol Event** | Send, validate, or send-and-validate a server-side event to GA4 via Measurement Protocol. Auto-fetches the API secret (creates one if none exist) and stream identifiers using OAuth |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Run a report:**

```text
Show me total users and sessions for example.com over the last 30 days, broken down by country
```

**Real-time monitoring:**

```text
How many active users are on my site right now and what pages are they viewing?
```

**Check compatibility:**

```text
Can I combine the "sessionDefaultChannelGroup" dimension with the "totalRevenue" metric in a report?
```

**Inspect a property:**

```text
List all properties in my Marketing GA4 account and show me each property's data retention settings
```

**Manage custom dimensions:**

```text
Create a custom dimension on the example.com property that captures the "plan_tier" user property
```

**Manage conversions:**

```text
List all conversion events on the example.com property and mark "signup_completed" as a conversion
```

**Audience export:**

```text
Start an audience export for the "Engaged Users" audience on example.com, then download the users once it's ready
```

**Send a server-side event:**

```text
Send a "purchase" event with value=49.99 and currency=USD to GA4 for client_id 12345 via Measurement Protocol
```

#### Troubleshooting

| Issue                                    | Solution                                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication failed                    | Verify your Google account has access to the GA4 property you're querying                                                                                           |
| Property not found                       | Use the property's numeric ID (e.g., `properties/123456789`) when prompting                                                                                         |
| Real-time report empty                   | Real-time data only covers the last 30 minutes. Try [Run Report](#reporting) for historical data                                                                    |
| Measurement Protocol event not appearing | Use the validate mode first to confirm the event payload is well-formed before sending                                                                              |
| Permission denied on update or delete    | These tools require analytics edit access; confirm your Google account has the right role on the property                                                           |
| Tool not available                       | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                                 |
| Unexpected results                       | The agent may chain multiple tools (e.g., listing accounts first, then properties, then running a report). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "What were my top 10 pages last week on example.com?" will look up the property ID first, then run the report. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Analytics MCP server](https://www.gumloop.com/mcp/ganalytics) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Calendar

*Manage events and scheduling with AI-powered calendar automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_calendar

Manage events and scheduling with AI-powered calendar automation.

Google Calendar is Google's scheduling service for managing events and appointments. The Google Calendar MCP server lets you create, update, and search events using natural language.

#### What Can It Do?

* **List and search events** for any date or time range with detailed attendee information, filterable by event type
* **Create meetings** with attendees and details, including special event types like Out of Office, Focus Time, and Working Location
* **Auto-generate Google Meet links** when creating events
* **Update or cancel events** without opening your calendar
* **Update attendee responses** for any event
* **Check free slots** for smart scheduling
* **Manage attendees** by adding or removing them from events
* **List calendars** accessible to the user
* **Move events** between calendars
* **View recurring event instances** with date filtering
* **Manage access control** rules for calendar sharing

#### Where to Use It

##### In Agents (Recommended)

Add Google Calendar as a tool to any agent. The agent can then manage your schedule conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Calendar tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a 30-minute meeting tomorrow")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                               | Description                                                                                                                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **List Events**                    | Retrieve events for a date range (includes attendee details with response status). Supports filtering by event type: default, Out of Office, Focus Time, Working Location, Birthday, and from Gmail.             |
| **Get Event**                      | Get a single event by ID with full details                                                                                                                                                                       |
| **Create Event**                   | Add a new event to your calendar (optionally auto-generates a Google Meet link via `create_conference`). Supports creating Out of Office, Focus Time, and Working Location events with type-specific properties. |
| **Update Event**                   | Modify an existing event. Supports updating event type properties such as Out of Office, Focus Time, and Working Location.                                                                                       |
| **Delete Event**                   | Remove an event                                                                                                                                                                                                  |
| **Update Attendee Status**         | Change an attendee's response status for an event                                                                                                                                                                |
| **Manage Attendee**                | Add or remove an attendee from an event                                                                                                                                                                          |
| **Check Free Slots**               | Find available time blocks                                                                                                                                                                                       |
| **List Calendars**                 | List all calendars accessible to the user                                                                                                                                                                        |
| **Move Event**                     | Move an event to a different calendar                                                                                                                                                                            |
| **List Recurring Event Instances** | List individual occurrences of a recurring event                                                                                                                                                                 |
| **List ACL Rules**                 | List access control rules for a calendar                                                                                                                                                                         |
| **Manage ACL Rule**                | Add or remove an access control rule on a calendar                                                                                                                                                               |

#### Example Prompts

Use these with your agent or in the Agent Node:

**View schedule:**

```text
What meetings do I have tomorrow?
```

**Create a meeting:**

```text
Schedule a 45-minute meeting with sarah@company.com next Tuesday at 2pm
```

**Create a meeting with a Google Meet link:**

```text
Schedule a 30-minute meeting with the eng team tomorrow at 10am and add a Google Meet link
```

**Check availability:**

```text
Find free 30-minute slots on Friday between 9am and 5pm
```

**Update a meeting:**

```text
Move my 10am meeting to 2pm
```

**Cancel a meeting:**

```text
Delete my meeting with John tomorrow
```

**Set Out of Office:**

```text
Create an out of office event for next Friday with the auto-decline message "On PTO"
```

**Block focus time:**

```text
Block 2 hours of focus time tomorrow morning starting at 9am
```

**Filter by event type:**

```text
Show me all out of office events on my calendar this month
```

**Check attendee responses:**

```text
Who has accepted the team standup meeting tomorrow?
```

**Add an attendee:**

```text
Add jane@company.com to my 3pm meeting tomorrow
```

**List calendars:**

```text
Show me all my calendars
```

**Move an event:**

```text
Move the project review meeting to my Work calendar
```

**View recurring instances:**

```text
Show me all instances of my weekly team standup for this month
```

**Manage calendar access:**

```text
Share my calendar with the marketing team as readers
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify dates and times clearly with timezone                                                                                                   |
| Action not completing            | Check that you've authenticated with Google Calendar                                                                                            |
| Unexpected results               | The agent may chain multiple tools (e.g., checking availability first, then creating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Schedule a meeting when I'm free" will check availability first, then create the event. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Calendar MCP server](https://www.gumloop.com/mcp/gcalendar) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Cloud Storage

*Manage buckets, files, and storage operations with AI-powered cloud storage automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_cloud_storage

Manage buckets, files, and storage operations with AI-powered cloud storage automation.

Google Cloud Storage is a scalable object storage service. The Google Cloud Storage MCP server lets you manage buckets, upload and download files, and organize your storage using natural language.

#### What Can It Do?

* **Upload and download files** to and from GCS buckets
* **Create and manage buckets** with custom configurations
* **Search and browse files** with filtering and pagination
* **Copy and move files** within or across buckets

#### Where to Use It

##### In Agents (Recommended)

Add Google Cloud Storage as a tool to any agent. The agent can then interact with Google Cloud Storage conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Google account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Cloud Storage tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all files in my data bucket")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool               | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| **List Buckets**   | List all accessible GCS buckets with optional filtering by prefix and project                     |
| **Search Files**   | List files/objects in a bucket with filtering by prefix, date range, and pagination support       |
| **File Details**   | Get detailed metadata for a specific file including size, content type, checksums, and timestamps |
| **Download File**  | Generate signed or public download URLs for files with configurable expiration time               |
| **Bucket Details** | Get comprehensive bucket information including versioning, lifecycle rules, and IAM settings      |
| **Upload File**    | Upload files from local filesystem to GCS buckets with optional content type specification        |
| **Delete File**    | Delete files/objects from GCS buckets                                                             |
| **Copy File**      | Copy files within the same bucket or across different buckets                                     |
| **Move File**      | Move or rename files within or across buckets (copy then delete)                                  |
| **Create Bucket**  | Create new GCS buckets with configurable location and storage class                               |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List files:**

```text
Show me all files in my data-exports bucket
```

**Upload a file:**

```text
Upload report.csv to the reports bucket
```

**Download a file:**

```text
Generate a download link for backup.zip in the archives bucket
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Google Cloud Storage credentials and that you have the required permissions                             |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Cloud Storage MCP server](https://www.gumloop.com/mcp/gcs) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google DV360

*Manage campaigns, line items, and targeting with AI-powered programmatic advertising automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_dv360

Manage campaigns, line items, and targeting with AI-powered programmatic advertising automation.

Google Display & Video 360 is a programmatic advertising platform. The Google DV360 MCP server lets you manage campaigns, line items, and targeting options using natural language.

#### What Can It Do?

* **Manage campaigns and line items** across advertisers
* **Configure targeting options** for precise audience reach
* **Track performance data** with comprehensive metrics
* **Control entity status** to pause or activate campaigns

#### Where to Use It

##### In Agents (Recommended)

Add Google DV360 as a tool to any agent. The agent can then interact with Google DV360 conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Google account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google DV360 tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List campaigns for my advertiser")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                         | Description                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| **List Partners**            | List partners accessible to the current user to get valid partner IDs for other operations |
| **List Advertisers**         | List advertisers in your Google DV360 account with filtering options                       |
| **Get Advertiser**           | Get detailed information about a specific advertiser by ID                                 |
| **List Campaigns**           | List campaigns for a specific advertiser with filtering options                            |
| **Get Campaign**             | Get detailed information about a specific campaign by ID                                   |
| **List Line Items**          | List line items for a specific advertiser with filtering options                           |
| **Get Line Item**            | Get detailed information about a specific line item by ID                                  |
| **Get Targeting Option**     | Get a specific targeting option assigned to a line item                                    |
| **List Targeting Options**   | List targeting options assigned to a line item for a specific targeting type               |
| **Search Targeting Options** | Search targeting options across multiple line items and targeting types                    |
| **Update Targeting Options** | Update targeting options for multiple line items (delete and create in one operation)      |
| **Update Status**            | Update the status of a campaign, insertion order, or line item (pause/activate)            |
| **Get Performance**          | Get comprehensive performance data                                                         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List campaigns:**

```text
Show me all active campaigns for my advertiser
```

**Check performance:**

```text
What's the performance data for my Q4 campaign?
```

**Manage targeting:**

```text
List the targeting options on my display line item
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Google DV360 credentials and that you have the required permissions                                     |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google DV360 MCP server](https://www.gumloop.com/mcp/gdv360) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Docs

*Create, read, and update Google Docs with AI-powered document automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_docs

Create, read, and update Google Docs with AI-powered document automation.

Google Docs is the go-to collaborative document editor. The Google Docs MCP server lets you search, read, create, and update documents using natural language - including rich text formatting with Markdown and HTML.

#### What Can It Do?

* **Search documents** in Google Drive by keyword
* **Read document content** including body text, lists, images, footnotes, headers, footers, and styles
* **Create new documents** with plain text, Markdown, or HTML content
* **Update existing documents** by appending, prepending, replacing, or inserting content
* **Manage tables** by inserting new tables and updating individual cells
* **Navigate multi-tab documents** by listing and reading individual tabs
* **Create and rename tabs** in multi-tab documents

#### Where to Use It

##### In Agents (Recommended)

Add Google Docs as a tool to any agent. The agent can then search and edit your documents conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Docs tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Read the full content of a Google Doc")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Read Tools

| Tool            | Description                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Search Docs** | Search for Google Docs in Drive by keyword                                                                                                                           |
| **Read Doc**    | Read content from a Google Doc including body, lists, inline objects, footnotes, headers, footers, and styles. Supports reading specific tabs in multi-tab documents |
| **List Tabs**   | List all tabs in a Google Doc with their IDs and titles                                                                                                              |

##### Write Tools

| Tool                  | Description                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create Doc**        | Create a new Google Doc with content in plain text, Markdown, or HTML format                                                                                                |
| **Update Doc**        | Update content in an existing Google Doc. Supports append, prepend, replace, insert at index, and find-and-replace operations. Content can be plain text, Markdown, or HTML |
| **Insert Table**      | Insert a table into a Google Doc with optional data and header styling                                                                                                      |
| **Update Table Cell** | Update the content of a specific table cell                                                                                                                                 |
| **Create Tab**        | Create a new tab in an existing Google Doc, optionally nested under a parent tab and at a specific position                                                                 |
| **Rename Tab**        | Rename an existing tab in a Google Doc                                                                                                                                      |

> **Info:** **Create Doc** and **Update Doc** support a `content_format` parameter with three options: `plain` (default), `markdown` (CommonMark), and `html` (rich formatting including bold, italic, colors, headings, lists, tables, code blocks, and images). When using Markdown or HTML, manual style parameters are ignored.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search for documents:**

```text
Search for Google Docs matching "quarterly report"
```

**Read a document:**

```text
Read the full content of this Google Doc including all tabs
```

**Create a document with Markdown:**

```text
Create a new Google Doc titled "Sprint Retrospective" with markdown content including headings and bullet points
```

**Create a document with HTML:**

```text
Create a new Google Doc titled "Styled Report" with HTML content including bold headings, colored text, and a bulleted list
```

**Append content:**

```text
Append a new section to this Google Doc with a summary in markdown format
```

**Find and replace:**

```text
Find all occurrences of "DRAFT" and replace with "FINAL" in this document
```

**Insert a table:**

```text
Insert a 4x3 table with a header row containing Name, Status, and Due Date
```

**List tabs:**

```text
List all tabs in this Google Doc with their IDs and titles
```

**Create a tab:**

```text
Create a new tab titled "Q3 Planning" in this Google Doc
```

**Rename a tab:**

```text
Rename the tab with ID t.abc123 to "Archived" in this Google Doc
```

#### Troubleshooting

| Issue                                | Solution                                                                                                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right document | Use specific document titles or IDs                                                                                                        |
| Action not completing                | Check that you've authenticated and have edit access to the document                                                                       |
| Unexpected results                   | The agent may chain multiple tools (e.g., searching first, then reading content). Review the agent's reasoning to understand its approach. |
| Tool not available                   | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |
| Rich text not rendering              | Make sure to set `content_format` to `markdown` or `html` when using formatted content                                                     |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find and update my meeting notes" will search first, then update the content. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Docs MCP server](https://www.gumloop.com/mcp/gdocs) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Drive

*Search, organize, and share files with AI-powered cloud storage automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_drive

Search, organize, and share files with AI-powered cloud storage automation.

Google Drive is Google's cloud storage service for files and folders. The Google Drive MCP server lets you search, create, move, and share files using natural language.

#### What Can It Do?

* **Search files and folders** by name, keyword, or date
* **Create, copy, move, and delete** files and folders
* **Generate new documents** and folder structures on demand
* **Upload and download files** between Gumloop storage and Google Drive
* **Share files** with specific permissions and get sharing links

#### Where to Use It

##### In Agents (Recommended)

Add Google Drive as a tool to any agent. The agent can then manage your files conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Drive tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for files modified this week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                            | Description                                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Search**                      | Search for files in Drive                                                                             |
| **Copy File**                   | Create a copy of a file                                                                               |
| **Create Folder Subfolder**     | Create folders and subfolders                                                                         |
| **Move File**                   | Move files between folders                                                                            |
| **Create Plain Text File**      | Create new text files                                                                                 |
| **Add File Sharing Preference** | Share files and get links                                                                             |
| **Update Name**                 | Rename files or folders                                                                               |
| **Get File**                    | Get file metadata and optionally read content (see [supported file types](#get-file-content-reading)) |
| **List Contents**               | List files in a folder (excludes trashed files by default)                                            |
| **Upload File**                 | Upload a file from Gumloop storage to Google Drive with optional folder destination                   |
| **Download File**               | Download a file from Google Drive to Gumloop storage                                                  |
| **Delete**                      | Delete files or folders                                                                               |

> **Info:** **List Contents** excludes trashed files by default. Set `trashed` to `true` to include trashed files alongside live ones, or `only_trashed` to `true` to return only trashed files (`only_trashed` takes precedence over `trashed`).

#### Get File Content Reading

The **Get File** tool can return file metadata by default, and optionally read file content when the `read` parameter is set to `true`.

**Supported file types** (uploaded/binary files):

* Plain text files (`.txt`, `.csv`, `.json`, etc.)
* PDFs (`.pdf`)
* Microsoft Office documents (`.docx`, `.xlsx`, `.pptx`)
* Other common formats that store content as binary data

**Not supported** (native Google Workspace files):

* Google Docs
* Google Sheets
* Google Slides

Native Google Workspace files (Docs, Sheets, Slides) do not have downloadable binary content through the Drive API, so `Get File` cannot extract their content. To read or modify the content of these files, use their dedicated MCP integrations instead:

* **Google Docs** → [Google Docs MCP](https://docs.gumloop.com/nodes/mcp/google_docs)
* **Google Sheets** → Google Sheets MCP

> **Warning:** If you use `Get File` with `read=true` on a native Google Workspace file (Doc, Sheet, or Slide), it will return metadata successfully but fail to extract the file content. Use the dedicated MCP integration for that file type instead (e.g., Google Docs MCP for Docs, Google Sheets MCP for Sheets).

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search files:**

```text
Find files containing "invoice" modified in the last week
```

**Create a folder:**

```text
Create a folder called "Q4 Reports" with subfolders for each month
```

**Share a file:**

```text
Share the budget spreadsheet with view access for anyone with the link
```

**Move files:**

```text
Move all files from the Inbox folder to the Archive folder
```

**Get file details:**

```text
Get the details and sharing link for the marketing presentation
```

**List only trashed files:**

```text
List only the trashed files in my Reports folder
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                          |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific file names or folder paths                                                                                           |
| Action not completing            | Check that you've authenticated and have access to the files                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then moving). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Share the Q4 report" will find the file first, then share it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Drive MCP server](https://www.gumloop.com/mcp/gdrive) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Maps

*Find and enrich location data with AI-powered place discovery.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_maps

Find and enrich location data with AI-powered place discovery.

Google Maps is the world's most popular mapping platform with millions of businesses and places. The Google Maps MCP server lets you search places, get details, and collect reviews using natural language.

#### What Can It Do?

* **Search places** by keyword, category, or location
* **Get place details** including contact info, ratings, and hours
* **Collect customer reviews** for reputation monitoring
* **Build lead lists** with geo-targeted searches

#### Where to Use It

##### In Agents (Recommended)

Add Google Maps as a tool to any agent. The agent can then search and explore location data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Maps tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Find coffee shops near Times Square")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description                    |
| ----------------------- | ------------------------------ |
| **Search Places**       | Search by location and keyword |
| **Get Place Details**   | Get full info for a place      |
| **Search By Category**  | Find places by category        |
| **Get Place Reviews**   | Pull customer reviews          |
| **Find Places In Area** | List places in a map area      |

#### Credit Costs

| Tool                | Credits Per Use |
| ------------------- | --------------- |
| Search Places       | 3 per item      |
| Get Place Details   | 5 per item      |
| Search By Category  | 3 per item      |
| Get Place Reviews   | 3 per item      |
| Find Places In Area | 3 per item      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search places:**

```text
Find coffee shops within 5 miles of Times Square
```

**Get details:**

```text
Get the contact info and rating for this restaurant
```

**Search by category:**

```text
Find coworking spaces in Austin, TX
```

**Get reviews:**

```text
Get the latest reviews for this business
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Be specific with location and search terms                                                                                                 |
| Action not completing            | Check that you've authenticated and have API credits                                                                                       |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get reviews for the best-rated coffee shop in Seattle" will search first, then get reviews. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Maps MCP server](https://www.gumloop.com/mcp/gmaps) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Meet

*Manage video meetings and transcripts with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_meet

Manage video meetings and transcripts with AI-powered automation.

Google Meet is Google's video conferencing service integrated with Google Calendar. The Google Meet MCP server lets you create, manage, and access meeting transcripts using natural language.

#### What Can It Do?

* **Create meetings** with specific times and attendees
* **Manage attendees** and update meeting details
* **Search meetings** by date or get specific meeting info
* **Access transcripts** from completed meetings

#### Where to Use It

##### In Agents (Recommended)

Add Google Meet as a tool to any agent. The agent can then manage your meetings conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Meet tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a meeting for tomorrow at 10am")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                      |
| --------------------------- | -------------------------------- |
| **Create Meeting**          | Create a new Google Meet session |
| **Add Attendees**           | Add attendees to a meeting       |
| **Fetch Meetings By Date**  | List meetings for a date         |
| **Get Meeting Details**     | Get full meeting info            |
| **Update Meeting**          | Change meeting details           |
| **Delete Meeting**          | Remove a meeting                 |
| **Read Meeting Transcript** | Get transcript text              |
| **List Conference Records** | List past meeting records        |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a meeting:**

```text
Create a Google Meet for tomorrow at 10:30am called "Team Sync"
```

**Add attendees:**

```text
Add john@company.com and sarah@company.com to the team meeting
```

**Find meetings:**

```text
What meetings do I have scheduled for Friday?
```

**Get transcript:**

```text
Get the transcript from yesterday's client call
```

**Update meeting:**

```text
Move the Q4 planning meeting to 2pm
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify dates and meeting names clearly                                                                                                             |
| Action not completing            | Check that you've authenticated with Google Meet                                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a meeting first, then adding attendees). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the transcript from the Acme call" will find the meeting first, then retrieve the transcript. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Meet MCP server](https://www.gumloop.com/mcp/gmeet) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google PageSpeed

*Analyze website performance, accessibility, SEO, and Core Web Vitals using Google PageSpeed Insights.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_pagespeed

Analyze website performance, accessibility, SEO, and Core Web Vitals using Google PageSpeed Insights.

Google PageSpeed Insights is Google's tool for measuring webpage performance. The Google PageSpeed MCP server lets you run Lighthouse audits, get performance scores, and check Core Web Vitals field data for any URL.

#### What Can It Do?

* **Run full PageSpeed analysis** to get Lighthouse scores across performance, accessibility, best practices, and SEO
* **Get detailed Lighthouse audits** for a specific category with individual audit results and recommendations
* **Check Core Web Vitals** field data (LCP, FID, CLS, INP, TTFB) from real-user metrics
* **Analyze for desktop or mobile** with locale-specific results

#### Where to Use It

##### In Agents (Recommended)

Add Google PageSpeed as a tool to any agent. The agent can analyze any URL conversationally and explain the results.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Google PageSpeed API key

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google PageSpeed tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run a mobile performance audit on my homepage")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                       | Description                                                                                                                                                                                                                                                       | Credits |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Run PageSpeed Analysis** | Run a full PageSpeed analysis on a URL. Returns Lighthouse scores for selected categories (performance, accessibility, best practices, SEO), performance metrics, and real-user loading experience data. Supports desktop or mobile strategy and locale settings. | 5       |
| **Get Lighthouse Audits**  | Get detailed Lighthouse audit results for a specific category on a URL. Returns individual audit pass/fail results with descriptions and recommendations.                                                                                                         | 5       |
| **Get Core Web Vitals**    | Get Core Web Vitals field data (LCP, FID, CLS, INP, TTFB) for a URL. Returns real-user loading experience metrics with percentile values and performance categories (FAST, AVERAGE, SLOW).                                                                        | 5       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Full site analysis:**

```text
Run a PageSpeed analysis on https://example.com for both desktop and mobile
```

**SEO audit:**

```text
Get the SEO audit results for https://example.com
```

**Core Web Vitals check:**

```text
Check the Core Web Vitals for https://example.com on mobile
```

**Accessibility review:**

```text
Run an accessibility audit on https://example.com and list the failing checks
```

**Compare strategies:**

```text
Compare the performance scores of https://example.com on desktop vs mobile
```

#### Troubleshooting

| Issue                      | Solution                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| No loading experience data | Field data requires sufficient real-user traffic. New or low-traffic pages may not have Core Web Vitals data available.                                |
| Authentication failed      | Verify your Google PageSpeed API key is connected and valid                                                                                            |
| Slow response times        | PageSpeed analysis runs a full Lighthouse audit which can take 10-30 seconds per request                                                               |
| Tool not available         | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                    |
| Unexpected results         | The agent may chain multiple tools (e.g., running a full analysis then drilling into audits). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "What's wrong with my site's performance?" will run the analysis, then drill into the performance audits to identify specific issues. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google PageSpeed MCP server](https://www.gumloop.com/mcp/gpagespeed) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Search Console

*Query search performance, inspect URLs, and manage sitemaps with AI-powered SEO automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_search_console

Query search performance, inspect URLs, and manage sitemaps with AI-powered SEO automation.

Google Search Console is Google's tool for monitoring and maintaining your site's presence in search results. The Google Search Console MCP server lets you query search analytics, inspect URL indexing status, and manage sitemaps using natural language.

#### What Can It Do?

* **Query search performance data** with dimensions like query, page, country, and device
* **Inspect URL indexing status** to check if Google can find and index your pages
* **List and manage sitemaps** submitted to Search Console
* **View Search Console properties** and permission levels
* **Filter analytics** by date ranges, search types, and custom dimension filters

#### Where to Use It

##### In Agents (Recommended)

Add Google Search Console as a tool to any agent. The agent can then analyze your search performance and indexing status conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Google account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Search Console tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get top queries for my site last month")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                       | Description                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| **List Sites**             | List Search Console properties accessible to the user                                          |
| **Get Site**               | Get permission details for a Search Console property                                           |
| **Query Search Analytics** | Query search performance data with dimensions (query, page, country, device, date) and filters |
| **Inspect URL**            | Inspect Google indexing status for a URL including crawl and index coverage                    |
| **List Sitemaps**          | List submitted sitemaps for a Search Console property                                          |
| **Get Sitemap**            | Get details for a submitted sitemap including processing status and content breakdown          |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check search performance:**

```text
Show me the top 20 queries for my site in the last 30 days sorted by clicks
```

**Analyze page performance:**

```text
What pages on example.com got the most impressions last month?
```

**Inspect a URL:**

```text
Is https://example.com/blog/my-post indexed by Google?
```

**Filter by device:**

```text
Compare my site's search performance on mobile vs desktop for the past week
```

**Check sitemaps:**

```text
List all sitemaps submitted for https://example.com and their status
```

**Country breakdown:**

```text
Show me search clicks and impressions by country for example.com last quarter
```

#### Troubleshooting

| Issue                 | Solution                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| No data returned      | Search Console data is typically available with a 2-3 day delay. Try querying an older date range.                                                |
| Authentication failed | Verify your Google account has access to the Search Console property you're querying                                                              |
| Property not found    | Use the exact property URL format from Search Console (e.g., `https://www.example.com/` or `sc-domain:example.com`)                               |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |
| Unexpected results    | The agent may chain multiple tools (e.g., listing sites first, then querying analytics). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "How is my site performing?" will list your properties first, then query search analytics for the relevant one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Search Console MCP server](https://www.gumloop.com/mcp/gsearchconsole) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Sheets

*Read and write spreadsheet data with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_sheet

Read and write spreadsheet data with AI-powered automation.

Google Sheets is Google's cloud-based spreadsheet application for data management and collaboration. The Google Sheets MCP server lets you read, write, and manipulate spreadsheet data using natural language.

#### What Can It Do?

* **Read spreadsheet data** from any range or entire sheets
* **Write and update cells** with new values or formulas
* **Create and manage sheets** within spreadsheets
* **Format cells** with bold, colors, font size, number formats, and alignment
* **Manage rows and columns** — insert or delete as needed
* **Sort and find-replace** data across ranges
* **Create charts** — bar, line, pie, scatter, area, and column charts from data
* **Search and filter data** based on conditions

#### Where to Use It

##### In Agents (Recommended)

Add Google Sheets as a tool to any agent. The agent can then work with your spreadsheets conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Sheets tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Read the sales data from column A")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------ |
| **Create Sheet**         | Create a new Google Sheets document                                                  |
| **Add Sheet**            | Add a new sheet tab to an existing spreadsheet                                       |
| **Get Spreadsheet Info** | Retrieve spreadsheet metadata (title, sheets, etc.)                                  |
| **Get Sheet Names**      | List all sheet tab names in a spreadsheet                                            |
| **Batch Get**            | Read values from multiple ranges                                                     |
| **Batch Update**         | Write values to multiple ranges                                                      |
| **Append Values**        | Append values to the end of a range (like inserting rows)                            |
| **Lookup Row**           | Search for a row by column value in a specified range                                |
| **Clear Values**         | Clear values from a given range                                                      |
| **Copy Sheet**           | Copy a sheet from one spreadsheet to another                                         |
| **Format Cells**         | Apply formatting to a cell range (bold, colors, font size, number format, alignment) |
| **Manage Rows/Columns**  | Insert or delete rows and columns in a sheet                                         |
| **Manage Sheet**         | Rename or delete a sheet tab in a spreadsheet                                        |
| **Sort Range**           | Sort a range of cells by one or more columns                                         |
| **Find Replace**         | Find and replace values in a spreadsheet                                             |
| **Add Chart**            | Create a chart (bar, line, pie, scatter, area, column) from a data range             |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Read data:**

```text
Read all data from the Sales sheet in my Q4 Report spreadsheet
```

**Write data:**

```text
Update cell B2 in the inventory sheet to 150
```

**Append rows:**

```text
Add a new row with "John", "Sales", "2024-01-15" to the employee sheet
```

**Search:**

```text
Find all rows where the status column says "Pending"
```

**Get info:**

```text
What sheets are in my Budget spreadsheet?
```

**Format cells:**

```text
Make the header row bold with a blue background in my Sales sheet
```

**Sort data:**

```text
Sort the data in my inventory sheet by price from highest to lowest
```

**Find and replace:**

```text
Replace all instances of "TBD" with "Confirmed" in the Events sheet
```

**Create a chart:**

```text
Create a bar chart from the revenue data in columns A through D
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                         |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify the spreadsheet name and sheet tab clearly                                                                               |
| Action not completing            | Check that you've authenticated and have edit access                                                                             |
| Unexpected results               | The agent may chain multiple tools (e.g., reading first, then writing). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)              |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the total in my budget sheet" will read the current data first, then update. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Sheets MCP server](https://www.gumloop.com/mcp/gsheets) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Slides

*Create, read, and manage Google Slides presentations with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_slides

Create, read, and manage Google Slides presentations with AI-powered automation.

Google Slides is Google's cloud-based presentation tool for creating and collaborating on slide decks. The Google Slides MCP server lets you search, create, edit, and manage presentations using natural language.

#### What Can It Do?

* **Search and open presentations** in Google Drive
* **Create new presentations** with slides, text, tables, images, and styling
* **Add and duplicate slides** with predefined or custom layouts
* **Add elements** like text boxes, images, shapes, tables, videos, and lines
* **Update elements** including styling, position, and text content
* **Manage tables** by inserting/deleting rows, columns, and merging cells
* **Find and replace text** across an entire presentation
* **Work with speaker notes** — read and update notes per slide
* **Manage comments** — list, create, reply, resolve, and delete

#### Where to Use It

##### In Agents (Recommended)

Add Google Slides as a tool to any agent. The agent can then create and edit presentations conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Slides tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a presentation with a title slide")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Presentation Tools

| Tool                       | Description                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| **Search Presentations**   | Search for Google Slides presentations in Drive                      |
| **Get Presentation**       | Get presentation content, structure, and metadata                    |
| **Get Presentation Link**  | Get shareable and present-mode links for a presentation              |
| **Export Presentation**    | Export a presentation to PDF or PPTX format                          |
| **Create Presentation**    | Create a new presentation with optional slides, content, and styling |
| **Duplicate Presentation** | Create a copy of an existing presentation                            |

##### Slide & Element Tools

| Tool               | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| **Add Slide**      | Add a new slide or duplicate an existing slide                   |
| **Add Element**    | Add a text box, image, shape, table, video, or line to a slide   |
| **Update Element** | Update styling, transform, or properties of an existing element  |
| **Manage Table**   | Insert or delete rows/columns, or merge/unmerge cells in a table |
| **Find Replace**   | Find and replace text across an entire presentation              |

##### Speaker Notes & Comments

| Tool                     | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| **Get Speaker Notes**    | Get speaker notes for one or all slides                               |
| **Update Speaker Notes** | Update speaker notes for a slide                                      |
| **Manage Comments**      | List, create, reply to, resolve, or delete comments on a presentation |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create a presentation:**

```text
Create a presentation titled "Q3 Review" with a title slide and three content slides
```

**Add content to a slide:**

```text
Add a text box with "Key Metrics" to the second slide of my presentation
```

**Export a presentation:**

```text
Export my presentation as a PDF for sharing
```

**Work with speaker notes:**

```text
Add speaker notes to slide 3 with talking points about the revenue forecast
```

**Find and replace:**

```text
Replace all instances of "2025" with "2026" in the presentation
```

**Manage comments:**

```text
List all comments on the presentation and resolve the ones about formatting
```

**Duplicate a presentation:**

```text
Make a copy of the Q3 Review presentation for Q4 planning
```

#### Troubleshooting

| Issue                                    | Solution                                                                                                                           |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right presentation | Use specific presentation titles or IDs                                                                                            |
| Action not completing                    | Check that you've authenticated with Google                                                                                        |
| Unexpected results                       | The agent may chain multiple tools (e.g., searching first, then editing). Review the agent's reasoning to understand its approach. |
| Tool not available                       | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add a summary slide to my Q3 presentation" will search for the presentation first, then add the slide. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Slides MCP server](https://www.gumloop.com/mcp/gslides) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Google Tasks

*Manage to-dos and task lists with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/google_tasks

Manage to-dos and task lists with AI-powered automation.

Google Tasks is Google's task management service integrated with Gmail and Calendar. The Google Tasks MCP server lets you create, organize, and update tasks using natural language.

#### What Can It Do?

* **Create and manage tasks** with titles, notes, and due dates
* **Organize task lists** for different projects or contexts
* **Mark tasks complete** and track progress
* **Query tasks** by list, status, or due date

#### Where to Use It

##### In Agents (Recommended)

Add Google Tasks as a tool to any agent. The agent can then manage your tasks conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Google Tasks tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a task in my Work list")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                               |
| ------------------------ | ----------------------------------------- |
| **List Task Lists**      | Retrieve all your task lists              |
| **Find Task List**       | Find a task list by name                  |
| **List Tasks in a List** | List tasks within a specific list         |
| **Create Task**          | Create a new task with due date and notes |
| **Update Task**          | Update task title, due date, or notes     |
| **Complete Task**        | Mark a task as completed                  |
| **Delete Task**          | Delete a task from a list                 |

#### Example Prompts

Use these with your agent or in the Agent Node:

**View tasks:**

```text
What tasks do I have due this week?
```

**Create a task:**

```text
Add "Review quarterly report" to my Work list with a due date of Friday
```

**Complete a task:**

```text
Mark the "Send invoice" task as complete
```

**List by project:**

```text
Show me all tasks in my Marketing list
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify the task list name clearly                                                                                                              |
| Action not completing            | Check that you've authenticated with Google Tasks                                                                                               |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a list first, then creating a task). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add a task to my Work list" will find the list ID first, then create the task. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Google Tasks MCP server](https://www.gumloop.com/mcp/gtasks) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Granola

*Search and access your Granola meeting notes.*

**Source:** https://docs.gumloop.com/nodes/mcp/granola

Search and access your Granola meeting notes.

Granola is an AI-powered meeting notes platform that automatically captures and organizes your meetings. The Granola MCP server lets you search and access your meeting notes using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Granola. Authentication uses OAuth — just connect your Granola account and start using it immediately.

#### What Can It Do?

* **Search meeting notes** by topic, participant, or date
* **Access transcripts** and summaries from past meetings
* **Find action items** and key decisions from meetings

#### Where to Use It

##### In Agents (Recommended)

Add Granola as a tool to any agent. The agent can then search and retrieve your meeting notes conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Granola account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Granola tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Granola uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Granola to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search notes:**

```text
Find my meeting notes from last week about the product roadmap
```

**Get action items:**

```text
What action items came out of my meeting with the engineering team?
```

**Find decisions:**

```text
What was decided about the Q3 budget in recent meetings?
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Granola account                                                                           |
| No notes found     | Check that Granola has been recording your meetings                                                                 |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Greenhouse

*Manage recruiting workflows with AI-powered applicant tracking and candidate management.*

**Source:** https://docs.gumloop.com/nodes/mcp/greenhouse

Manage recruiting workflows with AI-powered applicant tracking and candidate management.

Greenhouse is a leading applicant tracking system (ATS) and recruiting platform. The Greenhouse MCP server lets you manage candidates, applications, interviews, jobs, and scorecards through the Greenhouse Harvest API using natural language.

#### What Can It Do?

* **Manage candidates** including create, update, delete, anonymize, and merge
* **View activity history** for candidates and applications
* **Track applications** through stages with reject, hire, and move actions
* **Schedule and manage interviews** with interviewers and locations
* **Maintain jobs and job posts** with notes and interview stages
* **Review scorecards** with questions, answers, and candidate attributes
* **List and download attachments** like resumes, cover letters, and offer packets

#### Where to Use It

##### In Agents (Recommended)

Add Greenhouse as a tool to any agent. The agent can then interact with your recruiting data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Greenhouse account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Greenhouse tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all active candidates for the Engineering role")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Candidate Tools

| Tool                        | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **List Candidates**         | List candidates with filtering by email, tags, custom fields, and date ranges             |
| **List Candidate Activity** | List recent activity metadata for a candidate                                             |
| **Create Candidate**        | Create a new candidate with contact details, tags, and an optional application            |
| **Update Candidate**        | Update candidate info including name, company, title, and contact details                 |
| **Delete Candidate**        | Permanently delete a candidate                                                            |
| **Anonymize Candidate**     | Anonymize specific candidate fields (e.g., email, phone, attachments) for GDPR compliance |
| **Merge Candidates**        | Merge a secondary candidate into a primary candidate record                               |

##### Application Tools

| Tool                          | Description                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| **List Applications**         | List applications with filtering by candidate, job, stage, status, and date ranges |
| **List Application Activity** | List recent activity metadata for an application                                   |
| **Reject Application**        | Reject an application with a reason, optional notes, and rejection email           |
| **Unreject Application**      | Reverse a previous rejection on an application                                     |
| **Hire Application**          | Mark an application as hired with optional start date and opening                  |
| **Move Application**          | Move an application to a different stage or transfer to another job                |
| **Update Application**        | Update application fields like source, referrer, recruiter, and custom fields      |
| **Delete Application**        | Permanently delete an application                                                  |

##### Interview Tools

| Tool                  | Description                                                                         |
| --------------------- | ----------------------------------------------------------------------------------- |
| **List Interviews**   | List interviews with filtering by job, application, status, and date ranges         |
| **Create Interview**  | Schedule a new interview with interviewers, time, location, and video conferencing  |
| **Update Interview**  | Update interview details like time, location, and interviewers                      |
| **Delete Interview**  | Permanently delete an interview                                                     |
| **List Interviewers** | List interviewers with filtering by interview, user, scorecard, and response status |

##### Job Tools

| Tool                          | Description                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------- |
| **List Job Posts**            | List job posts with filtering by job, board, and status (active, live, internal)              |
| **List Jobs**                 | List jobs with filtering by department, office, status (open, draft, closed), and date ranges |
| **Update Job**                | Update job details including name, notes, department, offices, and custom fields              |
| **List Job Interview Stages** | List interview stages for jobs with filtering options                                         |
| **List Job Notes**            | List job notes with filtering by job, user, and visibility                                    |
| **Create Job Note**           | Add a note to a job with visibility settings                                                  |
| **Update Job Note**           | Update an existing job note                                                                   |
| **Delete Job Note**           | Permanently delete a job note                                                                 |

##### Organization Tools

| Tool                 | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| **List Users**       | List users with filtering by agency, office, department, and email |
| **List Approvers**   | List approvers with filtering by group, user, and status           |
| **List Departments** | List departments in your Greenhouse account                        |

##### Attachment Tools

| Tool                 | Description                                                                                                                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **List Attachments** | List attachments (resumes, cover letters, offer packets) with filtering by candidate, application, type, and date ranges. Supports downloading files and storing them in Gumloop workspace storage |

##### Scorecard Tools

| Tool                                             | Description                                                                         |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **List Scorecards**                              | List scorecards with filtering by interview kit, submitter, application, and status |
| **List Scorecard Questions**                     | List scorecard questions with optional multi-choice question options                |
| **List Scorecard Question Answers**              | List question answers with optional selected option details                         |
| **List Scorecard Question Candidate Attributes** | List mappings between scorecard questions and candidate attributes                  |
| **List Scorecard Candidate Attributes**          | List candidate attributes with ratings from scorecards                              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List active candidates:**

```text
Show me all candidates who applied in the last 30 days
```

**Create a candidate:**

```text
Create a new candidate named Jane Smith with email jane@example.com and tag her as Engineering
```

**Move an application:**

```text
Move the application for John Doe to the Interview stage
```

**Schedule an interview:**

```text
Schedule a technical interview for application 12345 tomorrow at 2pm in the NYC office
```

**Review scorecards:**

```text
Show me all completed scorecards for the Senior Engineer role
```

**Reject an application:**

```text
Reject application 67890 with reason "Position filled" and send a rejection email
```

**Download attachments:**

```text
Download all resumes for candidate 5851191 and save them to workspace storage
```

#### Troubleshooting

| Issue                 | Solution                                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Greenhouse account is connected and has the required Harvest API permissions                                                        |
| Candidate not found   | Use specific names, emails, or candidate IDs for accurate lookups                                                                               |
| Action not completing | Ensure your Greenhouse user has the necessary permissions for the operation                                                                     |
| Pagination issues     | Use the `max_limit` parameter to control how many results are returned                                                                          |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |
| Unexpected results    | The agent may chain multiple tools (e.g., finding the candidate first, then updating). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Reject all applications for the closed Marketing Manager role" will list the job, find its applications, then reject each one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Greenhouse MCP server](https://www.gumloop.com/mcp/greenhouse) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Gumloop

*Manage workflows and agents programmatically with AI-powered automation control.*

**Source:** https://docs.gumloop.com/nodes/mcp/gumloop

Manage workflows and agents programmatically with AI-powered automation control.

Gumloop is an AI automation platform for building agents and workflows. The Gumloop MCP server lets you manage flows, trigger runs, monitor executions, interact with agents, manage skills and artifacts, connect MCP servers, and search documentation using natural language.

#### What Can It Do?

* **List and manage saved flows** and workbooks in your account
* **Trigger flow runs** with optional input parameters
* **Monitor run status** and retrieve detailed execution results
* **Create, configure, and manage agents** with full lifecycle control
* **Run agent sessions** and send follow-up messages conversationally
* **Manage skills** by creating, updating, downloading, and deleting skill packs
* **Access agent artifacts** produced during sessions
* **List teams** (workspaces) you belong to
* **Connect and interact with MCP servers** including listing tools, calling tools, reading resources, and using prompts
* **Search documentation** and get AI-powered answers
* **Access audit logs** for organization-level activity tracking
* **Export organization data** for workflows, agents, agent interactions, or credit logs and poll export status

#### Where to Use It

##### In Agents (Recommended)

Add Gumloop as a tool to any agent. The agent can then manage your automations conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Gumloop tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Start my daily report flow")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Workflow Management

| Tool                 | Description                                                                           |
| -------------------- | ------------------------------------------------------------------------------------- |
| **List Saved Flows** | List saved flows/items in your account for a specific user or project                 |
| **List Workbooks**   | List workbooks and their associated saved flows with nested flow information          |
| **Start Flow Run**   | Trigger a flow execution with optional input parameters                               |
| **Get Run Details**  | Retrieve detailed flow run information including state, outputs, logs, and timestamps |
| **Get Run History**  | Retrieve automation run history for workbooks or saved items with execution details   |

##### Agent Management

| Tool             | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| **List Agents**  | List agents in your account, with optional search and workspace filtering |
| **Get Agent**    | Fetch a single agent's configuration by its ID                            |
| **Create Agent** | Create a new agent with a name, model, and optional configuration         |
| **Update Agent** | Update an existing agent's metadata or configuration                      |
| **List Models**  | List the model groups available to agents                                 |

##### Agent Sessions

| Tool                     | Description                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| **Start Agent**          | Send a message to a Gumloop agent and start an asynchronous interaction                  |
| **Get Agent Status**     | Poll the status of an agent interaction and retrieve the agent's response when completed |
| **Create Agent Session** | Start a session on an agent and return the completed response                            |
| **Get Session**          | Fetch the state and result of an agent session by ID                                     |
| **Send Session Message** | Send a follow-up message to an existing agent session and return the completed response  |
| **Cancel Session**       | Cancel an in-progress agent session                                                      |
| **List Agent Sessions**  | List an agent's sessions with search, filters, sort, and pagination                      |

##### Skills

| Tool               | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| **List Skills**    | List skills in your account, with optional search, filtering, and pagination |
| **Create Skill**   | Create a skill from one or more files stored in your workspace               |
| **Update Skill**   | Replace a skill's files with files stored in your workspace                  |
| **Delete Skill**   | Delete a skill from your account                                             |
| **Download Skill** | Get a download URL for a skill archive                                       |

##### Artifacts

| Tool                     | Description                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| **List Agent Artifacts** | List the artifacts an agent has produced, with optional session filtering and pagination |
| **Download Artifact**    | Get a download URL for an agent artifact                                                 |

##### Teams

| Tool           | Description                                                   |
| -------------- | ------------------------------------------------------------- |
| **List Teams** | List the teams (workspaces) the authenticated user belongs to |

##### MCP Server Management

| Tool                      | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| **List MCP Servers**      | List the MCP servers connected to your account                             |
| **Get MCP Server**        | Fetch a single connected MCP server's configuration by ID                  |
| **List MCP Server Tools** | List the tools exposed by a connected MCP server                           |
| **Call MCP Tool**         | Execute a single tool on a connected MCP server                            |
| **List MCP Resources**    | List the resources exposed by a connected MCP server                       |
| **Read MCP Resource**     | Read the contents of a resource from a connected MCP server by URI         |
| **List MCP Prompts**      | List the prompts exposed by a connected MCP server                         |
| **Get MCP Prompt**        | Get a rendered prompt from a connected MCP server, with optional arguments |

##### Documentation & Admin

| Tool                     | Description                                                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Search Documentation** | Search Gumloop documentation using semantic and keyword search with filtering options                                                                        |
| **Ask Gummie**           | Ask questions and get AI-powered answers from Gumloop documentation with citations                                                                           |
| **Search Brain**         | Search your Company Brain's indexed knowledge sources for relevant content                                                                                   |
| **Get Audit Logs**       | Retrieve organization audit logs with event details and filtering by time period (admin only)                                                                |
| **Export Data**          | Create and initiate an organization data export for workflows, agents, agent interactions, or credit logs, returning a `data_export_id` to poll (admin only) |
| **Get Export Status**    | Poll a data export's status and optionally get a signed download URL for the completed CSV                                                                   |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List flows:**

```text
Show me all my saved flows
```

**Trigger a run:**

```text
Start the "Daily Report" flow with input parameter date set to today
```

**Check run status:**

```text
What's the status of my latest flow run?
```

**Create an agent:**

```text
Create a new agent called "Research Assistant" using the GPT-4o model
```

**Start a session:**

```text
Start a session with my Research Assistant agent and ask "Summarize the latest quarterly report"
```

**Send a follow-up message:**

```text
Send a follow-up message to my active session: "Can you break that down by region?"
```

**Manage skills:**

```text
List all skills in my account
```

**Download an artifact:**

```text
Show me the artifacts from my last agent session and download the report
```

**List connected MCP servers:**

```text
What MCP servers are connected to my account?
```

**Call an MCP tool:**

```text
Use my connected Slack MCP server to send a message to #general
```

**Search docs:**

```text
Search the Gumloop documentation for how to set up webhooks
```

**Ask Gummie:**

```text
How do I configure a Slack trigger for my workflow?
```

**View audit logs:**

```text
Show me the organization audit logs from the past week
```

**Export data:**

```text
Export all workflow runs from January 1 to March 31 and give me the download link when it's ready
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify flow names or project IDs explicitly                                                                                                    |
| Action not completing            | Check that you've authenticated with Gumloop                                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., listing flows first, then triggering a run). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                             |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Run my latest flow and show me the results" will list flows, trigger a run, and poll for completion. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Gumloop MCP server](https://www.gumloop.com/mcp/gumloop) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Hex

*Manage data projects and analytics workflows with AI-powered Hex automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/hex

Manage data projects and analytics workflows with AI-powered Hex automation.

Hex is a collaborative data platform for analytics, data science, and reporting. The Hex MCP server lets you manage projects, trigger runs, organize collections, and administer users and groups using natural language.

#### What Can It Do?

* **List and manage projects** including status updates and sharing permissions
* **Trigger and monitor project runs** with optional input parameters
* **Organize work** with collections for grouping related projects
* **Manage data connections** to external databases and warehouses
* **Administer users and groups** for workspace access control

#### Where to Use It

##### In Agents (Recommended)

Add Hex as a tool to any agent. The agent can then manage your Hex workspace conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Hex tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run my weekly analytics project")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Projects

| Tool                                   | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| **List Projects**                      | List projects in your Hex workspace, or get a specific project by ID |
| **Update Project Status**              | Update the status of a Hex project                                   |
| **Update Project Sharing (Users)**     | Update user-level sharing permissions on a project                   |
| **Update Project Sharing (Workspace)** | Update workspace and public sharing permissions on a project         |

##### Runs

| Tool                  | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| **Run Project**       | Trigger a run of a published Hex project                          |
| **List Project Runs** | List runs for a project, or get a specific run's status by run ID |
| **Cancel Run**        | Cancel an active run for a project                                |

##### Collections

| Tool                  | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| **List Collections**  | List collections in your workspace, or get a specific collection by ID |
| **Create Collection** | Create a new collection in your workspace                              |
| **Update Collection** | Update a collection's permissions and settings                         |

##### Data Connections

| Tool                       | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| **List Data Connections**  | List data connections in your workspace, or get a specific connection by ID |
| **Update Data Connection** | Update a data connection's settings, credentials, or sharing configuration  |

##### Administration

| Tool                | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **List Users**      | List users in your Hex workspace                             |
| **Deactivate User** | Deactivate a user in your workspace                          |
| **List Groups**     | List groups in your workspace, or get a specific group by ID |
| **Create Group**    | Create a new group with optional initial members             |
| **Update Group**    | Update a group's name and/or add or remove members           |
| **Delete Group**    | Delete a group from your workspace                           |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List projects:**

```text
Show me my most recently published Hex projects
```

**Run a project:**

```text
Trigger a run of the Weekly Sales Report project
```

**Check run status:**

```text
What's the status of my latest run for the Revenue Dashboard?
```

**Cancel a run:**

```text
Cancel the currently running job for my Analytics project
```

**Manage collections:**

```text
Create a new collection called "Q1 Reports" and list all existing collections
```

**Share a project:**

```text
Give editor access to alice@company.com on the Revenue Dashboard project
```

**Manage groups:**

```text
Create a new group called "Data Team" and add alice@company.com and bob@company.com
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific project names or provide project IDs                                                                                                  |
| Action not completing            | Check that you've authenticated with Hex                                                                                                           |
| Unexpected results               | The agent may chain multiple tools (e.g., listing projects first, then triggering a run). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Run my latest project and check the status" will find the project, trigger a run, and poll for completion. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Hex MCP server](https://www.gumloop.com/mcp/hex) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### HubSpot

*Manage your CRM with AI-powered contact, deal, and ticket automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/hubspot

Manage your CRM with AI-powered contact, deal, and ticket automation.

HubSpot is an all-in-one CRM platform for sales, marketing, and customer service. The HubSpot MCP server lets you manage contacts, companies, deals, tickets, and engagements using natural language.

#### What Can It Do?

* **Manage contacts and companies** with full CRUD operations
* **Track and search deals** through your sales pipeline
* **Handle support tickets** and customer interactions
* **Log engagements** like calls, emails, and meetings
* **Send transactional emails** using HubSpot email templates
* **Create associations** between records
* **Manage products** in your product catalog
* **Work with lists** for contact segmentation
* **Manage properties** and custom object schemas
* **Work with any CRM object type** using generic CRUD tools
* **Build forms and workflows** for marketing automation
* **Handle files** with upload, download, and management
* **Access conversations** and inbox threads
* **Manage blog posts and landing pages** for content marketing
* **Track email and campaign analytics** for performance insights

#### Where to Use It

##### In Agents (Recommended)

Add HubSpot as a tool to any agent. The agent can then manage your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with HubSpot tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a contact with email and name")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                           | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| **List Contacts**              | List contacts with optional filtering                                         |
| **Create Contact**             | Create a new contact                                                          |
| **Get Contact**                | Retrieve a specific contact by ID                                             |
| **Update Contact**             | Update an existing contact                                                    |
| **Search Contacts**            | Search with advanced filters                                                  |
| **Merge Contacts**             | Merge two contact records                                                     |
| **GDPR Delete Contact**        | Permanently delete a contact for GDPR compliance                              |
| **List Companies**             | List companies with filtering                                                 |
| **Create Company**             | Create a new company                                                          |
| **Get Company**                | Retrieve a specific company                                                   |
| **Update Company**             | Update an existing company                                                    |
| **Search Companies**           | Search with advanced filters                                                  |
| **List Deals**                 | List deals with filtering                                                     |
| **Search Deals**               | Search for deals using advanced filters, date ranges, sorting, and pagination |
| **Create Deal**                | Create a new deal                                                             |
| **Get Deal**                   | Retrieve a specific deal by ID                                                |
| **Update Deal**                | Update an existing deal                                                       |
| **List Tickets**               | List tickets with filtering                                                   |
| **Get Ticket**                 | Retrieve a specific ticket by ID                                              |
| **Create Ticket**              | Create a new ticket                                                           |
| **Update Ticket**              | Update an existing ticket                                                     |
| **Delete Ticket**              | Delete a ticket                                                               |
| **Merge Tickets**              | Merge two tickets                                                             |
| **List Products**              | List products in the catalog                                                  |
| **Get Product**                | Retrieve a specific product                                                   |
| **Create Product**             | Create a new product                                                          |
| **Update Product**             | Update an existing product                                                    |
| **Delete Product**             | Delete a product                                                              |
| **Get Engagements**            | Get engagement data for a contact                                             |
| **Get Engagement**             | Get a specific engagement by ID                                               |
| **List Engagements**           | List all engagements                                                          |
| **Get Recent Engagements**     | Get recently created or modified engagements                                  |
| **Get Call Dispositions**      | Get available call disposition options                                        |
| **Create Engagement**          | Create a call, email, meeting, or note                                        |
| **Update Engagement**          | Update an existing engagement                                                 |
| **Delete Engagement**          | Delete an engagement                                                          |
| **Log Email**                  | Log an email activity on a HubSpot contact's timeline                         |
| **Send Transactional Email**   | Send a transactional email to a recipient using a HubSpot email template      |
| **Get Associations**           | Get associations for an object                                                |
| **Create Association**         | Link two objects together                                                     |
| **Delete Association**         | Remove an association between objects                                         |
| **Get Association Types**      | Get available association types                                               |
| **List Lists**                 | List all contact lists                                                        |
| **Get List**                   | Get a specific list                                                           |
| **Create List**                | Create a new contact list                                                     |
| **Delete List**                | Delete a list                                                                 |
| **Get List Memberships**       | Get contacts in a list                                                        |
| **Add List Members**           | Add contacts to a list                                                        |
| **Remove List Members**        | Remove contacts from a list                                                   |
| **List Properties**            | List properties for an object type                                            |
| **Create Property**            | Create a new property                                                         |
| **Update Property**            | Update an existing property                                                   |
| **Delete Property**            | Delete a property                                                             |
| **List Custom Object Schemas** | List custom object schemas                                                    |
| **List Custom Objects**        | List custom object records                                                    |
| **Create Custom Object**       | Create a custom object record                                                 |
| **Update Custom Object**       | Update a custom object record                                                 |
| **List CRM Objects**           | List CRM records for any object type                                          |
| **Get CRM Object**             | Get one or many CRM records for any object type                               |
| **Search CRM Objects**         | Search CRM records for any object type                                        |
| **Create CRM Object**          | Create one or many CRM records for any object type                            |
| **Update CRM Object**          | Update one or many CRM records for any object type                            |
| **Upsert CRM Objects**         | Create or update CRM records by unique property values                        |
| **Archive CRM Object**         | Archive one or many CRM records for any object type                           |
| **List Forms**                 | List all forms                                                                |
| **Get Form Submissions**       | Get submissions for a form                                                    |
| **List Workflows**             | List all workflows                                                            |
| **Enroll In Workflow**         | Enroll a contact in a workflow                                                |
| **Get Events**                 | Get timeline events                                                           |
| **Get Email Statistics**       | Get email campaign statistics                                                 |
| **List Campaigns**             | List marketing campaigns                                                      |
| **List Blog Posts**            | List blog posts                                                               |
| **Create Blog Post**           | Create a new blog post                                                        |
| **Update Blog Post**           | Update a blog post                                                            |
| **Delete Blog Post**           | Delete a blog post                                                            |
| **List Landing Pages**         | List landing pages                                                            |
| **List Files**                 | List files in the file manager                                                |
| **Upload File**                | Upload a file                                                                 |
| **Download File**              | Download a file                                                               |
| **Delete File**                | Delete a file                                                                 |
| **List Conversation Inboxes**  | List conversation inboxes                                                     |
| **List Conversation Threads**  | List conversation threads                                                     |
| **Get Thread Messages**        | Get messages in a thread                                                      |
| **Send Thread Message**        | Send a message in a thread                                                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find contacts:**

```text
Find all contacts at Microsoft with Director in their title
```

**Create a deal:**

```text
Create a deal called "Enterprise License - Acme" for $75,000 in the proposal stage
```

**Search deals:**

```text
Find all deals closing this quarter with amount over $50,000
```

**Update a contact:**

```text
Update john@company.com to lifecycle stage "customer"
```

**Check tickets:**

```text
Show me all high-priority open tickets
```

**Log an activity:**

```text
Log a 15-minute call with the Acme contact about their renewal
```

**Log an email on the timeline:**

```text
Log an email on john@acme.com's timeline with subject "Q4 renewal" and the body of my follow-up
```

**Send a transactional email:**

```text
Send the "Welcome Email" transactional template to jane@company.com
```

> **Info:** The legacy **Send Email** tool is deprecated. Use **Send Transactional Email** for outbound sends (requires the `transactional-email` scope and a configured HubSpot email template) and **Log Email** to record an email activity on a contact's timeline.

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific names, emails, or IDs                                                                                                  |
| Action not completing            | Check that you've authenticated with HubSpot                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the Acme deal to closed-won" will find the deal first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [HubSpot MCP server](https://www.gumloop.com/mcp/hubspot) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Incident.io

*Streamline incident response with AI-powered incident and alert management.*

**Source:** https://docs.gumloop.com/nodes/mcp/incident_io

Streamline incident response with AI-powered incident and alert management.

Incident.io is an incident management platform for modern engineering teams. The Incident.io MCP server lets you create, update, and search incidents and alerts using natural language.

#### What Can It Do?

* **Search incidents** by status, severity, type, or date range
* **Create new incidents** with details and Slack integration
* **Update incident status** and severity as response progresses
* **List and link alerts** to incidents for better context

#### Where to Use It

##### In Agents (Recommended)

Add Incident.io as a tool to any agent. The agent can then manage your incidents conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Incident.io tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all critical incidents from this week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                       |
| ------------------------ | --------------------------------- |
| **List Users**           | List users in your account        |
| **List Incidents**       | List incidents with filtering     |
| **Create Incident**      | Create a new incident             |
| **Edit Incident**        | Update status or severity         |
| **List Alerts**          | List alerts with filtering        |
| **List Incident Alerts** | List alerts linked to an incident |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find incidents:**

```text
Show me all critical incidents from this week
```

**Create an incident:**

```text
Create a new incident titled "Database connection issues" with severity critical
```

**Update status:**

```text
Set the API outage incident to resolved
```

**List alerts:**

```text
Show me all firing alerts from today
```

**Check incident details:**

```text
What's the status of the payment processing incident?
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific incident names or IDs                                                                                                  |
| Action not completing            | Check that you've authenticated with Incident.io                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Resolve the database incident" will find the incident first, then update its status. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Incident.io MCP server](https://www.gumloop.com/mcp/incident-io) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Instagram

*Scrape public Instagram data with AI-powered social media automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/instagram

Scrape public Instagram data with AI-powered social media automation.

Instagram is the world's leading photo and video sharing platform. The Instagram MCP server lets you search profiles, pull posts, download reels, and collect engagement data using natural language.

#### What Can It Do?

* **Scrape posts and reels** from any public profile by username or directly by URL
* **Pull comments** and engagement metrics
* **Search profiles** by name or username
* **Collect hashtag feeds** for content discovery

#### Where to Use It

##### In Agents (Recommended)

Add Instagram as a tool to any agent. The agent can then search and analyze Instagram data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Instagram tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get the latest 10 posts from @nike")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Scrape Posts**        | Scrape posts by username or directly by post URL. Returns captions, likes, comments, media URLs, tagged users, and metadata |
| **Scrape Reels**        | Scrape reels by username or directly by reel URL. Returns captions, view counts, likes, duration, hashtags, and video URLs  |
| **Get Post Comments**   | Retrieves comments on a post                                                                                                |
| **Get Hashtag Posts**   | Collects posts using a hashtag                                                                                              |
| **Find Users**          | Searches profiles by name                                                                                                   |
| **Get Profile Details** | Fetches profile metadata                                                                                                    |
| **Get Profile Stories** | Downloads active stories                                                                                                    |
| **Get Tagged Posts**    | Gets posts where user is tagged                                                                                             |

#### Credit Costs

| Tool                | Credits Per Use |
| ------------------- | --------------- |
| Scrape Posts        | 3 per item      |
| Scrape Reels        | 3 per item      |
| Get Post Comments   | 3 per item      |
| Get Hashtag Posts   | 3 per item      |
| Find Users          | 3 per item      |
| Get Profile Details | 5 per item      |
| Get Profile Stories | 3 per item      |
| Get Tagged Posts    | 3 per item      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Scrape posts by username:**

```text
Scrape the latest 15 posts from @nike with captions and like counts
```

**Scrape posts by URL:**

```text
Scrape these Instagram posts: https://www.instagram.com/p/ABC123/ and https://www.instagram.com/p/DEF456/
```

**Scrape reels by username:**

```text
Scrape 10 reels from @natgeo with view counts and durations
```

**Scrape reels by URL:**

```text
Scrape these Instagram reels: https://www.instagram.com/reel/XYZ789/
```

**Search hashtags:**

```text
Find 20 posts using #coffeeshop
```

**Find influencers:**

```text
Search for fitness coach profiles with over 10k followers
```

**Get profile info:**

```text
Get the follower count and bio for @natgeo
```

**Pull comments:**

```text
Get the comments from this Instagram post URL
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use exact usernames with @ symbol, or provide direct Instagram URLs                                                                              |
| Action not completing            | Check that you've authenticated and the profile is public                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a profile first, then getting posts). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                              |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get reels from the top fitness influencer" will search profiles first, then get reels. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Instagram MCP server](https://www.gumloop.com/mcp/instagram) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Intercom

*Manage customer conversations and support with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/intercom

Manage customer conversations and support with AI-powered automation.

Intercom is a customer messaging platform for sales, marketing, and support. The Intercom MCP server lets you manage contacts, conversations, tickets, and help center content using natural language.

#### What Can It Do?

* **Search and manage contacts** by name or email
* **Handle conversations** with replies and tags
* **Create and update tickets** for support workflows
* **Work with companies** and help center articles

#### Where to Use It

##### In Agents (Recommended)

Add Intercom as a tool to any agent. The agent can then manage your customer data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Intercom tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a ticket for a billing issue")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                      | Description                          |
| ------------------------- | ------------------------------------ |
| **Search Contacts**       | Search for contacts by name or email |
| **Update Contact**        | Update, archive, or block a contact  |
| **Create Contact**        | Create a new contact                 |
| **Create Conversation**   | Start a new conversation             |
| **Reply To Conversation** | Reply to an existing conversation    |
| **Update Conversation**   | Add or remove tags                   |
| **Search Conversations**  | Search conversations by criteria     |
| **Search Companies**      | Search for companies                 |
| **Create Company**        | Create a new company                 |
| **List Articles**         | List help center articles            |
| **Search Tickets**        | Search for tickets                   |
| **Create Ticket**         | Create a new support ticket          |
| **Update Ticket**         | Update ticket status                 |
| **Add Comment To Ticket** | Add a comment to a ticket            |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find a contact:**

```text
Find the contact with email john@company.com
```

**Create a ticket:**

```text
Create a support ticket for billing discrepancy for this contact
```

**Search conversations:**

```text
Find all open conversations tagged "urgent"
```

**Update a ticket:**

```text
Set the billing ticket status to in progress
```

**Reply to conversation:**

```text
Reply to the conversation saying we're looking into it
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific emails or conversation IDs                                                                                                              |
| Action not completing            | Check that you've authenticated with Intercom                                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a contact first, then creating a ticket). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                  |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a ticket for [john@company.com](mailto:john@company.com)" will find the contact first, then create the ticket. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Intercom MCP server](https://www.gumloop.com/mcp/intercom) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Ironclad

*Manage contracts and workflows with AI-powered CLM automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/ironclad

Manage contracts and workflows with AI-powered CLM automation.

Ironclad is a contract lifecycle management platform for legal and business teams. The Ironclad MCP server lets you search, update, and monitor workflows and records using natural language.

#### What Can It Do?

* **Search and monitor workflows** with filters and pagination
* **Manage approvals and signatures** to keep deals moving
* **Read and update records** with properties and relationships
* **Post comments** and track collaboration

#### Where to Use It

##### In Agents (Recommended)

Add Ironclad as a tool to any agent. The agent can then manage your contracts conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Ironclad tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List workflows pending approval")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                                | Description                            |
| ----------------------------------- | -------------------------------------- |
| **Get Me**                          | Get current authenticated user info    |
| **List Workflows**                  | List workflows with filtering          |
| **Get Workflow**                    | View a specific workflow               |
| **List Workflow Approval Requests** | List approval requests                 |
| **Update Workflow Approval**        | Update approval status                 |
| **Get Workflow Sign Status**        | Get signature status                   |
| **Manage Workflow Signature**       | Send requests or create recipient URLs |
| **List Workflow Comments**          | List comments on a workflow            |
| **Create Workflow Comment**         | Post a new comment                     |
| **Update Workflow Metadata**        | Update workflow fields                 |
| **List Records**                    | List records with filtering            |
| **Get Record**                      | View a specific record                 |
| **Update Record Metadata**          | Update record properties               |
| **Get Workflow Schema**             | Get workflow design schema             |
| **Get Records Schema**              | Get record type schemas                |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find workflows:**

```text
Show me all workflows pending approval from this week
```

**Update approval:**

```text
Approve the NDA workflow for the legal role
```

**Add a comment:**

```text
Add a comment saying "Ready for signature" to the Acme contract workflow
```

**Search records:**

```text
Find all contracts with "subscription" in the title
```

**Check signature status:**

```text
What's the signature status on the vendor agreement?
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                     |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific workflow names or record titles                                                                                                 |
| Action not completing            | Check that you've authenticated with Ironclad                                                                                                |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a workflow first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                          |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Approve the Acme NDA" will find the workflow first, then update the approval. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Ironclad MCP server](https://www.gumloop.com/mcp/ironclad) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Jam

*Access your Jam bug reports and debug logs.*

**Source:** https://docs.gumloop.com/nodes/mcp/jam

Access your Jam bug reports and debug logs.

Jam is a bug reporting tool that captures browser context, console logs, and network requests automatically. The Jam MCP server lets you access your bug reports and debug information using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Jam. Authentication uses OAuth — just connect your Jam account and start using it immediately.

#### What Can It Do?

* **Access bug reports** with full browser context
* **View debug logs** including console output and network requests
* **Search issues** by description, reporter, or status

#### Where to Use It

##### In Agents (Recommended)

Add Jam as a tool to any agent. The agent can then access and analyze your bug reports conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Jam account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Jam tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Jam uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Jam to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**View bugs:**

```text
Show me the latest bug reports from this week
```

**Debug an issue:**

```text
Get the console logs and network requests for bug report #123
```

**Search reports:**

```text
Find all bug reports related to the login page
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Jam account                                                                               |
| No reports found   | Check that bug reports have been submitted through the Jam extension                                                |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Jira

*Manage projects and issues with AI-powered development workflow automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/jira

Manage projects and issues with AI-powered development workflow automation.

Jira is Atlassian's project tracking platform for agile teams. The Jira MCP server lets you create projects, file issues, update tickets, and manage users using natural language.

#### What Can It Do?

* **Create and manage projects** for teams or initiatives
* **File, update, and transition issues** without opening Jira
* **Search with JQL** to find issues across your workspace
* **Add and download file attachments** between issues and Gumloop storage
* **Post internal comments** on Jira Service Management issues
* **Write descriptions and comments in markdown** with automatic conversion to Atlassian Document Format (ADF) for rich text rendering
* **Manage users and groups** for permissions
* **Create and manage service desk requests**

#### Where to Use It

##### In Agents (Recommended)

Add Jira as a tool to any agent. The agent can then manage your development workflow conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Jira tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a bug in project APP")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Create Project**          | Set up a new Jira project                                                                                                          |
| **Get Project**             | Retrieve project metadata                                                                                                          |
| **Update Project**          | Modify project details                                                                                                             |
| **Delete Project**          | Delete a project                                                                                                                   |
| **List Projects**           | List all accessible projects                                                                                                       |
| **Create Issue**            | Create a new issue, bug, or story                                                                                                  |
| **Get Issue**               | Retrieve issue details                                                                                                             |
| **Update Issue**            | Modify issue fields                                                                                                                |
| **Delete Issue**            | Remove an issue                                                                                                                    |
| **Transition My Issue**     | Move an issue to a new status                                                                                                      |
| **Search Issues**           | Search using JQL                                                                                                                   |
| **Comment On Issue**        | Add a comment (supports internal/private notes for JSM issues and markdown input that is converted to ADF for rich text rendering) |
| **Add Attachment**          | Add a file attachment to an issue from Gumloop storage                                                                             |
| **Download Attachment**     | Download a file attachment from a Jira issue to Gumloop storage                                                                    |
| **List Fields**             | List all available fields including custom fields                                                                                  |
| **Get Edit Metadata**       | Get editable fields and allowed values for an issue                                                                                |
| **List Issues**             | List issues by JQL query                                                                                                           |
| **Execute JQL**             | Execute a raw JQL query for advanced searching and filtering                                                                       |
| **Add User To Issue**       | Add a user as assignee, reporter, or watcher                                                                                       |
| **List Users**              | List all users                                                                                                                     |
| **Add User To Group**       | Add user to a group                                                                                                                |
| **Remove User From Group**  | Remove a user from a group                                                                                                         |
| **List Groups**             | List all user groups                                                                                                               |
| **Create Group**            | Create a new user group                                                                                                            |
| **Get Myself**              | Get info about the authenticated user                                                                                              |
| **Get My Issues**           | Get your assigned issues                                                                                                           |
| **Get My Recent Activity**  | View recently updated issues you interacted with                                                                                   |
| **Get My Permissions**      | Check what actions you can perform in a project                                                                                    |
| **List Issue Link Types**   | List available link types (Blocks, Duplicate, Relates, etc.)                                                                       |
| **Create Issue Link**       | Link two issues together (e.g., blocks, duplicates, relates to)                                                                    |
| **Delete Issue Link**       | Remove a link between issues                                                                                                       |
| **Get Issue Links**         | Get all links for a specific issue                                                                                                 |
| **List Service Desks**      | List all Jira Service Management service desks                                                                                     |
| **Get Request Types**       | Get available request types for a service desk                                                                                     |
| **Create Customer Request** | Create a new customer request in a service desk                                                                                    |
| **Get Customer Request**    | Retrieve a customer request by issue key                                                                                           |
| **List Customer Requests**  | List customer requests from service desks                                                                                          |
| **Get Request Type Fields** | Get fields required to create a specific request type                                                                              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create an issue:**

```text
Create a bug in project APP with summary "Login button unresponsive"
```

**Find issues:**

```text
Search for high-priority issues in the CRM project
```

**Update status:**

```text
Move issue APP-234 to In Progress
```

**Add a comment:**

```text
Add comment "Verified in staging" to issue CRM-89
```

**Add an internal note (JSM):**

```text
Add an internal comment "Escalated to engineering" to service desk issue SD-45
```

**Attach a file:**

```text
Attach the file "report.pdf" from my storage to issue APP-100
```

**Download an attachment:**

```text
Download all attachments on issue APP-100 to my Gumloop storage
```

**Write a rich comment in markdown:**

```text
Comment on CRM-89 with "**Status:** verified in staging. See [runbook](https://wiki/runbook) for rollback steps."
```

**Check my work:**

```text
What issues are assigned to me?
```

**List service desks:**

```text
List all service desks and show me the available request types for each
```

**Create a service request:**

```text
Create a customer request in service desk 1 for request type 5 with summary "New laptop setup"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific issue keys (e.g., APP-234) or project keys                                                                                    |
| Action not completing            | Check that you've authenticated with Jira                                                                                                  |
| Unexpected results               | The agent may chain multiple tools (e.g., finding an issue first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Close all bugs in project WEB" will search first, then transition each. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Jira MCP server](https://www.gumloop.com/mcp/jira) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Klaviyo

*Manage Klaviyo profiles, campaigns, lists, and marketing data.*

**Source:** https://docs.gumloop.com/nodes/mcp/klaviyo

Manage Klaviyo profiles, campaigns, lists, and marketing data.

Klaviyo is the marketing automation platform for email, SMS, and push notifications. The Klaviyo MCP server lets you manage profiles, campaigns, lists, and marketing data using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Klaviyo. Authentication uses OAuth — just connect your Klaviyo account and start using it immediately.

#### What Can It Do?

* **Manage profiles** and subscriber data
* **Work with campaigns** for email and SMS
* **Organize lists** and segments
* **Access marketing data** and analytics

#### Where to Use It

##### In Agents (Recommended)

Add Klaviyo as a tool to any agent. The agent can then manage your marketing operations conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Klaviyo account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Klaviyo tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Klaviyo uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Klaviyo to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Manage campaigns:**

```text
Show me all active email campaigns and their open rates
```

**Work with lists:**

```text
How many subscribers are in the "VIP Customers" list?
```

**View profiles:**

```text
Find the profile for customer@example.com and show their engagement history
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have admin access to your Klaviyo account                                                                |
| Data not loading   | Check that your OAuth scope includes the requested data                                                             |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### LaunchDarkly

*Manage feature flags, segments, and environments with AI-powered release automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/launchdarkly

Manage feature flags, segments, and environments with AI-powered release automation.

LaunchDarkly is a feature management platform. The LaunchDarkly MCP server lets you create and manage feature flags, segments, and environments using natural language.

#### What Can It Do?

* **Create and manage feature flags** across projects
* **Target specific users and segments** with flag rules
* **Monitor flag status** across environments
* **Manage segments** for grouped targeting

#### Where to Use It

##### In Agents (Recommended)

Add LaunchDarkly as a tool to any agent. The agent can then interact with LaunchDarkly conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with LaunchDarkly tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all feature flags in production")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------- |
| **List Projects**           | List all projects in your LaunchDarkly account                                         |
| **List Environments**       | List all environments within a project                                                 |
| **List Feature Flags**      | List all feature flags in a project with filtering options                             |
| **Get Feature Flag**        | Get a single feature flag by key with rollout info                                     |
| **Create Feature Flag**     | Create a new feature flag                                                              |
| **Update Feature Flag**     | Update a feature flag - turn on/off, add/remove targets by context (e.g. business\_id) |
| **Delete Feature Flag**     | Delete a feature flag                                                                  |
| **Get Feature Flag Status** | Get flag status in an environment (new, active, inactive, launched)                    |
| **List Code Repositories**  | List connected code repositories for code references                                   |
| **List Segments**           | List all segments in an environment                                                    |
| **Get Segment**             | Get a segment with included/excluded contexts                                          |
| **Create Segment**          | Create a new segment                                                                   |
| **Update Segment**          | Update a segment - add/remove contexts (e.g. business\_id) to include/exclude          |
| **Delete Segment**          | Delete a segment                                                                       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List flags:**

```text
Show me all feature flags in the production project
```

**Toggle a flag:**

```text
Turn on the new-checkout flag in the staging environment
```

**Check status:**

```text
What's the status of the dark-mode flag?
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your LaunchDarkly credentials and that you have the required permissions                                     |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [LaunchDarkly MCP server](https://www.gumloop.com/mcp/launchdarkly) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Linear

*Manage issues and projects with AI-powered product development automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/linear

Manage issues and projects with AI-powered product development automation.

Linear is a modern issue tracking platform for product teams. The Linear MCP server lets you manage issues, projects, initiatives, and more using natural language.

#### What Can It Do?

* **Search issues** using keywords, labels, states, or assignees
* **Create new issues** in any team or project
* **Update issue status**, priority, or assignee
* **Manage projects** with filtering by team, status, and initiative
* **Manage initiatives** with full CRUD, status tracking, and project linking
* **Triage bugs** and feature requests automatically

#### Where to Use It

##### In Agents (Recommended)

Add Linear as a tool to any agent. The agent can then manage your issues conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Linear tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a bug in team Platform")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Issue Tools

| Tool              | Description                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Search Issues** | Search issues with filters including team, label, state, assignee, cycle, project, and date ranges. Filters accept both names and IDs. |
| **Create Issue**  | Create a new issue in any team with title, description, priority, labels, and assignee                                                 |
| **Update Issue**  | Update status, priority, assignee, labels, and other issue fields                                                                      |
| **Delete Issue**  | Permanently delete an issue                                                                                                            |

##### Comment Tools

| Tool               | Description                        |
| ------------------ | ---------------------------------- |
| **List Comments**  | List comments for a specific issue |
| **Create Comment** | Create a comment on an issue       |
| **Delete Comment** | Delete a comment on an issue       |

##### Project Tools

| Tool               | Description                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| **List Projects**  | List projects with filtering by team, status, initiative, and date ranges. Filters accept both names and IDs. |
| **Get Project**    | Retrieve details of a specific project                                                                        |
| **Create Project** | Create a new project with name, description, teams, and target dates                                          |
| **Update Project** | Update project details including name, status, and dates                                                      |
| **Delete Project** | Permanently delete a project                                                                                  |

##### Initiative Tools

| Tool                  | Description                                                                    |
| --------------------- | ------------------------------------------------------------------------------ |
| **List Initiatives**  | List initiatives with filtering by status, health, name, and date ranges       |
| **Get Initiative**    | Retrieve details of a specific initiative including linked projects            |
| **Create Initiative** | Create a new initiative with name, description, status, target date, and owner |
| **Update Initiative** | Update initiative details and link or unlink projects                          |
| **Delete Initiative** | Permanently delete an initiative                                               |

##### Status Update Tools

| Tool                     | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **List Status Updates**  | List project status updates (health/progress reports) with optional date filtering |
| **Post Status Update**   | Create or edit a project status update with health status and description          |
| **Delete Status Update** | Delete a project status update                                                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find issues:**

```text
Search for bugs labeled "critical" in the Backend team
```

**Create an issue:**

```text
Create an issue in team Growth titled "Add referral tracking"
```

**Update status:**

```text
Move the API rate limit issue to In Progress
```

**Assign work:**

```text
Assign the database timeout issue to alice@company.com
```

**Check status:**

```text
What's the status of the checkout bug?
```

**List projects:**

```text
Show me all active projects in the Platform team
```

**Create an initiative:**

```text
Create a new initiative called "Q2 Platform Improvements" with status Planned
```

**Link a project to an initiative:**

```text
Link the API Redesign project to the Q2 Platform Improvements initiative
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific issue titles or team names                                                                                             |
| Action not completing            | Check that you've authenticated with Linear                                                                                         |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Set the checkout bug to high priority" will find the issue first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Linear MCP server](https://www.gumloop.com/mcp/linear) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Looker

*Access enterprise dashboards and analytics with AI-powered business intelligence automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/looker

Access enterprise dashboards and analytics with AI-powered business intelligence automation.

Looker is a Google Cloud business intelligence platform for data exploration and visualization. The Looker MCP server lets you manage dashboards, run queries, explore LookML models, schedule deliveries, and monitor alerts using natural language.

#### What Can It Do?

* **Manage dashboards** by listing, creating, updating, and deleting dashboards and their elements
* **Work with Looks** to create, run, and manage saved queries
* **Run queries** inline or from saved definitions, with async task support
* **Explore LookML models** and their dimensions, measures, and relationships
* **Schedule deliveries** for reports and dashboards
* **Manage alerts** for threshold-based notifications
* **Organize content** with folders, boards, favorites, and metadata
* **Render dashboards and Looks** as downloadable images or PDFs

#### Where to Use It

##### In Agents (Recommended)

Add Looker as a tool to any agent. The agent can then access your dashboards and analytics conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Looker tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Run the monthly sales dashboard query")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Setting Up Credentials

Looker uses API3 client credentials for authentication. You'll need:

1. A Looker Enterprise instance with API access enabled
2. A dedicated service account Client ID and Client Secret (generated in Looker Admin → Users → API Keys)
3. Your Looker API Host URL (e.g., `https://company.cloud.looker.com`)

Add these credentials to your [Connectors page](https://www.gumloop.com/personal/connectors).

#### Available Tools

##### Dashboards

| Tool                     | Description                      |
| ------------------------ | -------------------------------- |
| **List Dashboards**      | Search Looker dashboards         |
| **Get Dashboard**        | Get a Looker dashboard           |
| **Create Dashboard**     | Create a Looker dashboard        |
| **Update Dashboard**     | Update a Looker dashboard        |
| **Delete Dashboard**     | Delete a Looker dashboard        |
| **Move or Copy Content** | Move or copy a dashboard or Look |

##### Dashboard Elements

| Tool                         | Description               |
| ---------------------------- | ------------------------- |
| **List Dashboard Elements**  | Search dashboard tiles    |
| **Create Dashboard Element** | Create a dashboard tile   |
| **Update Dashboard Element** | Update a dashboard tile   |
| **Delete Dashboard Element** | Delete a dashboard tile   |
| **Create Dashboard Filter**  | Create a dashboard filter |
| **Update Dashboard Filter**  | Update a dashboard filter |
| **Delete Dashboard Filter**  | Delete a dashboard filter |

##### Looks

| Tool            | Description          |
| --------------- | -------------------- |
| **List Looks**  | Search Looker Looks  |
| **Get Look**    | Get a Looker Look    |
| **Create Look** | Create a Looker Look |
| **Update Look** | Update a Looker Look |
| **Delete Look** | Delete a Looker Look |
| **Run Look**    | Run a Looker Look    |

##### Queries

| Tool                       | Description                       |
| -------------------------- | --------------------------------- |
| **Run Query**              | Run a saved Looker query          |
| **Run Inline Query**       | Run an inline Looker query        |
| **Create Query**           | Create a Looker query             |
| **Get Query**              | Get a Looker query                |
| **Create Query Task**      | Create an async Looker query task |
| **Get Query Task**         | Get a Looker query task           |
| **Get Query Task Results** | Get Looker query task results     |

##### Rendering

| Tool                             | Description                    |
| -------------------------------- | ------------------------------ |
| **Create Dashboard Render Task** | Create a dashboard render task |
| **Create Look Render Task**      | Create a Look render task      |
| **Get Render Task**              | Get a Looker render task       |
| **Get Render Task Results**      | Get Looker render task results |

##### LookML

| Tool                         | Description          |
| ---------------------------- | -------------------- |
| **List LookML Models**       | List LookML models   |
| **Get LookML Model**         | Get a LookML model   |
| **Get LookML Model Explore** | Get a LookML explore |

##### Folders & Content

| Tool                        | Description                    |
| --------------------------- | ------------------------------ |
| **List Folders**            | Search Looker folders          |
| **Get Folder**              | Get a Looker folder            |
| **Create Folder**           | Create a Looker folder         |
| **Update Folder**           | Update a Looker folder         |
| **Delete Folder**           | Delete a Looker folder         |
| **Search Content**          | Search Looker content          |
| **List Content Favorites**  | Search content favorites       |
| **Create Content Favorite** | Favorite Looker content        |
| **Delete Content Favorite** | Remove a content favorite      |
| **Get Content Metadata**    | Get Looker content metadata    |
| **Update Content Metadata** | Update Looker content metadata |
| **Validate Content**        | Run Looker content validation  |

##### Boards

| Tool                     | Description            |
| ------------------------ | ---------------------- |
| **List Boards**          | List Looker boards     |
| **Get Board**            | Get a Looker board     |
| **Create Board**         | Create a Looker board  |
| **Update Board**         | Update a Looker board  |
| **Delete Board**         | Delete a Looker board  |
| **Create Board Section** | Create a board section |
| **Update Board Section** | Update a board section |
| **Delete Board Section** | Delete a board section |
| **Create Board Item**    | Create a board item    |
| **Update Board Item**    | Update a board item    |
| **Delete Board Item**    | Delete a board item    |

##### Scheduled Plans & Delivery

| Tool                        | Description                 |
| --------------------------- | --------------------------- |
| **List Scheduled Plans**    | List Looker scheduled plans |
| **Get Scheduled Plan**      | Get a scheduled plan        |
| **Create Scheduled Plan**   | Create a scheduled plan     |
| **Update Scheduled Plan**   | Update a scheduled plan     |
| **Delete Scheduled Plan**   | Delete a scheduled plan     |
| **Run Scheduled Plan Once** | Run a scheduled plan once   |

##### Alerts

| Tool             | Description           |
| ---------------- | --------------------- |
| **List Alerts**  | Search Looker alerts  |
| **Get Alert**    | Get a Looker alert    |
| **Create Alert** | Create a Looker alert |
| **Update Alert** | Update a Looker alert |
| **Delete Alert** | Delete a Looker alert |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List dashboards:**

```text
Show me all dashboards that contain "revenue" in the title
```

**Run a Look:**

```text
Run the "Monthly Sales Summary" Look and show me the results
```

**Run an inline query:**

```text
Run a query on the orders explore showing total revenue by region for this quarter
```

**Explore LookML:**

```text
What dimensions and measures are available in the orders explore?
```

**Schedule a report:**

```text
Create a scheduled plan to email the Sales Dashboard every Monday at 9am
```

**Manage content:**

```text
Move the Q4 dashboard to the Finance folder
```

**Render a dashboard:**

```text
Generate a PDF export of the Executive Summary dashboard
```

**Check alerts:**

```text
Show me all active alerts for the revenue metrics
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Client ID and Client Secret are correct and the service account has API access                          |
| Dashboard not found   | Use exact dashboard titles or IDs. Try listing dashboards first to find the correct reference.                      |
| Query timeout         | Large queries may take time. Use async query tasks for complex queries.                                             |
| Permission denied     | Ensure the service account has the appropriate Looker role and model access                                         |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Show me last month's revenue trend" will find the right Look or explore, run the query, and present the results. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Looker MCP server](https://www.gumloop.com/mcp/glooker) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Loops

*Manage mailing lists, contacts, and email automation with AI-powered workflows.*

**Source:** https://docs.gumloop.com/nodes/mcp/loops

Manage mailing lists, contacts, and email automation with AI-powered workflows.

Loops is a modern email platform for SaaS companies. The Loops MCP server lets you manage contacts, mailing lists, and send transactional or event-triggered emails using natural language.

#### What Can It Do?

* **Manage contacts** including create, update, find, and delete
* **Organize mailing lists** and subscriber segments
* **Send event-triggered emails** to automate communication flows
* **Send transactional emails** with dynamic data variables
* **Retrieve contact properties** for audience insights

#### Where to Use It

##### In Agents (Recommended)

Add Loops as a tool to any agent. The agent can then interact with your email platform conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Loops account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Loops tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Find a contact by email address")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                          | Description                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| **List Mailing Lists**        | Retrieve all mailing lists with name, description, and privacy settings                                   |
| **Find Contact**              | Find a contact by email address or user ID                                                                |
| **Create Contact**            | Create a new contact with email and optional properties like name, source, and mailing list subscriptions |
| **Update Contact**            | Update or create a contact with new properties (requires email or userId)                                 |
| **Delete Contact**            | Delete a contact by email address or user ID                                                              |
| **List Contact Properties**   | Retrieve contact properties, optionally filtered to custom properties only                                |
| **Send Event**                | Send events to trigger emails in Loops, identified by email or userId                                     |
| **Send Transactional Email**  | Send a transactional email with data variables and optional attachments                                   |
| **List Transactional Emails** | Retrieve transactional emails with automatic pagination support                                           |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find a contact:**

```text
Find the contact with email sarah@company.com
```

**Create a contact:**

```text
Create a new contact with email john@startup.io, first name John, last name Doe, and subscribe them to the Product Updates mailing list
```

**Send an event:**

```text
Send a "signup_completed" event for the contact with email new_user@example.com
```

**Send a transactional email:**

```text
Send the welcome email template to alex@business.com with the data variable company_name set to "Acme Inc"
```

**List mailing lists:**

```text
Show me all my mailing lists and their privacy settings
```

#### Troubleshooting

| Issue                 | Solution                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Contact not found     | Verify the email address or userId is correct                                                                                               |
| Action not completing | Check that you've authenticated with your Loops API key                                                                                     |
| 409 Conflict error    | The contact already exists; use Update Contact instead of Create Contact                                                                    |
| Unexpected results    | The agent may chain multiple tools (e.g., finding a contact first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                         |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Subscribe [john@example.com](mailto:john@example.com) to the Newsletter list" will find the contact first, then update their mailing list subscriptions. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Loops MCP server](https://www.gumloop.com/mcp/loops) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Luma

*Manage events, guests, tickets, and calendars on Lu.ma with AI-powered event management.*

**Source:** https://docs.gumloop.com/nodes/mcp/luma

Manage events, guests, tickets, and calendars on Lu.ma with AI-powered event management.

Luma (lu.ma) is an event management platform for hosting in-person and virtual events, managing guest lists, selling tickets, and building community calendars. The Luma MCP server lets you create and manage events, handle guest registrations, configure ticket types, manage memberships, and organize your calendar using natural language.

#### What Can It Do?

* **Create and manage events** with details like location, time, visibility, cover images, and custom URLs
* **Handle guest lists** including adding guests, updating approval status, sending invitations, and filtering by status
* **Configure ticket types** for free or paid events with capacity limits and approval requirements
* **Manage memberships** with tiers, member additions, and status updates
* **Organize your calendar** with event tags, person tags, people lists, coupon management, and contact imports
* **Manage event hosts** with configurable access levels and visibility

#### Where to Use It

##### In Agents (Recommended)

Add Luma as a tool to any agent. The agent can manage your events and calendar conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Luma API key

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Luma tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a new event on my Luma calendar")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Event Management

| Tool                   | Description                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **List Events**        | List events from your calendar with date filtering and sorting, or look up a specific event by API ID or URL                |
| **Get Event**          | Get full details of a specific event including its hosts                                                                    |
| **Create Event**       | Create a new event with name, time, timezone, description, location, visibility, cover image, custom URL slug, and capacity |
| **Update Event**       | Update any event property with an option to suppress notifications                                                          |
| **Manage Event Hosts** | Add a host to an event with configurable access level (none, check-in, manager) and visibility                              |

##### Guest Management

| Tool                    | Description                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Get Guests**          | List guests for an event with filtering by approval status and sorting, or look up a specific guest by ID or email |
| **Add Guests**          | Add guests to an event with optional ticket type assignment                                                        |
| **Update Guest Status** | Approve or decline a guest with optional refund                                                                    |
| **Send Invites**        | Send event invitations to a list of guests with an optional custom message (max 200 characters)                    |

##### Calendar & People

| Tool                   | Description                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| **List People**        | List people from your calendar with search, tag filtering, membership tier filtering, and sorting |
| **Import People**      | Bulk import people to your calendar by email and name                                             |
| **Manage Event Tags**  | List, create, update, delete, apply, or remove event tags                                         |
| **Manage Person Tags** | List, create, update, delete, apply, or remove person tags                                        |

##### Tickets & Memberships

| Tool                    | Description                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manage Ticket Types** | List, get, create, update, or delete ticket types for an event. Supports free and paid tickets with pricing, capacity, approval settings, and visibility |
| **Manage Memberships**  | List membership tiers, add members, or update member status (approve/decline) with optional payment skip                                                 |
| **Manage Coupons**      | List, create, or update discount coupons for events or the calendar. Supports percentage and fixed-amount discounts                                      |

##### System

| Tool         | Description                                  |
| ------------ | -------------------------------------------- |
| **Get User** | Get the current authenticated user's profile |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create an event:**

```text
Create a public event called "AI Workshop" on March 15th at 2pm EST in New York with a max capacity of 50
```

**Manage guests:**

```text
Show me all pending guests for my latest event and approve them
```

**Send invitations:**

```text
Send invitations to alice@example.com and bob@example.com for my AI Workshop event
```

**Set up tickets:**

```text
Create a paid ticket type called "Early Bird" for $25 USD with a capacity of 20 for my workshop event
```

**Manage your calendar:**

```text
List all people tagged as "VIP" in my calendar
```

**Create a coupon:**

```text
Create a 20% off coupon code "EARLYBIRD" for my workshop event
```

#### Troubleshooting

| Issue                    | Solution                                                                                                                                           |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication failed    | Verify your Luma API key is connected and valid. You can generate an API key from your Luma account settings.                                      |
| Event not found          | Use the event API ID or the full lu.ma URL for lookups                                                                                             |
| Guest operations failing | Ensure you're using the correct event API ID (not the event ID) for guest management                                                               |
| Cover image rejected     | Cover image URLs must be Luma CDN URLs (`https://images.lumacdn.com/...`). Upload images through Luma first.                                       |
| Tool not available       | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |
| Unexpected results       | The agent may chain multiple tools (e.g., finding the event first, then managing guests). Review the agent's reasoning to understand its approach. |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Approve all pending guests for my workshop" will list events, find the right one, get pending guests, then approve each one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Luma MCP server](https://www.gumloop.com/mcp/luma) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Microsoft Teams

*Manage teams, channels, and meetings with AI-powered collaboration automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/microsoft_teams

Manage teams, channels, and meetings with AI-powered collaboration automation.

Microsoft Teams is Microsoft's collaboration platform for chat, meetings, and teamwork. The Microsoft Teams MCP server lets you create channels, send messages, manage meetings, and work with members using natural language.

> **Info:** Looking to deploy an agent **inside** a Teams channel so your team can @mention it? See [Using Agents in Microsoft Teams](https://docs.gumloop.com/core-concepts/agents_teams). This page covers the MCP integration that lets agents **use** Teams as a tool.

#### What Can It Do?

* **List and create teams and channels** for your organization
* **Send and retrieve messages** in chats and channels
* **Manage team membership** by adding or removing users
* **Schedule, update, and cancel meetings** automatically

#### Where to Use It

##### In Agents (Recommended)

Add Microsoft Teams as a tool to any agent. The agent can then manage your Teams workspace conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Microsoft Teams tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Send a message to the General channel")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                           | Description                  |
| ------------------------------ | ---------------------------- |
| **Get Teams**                  | List all teams you belong to |
| **Get Team Details**           | Fetch details of a team      |
| **Get Team Channels**          | List channels in a team      |
| **Create Team Channel**        | Create a new channel         |
| **Get Direct Messages**        | List your direct chats       |
| **Get Direct Message History** | Get chat message history     |
| **Send Direct Message**        | Send a direct message        |
| **Get Team Channel Messages**  | Get channel messages         |
| **Send Team Channel Message**  | Post a channel message       |
| **Post Message Reply**         | Reply to a message           |
| **Get Team Members**           | List team members            |
| **Add Team Member**            | Add a user to a team         |
| **Create Meeting**             | Schedule a new meeting       |
| **List Meetings**              | List upcoming meetings       |
| **Update Meeting**             | Modify a meeting             |
| **Delete Meeting**             | Cancel a meeting             |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List channels:**

```text
Show me all channels in the Marketing team
```

**Send a message:**

```text
Post "Sprint review at 2pm" to the Announcements channel in Product team
```

**Add a member:**

```text
Add sarah@company.com to the Engineering team
```

**Schedule a meeting:**

```text
Create a Teams meeting called "Q3 Planning" for tomorrow at 10am with john@company.com
```

**Check messages:**

```text
Get the latest messages from the Support channel
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use exact team and channel names                                                                                                        |
| Action not completing            | Check that you've authenticated with Microsoft 365                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a team first, then posting). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                     |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Post to the Marketing Announcements channel" will find the team and channel first, then post. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Microsoft Teams MCP server](https://www.gumloop.com/mcp/teams) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Microsoft Word

*Manage Word documents with AI-powered document automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/microsoft_word

Manage Word documents with AI-powered document automation.

Microsoft Word is part of Microsoft 365 for document creation and editing. The Microsoft Word MCP server lets you list, search, read, edit, and download Word documents from OneDrive using natural language.

#### What Can It Do?

* **List and search documents** across your OneDrive
* **Read document contents** for analysis or processing
* **Create and edit documents** with new content
* **Generate download links** for sharing

#### Where to Use It

##### In Agents (Recommended)

Add Microsoft Word as a tool to any agent. The agent can then manage your documents conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Microsoft Word tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Read the contents of the project charter")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                  | Description                       |
| --------------------- | --------------------------------- |
| **List Documents**    | List Word documents from OneDrive |
| **Create Document**   | Create a new Word document        |
| **Read Document**     | Get the full text of a document   |
| **Write Document**    | Append text to a document         |
| **Search Documents**  | Find documents by keyword         |
| **Download Document** | Get a download URL                |
| **Delete Document**   | Remove a document                 |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List documents:**

```text
Show me all Word documents in the Proposals folder
```

**Read content:**

```text
Read the contents of the Annual Report 2024 document
```

**Create a document:**

```text
Create a new document called "Meeting Notes" with the text "Q3 Planning Session"
```

**Search documents:**

```text
Find documents containing "budget forecast"
```

**Get download link:**

```text
Generate a download link for the Contract Final Version document
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                           |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use exact document names or folder paths                                                                                           |
| Action not completing            | Check that you've authenticated with Microsoft 365                                                                                 |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then reading). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Read the latest proposal" will search for it first, then read the contents. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Microsoft Word MCP server](https://www.gumloop.com/mcp/word) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Monday

*Manage boards, items, and projects with AI-powered work management automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/monday

Manage boards, items, and projects with AI-powered work management automation.

Monday.com is a work operating system for managing projects and workflows. The Monday MCP server lets you create boards, manage items, update columns, and track work using natural language.

#### What Can It Do?

* **Create and manage boards** for teams or projects
* **Add and update items** with statuses and due dates
* **Organize with groups** and subitems
* **Post updates** and track collaboration

#### Where to Use It

##### In Agents (Recommended)

Add Monday as a tool to any agent. The agent can then manage your work conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Monday tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create an item in the Sprint board")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description               |
| ----------------------- | ------------------------- |
| **Get Boards**          | Get all accessible boards |
| **Get Board**           | Get a specific board      |
| **Create Board**        | Create a new board        |
| **Create Item**         | Create a new item         |
| **Get Item**            | Get item details          |
| **Update Item**         | Update item properties    |
| **Delete Item**         | Delete an item            |
| **Search Items**        | Search items with filters |
| **Change Column Value** | Update a column value     |
| **Create Group**        | Create a new group        |
| **Create Subitem**      | Create a subitem          |
| **Get Updates**         | Get item comments         |
| **Create Update**       | Post a comment            |
| **Archive Item**        | Archive an item           |
| **Archive Board**       | Archive a board           |

#### Example Prompts

Use these with your agent or in the Agent Node:

**View boards:**

```text
Show me all my Monday boards
```

**Create an item:**

```text
Create an item called "Website Launch" in the Marketing board
```

**Update status:**

```text
Set the status to "Done" for the API Integration task
```

**Search items:**

```text
Find all high-priority items in the Sprint board
```

**Add a comment:**

```text
Post an update "Meeting moved to Thursday" on the Client Presentation item
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific board and item names                                                                                                                 |
| Action not completing            | Check that you've authenticated with Monday.com                                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a board first, then creating an item). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a task in the Sprint board" will find the board first, then create the item. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Monday MCP server](https://www.gumloop.com/mcp/monday) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### NetSuite

*Manage ERP data with AI-powered business automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/netsuite

Manage ERP data with AI-powered business automation.

NetSuite is Oracle's cloud-based ERP platform for business management. The NetSuite MCP server lets you query records, run SuiteQL, and manage customers, invoices, and orders using natural language.

#### What Can It Do?

* **List and query records** like customers, invoices, and sales orders
* **Run SuiteQL queries** for advanced data retrieval
* **Create and update records** across your organization
* **Inspect schemas** to understand available fields

#### Where to Use It

##### In Agents (Recommended)

Add NetSuite as a tool to any agent. The agent can then manage your ERP data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with NetSuite tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List customers with name containing Acme")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                  | Description                    |
| --------------------- | ------------------------------ |
| **List Record**       | List records with filtering    |
| **Get Record**        | Get a single record by ID      |
| **Create Record**     | Create new records             |
| **Update Record**     | Update existing records        |
| **Delete Record**     | Delete records                 |
| **Run SuiteQL Query** | Execute SuiteQL queries        |
| **Get Record Schema** | Get schema for any record type |

#### Setting Up Credentials

NetSuite uses OAuth 2.0 for authentication. See the [NetSuite OAuth Configuration Guide](https://docs.gumloop.com/nodes/integrations/netsuite-oauth-config) for detailed setup instructions.

#### Example Prompts

Use these with your agent or in the Agent Node:

**List customers:**

```text
Show me all customers with name containing "Tech"
```

**Get order details:**

```text
Get the details for sales order 12345
```

**Run a query:**

```text
Run SuiteQL: SELECT id, companyName FROM customer WHERE companyName LIKE '%Corp%'
```

**Create a record:**

```text
Create a customer with name "Acme Corp" and email "info@acme.com"
```

**Check schema:**

```text
What fields are available on the invoice record?
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific record IDs or exact names                                                                                              |
| Action not completing            | Check that you've authenticated with NetSuite                                                                                       |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |
| Authentication errors            | Verify your OAuth connection and role permissions                                                                                   |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the Acme customer phone number" will find the customer first, then update. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* [NetSuite OAuth Configuration Guide](https://docs.gumloop.com/nodes/integrations/netsuite-oauth-config) for setup
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [NetSuite MCP server](https://www.gumloop.com/mcp/netsuite) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Notion

*Search and query your workspace with AI-powered knowledge management automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/notion

Search and query your workspace with AI-powered knowledge management automation.

Notion is an all-in-one workspace for notes, databases, and collaboration. The Notion MCP server lets you search, create, update, and query pages and databases using natural language.

#### What Can It Do?

* **Search pages** by keyword across your workspace
* **Create and update pages** as sub-pages or database entries with markdown content
* **Create and update databases** with custom property schemas
* **Query databases** with filters to get specific rows
* **Manage data sources** within databases (list, inspect, and update schemas)
* **Retrieve page content** including blocks and properties
* **List users and databases** for workspace discovery
* **Comment on pages and blocks** with threaded discussions
* **Manipulate blocks** by appending, updating, or deleting content

#### Where to Use It

##### In Agents (Recommended)

Add Notion as a tool to any agent. The agent can then search and retrieve your Notion data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Notion tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for pages containing 'roadmap'")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Read Tools

| Tool                   | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Search Pages**       | Search all pages by keyword (supports pagination for large result sets)         |
| **List All Pages**     | List pages across databases                                                     |
| **Get Page**           | Retrieve a page by ID or URL                                                    |
| **List Databases**     | List all databases                                                              |
| **Get Database**       | Get database properties and schema                                              |
| **Query Database**     | Query with filters                                                              |
| **Get Block Children** | List content blocks                                                             |
| **Get Block**          | Get a single block                                                              |
| **List All Users**     | List workspace users                                                            |
| **Get User**           | Get user details                                                                |
| **List Data Sources**  | List all data sources under a database, each with its own schema and properties |
| **Get Data Source**    | Retrieve a specific data source by ID to inspect its schema                     |
| **List Comments**      | List comments on a page or block                                                |

##### Write Tools

| Tool                   | Description                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------ |
| **Create Page**        | Create a new page as a sub-page or database entry with properties, markdown content, or block children |
| **Update Page**        | Update page properties, title, icon, cover, or archive/trash status                                    |
| **Create Database**    | Create a new database with custom property schema under an existing page                               |
| **Update Database**    | Update database title, description, icon, cover, or trash/lock status                                  |
| **Update Data Source** | Update a data source's property schema, title, description, icon, or trash status                      |
| **Create Comment**     | Create a comment on a page, block, or reply to an existing discussion thread                           |
| **Append Blocks**      | Append child blocks to a page or block (supports up to 100 blocks and two levels of nesting)           |
| **Update Block**       | Update an existing block's content (paragraph text, to-do status, callout icons, etc.)                 |
| **Delete Block**       | Archive (soft-delete) a block by ID                                                                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search pages:**

```text
Find pages containing "product roadmap"
```

**Query a database:**

```text
Get all tasks from the Sprint database where status is "In Progress"
```

**Get page content:**

```text
What's in the Q4 Planning page?
```

**List databases:**

```text
Show me all databases in my Notion workspace
```

**Check database schema:**

```text
What properties does the Projects database have?
```

**Create a page:**

```text
Create a new page called "Meeting Notes" under the Team Wiki page with today's meeting agenda in markdown
```

**Create a database entry:**

```text
Add a new task to the Sprint database with title "Fix login bug", status "In Progress", and priority "High"
```

**Create a database:**

```text
Create a new database called "Project Tracker" with columns for Name, Status, Priority, Due Date, and Assignee
```

**Update a page:**

```text
Archive the Q3 Planning page and remove its cover image
```

**List data sources:**

```text
List all data sources under the Projects database and show their schemas
```

**Update a data source schema:**

```text
Add a "Priority" select column with options High, Medium, and Low to this data source
```

**Add a comment:**

```text
Add a comment saying "Looks good to me!" on the Q4 Planning page
```

**List comments:**

```text
Show me all comments on the Product Roadmap page
```

**Append blocks:**

```text
Add a callout block with a lightbulb emoji and text "Remember to update the timeline" to the Sprint Planning page
```

**Update a block:**

```text
Mark the first to-do item as completed on my Tasks page
```

**Delete a block:**

```text
Remove the outdated note block from the Meeting Notes page
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific page titles or database names                                                                                                 |
| Action not completing            | Check that you've authenticated and the page is shared with the integration                                                                |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then getting content). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the meeting notes from last week" will search first, then retrieve the content. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Notion MCP server](https://www.gumloop.com/mcp/notion) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Outlook

*Manage email with AI-powered inbox automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/outlook

Manage email with AI-powered inbox automation.

Microsoft Outlook is Microsoft's email and calendar service. The Outlook MCP server lets you read, send, organize, and manage emails using natural language.

#### What Can It Do?

* **Read and search emails** by sender, subject, or date
* **Send and forward emails** without opening Outlook
* **Create drafts** for later review
* **Archive or delete emails** to keep your inbox organized

#### Where to Use It

##### In Agents (Recommended)

Add Outlook as a tool to any agent. The agent can then manage your email conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Outlook tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Read unread emails from today")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool              | Description                                                                         |
| ----------------- | ----------------------------------------------------------------------------------- |
| **Read Emails**   | Fetch emails with filters                                                           |
| **Send Email**    | Send a new email, or send an existing draft by ID                                   |
| **Update Email**  | Change read/unread or flagged status                                                |
| **Create Draft**  | Create a new draft, or create a threaded reply/reply-all draft to an existing email |
| **Forward Email** | Forward an email                                                                    |
| **Archive Email** | Move to Archive folder                                                              |
| **Trash Email**   | Move to Deleted Items                                                               |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Read emails:**

```text
Show me unread emails from this week
```

**Send an email:**

```text
Send an email to john@company.com with subject "Project Update" and body "Here's the latest status..."
```

**Create a draft:**

```text
Create a draft to the sales team about the Q4 forecast
```

**Reply as a threaded draft:**

```text
Create a reply-all draft to the latest email from John with the message "Thanks, will review today"
```

**Send an existing draft:**

```text
Send the draft I just created
```

**Archive emails:**

```text
Archive all newsletters older than 30 days
```

**Forward an email:**

```text
Forward the budget approval email to sarah@company.com
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific sender emails or subject lines                                                                                           |
| Action not completing            | Check that you've authenticated with Microsoft 365                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then forwarding). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                   |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Forward the latest email from John" will find the email first, then forward it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Outlook MCP server](https://www.gumloop.com/mcp/outlook) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Outlook Calendar

*Manage calendar events and check availability with AI-powered scheduling automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/outlook_calendar

Manage calendar events and check availability with AI-powered scheduling automation.

Microsoft Outlook Calendar is Microsoft's scheduling and calendar service. The Outlook Calendar MCP server lets you view, create, update, and manage calendar events using natural language.

#### What Can It Do?

* **List calendars** and browse events across time ranges
* **Create and update events** with attendees, locations, and Teams meetings
* **Delete events** to keep your schedule clean
* **Check availability** for one or more users to find free time slots

#### Where to Use It

##### In Agents (Recommended)

Add Outlook Calendar as a tool to any agent. The agent can then manage your calendar conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Outlook Calendar tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List my events for this week")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| **List Calendars**     | List all calendars for the authenticated user                          |
| **List Events**        | List events from a calendar for a specified time range                 |
| **Get Event**          | Get details of a specific calendar event                               |
| **Create Event**       | Create a new event with attendees, location, and Teams meeting support |
| **Update Event**       | Update an existing calendar event                                      |
| **Delete Event**       | Delete an event from a calendar                                        |
| **Check Availability** | Check free/busy availability for one or more users                     |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List events:**

```text
Show me my calendar events for this week
```

**Create an event:**

```text
Schedule a team meeting tomorrow at 2pm for 1 hour with john@company.com and jane@company.com, include a Teams link
```

**Check availability:**

```text
Check when john@company.com and jane@company.com are both free this Thursday afternoon
```

**Update an event:**

```text
Move my 3pm meeting to 4pm and add a conference room
```

**Delete an event:**

```text
Cancel my meeting with the design team on Friday
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                 |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific event subjects or date ranges                                                                                               |
| Action not completing            | Check that you've authenticated with Microsoft 365                                                                                       |
| Unexpected results               | The agent may chain multiple tools (e.g., listing events first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                      |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Reschedule my meeting with John to next week" will find the event first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Outlook Calendar MCP server](https://www.gumloop.com/mcp/outlook_calendar) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Outreach

*Manage sales engagement with AI-powered outreach automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/outreach

Manage sales engagement with AI-powered outreach automation.

Outreach is a sales engagement platform that helps revenue teams manage prospects, sequences, emails, and tasks. The Outreach MCP server lets you manage your entire sales engagement workflow using natural language.

#### What Can It Do?

* **Manage prospects** — list, create, update, and delete prospect records
* **Handle accounts** — create and manage company records
* **Run sequences** — create, activate, and manage multi-step outreach sequences
* **Send emails** — send one-off emails or use templates through connected mailboxes
* **Manage tasks** — create, assign, complete, and track sales tasks
* **Log calls** — record call activities against prospects
* **Track opportunities** — manage sales deals through pipeline stages
* **Monitor engagement** — view email opens, clicks, replies, and other activity events

#### Where to Use It

##### In Agents (Recommended)

Add Outreach as a tool to any agent. The agent can then manage your sales engagement conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Outreach tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Add prospect to outbound sequence")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Prospects

| Tool                     | Description                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **List Prospects**       | List prospects with filtering and pagination support                                                   |
| **Get Prospect**         | Get a single prospect by ID, including contact details and engagement state                            |
| **Create Prospect**      | Create a new prospect with contact details and optional links to an account, owner, stage, and persona |
| **Update Prospect**      | Update an existing prospect's contact details or linked records                                        |
| **Delete Prospect**      | Permanently delete a prospect by ID                                                                    |
| **List Prospect Notes**  | List notes attached to prospects, optionally filtered to a single prospect                             |
| **Create Prospect Note** | Create a note on a prospect                                                                            |

##### Accounts

| Tool                    | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **List Accounts**       | List accounts with filtering and pagination support                      |
| **Get Account**         | Get a single account by ID                                               |
| **Create Account**      | Create a new account (company record)                                    |
| **Update Account**      | Update an existing account                                               |
| **Delete Account**      | Permanently delete an account by ID                                      |
| **List Account Notes**  | List notes attached to accounts, optionally filtered to a single account |
| **Create Account Note** | Create a note on an account                                              |

##### Opportunities

| Tool                        | Description                                                                 |
| --------------------------- | --------------------------------------------------------------------------- |
| **List Opportunities**      | List opportunities (sales deals) with filtering and pagination support      |
| **Get Opportunity**         | Get a single opportunity by ID                                              |
| **Create Opportunity**      | Create a new opportunity, optionally linked to an account, stage, and owner |
| **Update Opportunity**      | Update an existing opportunity                                              |
| **Delete Opportunity**      | Permanently delete an opportunity by ID                                     |
| **List Opportunity Stages** | List opportunity stages (pipeline stages for sales deals)                   |

##### Sequences

| Tool                              | Description                                                                 |
| --------------------------------- | --------------------------------------------------------------------------- |
| **List Sequences**                | List sequences with filtering, sorting, and pagination support              |
| **Get Sequence**                  | Get a single sequence by ID                                                 |
| **Create Sequence**               | Create a new sequence (interval- or date-based)                             |
| **Update Sequence**               | Update an existing sequence's attributes                                    |
| **Update Sequence Status**        | Activate or deactivate a sequence                                           |
| **Delete Sequence**               | Delete a sequence by ID                                                     |
| **List Sequence Steps**           | List sequence steps, optionally filtered by sequence                        |
| **Create Sequence Step**          | Add a step (auto email, manual email, call, or task) to a sequence          |
| **Update Sequence Step**          | Update an existing sequence step                                            |
| **Add Template to Sequence Step** | Attach an email template to a sequence step                                 |
| **Add Prospect to Sequence**      | Add a prospect to a sequence by creating a sequence state                   |
| **List Sequence States**          | List sequence states (prospects in sequences) with filtering and pagination |
| **Get Sequence State**            | Get a single sequence state by ID                                           |
| **Update Sequence State**         | Pause, resume, or finish a prospect's sequence state                        |
| **Remove Prospect from Sequence** | Remove a prospect from a sequence                                           |

##### Emails

| Tool               | Description                                                                         |
| ------------------ | ----------------------------------------------------------------------------------- |
| **List Emails**    | List emails with filtering and pagination, including delivery and engagement state  |
| **Get Email**      | Get a single email by ID, including content, delivery state, and engagement details |
| **Send Email**     | Send a one-off email to a prospect through a connected mailbox                      |
| **List Mailboxes** | List connected email accounts with filtering and pagination                         |

##### Templates & Snippets

| Tool                | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| **List Templates**  | List reusable email templates with filtering and pagination       |
| **Get Template**    | Get a single email template by ID                                 |
| **Create Template** | Create a reusable email template for one-off emails and sequences |
| **Update Template** | Update an existing email template                                 |
| **List Snippets**   | List reusable email snippets with filtering and pagination        |
| **Get Snippet**     | Get a single email snippet by ID                                  |

##### Tasks

| Tool              | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| **List Tasks**    | List tasks with filtering and pagination support           |
| **Get Task**      | Get a single task by ID                                    |
| **Create Task**   | Create a new task, optionally tied to a prospect           |
| **Update Task**   | Update an existing task's action, due date, note, or owner |
| **Complete Task** | Mark a task as complete                                    |
| **Delete Task**   | Delete a task by ID                                        |

##### Calls

| Tool                       | Description                                         |
| -------------------------- | --------------------------------------------------- |
| **List Calls**             | List logged calls with filtering and pagination     |
| **Get Call**               | Get a single logged call by ID                      |
| **Log Call**               | Log a call against a prospect                       |
| **List Call Dispositions** | List call dispositions used to categorize call logs |
| **List Call Purposes**     | List call purposes used to categorize call logs     |

##### Users & Teams

| Tool              | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **List Users**    | List Outreach users (seat holders) with filtering and pagination |
| **Get User**      | Get a single Outreach user by ID                                 |
| **List Teams**    | List teams (groups of users) with filtering and pagination       |
| **List Stages**   | List prospect stages (pipeline categories)                       |
| **List Personas** | List personas (categories describing types of prospects)         |

##### Events

| Tool            | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| **List Events** | List activity events (email opens, clicks, replies) with filtering and pagination |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find prospects:**

```text
List all prospects at acme.com
```

**Add to sequence:**

```text
Add john@acme.com to the "Enterprise Outbound" sequence
```

**Send email:**

```text
Send a follow-up email to the prospect asking about their timeline
```

**Manage tasks:**

```text
Create a task to call the prospect tomorrow at 2pm
```

**Track engagement:**

```text
Show me all email opens and clicks from the last 7 days
```

**Pipeline management:**

```text
Create an opportunity for Acme Corp at $50,000 in the "Proposal" stage
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific emails or prospect IDs                                                                                                                    |
| Action not completing            | Check that you've authenticated with Outreach                                                                                                          |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a prospect first, then adding to sequence). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                    |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add [john@company.com](mailto:john@company.com) to the outbound sequence" will find the prospect first, then add to the sequence. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Outreach MCP server](https://www.gumloop.com/mcp/outreach) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### PagerDuty

*Manage incidents and on-call schedules with AI-powered response automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/pagerduty

Manage incidents and on-call schedules with AI-powered response automation.

PagerDuty is an incident management platform for operational reliability. The PagerDuty MCP server lets you retrieve incidents, manage schedules, and track on-call coverage using natural language.

#### What Can It Do?

* **List and filter incidents** by status or priority
* **Manage on-call schedules** and coverage
* **Get service information** and escalation policies
* **Track notifications** and alert history

#### Where to Use It

##### In Agents (Recommended)

Add PagerDuty as a tool to any agent. The agent can then manage your incident response conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with PagerDuty tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List open incidents")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                  |
| ---------------------- | ---------------------------- |
| **Get User**           | Fetch user details           |
| **List Incidents**     | List incidents with filters  |
| **List Services**      | Get all services             |
| **List Schedules**     | Get all on-call schedules    |
| **Create Schedule**    | Create a new schedule        |
| **Get Schedule**       | Get schedule details         |
| **Delete Schedule**    | Remove a schedule            |
| **List Oncalls**       | List current on-call entries |
| **List Notifications** | List recent notifications    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check incidents:**

```text
Show me all open incidents
```

**On-call coverage:**

```text
Who is on call for the API team right now?
```

**List services:**

```text
Show me all PagerDuty services and their escalation policies
```

**Create a schedule:**

```text
Create an on-call schedule called "Weekend Support" starting next Monday
```

**Check notifications:**

```text
Show me notifications for the last 24 hours
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific schedule or service names                                                                                                               |
| Action not completing            | Check that you've authenticated with PagerDuty                                                                                                       |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a schedule first, then listing on-calls). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                  |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Who is on call for the database schedule?" will find the schedule first, then list on-call entries. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [PagerDuty MCP server](https://www.gumloop.com/mcp/pagerduty) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Parallel

*Search the web and extract content with AI-powered research automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/parallel

Search the web and extract content with AI-powered research automation.

Parallel.ai provides accurate web search, content extraction, and site monitoring. The Parallel MCP server lets you search, extract, and monitor web data using natural language.

#### What Can It Do?

* **Search the web** with high-accuracy results
* **Extract clean content** from any URL
* **Monitor websites** for changes and updates
* **Run task automation** with structured outputs

#### Where to Use It

##### In Agents (Recommended)

Add Parallel as a tool to any agent. The agent can then search and extract web data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Parallel tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search the web for AI news")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                   |
| --------------------------- | --------------------------------------------- |
| **Extract**                 | Extract content from web URLs                 |
| **Search**                  | Search the web for results                    |
| **List Monitors**           | List active web monitors                      |
| **Create Monitor**          | Create a new web monitor                      |
| **Get Monitor**             | Get monitor details                           |
| **Update Monitor**          | Update an existing monitor                    |
| **Delete Monitor**          | Delete a monitor                              |
| **List Monitor Events**     | List events for a monitor                     |
| **Get Monitor Event Group** | Retrieve a specific event group for a monitor |
| **Create Task Run**         | Start a new task run                          |
| **Get Task Run**            | Get task run status                           |
| **Get Task Run Result**     | Get completed task results                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search the web:**

```text
Search for "AI startup funding 2025" and return the top 5 results
```

**Extract content:**

```text
Extract the main content from this URL: https://example.com/article
```

**Create a monitor:**

```text
Create a monitor to track changes on this competitor's pricing page
```

**Check monitor events:**

```text
What changes were detected on my monitors this week?
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Be more specific with search queries                                                                                                  |
| Action not completing            | Check that you've authenticated with Parallel                                                                                         |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then extracting). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                   |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Find and extract the top article about AI" will search first, then extract content. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Parallel MCP server](https://www.gumloop.com/mcp/parallel) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Pipedrive

*Manage your sales pipeline with AI-powered CRM automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/pipedrive

Manage your sales pipeline with AI-powered CRM automation.

Pipedrive is a sales CRM designed to help teams manage deals and close more business. The Pipedrive MCP server lets you manage deals, contacts, organizations, activities, and more using natural language.

#### What Can It Do?

* **Manage deals** through your sales pipeline
* **Create and update contacts** and organizations
* **Schedule activities** and tasks
* **Track email threads** and communications
* **Manage projects** and notes

#### Where to Use It

##### In Agents (Recommended)

Add Pipedrive as a tool to any agent. The agent can then manage your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Pipedrive tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a deal for Acme Corp")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                     | Description                 |
| ------------------------ | --------------------------- |
| **List Deals**           | Get deals with filtering    |
| **Search Deals**         | Search deals by title       |
| **Create Deal**          | Create a new deal           |
| **Update Deal**          | Update deal properties      |
| **Delete Deal**          | Delete a deal               |
| **Search Organizations** | Search organizations        |
| **Create Organization**  | Create an organization      |
| **Update Organization**  | Update organization details |
| **List Persons**         | List contacts               |
| **Search Persons**       | Search contacts             |
| **Create Person**        | Create a contact            |
| **Update Person**        | Update contact details      |
| **List Activities**      | Get activities              |
| **Create Activity**      | Schedule an activity        |
| **Get Mail Threads**     | List email threads          |
| **Create Note**          | Add a note to a record      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find deals:**

```text
Show me all open deals over $50,000
```

**Create a deal:**

```text
Create a deal called "Enterprise License" for $75,000 linked to Acme Corp
```

**Search contacts:**

```text
Find the contact with email john@company.com
```

**Schedule activity:**

```text
Schedule a call with the Acme team for tomorrow at 2pm
```

**Add a note:**

```text
Add a note to the Acme deal saying "Meeting went well, following up next week"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific deal titles or contact emails                                                                                                               |
| Action not completing            | Check that you've authenticated with Pipedrive                                                                                                           |
| Unexpected results               | The agent may chain multiple tools (e.g., finding an organization first, then creating a deal). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                      |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Create a deal for Acme Corp" will find the organization first, then create the deal. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Pipedrive MCP server](https://www.gumloop.com/mcp/pipedrive) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### PostgreSQL

*Query and manage PostgreSQL databases with AI-powered schema exploration and SQL execution.*

**Source:** https://docs.gumloop.com/nodes/mcp/postgresql

Query and manage PostgreSQL databases with AI-powered schema exploration and SQL execution.

PostgreSQL is a powerful open-source relational database. The PostgreSQL MCP server lets you explore schemas, execute SQL queries, and analyze query plans using natural language.

#### What Can It Do?

* **Explore database schemas** and table structures
* **Execute SQL queries** and view results
* **Analyze query performance** with execution plans
* **Browse tables, views, and sequences** across schemas

#### Where to Use It

##### In Agents (Recommended)

Add PostgreSQL as a tool to any agent. The agent can then interact with PostgreSQL conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with PostgreSQL tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all tables in the database")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **List Schemas**       | List all schemas with their owners                                   |
| **List Objects**       | List tables, views, sequences, or extensions in a schema             |
| **Get Object Details** | Get detailed information about a table, view, sequence, or extension |
| **Execute Sql**        | Execute any SQL query and return results                             |
| **Explain Query**      | Show query execution plan with costs and strategy                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Explore schema:**

```text
List all tables in the public schema
```

**Run a query:**

```text
Show me the top 10 customers by order count
```

**Analyze performance:**

```text
Explain the query plan for selecting from the orders table
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your PostgreSQL credentials and that you have the required permissions                                       |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [PostgreSQL MCP server](https://www.gumloop.com/mcp/postgresql) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Pylon

*Manage your Pylon support issues, accounts, and contacts.*

**Source:** https://docs.gumloop.com/nodes/mcp/pylon

Manage your Pylon support issues, accounts, and contacts.

Pylon is a B2B customer support platform built for modern SaaS teams. The Pylon MCP server lets you manage support issues, accounts, and contacts using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Pylon. Authentication uses OAuth — just connect your Pylon account and start using it immediately.

#### What Can It Do?

* **Manage support issues** and track their status
* **View and update accounts** and customer information
* **Search contacts** and communication history

#### Where to Use It

##### In Agents (Recommended)

Add Pylon as a tool to any agent. The agent can then manage your support operations conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Pylon account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Pylon tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Pylon uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Pylon to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**View issues:**

```text
Show me all open support issues for Acme Corp
```

**Update a ticket:**

```text
Mark issue #456 as resolved with a note about the fix
```

**Search contacts:**

```text
Find all contacts at company "TechStart Inc"
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have access to your Pylon workspace                                                                      |
| Issues not loading | Check that your account has the required permissions                                                                |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### QuickBooks

*Manage accounting, invoices, customers, and financial reports with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/quickbooks

Manage accounting, invoices, customers, and financial reports with AI-powered automation.

QuickBooks Online is Intuit's cloud-based accounting platform used by millions of small and mid-sized businesses. The QuickBooks MCP server lets you manage invoices, customers, vendors, payments, bills, and financial reports using natural language.

#### What Can It Do?

* **Manage invoices** — create, update, send, void, and delete invoices
* **Track customers and vendors** — create and update contact records
* **Record payments and bills** — log customer payments, vendor bills, and bill payments
* **Generate financial reports** — Profit & Loss, Balance Sheet, Cash Flow, Trial Balance, and more
* **Query any entity** — use SQL-like syntax to list and filter any QuickBooks object

#### Where to Use It

##### In Agents (Recommended)

Add QuickBooks as a tool to any agent. The agent can then manage your accounting data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your QuickBooks account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with QuickBooks tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create an invoice for a customer")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Querying

| Tool              | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| **Execute Query** | Run a SQL-like query to list and filter any QuickBooks entity |

##### Invoices

| Tool               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| **Get Invoice**    | Retrieve a single invoice by ID                           |
| **Create Invoice** | Create a new invoice for a customer with line items       |
| **Update Invoice** | Update an existing invoice                                |
| **Delete Invoice** | Delete an invoice                                         |
| **Void Invoice**   | Void an invoice (keeps the record but zeroes the balance) |
| **Send Invoice**   | Send an invoice via email to the customer                 |

##### Customers

| Tool                | Description                  |
| ------------------- | ---------------------------- |
| **Get Customer**    | Retrieve a customer by ID    |
| **Create Customer** | Create a new customer record |
| **Update Customer** | Update an existing customer  |

##### Vendors

| Tool              | Description                |
| ----------------- | -------------------------- |
| **Get Vendor**    | Retrieve a vendor by ID    |
| **Create Vendor** | Create a new vendor record |
| **Update Vendor** | Update an existing vendor  |

##### Payments

| Tool                    | Description                                |
| ----------------------- | ------------------------------------------ |
| **Get Payment**         | Retrieve a customer payment by ID          |
| **Create Payment**      | Record a customer payment against invoices |
| **Delete Payment**      | Void a customer payment                    |
| **Create Bill Payment** | Record a bill payment to a vendor          |

##### Bills

| Tool            | Description                     |
| --------------- | ------------------------------- |
| **Get Bill**    | Retrieve a vendor bill by ID    |
| **Create Bill** | Create a new bill from a vendor |
| **Update Bill** | Update an existing bill         |

##### Estimates

| Tool                | Description                                |
| ------------------- | ------------------------------------------ |
| **Get Estimate**    | Retrieve an estimate by ID                 |
| **Create Estimate** | Create a new estimate/quote for a customer |
| **Update Estimate** | Update an existing estimate                |

##### Items (Products & Services)

| Tool            | Description                              |
| --------------- | ---------------------------------------- |
| **Get Item**    | Retrieve a product or service item by ID |
| **Create Item** | Create a new product or service item     |
| **Update Item** | Update an existing item                  |

##### Accounts (Chart of Accounts)

| Tool               | Description                                   |
| ------------------ | --------------------------------------------- |
| **Get Account**    | Retrieve an account by ID                     |
| **Create Account** | Create a new account in the chart of accounts |
| **Update Account** | Update an existing account                    |

##### Employees

| Tool                | Description                                     |
| ------------------- | ----------------------------------------------- |
| **Get Employee**    | Retrieve an employee by ID                      |
| **Create Employee** | Create a new employee record                    |
| **Update Employee** | Update an existing employee using sparse update |

##### Journal Entries

| Tool                     | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **Get Journal Entry**    | Retrieve a journal entry by ID                     |
| **Create Journal Entry** | Create a new journal entry with debit/credit lines |

##### Sales Receipts & Credit Memos

| Tool                     | Description                            |
| ------------------------ | -------------------------------------- |
| **Get Sales Receipt**    | Retrieve a sales receipt by ID         |
| **Create Sales Receipt** | Create a new sales receipt (cash sale) |
| **Get Credit Memo**      | Retrieve a credit memo by ID           |
| **Create Credit Memo**   | Create a credit memo for a customer    |

##### Vendor Credits & Purchases

| Tool                     | Description                       |
| ------------------------ | --------------------------------- |
| **Get Vendor Credit**    | Retrieve a vendor credit by ID    |
| **Create Vendor Credit** | Create a vendor credit            |
| **Get Purchase**         | Retrieve a purchase/expense by ID |
| **Get Purchase Order**   | Retrieve a purchase order by ID   |

##### Time Activities

| Tool                     | Description                          |
| ------------------------ | ------------------------------------ |
| **Get Time Activity**    | Retrieve a time tracking entry by ID |
| **Create Time Activity** | Log a new time tracking entry        |
| **Update Time Activity** | Update an existing time activity     |

##### Financial Reports

| Tool                            | Description                                 |
| ------------------------------- | ------------------------------------------- |
| **Get Profit And Loss Report**  | Run a Profit & Loss report for a date range |
| **Get Balance Sheet Report**    | Run a Balance Sheet report as of a date     |
| **Get Cash Flow Report**        | Run a Statement of Cash Flows report        |
| **Get Trial Balance Report**    | Run a Trial Balance report as of a date     |
| **Get Aged Receivables Report** | Run an Aged Receivables report              |
| **Get Aged Payables Report**    | Run an Aged Payables report                 |
| **Get General Ledger Report**   | Run a General Ledger report                 |

##### Company Info

| Tool                 | Description                               |
| -------------------- | ----------------------------------------- |
| **Get Company Info** | Retrieve connected company information    |
| **Get Preferences**  | Retrieve company preferences and settings |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Create an invoice:**

```text
Create an invoice for customer John Smith for 5 hours of consulting at $150/hour
```

**Check outstanding receivables:**

```text
Run an aged receivables report and show me anything overdue by more than 30 days
```

**Record a payment:**

```text
Record a $750 payment from Acme Corp against invoice INV-1042
```

**Get financial overview:**

```text
Show me the Profit & Loss report for Q1 2026
```

**Find a customer:**

```text
Find all invoices for customers in California with a balance over $1000
```

#### Troubleshooting

| Issue                  | Solution                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failing | Ensure you've connected your QuickBooks Online account (not Desktop)                                                |
| Entity not found       | Use `Execute Query` to search for the correct ID first                                                              |
| Action not completing  | Check that you've authenticated with the correct QuickBooks company                                                 |
| Tool not available     | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** Use `Execute Query` with SQL-like syntax to find IDs before performing updates or deletes. For example: `SELECT * FROM Customer WHERE DisplayName LIKE 'Acme%'`

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [QuickBooks MCP server](https://www.gumloop.com/mcp/quickbooks) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Ramp

*Manage your Ramp cards, spend, bills, and transactions.*

**Source:** https://docs.gumloop.com/nodes/mcp/ramp

Manage your Ramp cards, spend, bills, and transactions.

Ramp is the corporate card and spend management platform that helps businesses control expenses. The Ramp MCP server lets you manage cards, track spending, and handle bills using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Ramp. Authentication uses OAuth — just connect your Ramp account and start using it immediately.

#### What Can It Do?

* **Manage corporate cards** and spending limits
* **Track transactions** and categorize expenses
* **Handle bills** and vendor payments
* **View spend analytics** and budget utilization

#### Where to Use It

##### In Agents (Recommended)

Add Ramp as a tool to any agent. The agent can then manage your corporate spending conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Ramp account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Ramp tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Ramp uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Ramp to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**View transactions:**

```text
Show me all transactions over $500 from this month
```

**Check spending:**

```text
What's our total software spend for Q2?
```

**Manage bills:**

```text
List all pending bills due this week
```

#### Troubleshooting

| Issue                    | Solution                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect           | Ensure you have admin access to your Ramp account                                                                   |
| Transactions not loading | Check that your role has permission to view the requested data                                                      |
| Tool not available       | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Reddit

*Search and engage with Reddit communities using AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/reddit

Search and engage with Reddit communities using AI-powered automation.

Reddit is a social platform with millions of users across 100k+ communities. The Reddit MCP server lets you search subreddits, fetch posts, manage comments, and publish content using natural language.

> **Warning:** **Reddit MCP nodes require you to bring your own Reddit app credentials.** If you only need read-only access, use the [Reddit Scraper](https://docs.gumloop.com/nodes/integrations/reddit_scraper) node instead, which works without credentials. >  >   If you only need to fetch posts, comments, or search subreddits, use the **[Reddit Scraper](https://docs.gumloop.com/nodes/integrations/reddit_scraper)** node instead. It works out of the box without any custom credentials and is easier to set up.

#### What Can It Do?

* **Search subreddits** and discover communities
* **Fetch posts** with full details and comments
* **Create and edit posts** in any subreddit
* **Manage comments** on your posts

#### Where to Use It

##### In Agents (Recommended)

Add Reddit as a tool to any agent. The agent can then interact with Reddit conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Reddit app credentials

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Reddit tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get top posts from r/programming")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Setting Up Credentials

Reddit MCP requires your own Reddit app credentials. See the [Reddit app preferences](https://www.reddit.com/prefs/apps) to create an app, or request [enterprise API access](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164\&tf_14867328473236=api_request_type_enterprise) for high-volume use cases.

#### Available Tools

| Tool                        | Description                      |
| --------------------------- | -------------------------------- |
| **Retrieve Reddit Post**    | Fetch top posts from a subreddit |
| **Get Reddit Post Details** | Get full details of a post       |
| **Create Reddit Post**      | Publish a new post               |
| **Edit Reddit Post**        | Update an existing post          |
| **Delete Reddit Post**      | Remove a post                    |
| **Fetch Post Comments**     | Get comments on a post           |
| **Create Reddit Comment**   | Add a comment                    |
| **Edit Reddit Comment**     | Update a comment                 |
| **Delete Reddit Comment**   | Remove a comment                 |
| **Search Subreddits**       | Find subreddits by name          |
| **Search Posts**            | Search posts across Reddit       |
| **Search Users**            | Find users by profile            |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Get trending posts:**

```text
Get the top 10 hot posts from r/technology
```

**Search subreddits:**

```text
Find subreddits about machine learning
```

**Get post details:**

```text
Get the full details and comments for this Reddit post URL
```

**Search posts:**

```text
Search r/startups for posts about fundraising
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific subreddit names or post URLs                                                                                                  |
| Action not completing            | Check that you've configured Reddit app credentials                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |
| Authentication errors            | Verify your Reddit app credentials in [Connectors page](https://www.gumloop.com/personal/connectors)                                       |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get comments from the top post in r/programming" will fetch posts first, then get comments. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* [Reddit Scraper](https://docs.gumloop.com/nodes/integrations/reddit_scraper) for read-only access without credentials
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Reddit MCP server](https://www.gumloop.com/mcp/reddit) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Reducto

*Parse, extract, split, and edit documents with AI-powered document processing automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/reducto

Parse, extract, split, and edit documents with AI-powered document processing automation.

Reducto is a document processing API that converts complex documents — PDFs, scanned files, and more — into structured, machine-readable content. The Reducto MCP server lets you parse documents, extract structured data, split documents into sections, and fill forms using natural language.

#### What Can It Do?

* **Parse documents** — convert PDFs and other files into structured text, tables, and figures
* **Extract structured data** — pull specific fields from documents using a JSON schema
* **Split documents** — divide a document into logical sections based on descriptions
* **Edit documents** — fill forms or modify documents with natural language instructions
* **Manage jobs** — track, monitor, and cancel document processing jobs

#### Where to Use It

##### In Agents (Recommended)

Add Reducto as a tool to any agent. The agent can then process and extract data from documents conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Reducto API key

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Reducto tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Extract invoice data from a PDF")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                  | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| **Upload Document**   | Upload a file from Gumloop storage to Reducto for processing                 |
| **Download Document** | Download a Reducto result file back to Gumloop storage                       |
| **Parse Document**    | Parse a document into structured content including text, tables, and figures |
| **Extract Data**      | Extract structured data from a document using a JSON schema                  |
| **Split Document**    | Split a document into logical sections based on descriptions                 |
| **Edit Document**     | Fill forms or modify a document with natural language instructions           |
| **List Jobs**         | List processing jobs with pagination support                                 |
| **Get Job Status**    | Get the status and result of a processing job                                |
| **Cancel Job**        | Cancel a running processing job                                              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Parse a document:**

```text
Upload and parse the contract PDF, then give me a summary of the key terms
```

**Extract structured data:**

```text
Extract the invoice number, date, line items, and total from this PDF invoice
```

**Split a document:**

```text
Split this 50-page report into sections: Executive Summary, Methodology, Results, and Appendix
```

**Fill a form:**

```text
Fill in the application form with the applicant's name, address, and date of birth from the provided data
```

**Check job status:**

```text
What's the status of my document processing jobs?
```

#### Troubleshooting

| Issue                     | Solution                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Upload failing            | Ensure the file exists in Gumloop storage before uploading                                                          |
| Extraction missing fields | Refine your JSON schema to be more specific about the fields you need                                               |
| Job taking too long       | Use `Get Job Status` to monitor progress; large documents may take longer                                           |
| Tool not available        | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

> **Tip:** For best extraction results, provide a detailed JSON schema that describes exactly what fields you need and their expected data types. The more specific your schema, the more accurate the extraction.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Reducto MCP server](https://www.gumloop.com/mcp/reducto) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Robinhood

*Trade and manage your Robinhood portfolio.*

**Source:** https://docs.gumloop.com/nodes/mcp/robinhood

Trade and manage your Robinhood portfolio.

Robinhood is a commission-free trading platform for stocks, ETFs, options, and crypto. The Robinhood MCP server lets you trade and manage your portfolio using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Robinhood. Authentication uses OAuth — just connect your Robinhood account and start using it immediately.

#### What Can It Do?

* **Trade stocks and ETFs** with market or limit orders
* **Manage your portfolio** and view holdings
* **Check account balances** and buying power
* **View market data** and stock quotes

#### Where to Use It

##### In Agents (Recommended)

Add Robinhood as a tool to any agent. The agent can then manage your portfolio conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Robinhood account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Robinhood tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Robinhood uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Robinhood to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check portfolio:**

```text
Show me my current portfolio holdings and their performance
```

**Place a trade:**

```text
Buy 10 shares of AAPL at market price
```

**View account:**

```text
What's my current buying power?
```

#### Troubleshooting

| Issue               | Solution                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect      | Ensure your Robinhood account is active and in good standing                                                        |
| Trade not executing | Check that you have sufficient buying power and the market is open                                                  |
| Tool not available  | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Rocketlane

*Manage your Rocketlane projects, tasks, and customer onboarding.*

**Source:** https://docs.gumloop.com/nodes/mcp/rocketlane

Manage your Rocketlane projects, tasks, and customer onboarding.

Rocketlane is a customer onboarding and professional services automation platform that helps teams deliver projects on time and create a consistent onboarding experience. The Rocketlane MCP server lets you manage projects, tasks, and customer onboarding workflows using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Rocketlane. Authentication uses OAuth — just connect your Rocketlane account and start using it immediately.

#### What Can It Do?

* **Manage projects** — create, update, and track customer onboarding projects
* **Handle tasks** — assign, update, and complete tasks across projects
* **Track onboarding** — monitor customer onboarding progress and milestones

#### Where to Use It

##### In Agents (Recommended)

Add Rocketlane as a tool to any agent. The agent can then manage your customer onboarding projects conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Rocketlane account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Rocketlane tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Rocketlane uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Rocketlane to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check project status:**

```text
Show me the status of all active onboarding projects
```

**Manage tasks:**

```text
List all overdue tasks across my Rocketlane projects
```

**Track onboarding:**

```text
What's the onboarding progress for Acme Corp?
```

**Create a task:**

```text
Create a task to schedule a kickoff call with the new client
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Rocketlane account with the appropriate permissions                                       |
| Data not loading   | Check that your Rocketlane workspace has projects and tasks configured                                              |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Salesforce

*Manage your CRM with AI-powered Salesforce automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/salesforce

Manage your CRM with AI-powered Salesforce automation.

Salesforce is the world's leading CRM platform for sales, service, and marketing. The Salesforce MCP server lets you query, create, update, and manage any object using natural language.

#### What Can It Do?

* **Query records** with SOQL or SOSL
* **Create, update, and delete** any object
* **Run reports** and pull data for analysis
* **View and manage dashboards** including refreshing, cloning, and updating layouts
* **Manage campaigns** by adding leads and contacts
* **Download files and attachments** from Salesforce to Gumloop storage
* **Convert leads** and create related records
* **Run bulk data jobs** to insert, update, upsert, or delete large record sets asynchronously

#### Where to Use It

##### In Agents (Recommended)

Add Salesforce as a tool to any agent. The agent can then manage your CRM conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Salesforce tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Query accounts in California")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Soql Query**              | Execute SOQL queries                                                                                                           |
| **Sosl Search**             | Search across objects                                                                                                          |
| **Describe Object**         | Get object metadata                                                                                                            |
| **Get Record**              | Retrieve a record by ID                                                                                                        |
| **Create Record**           | Create a new record                                                                                                            |
| **Update Record**           | Update an existing record                                                                                                      |
| **Delete Record**           | Delete a record                                                                                                                |
| **Bulk Ingest Start**       | Start an async bulk insert, update, upsert, or delete job for large record sets                                                |
| **Bulk Ingest Results**     | Get the status and results of an async bulk ingest job                                                                         |
| **Run Report**              | Execute a Salesforce report                                                                                                    |
| **List Reports**            | List available reports                                                                                                         |
| **Add Lead To Campaign**    | Add a lead to a campaign                                                                                                       |
| **Add Contact To Campaign** | Add a contact to a campaign                                                                                                    |
| **Convert Lead**            | Convert lead to account/contact                                                                                                |
| **Get File**                | Download a file or attachment from Salesforce to storage. Supports ContentVersion, ContentDocument, and legacy Attachment IDs. |
| **Create Report**           | Create a new Salesforce report                                                                                                 |
| **Update Report**           | Update an existing report's metadata                                                                                           |
| **Clone Report**            | Clone an existing report                                                                                                       |
| **List Dashboards**         | List recently viewed dashboards                                                                                                |
| **Get Dashboard**           | Retrieve a dashboard's results and component data                                                                              |
| **Create Dashboard**        | Create a new dashboard by cloning an existing one                                                                              |
| **Update Dashboard**        | Update a dashboard's metadata and structure                                                                                    |
| **Manage Dashboard**        | Refresh or delete a dashboard                                                                                                  |
| **Create Note**             | Create a note on a record                                                                                                      |
| **Create File**             | Upload a file                                                                                                                  |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Query records:**

```text
Find the 10 largest accounts in California
```

**Get opportunity details:**

```text
Get the details for opportunity OPP-12345
```

**Create a task:**

```text
Create a follow-up task for the Acme account due next Friday
```

**Update a record:**

```text
Update contact john@acme.com with new phone number 415-555-1234
```

**Run a report:**

```text
Run the Q4 Pipeline report and show me the summary
```

**Create a report:**

```text
Create a new tabular report for accounts in the Technology industry
```

**Clone a report:**

```text
Clone the Q4 Pipeline report and name it Q1 Pipeline
```

**Refresh a dashboard:**

```text
Refresh the "Sales Leaderboard" dashboard and send me the results
```

**Clone a dashboard:**

```text
Create a new dashboard by cloning the "Sales Leaderboard" and name it "Q1 Sales Leaderboard"
```

#### Connecting Gumloop to Salesforce

Gumloop is a **Salesforce Connected App** — it is not listed on the Salesforce AppExchange marketplace. A Salesforce administrator must authorize the connection before users can authenticate.

**Quickest setup:** Have your Salesforce admin visit the [Salesforce Connectors page](https://www.gumloop.com/personal/connectors?provider=salesforce) in Gumloop and complete the OAuth flow. This automatically installs the Gumloop connected app in your Salesforce organization.

If a non-admin user attempts to connect first, the admin will see an approval request in Salesforce under **Setup > Apps > Connected Apps > Manage Connected Apps**.

For full setup instructions, see the [Credentials page — Salesforce Setup](https://docs.gumloop.com/core-concepts/credentials#salesforce-setup-admin-only).

> **Info:** For more details on Salesforce's connected app restrictions, see the [official Salesforce documentation](https://help.salesforce.com/s/articleView?id=005132365\&type=1).

#### Troubleshooting

| Issue                                                              | Solution                                                                                                                           |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| "Administrators need to pre-install the Gumloop application" error | A Salesforce admin must first authorize Gumloop. See [Connecting Gumloop to Salesforce](#connecting-gumloop-to-salesforce) above.  |
| Agent not finding the right data                                   | Use specific record IDs or exact names                                                                                             |
| Action not completing                                              | Check that you've authenticated with Salesforce                                                                                    |
| Unexpected results                                                 | The agent may chain multiple tools (e.g., querying first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available                                                 | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Update the Acme opportunity to Closed Won" will find the opportunity first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Salesforce MCP server](https://www.gumloop.com/mcp/salesforce) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Salesloft

*Manage sales engagement with AI-powered outreach automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/salesloft

Manage sales engagement with AI-powered outreach automation.

Salesloft is a sales engagement platform for SDR and revenue teams. The Salesloft MCP server lets you manage people, accounts, cadences, calls, and conversations using natural language.

#### What Can It Do?

* **Find and manage people** and accounts
* **Add prospects to cadences** and track performance
* **Retrieve calls and emails** for reporting
* **Access AI conversation insights** and recordings

#### Where to Use It

##### In Agents (Recommended)

Add Salesloft as a tool to any agent. The agent can then manage your sales engagement conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Salesloft tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Add person to outbound cadence")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                           | Description              |
| ------------------------------ | ------------------------ |
| **List People**                | List people with filters |
| **Create Person**              | Create a new person      |
| **Get Person**                 | Get person details       |
| **Update Person**              | Update person properties |
| **List Accounts**              | List accounts            |
| **Create Account**             | Create an account        |
| **Get Account**                | Get account details      |
| **List Cadences**              | List cadences            |
| **Get Cadence Stats**          | Get cadence performance  |
| **Create Cadence Membership**  | Add person to cadence    |
| **List Calls**                 | List calls with filters  |
| **Get Conversation**           | Get conversation details |
| **Get Conversation Extensive** | Get AI insights          |
| **List Emails**                | List emails              |
| **Create Note**                | Create a note            |
| **Create Task**                | Create a task            |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find people:**

```text
Search for people with email containing @acme.com
```

**Add to cadence:**

```text
Add this person to the Outbound Q1 cadence
```

**Check cadence stats:**

```text
What are the reply rates for the Enterprise cadence?
```

**Get conversation insights:**

```text
Get the AI summary and action items from this conversation
```

**List recent calls:**

```text
Show me all calls from last week with their dispositions
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific emails or person IDs                                                                                                                   |
| Action not completing            | Check that you've authenticated with Salesloft                                                                                                      |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a person first, then adding to cadence). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add [john@company.com](mailto:john@company.com) to the outbound cadence" will find the person first, then add to cadence. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Salesloft MCP server](https://www.gumloop.com/mcp/salesloft) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Seismic

*Manage your sales enablement content with AI-powered Seismic automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/seismic

Manage your sales enablement content with AI-powered Seismic automation.

Seismic is the leading sales enablement platform for managing, distributing, and tracking content. The Seismic MCP server lets you search content, manage files and folders, create LiveSend links, and access reporting data using natural language.

#### What Can It Do?

* **Search and discover content** across your library with advanced filtering
* **Manage files and folders** including create, update, copy, and delete operations
* **Create LiveSend links** for secure content sharing with recipients
* **Access reporting data** including user activities, content engagement, and AI activities
* **Manage Digital Sales Rooms (DSRs)** for personalized buyer experiences

#### Where to Use It

##### In Agents (Recommended)

Add Seismic as a tool to any agent. The agent can then manage your sales content conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Seismic account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Seismic tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for content about product pricing")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

Seismic uses OAuth 2.0 for authentication. When connecting your Seismic account, you'll need to authorize Gumloop to access your Seismic tenant. The integration requires your Seismic tenant subdomain for authentication.

The following OAuth scopes are requested:

* `seismic.user.view` - View user information
* `seismic.self.view` - View your own profile and favorites
* `seismic.reporting` - Access reporting data
* `seismic.library.manage` - Manage library content
* `seismic.search` - Search content
* `seismic.gen-search` - Use generative search features
* `seismic.delivery` - Create and manage content delivery
* `seismic.engagement.manage` - Manage engagements and DSRs

#### Available Tools

| Tool                         | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| **Search Content**           | Search Seismic content with advanced filtering, sorting, and pagination |
| **Search Generative**        | Get AI-generated answers with source documents from your content        |
| **Search Generative Source** | Get source documents for generative search queries                      |
| **Get File Info**            | Get file information including metadata and custom properties           |
| **Update File Info**         | Update file properties including name, owner, and description           |
| **Download File**            | Download the binary content of a file or specific version               |
| **Copy File**                | Copy a file to any target folder within the same teamsite               |
| **Create Folder**            | Create a new folder inside a given folder                               |
| **Get Folder Info**          | Get folder information and properties                                   |
| **Update Folder Info**       | Update folder properties including name and location                    |
| **Copy Folder**              | Copy a folder and its contents to a target folder                       |
| **List Folder Items**        | Get the list of items in a folder with pagination                       |
| **Delete Item**              | Delete any item type from the teamsite                                  |
| **Get Item Info**            | Get information for any item type                                       |
| **Copy Item**                | Copy any item type to a target folder                                   |
| **List Item Versions**       | Get the list of versions for a given item                               |
| **Search Items**             | Search items using filters such as external ID                          |
| **Create URL**               | Add a new URL to the teamsite with metadata                             |
| **Create LiveSend Link**     | Create a LiveSend link for secure content sharing                       |
| **Get LiveSend Settings**    | Get LiveSend settings including password rules                          |
| **List Delivery Options**    | Get available delivery options including custom integrations            |
| **Get Custom Delivery Form** | Get required inputs for a custom delivery form                          |
| **Deliver Custom Content**   | Deliver content via custom delivery options                             |
| **Create Link Delivery**     | Create a link delivery for a Digital Sales Room                         |
| **Generate LiveSend Link**   | Generate a LiveSend link with contents and recipients                   |
| **List Engagements**         | Get engagement information with advanced filtering                      |
| **List CRM Contexts**        | Get CRM context information with filtering                              |
| **List Users**               | Get list of users with filtering and pagination                         |
| **Get User Details**         | Get detailed information for a specific user                            |
| **Get My Favorites**         | Get your favorite content items                                         |
| **Get My Recents**           | Get your recently accessed content items                                |
| **Get My Teamsites**         | Get your assigned teamsites                                             |
| **Get My Profiles**          | Get content profiles assigned to you                                    |
| **Create DSR**               | Create a new Digital Sales Room                                         |
| **List DSRs**                | Get list of Digital Sales Rooms                                         |
| **Get DSR Details**          | Get comprehensive details for a specific DSR                            |
| **Get DSR Comments**         | Get comments from Digital Sales Rooms                                   |
| **Get Reports**              | Get various types of reporting data                                     |
| **Get Users (Reporting)**    | Get list of users from reporting API                                    |
| **Get Group Members**        | Get details on users who are members of a group                         |
| **Get Groups**               | List all user groups in the platform                                    |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search for content:**

```text
Search for all content items about product pricing updated in the last month
```

**Get file information:**

```text
Get the details for the file with ID abc123 in teamsite xyz
```

**Create a LiveSend link:**

```text
Create a LiveSend link for the Q4 presentation to share with john@company.com
```

**List folder contents:**

```text
Show me all items in the Marketing Materials folder
```

**Get reporting data:**

```text
Get the content activity report for the last 30 days
```

#### Troubleshooting

| Issue                               | Solution                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right content | Use specific search terms and filters                                                                                                      |
| Action not completing               | Check that you've authenticated with Seismic                                                                                               |
| Unexpected results                  | The agent may chain multiple tools (e.g., searching first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available                  | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |
| Teamsite ID required                | Many operations require a teamsite ID - use "Get My Teamsites" first to find available teamsites                                           |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Share the latest pricing deck with the sales team" will search for the content first, then create a LiveSend link. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Seismic MCP server](https://www.gumloop.com/mcp/seismic) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Semrush

*Pull SEO and marketing analytics with AI-powered competitive research automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/semrush

Pull SEO and marketing analytics with AI-powered competitive research automation.

Semrush is a leading SEO and digital marketing platform. The Semrush MCP server lets you analyze domains, research keywords, and audit backlinks using natural language.

#### What Can It Do?

* **Analyze domains** for keywords, traffic, and competitors
* **Research keywords** with volume, difficulty, and SERP data
* **Audit backlinks** and referring domains
* **Compare competitors** by shared or unique keywords

#### Where to Use It

##### In Agents (Recommended)

Add Semrush as a tool to any agent. The agent can then perform SEO research conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Semrush tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get domain keywords for hubspot.com")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                                      | Description                                                                                                                                           | Credits |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Get Domain Rank Report**                | Get SEMrush rank report showing the most popular domains ranked by traffic from Google's top 100 organic search results                               | 4       |
| **Get Domain Overview Data**              | Get overview data across all regional databases showing keyword rankings in both organic and paid search for domains, subdomains, subfolders, or URLs | 5       |
| **Get Winners Losers Report**             | Get changes in keyword rankings, traffic, and budget estimates of the most popular websites showing winners and losers                                | 4       |
| **Get Domain Keywords**                   | Get keywords that bring users to a target via Google's organic or paid search results for domains, subdomains, subfolders, or URLs                    | 3       |
| **Get Domain Ad Copies**                  | Get unique ad copies that appeared when target ranked in Google's paid search results for domains, subdomains, or subfolders                          | 3       |
| **Get Domain Competitors**                | Get domain's competitors in organic or paid search results                                                                                            | 4       |
| **Get Domain Ad History**                 | Get keywords a domain has bid on in the last 12 months and its positions in paid search results                                                       | 4       |
| **Compare Domains By Keywords**           | Compare up to five domains by common keywords, unique keywords, or all keywords                                                                       | 8       |
| **Get Domain Pla Keywords**               | Get keywords that trigger a domain's product listing ads (PLA) in Google's paid search results                                                        | 3       |
| **Get Domain Pla Copies**                 | Get product listing ad (PLA) copies that appeared when domain ranked in Google's paid search results                                                  | 3       |
| **Get Domain Pla Competitors**            | Get domains that compete against the requested domain in Google's paid search results with product listing ads (PLA)                                  | 4       |
| **Get Domain Organic Subdomains**         | Get subdomains of the analyzed domain ranking in Google's top 100 organic search results                                                              | 3       |
| **Get Organic Pages**                     | Get unique pages ranking in Google's top 100 organic search results for domains, subdomains, or subfolders                                            | 3       |
| **Get Keyword Overview**                  | Get keyword overview data for a specific database or across all regional databases including volume, CPC, and competition                             | 5       |
| **Get Keyword Search Results**            | Get domains ranking in Google's organic or paid search results for a keyword                                                                          | 3       |
| **Research Related Keywords**             | Get keyword research data including related keywords, broad match keywords, or question-based keywords                                                | 3       |
| **Get Keyword Ads History**               | Get domains that have bid on a keyword in the last 12 months and their positions                                                                      | 4       |
| **Get Keyword Difficulty Score**          | Get keyword difficulty index to estimate how difficult it would be to rank in Google's top 10 for a keyword                                           | 8       |
| **Get Backlinks Overview**                | Get a summary of backlinks including type, referring domains, and IP addresses for a domain                                                           | 5       |
| **Get Backlinks List**                    | Get a list of backlinks for a domain, root domain, or URL                                                                                             | 3       |
| **Analyze Backlinks Data**                | Get backlinks analysis data including referring domains, IPs, TLD distribution, geographical distribution, or anchor texts                            | 6       |
| **Get Backlinks Pages**                   | Get indexed pages of the queried domain                                                                                                               | 3       |
| **Get Backlinks Competitors**             | Get domains that share a similar backlink profile with the analyzed domain                                                                            | 4       |
| **Get Backlinks Authority Score Profile** | Get distribution of referring domains by Authority Score                                                                                              | 5       |
| **Get Backlinks Categories Profile**      | Get categories that referring domains belong to                                                                                                       | 5       |
| **Get Domain Categories**                 | Get categories that the queried domain belongs to                                                                                                     | 5       |
| **Get Backlinks Historical Data**         | Get monthly historical trends of backlinks and referring domains                                                                                      | 10      |
| **Get Subdomain Competitors**             | Get subdomain's competitors in organic or paid search results                                                                                         | 4       |
| **Get Traffic Summary**                   | Get traffic summary metrics including total visits, unique visitors, pages per visit, and bounce rate for domains                                     | 4       |
| **Get Daily Traffic**                     | Get day-by-day traffic breakdown including visits, traffic sources (direct, organic, paid, social), and engagement metrics                            | 4       |
| **Get Weekly Traffic**                    | Get week-by-week traffic analysis including visits, traffic sources, and engagement metrics for broader trend analysis                                | 4       |
| **Get Traffic Sources**                   | Get detailed traffic sources breakdown by channel (direct, search, social, referral, email, display) and type (organic, paid)                         | 4       |
| **Get Purchase Conversion**               | Get purchase conversion rate showing percentage of sessions ending in a purchase (desktop only, requires Premium API access)                          | 4       |
| **Get Top Pages**                         | Get most popular pages of domains showing which content resonates most with the audience                                                              | 4       |
| **Get Traffic Rank**                      | Get domains sorted by traffic rank to benchmark against competitors and understand relative market position                                           | 4       |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Competitive analysis:**

```text
Who are the top organic competitors for monday.com?
```

**Keyword research:**

```text
Get the search volume and difficulty for "digital nomad visa"
```

**Backlink audit:**

```text
How many backlinks does shopify.com have?
```

**Domain overview:**

```text
Give me an overview of tesla.com's organic and paid traffic
```

**Compare domains:**

```text
Compare shopify.com, wix.com, and bigcommerce.com by unique keywords
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use exact domain names without https\://                                                                                                   |
| Action not completing            | Check that you've authenticated with Semrush                                                                                               |
| Unexpected results               | The agent may chain multiple tools (e.g., getting overview first, then keywords). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Analyze competitor.com's SEO" will gather overview, keywords, and backlinks. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Semrush MCP server](https://www.gumloop.com/mcp/semrush) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Sentry

*Investigate Sentry issues, errors, releases, and performance data.*

**Source:** https://docs.gumloop.com/nodes/mcp/sentry

Investigate Sentry issues, errors, releases, and performance data.

Sentry is the application monitoring platform for error tracking, performance monitoring, and release management. The Sentry MCP server lets you investigate issues, errors, and performance data using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Sentry. Authentication uses OAuth — just connect your Sentry account and start using it immediately.

#### What Can It Do?

* **Investigate issues** and error reports
* **Track errors** with stack traces and context
* **Monitor releases** and their health
* **Analyze performance** data and bottlenecks

#### Where to Use It

##### In Agents (Recommended)

Add Sentry as a tool to any agent. The agent can then investigate errors and performance issues conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Sentry account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Sentry tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Sentry uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Sentry to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Investigate issues:**

```text
Show me the top unresolved issues in the production project
```

**Check errors:**

```text
What's the stack trace for the most frequent error this week?
```

**Monitor releases:**

```text
How is the latest release performing compared to the previous one?
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have member access to your Sentry organization                                                           |
| No issues found    | Check that the correct project is selected                                                                          |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Shopify

*Manage your Shopify store, blog posts, and e-commerce operations with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/shopify

Manage your Shopify store, blog posts, and e-commerce operations with AI-powered automation.

Shopify is a leading e-commerce platform for online stores and retail point-of-sale systems. The Shopify MCP server lets you manage products, orders, customers, inventory, collections, discounts, fulfillment, blog posts, metafields, and more using natural language.

#### What Can It Do?

* **Manage products** — search, create, update, delete products and variants
* **Track inventory** — check levels, adjust quantities, and manage locations
* **Handle orders** — search, view, cancel, close, tag, and edit orders
* **Process refunds and returns** — create refunds and returns on orders
* **Manage customers** — search, create, and update customer records
* **Fulfill orders** — create fulfillments, update tracking, and cancel shipments
* **Organize collections** — create, update, delete collections and manage product groupings
* **Run discounts** — create discount codes, automatic discounts, free shipping, and BXGY deals
* **Manage draft orders** — create, complete, and delete draft orders
* **Track abandoned checkouts** — search and view incomplete carts
* **Update store content** — create and manage online store pages
* **Manage blogs and articles** — create blogs, publish posts, and moderate comments
* **Work with metafields** — get, set, and delete metafields on any resource

#### Where to Use It

##### In Agents (Recommended)

Add Shopify as a tool to any agent. The agent can then manage your store conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Shopify tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for out-of-stock products")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Shop

| Tool                 | Description                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| **Get Shop Details** | Get store details including name, domain, currency, plan, and contact info |

##### Products

| Tool                         | Description                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **Search Products**          | Search products with query filters, sort, and pagination                                |
| **Get Product**              | Get a single product by ID with full details including variants, images, and metafields |
| **Create Product**           | Create a new product                                                                    |
| **Update Product**           | Update an existing product's details                                                    |
| **Delete Product**           | Delete a product and all associated variants and media                                  |
| **Create Product Variant**   | Add a new variant to an existing product                                                |
| **Update Product Variant**   | Update a variant's price, SKU, weight, or other properties                              |
| **Reorder Product Variants** | Reorder variants on a product                                                           |
| **Delete Product Variants**  | Delete one or more variants from a product in bulk                                      |
| **Add Product Image**        | Add an image to a product from a URL                                                    |
| **Delete Product Media**     | Delete media from a product                                                             |
| **Reorder Product Media**    | Reorder media on a product                                                              |
| **Update Product Media**     | Update media on a product                                                               |

##### Inventory

| Tool                           | Description                                                           |
| ------------------------------ | --------------------------------------------------------------------- |
| **Get Locations**              | Get all inventory locations (warehouses, stores, fulfillment centers) |
| **Get Inventory Level**        | Get inventory quantities for an item across all locations             |
| **Adjust Inventory**           | Adjust inventory quantity for an item at a specific location          |
| **Update Inventory Tracking**  | Enable or disable inventory tracking for an inventory item            |
| **Get Variant Inventory Item** | Get the inventory item ID and levels for a product variant            |

##### Orders

| Tool                                  | Description                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------- |
| **Search Orders**                     | Search orders by status, date, customer, or fulfillment status                  |
| **Get Order**                         | Get a single order by ID with full details                                      |
| **Cancel Order**                      | Cancel an order with a reason, optionally restocking and notifying the customer |
| **Close Order**                       | Close (archive) a fully-processed order                                         |
| **Update Order Note**                 | Update the internal staff note and other editable fields on an order            |
| **Add Order Tags**                    | Add tags to an order for categorization and filtering                           |
| **Create Refund**                     | Refund line items, shipping, and duties on an order with optional restocking    |
| **Create Return**                     | Create a return on an order for fulfilled items                                 |
| **Begin Order Edit**                  | Start an order editing session                                                  |
| **Order Edit Add Variant**            | Add a product variant as a new line item to an order being edited               |
| **Order Edit Set Line Item Quantity** | Set the quantity of a line item on an order being edited                        |
| **Commit Order Edit**                 | Apply staged order edit changes to the original order                           |

##### Abandoned Checkouts

| Tool                           | Description                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| **Search Abandoned Checkouts** | Search abandoned checkouts (incomplete carts) with filters for status, recovery state, and dates |
| **Get Abandoned Checkout**     | Get a single abandoned checkout with full details                                                |

##### Customers

| Tool                 | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| **Search Customers** | Search customers by name, email, phone, tags, or other criteria     |
| **Get Customer**     | Get a single customer by ID with full details                       |
| **Create Customer**  | Create a new customer with contact information, addresses, and tags |
| **Update Customer**  | Update an existing customer's details                               |

##### Fulfillment

| Tool                            | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| **Get Fulfillment Orders**      | Get fulfillment orders for a specific order            |
| **Create Fulfillment**          | Create a fulfillment with tracking information         |
| **Update Fulfillment Tracking** | Update tracking information on an existing fulfillment |
| **Cancel Fulfillment**          | Cancel a fulfillment, restocking the items             |

##### Collections

| Tool                                | Description                                          |
| ----------------------------------- | ---------------------------------------------------- |
| **Search Collections**              | Search collections by title, type, or other criteria |
| **Get Collection**                  | Get a single collection by ID including its products |
| **Create Collection**               | Create a custom or smart collection                  |
| **Update Collection**               | Update a collection's details                        |
| **Delete Collection**               | Delete a collection                                  |
| **Add Products to Collection**      | Add products to a custom collection                  |
| **Remove Products from Collection** | Remove products from a custom collection             |

##### Discounts

| Tool                              | Description                                                          |
| --------------------------------- | -------------------------------------------------------------------- |
| **Search Discount Codes**         | Search discount codes                                                |
| **Create Discount Code**          | Create a percentage or fixed-amount discount code                    |
| **Create Automatic Discount**     | Create an automatic discount that applies at checkout without a code |
| **Delete Discount**               | Delete a discount code or automatic discount                         |
| **Update Discount**               | Update an existing discount                                          |
| **Create Free Shipping Discount** | Create a free shipping discount                                      |
| **Create BXGY Discount**          | Create a buy X get Y discount                                        |

##### Draft Orders

| Tool                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| **Search Draft Orders**  | Search draft orders                                          |
| **Create Draft Order**   | Create a draft order for phone sales, custom pricing, or B2B |
| **Complete Draft Order** | Complete a draft order, converting it into a real order      |
| **Delete Draft Order**   | Delete an incomplete draft order                             |

##### Content

| Tool             | Description                                   |
| ---------------- | --------------------------------------------- |
| **Search Pages** | Search store pages                            |
| **Create Page**  | Create a new page in the online store         |
| **Update Page**  | Update a page's content, title, or visibility |
| **Delete Page**  | Delete a page from the online store           |

##### Blogs & Articles

| Tool                 | Description                                                          |
| -------------------- | -------------------------------------------------------------------- |
| **Search Blogs**     | Search blogs in the online store                                     |
| **Create Blog**      | Create a new blog in the online store                                |
| **Search Articles**  | Search blog posts (articles) across the store's blogs                |
| **Create Article**   | Create a new blog post (article) in a blog                           |
| **Update Article**   | Update a blog post's content, title, SEO, image, tags, or visibility |
| **Delete Article**   | Delete a blog post (article)                                         |
| **Search Comments**  | List comments on blog posts, store-wide or for a single article      |
| **Moderate Comment** | Approve, mark as spam/not spam, or delete a blog comment             |

##### Metafields

| Tool                 | Description                                |
| -------------------- | ------------------------------------------ |
| **Get Metafields**   | Get metafields for a specific resource     |
| **Set Metafield**    | Create or update a metafield on a resource |
| **Delete Metafield** | Delete a metafield                         |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search products:**

```text
Find all products with "sneaker" in the title that are in stock
```

**Manage inventory:**

```text
Show me inventory levels for SKU "BLU-SHIRT-M" across all locations
```

**Process orders:**

```text
Search for unfulfilled orders from the last 7 days
```

**Customer management:**

```text
Find all customers tagged "VIP" and show their order history
```

**Create a discount:**

```text
Create a 20% off discount code "SUMMER20" for all products
```

**Fulfill an order:**

```text
Create a fulfillment for order #1234 with tracking number "1Z999AA10123456784"
```

**Manage collections:**

```text
Add the new fall products to the "Seasonal" collection
```

**Draft orders:**

```text
Create a draft order for 2x "Premium Widget" at a custom price of $45 each
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific product IDs, order numbers, or customer emails                                                                         |
| Action not completing            | Check that you've authenticated and your Shopify app has the required permissions                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Cancel all unfulfilled orders older than 30 days" will search for matching orders first, then cancel each one. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Shopify MCP server](https://www.gumloop.com/mcp/shopify) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Sigma Computing

*Manage workbooks, members, teams, and data connections with AI-powered analytics automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/sigma_computing

Manage workbooks, members, teams, and data connections with AI-powered analytics automation.

Sigma Computing is a cloud analytics platform that lets teams explore and visualize data using a spreadsheet-like interface. The Sigma Computing MCP server lets you manage workbooks, members, teams, workspaces, and data connections using natural language.

#### What Can It Do?

* **Manage workbooks** including creation, duplication, export, and permissions
* **Organize members and teams** with invitations, role updates, and team assignments
* **Control workspaces** with creation, permissions, and grants
* **Monitor data connections** and test connectivity

#### Where to Use It

##### In Agents (Recommended)

Add Sigma Computing as a tool to any agent. The agent can then manage your analytics environment conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Sigma Computing tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all workbooks in my workspace")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Workbook Tools

| Tool                             | Description                                                          |
| -------------------------------- | -------------------------------------------------------------------- |
| **Get Current User**             | Get the identity and authentication status of the current user       |
| **List Workbooks**               | List workbooks with optional pagination                              |
| **Get Workbook**                 | Get workbook details by ID                                           |
| **Create Workbook**              | Create a new workbook                                                |
| **Duplicate Workbook**           | Create a copy of an existing workbook                                |
| **List Workbook Pages**          | List pages in a workbook                                             |
| **List Workbook Elements**       | List all elements in a workbook                                      |
| **Get Workbook Schema**          | Get the schema of a workbook including columns and element structure |
| **Get Workbook Sources**         | Get data sources connected to a workbook                             |
| **List Workbook Queries**        | List SQL queries in a workbook                                       |
| **Export Workbook**              | Trigger a data export from a workbook                                |
| **Download Workbook Export**     | Download a previously exported workbook file                         |
| **Send Workbook**                | Send a scheduled export of a workbook via email                      |
| **Grant Workbook Permission**    | Grant a member or team access to a workbook                          |
| **Tag Workbook**                 | Add a tag to a workbook                                              |
| **Get Workbook Version History** | Get the version history of a workbook                                |

##### Member Tools

| Tool                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| **List Members**      | List organization members with search and pagination |
| **Get Member**        | Get member details by ID                             |
| **Create Member**     | Invite a new member to the organization              |
| **Update Member**     | Update a member's account type or profile            |
| **Deactivate Member** | Deactivate a member from the organization            |
| **List Member Teams** | List teams that a member belongs to                  |

##### Team Tools

| Tool                    | Description                                      |
| ----------------------- | ------------------------------------------------ |
| **List Teams**          | List all teams in the organization               |
| **Get Team**            | Get team details by ID                           |
| **Create Team**         | Create a new team                                |
| **Update Team**         | Update a team's name, description, or visibility |
| **Delete Team**         | Delete a team permanently                        |
| **List Team Members**   | List members of a team                           |
| **Update Team Members** | Add or remove members from a team                |

##### Workspace Tools

| Tool                           | Description                                  |
| ------------------------------ | -------------------------------------------- |
| **List Workspaces**            | List workspaces with optional name filter    |
| **Get Workspace**              | Get workspace details by ID                  |
| **Create Workspace**           | Create a new workspace                       |
| **Update Workspace**           | Update a workspace's name or description     |
| **Delete Workspace**           | Delete a workspace                           |
| **List Workspace Grants**      | List permission grants for a workspace       |
| **Grant Workspace Permission** | Grant a member or team access to a workspace |

##### Connection and Template Tools

| Tool                              | Description                                                    |
| --------------------------------- | -------------------------------------------------------------- |
| **List Connections**              | List data connections with optional search and archived filter |
| **Get Connection**                | Get connection details by ID                                   |
| **Test Connection**               | Test if a data connection is active and working                |
| **Lookup Connection Path**        | Look up a database/schema/table path within a connection       |
| **List Templates**                | List available workbook templates                              |
| **Get Template**                  | Get template details by ID                                     |
| **Create Workbook From Template** | Create a new workbook from a template                          |
| **List Account Types**            | List all account types in the organization                     |
| **List User Attributes**          | List custom user attributes and their values                   |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List workbooks:**

```text
Show me all workbooks in my Sigma Computing account
```

**Export data:**

```text
Export the Q4 Sales Dashboard workbook as a PDF
```

**Manage teams:**

```text
Create a new team called "Data Analysts" and add jane@company.com
```

**Check connections:**

```text
Test if the Snowflake data connection is working
```

**Create from template:**

```text
Create a new workbook from the Monthly Report template
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific workbook names or IDs                                                                                                                 |
| Action not completing            | Check that you've authenticated with Sigma Computing                                                                                               |
| Permission denied                | Ensure your account has the required admin or editor role                                                                                          |
| Unexpected results               | The agent may chain multiple tools (e.g., listing workbooks first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Share the sales dashboard with the analytics team" will find the workbook first, then grant permission. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Sigma Computing MCP server](https://www.gumloop.com/mcp/sigma-computing) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Similarweb

*Analyze website traffic, audiences, and competitor insights with Similarweb.*

**Source:** https://docs.gumloop.com/nodes/mcp/similarweb

Analyze website traffic, audiences, and competitor insights with Similarweb.

Similarweb is a digital intelligence platform providing website traffic analysis, audience insights, and competitive benchmarking. The Similarweb MCP server lets you analyze web traffic and competitor data using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Similarweb. Authentication uses OAuth — just connect your Similarweb account and start using it immediately.

#### What Can It Do?

* **Analyze website traffic** volumes and trends
* **Research audiences** and demographics
* **Compare competitors** with benchmarking data
* **Track industry trends** and market insights

#### Where to Use It

##### In Agents (Recommended)

Add Similarweb as a tool to any agent. The agent can then research and analyze web data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Similarweb account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Similarweb tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Similarweb uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Similarweb to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Analyze traffic:**

```text
What's the monthly traffic for competitor.com over the last 6 months?
```

**Compare sites:**

```text
Compare the traffic sources for example.com and competitor.com
```

**Research audience:**

```text
What demographics visit techblog.com?
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Similarweb subscription                                                                   |
| No data available  | Some domains may not have sufficient traffic data                                                                   |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Slack

*Manage your workspace with AI-powered team communication automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/slack

Manage your workspace with AI-powered team communication automation.

Slack is the leading platform for team communication and collaboration. The Slack MCP server lets you read and post messages, manage channels, and search your workspace using natural language.

#### What Can It Do?

* **Read and send messages** to channels and users
* **Manage channels** by creating, archiving, and updating topics and purposes
* **Search your workspace** for messages, files, and people
* **Handle membership** by adding or removing users
* **React to messages** with emoji reactions
* **Pin and unpin messages** in channels
* **Upload and download files** to and from channels
* **Create and manage canvases** with rich content

#### Where to Use It

##### In Agents (Recommended)

Add Slack as a tool to any agent. The agent can then manage your workspace conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Slack tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Post a message to #general")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                         | Description                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Read Messages**            | Read messages from a channel                                                                                                                                                                                                                                                                                                                         |
| **Send Message**             | Post a message to a channel or user, or stage it as a draft in the user's "Drafts & sent" sidebar (`draft=true`). Supports `unfurl_links` parameter to control link previews. The bot can send messages to public channels even if it hasn't been added to them (via the `chat:write.public` scope). For private channels, the bot must be a member. |
| **Send Ephemeral Message**   | Send a message only visible to one user. Supports `blocks` parameter for rich Block Kit layouts.                                                                                                                                                                                                                                                     |
| **Create Canvas**            | Create a rich canvas message                                                                                                                                                                                                                                                                                                                         |
| **Add User To Channel**      | Add a user to a channel                                                                                                                                                                                                                                                                                                                              |
| **Remove From Channel**      | Remove a user from a channel                                                                                                                                                                                                                                                                                                                         |
| **Delete Message**           | Delete a message                                                                                                                                                                                                                                                                                                                                     |
| **Get Message Thread**       | Get a message and replies                                                                                                                                                                                                                                                                                                                            |
| **Search Users**             | Search for users                                                                                                                                                                                                                                                                                                                                     |
| **Create Channel**           | Create a new channel                                                                                                                                                                                                                                                                                                                                 |
| **Archive Channel**          | Archive a channel                                                                                                                                                                                                                                                                                                                                    |
| **Update Channel Topic**     | Update a channel's topic                                                                                                                                                                                                                                                                                                                             |
| **List Users In Channel**    | List channel members                                                                                                                                                                                                                                                                                                                                 |
| **Search**                   | Search messages and files                                                                                                                                                                                                                                                                                                                            |
| **Create Standalone Canvas** | Create a standalone canvas not tied to a channel                                                                                                                                                                                                                                                                                                     |
| **Lookup Canvas Sections**   | Retrieve sections and content from a canvas                                                                                                                                                                                                                                                                                                          |
| **Edit Canvas**              | Insert, replace, or delete content in a canvas                                                                                                                                                                                                                                                                                                       |
| **Delete Canvas**            | Delete an existing canvas                                                                                                                                                                                                                                                                                                                            |
| **Set Canvas Access**        | Set access levels for a canvas (channel-wide or specific users/teams)                                                                                                                                                                                                                                                                                |
| **Remove Canvas Access**     | Remove access to a canvas for specific users or teams                                                                                                                                                                                                                                                                                                |
| **Get User Presence**        | Check a user's online status                                                                                                                                                                                                                                                                                                                         |
| **Update Channel Purpose**   | Update a channel's purpose description                                                                                                                                                                                                                                                                                                               |
| **Unarchive Channel**        | Unarchive a previously archived channel                                                                                                                                                                                                                                                                                                              |
| **Get Conversation Info**    | Retrieve information about a conversation                                                                                                                                                                                                                                                                                                            |
| **List Pinned Items**        | List pinned items in a channel                                                                                                                                                                                                                                                                                                                       |
| **Pin Message**              | Pin a message in a channel                                                                                                                                                                                                                                                                                                                           |
| **Unpin Message**            | Unpin a message from a channel                                                                                                                                                                                                                                                                                                                       |
| **React To Message**         | Add an emoji reaction to a message                                                                                                                                                                                                                                                                                                                   |
| **List Channels**            | List channels in the workspace                                                                                                                                                                                                                                                                                                                       |
| **Upload File**              | Upload a file or image to a channel                                                                                                                                                                                                                                                                                                                  |
| **Download File**            | Download a file from Slack to Gumloop storage                                                                                                                                                                                                                                                                                                        |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Send a message:**

```text
Post "Daily standup starts in 10 minutes" to #engineering
```

**Read messages:**

```text
Show me the last 20 messages in #support
```

**Create a channel:**

```text
Create a private channel called "project-phoenix"
```

**Search workspace:**

```text
Search for messages from sarah about quarterly report
```

**Add a user:**

```text
Add john@company.com to the #marketing channel
```

**React to a message:**

```text
Add a thumbsup reaction to the last message in #general
```

**Pin a message:**

```text
Pin the latest announcement in #company-updates
```

**Draft a message:**

```text
Draft a message to #engineering saying "Deploy scheduled for Friday at 5pm"
```

> **Info:** When Slack tools are used through an agent, messages are posted as the **Gumloop bot** by default rather than as the authenticated user. This helps distinguish automated messages from manual ones.

#### Troubleshooting

| Issue                            | Solution                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use exact channel names with # prefix                                                                                                             |
| Action not completing            | Check that you've authenticated with Slack                                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a user first, then adding to channel). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add the new hire to the engineering channel" will find the user first, then add them. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Slack MCP server](https://www.gumloop.com/mcp/slack) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Snowflake

*Query your data warehouse with AI-powered SQL automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/snowflake

Query your data warehouse with AI-powered SQL automation.

Snowflake is a cloud data platform for analytics and data warehousing. The Snowflake MCP server lets you run SQL queries and inspect table schemas using natural language.

#### What Can It Do?

* **Run SQL queries** and return structured results
* **Describe table schemas** to understand your data
* **Bulk load data** into tables via staging
* **Tag queries** for tracking in Snowflake's query history
* **Power analytics workflows** with live data

#### Where to Use It

##### In Agents (Recommended)

Add Snowflake as a tool to any agent. The agent can then query your data warehouse conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Snowflake tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Query orders from last month")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool               | Description                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Describe Table** | Get table structure and columns                                                                                                                                |
| **Execute Query**  | Run a SQL query. Automatically injects a structured QUERY\_TAG (including user\_email and agent\_id) on every call for tracking in Snowflake's QUERY\_HISTORY. |
| **Stage Data**     | Bulk load data into a table via staging                                                                                                                        |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Query data:**

```text
Get all orders from last month with total over $1000
```

**Check table schema:**

```text
What columns are in the customers table?
```

**Aggregate data:**

```text
Show me daily revenue for the past 30 days
```

**Run custom SQL:**

```text
Run SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id
```

**Run a tagged query:**

```text
Run a query to get daily active users, tagged with "team:growth" for tracking
```

**Bulk load data:**

```text
Stage and load this CSV data into the customers table
```

#### Configuration Options

| Option               | Description                                                                                                                       | Default |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **`ocsp_fail_open`** | Allow connection when OCSP certificate validation fails. Enable if encountering certificate validation errors with large queries. | `false` |
| **`insecure_mode`**  | Skip OCSP certificate revocation checking entirely. Enable if encountering error `254007` on large result set downloads.          | `false` |

> **Warning:** Only enable `insecure_mode` if you are experiencing OCSP-related errors (e.g., error code 254007) when downloading large result sets. This disables certificate revocation checks on S3 result retrieval.

#### Troubleshooting

| Issue                            | Solution                                                                                                                                     |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Specify schema and table names clearly                                                                                                       |
| Action not completing            | Check that you've authenticated with Snowflake                                                                                               |
| Unexpected results               | The agent may chain multiple tools (e.g., describing a table first, then querying). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                          |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Query the sales table" will describe it first to understand the schema, then run the query. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Snowflake MCP server](https://www.gumloop.com/mcp/snowflake) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Sprig

*Pull survey data and AI insights with AI-powered research automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/sprig

Pull survey data and AI insights with AI-powered research automation.

Sprig is a product research platform for capturing user feedback and insights. The Sprig MCP server lets you retrieve survey responses, study configurations, and AI-generated themes using natural language.

#### What Can It Do?

* **Retrieve survey responses** with date filtering
* **Pull study configurations** by status
* **Access AI-generated themes** and insights
* **Look up user profiles** and attributes

#### Where to Use It

##### In Agents (Recommended)

Add Sprig as a tool to any agent. The agent can then access your research data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Sprig tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get responses from last month's survey")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                   | Description                         |
| ---------------------- | ----------------------------------- |
| **Retrieve Responses** | Get survey responses with filtering |
| **Retrieve Surveys**   | List study configurations           |
| **Retrieve Themes**    | Get AI-generated themes             |
| **Get User**           | Look up user by ID                  |
| **Upsert User**        | Create or update a user             |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Get responses:**

```text
Get all responses from the onboarding survey from last month
```

**List surveys:**

```text
Show me all active surveys
```

**Get themes:**

```text
What are the AI-generated themes from the NPS study?
```

**Look up user:**

```text
Get the profile and attributes for this user ID
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific survey IDs or date ranges                                                                                                             |
| Action not completing            | Check that you've authenticated with Sprig                                                                                                         |
| Unexpected results               | The agent may chain multiple tools (e.g., listing surveys first, then getting responses). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                                |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get responses from the onboarding survey" will find the survey first, then retrieve responses. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Sprig MCP server](https://www.gumloop.com/mcp/sprig) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Stripe

*Manage customers, subscriptions, and payments with AI-powered billing automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/stripe

Manage customers, subscriptions, and payments with AI-powered billing automation.

Stripe is an online payment processing platform. The Stripe MCP server lets you manage customers, subscriptions, invoices, and products using natural language.

#### What Can It Do?

* **Manage customers** with creation, search, and updates
* **Handle subscriptions** with create, update, and cancel
* **Track payments** and charges
* **Manage invoices** and products
* **Create and manage coupons** for discounts

#### Where to Use It

##### In Agents (Recommended)

Add Stripe as a tool to any agent. The agent can then interact with Stripe conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Stripe tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all active subscriptions")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                      | Description                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| **List Customers**        | List all Stripe customers                                         |
| **Retrieve Balance**      | Retrieve the current Stripe account balance                       |
| **List Subscriptions**    | List all subscriptions in the Stripe account                      |
| **Update Subscription**   | Update metadata or attributes of a Stripe subscription            |
| **List Payment Intents**  | List all payment intents                                          |
| **List Charges**          | List all charges processed by the Stripe account                  |
| **Create Customer**       | Create a new customer in Stripe                                   |
| **List Invoices**         | List all invoices created in Stripe                               |
| **Retrieve Customer**     | Retrieve details of a specific customer by ID                     |
| **List Products**         | List all available products in Stripe                             |
| **Cancel Subscription**   | Cancel a subscription by ID                                       |
| **Retrieve Subscription** | Retrieve a subscription by its ID                                 |
| **Create Subscription**   | Create a subscription for a customer with a price                 |
| **Update Customer**       | Update customer attributes such as name, email, etc.              |
| **Create Coupon**         | Create a new Stripe coupon for discounts                          |
| **Retrieve Coupon**       | Retrieve a specific Stripe coupon by ID                           |
| **List Coupons**          | List all Stripe coupons with optional filtering and pagination    |
| **Delete Coupon**         | Delete a Stripe coupon (prevents new customers from redeeming it) |
| **Search Customers**      | Search for customers using Stripe's Search Query Language         |
| **Search Invoices**       | Search for invoices using Stripe's Search Query Language          |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List customers:**

```text
Show me all Stripe customers
```

**View subscriptions:**

```text
List all active subscriptions
```

**Check balance:**

```text
What's my current Stripe account balance?
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Stripe credentials and that you have the required permissions                                           |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Stripe MCP server](https://www.gumloop.com/mcp/stripe) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Supabase

*Manage Supabase projects, databases, branches, and logs.*

**Source:** https://docs.gumloop.com/nodes/mcp/supabase

Manage Supabase projects, databases, branches, and logs.

Supabase is the open-source Firebase alternative providing databases, authentication, storage, and edge functions. The Supabase MCP server lets you manage your projects, databases, and infrastructure using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Supabase. Authentication uses OAuth — just connect your Supabase account and start using it immediately.

#### What Can It Do?

* **Manage projects** and their configurations
* **Work with databases** including schema and queries
* **Handle branches** for database development workflows
* **View logs** and monitor project health

#### Where to Use It

##### In Agents (Recommended)

Add Supabase as a tool to any agent. The agent can then manage your backend infrastructure conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Supabase account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Supabase tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Supabase uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Supabase to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Manage projects:**

```text
List all my Supabase projects and their status
```

**Work with databases:**

```text
Show me the schema for the users table in my production project
```

**View logs:**

```text
Get the recent error logs from my project
```

#### Troubleshooting

| Issue              | Solution                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect     | Ensure you have an active Supabase account with project access                                                      |
| Project not found  | Check that you have the correct organization selected                                                               |
| Tool not available | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Tableau

*Access dashboards and analytics with AI-powered business intelligence automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/tableau

Access dashboards and analytics with AI-powered business intelligence automation.

Tableau is a leading business intelligence platform for data visualization. The Tableau MCP server lets you list workbooks, export views, and access Pulse metrics using natural language.

#### What Can It Do?

* **List workbooks and views** across your site
* **Export view data** as CSV or images
* **Access Tableau Pulse** metrics and AI insights
* **Search content** across your organization
* **Query datasources directly** using VizQL Data Service with date aggregations, binning, field aliases, and advanced filtering

#### Where to Use It

##### In Agents (Recommended)

Add Tableau as a tool to any agent. The agent can then access your dashboards conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Tableau tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all workbooks in the Finance project")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Setting Up Credentials

Tableau uses Personal Access Tokens (PAT) for authentication. Generate a token in your Tableau account settings, then add it to your [Connectors page](https://www.gumloop.com/personal/connectors).

#### Available Tools

| Tool                                  | Description                                                                                                                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **List Views**                        | List all views on a site                                                                                                                                                            |
| **Get View Data**                     | Export view data as CSV                                                                                                                                                             |
| **Get View Image**                    | Export view as PNG                                                                                                                                                                  |
| **List Workbooks**                    | List all workbooks                                                                                                                                                                  |
| **Get Workbook**                      | Get workbook details                                                                                                                                                                |
| **List Datasources**                  | List published data sources                                                                                                                                                         |
| **Search Content**                    | Search across all content                                                                                                                                                           |
| **List All Pulse Metric Definitions** | List Pulse metrics                                                                                                                                                                  |
| **Generate Pulse Insight Bundle**     | Get AI insights                                                                                                                                                                     |
| **Get Datasource Metadata**           | Get field metadata from a published datasource using VizQL Data Service                                                                                                             |
| **Query Datasource**                  | Query data directly from a published datasource with custom fields, filters, aggregations, date grouping (YEAR/QUARTER/MONTH/WEEK/DAY), binning, field aliases, and context filters |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List workbooks:**

```text
Show me all workbooks in the Finance project
```

**Export data:**

```text
Get the data from the Sales Dashboard view as CSV
```

**Get dashboard image:**

```text
Export an image of the Executive Summary dashboard
```

**Search content:**

```text
Search for workbooks and views containing "revenue"
```

**Get Pulse insights:**

```text
Generate AI insights for the monthly sales metric
```

**Get datasource metadata:**

```text
Show me all available fields in the Sales datasource
```

**Query datasource directly:**

```text
Query the Sales datasource for total revenue by region, sorted by revenue descending
```

**Query with date aggregation:**

```text
Query the Orders datasource for monthly order count grouped by MONTH, filtered to the last 6 months
```

**Query with binning:**

```text
Query the Sales datasource for revenue distribution using bins of size 1000
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use exact workbook or view names                                                                                                                 |
| Action not completing            | Check that your Personal Access Token is valid                                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., listing workbooks first, then getting views). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                              |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Export the Finance dashboard" will find the view first, then export it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Tableau MCP server](https://www.gumloop.com/mcp/tableau) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### TikTok

*Scrape TikTok data with AI-powered social media automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/tiktok

Scrape TikTok data with AI-powered social media automation.

TikTok is a leading short-form video platform with billions of users. The TikTok MCP server lets you search videos, analyze profiles, and collect engagement data using natural language.

#### What Can It Do?

* **Get hashtag videos** with engagement metrics
* **Analyze creator profiles** and their content
* **Export follower lists** for research
* **Pull video details** including stats and music info

#### Where to Use It

##### In Agents (Recommended)

Add TikTok as a tool to any agent. The agent can then search and analyze TikTok data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with TikTok tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Get the top 20 #fitness videos")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                      | Description                                                          |
| ------------------------- | -------------------------------------------------------------------- |
| **Get Hashtag Videos**    | Get videos for a hashtag                                             |
| **Get Profile Videos**    | List videos from a profile                                           |
| **Get Profile Followers** | List followers for a profile                                         |
| **Get Video Details**     | Get full video metadata                                              |
| **Search Videos**         | Search by keyword                                                    |
| **Get Video Comments**    | Get comments from videos with text, usernames, likes, and timestamps |

#### Credit Costs

| Tool                  | Credits    |
| --------------------- | ---------- |
| Get Hashtag Videos    | 3 per item |
| Get Profile Videos    | 3 per item |
| Get Profile Followers | 3 per item |
| Get Video Details     | 5 per item |
| Search Videos         | 3 per item |
| Get Video Comments    | 3 per item |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Get trending content:**

```text
Get the top 20 #travelhacks videos
```

**Analyze a creator:**

```text
Show me the latest 15 videos from @gymshark
```

**Search for content:**

```text
Search TikTok for "meal prep" videos
```

**Get video details:**

```text
Get the details for this TikTok video URL
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use exact usernames with @ symbol                                                                                                                 |
| Action not completing            | Check that you've authenticated                                                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a profile first, then getting videos). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get engagement stats for the top fitness influencer" will search profiles first, then get videos. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [TikTok MCP server](https://www.gumloop.com/mcp/tiktok) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Trello

*Manage boards, lists, and cards with AI-powered project management automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/trello

Manage boards, lists, and cards with AI-powered project management automation.

Trello is a visual project management tool that organizes work into boards, lists, and cards. The Trello MCP server lets you manage your boards, lists, cards, checklists, and labels using natural language.

#### What Can It Do?

* **Manage boards** with creation, updates, and member management
* **Organize lists and cards** including creation, updates, and deletion
* **Track progress** with checklists, labels, and comments
* **Search across** boards, cards, members, and organizations

#### Where to Use It

##### In Agents (Recommended)

Add Trello as a tool to any agent. The agent can then manage your project boards conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Trello tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Create a card in the To Do list")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

##### Board Tools

| Tool                   | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| **List Boards**        | List boards for the authenticated user with filtering options |
| **Get Board**          | Get a specific board by ID                                    |
| **Create Board**       | Create a new board                                            |
| **Update Board**       | Update an existing board                                      |
| **Delete Board**       | Permanently delete a board                                    |
| **List Board Members** | List members of a board                                       |
| **List Board Lists**   | List all lists on a board                                     |
| **List Board Labels**  | List all labels on a board                                    |

##### List Tools

| Tool            | Description                  |
| --------------- | ---------------------------- |
| **Get List**    | Get a specific list by ID    |
| **Create List** | Create a new list on a board |
| **Update List** | Update an existing list      |

##### Card Tools

| Tool                 | Description                 |
| -------------------- | --------------------------- |
| **List Cards**       | List cards on a list        |
| **Get Card**         | Get a specific card by ID   |
| **Create Card**      | Create a new card on a list |
| **Update Card**      | Update an existing card     |
| **Delete Card**      | Permanently delete a card   |
| **Add Card Comment** | Add a comment to a card     |

##### Checklist Tools

| Tool                      | Description                       |
| ------------------------- | --------------------------------- |
| **List Card Checklists**  | List all checklists on a card     |
| **Create Checklist**      | Create a new checklist on a card  |
| **Delete Checklist**      | Delete a checklist from a card    |
| **Create Checklist Item** | Create a new item on a checklist  |
| **Update Checklist Item** | Update a checklist item on a card |

##### Label and Search Tools

| Tool                   | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| **Create Label**       | Create a new label on a board                            |
| **Update Label**       | Update an existing label                                 |
| **Delete Label**       | Delete a label from a board                              |
| **Search**             | Search for boards, cards, members, and organizations     |
| **Get My Profile**     | Get the authenticated user's profile                     |
| **List Organizations** | List organizations/workspaces for the authenticated user |
| **Get Organization**   | Get a specific organization/workspace by ID              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List boards:**

```text
Show me all my Trello boards
```

**Create a card:**

```text
Create a card called "Fix login bug" in the To Do list on the Engineering board
```

**Move a card:**

```text
Move the "Design review" card to the Done list
```

**Add a checklist:**

```text
Add a checklist called "Launch steps" to the Release card with items: update docs, notify team, deploy
```

**Search:**

```text
Search for cards about "onboarding" across all my boards
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific board or card names                                                                                                               |
| Action not completing            | Check that you've authenticated with Trello                                                                                                    |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a board first, then listing cards). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                            |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Add a comment to the latest card in To Do" will find the list, get cards, then add a comment. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Trello MCP server](https://www.gumloop.com/mcp/trello) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Vercel

*Manage your Vercel projects, deployments, and logs.*

**Source:** https://docs.gumloop.com/nodes/mcp/vercel

Manage your Vercel projects, deployments, and logs.

Vercel is the platform for frontend developers, providing hosting, serverless functions, and continuous deployment. The Vercel MCP server lets you manage your projects, deployments, and logs using natural language.

> **Info:** This is a **third-party managed** MCP server operated by Vercel. Authentication uses OAuth — just connect your Vercel account and start using it immediately.

#### What Can It Do?

* **Manage projects** and their settings
* **View deployments** and their status
* **Access logs** for debugging
* **Configure domains** and environment variables

#### Where to Use It

##### In Agents (Recommended)

Add Vercel as a tool to any agent. The agent can then manage your deployments conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your Vercel account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Vercel tools. This gives you the flexibility of an agent within a deterministic workflow.

#### Authentication

Vercel uses **OAuth 2.0** for authentication. When you connect the integration, you'll be redirected to Vercel to authorize access. No API keys or manual configuration required.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Check deployments:**

```text
Show me the latest deployments for my project
```

**View logs:**

```text
Get the build logs for my most recent deployment
```

**Manage projects:**

```text
List all my Vercel projects and their domains
```

#### Troubleshooting

| Issue                | Solution                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Cannot connect       | Ensure you have access to the Vercel team you want to manage                                                        |
| Deployment not found | Check the project name matches exactly                                                                              |
| Tool not available   | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

### Webflow

*Manage sites, collections, forms, and pages with AI-powered web design automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/webflow

Manage sites, collections, forms, and pages with AI-powered web design automation.

Webflow is a visual web development platform. The Webflow MCP server lets you manage sites, CMS collections, forms, pages, and users using natural language.

#### What Can It Do?

* **Manage sites** and custom domains
* **Create and update CMS collections** and items
* **Handle form submissions** across your sites
* **Manage pages** and user access

#### Where to Use It

##### In Agents (Recommended)

Add Webflow as a tool to any agent. The agent can then interact with Webflow conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Webflow tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List all CMS collections on my site")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                              | Description                                                |
| --------------------------------- | ---------------------------------------------------------- |
| **Get Authorized User**           | Get information about the authorized Webflow user          |
| **List Sites**                    | List all sites the provided access token is able to access |
| **Get Site**                      | Get details of a specific site by its ID                   |
| **Get Custom Domains**            | Get a list of all custom domains related to a site         |
| **List Forms**                    | List forms for a given site                                |
| **List Form Submissions**         | List form submissions for a given form                     |
| **Get Form Submission**           | Get information about a specific form submission           |
| **List Form Submissions By Site** | List form submissions for a given site                     |
| **Delete Form Submission**        | Delete a form submission                                   |
| **List Pages**                    | List all pages for a site                                  |
| **Get Page Metadata**             | Get metadata information for a single page                 |
| **Get Page Content**              | Get content from a static page                             |
| **List Collections**              | List all Collections within a Site                         |
| **Get Collection**                | Get the full details of a collection from its ID           |
| **Delete Collection**             | Delete a collection using its ID                           |
| **Create Collection**             | Create a Collection for a site                             |
| **List Collection Items**         | List all Items within a Collection                         |
| **Get Collection Item**           | Get details of a selected Collection Item                  |
| **Update Collection Item**        | Update a selected Item in a Collection                     |
| **Update Collection Items**       | Update a single item or multiple items in a Collection     |
| **Create Collection Item**        | Create Item in a Collection                                |
| **Delete Collection Item**        | Delete an item from a collection                           |
| **Delete Collection Items**       | Delete Items from a Collection                             |
| **List Users**                    | Get a list of users for a site                             |
| **Get User**                      | Get a User by ID                                           |
| **Delete User**                   | Delete a User by ID                                        |
| **Invite User**                   | Create and invite a user with an email address             |

#### Example Prompts

Use these with your agent or in the Agent Node:

**List sites:**

```text
Show me all my Webflow sites
```

**Manage collections:**

```text
List all CMS collections on my site
```

**View submissions:**

```text
Get the latest form submissions for my contact form
```

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Webflow credentials and that you have the required permissions                                          |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Unexpected results    | The agent may chain multiple tools together. Review the agent's reasoning to understand its approach.               |

> **Tip:** Agents are smart enough to chain multiple API calls together. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Webflow MCP server](https://www.gumloop.com/mcp/webflow) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Workday

*Download custom reports from Workday and access employee data with AI-powered automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/workday

Download custom reports from Workday and access employee data with AI-powered automation.

Workday is a leading enterprise cloud platform for human capital management, financial management, and planning. The Workday MCP server lets you download custom reports from Workday using natural language.

#### What Can It Do?

* **Download custom reports** from Workday using report URLs
* **Export data** to your workspace for further processing

> **Info:** The Workday integration downloads report files from Workday. To parse the file contents, perform data analysis, or do any operations on the downloaded data, add the [Code Sandbox tool](https://docs.gumloop.com/core-concepts/agent_sandbox_and_secrets) to your agent. This enables your agent to read and process the downloaded files using Python.

#### Where to Use It

##### In Agents (Recommended)

Add Workday as a tool to any agent. The agent can then fetch reports conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Enter your Workday credentials

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Workday tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Download the employee roster report")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Authentication

Workday uses Basic Authentication with your Workday username and password. When connecting your Workday account, you'll need to provide:

* **Username**: Your Workday username (typically your email or employee ID)
* **Password**: Your Workday password

> **Warning:** Make sure your Workday account has the necessary permissions to access the reports you want to download. Contact your Workday administrator if you need additional access.

#### Available Tools

| Tool           | Description                                                     |
| -------------- | --------------------------------------------------------------- |
| **Get Report** | Download a custom report file from Workday using the report URL |

> **Tip:** The Get Report tool downloads the report file to your workspace. To parse, analyze, or transform the data in the downloaded file, enable the [Code Sandbox tool](https://docs.gumloop.com/core-concepts/agent_sandbox_and_secrets) for your agent. This allows the agent to use Python to read JSON, CSV, or other file formats and perform operations on the data.

#### Example Prompts

Use these with your agent or in the Agent Node:

**Download a report:**

```text
Download the employee roster report from https://wd5.myworkday.com/company/d/task/report.htmld
```

**Save report to workspace:**

```text
Fetch the Q4 headcount report and save it to my workspace as headcount_q4.json
```

#### Report URL Format

Workday custom reports are accessed via URLs that follow this pattern:

```text
https://{tenant}.myworkday.com/{company}/d/task/{report_path}
```

You can find your report URLs in Workday by:

1. Navigating to the report you want to access
2. Looking for the "Web Service" or "REST API" URL in the report settings
3. Copying the full URL to use with this integration

#### Troubleshooting

| Issue                 | Solution                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authentication failed | Verify your Workday username and password are correct                                                               |
| Report not found      | Check that the report URL is correct and accessible                                                                 |
| Permission denied     | Ensure your Workday account has access to the requested report                                                      |
| Tool not available    | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals) |
| Timeout errors        | Large reports may take longer to download - try again or contact support                                            |

> **Tip:** If you're having trouble accessing reports, work with your Workday administrator to ensure your account has the "Web Service" permission for the reports you need.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Workday MCP server](https://www.gumloop.com/mcp/workday) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### X (Twitter)

*Manage your X presence with AI-powered social media automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/x

Manage your X presence with AI-powered social media automation.

X (formerly Twitter) is a leading social platform for real-time conversations. The X MCP server lets you search tweets, manage bookmarks, post content, and analyze engagement using natural language.

#### What Can It Do?

* **Search tweets** by keyword, user, or date
* **Post and manage tweets** without leaving your workflow
* **Track mentions** and engagement
* **Manage followers** and bookmarks

#### Where to Use It

##### In Agents (Recommended)

Add X as a tool to any agent. The agent can then manage your X presence conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with X tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search tweets about AI automation")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description                  |
| ----------------------- | ---------------------------- |
| **Search Tweets**       | Search tweets by query       |
| **Get User Tweets**     | Get tweets from a user       |
| **Get User Mentions**   | Get tweets mentioning a user |
| **Get User Timeline**   | Get your home timeline       |
| **Create Tweet**        | Post a new tweet             |
| **Delete Tweet**        | Delete a tweet               |
| **Get Bookmarks**       | Get bookmarked tweets        |
| **Create Bookmark**     | Bookmark a tweet             |
| **Get Followers**       | Get user's followers         |
| **Get Following**       | Get accounts a user follows  |
| **Manage Follow**       | Follow or unfollow a user    |
| **Get Trends By WOEID** | Get trending topics          |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search tweets:**

```text
Search for tweets about "AI automation" from the last 7 days
```

**Monitor mentions:**

```text
Get tweets mentioning @gumloop from today
```

**Post a tweet:**

```text
Create a tweet: "Excited to announce our new product launch!"
```

**Get trending topics:**

```text
What's trending in the United States right now?
```

**Analyze engagement:**

```text
Get users who liked this tweet
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Agent not finding the right data | Use specific keywords or user handles                                                                                                      |
| Action not completing            | Check that you've authenticated with X                                                                                                     |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                        |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the latest tweets from our competitor" will find the user first, then get tweets. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [X MCP server](https://www.gumloop.com/mcp/x) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### YouTube

*Search and analyze YouTube content with AI-powered video automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/youtube

Search and analyze YouTube content with AI-powered video automation.

YouTube is the world's largest video platform with billions of users. The YouTube MCP server lets you search videos, get channel data, and collect comments using natural language.

#### What Can It Do?

* **Search videos** by keyword with filters
* **Get video details** with full metadata
* **Analyze channels** and their content
* **Collect comments** for sentiment analysis

#### Where to Use It

##### In Agents (Recommended)

Add YouTube as a tool to any agent. The agent can then search and analyze YouTube data conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with YouTube tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Search for Python tutorial videos")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                    | Description                    |
| ----------------------- | ------------------------------ |
| **Search Videos**       | Search by keyword with filters |
| **Get Video Details**   | Get full video metadata        |
| **Get Channel Videos**  | List videos from a channel     |
| **Get Playlist Videos** | Get videos from a playlist     |
| **Get Channel Details** | Get channel stats              |
| **Get Video Comments**  | Collect comments               |

#### Credit Costs

| Tool                | Credits    |
| ------------------- | ---------- |
| Search Videos       | 3 per item |
| Get Video Details   | 4 per item |
| Get Channel Videos  | 3 per item |
| Get Playlist Videos | 3 per item |
| Get Channel Details | 5 per item |
| Get Video Comments  | 5 per item |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Search videos:**

```text
Find Python pandas tutorials uploaded this year
```

**Get video details:**

```text
Get the details for this YouTube video URL
```

**Analyze a channel:**

```text
How many subscribers does @mkbhd have?
```

**Get comments:**

```text
Get the top 50 comments from this video
```

**Channel content:**

```text
Show me the latest 10 videos from @MrBeast
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use exact channel handles or video URLs                                                                                                           |
| Action not completing            | Check that you've authenticated                                                                                                                   |
| Unexpected results               | The agent may chain multiple tools (e.g., finding a channel first, then getting videos). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the top comments from MrBeast's latest video" will find the channel, get recent videos, then fetch comments. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [YouTube MCP server](https://www.gumloop.com/mcp/youtube) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Zendesk

*Manage support tickets and customers with AI-powered helpdesk automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/zendesk

Manage support tickets and customers with AI-powered helpdesk automation.

Zendesk is a leading customer service platform for support teams. The Zendesk MCP server lets you search tickets, manage users, and work with triggers and automations using natural language.

#### What Can It Do?

* **Search and manage tickets** with advanced filters
* **Batch create and update tickets** for bulk operations
* **Look up users** and groups for routing
* **Work with views** and macros
* **Manage triggers** and automations
* **Audit ticket history** and review change events
* **Track ticket metrics** including response times and SLA data
* **Manage tags** for ticket and user categorization
* **Browse Help Center** articles and community posts
* **Access Talk/Voice data** including calls, call legs, and recordings

#### Where to Use It

##### In Agents (Recommended)

Add Zendesk as a tool to any agent. The agent can then manage your support operations conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Zendesk tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "List open high-priority tickets")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Available Tools

| Tool                        | Description                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **List Tickets**            | Search or list tickets                                                                                      |
| **Get Ticket**              | Get ticket details                                                                                          |
| **Create Ticket**           | Create a new ticket                                                                                         |
| **Update Ticket**           | Update ticket fields                                                                                        |
| **Merge Tickets**           | Merge duplicate tickets                                                                                     |
| **Create Comment**          | Add a comment                                                                                               |
| **List Comments**           | List ticket comments                                                                                        |
| **List Ticket Attachments** | List attachments on a ticket                                                                                |
| **Get Attachment**          | Get attachment details                                                                                      |
| **List Ticket Fields**      | List available ticket fields                                                                                |
| **List Ticket Forms**       | List available ticket forms                                                                                 |
| **List Users**              | List agents or end-users                                                                                    |
| **Get User**                | Get user details                                                                                            |
| **Search Users**            | Search by email or name                                                                                     |
| **List Groups**             | List agent groups                                                                                           |
| **Get Group**               | Get group details                                                                                           |
| **List Tags**               | List all tags                                                                                               |
| **Search Tags**             | Search for tags                                                                                             |
| **Add Tags**                | Add tags to a ticket, user, or organization                                                                 |
| **Remove Tags**             | Remove tags from a ticket, user, or organization                                                            |
| **List Views**              | List available views                                                                                        |
| **Get View**                | Get view details                                                                                            |
| **Get Tickets In View**     | Get tickets from a view                                                                                     |
| **List Triggers**           | List all triggers                                                                                           |
| **Search Triggers**         | Search for triggers                                                                                         |
| **Get Trigger**             | Get trigger details                                                                                         |
| **List Trigger Categories** | List trigger categories                                                                                     |
| **List Automations**        | List all automations                                                                                        |
| **Search Automations**      | Search for automations                                                                                      |
| **Get Automation**          | Get automation details                                                                                      |
| **List Macros**             | List available macros                                                                                       |
| **Search Macros**           | Search for macros                                                                                           |
| **Get Macro**               | Get macro details                                                                                           |
| **Preview Macro**           | Preview what changes a macro would make to a ticket without actually applying them                          |
| **Apply Macro**             | Apply a macro to a ticket, executing all macro actions including field changes and comments                 |
| **List Articles**           | List Help Center articles                                                                                   |
| **Get Article**             | Get a Help Center article                                                                                   |
| **Search Help Center**      | Search across Help Center content                                                                           |
| **List Posts**              | List community posts                                                                                        |
| **Get Post**                | Get a community post                                                                                        |
| **List Ticket Audits**      | List all audits for a ticket including field updates, status changes, and assignments                       |
| **Get Ticket Audit**        | Get a specific audit record for a ticket                                                                    |
| **Get Ticket Metrics**      | Get performance metrics for a ticket including response times, resolution times, and SLA data               |
| **Batch Create Tickets**    | Create up to 100 tickets at once with full ticket options including custom fields, tags, and assignments    |
| **Batch Update Tickets**    | Update up to 100 tickets at once including status, priority, tags, custom fields, assignments, and comments |
| **List Talk Calls**         | List Zendesk Talk voice calls                                                                               |
| **List Talk Call Legs**     | List call legs for a Talk call                                                                              |
| **Download Talk Recording** | Download a Talk call recording                                                                              |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Find tickets:**

```text
Show me all open high-priority tickets from this week
```

**Create a ticket:**

```text
Create a ticket with subject "Login issue" for customer@example.com
```

**Update a ticket:**

```text
Set ticket 12345 to solved and add a comment "Issue resolved"
```

**Search users:**

```text
Find the user with email john@acme.com
```

**Check views:**

```text
How many tickets are in the "Unassigned" view?
```

**Preview a macro:**

```text
Preview what macro 456 would do to ticket 12345
```

**Apply a macro:**

```text
Apply macro 456 to ticket 12345
```

**Audit ticket history:**

```text
Show me all the changes made to ticket 12345
```

**Check ticket metrics:**

```text
What are the response times and SLA metrics for ticket 12345?
```

**Batch create tickets:**

```text
Create 3 tickets for the onboarding team: "Setup account", "Configure SSO", and "Schedule training"
```

**Batch update tickets:**

```text
Set tickets 101, 102, and 103 to solved with a comment "Resolved in bulk"
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific ticket IDs or user emails                                                                                              |
| Action not completing            | Check that you've authenticated with Zendesk                                                                                        |
| Unexpected results               | The agent may chain multiple tools (e.g., searching first, then updating). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                 |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Resolve the billing issue ticket" will find the ticket first, then update it. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Zendesk MCP server](https://www.gumloop.com/mcp/zendesk) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

### Zoom

*Manage meetings and recordings with AI-powered video conferencing automation.*

**Source:** https://docs.gumloop.com/nodes/mcp/zoom

Manage meetings and recordings with AI-powered video conferencing automation.

Zoom is a leading video conferencing platform for meetings and webinars. The Zoom MCP server lets you schedule meetings, list sessions, and retrieve recordings using natural language.

#### What Can It Do?

* **Schedule meetings** with specific details
* **List upcoming meetings** for any user
* **Get meeting details** from a link
* **Retrieve recordings** and transcripts

#### Where to Use It

##### In Agents (Recommended)

Add Zoom as a tool to any agent. The agent can then manage your meetings conversationally, choosing the right actions based on context.

*[Video]*

**To add an MCP tool to your agent:**

1. Open your agent's configuration
2. Click **Add tools** → **Connect an app with MCP**
3. Search for the integration and select it
4. Authenticate with your account

> **Tip:** You can control which tools your agent has access to. After adding an integration, click on it to enable or disable specific tools based on what your agent needs.

##### In Workflows (Via Agent Node)

For automated pipelines, use an [Agent Node](https://docs.gumloop.com/core-concepts/agent_node) with Zoom tools. This gives you the flexibility of an agent within a deterministic workflow.

##### As a Custom MCP Node

You can also create a standalone MCP node for a specific action. This generates a reusable node that performs one task, useful when you need the same operation repeatedly in workflows.

  *[Video: MCP Nodes tutorial]*

**To create a custom MCP node:**

1. Go to your node library and search for the integration
2. Click **Create a node with AI**
3. Describe the specific action you want (e.g., "Schedule a meeting for tomorrow")
4. Test the node and save it for reuse

> **Info:** Custom MCP nodes are single-purpose by design. For tasks that require multiple steps or dynamic decision-making, use an agent instead.

#### Setting Up Credentials

Connect your Zoom account via [Connectors page](https://www.gumloop.com/personal/connectors?provider=zoom). Follow the OAuth flow to grant access.

#### Available Tools

| Tool                       | Description             |
| -------------------------- | ----------------------- |
| **Create Meeting**         | Schedule a new meeting  |
| **List Meetings**          | List scheduled meetings |
| **Get Meeting**            | Get meeting details     |
| **Get Meeting Transcript** | Get transcript info     |
| **Get Meeting Recordings** | Get recording info      |

#### Example Prompts

Use these with your agent or in the Agent Node:

**Schedule a meeting:**

```text
Schedule a Zoom meeting for tomorrow at 2pm called "Team Sync"
```

**List meetings:**

```text
Show me my upcoming meetings this week
```

**Get meeting details:**

```text
Get the details for this Zoom meeting link
```

**Get recordings:**

```text
Get the recording for yesterday's team meeting
```

**Get transcript:**

```text
Get the transcript from this meeting
```

#### Troubleshooting

| Issue                            | Solution                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent not finding the right data | Use specific meeting topics or links                                                                                                              |
| Action not completing            | Check that you've authenticated with Zoom                                                                                                         |
| Unexpected results               | The agent may chain multiple tools (e.g., listing meetings first, then getting details). Review the agent's reasoning to understand its approach. |
| Tool not available               | Verify the tool is [enabled in your agent's MCP configuration](https://docs.gumloop.com/core-concepts/agents#tool-management-and-approvals)                               |

> **Tip:** Agents are smart enough to chain multiple API calls together. For example, asking "Get the transcript from the sales call" will find the meeting first, then retrieve the transcript. If results seem off, check the agent's step-by-step reasoning.

#### Need Help?

* [Agents documentation](https://docs.gumloop.com/core-concepts/agents) for setup and best practices
* [Agent Node guide](https://docs.gumloop.com/core-concepts/agent_node) for workflow integration
* Need help? [Reach out to us](https://portal.usepylon.com/gumloop/forms/help)
* Contact [support@gumloop.com](mailto:support@gumloop.com) for assistance

***

**Use this integration directly in Claude or Cursor.** Connect remotely via the [Zoom MCP server](https://www.gumloop.com/mcp/zoom) using credentials from your [Connectors page](https://www.gumloop.com/personal/connectors).

---