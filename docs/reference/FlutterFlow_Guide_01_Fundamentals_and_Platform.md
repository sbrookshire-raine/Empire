# FlutterFlow Documentation — Complete Guide (Part 1 of 7: Fundamentals, Account, CLI & Builder UI)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 51
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 1 of 7 — Fundamentals, Account, CLI & Builder UI
- **Other parts in this guide:**
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Accounts & Billing**

- [Account Management](#account-management)
- [Manage Custom Domains](#manage-custom-domains)
- [Payments & Billing](#payments-billing)
- [Plan Comparison](#plan-comparison)
- [Plans & Pricing](#plans-pricing)
- [Privacy And Terms Of Service](#privacy-and-terms-of-service)
- [Referral Program](#referral-program)
- [Refunds](#refunds)
- [Subscriptions](#subscriptions)

**Before You Begin**

- [App Development](#app-development)
- [Create an account](#create-an-account)

**Best Practices**

- [Best Practices: Secure API Keys](#best-practices-secure-api-keys)

**Collaboration**

- [Branching](#branching)
- [Saving and Versioning](#saving-and-versioning)

**Designer / App Builder**

- [Collaboration](#collaboration)
- [Components](#components)
- [Export](#export)
- [Import from FlutterFlow](#import-from-flutterflow)
- [Integrations](#integrations)
- [Iterate](#iterate)
- [Prompting](#prompting)
- [Quickstart](#quickstart)
- [Slides](#slides)
- [Workspace](#workspace)

**FlutterFlow CLI**

- [FlutterFlow CLI](#flutterflow-cli)
- [Build with AI Agents](#build-with-ai-agents)
- [Exporting Projects](#exporting-projects)

**FlutterFlow UI & Dashboard**

- [App Builder](#app-builder)
- [Canvas](#canvas)
- [Dashboard](#dashboard)
- [My Teams](#my-teams)
- [Resource Hierarchy Overview](#resource-hierarchy-overview)
- [Storyboard](#storyboard)
- [Toolbar](#toolbar)
- [Widget Palette](#widget-palette)

**Generated Code Reference**

- [Generated Code: Components](#generated-code-components)
- [DataTypeStruct class](#datatypestruct-class)
- [FFAppState](#ffappstate)
- [FlutterFlow Model](#flutterflow-model)
- [Generated Code: Pages](#generated-code-pages)
- [Directory Structure](#directory-structure)
- [FlutterFlow State Management](#flutterflow-state-management)

**Miscellaneous**

- [Additional Resources To Get Help](#additional-resources-to-get-help)
- [Application & Data Ownership](#application-data-ownership)
- [Customer Support Policy](#customer-support-policy)
- [Enterprise](#enterprise)
- [Hire FlutterFlow Developer](#hire-flutterflow-developer)
- [Security](#security)
- [Submit Bug Reports](#submit-bug-reports)

**Quickstart**

- [Quickstart Guide](#quickstart-guide)

**Roadmap**

- [Roadmap](#roadmap)

---

## Accounts & Billing

### Account Management {#account-management}

*This section contains information on changing your password, verifying your email, and deleting your account.*

**Source:** https://docs.flutterflow.io/accounts-billing/account-management

This section contains information on changing your password, verifying your email, and deleting your account.

##### I can't log in to my account / I forgot my login info.

To reset your account password:

1. From `flutterflow.io` select Login in the top right corner.
2. At the bottom of the page, select **Reset Password**.
3. You will receive an email with a link to reset your password.
4. Click the reset link and enter your new password.

If you can’t remember your username or are experiencing any other issues, please reach out to us at `support@flutterflow.io`

##### How do I change my password?

To change your password, please use the following steps:

1. Navigate to your [account page in FlutterFlow](https://app.flutterflow.io/account).
2. Under Personal Info, select Reset Password.
3. You will receive an email with a link to reset your password.
4. Click the reset link and enter your new password.

##### How do I check if my account is verified?

To check if you have verified your account:

1. Navigate to your [account page in FlutterFlow](https://app.flutterflow.io/account).
2. If you have a green checkmark next to your email, your account is verified.

![check-account-verification.png](https://docs.flutterflow.io/assets/images/check-account-verification-6e149bec567f3535f1e7cd83630e6c91.png)

##### I didn't get the email to verify my account, how do I resend the verification email?

If you did not receive a verification email, please follow these steps:

1. Navigate to your [account page in FlutterFlow](https://app.flutterflow.io/account).
2. Check that your email address is correct. If your email is incorrect, please reach out to `support@flutterflow.io` to correct this.
3. From the **Profile Information** section, select **Verify Email**.

You should receive a new confirmation email. If you do not receive the verification email, please contact us at <support@flutterflow.io>.

![email-verification.png](https://docs.flutterflow.io/assets/images/email-verification-d0cf7266c2f94c0dd089788be25f97a8.png)

##### How do I delete my account?

To delete your FlutterFlow account, please follow these steps:

1. Log in to your FlutterFlow account and select **Account** from the top right.
2. Scroll down to the **My Plan** section and select **Delete Account** (bottom right corner)

> **Danger:** This step can not be undone. We will not be able to recover your projects.

##### How do I change or update my email address?

To change your login email in FlutterFlow:

1. Log into your FlutterFlow account.
2. Go to the dashboard and select your account tile (showing your name and email).
3. Click on **Update Email**.
4. Enter your current email and password.
5. Input your new email and click **Confirm & Log Out**.
6. Verify the new email via the link sent to it.
7. Now, you need to create a new password for your new email address. To do so, click on the **Forgot Password** on the login page and enter your new email address.
8. You'll receive the password reset link at your new email address. Click the link and reset the password.

Now, you are ready to log in with your new email address and password.

![update-email.png](https://docs.flutterflow.io/assets/images/update-email-bf385749e89a9ee1251f7766e3d028a3.png)

##### How do I generate an API Token?

An API token is required to use the [CLI](https://docs.flutterflow.io/flutterflow-cli) and the [Visual Studio Code Extension](https://docs.flutterflow.io/concepts/custom-code/vscode-extension) .

To create an API token tied to your account:

1. Navigate to your [account page in FlutterFlow](https://app.flutterflow.io/account).
2. Near the bottom of the page, click **Create Token**

---

### Manage Custom Domains {#manage-custom-domains}

*All paid plans include one free custom domain, with the option to purchase more if needed.*

**Source:** https://docs.flutterflow.io/accounts-billing/manage-custom-domains

All paid plans include one free custom domain, with the option to purchase more if needed.

##### How do I purchase additional custom domains?

To purchase domains, paid users can go to their [**account**](https://app.flutterflow.io/account) page, find the **Custom Domains** section, and click the **Add Domains** button.

![add-domain](https://docs.flutterflow.io/assets/images/add-domain-84a700e31e777337a9020b211d5d11e7.avif)

The **Team** owner can purchase domains from the **My Team** page. Under the **Custom Domains** section, click **Add Domains** to add one for the team.

![add-domain-team](https://docs.flutterflow.io/assets/images/add-domain-team-67be7960a4784781dd35a82b46d31fd1.avif)

> **Note:** Note that purchasing a domain is not possible during the trial period. If you're interested in obtaining a domain, please reach out to our support team for further assistance.

##### How do I remove custom domains?

To remove the custom domain, paid users can go to their [**account**](https://app.flutterflow.io/account) page, find the **Custom Domains** section, and click **Remove Domains** to remove the existing custom domain.

The **Team** owner can remove domain from the **My Team** page. In the **Custom Domains** section, click **Remove Domains**.

![remove-domain-team](https://docs.flutterflow.io/assets/images/remove-domain-team-0e5a27ab84bb66dbba1da439fda3369c.avif)

---

### Payments & Billing {#payments-billing}

*This section contains information on the payment methods we accept and how to change your payment method.*

**Source:** https://docs.flutterflow.io/accounts-billing/payments-billing

This section contains information on the payment methods we accept and how to change your payment method.

#### Invoices

###### Can I Add A Tax ID (e.g. VAT) to my invoice?

If you need to include VAT in your invoices, please reach out to our support team at <support@flutterflow.io>, and we’ll be happy to assist you with the process.

#### Payment Methods

##### What payment methods do you accept?

We currently accept Visa, Mastercard, American Express, and JCB.

##### Can I use a gift card in addition to my credit card?

At this time we are unable to process Gift Card payments.

##### My payment failed, how can I change to a different credit card?

Failed subscription payments happen from time to time. These steps will help you troubleshoot the issue and update your payment method.

> **Info:** The most common causes for failed payments are insufficient funds, payment blocked by your credit card provider, or an expired card. If your payment fails, please reach out to your credit card provider for more details on why the payment failed.

You can use these steps to update your payment method on an open invoice (where your credit card has not been charged), you can change your payment method using these steps:

1. Head to the [My Account Page](https://app.flutterflow.io/account)
2. Select **Manage Billing**
3. Scroll to **Invoice History**
4. Locate the invoice that failed (should be at the top) and click the icon

![img\_17.png](https://docs.flutterflow.io/assets/images/img_17-91a070fe48a576c3e4425fe28ae995e7.png)

5. Enter your updated payment information

Once your updated transaction is successfully completed, your system access will be restored.

##### I used the wrong credit card, can I change it?

Once your subscription has been purchased, we unfortunately are unable to change your payment method for this month.

You can change your default payment method for next month's purchase using these steps:

1. After logging into your FlutterFlow, select [“Account”](https://app.flutterflow.io/account) from the top right.
2. In the **My Plan** section, select **Manage Billing.**
3. Scroll down to the **Payment Methods** section.
4. Select **+ New Payment Method,** enter your payment details, and then select **Add.**
5. Remove your old payment method by selecting the three dots to the right of your payment and then selecting **Delete.**

> **Note:** You can change the default payment method by selecting the three dots next to the payment method and then selecting **Make Default.**

---  ### Plan Comparison {#plan-comparison}

*Compare FlutterFlow plans and features to find the right plan for your needs*

**Source:** https://docs.flutterflow.io/accounts-billing/plan-comparison

Choose the plan that fits your development needs and team size.

← Scroll horizontally to see all plans →

Currency:

USDINR

Billing:

MonthlyAnnual

| Plan                                                                                                             | Free; $0; per month         | Basic; $39; per month                                     | Growth; 1st seat: $80, 2nd seat: $55; per month           | Business; 1st seat: $150, Seats 2-5: $85 each\*; per month | Enterprise; Custom; pricing |
| ---------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------- |
| **Core Platform Features**                                                                                       |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Visual Development Environment; Drag & drop builder for creating apps visually                               | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| 1K+ Prebuilt Templates; Ready-to-use app templates and components                                            | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Project Count; Number of projects you can create                                                             | 2 projects                          | Unlimited                                                         | Unlimited                                                         | Unlimited                                                          | Custom                              |
| AI Generation; AI-powered assistance for building and coding                                                 | 5 requests/lifetime                 | 50 requests/mo                                                    | 200 requests/mo                                                   | 500 requests/mo                                                    | Custom                              |
| **Data & Integrations**                                                                                          |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Firebase Integration; Connect to Firestore, Firebase Auth, and more                                          | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Supabase Integration; Connect to Supabase for database and auth                                              | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| AI Agents; Create AI agents with OpenAI, Anthropic, and Google                                               | 0                                   | 1                                                                 | Unlimited                                                         | Unlimited                                                          | Unlimited                           |
| API Endpoints; Connect to external APIs and services                                                         | 2                                   | Unlimited                                                         | Unlimited                                                         | Unlimited                                                          | Custom                              |
| Swagger/OpenAPI Imports; Import API specifications automatically                                             | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Development Environments; Separate databases and configuration values for testing and production             | 1 (default only)                    | 1 (default only)                                                  | Up to 1 additional (+default)                                     | Up to 2 additional (+default)                                      | Custom                              |
| **Development Features**                                                                                         |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Code Extensibility; Add custom code to extend functionality                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Live Debugging; Test your app in the browser and hot reload                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Test Mode Session Expiration; How long a Test Mode session remains active before expiring                    | 20 minutes                          | No expiration                                                     | No expiration                                                     | No expiration                                                      | No expiration                       |
| Visual Logic Builder; Create app logic with a visual editor                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| State Management; Manage app data and user interface states                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Custom Code Expressions; Write custom expressions and logic                                                  | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| One-Click Localization (i18n); Automatically translate your app using Google Translate API                   | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Push to GitHub; Push your project code to GitHub                                                             | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| VS Code Extension; Sync custom code files back and forth between FlutterFlow and VS Code                     | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Automated Testing; Run automated tests on your applications                                                  | ❌                                  | ❌                                                                | 1 test per project                                                | Up to 3 tests per project                                          | Unlimited tests                     |
| Test Pilot; AI-powered QA testing with additional credits                                                    | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Custom Classes; Bring custom Dart classes into your app                                                      | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| YAML Editing; Refactor your project with by editing the YAML representation                                  | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Project API; Programmatic access to project data                                                             | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| MCP Server (Experimental); Model Context Protocol server integration                                         | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Cloud Functions; Write and deploy Firebase Cloud Functions directly from FlutterFlow                         | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| CLI; Command-line interface for downloading code and project management                                      | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Configuration File Snippets; Directly modify Info.plist, main.dart, Android manifest, and other config files | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Local Run Desktop Emulator; Run code locally with automatic environment setup                                | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| **Design Features**                                                                                              |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Design Systems; Consistent color schemes, typographic, icons, and more                                       | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Animations & Haptic Touch; Add animations and haptic feedback to your app                                    | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Custom Fonts & Icons; Upload and use custom fonts and icons                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Custom Typography Presets; Create reusable text styles and presets                                           | ❌                                  | ❌                                                                | ❌                                                                | ✅                                                                 | ✅                                  |
| Screenshot Generator; Generate app screenshots automatically for App Store review                            | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Figma Theme Import; Import color and typography themes from Figma                                            | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Figma Frame Import; AI-powered import of Figma frames to FlutterFlow                                         | ❌                                  | ❌                                                                | ❌                                                                | 100 requests/mo                                                    | Custom                              |
| **Advanced App Features**                                                                                        |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Push Notifications; Send notifications to app users                                                          | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Payments Integration; Integrate Stripe and other payment providers                                           | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Ads Integration; Monetize your app with advertisements                                                       | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Third-Party Package Imports; Add pub.dev packages and GitHub dependencies                                    | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Debug Panel; Advanced debugging tools and console                                                            | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| **Collaboration Features**                                                                                       |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Number of Editors; Team members who can edit projects                                                        | 1                                   | 1                                                                 | Up to 2                                                           | Up to 5\*                                                          | Custom                              |
| Single Project Collaborator Add-Ons; Allow non-team members to collaborate on a single project               | None                                | None                                                              | Up to 4 collaborators available for purchase                      | Up to 10 collaborators available for purchase                      | N/A                                 |
| Real-Time Collaboration; Work together on projects simultaneously                                            | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Project Commenting; Add comments and feedback to projects                                                    | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Manual Commits; Make explicit named commits to the current branch for version control                        | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Number of Branches; Create and manage multiple project branches (all plans include main branch)              | 1 (main only)                       | 1 (main only)                                                     | Up to 2 open branches (+main)                                     | Up to 5 open branches (+main)                                      | Custom                              |
| Automated Snapshot Backups; Automatic project backups and version control                                    | Up to 1 hour prior                  | Up to 1 day prior                                                 | Up to 3 days prior                                                | Up to 7 days prior                                                 | Custom                              |
| Activity Logging; Track project changes and user activity                                                    | ❌                                  | ❌                                                                | ❌                                                                | ❌                                                                 | ✅                                  |
| Project Level Access Control; Manage permissions for individual projects                                     | Manage view-only collaborators only | Manage view-only collaborators only                               | ✅                                                                | ✅                                                                 | ✅                                  |
| Centralized Billing; Manage team billing from one account                                                    | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| **Library Features**                                                                                             |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Library Imports; Add FlutterFlow libraries to your projects                                                  | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Library Publishing; Publish your projects as reusable libraries                                              | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| **Deployment**                                                                                                   |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Web Deployment; Deploy your app as a web application                                                         | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Free Subdomains; Deploy your web app to FlutterFlow subdomains                                               | Up to 2                             | Up to 20                                                          | Up to 20                                                          | Up to 20                                                           | Unlimited                           |
| Custom Domains; Deploy to your own custom domain                                                             | ❌                                  | Connect 1 domain for free, additional connections will be charged | Connect 1 domain for free, additional connections will be charged | Connect 1 domain for free, additional connections will be charged  | Custom                              |
| Custom Web Favicon; Set custom favicon for web publishing                                                    | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| FlutterFlow Watermark Removal; Remove FlutterFlow branding from published apps                               | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Code Download; Download your project's source code                                                           | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| APK Download; Download Android APK files                                                                     | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| One-Click Apple & Google Store Deployment; Deploy directly to app stores with one click                      | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| **Support**                                                                                                      |                                     |                                                                   |                                                                   |                                                                    |                                     |
| Account and Billing Support; Help with account management and billing questions                              | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Community Support; Access to FlutterFlow community forums                                                    | ✅                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Email Support; Get help via email from our support team                                                      | ❌                                  | ✅                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| In-App Support; Chat support directly within FlutterFlow                                                     | ❌                                  | ❌                                                                | ✅                                                                | ✅                                                                 | ✅                                  |
| Dedicated Live Support; Direct access to dedicated support specialists                                       | ❌                                  | ❌                                                                | ❌                                                                | ❌                                                                 | ✅                                  |

#### Business Plan Extensions

##### \*Agencies Expansion

Includes all Business features, plus the ability to add up to 7 additional seats (12 total per team) at **$85/seat/month** (USD) or **₹2,850/seat/month** (INR) and collaborate with up to 20 other paid users at the project level via Single Project Collaborator Passes. Must be approved as an Expert Agency via [Contra](https://contra.com/opportunity/rWlmk2Yv-become-a-flutter-flow-agency).

##### Localized Pricing

INR pricing reflects localized rates adjusted for local purchasing power, providing the same features and plan structures as USD pricing. All plans include the same comprehensive feature set regardless of currency.

---

### Plans & Pricing {#plans-pricing}

*For our most up-to-date information, please visit FlutterFlow pricing.*

**Source:** https://docs.flutterflow.io/accounts-billing/plan-pricing

> **Info:** For our most up-to-date information, please visit **[FlutterFlow pricing](https://flutterflow.io/pricing)**. Regional discounts are available, please **[log in to FlutterFlow](https://app.flutterflow.io/)** to see the pricing for your region.

#### Pricing Update \[June 2025]

FlutterFlow has evolved significantly, from a visual builder to a complete development environment with features like code export, GitHub integration, branching, AI agents, and app deployment tools. As the platform has matured, so have the ways people use it. To better reflect how teams build and scale today, we're introducing updated pricing plans. These updates will help us continue improving the platform, supporting your workflows, and delivering the advanced features needed for building production-ready apps.

##### What's Changing?

As part of broader improvements to the platform, FlutterFlow is updating its pricing and packaging model effective **August 18, 2025**. The update introduces new plan tiers aligned with team size, simplifies billing, and ensures better alignment between user needs and platform capabilities.

**Key Changes**

* We're retiring our legacy plans: **Standard**, **Pro**, and **Teams** and introducing a new, simplified lineup: **Free**, **Basic**, **Growth**, **Business**. Our Enterprise offering will continue as is, providing advanced features and support for larger teams.
* If you're already using FlutterFlow, you'll be automatically moved to the new plan that best fits your current team size. No action needed on your part.
* That said, feature access will look a little different. Some users will gain powerful new capabilities, while others might see a few features move to higher tiers.

To understand how each new plan compares, **[view the detailed plan comparison](https://docs.flutterflow.io/accounts-billing/plan-comparison).**

#### FAQS

##### General / Timeline

Who is affected by this pricing change?

All current Free, Standard, Pro, and Teams plan users will move to the new structure.

Enterprise customers on custom contracts are not affected by these changes.

When does the new pricing take effect for me?

* For new users, the pricing and packaging will apply immediately on August 18, 2025. After this date, no legacy plans (Standard, Pro, Teams) can be purchased or updated.

* For existing Free, Standard, Pro, and Teams plan users, billing and feature access will remain unchanged during a **30-day transition period** where you will have the ability to select a new plan. On September 18, 2025, your account will be moved to one of the new plans if no action is taken.

  * **Important exception:** If you're currently on a Teams plan, you will no longer be able to use your team features on personal projects starting August 18, 2025. To maintain existing Teams plan feature access on those projects, you must either: * Move your personal projects into your Team, or
    * Convert your current Teams plan to a new Growth or Business plan and purchase a separate Basic plan for your personal work.

* **Note:** All plan updates will take effect at 12:00 AM local time on the specified effective date.

![Pricing Update Timeline - 2025](https://docs.flutterflow.io/assets/images/pricing-timeline-2025-light-8cba34a0d150e869d9848ff396cf9721.png)![Pricing Update Timeline - 2025](https://docs.flutterflow.io/assets/images/pricing-timeline-2025-dark-462f7c30b4684ef64f55daca68e988ff.png)

Why is FlutterFlow updating its pricing?

When we launched FlutterFlow, we had one goal: make it radically easier to build beautiful, powerful digital products. Four years later, we’re a full development platform that goes from idea to app store. We now have collaboration features, AI tools, lots of integrations, branching, development environments, and more, built in.

Now our plans are evolving to reflect that growth. We’ve introduced new features across every tier and restructured our plans to better align with the way people build today and how their needs change as they move from MVP to scaling production apps.

##### Plans

How do the new plans differ from the current plans?

The new plans introduce pricing by team size, differentiation between team and personal projects, and more structured feature access to support different types of users and teams as they grow.

Key changes include:

* New plan tiers based on team size, with clearer limits of number of developers that can work together.
* Collaboration primarily at the team level to support scalable workflows and controls, with a new option to enable single-project collaboration as an add-on.
* Updated feature access, with certain advanced features now only available in higher tiers.
* Plan-based Support levels, with availability varying by plan.
* Revised pricing structure, with updated USD and INR rates.

For a detailed comparison of the current and new plans, including feature breakdown and pricing, please see the **[Detailed Plan Changes](https://docs.flutterflow.io/accounts-billing/plan-comparison)** table above.

What is the difference between team projects and personal projects?

[**Team + Restricted Team Projects:**](https://docs.flutterflow.io/resources/projects/collaboration/)

* Give you access to all the features of your Growth or Business plan
* Can be shared with your whole team, or restricted to specific members
* The team owner always has access to every project in the team

**Personal projects:**

* Belong only to you; team owners cannot access them
* Only include the features available in your personal plan
* Note: If you want to use Growth or Business features by yourself, you can create a team of one

To update the collaboration type of a project, go to the Collaboration tab in your project settings and choose from one of the following options: Team Project, Personal Project, or Restricted Team Project

Which plan is best suited for different types of users?

The tiers are designed as a general guide to help highlight which plans tend to work best for different types of use cases, but we know that every user’s needs are different and you’re always welcome to choose the one that works best for you. That said, here’s how we generally recommend thinking about the tiers based on common usage patterns:

* **Free:** App builders learning and prototyping.
* **Basic:** Independent builders shipping production-ready apps.
* **Growth:** Solo developers or small teams needing advanced functionality.
* **Business:** Established teams (3–5 users) ready for advanced development workflows.
* **Enterprise:** Larger teams needing advanced security, governance, and collaboration features.

How do I know which plan I will be moved to if I do not make a selection before September 18, 2025?

If you do not make a selection during the election period (August 18, 2025 - September 17, 2025), your new plan will be automatically determined based on your current **team size**. For example:

* Users on the Free plan will remain in the Free plan, but with new feature restrictions.
* Solo users in Standard will move to the **Basic** plan.
* Pro plan users and Teams of 2 will move to the **Growth** plan.
* Teams of 3-5 will move to the **Business** plan.
* Teams with 6+ users will move to the Business plan and retain their current seat count as of September 18, 2025 for up to 12 months. During this period, no additional seats can be added. After 12 months, you will need to upgrade to an Enterprise plan to continue building with more than 5 team seats.
* * We highly encourage you to begin evaluating your team’s resourcing and expansion needs early, as this plan will not support usage growth beyond the feature limits of the Business tier. Early planning and engaging with our sales team can help ensure a smooth migration, avoid disruption, and prevent any risk of project or data access issues at the 12-month cut-off. To start the conversation, please reach out to [](mailto:sales@flutterflow.io)<sales@flutterflow.io> to explore the best solution package for your team.
  Expert Agencies (approved via [**Contra**](https://contra.com/opportunity/rWlmk2Yv-become-a-flutter-flow-agency)) will move to the **Business** plan with Agencies Expansion included.

We'll notify you directly in the app and by email before the September 18, 2025 migration, so you'll have a chance to review or adjust your plan if needed. If you're unsure, contact us and we'll help you confirm your new plan

Are there any benefits to electing into a new plan vs. being auto-migrated?

Yes! By proactively choosing to move to any of the new plans with annual billing during the election period (before September 18, 2025), you will receive **20% off your first year**.

Can I stay on my old plan?

No. All existing plans will be retired on September 18, 2025, and users will be automatically transitioned to the new plans based on their current team size. This helps us simplify billing, improve feature alignment, and deliver a more consistent experience across all teams.

If you’re currently a paying user and would prefer not to be part of the migration to one of the new paid plans, you have two paths:

* **Continue building on the Free plan**: you can downgrade your plan to Free, where you will be able to view, edit, and run any 2 existing projects of your choosing inside the editor, but paid‑tier features, deployments, and team seats will be disabled until you upgrade.
* **Export your code**: download the full Flutter source and assets for each project before September 18, 2025 and continue building locally to retain full ownership of your codebase.

If you’d like to review your options or adjust your usage ahead of time, our support team is here to help. You will receive an email confirming the plan your account will move to, but can also confirm by logging into your account after August 18, 2025 to see how your team maps to the new tiers.

What's included in the Enterprise plan?

The Enterprise plan is built for organizations that need advanced security, scale, and white-glove support while managing production-grade apps across teams. In addition to all features available in lower tiers, Enterprise includes:

* Controlled FlutterFlow upgrades through version pinning
* Unlimited access to automated snapshot backups for project history and rollback
* Single Sign-On (SSO) and Activity Logging for secure, centralized access
* Unlimited development environments to mirror staging, QA, and production workflows
* Advanced accessibility features to meet regulatory requirements
* No automatic right for FlutterFlow to use your logo
* Live and dedicated technical support, plus access to custom engineering solutions when needed

To learn more or explore a custom Enterprise solution for your team, please reach out to [](mailto:sales@flutterflow.io)<sales@flutterflow.io> – we'd be happy to walk you through options that match your scale and needs.

##### Feature Access

Will my existing FlutterFlow apps stop working?

1. No, your current apps will continue to function and remain deployed, though access to certain features may change depending on your new plan tier starting September 18, 2025.; 2. If you elect into a new plan during the election period before September 18, 2025, those feature changes will take effect as soon as your new plan becomes active.; ; What happens to features I already use but are not part of my new plan?

* Access to features will be updated according to your new plan beginning September 18, 2025. If you're currently using a feature that is moving to a higher tier, there are two possible outcomes:

  * **Build-time features** (like activity logging, automated testing, or Figma Frame imports) will no longer be accessible. You’ll see an upgrade prompt if you attempt to use them.

  * **Run-time features** (like API endpoints, branching, GitHub integration, or dev environments) will be grandfathered and continue to work as-is, but you won’t be able to create additional instances beyond what you already have. For example:

    * If you are currently building on a Free plan with 3 API endpoints, you can continue editing them, but won’t be able to add a 4th without upgrading to a paid plan.

    * If you’ve used branching or added multiple development environments and currently exceed your new plan limits, those remain active but you’ll be prompted to upgrade if you try to add more.

* This approach ensures existing work isn’t disrupted, while still aligning future access with your selected plan.

##### Free Users

I am a Free user and I will lose access to technical support. Where else can I look to for help when building?

* Starting August 18, 2025 for new users and September 18, 2025 for existing users, 1:1 support will no longer be included with the Free plan. However, we offer a collection of self-serve resources to help you continue building with confidence:

  * Our Help Center at [docs.flutterflow.io](http://docs.flutterflow.io) offers a free collection of step-by-step guides on how to build, get started, and make the most of FlutterFlow’s features.

    * We are also launching new troubleshooting guides to help you resolve common issues and workflows.

    * Plus, a new AI-powered assistant will help you quickly find answers and relevant resources within the Help Center.

  * You can turn to our [Community Forum](https://community.flutterflow.io/) to ask questions, share learnings, and get help from other FlutterFlow builders.

  * We also offer free educational content via our [YouTube channel](https://www.youtube.com/@flutterflow) to support your learning and skill development.

* These resources are designed to help all users succeed without needing to rely on 1:1 technical support.

  * Our Support team will still be available at [](mailto:support@flutterflow.io)<support@flutterflow.io> to all users to assist with billing or account-related issues.

I am a Free user and have more than 2 projects – what will happen to them?

* Starting September 18, 2025, all personal Free plan projects will be archived until you actively select two to keep editable. This selection is permanent and cannot be changed afterwards. All other projects will be archived – they'll still appear on your dashboard, and published apps will remain live, but you won't be able to open, edit, or publish updates unless you upgrade.

  * **Marketplace exception:** Existing Free plan projects published to the Marketplace prior to August 18, 2025 will not count toward your 2-project limit. If a project is later removed from Marketplace and you exceed the limit, it will be automatically archived.

* For users on a team-based plan but not on a personal paid plan, this 2-project selection requirement only applies to your personal projects. You will still be able to edit any projects that belong to your team.

* We've set this policy to ensure everyone can explore FlutterFlow for free while keeping heavy usage sustainable. We won't remove any of your existing projects. They're safe and accessible whenever you decide to upgrade.

Can I still deploy my existing FlutterFlow apps if I stay on the Free Plan with >2 projects?

Any existing projects already live will remain deployed, even if you have more than 2 projects currently deployed. However, on the new Free plan, you’ll be limited to editing and publishing updates to at most 2 active projects. All other projects will remain deployed, but you won’t be able to make changes or redeploy them unless you upgrade to a paid plan.

What if I delete one of my 2 active projects?

If you delete one of your active projects, we’ll automatically unarchive your most recently edited archived project to replace it.

If you only had 2 projects total and delete one, you’ll be able to create a new project instead.

##### Teams (Growth/Business)

What happens to projects with multiple collaborators?

Starting September 18, 2025, all project collaboration must occur within a team (Growth or Business). This means:

* **Team projects.** Everyone on your team keeps full edit access. Any project collaborator who is not a paid seat on your team will be switched to view-only access at the project level until they’re added as a paid team member.
* **Projects not associated with a team.** The project owner keeps full edit access and all other project collaborators become view-only members on that project. To keep editing together, move the project into a team and invite those collaborators as team members.
* **Solo projects:** If you are the only editor, nothing changes. You retain full edit access.

Note: If you choose to migrate to a new paid plan before September 18, 2025, any collaborators not on your team will immediately move to view-only access at the time of conversion.

I’m currently on a Teams plan and want to change the number of users. Can I still do this on or after August 18, 2025?

No. As a part of the existing Teams plan retirement, team size will be locked on August 18, 2025. To adjust your team size after that date, please transition to one of the new plans (Growth or Business).

I am currently on a Teams plan with 6+ users and do not want to migrate to the Enterprise plan – how do I stay on the Business tier and how will I be charged?

* Teams with more than 5 users who do not wish to move yet to an Enterprise contract can continue on the Business tier under a transitional pricing structure. These teams will be billed at the standard Business tier seat pricing and then $85/seat/month for each additional seat over 5. Pricing will be based on the number of users in the team as of September 18, 2025 and billed on a monthly basis.

- This option allows larger retail teams to continue operating under the Business feature set without immediate contract negotiation, but will be available only to existing 6+ seat teams for 12 months from September 18, 2025 through September 18, 2026 to ensure continuity without immediate contract negotiation.

* Note: Your seat count will be locked based on your team size as of September 18, 2025. You may reduce seats later, but will not be able to add more or expand beyond the feature set and usage limits of the current Business tier (except for any run-time features already in use that are grandfathered).

However, if you would like to maintain a single account, collaboration across all of your team members, enterprise level features and support, please reach out to [](mailto:sales@flutterflow.io)<sales@flutterflow.io>.

Can I belong to multiple teams? How will that be billed?

Yes, starting August 18, 2025, users will be able to belong to multiple teams in FlutterFlow in the new plans – this is a new capability as part of our updated team and collaboration structure. Each team is treated as a separate billing entity, with its own plan, users, and usage limits.

If you are added as an editor on more than one team, you will count toward the seat total on each of those teams, and each team will manage your seat and billing as part of their own subscription. You will not be billed individually – all billing remains centralized at the team level.

Note: you can also be added as a view-only collaborator on projects that are a part of different teams. View-only collaborators do not count toward any seat limits or billing.

Can I share projects across multiple teams?

* No, projects cannot be shared across multiple teams. Each project belongs to at most one team, and access is managed within that team’s structure.
* If you want someone from another team to collaborate on a project, they must be invited into your team as an editor or granted access using a Single Project Collaborator Pass.

What if I want to continue collaborating with project collaborators who are not on a Teams plan with me?

* With the new pricing model, collaboration is only supported within shared Teams plans. This means that to work together on a project, all collaborators must be part of the same Growth, Business, or Enterprise team. However, users can now be members of multiple teams at the same time, which allows you to create separate teams for different projects, depending on who you need to collaborate with.

* Project-level collaboration (where individuals outside your team could be added to specific projects) is being phased out to simplify permissions, ensure security, and support shared billing.

* If you would like to continue collaborating: * You can invite others to join your team (additional seats may require an upgrade depending on your plan).
  * Or, they can create a new team and invite you, depending on who should own billing and project access.
  * **New:** If you're on a Growth or Business plan, you may also purchase Single Project Collaborator passes, which allows you to grant another paid user access to a single project without adding them to your full team. Each pass is $15/month and can be reassigned to different collaborators or projects as needed. You can purchase up to 4 (Growth) or up to 10 (Business). This collaborator must also be on a paid plan to be eligible to be a single project collaborator.

* This change ensures that every project has clear ownership, consistent permissions, and a scalable path for team-based collaboration.

I build apps for clients (agency/freelancer). What plan should I choose?

* We will now offer multiple plan options to support agencies of all sizes – whether you’re a solo freelancer, a fast-growing studio, or an established consultancy. We believe the best path depends on your team size and how you prefer to work with your clients:

  * Solo freelancers or small agencies (1-5 developers)

    * We recommend the Business plan, which supports up to 5 team members with advanced features like branching and access control.

  * Agencies with more than 5 developers:

    * If your client plans to manage the code:

      * We recommend encouraging your client to purchase their own Business or Enterprise plan and then invite your agency developers to join, either as [Team members or as collaborators](https://docs.flutterflow.io/resources/projects/collaboration/) (with a collaborator pass). To learn more about our Enterprise offering, they can reach out to [](mailto:sales@flutterflow.io)<sales@flutterflow.io>.

    * If you intend to maintain the code on behalf of your client:

      * You may qualify for our new Agencies Expansion package, coming out with the Business plan and available to all verified FlutterFlow Expert Agencies.

        * As part of the add-on, you can:

          * Continue to purchase additional seats beyond the 5 included in Business at $85/seat/month
          * And, continue to invite additional paid users to specific projects without requiring them to be team members via Single Project Collaborator Passes.

        * To become eligible now, you can apply to be an Expert Agency on our [Contra](https://contra.com/opportunity/rWlmk2Yv-become-a-flutter-flow-agency) page. Existing Expert Agencies listed on Contra will be pre-approved to select the Agencies Expansion package starting August 18, 2025.

You can transfer ownership of projects between yourself and your client. To transfer a project to a client, simply add them as a collaborator using a pass, transfer ownership, and then remove them and the pass if no longer needed after the handoff.

##### Billing

How will my billing cycle be affected when I move to the new plan?

To ensure a smooth transition, billing changes will align with your existing billing cycle:

* You will stay on your current pricing until your next billing renewal (monthly or annual). For example:
* * If your monthly billing date is September 3, 2025, your features will switch to the new plan on September 18, 2025 (or earlier if you elect to switch), but new pricing will apply starting your next billing cycle on October 3, 2025.
  * If you’re on an annual plan, your price won’t change until your next annual renewal. After that, the new pricing will apply for the following 12 months.
  You will have the option to upgrade early to the new pricing plan if you choose, with any remaining credit from your current plan applied toward the new plan.

If you are currently on an annual plan and choose to cancel your subscription during the transition period (August 18, 2025 - September 17, 2025), you will be eligible for a pro-rated refund. This is to account for any features you may have prepaid for under your current plan that will no longer be available once the new plans take effect.

If you have questions about your billing, please contact support at [](mailto:support@flutterflow.io)<support@flutterflow.io>

Will there still be a discount for paying annually on the new plans?

Yes, we will continue offering a meaningful discount on all new plans when billed annually instead of monthly – typically around 25%. This discount remains available regardless of your location or currency and reflects 12 months of service at a reduced monthly rate.

*Note: Annual billing is not available for Business teams with greater than 5 seats on transitional pricing, as this is intended to support existing users during their migration period.*

How will prices change with respect to country discounts?

Localized pricing will continue where applicable. If you’re in a supported region, your billing will reflect adjusted rates at existing discounts based on your location.

What if I am billed in INR right now?

If your account is billed in INR, your pricing will follow our localized rates:

* **Basic Plan:** ₹1,300 INR per seat per month.
* **Growth Plan:** ₹2,650 INR for the first seat, and ₹1,850 INR for the second seat per month.
* **Business Plan:** ₹5,100 INR for the first seat, and ₹2,850 INR each for seats 2–5 per month.
  * Agencies Expansion: Each additional seat beyond 5 at ₹2,850 INR/month.

All INR pricing reflects the same features and plan structures as USD pricing, with adjustments for local purchasing power.

##### Miscellaneous

I have special access. How will this change impact me?

* If you currently have Special Access (such as through a community program, academic use, or other exception), your FlutterFlow experience will remain unchanged. You will continue to have the same benefits provided under your existing Special Access status, which is separate from the new plan structure.

* **Note:**

  * Users with Special Access can collaborate with an unlimited number of users, but those collaborators must also have either Special Access or be on a paid teams (Growth or Business) plan.
  * Special Access may be granted at either the individual or team level. If only the individual has Special Access, they will not have full feature access when working on team projects unless the team also has Special Access.

Will the referral program still exist with the new plans, now that the Pro plan is going away?

* With the retirement of the Pro plan, our current referral program will also be sunset. This means any active referral discounts will end at your next renewal. However, any earned referral credits will remain in your account and can be redeemed for equivalent free months of the new Growth plan.
* We’re actively exploring what a future referral or incentive program could look like under the new pricing model, with the goal of better supporting and rewarding our community as we grow.

Are there any changes to DreamFlow plans as well?

Dreamflow is a separate product and Dreamflow plans are not affected by this plan update.

---

### Privacy And Terms Of Service {#privacy-and-terms-of-service}

*How do I request the deletion of my personal data?*

**Source:** https://docs.flutterflow.io/accounts-billing/privacy-terms-of-service

##### How do I request the deletion of my personal data?

To request deletion of your personal data, please reach out to our support team at <support@flutterflow.io>

##### How do I request a copy of my personal data?

To request deletion of your personal data, please reach out to our support team at <support@flutterflow.io>.

##### How do I unsubscribe from email communications / marketing emails?

To unsubscribe from FlutterFlow emails, please click the “Unsubscribe” link in the footer of our emails.

##### Where can I view your Privacy Policy?

You can review the most recent version of our Privacy Policy [on the website](https://www.flutterflow.io/privacy).

##### Where can I view your Terms of Service (ToS)?

You can review the most recent version of our Terms of Service [linked on the website](https://www.flutterflow.io/tos).

---

### Referral Program {#referral-program}

*With the retirement of the Pro plan, the existing referral program has been discontinued. Any active referral discounts will end at your next renewal. However, referral credits you’ve already earned will remain in your account and can be redeemed for free months on the new Growth plan.*

**Source:** https://docs.flutterflow.io/accounts-billing/referral-program

Discontinued

With the retirement of the Pro plan, the existing referral program has been discontinued. Any active referral discounts will end at your next renewal. However, referral credits you’ve already earned will remain in your account and can be redeemed for free months on the new Growth plan.

We are also exploring new referral and incentive programs to better support and reward our community under the updated pricing model.

---

### Refunds {#refunds}

*If you're not happy with your FlutterFlow subscription, you can cancel at any time.*

**Source:** https://docs.flutterflow.io/accounts-billing/subscriptions/refunds

If you're not happy with your FlutterFlow subscription, you can [cancel at any time](https://docs.flutterflow.io/accounts-billing/subscriptions/subscriptions#cancel-my-plan).

However, there are no refunds for cancellation. In the event that the Company suspends or terminates your Account or these Terms, you understand and agree that you shall receive no refund, whether for any unused time on a subscription, any license or subscription fees for any portion of the Service, any content or data associated with your User Account, or for anything else.

---

### Subscriptions {#subscriptions}

*This section provides information on free trials, plan changes, and other subscription-related questions.*

**Source:** https://docs.flutterflow.io/accounts-billing/subscriptions/subscriptions

This section provides information on free trials, plan changes, and other subscription-related questions.

#### Free Trials

The first paid plan you purchase will come with a free 14-day trial. For 14 days, you will have access to the features of the plan you selected before you are charged. If you can cancel your subscription during this 14-day trial, you will not be charged.

> **Info:** The 14-day trial applies only to your first paid plan. Any later plan (Basic, Growth, or Business) won’t include a trial, even if the first plan is still in trial.

##### How do I start a free trial?

To start a free trial, please follow these steps:

1. Navigate to [app.flutterflow.io](http://app.flutterflow.io/)
2. Click the “Create Account” text and enter your name, email address, and password. Then press the “Create Account” button to create your account.
3. Validate your email address by clicking on the link in the message sent to the email address you provided.
4. To start trialing on a **Basic** plan, click on your profile picture in the bottom left corner, then click “Upgrade Plan.” Select “Start Free Trial” and fill out and submit the form with your payment information.
5. To instead start trialing on a **Growth** or **Business** plan, click “My Team”, and create a team. Then press the “Subscribe” button, select your desired plan and number of seats, click on “Start Free Trial”, and fill out and submit the form with your payment information.

##### What happens at the end of the trial period?

At the end of your trial period, your payment method will be charged. You can cancel at any time during the trial period.

#### Upgrade Plan

##### How do I upgrade my plan?

If you would like to upgrade from a Basic plan, follow the steps to purchase a new Growth or Business plan, and then cancel your existing Basic plan if you no longer want it.

To upgrade a team directly from a Growth plan to a Business plan, please follow these steps:

1. Click on “My Team” and select the team that has the Growth plan you wish to upgrade.
2. Click on “Upgrade to Business Plan” near the top right corner.
3. View the invoice and confirm that you are willing to be charged this amount for the upgrade.

##### How do I check what plan I am subscribed to?

To view your plan details, go to the [**FlutterFlow Account Page**](https://app.flutterflow.io/account) and select **Manage Billing.** The **Current Plan** section will show which plan(s) you are subscribed to.

#### Downgrade Plan

##### How to downgrade?

If you wish to downgrade from Growth to Basic or from Business to Growth or Basic, you should cancel your existing plan and then sign up for the new one after it expires.

##### What happens when I downgrade to the free plan? Will my projects be deleted?

On the free plan, you will be restricted to two projects. Any other projects won't be deleted, but will be archived and made accessible if you return to any paid plan.

#### Cancel My Plan

You can cancel your plan at any time. You will have access to the paid features until your next billing cycle date.

Please follow these steps to cancel your account:

1. Log in to FlutterFlow and click on your profile picture to go to the Account page.
2. Find the plan you want to cancel, and select **Cancel Plan**.
3. Complete the Cancellation Survey and select **Cancel Subscription.**

> **Warning:** Your FlutterFlow account can have multiple team plans and a personal plan at the same time; you must cancel each plan manually. Canceling one plan does not automatically cancel any other active plan.

#### Other Subscription Questions

##### When will my plan renew / When will I be charged?

You can view the next billing cycle date in the "My Plan" section of the [Flutterflow Account Page](https://app.flutterflow.io/account).

![renew](https://docs.flutterflow.io/assets/images/renew-b7de713dccd5a228d37fb4534fd1cf72.png)

The next billing cycle date for this plan is September 12, 2025.

##### Do subscriptions renew automatically?

Yes, our subscriptions renew automatically to avoid disrupting your app development. Monthly subscriptions renew on the same day each month (typically the day you subscribed).

##### Can I pause my subscription?

We do not currently offer the option to pause your subscription.

##### Can I transfer my subscription to another user?

We are unable to transfer a paid FlutterFlow subscription to another FlutterFlow account.

##### If I have a paid plan, will project collaborators be able to use paid features?

No. Having a paid plan yourself does not give your project collaborators access to paid features. Starting **September 17, 2025**, all collaboration must happen within a **Growth, Business, or Enterprise plan**, and every collaborator must have a **paid seat** in that team to have full edit access. Anyone not on your team will be switched to **view-only** until added as a paid team member.

##### If I upgrade from the Growth Plan to the Business Plan in the middle of my billing cycle, will I be charged for both plans?

Upgrades are automatic, so the system will count the remaining days from the Growth plan and reduce it from the Business Plan price.

For example, if you paid $80 for Growth and you have 15 days remaining in the billing cycle, then on upgrading to Business (let's say priced at $150), you will eventually pay $(150-40) = $110.

> **Info:** FlutterFlow provides different pricing options depending on your region. To see the exact prices for your area, visit the [**Plans & Pricing**](https://docs.flutterflow.io/accounts-billing/plan-pricing) page.

---

---

## Before You Begin

### App Development {#app-development}

*Before you jump in and start using FlutterFlow, it's helpful to have an idea of how app development works more broadly.*

**Source:** https://docs.flutterflow.io/before-you-begin/app-architecture

Before you jump in and start using FlutterFlow, it's helpful to have an idea of how app development works more broadly.

Traditionally, developing an app required writing a lot of code. You can think of code as a set of instructions for the computer, or device, executing the code.

The codebase is usually divided up into two pieces: instructions for the frontend, and instructions for the backend.

#### Frontend vs Backend

Frontend development deals with creating the parts of an application that users interact with directly. This includes:

* Defining the visual pieces of your app, like text or buttons
* Figuring out how these pieces should be laid out on the screen
* Setting up logic for how your app should react to retrieved data and user interactions

Backend usually refers to more complex logic and data storage. This includes:

* Setting up a database that is capable of storing, sending and retrieving data
* Leveraging off-the-shelf services, like authentication providers or payment platforms
* Defining business logic, either by writing code or using a low-code tool

The interaction between frontend and backend often occurs through APIs (Application Programming Interfaces). In most cases, the backend exposes endpoints for the frontend to send requests to. The backend handles the request, and sends some data back in response - which the frontend can use to change its visual appearance.

#### Where does the code execute?

Backend code runs on a server, which could be located in a data center or hosted on a cloud platform like AWS, Google Cloud, or Azure. The server is responsible for handling requests, processing data, and sending responses back to the frontend.

Frontend code runs on the user's device. This could be a web browser for web applications or the operating system for mobile applications. The frontend code is responsible for displaying the user interface and handling user interactions.

#### Frontend architecture

When it comes to developing the frontend of your application, there are several key architectural patterns and best practices to consider. These include:

* **Component-Based Architecture:** Breaking down the UI into reusable components, each responsible for a specific part of the interface. This makes the code more modular and easier to maintain.
* **State Management:** Managing the state of the application, which includes the data displayed in the UI and the user's interactions.
* **Responsive Design:** Ensuring that your application looks and works well on different screen sizes and orientations. This involves using flexible layouts and scalable assets.
* **Performance Optimization:** Making sure your app runs smoothly by optimizing rendering, minimizing the number of network requests, and reducing the size of your assets.

By understanding these concepts and implementing best practices, you can create robust and user-friendly applications with FlutterFlow.

---

### Create an account {#create-an-account}

*Ensure you meet system requirements and grasp technical concepts for smooth building in FlutterFlow.*

**Source:** https://docs.flutterflow.io/before-you-begin/setup-flutterflow

Create your free account to get started with FlutterFlow. After you've set up your account, you'll be able to create as many projects as you like.

You can [**sign up**](https://app.flutterflow.io/create-account) via Apple, Google, or Github.

#### System Requirements

The FlutterFlow application can be accessed from your browser or installed as a desktop app.

##### General recommendations:

* Use a screen that is at least **1280 x 1024**

##### Browser recommendations:

* FlutterFlow works best on **Google Chrome**
* We recommend keeping your browser up-to-date, specifically within the latest two versions
* You should allow pop-up and redirects and ClipBoard from *app.flutterflow\.io*.

##### Desktop recommendations:

* **macOS**: While FlutterFlow should work on 10.13 or higher, we recommend using 13 or higher
* **Windows**: While FlutterFlow should work on 7 or higher, we recommend using 10 or higher

> **Info:** Some Windows users may experience a crash. To fix this, install the [**Microsoft Visual C++ 2015–2022 Redistributable (both x64 and x86)**](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) from the official Microsoft site.

For details on target platform system requirements, please see the [Flutter documentation](https://docs.flutter.dev/reference/supported-platforms).

##### Desktop vs Web:

We recommend using the desktop application for improved performance and access to features like [**local run**](https://docs.flutterflow.io/testing/local-run).

However, our desktop applications are currently in a preview phase, which may result in some instability.

---

---

## Best Practices

### Best Practices: Secure API Keys {#best-practices-secure-api-keys}

*Learn best practices for securing API keys in your FlutterFlow app, including key restrictions, geographical restrictions, IP address binding, and service-specific limitations.*

**Source:** https://docs.flutterflow.io/best-practices/secure-api-keys

Google Cloud API key restriction is essential for managing access and enhancing security when working with Google Cloud services. This overview explains how to effectively restrict API keys, allowing developers to control how and where their keys can be used. Developers can set geographical restrictions, bind keys to specific IP addresses, or limit usage to particular services. These measures ensure that API keys are secured, helping to protect projects and maintain optimal functionality.

To minimize potential damage from compromised API keys:

* **Add restrictions to your API key:** By setting restrictions, you can limit how an API key can be used, thus reducing the impact if it becomes compromised.

* **Delete unnecessary API keys:** Remove any API keys that are no longer required to reduce exposure to attacks.

* **Rotate your API keys periodically:** Regularly create new API keys, delete the old ones, and update your applications to use the new keys. This practice helps maintain security and limit the lifespan of any single key.

#### Add restrictions to your API key

API keys are unrestricted by default. Unrestricted keys are insecure because they can be used by anyone, from anywhere. You can add either [application restrictions](https://cloud.google.com/docs/authentication/api-keys?#adding-application-restrictions) or [API restrictions](https://cloud.google.com/docs/authentication/api-keys?#api_key_restrictions) to enhance security.

In the following example, we will use the **Map API keys** and restrict them to specific platforms using their unique identifiers.

At this stage, you should already have API keys created, but they are currently unrestricted. If they are not yet created, you can follow the integration process for any of the Google Cloud services we support in FlutterFlow, or for Maps, [you can go here.](https://docs.flutterflow.io/integrations/google-maps/generate-maps-keys)

All your created API keys should be available on the [Cloud Credentials Page](https://console.cloud.google.com/apis/credentials). (Ensure you are logged into the correct Google account and are in the right Google Cloud project.)

Follow the steps below to enable the iOS key exclusively for iOS apps with a unique package name:

[Restrict API Keys](https://demo.arcade.software/givOcppDSZHXzWJDloWj?embed\&show_copy_link=true)

Now your iOS API Key will only work when accessed from your app with the given unique identifier. You can also restrict the API keys by **HTTP referrers** or **IP addresses**. Here's a quick overview from the official docs:

![app-restriction.png](https://docs.flutterflow.io/assets/images/app-restriction-85dca210a3d64c0162faf32140c4ffa0.png)

Learn More

Learn more about **securing API keys for all platforms and restricting API usage** by visiting the official [**Google Cloud Docs**](https://cloud.google.com/docs/authentication/api-keys?#securing).

---

---

## Collaboration

### Branching {#branching}

*Learn how branching in FlutterFlow allows you to add new features without disrupting your current progress. Understand the workflow of creating and merging branches, resolving conflicts, and the difference between merging and rebasing, with practical examples and tips.*

**Source:** https://docs.flutterflow.io/collaboration/branching

Branching creates a separate copy of your work, so you can add new features without disrupting your current progress. It enables multiple developers or teams to work simultaneously on different features without interfering with each other.

Suppose you have an eCommerce app and you want to add a new feature, such as a product recommendation system. Instead of incorporating it directly into your existing `main` branch and potentially causing problems, you can create a branch to work on this new feature in isolation. Once it's complete, you can integrate it back into the `main` branch.

> **Info:** While all users can access the branching menu and create commits, only **Growth** plan and above support creating new branches.

> **Warning:** Creating a branch here doesn't create one on GitHub. Branches stay and are managed solely within FlutterFlow. You can also learn more about [**managing custom code on GitHub**](https://docs.flutterflow.io/exporting/push-to-github#manage-custom-code-on-github).

#### Branching Overview

Before you create and merge a branch, it is essential to understand the general workflow. Here's what it looks like:

![branching](https://docs.flutterflow.io/assets/images/branching-overview-bbc4d99782390c8234732aaed3f94c1e.avif)

First, create a new branch from the `main` branch. After making your changes in a new branch and finalizing the feature, merge this new branch back into the `main` branch. If there are any conflicts, you must resolve them first.

> **Note:** It’s important to understand what merging actually means. Merging does not perform a "union" of data between branches. Instead, Git merge reconciles differences (diffs) between the branches. When you merge, Git compares the changes made in the new branch with the main branch and applies these changes directly.

For instance, if a branch is created and all existing data is deleted before new content is added, Git interprets this as a replacement. When the branch is merged back into the main branch, those deletions will also be applied removing the original data. This behaviour can be surprising to those expecting Git to automatically preserve all content from both branches. Learn more about [**Merging**](https://docs.flutterflow.io/collaboration/branching#merging).

To avoid accidental data loss, ensure that your branch workflow involves incremental and intentional changes rather than deleting and replacing all existing content unless that's specifically your goal.

#### Creating a New Branch

To create a new branch from the current branch, simply go to the **Branching Options** button next to current branch in the **Branching menu.**

[Sharing a Project with a User](https://demo.arcade.software/5n61rPZR7WuWxs0lTFkE?embed\&show_copy_link=true)

> **Tip:** You can create a new branch from any existing branch, however it's most common to create new branches from `main`

#### Commits

A commit is essentially a saved snapshot of your project at a particular point in time. When you make changes to your project (such as adding new widgets, modifying actions, or configuring integrations), you can create a commit to save these changes. Each commit stores a record of what has been modified and serves as a version history for your branch, making it easy to see what has changed and roll back to previous versions if needed.

##### Create Commits

To create a commit, follow these steps:

Best Practices for Commits

* **Commit Frequently:** Save your work often to ensure that changes are tracked, and you have a detailed version history. You can use the keyboard shortcut (cmd + enter) for faster iteration!
* **Use Clear Messages:** Always provide meaningful commit messages that explain what was done.
* **Test Before Committing:** Ensure that the project works as expected before committing significant changes.

##### View Commit Changes

Once the commit is created, you can see the list of all commits under the **Branch History** section. Here, each commit is displayed with a timestamp, the user who made the changes, and a commit message. You can also search and filter through commits by specific users and date range.

To see the commit changes, simply click on the commit. You’ll then land on a **Commit View** page where you can:

* **Review Changed Files**: In the left panel, files that have been modified are marked with a gray dot, making it easy to spot which parts of your project have updates.
* **Compare Before and After**: The center pane provides a side-by-side diff of the YAML for each changed file. Lines highlighted in red indicate removed or altered content, while lines in green show newly added or updated content.
* **See Commit Statistics**: At the top of the page, you’ll see a quick summary of how many files were changed and the total lines added (+) or removed (-).

[Viewing Commits](https://demo.arcade.software/RwImFTtbmT0hkxj1RtuF?embed\&show_copy_link=true)

##### Commit Options

The options provided for each commit are as follows:

* **View Commit:** This option lets you view the details of a particular commit.
* **Restore Branch to Commit:** This option allows you to revert your branch to a previous commit. It creates a new commit that resets the branch to the state of the selected commit. This is particularly useful if a recent commit introduced issues, and you need to return to a stable point in the project's history.
* **Copy Commit ID:** Every commit is assigned a unique ID. This option allows you to copy the commit ID, which can be useful for referencing specific commits in collaboration with team members.

##### Commits vs. Snapshots and Versions

FlutterFlow offers multiple ways to save the state of your project at specific points in time.

* **Snapshots** are automatically created as you edit your project. Think of them as automatic backups that you can revert to whenever needed.
* **Versions and commits**, on the other hand, are manually created checkpoints. While both serve a similar purpose, commits offer more flexibility by allowing you to view the specific changes made in each commit. If you're using a plan that supports branching, it's recommended to use commits for better tracking and version control.

You can learn more about [snapshots and versions here](https://docs.flutterflow.io/collaboration/saving-versioning).

#### Merging

Merging allows you to push the changes you've made in one branch into another. For example, you may want to push your changes from a feature branch, or a branch where you are developing a new feature, back into the `main` branch once it's ready to be deployed to your users.

Say your feature branch has two commits: `Commit 1` and `Commit 3` (which are your changes), and `Commit 2` (made by a colleague in the main branch). The merge would look like the below image:

![after-merging](https://docs.flutterflow.io/assets/images/after-merging-bb3a6676d00f240174f0d6d2c7ec13c5.png)

You can also merge changes from the parent branch, into the current branch. For example, say you want to pull the latest commits on `main` into your feature branch. This merge would look like the below image:

![after-merging-2](https://docs.flutterflow.io/assets/images/after-merging-2-0e2dd391925885e88d24733e9c17265a.png)

During a merge, Git compares the changes made in both branches, if the changes don't overlap or conflict then the branches are automatically combined. If there are conflicts (for example, both branches modified the same widget property) you'll need to resolve these before the merge can be completed.

Few things to note here

* At the moment, FlutterFlow only supports merging into the parent branch, or the branch that the current branch was created from.
* Only the user who initiated the merge can access both the branches during an ongoing merge.
* Merges result in a merge [commit](https://docs.flutterflow.io/collaboration/branching#commits), which means you can undo a merge by restoring the branch to a prior commit
* If you leave the project during the merge and come back, the progress you have made on the merge will be preserved.

Merging in FlutterFlow uses Git under the hood to calculate differences between project files. Each project is backed by a repository of YAML files (except for custom code, which appears as Dart files). These YAML files map directly to various project properties, and Git calculates differences among these files to identify merge conflicts.

Future Plans

* **Hover-Based Documentation**: Display helpful tooltips for YAML fields (scheduled before production release).
* **Inline YAML Errors**: Show errors directly in the file for quicker fixes (scheduled before production release).
* **Simplified YAML**: Make YAML files and errors more user-friendly and understandable.
* **Enhanced Visual Diff Tools**: Provide more intuitive views for comparing changes.
* **User Experience Improvements**: Continuously refine merging workflows and UI elements.
* **Performance Optimizations**: Improve speed when initiating merges.

##### Initiating a Merge

To initiate the Merge, navigate to **Toolbar >** select **Branching > Branching options >** select **Merge**.

When performing a merge in FlutterFlow, you’ll see a screen with multiple panels and info sections. Here are the details of it.

![merging-window](https://docs.flutterflow.io/assets/images/merging-window-5801e73a0c51551eab1cbad7aed64101.avif)

**Top Panel**

* **Branch Information**: At the top of the merge interface, you’ll see exactly which branches are being merged. You have two options for merging directions: * **Parent → Child**: Pulls changes down from the parent into the child branch, often used to keep a feature branch in sync with the parent branch. ![parent-child](data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAEHkAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAgAAAAB2AAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQAMAAAAABNjb2xybmNseAACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAEIFtZGF0EgAKChghv/1YIEBA0IAy6CBMBALcyCQVHYobGOaKC0IqP6O5xtKbgYA2Wq9F41pDRlkCgPz01TnI5LGNsvy777nzBDcuimNihtJBxSG7Nik2hJJYbY+lx9mqt9kO9H2Hivo8OAw0/Pl1j3m5m7Bwt6rs8vEX/9PL4Rv6KTiT1I/iTPmJSShILXqVJiGoNZnDQDLRrMJZ+kiY4k+lX+5IqvDT5Yr0Ixd08598iGd+liyswiYCWJ70tOQM47cfkoieyKMNCBuGJT5X175e7Qwcan7Q9/evAA4Bpkq+Y8ZPAvbo4vI5FHqMNFxwlXfEGc051m1Kfuv8IOMlnkEpTxQSygJIicbuKZj7YefTPIKF5wyVzS3Y141lBKZI/aGK+lV7111OcOC/M2kHmsga+ujtekOJNLU3Gm8VLgf4liUnlX1Syawu/pQFe7fhIKrcrFGGl/gj41oaM9cA6DMNdcv/9Vlc9VmJGTU2oBqdEkEhU6mH5T8HWi8m82fM4jbNteudfVSJ4wfLyimmPcV64o571+y3XPWfvnWGRcifzvK9IPKaD4Q/XJNezi5o2KRuDwEohT26l6i89HLKhth3fTxOMfoSuKxyRVmaYgVuZCcO9/4x3YS2vnsnupP05wzI1wJduTJrhNR/bhRC6DUTSOb43h5SUWXbJv1ihtLRqNw22tnjNJXrTKYWzMWqT9b+nvUSW5Au3Iqywlhq4tczT5B/c+5FN/dyDoXX7WYp08UKBXBzJItF/dROcvQNdL/kQo35IKwdn/7t4u8NjzvUOWEflcKd29hjQs5d0iQo5tg88tTGYSHWuTH6nW1iV1D9Sqw+atVJ6LNhl66VNgaKET2CQpfjt3FOCnkolLO51gjXiF0zkyJveKm0OSTdmb/DztrLzC0Fv90ctk+UVmyQBNq74mYnIjTLpw7PoDsB/G8v27D8WSJCuoO64WdWli1AFO4MkZBuaxRrsc+Xa07s3s0xl4YFKzZcEKSnT3bRYzbbbLOIgof5N4wFee3J0WOZtvDfaiUrFOZV5T8HaEMrDxkKFkHspKbDH5rX3rc3UjzPiUJzpix/pfwLsV3cFGPfllYZsF6XSeTmwjILqZF9ohDQRSydWXRYfHURKHiJTuJmQ9EzRolBZJpzxMoOBs/eqwM8qkOmgkLV2xm8pnkQjJqxKu4V3pkX5A6CUfvUcSeD4taba/CRr6yb0gYF1iQxhNKyM5gWdJ+F+ZG+2H8zukFGmwlJG1+zctJD6iBNxYgYWBUKvKOK+4rREhmZHru2ia6GGWYqjdMjE18CmZTguy81mddnb3uC9ECIMUFLflV3NdfjJvogny2ya1neziLXiJ1jfE3Ffd7AzGGvKtTpbkK4lvpoR10o9FcODpfjJ41aU9wQ8pH6xV2ckWrFqjCIOtyRBCLokVLspZQNNE/3sScfeQWBL/8L7NqBDb0tUysq5JqbTGBeBRCiWiLI2OyOAKjv9l5aCoBd+7/6CB2U6vhkdpdlSGvJFNUnbKKih0E2ENqWgHb1V/Uk8LmEplT21yUxy7DntPFx4+0LDQZojJJWATfMNHJXPW5owCAzJD9Zf2giQ6s74QUFccaO1edbxhGDu1m7pP/+5tjkseaYxsmRPg6bvQS6Ekbbph3kpI7ac0feYJ6wd8FmiqqMQOzhd6/a+/URb/GMUhtju0bmN+eHOlbdWNN8VyOQnT9x7g7C0an2RY4Rwx39yey3oBCc97XIyGgIRDo20Y2yrU/UZHB8s03fHTJ1Xms1LWSo7nTDO2IewRG00d0kgqjXMLflkP3NbFyUPCtDL4VbSZXi06SQffDESjHqGRotiZgvffVqHZANWFBK/HcZ7w6VCnpjtEeNOFVkSpaWOo5p1n+kcHhyxlWT6CdNm+iq3iaozl3V7xiTtL8jJvnjd6SEyBMlUYst+65x7VRisrrZpiam7gLsA5V74uO+AOPFIRGOppD+eNzNekfPd8U5jOMEQkzlD5XRoLsP9bwvbg7JcjYLk8MFs+fItUbqMo08bpFgxWkbMHlbfkJDkFx9Sqd2GT+UHmALfASYwCN/mAxStt7vFYbajTAyFrrF64JuuPIFhuf0382Er6cujZkmYvbFJPtkh6zWy8s7/qbmxZs2ZDnKh4OSJtFVC3JMIj/Tl5UDePuD8riNRPgZ7hJCQ96Z19sAs8biun6GWILGWKhKUS3OF/ziDmociLGlbhiiGaTreFclN5oDI1sBtKDGTo5EAwhY/iT612/RoIrlzX3Uul7Bk0UfsX5wUpiwxuDBd1xWhO7GUKCWFTOMPXtYWxrE7AkukYn/NFc5HSr0XQuTGg+BKys+RVh7c2ZDwIeptsAf+RzfWyQhT88snZ7T3BzUwqmrx28WX1bGWS+aCWhwIdi8PsuB7ghgOXwuKBjo12RTkX+svzIO2iRaZ+fxIEghXVbiMr0JcRciFvCXapDHCzX9jIqwREugB3FzvZkO7UnhllVRz06YMXzKbRO0/t/1ZEaM2BINZPi5DSD5sbXtJPTf8ppWzeQ53ll2+x9ZAHshuEyG5Y4i/TNjFYdQ/b5Vf/////5yxL3+QOiQNVcaHANY4xEHUzLVvbanwzUg7orhWSAB2uevML4Jrja6SqrjxKSke+57Dj1b3yM2ZlXsjyQLpWU16UxJLkYTZ0NEqKvp8r7ruGVqcAAmkIs1ARRkwASpMx41uJsQ6S7VUM5Vj90C/y67CsOfvy2pT9ybp61bpD+qXWXOnEHIQ2NmPuwcj1O05+g3CZYK1KOnngbM8fjwpKLeYk119iUNjMBwQHOJjUnbjp9XTug4HjBST1aStJRLvCkywL6qcvpiwTRXZXoY8fmlTtzziXT6eYi8DG1bMGGITp4iWHyjx8DK15AH9Q5Oqj+C6/Altf9jzU4pqs1VjnvvHAMvkXqVX7OEmP6CGG75hK83JrEOcymbmzCLxye3c21s8yw20/GLGZZ06Wy46Qbye1LlYaxEDDTaiAijtAriQyABM3AZxp4PiF5CS81OnqmOV0VN47CU2ox5ru4iaEHNF6iuuFBcUshfgSHyYkKdMUhCePs1uhuY5I8VsjxUx68JXN1ZkElym4jdOM5mo/EPKKql/UC1/JjS12Xq0aYGlihkqFqBB9ZffWuQjAmmqPaMW4dYa6UK7fmb92ifFnH3FqokhzctRdTuFjcj/jVKHxt/xdjWf7GUGrWXGeJvgU/g1VP0JYuBjl9ZyidsHzJ0JgTn48ceeMSJlXkn9YgBPMI5t2TcjCpu7AdGdXbv+cqw7qxY5N5BeqNtmng7dMRmlOZ/11LGu8XfUblu1XeKlsxV4UP76NlmYqZN58zsu463NoeTag8Epi558jLUeUxNh3xj9MGeGO4L92YMB1sMFZ2kGYQuM/rLMnYrSXcoDxAOHhVbOG9tcESQ1LmV1P1L7S30JVZehbF6rr9cyX0qpBEctHfau/s4sOJvjRMGUfrR2JrG4jZaSf2ZhdS2SYukSmRILXmP+vAT9j0DuGd0MQVNYj+D5bbp3rHp6CdBe8rmmz4GS5GsQ5HsJvFedg2w9X/SZI9OhVvIlJWs1U8K2LuR+CzFWaWxXZZtAqpiryabU4LxjbXrtHL4enuycB3DVTttbBUyJ1KupKFSC3bKm9Ft3c77b/RMm8c8PUfNToPVlpypxVFRDW3h4UXs4iw3i189JNeO7ffn1//opvNbfRZ7RpMbaZiKg3w5HZg6jpYrqM9zp8+Aqlfc8Av6+y82gHzzcTKRybvlJAMr0Runhowjtv2XGXJHKr4BxT56MbZuvcaG/PNQeYgDcLn71zTqqhT6RLkYP7EinvjnFmf1F0dJ6CHOciijJ5vL8tVClU+l+BMtbhwFgAWyEhbUH9TO0TOXjethrMkuxCo0eUHB6mju6MDye8XF8SO9OpqJh6nDHtZAnRiYHKocjZQmvFuoeFuY7GA5hPtuGyvE0PAuAQr+jhFQUN87wbBSeQXK/lYVosLe2JQKszxkEvg631fvTd46/SmJ4VtoCUOVgVz7ueBWDHEryDUIDGZpZP+Ce3/3p0LcYhgIJ33R1CLSCW0rXEwcnNz+4kylHhV2q3REcqkxstg5gVSNtEZT1KHZfkyN2kGiiZ4v2mA/hMdZTED/w/2f9rPNPneK0+usTP2N5BsAMZ5io5ZfZV4Sl5KtOikJT6ATDh8SjV/dgqKl9zwGv1/Oh40a2edU4Dbk5mqMoFJnzljVKZ1q5tgclDlHB5emkanmUjVdZ0nel/XZNnzchTTqbACQ1tv0R4Y+t1CFleuL9IEyJtjLE4G8/ZSAg84pffwC9qIho9h4pyJdOpLly16vcsQxEtIltHYvs6TUkEuiXXkluN9VVHWsk2hJblDbvBpB7zTts8f90bjlsj7NNY0oqWBms/VGfmXxPW7PwDc+6zMMIqnI4HeuNjXg7fxoVrMbuT545MlTc8cJeuUBhmalw2710dCIijy7rGh6NXI/nTEgNCavM4g1p8fM2xLmmlkgqOAKr8MOVR0o38Ctb5Hv2u8sUcAHRyflrd/d8NZ8eCHz3gXOT3ybYFFO7oys7XuoPtEQtsLbiD02tgl2Gx+qBaQg9Al5v62daTwKnPyFjQWHVXWIyLZYYppaVHGGiOLedqnbez8cd0Gh8t9qp3zH2wqzKwtYTuTB2X6ylSbA+UOGwQFzeF31pU54My+4eHN+SO23iSequoTEVKG9nuZHR+wh9eAHbZUJczp/Bu8N4RWERfR5ZxT4D5HfKW0Xrs4CSJy0eKNYfPMTJ1ars0PqQgt4IZL4CxkB7su8/EgqCDa41wh5qbuPfoToZ1NrlYg86A/wZ40SB5FHzXVEW184cl8yV4eiCOj/NV0OGe1Bp3x0F9ja7+bn0O0ydW1L+wyVHfMnzp8PpSpSF9ir5eQmuTCqXXUHSky9IAEJVAyvA6w2lF1EEuWipUkInqztch/aqFTEG07KNh7e5ETUege6UQmWXHLsjfLfptz8DI+vxfnn/H8Mvr6SAJyNCyJB/Ti78c+mQFHDT9wHeLB5yHDgv4kynKvYKpP1JNtBEcc48iJSzjS8OzPASEBluQbmeYECgV3yS76DQVtO4aKGsY4g8vld2+uq8U9VflM+bZ2NJSzUfqaPYxBlU41kAYxKUcu9iax5V1SF43qbdLwn63nTjDa27Sd+vC5LEHEUSV47hdcoWoqcMVasJb+JJp0BrEYcpfnN2jFEy0BRRFZma7Feg4Ee4CGp+t8R7coHs9Ockx3MQpXej4JfJkb7xyCnO0tnc2n00DyARwrUWv9ol2LR6U23bEholMCKkrk7YOV4pIqOw9FhithBn0tdC+ccRh/+7Z7hhnImM1BaPArfpmFNGa9RZFqffJiKRQq3EKPvi1yKe/hZIQtb2UyByWpdzRIMpYIRvcMti9R93937aFFhXW/xl2abiw+g4dYBt03TX+VoOwjDXbbH35BUgXHWx1lsPfg3n6D/tL0IPGtLs/Dzriufg3BW8w1x1n4upYPuMYoZl+l7qEnUZ5UV3VXx5Y0eojl6Xj/BDGefCLUpolzyp+HaDzdOFuR+h12EbLG9zkF4Xl7Oyz/T2TI0hk4ALPYRHq6Z4lwpw1fR7dnaBfdntdK7rz1uzc5WO75k7UEj7aMrrhtkwiA=)
  * **Child → Parent**: Pushes features (or other changes) from the child branch back up to the parent, commonly done once a feature is ready to go into the parent branch. ![child-parent](data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAADuUAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAgYAAAB2AAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQAMAAAAABNjb2xybmNseAACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAADu1tZGF0EgAKChgloF6sECAgaEAy1B1MCALcadegjvSXVVMhTnMfpIeMu7tj9vlTGPplB7nhRDgszQovRNQr2g80Cg7A4WrfgQ2ncpyzvI2bUGLK5gVJtErBYSKHPfY4n/ZSljcE+dWCXX5KtsSjibBuFHiYM6XTk9NWLKMP9xF0dR96wvjLmCRuZrBtigURHjPp1q7qZ0Hrzo8ThD9i7jExozEKvRKlBNDKVU0OknMKrzDNDQ2HrIocwIVKK2xm3WciEPw3zGfLnsYKyV+vm0CGETpPWONJ0k25VBGXzwtTCNs5ppapxFwKFmQguD1hlM5+AlbIND6r1jlAB2Ty7giTPxuLpwKR0peGus4pQgpWfhQyCSv60CfuFNNZWAMQw5PE9aO6lPbFAymGkeoCmOKsotpo5glfaPqu0Y7gnl7UM1ewFki8aXWzQ/buNR9uREYZTz7YLPQeUK7BkQI1atf7BbMZvb0Il98v5qCjiq1SkMLLDlorlhl4j8YnbGUoBml99iGt0WwFnsZfNtejtwjWBmmVA7xIh7NCV/5NPONhCHsHUdt5znGb0qrSaOyhlIWIn5xHKa4e6bKNXwvrEHpAEyJUVMgOR9S/9CWDsZ22chF6Q3fmifBK6ZJf/zp/UGROwJcTb5CkIxpF9iSOdfzfYYVbwZ6c3yXMVVnPMDxZLstEP+k6sSpkOH4qElzAKxQ8uO95Noakoz1RlQGw8+uqo3uJV56FzHDDo9k+gBbZdHYsA7DI1fPV6bTWUt84fsKENVN0HAWn71FJxi5dRVPvNnTcrAKcFjyePFSh6EszlO7pqG/FyMqTrRzvzomJEP5e4ra4MRKNCJ8jZZJWt/kFBTxCjIbO02j6dBDvAWbl8ByNuAYWt5/GSrqU99kt1U60/wrSC+VGvdnDVB80W1dkgRjh38Az2l8B/It+TzWXPyL04xSCValn0qneUrD8TggPjZxy0KD3WCVbtgBD8GUNxxEN0Fz6QQ/o/6ug2oG1Tw7rC5vMfJH3ivhJHy676Xhanr60VtgMCk8ZLTSOsbhN+YJCQk7FnylciY+8Sw5EOuXb0jiYOpCVjnd3kO0GM98SvZXuG57DHlHJMnyZlG8q86IsjawZFsa9Dgs7Na9NQqRZ4DjEnl0igS8YykhtDdjFQdpRp1TPTpT2PEzpV2ZqqCfFkwA82TPPpmhdndv4o5AqDLOc/5qtIybvMGKLZjCZjSM/fCXJXcv9K3p21WKcce+seDH5+JLDoYzbR+F7fVtbxQ8nOan2XMgk5ZOP/40IHChEf4UqoFGQR/KZul/YpKFDJ0sI6q7EIKKmh6z9Gz8FhreB4IwVOtGJnFt9ykpez3z9j/bV01Qsp+kSsn+uqzSvZJnj8jZlgFt82J2YAyr1QGMGXoaAAerf7SWhBQYDYiT+SlV1fdq4wT8CQzsMo45jE8Sbm+xr6B10F+AeJuh78okUHr/aopcR45G+QIMYb7saZqbzCq5zh1beDFhPzCL8eniVpspCYsi3NnSCF0bXibmn9Pt0BIGSkEvg9SLDlrpMh0Ogblpg1gS9rn98AFI/oyhbKf2o6oh45tXM3QtGjY6A0CVm8SL6nveMp5KUv+n3rq7NbDPe0dl4aTRNQYRlyqDCD82n5bDOdVvVgh7p961Y1w703fMIBWvSvqRQ+7jx/hVIFDJx8iEjPrij8gO3MtcQvIoy6UxTlWIhb8/DwisgIcQGeclGm+DKgK4leqymsi7tKh1ghKe679xjIBafjxyqoYqalg9C0H6QolslyAjYBYZ95onE9hgJsuC9GH1/kUSGxG8US3HGN3uXDkZB4JDT2iLhS8Ay4+W/grvzPIqUpTZwbWjoT/QS9x9fCtUGihV/lfm/t43GaF/qSiP8sARn//ngpdL+5vair0GFY4OTPwZqmj6UlVz+7aoidaPAmOF3jLJbO53xHTd267Wz0/uODKnf3bsupnmSGc4RwA8k15jy99wxwGJacqTuz77F12ELjm68XTHqzweT+/Y3kpp6BHEN5i1S3rzJ3PaMycfcFIB7TTfDDe2zOrldpLbG4Gh22xrXpc32LNFtMEwUkqLd2uOx2ODr3nsBqo/e/uh3o7nBcN6Zzh2zt8KJQd3mtfipsvM1HqJZmQBUhpWBou31Iqw9+BD2T2amqB2Eu9pbQ9tUNPyRTp441FKJow6tu7/ni0MADmSd9MAZTvGeZ7S8cI8Sa9e5agWUO3Qd/AYaJIqRQUbT1a/ZOWwW7o/bF5iIFNWIWvD+djAs59se89h7Lth6oH2oFL8z9KK6KF9LF14GxHE7anNu5pURyeMFBBKtPrYECbOQMKm+YjXN88LWjlZGtr0IzonBkYSiw9pBxUvZeRov1EhrbPgftwQLi5JfqCUQ1XEBDc8+TW2UJ41zygaGppqJK32CDAt48EBsywuRR9wUDa8GFN+4d6BDeMhaRLBJKvJg+wsbzbNooUdUIj+0RjxcMEtjrza+JJ62IY5YxRyhtnSg6iJcJDH5RNDlLSZpNzSjG3T1a8ItpSycfDH5pFWT5hhgOI8DOAkcO0prDdhwjaA1CpPZWT9jVFrKhPIlkXLuWcyXHLh9PHo9tmeKBRFu8rzGTj9FtmxwoZwE+U6Fte//b3LqPqnkbJLVSke7hQN9RfI+/RII7QGM9u0HFR8Hq5GxASkM05jzJL5UJzshpTVINjcAeOGl1G37vxmcQ6J+L8TVGG3btLjimqw2yHN7U7qSPeP1zNDMJit9JyrZx/qWcHYK0ePqgJ9KrHbv8khwo7J9ZmgQv7oAfEiSu4EQz3YVkrN1o7D3P2yy4j/tGycQsFQCCV5gIf9xLVc0ziDkgvKRMqfNRe0pgL3I8utB9qZX0QvsaM/oN71TC522/S7TVPrucL1o8aczn7wQsc7SKj6vZwtY18pAG3XEhmn1daMTvVTh+0Xgxpg7xm+OJ4NLB3fiVa41gU3Z8IwtYugsySJxBcI1LTKkwFXnwz+jQrePxw3A9B+Z1x6ofDg4Keu1l6d7FmUL7GaFb5tTx+XlqA7ghYiIty2NR/poZBWvPzGkTDLMex5bALk7xpCo2GfuKf+3Bf6wViPDSYEI5xYxJ+QyEoos8OJSoefhmsripW5On/4J0CwVovALwHTaaYjAH5V9BboMltr+UJHD0HOPGfxHMNZLJIal3KQoIHT4/kWDUSe3dOdPvjmOShSMbExtwoiv94mInz6N05GRTPhCAGUopsIB7WAknJXHneVGy4KD+HhiSIdep2r/KevHvGxtlaY/EsQaxm4Y2aW+hjBQlbIf6wxrgKywZjU0IyX2K0LG8ySCkDZv/J91LDblIMgN29Xi7NGP6v6Riw+arpI6j2fwjdYYSPEq08fLNNhaRTLZxBQG8ABlHWmm7ELepsbWbHBk5D1+vdn+fN4GWgVGCvZM8r/Mekgk5IfEhRISLdl8U0No+HDu6HTQ8I7RlhJPuyeovYSTWeNk2cjgu1NfutdPNMxgyGcK7itWS10HnM6yYqtdEQMz+2Y+uCoNo6063NeL26jBxD5OPl1b6QMHD/DqnIHJ2EexFfAnjuX2zejv9iH4PJmBwNhDkiPTEqtQfCHwlSLF3x1AdXzgZsNELbOtKU/+GEtPbCXygvwaPj3Z9quxOsOQRO6XcTTpYuTRUzydAzZL/Ipa3mT0TzSZY3s6ux2eAiD6jkMdw2SSpd+nGLiyL8ERvEOoZV/8E954Rrit8LR5HNoNs+BqQ2KOt6QZfbQnIDwGOM6v7QZI+502FoV94Dfq0U/HYzYHIuCkO/b330xPKcszm0TfLVWeavkXeDPhsZ+GuMRGdhP2Gj+CPfi9Jnjb8WB3B9J0ImCjauA75qQlThS+z0J+WU9yLI2SWXTEIRoypDr7iT0Kp4RzLl3SLMWgekEinWk5/hW1lB/6Sv/D2mEAOJyLC1XCLGGN4nbkuqBXBEWlOs1ETqV6ETl4vyIt7e+7q8EwAX2kZ6FwqvvssJiJNEbAhXmGEbTgQYlqJpLIC1TMWgskN8HnQNHlm6gxlEK8gbADkWmGQ6e9HWDXz684y0usBslUkObarNoeVag6zDGMs/yGn4e8B7EKPSPLTkXz7mKFWjN25oa83T0i2Ocv+vb1IHDvdv4+t+CGCRbuyjspn+Y+uhplprPUexF/mwO65eu+obk8m5HnBzoz5xqfOJZPlkc+IA/c+2TQ6dsH62dKqy9i6J9xPL9hcTSdfAkaYhr3QT0FIblh77YTsjxXSl9+ucQR7elnd+W2Zx0fPQQdHMd8L7S0TGoNmLt4BytoCGgRs6gU6qPV6wYTe5QShsKW27iQmh1N+BdECj30M0d6Svl4eacl3kOnaknVZQqs/977nCVqSuvRW0NitrzdN1u3m1oqH/tntwmmyXtgacRaw44BfyJ42wAF2bg3lVbRVtfPcrqPOjBybZe+yxHUXQ4tgNM3hIw661AOYcg97H5YVUtUy0tZoUE+ZD6SgX80cRCXjHDeWNo4JJdHMLoSpJ/TFgCko4AVviykXwEygmTzH7fVFk5AqBF4VKNdNCBTtnK7Z78rA0qDB6vxuSXRBXSckf2/DSsfv/Qh6K8AK7jEhi/rsQSIlemEtxRmleEB6T1XcPWhZBxHDNwGHML219/ecjFLmDWBNPyJpTCzQGVYooFfIa02QJzYRlnS7Hy/WXE2btQLPnbh/p7w6yTWb3wMCpwqK5rzbzqzCK9P/OPldHuMq4kINklxwIc3N+05VQr8rfiiOBueOP0Gyt+CsmWwEc5RnmXO/RHonKmBmUy6KJeyUCbKMqcZ3sW4eY2m8yneeJr6PSFffff5OEqwhj88ir4mmW9afLr9fDaxxNynU3e2lxLwRJUBFSd4XMb+YpZAnhQt091jBMj7nLJ3k3/hMn+Ia8djkBSUxNCjkSZwz9SV+7Zrsdxsx58K1Z8ZWHbzgpnQYNrzYeSEw2L0xZvTpPPRGg1qVoAFFttRImNBx6H2xxdy2x3zjUholvHRqFKV3bCOCBIsZQkjkgwpPQJjfZmh/xIA3ZCSBxIF51D77vqvoKvizViKw0QcgyLiHk/WtHkiV0/To2dKwkgIw09OBNgiQ6lqS5YesAzhAgzA)

* **YAML Validation Errors**: These occur when the resulting data is not in a “FlutterFlow-friendly” format—whether that’s due to manual edits or merges that generate incompatible YAML. For example, imagine you have two pages in your project, and each branch independently deletes a different one. After merging, there are zero pages left. Even though no lines of code are edited or directly have a conflict, this results in a YAML Validation Error. Clicking on these errors should redirect you to the specific file. Invalid lines will be underlined in red within the file, and, you cannot complete the merge while YAML errors exist. ![yaml-validation-error](https://docs.flutterflow.io/assets/images/yaml-validation-error-191b32eac7c334bdb481a34ece669a4d.avif)

* **Project Errors**: Project errors occur when the result of a merge creates a problem in your project. For example, this might happen if the merge results in two data types having the same name. These errors need to be resolved to ensure your project works as expected. You have several options to deal with project errors: * **Fix Errors During the Merge**: This approach ensures that the merged project is error-free right from the start. Here’s how you can do it: * **Edit the YAML files:** Update the project YAML files (in the Right Lower Panel) to fix issues, such as renaming a data type that causes a conflict.

    * **Edit the Project Directly while Merging:** While still in the merge process, open the project, make the necessary changes (like renaming the conflicting data type), and then continue.

  * **Fix Errors After the Merge**: If you prefer, you can complete the merge first and address the errors later. For example, finish the merge process as it is. After merging, go back to the project and resolve any issues.

* **Cancel**: Abandons the merge process and discards any conflict resolutions you’ve already applied during this merge session.

* **Merge**: Finalizes the merge once all merge conflicts and YAML validation errors are cleared. Project errors can remain if you choose to resolve them later.

* **Bulk Accept Changes**: Accessible via the **arrow** next to **Merge** button. This option lets you accept all changes from one branch at once—handy if you already know which branch’s changes take precedence. ![bulk-accept](https://docs.flutterflow.io/assets/images/bulk-accept-dd67d3857d7e5b5ff873c4e53f05cddb.avif)

**Left Panel**

The left-hand side panel displays all the project files in YAML format. YAML (Yet Another Markup Language) files use a simple, human-readable format to define configuration data. They are particularly useful during a merge because they allow you to directly review, understand, and resolve any changes or conflicts in your project’s file.

* **Filter Files:** You can use filters to narrow down the list of YAML files based on specific criteria:

  * **All Files (Unchanged Files)**: Shows every YAML file in the project that has no changes.

  * **Files with Changes**: Displays only files where a change has been made on either branch.

  * **Files with Conflicts**: Shows only files that have merge conflicts, where the changes in one branch directly contradict the changes in the other.

    info

    * A **change** refers to any update, addition, or deletion made in one of the branches. For example, modifying a field name or changing the properties of a widget. ![change](https://docs.flutterflow.io/assets/images/change-7047276948eae556fafbf757de879206.avif)
    * A **conflict** occurs when the same part of a file has been changed in both branches, making it unclear which version to keep. For instance, if one branch changes the color of the Container to blue and the other changes it to red, this creates a conflict. ![conflict](https://docs.flutterflow.io/assets/images/conflict-e8856491422d4b03fa8dc2bffdf9efda.avif)

* **Search File:** If you’re looking for a particular file, you can use the search bar to locate it quickly. This is especially useful in larger projects with many files.

Clicking on a file in the panel opens it in the editor, allowing you to view, edit, and resolve issues directly.

**Right Upper Panel**

The Upper Right Panel offers a quick, side-by-side comparison of file changes from both branches, along with easy one-click accept buttons and previews. This panel makes it simple to decide which changes to keep or discard.

> **Info:** The edits are highlighted using green and red (Git) color coding:

* **Green** indicates lines or values **added** (or unique) in one branch.
* **Red** indicates lines or values **removed** (or replaced) by that branch.

- **Accept Change Button**: Quickly accept changes from one branch if you know it has the correct edits.
- **Eye (Preview) Icon**: Open or view the file in the FlutterFlow builder to see how the changes look. For example, you can preview a theme color change visually rather than just reading its name in the file.

**Right Lower Panel**

The **Lower Panel** displays the final merged files after Git applies its merging logic. It gives you a chance to manually inspect and edit the outcome—whether or not a conflict occurs.

Git attempts to combine changes from both branches automatically. If Git can’t reconcile certain lines, it flags a **merge conflict** in the file. Conflicts appear with special markers like `<<<<<<<`, `=======`, and `>>>>>>>`.

* `<<<<<<<`: Marks the beginning of other branch’s changes
* `=======`: Separates your current branch’s changes from the other branch’s changes.
* `>>>>>>>`: Marks the end of the conflict, indicating your current branch’s changes.

> **Tip:** You might decide to keep certain lines from `<<<<<<<` (from the other branch) or `>>>>>>>` (from your branch) or combine them manually.

You can modify files or edit the project directly from the lower panel at any time—even if there’s no conflict.

After editing, click **Save Changes** to confirm your changes. A red reset button appears if you want to undo your changes and restore the file to its initial state before you began editing.

For more information, check out the video below.

##### Resolve Merge Conflicts

A merge conflict occurs when multiple team members make changes to the same part of the project.

For example, imagine two developers, Alice and Bob, are working on the same FlutterFlow project and both decide to update the same button widget.

| **Developer** | **Branch Name** | **Changes**                                |
| ------------- | --------------- | ------------------------------------------ |
| Alice         | `feature-alice` | - Changes the button text to "Submit Form" |
|               |                 | - Changes the button color to blue         |
| Bob           | `feature-bob`   | - Changes the button text to "Send"        |
|               |                 | - Changes the button color to green        |

When Alice's changes are merged into the main project first, her updates will be integrated without any issues. However, when Bob tries to merge his changes afterward, a merge conflict will occur because the changes to the button text and color have already been modified by Alice.

When you initiate a merge using Git, the system attempts to automatically reconcile your project files. Any conflicts that cannot be automatically resolved are flagged for your attention.

You can review each file with merge conflicts and choose to:

* Accept all changes from one branch. ![accept-all-from-one-branch](https://docs.flutterflow.io/assets/images/accept-all-from-one-branch-dc23fea9853ea19f885cea8a473716eb.avif)

* Pick specific changes from any branch. ![accept-specific-change-from-file](https://docs.flutterflow.io/assets/images/accept-specific-change-from-file-3123c05847bd438e8ce69ad336f7bc5c.avif)

* Manually edit the YAML files. **Note that** it’s essential to correct any YAML validation errors that arise from manual edits. Finally, complete the merge by clicking **Merge**.

> **Tip:** * If you merged a child branch into its parent and are confident everything looks correct, you may delete the child branch.
* If you find any issues after the merge, you can revert the branch to an earlier commit. However, be aware that any changes made after that commit will be lost.

#### Branch-level Permissions

In your project, you have the ability to assign specific roles such as **Editors** and **Mergers** to project members for each branch.

To configure these permissions, navigate to **Settings & Integrations > Project Setup > Collaboration > Branch-Level Access**.

![branch-permission](https://docs.flutterflow.io/assets/images/branch-permission-9bf4148afe3cc265ffdb3ee474c17766.png)

* **Editors** assigned to a branch have the authority to make direct modifications to the project while working within that branch.
* **Mergers** on the other hand, are only allowed to merge other branches into that branch. This is especially useful for protected branches where you don't want any users to make direct modifications. Instead, users should only merge other branches into that branch.

#### Closing Branch

Closing a branch is a common practice after the branch has served its purpose, typically once its changes have been merged into another branch (like the `main` or `development` branch). By regularly closing inactive or merged branches, you help maintain a clean, efficient, and well-organized project.

When to Close a Branch

* **After a Merge:** Once the branch’s changes have been merged into the `main` branch (or another target branch), it’s safe to close the branch. This often happens after a feature is complete or a bug is fixed.
* **Unused Branch:** If a branch is no longer needed (e.g., a feature was abandoned or changes were made in another branch), it’s a good idea to close it.

Here’s how you can close a branch:

Best Practices

* **Review before deletion:** Before closing a branch, ensure that all necessary changes have been merged or no longer need to be kept.
* **Coordinate with your team:** If you’re working in a team, ensure that no one is actively using the branch before you close it, to avoid disrupting ongoing work.

Once a branch is closed, it will no longer appear in the list of active branches. However, you can restore a closed branch within **30 days** of its closure.

##### Restore Branch

To restore a branch, open the **Branch Filter** menu and enable **Show Closed Branches**. Search for or select the branch you want to restore, and it will open in a new browser tab. Then, within the closed branch, open the **Branching Options** menu and select **Restore Branch** to reactivate it.

#### FAQs

How YAML files are helpful during a merge?

YAML files play a key role in managing and resolving conflicts during the merge process because:

* YAML files hold important configuration data, such as settings, resource definitions, and project properties. During a merge, changes in these files reflect modifications to the structure or behavior of the project.
* The simple and hierarchical nature of YAML makes it easy to spot changes or conflicts, even in complex files.
* YAML files allow you to manually edit and resolve conflicts during the merge process.
* Since YAML files are text-based, they are version-controlled effectively, enabling multiple team members to make changes and merge their work.

Why didn’t all my changes appear after merging two branches?

Merging in Git is not like copying everything from one branch into another. It’s more like combining changes from two versions of a document based on a common starting point.

Let’s say you and your friend both made changes to the same project:

* You both started with the same original version (this is called the common ancestor).
* You made your changes in `Branch A`.
* Your friend made changes in `Branch B`.

When you merge `Branch B` into `Branch A`, Git compares:

* What changed in `Branch A` since the common starting point.
* What changed in `Branch B` since the common starting point.

If both of you changed different parts, Git can merge them easily. But if you both changed the same part in different ways, Git won’t know which one to keep, that's called a conflict, and you'll need to resolve it manually.

![git-merging-behavior](https://docs.flutterflow.io/assets/images/git-merging-behavior-086d608f27fae6843bcd054db6a244b0.avif)

Here are a few other things to know:

* **No conflicts ≠ no changes**: “No conflicts” doesn’t mean “no changes” and it definitely doesn’t mean the project is error-free.
* **Project errors are not bugs**: Project errors let you know that you are making mistakes when merging data. Even if changes are successfully merged, project errors indicate areas you should double-check to ensure everything merged as expected.
* If a change was previously accepted or rejected during a merge, it won’t appear as a diff the next time you merge the same branches. That’s expected behavior.

For example, you merge `Branch B` into `Branch A`, and `change C` (which exists in `Branch B`) gets copied over to `Branch A`. Later, you decide to undo `change C` directly on `Branch A`. Now, if you merge `Branch B` into `Branch A` again, Git will not re-flag `change C` as a difference. This is because Git considers it already merged and no longer a diff.

**Best Practice:** Keep your branch histories short and simple. After each merge, delete the merged branch to avoid unnecessary complexity. For example, if you merge `Branch B` into `Branch A`, and later want to undo or revise those changes, don’t go back and modify `Branch B`. Instead, create a new branch (e.g., `Branch C`) from `Branch A` to make your updates.

This approach prevents intertwining branch histories, avoids confusing merge behavior, and ensures clean, trackable diffs. Keeping branches focused and temporary makes merging more predictable and manageable.

---

### Saving and Versioning {#saving-and-versioning}

*Learn about versioning in your FlutterFlow.*

**Source:** https://docs.flutterflow.io/collaboration/saving-versioning

In this section, we discuss the important concepts of saving and versioning in your project. Understanding how to use versions, snapshots and commits can be crucial in preventing loss of work and maintaining progress.

#### Versions

Project Versions are now deprecated

You can no longer create new versions in FlutterFlow. However, any previously created versions will remain accessible. Moving forward, we recommend using [**Commits**](https://docs.flutterflow.io/collaboration/saving-versioning#commits), which provides a more robust way to track changes and manage your project history.

##### Restoring a version

Restoring the previous version will preserve the current version, then load the changes from the version you're restoring. Before restoration, you may want to view the changes in the previous version. To do this, select the **Peek** option, which opens the previous version in a new tab.

![restore-version](https://docs.flutterflow.io/assets/images/restore-version-801604fdeba89500669a9e66822f191e.avif)

#### Commits

Commits are similar to versions in that you can save the state of your project at a point in time. Commits are saved to a specific branch's history. With commits you can view the specific changes made in that commit and restore a branch to the state of a specific commit. For more details see this page on [Branching and Commits](https://docs.flutterflow.io/collaboration/branching#commits).

#### Snapshots

Snapshots are automatic saves of your project's state as you build it. They allow you to **Peek** or **Revert** to a previous state of the project if needed.

![snapshots](https://docs.flutterflow.io/assets/images/snapshots-4bb79f7b55a02f7d11d2dfe7001a8da2.avif)

> **Info:** * Users on the **Free** plan can access automated snapshot backups from **up to 1 hour prior**.
* The **Basic** plan allows access to backups from **up to 1 day prior**.
* The **Growth** plan provides access to backups from **up to 3 days prior**.
* The **Business** plan extends this to **up to 7 days prior**.
* For **Enterprise** users, snapshot retention is **customized**.

---

---

## Designer / App Builder

### Collaboration {#collaboration}

*Work on the same design together — in real time, with comments and shared access.*

**Source:** https://docs.flutterflow.io/designer/collaboration

Collaboration lets multiple people work on the same design at once. Edits, cursors, and comments all stay in sync, so a team can explore and refine a design together without passing files back and forth.

#### Sharing & Access

Designs are shared by email. You invite someone by entering their email address, and they get access to that specific design — there are no public links or anonymous access.

Each collaborator is given one of two roles:

* **View** — open the design and follow along, without making changes.
* **Edit** — make changes to the design alongside everyone else.

The owner manages who has access and can add, change a role, or remove collaborators at any time. Access is granted per design, so sharing one design doesn't expose anything else in your workspace.

##### Add a Collaborator

1. Open the design you want to share, then open the **Collaboration** dialog from the share control. The owner is shown at the top, with everyone the design is shared with listed under **Shared with**.
2. In the email field (`name@company.com`), type the address of the person you want to add.
3. Use the role dropdown next to the field to set their access — **View** or **Edit**. New collaborators default to **Edit**.
4. Select **Add** (or press Enter). They appear in the **Shared with** list, and live collaboration turns on for the design.

##### Change a Collaborator's Role

In the **Shared with** list, open the role dropdown on that person's row and switch between **View** and **Edit**. The change applies immediately.

##### Remove a Collaborator

In the **Shared with** list, select the remove icon on that person's row. They lose access right away. Removing the last collaborator turns off live collaboration for the design.

#### Real-Time Editing

Everyone with Edit access works on the same canvas at the same time. Changes appear instantly for all collaborators, like adding a frame, restyling an element, or updating the theme is reflected for everyone as it happens, with no manual saving or refreshing.

Because changes are merged automatically as they're made, multiple people can edit at the same time without overwriting each other's work or running into "who saved last" conflicts.

Active collaborators are shown on the canvas as you work, so you always know who else is in the design and what they're focused on.

#### Comments

Comments let you leave feedback directly on a design — pinned to a frame, an element, or the canvas itself — so discussion stays anchored to what it's about. Each comment opens a thread for replies, and the Designer Agent can act on a comment to make the change for you.

##### Add a Comment

1. Right-click on the canvas, a frame, or an element, and choose **Comment**. A **New comment** popover opens, anchored where you clicked.
2. The popover shows the target above the input — **On Canvas**, **On Frame …**, or the element name — so you know what the comment is pinned to.
3. Type in the **Add a comment** field (up to 4,000 characters).
4. Select **Send** (or press Enter). A canvas comment drops a pin with your avatar; a frame or element comment adds a count bubble to the frame.

##### View and Reply in a Thread

1. Select a canvas **pin**, or a frame's **comment bubble** (tooltip: *View comments*). A bubble with multiple threads opens a list first — pick the one you want.
2. The thread shows the original comment and all replies, oldest to newest. Long threads load more replies as you scroll.
3. Type in the **Write a reply** field at the bottom and press Enter or select **Send**.

##### Edit or Delete Your Own Comment

These actions appear only on comments you authored.

1. Hover the comment you wrote and select the **⋯** menu (tooltip: *Comment actions*).
2. Choose **Edit**, change the text in place, and send. The comment is marked **Edited**.
3. Choose **Delete** to remove the comment.

##### Ask the Designer Agent

1. Hover a comment or open its thread, then select **Ask agent to fix** (the sparkles action). It's available from a comment row, the thread header, and individual messages.
2. The agent reads the full thread, original comment and replies and applies the requested change to the target frame or element. It's unavailable while the editor is already busy.
3. When it finishes, the agent posts a reply in the thread confirming the change.

> **Info:** For comments on the canvas, this action instead creates a new frame from the comment.

---

### Components {#components}

*Learn how to create reusable UI components, add variants and toggles, and manage dynamic behavior using parameters and expressions in FlutterFlow Designer.*

**Source:** https://docs.flutterflow.io/designer/components

A **component** is a reusable UI building block that you can use across your app design. Instead of creating the same UI again and again, you build it once as a component and reuse it wherever needed. This helps keep your app design consistent and easier to maintain.

When you update a component, all places where it is used automatically get updated.

Imagine you are having a settings screen with multiple rows, such as:

* Notification toggle
* Privacy option
* Account settings

Each row has a similar layout with an icon, text, and an action such as switch or arrow. Instead of having each row separately, you can create one **Settings Item component** and reuse it multiple times with different content.

##### Creating Component

To create a new component, start by selecting an existing UI block on the canvas. Then click **Create Component** from the right-side panel, give your component a name, and choose the parameters you want to include (such as text, image, or icon). Once you confirm, the component is created and opens in Component Studio.

Inside Component Studio, you can bind these parameters to different UI elements. Select an element, then connect its properties (like text or image) to a parameter from the right panel. You can also add new parameters if needed. This allows each instance of the component to display different content while keeping the same structure and design.

> **Tip:** Once the component is created, you can also use AI to quickly update your component by describing the changes instead of manually editing everything.

##### Create Variants

A **variant** is a different version of the same component that allows you to change its appearance without creating a new component. Variants help you manage multiple styles, states, or layouts in one place to make your components more flexible and reusable. For example, a button component can have variants like **Filled** and **Outlined**.

To create a variant, first open your component and click **Add variant**. This creates a new option for the current component, such as an alternate style or layout. Once the new variant appears, select it and customize its properties to make it visually different from the default version, such as changing borders, spacing, colors, or other styling details.

If you want to introduce a completely new category of variation, click **+ Add variant** again to create a new dimension for the component.

##### Add Toggle

A **toggle** lets you switch between two states of a component, such as on/off or active/inactive, within the same component. For example, a settings item can have a toggle to show **enabled** or **disabled** states, or a card can toggle between **selected** and **unselected** styles.

To add a toggle, open your component and click **Add toggle** from the variants panel. This creates a new toggle dimension for your component. Once added, you’ll see two states (i.e., true/false). Select each state and customize the component to define how it should look in each case.

###### The `Has` Expression

The `Has` expression lets you automatically control a Boolean property based on whether a component parameter has been provided. This is useful when you want part of a component to appear only when data exists, without manually setting a separate true/false value each time.

For example:

* Show an image only when `image_url` is set
* Show a subtitle only when `subtitle` is set
* Show a time row only when `time` is set

A `Has` expression checks whether a parameter contains a value. If it does, the result is `true`. If it does not, the result is `false`.

Suppose you have a flight booking card component with an optional image on the right side. Instead of adding both `image_url` and a separate `show_image` flag, you can just use `image_url` and bind the **Visible** property to `has(image_url)`. If an image is provided, the card displays the image, and if not, it just appears as a text-only layout.

![control-using-has-expression](https://docs.flutterflow.io/assets/images/control-using-has-expression-33d71531048737ae78b8b2cda1971a4c.avif)

---

### Export {#export}

*Export your FlutterFlow Designer designs as PNGs, agent-ready prompts, or directly into a FlutterFlow project.*

**Source:** https://docs.flutterflow.io/designer/export

Once your screens are finalized, you can export your design for implementation. FlutterFlow Designer provides flexible export options depending on whether you want static assets, reusable prompts, or direct integration into FlutterFlow.

#### Export Options

* **Export Frames as PNGs:** Download high-quality PNG screenshots of your frames. This is ideal for adding to documentation, or presenting visual concepts.
* **Export Agent Prompt:** Download an agent-ready prompt as a Markdown file. This allows you to reuse the generated design structure as context in AI workflows or modify it further using natural language instructions.
* **Export to FlutterFlow:** Copy all frames directly to your clipboard for pasting into a FlutterFlow project. Simply select a widget on a FlutterFlow project page and paste to import all your design instantly.

#### Export Storyboard

To export the entire storyboard, open the top-left **FF Designer** menu and choose one of the export options (PNGs, Agent Prompt, or FlutterFlow). This method is best when your full flow is ready for implementation.

![export-all.avif](https://docs.flutterflow.io/assets/images/export-all-51648fdd1bb34062810c024ff8917b21.avif)

#### Export a Single Frame

To export a single frame, select a specific frame and use the **Export** section in the right panel. Use this when you only need to implement a particular screen.

![export-single-screen.avif](https://docs.flutterflow.io/assets/images/export-single-screen-e6ce2e1682fbb34dd8ecef32b722bc23.avif)

---

### Import from FlutterFlow {#import-from-flutterflow}

*Bring existing FlutterFlow screens into Designer to enhance layouts, explore new styles, and refine the user experience faster.*

**Source:** https://docs.flutterflow.io/designer/import

Importing from FlutterFlow allows you to bring your existing app screens directly into the Designer environment. Instead of rebuilding UI from scratch, you can enhance layouts, explore new styles, and refine user experience faster. This is especially helpful when you want to modernize an existing app, experiment with different design directions, or quickly generate improved versions of your current screens.

To import screens from FlutterFlow, select **Export to Designer** from the canvas menu options, then choose the pages you want to send in the export dialog. Once selected, click the export button to transfer them. After the process completes, the selected pages will open in FF Designer, where you can continue customizing and iterating on them.

---

### Integrations {#integrations}

*Connect FlutterFlow Designer with AI agents and developer tools to generate, edit, and update designs using natural language from your preferred environment.*

**Source:** https://docs.flutterflow.io/designer/integrations

You can connect FlutterFlow Designer with external AI agents and developer tools. This enables you to generate, edit, and inspect designs directly from your preferred AI environment instead of working only inside the Designer UI.

For example, you can use an agent like Claude or Codex to open your design, make layout changes, add components, or iterate on styles just by describing what you want in natural language.

Prerequisites

Before using integrations, make sure the following are set up:

* [**FlutterFlow Designer Desktop App**](https://storage.googleapis.com/flutterflow-downloads/designer/macos/prod/flutterflow-designer-latest-macos.dmg) is installed (currently available only on macOS)

* **Agent MCPs** are installed via CLI. The install commands are: * **Claude Code:** `npm install -g @anthropic-ai/claude-code`
  * **Gemini CLI:** `npm install -g @google/gemini-cli`
  * **Codex CLI:** `npm install -g @openai/codex`

* Supported **IDEs** are installed on your system. To download, use the official links: * **Cursor:** <https://cursor.com/download>
  * **Antigravity:** [https://antigravity.google/download](https://cursor.com/download)

#### Installation

To add integrations, go to the **Integrations** section inside FlutterFlow Designer. Here you will see available integrations under **Agent MCPs** (such as Claude Code, Gemini CLI, and Codex) and **IDEs** (such as Cursor, Antigravity). Click **Install** next to any integration you want to use.

#### Launch Agent

To launch an agent and update the design:

1. Open your design project and click the agent menu option in the top-right side.
2. Choose where you want to open the project, such as **Open in Claude Code**, **Open in Gemini CLI**, **Open in Cursor**, or **Open in Antigravity**.
3. Once the terminal opens, describe the change you want to make. For example, ask the agent to create more variations of a selected screen or modify the current design.
4. When the agent asks for permission to run a Designer MCP tool, approve the request so it can inspect and update the project.
5. Wait for the agent to complete the task. It will create or update frames inside your current design project.
6. Return to FF Designer and review the generated frames or changes.

#### MCP Calls

MCP Calls let an AI assistant work directly with your current FF Designer project. It can read, edit, create screens, update UI, manage components, adjust themes, and export designs.

There are two main calls:

* `create_session`: Connects the assistant to your open project and returns a session ID with available tools. Must be called first.
* `call_design_script`: Executes actions like editing screens, creating layouts, updating content, or exporting designs.

Using MCP Calls, an assistant can work with:

* **Designs**: Create, open, rename, or export projects
* **Frames (Screens)**: Create, duplicate, edit, or organize screens
* **Nodes (Elements)**: Update text, colors, images, layout, and structure
* **Components**: Create reusable UI, edit once and update everywhere
* **Theme**: Control colors, typography, spacing, and styles
* **Images & Assets**: Upload, replace, generate, and manage media
* **Captures**: Take screenshots of screens or elements
* **Selection**: Work on currently selected items
* **History**: Undo, redo, and review changes

The assistant operates directly on your design, making it easy to iterate quickly and visually.

---

### Iterate {#iterate}

*Refine and improve your generated screens visually, with AI prompts, or by editing the global theme.*

**Source:** https://docs.flutterflow.io/designer/iterate

After generating your initial storyboard, you can refine and improve your screens in two ways: [editing visually](https://docs.flutterflow.io/designer/iterate#edit-visually) on the canvas and [using AI prompts](https://docs.flutterflow.io/designer/iterate#use-ai-prompt). Each method is useful depending on the type of change you want to make.

#### Edit Visually

This is useful when you want precise control over layout and structure. It makes it easy to quickly add or adjust elements exactly where you want them.

To start, click on any UI element in the canvas. The selected element will be highlighted, and small dots will appear around it. You can click any of these dots to add a new UI element at that position. When you click a dot, a selector pop-up opens, allowing you to choose and insert a new element.

You can also rearrange elements using drag and drop. Simply select an element and move it to a new position within the layout.

##### Use Properties Panel

The Properties Panel allows you to make precise adjustments to any selected widget. When you click on an element in the canvas, its editable properties appear on the right side. From there, you can modify properties such as text content, typography settings, spacing, alignment, colors, borders, and other styling attributes. This gives you direct control over how each element looks and behaves without needing to regenerate the entire screen.

Unlike AI-driven changes, edits made here are exact and predictable, making it ideal for polishing the design once the overall layout and structure are already in place.

#### Use AI Prompt

This method is best for structural, layout, or multi-element changes. To make a change using AI Prompt:

1. Click on the screen (frame) you want to update from the canvas or Frames panel.
2. Use the prompt bar at the bottom to clearly describe what you want to modify.
3. If you're not satisfied with the result, use the regenerate option to explore a new variation of the same instruction.
4. You can click directly on a widget. The selected widget will automatically be added to the prompt bar as context for your next instruction, allowing more precise AI updates.

You can also select a page and ask the AI to generate variations of it. This helps you quickly explore different design directions.

#### Edit Theme

Editing a **Theme** allows you to modify the global design system of your entire storyboard at once. Instead of adjusting individual widgets, you can change core styling elements such as brand colors, typography, spacing, corner radius, and text scaling. Any updates made in the Theme Editor automatically apply across all screens, ensuring visual consistency without manual updates on each page.

---

### Prompting {#prompting}

*Generate your first app design from a prompt. Explore styles, attach reference images, and create a complete storyboard from a single description.*

**Source:** https://docs.flutterflow.io/designer/prompting

Prompting is how you turn an idea into screens. Describe your app in the main prompt box, optionally attach a reference image, and the Designer generates a complete editable storyboard for you.

#### Create Designs

Here's how you generate an initial screen design, refine, and export it:

1. You can select [**Explore Styles**](https://docs.flutterflow.io/designer/prompting#explore-styles) to first browse and refine design ideas, or choose **Instant Generation** to skip that step and quickly create designs from your prompt.

2. Go to the **main prompt box** and write your app vision with important details (e.g., app type, target users, key screens, primary actions, and any must-have features). For example: *"Design a travel planning app with a modern card-based layout, destination image grids, a bottom navigation bar with Explore, Trips, Bookings, and Account tabs, saved itineraries, map integration, and a trip detail screen with timeline and booking information."*

3. Optionally, [**attach an image**](https://docs.flutterflow.io/designer/prompting#add-image-attachments) such as a sketch, wireframe, or screenshot using the image attachment button below the prompt field. The Designer will use it as a reference to transform it into a fully editable design.

4. Use the mobile and desktop toggle to set your target platform. This ensures your designs are generated with the correct layout and screen dimensions for your intended device.

5. Click the **submit** (up-arrow) button to generate your design storyboard.

6. Review the generated screens. Scan through the generated frames to confirm: * The right screens exist (and no critical screens are missing)
   * The overall flow makes sense
   * The UI direction matches your intent

7. Select a screen to refine. You can [**use the prompt bar**](https://docs.flutterflow.io/designer/iterate#use-ai-prompt) to request changes to the selected screen.

8. You can also make precise tweaks from the [**Properties panel**](https://docs.flutterflow.io/designer/iterate#use-properties-panel). Select an element and adjust its properties on the right side, such as text, typography, spacing, styling.

9. To add a new screen, click on an empty area of the canvas, then in the bottom prompt input, describe the screen you want to add. Include its purpose, key UI elements, and how it connects to the overall flow, then submit.

10. Open the **Theme** tab to edit global styling like colors, typography, spacing, and radius so the entire design stays consistent.

11. You can generate a **shareable link** for feedback and review.

12. To export your design, open the top-left app menu (FF Designer) and choose an **export option**.

##### Explore Styles

**Explore Styles** helps you try different visual directions for your app before generating the final design. Instead of going straight to a full build, you can first browse style variations, compare layouts, adjust colors, and guide the design toward the look you want.

This is useful when you already know what your app should do, but want help deciding how it should look.

Once the styles are generated, browse through the generated variants and look for the one that feels closest to your vision. Each style gives you a different take on the same app idea, such as a different layout, spacing, typography, or visual mood.

When you hover over a style, you can use the following options:

* **Regenerate**: Recreates the style if something looks off or needs improvement.
* **More Like This**: Generates more variations similar to the selected style.
* **Remix Colors**: Keeps the overall style but changes the color palette.
* **Prompt for Changes**: Lets you describe specific updates you want for that style.
* **Use This Style**: Selects that style and starts the full generation process.

##### Add Image Attachments

You can attach reference images directly in the prompt to guide the design generation process. This is useful when you have an existing sketch, low-fidelity wireframe, competitor screenshot, or inspiration design that you want the Designer to follow.

To do so, simply click the image attachment button below the prompt field and upload your image. The AI will analyze the layout, visual hierarchy, and structure, then transform it into a clean, fully editable multi-screen design.

For example, you might upload a rough wireframe of a food delivery app showing a home screen with a search bar, restaurant cards, and a bottom navigation bar. Along with the image, you can add a prompt such as "Using the attached screenshot as a reference, convert this wireframe into a modern food delivery app design."

#### FAQ

Are charts from Designer converted into FlutterFlow chart widgets?

Yes. Bar charts, line charts, and pie charts created in the Designer are automatically converted into fully functional FlutterFlow chart widgets.

![ff-designer-chart-conversion](https://docs.flutterflow.io/assets/images/ff-designer-chart-conversion-fa4fa0a5bbaffd262bbff76cbf48c1c3.avif)

---

### Quickstart {#quickstart}

*Get started with designing your first app quickly.*

**Source:** https://docs.flutterflow.io/designer/quickstart

FF Designer lets you generate complete app designs from simple text prompts. Just describe what you want to build, explore different style directions, and the Designer will create a full set of screens for you. From there, you can refine the design using AI or manual editing and export it directly to continue building.

Ready to design your app? Simply:

1. Open FF Designer and click the prompt bar that says **Describe your app**
2. Enter your app idea and press **Enter** to generate designs
3. Browse style variants and click **Use This Style**
4. Review the generated screens in the canvas
5. Edit using AI or manually adjust elements and properties
6. Export your design to FlutterFlow, PNG, or Agent Prompt

The Designer generates complete app screens in seconds, giving you a strong starting point that you can quickly refine and turn into a real app.

#### Sample Prompts

Here are some prompts you can try in FF Designer to quickly generate complete app designs.

##### Personal Finance Tracker

**Prompt**

Design a personal finance app that helps users track expenses and manage budgets. Show a dashboard with total balance, recent transactions, and spending categories. Include detailed views for transaction history and budget insights. Make the UI clean, modern, and easy to understand.

![finance-app.avif](https://docs.flutterflow.io/assets/images/finance-app-8ffa78c3f7319b18a7e7762a8e221bdf.avif)

##### Fitness Workout App

**Prompt**

Create a fitness app with a home screen showing daily workouts, progress stats, and streaks. Include workout detail screens with exercises, sets, and timers. Make the design energetic, modern, and easy to follow.

![fitness-tracking-app.avif](https://docs.flutterflow.io/assets/images/fitness-tracking-app-bb5432071c0bf822fb2e5e325f0b1753.avif)

##### Food Delivery App

**Prompt**

Design a food delivery app with a home screen showing nearby restaurants, categories, and featured items. Include restaurant detail pages, menu listings, and a checkout flow. Make the UI modern, colorful, and easy to navigate.

![food-delivery-app.avif](https://docs.flutterflow.io/assets/images/food-delivery-app-2d46a90c637607c3c9370ed25f2929cc.avif)

---

### Slides {#slides}

*Turn a FlutterFlow Designer project into a presentation deck. Design 16:9 slides, present with presenter view, and import or export PowerPoint files.*

**Source:** https://docs.flutterflow.io/designer/slides

**Slides** turns a FlutterFlow Designer project into a presentation deck. Instead of designing phone, tablet, or desktop screens, each frame becomes a 16:9 slide. You get speaker notes, a real present-with-presenter-view mode, and two-way PowerPoint support: import an existing `.pptx` to edit, or export your deck back out to `.pptx`.

#### Set up a slide deck

1. Switch the project's device type to **Slides**.
2. Frames become fixed presentation sizes: **1280×720** (720p) or **1920×1080** (1080p).
3. Describe the deck you want in the prompt textbox (your topic, key points, and how many slides) and let Designer generate it.
4. Once the deck is generated, refine each slide manually, just like any other design project.

##### Speaker notes

Each slide gets its own **speaker notes** field in the right-hand panel. These notes show up in presenter mode and travel with PowerPoint import and export.

#### Present the slideshow

To start, click the **Present** button in the top bar (only visible on Slides projects), or use the present keyboard shortcut.

You get a two-window setup:

* A full-screen **audience view**: clean, black background, showing exactly what the room sees.
* A separate **presenter window** showing the current slide, a preview of the next slide, your speaker notes, an elapsed-time timer, and prev/next controls.

##### Navigation shortcuts

| Action   | Keys                                                       |
| -------- | ---------------------------------------------------------- |
| Next     | `→` · `↓` · `Space` · `Page Down` · or click/tap the slide |
| Previous | `←` · `↑` · `Page Up`                                      |
| Exit     | `Esc`                                                      |

> **Tip:** You can keep editing slides while presenting, and changes sync live into the presentation. When you exit, the canvas jumps back to whatever slide you ended on.

#### Export to PowerPoint

In the left panel, choose **Export to PowerPoint**, or use the **Export presentation (.pptx)** button in the right panel.

The result is a real, editable PowerPoint file: text stays as editable text and shapes stay as shapes (not flattened images) wherever possible. Charts export as native charts; icons that can't be represented natively are rendered as images.

---

### Workspace {#workspace}

*Learn about FlutterFlow Designer's workspace that provide a complete design environment with specialized tools.*

**Source:** https://docs.flutterflow.io/designer/workspace

The workspace is organized into panels that work together to provide a complete design experience.

![ff-designer.avif](https://docs.flutterflow.io/assets/images/ff-designer-36dc528ec8066b359fded4a387a0dc67.avif)

* **Frames Panel**: Displays all screens of the app and allows quick navigation between them.
* **Components Panel**: Create reusable UI elements.
* **Theme Panel**: Make global theme customization.
* **Layers Panel**: Shows the hierarchical structure of widgets within the selected screen.
* **Canvas Area**: Visual preview of all screens in storyboard layout.
* **Undo/Redo Controls**: Quickly revert or reapply recent design changes.
* **Light/Dark Mode Toggle**: Switch between light and dark preview modes to instantly see how your design adapts across themes.
* **Zoom Controls**: Adjust zoom level for better overview or detailed editing.
* **Share Button**: Share the current design or collaborate with others.
* **Properties Panel**: Edit properties of the selected widget such as layout, content, and styling.
* **Prompt Bar**: Use AI commands to describe changes and modify the selected screen or widget.

---

---

## FlutterFlow CLI

### FlutterFlow CLI {#flutterflow-cli}

*Learn how to download and manage your FlutterFlow projects locally using the FlutterFlow CLI.*

**Source:** https://docs.flutterflow.io/flutterflow-cli

The [FlutterFlow CLI](https://pub.dev/packages/flutterflow_cli) lets you manage FlutterFlow projects from the command line. You can create new projects, modify existing ones using AI agents, and download them to your local machine.

#### Installation

To use the FlutterFlow CLI, you first need to install it globally using Dart's package manager with the following command:

```
dart pub global activate flutterflow_cli
```

##### Get API Token

To use the CLI, you'll need to create an API token and use it in your requests. See the documentation [here on how to generate an API token.](https://docs.flutterflow.io/accounts-billing/account-management#how-do-i-generate-an-api-token)

#### FAQ

I am getting an error as FormatException: Missing argument for…

This error likely indicates that you haven't correctly entered the command option along with its value. Double-check that all required information has been entered. If everything is correct and you're still encountering the error, it might be due to using an outdated version of the FlutterFlow CLI. To resolve this, you can update to the latest version by running the installation command:

```
dart pub global activate flutterflow_cli
```

This should update the CLI and fix the issue.

---

### Build with AI Agents {#build-with-ai-agents}

*Create and edit FlutterFlow projects from your terminal using your preferred AI coding agent.*

**Source:** https://docs.flutterflow.io/flutterflow-cli/build

The [FlutterFlow CLI](https://pub.dev/packages/flutterflow_cli) lets you create and edit FlutterFlow apps from the terminal using your own AI coding agent — Claude Code, Gemini CLI, Codex, or any MCP-compatible client. You describe what you want in plain English, the agent plans and applies the changes, and the result lands as a real FlutterFlow project you can open in the visual builder.

A FlutterFlow project is the source of truth. The CLI is how you create or edit it from your local workspace.

![flutterflow-cli-ff-builder-using-same-ff-app](https://docs.flutterflow.io/assets/images/flutterflow-ff-builder-using-same-ff-app-ec46b7dc9dab6a03f2766eca594ffa83.avif)

#### Architecture

`flutterflow ai init` creates a local **workspace** - a folder pre-configured with an MCP config file pointing at the FlutterFlow MCP server. When you launch your AI agent inside that folder, it discovers the MCP server and gains a set of tools that talk to FlutterFlow's cloud:

1. You prompt the agent.
2. The agent plans changes and calls the MCP server's tools.
3. The MCP server applies those changes to your FlutterFlow project.
4. You verify the result in the FlutterFlow visual builder.

The workspace is just a folder on your disk. The actual project lives in FlutterFlow server.

What is MCP?

The [**Model Context Protocol**](https://modelcontextprotocol.io) is an open standard that lets AI agents call external tools. The FlutterFlow AI MCP server exposes FlutterFlow's project APIs to your agent so it can read and modify your project on your behalf.

Remember

* **FlutterFlow CLI is not a replacement for the visual builder.** FlutterFlow is still faster for most visual work. FlutterFlow CLI is for precision, repeatability, and automation.
* **FlutterFlow CLI doesn't execute your app.** It produces a FlutterFlow project, which you can test and run inside the FlutterFlow visual builder.

Prerequisites

Before you start, make sure you have:

* **FlutterFlow CLI installed.** See [**Installation**](https://docs.flutterflow.io/flutterflow-cli).
* **A FlutterFlow API key.** See [**generating an API token**](https://docs.flutterflow.io/accounts-billing/account-management#how-do-i-generate-an-api-token).
* **An MCP-compatible AI agent installed locally** — for example, [**Claude Code**](https://www.claude.com/product/claude-code), [**Gemini CLI**](https://github.com/google-gemini/gemini-cli), or [**Codex**](https://github.com/openai/codex).
* **A FlutterFlow project ID** (only if you're editing an existing project).

#### Setup Workspace

Open your terminal in the folder where you want the workspace to live, then run:

```
flutterflow ai init
```

By default, `flutterflow ai init` targets the production FlutterFlow environment. To initialize a workspace against a non-production environment, pass the environment explicitly:

```
flutterflow ai init --env beta
flutterflow ai init --env enterprise-india
```

This launches an interactive setup wizard. Walk through the prompts:

1. **Workspace name.** A short, lowercase name with no spaces. This becomes the folder name for your project. ```
   Workspace name
     Directory to scaffold the FlutterFlow AI workspace in.
   > mindfly
   ```

2. **Existing project ID.** Press **Enter** with no input to create a new app, or paste an existing project ID to bind the workspace to it. ```
   Existing project ID to edit (press Enter to create a new app)
   >
   ```

3. **FlutterFlow API key.** Paste your API key and press **Enter**. Input is masked.

4. **Register MCP server with detected coding CLIs.** The wizard scans your `PATH` and offers to register the FlutterFlow AI MCP server with each agent it finds (Claude Code, Gemini CLI, Codex). Answer `Y` (default) for each one you plan to use. ```
   Register FlutterFlow AI MCP server with coding CLIs
     Detected: claude, gemini, codex
     Register with claude? [Y/n]
   ```

5. **Confirm.** The wizard prints a summary. Review it and press **Enter** (default `Y`) to proceed. ```
   Ready to create:
     Workspace:  mindfly
     Project ID: (none — unlinked)
     API key:    set (***abcd)
     Base URL:   https://api.flutterflow.io  (built-in for prod)
     MCP CLIs:   claude, gemini, codex

   Proceed? [Y/n]
   ```

When the wizard finishes, you'll have a workspace folder ready for your agent. Depending on which CLIs you registered, the folder will contain one or more of:

* `.mcp.json` — for Claude Code
* `.gemini/settings.json` — for Gemini CLI
* `.codex/config.toml` — for Codex

Each file points the corresponding agent at the FlutterFlow AI MCP server.

#### Launch your Agent

Move into the workspace and start your agent. The example below uses Claude Code; the same pattern applies to any agent you registered in the wizard — `cd` into the workspace and launch the agent's CLI.

```
cd mindfly
claude
```

The first time the agent opens the workspace, it detects the new MCP server and asks you to approve it. The exact prompt varies by agent — Claude Code's looks like this:

```
New MCP server found in .mcp.json: flutterflow_ai

MCP servers may execute code or access system resources.
All tool calls require approval.

> 1. Use this and all future MCP servers in this project
  2. Use this MCP server
  3. Continue without using this MCP server
```

Choose **option 1** to approve the FlutterFlow AI MCP server (and any others added to this workspace later) without being asked again.

> **Why approve?** Without the MCP server, the agent can edit local files but can't push changes to your FlutterFlow project. With it approved, the agent has the same tools you'd run yourself from the CLI.

#### Generate a New App

With the agent connected, describe the app you want at the prompt:

```
> create a minimalist meditation app
```

Phrase it however you like — `a recipe-sharing app with a social feed`, `a habit tracker with streaks`, `a tip calculator for restaurants`. The agent plans the app, generates the changes, pushes them to FlutterFlow through the MCP server, and reports back. Open FlutterFlow in your browser and navigate to the project — the generated app will be reflected in the visual builder. From there you can keep refining visually or send another prompt to the agent.

Once the app exists, the workspace is bound to it. Follow-up prompts in the same session are treated as edits, not new generations, you'll see the agent acknowledge the switch with something like:

```
The project is bound, so I'll switch to edit mode.
Let me check the workspace and read the edit template.
```

From that point on, the same rules apply as when [editing an existing project](https://docs.flutterflow.io/flutterflow-cli/build#edit-an-existing-project) - concurrency, branches, scope, and refreshing context.

#### Edit an Existing Project

Prerequisite

Have your **project ID** ready. Open the project in the FlutterFlow editor. The project ID is the path segment after `/project/` in the URL.

Editing an existing project follows the same flow as [creating a new one](https://docs.flutterflow.io/flutterflow-cli/build#setup-workspace) — you run `flutterflow ai init` to scaffold a workspace, then drive changes from your agent. The only difference is one step in the wizard: when it asks for an **existing project ID**, paste yours instead of pressing Enter:

```
Existing project ID to edit (press Enter to create a new app)
> mindfly-c9lbgr
```

The workspace is now bound to that project. `cd` into the workspace folder, [launch your agent](https://docs.flutterflow.io/flutterflow-cli/build#launch-your-agent), and describe the changes you want — "add a profile screen", "switch the primary color to teal", "wire up the login form to Firebase Auth". The agent reads the current project, plans the change, and pushes it through the MCP server. Open FlutterFlow in your browser to verify.

##### Copy AI Selector

You can right-click any widget in the builder and select **Copy AI Selector** when you want the agent to update a specific widget in your app. This copies a precise location for the selected widget, which you can paste into your prompt so the agent knows exactly which widget to inspect or modify.

This is helpful when a page has repeated widgets, nested components, or similar labels. Instead of describing the widget only by its position or text, you can give the agent the copied selector value and ask for a targeted change, such as updating that widget's style, action, visibility, or data binding.

##### Concurrent Edits with Builder

You can edit visually while an agent is working, but writes use **optimistic concurrency**: when the agent pushes, the server checks the project's last-modified timestamp against the agent's snapshot. If anyone else (you in the visual builder, a teammate, or another agent) modified the project in between, the push is rejected. The agent will re-read the latest state and retry — which may also mean re-planning, if your change conflicts with what it was about to do.

So nothing gets silently overwritten, but expect occasional retries when you and the agent are editing the same project at once.

##### Agent Edit Scope

**In scope**

* Pages, components, app state, theme, navigation, action blocks, app events
* Custom functions, actions, widgets, classes, and enums
* API endpoints, queries, custom data types and enums
* Pub and library dependencies, design tokens, GenUI catalog, Firebase Auth wiring

**Out of scope**

* Anything outside the FlutterFlow project itself — running the app, deploying it, creating Firebase projects, managing secrets, App Store submissions.

##### Refreshing Stale Context

If you've made visual edits since the agent last read the project, the agent's local snapshot is stale. Two ways to fix it:

* **Ask the agent to refresh.** Most agents call the [`refresh-context`](https://docs.flutterflow.io/flutterflow-cli/build#mcp-tools) tool on their own when they detect drift, but you can prompt explicitly: "refresh the project context."
* **Run it from the CLI.** `flutterflow ai context-check` reports whether the local snapshot is behind, and `flutterflow ai refresh-context <project-id>` pulls the latest.

See [MCP tools](https://docs.flutterflow.io/flutterflow-cli/build#mcp-tools) for the full command list.

#### Live Sessions

Live Sessions let your AI agent apply changes to a running FlutterFlow app and display those updates directly on the connected device. This is useful when you want to iterate quickly. You can ask the agent to update screens, fix issues, inspect logs, trigger hot reloads or hot restarts, capture screenshots, and then immediately review the results on your running devices.

To use Live Sessions, run your app from the FlutterFlow desktop app on a connected device or simulator, then activate your agent. Once the live session starts, confirm its status in the desktop app, ask the agent to make changes, and review those updates as they appear in the running app.

> **Info:** Keep the desktop app and the running app session open for as long as you want live updates to continue.

#### Branches and Rollback

The CLI can point to any branch of a FlutterFlow project. Since each branch is accessed through its own URL, it has its own project ID. To work on a specific branch, open it in the FlutterFlow editor, copy the project ID from the URL, and paste it when `flutterflow ai init` prompts for an existing project ID.

To roll back, use FlutterFlow's project version history in the visual builder — the same mechanism you'd use for visual edits. Each agent push lands as a commit there with whatever commit message the agent supplied.

#### Switching Projects

A workspace is bound to one project. To work on a different project, run `flutterflow ai init` in a **new** folder and link it to the new project ID. `init` refuses to run in a non-empty directory, so it won't re-bind an existing workspace.

#### MCP tools

Run these from inside a FlutterFlow AI workspace. Your agent calls them via the MCP server; you can also run them directly in the terminal.

| Category           | Command             | What it does                                                                                                           |
| ------------------ | ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Build**          | `run`               | Apply changes to your FlutterFlow project.                                                                             |
|                    | `validate`          | Dry-run a change without pushing it.                                                                                   |
| **Explore**        | `inspect`           | Whole-project summary or a scoped view of structure.                                                                   |
|                    | `resources`         | List reusable project and library resources.                                                                           |
|                    | `search`            | Search the project for a name or identifier.                                                                           |
|                    | `status`            | Show workspace and project state.                                                                                      |
| **AI integration** | `mcp`               | Register the FlutterFlow MCP server with Claude Code, Codex, Gemini CLI, Cursor, Copilot, and other MCP-aware clients. |
| **Plan & audit**   | `plan`              | Capture intent before a run.                                                                                           |
|                    | `trace`             | Replay a prior run.                                                                                                    |
|                    | `history`           | List prior commands and outcomes.                                                                                      |
| **Diagnose**       | `doctor`            | Check for common workspace problems.                                                                                   |
|                    | `context-check`     | Report whether the local snapshot is behind the live project.                                                          |
|                    | `precache`          | Pre-load project context.                                                                                              |
| **Stay current**   | `upgrade`           | Update the FlutterFlow CLI tooling.                                                                                    |
|                    | `refresh-workspace` | Refresh the workspace's local config.                                                                                  |
|                    | `refresh-context`   | Pull the latest project state into the local snapshot.                                                                 |
| **Learn**          | `docs [topic]`      | Open FlutterFlow AI documentation for a topic.                                                                         |

Run `flutterflow ai --help` from inside a workspace for the full command list and per-command flags. When the agent invokes a command via MCP, every call is subject to your agent's approval rules.

---

### Exporting Projects {#exporting-projects}

*Learn how to download and manage your FlutterFlow projects locally using the FlutterFlow CLI.*

**Source:** https://docs.flutterflow.io/flutterflow-cli/exporting

Follow the steps below to export your project.

[Sharing a Project with a User](https://demo.arcade.software/Rc3s1P8DFypUKoPzVITL?embed\&show_copy_link=true)

##### Command Details

* If you wish to exclude assets from the download, use `-no-include-assets` in your command. This will download the project code without the assets. For example: `flutterflow export-code --project your_project_id --dest path_to_output_folde --no-include-assets --token your_token`

* You can download code from a specific branch by switching to that branch and using the toolbar command, or by including the `-branch-name` or `-b` flag in your command and specifying the branch you wish to download from.

###### All supported command options

| Flag                   | Behavior                                                                                                                                       | Default             |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| --dest / -d            | Specifies a destination folder other than the current directory.                                                                               | Current directory   |
| --\[no]-include-assets | Option to download assets (images, GIFs). Useful for consecutive code exports if the assets folder hasn't changed.                             | False               |
| --branch-name / -b     | Downloads from a specific branch.                                                                                                              | Main                |
| --\[no]-fix            | Option to run dart fix on the code after downloading.                                                                                          | False               |
| --\[no]-parent-folder  | Option to download the code into a subfolder instead of directly into the directory.                                                           | False               |
| --\[no]-as-module      | Whether to generate the project as a Flutter module.                                                                                           | False               |
| --\[no]-as-debug       | Whether to generate the project with debug logging to be able to use FlutterFlow Debug Panel inside the DevTools.                              | False               |
| --project-environment  | Which [development environment](https://docs.flutterflow.io/testing/dev-environments) to be used. If empty, the current environment in the project will be downloaded. | Current environment |

##### Filtered exports

If you are updating an existing project and do not want certain files to be overwritten during a code export, you can create a `.flutterflowignore` file in the root of your project directory. This file should contain a list of files to be ignored using globbing syntax.

###### Example:

If your project is located at:

```
/Users/yourname/projects/my_flutterflow_app/
```

Then, place the `.flutterflowignore` file in:

```
/Users/yourname/projects/.flutterflowignore
```

###### Example `.flutterflowignore` contents:

```
my_flutterflow_app/android/app/build.gradle    # Prevents FlutterFlow from overwriting native Android build configuration
my_flutterflow_app/ios/Runner/Info.plist       # Keeps iOS app metadata unchanged
my_flutterflow_app/web/index.html              # Ensures custom modifications to the web entry file are retained
```

This ensures that the specified files and directories are not overwritten during code export.

For more details on globbing syntax, refer to [this guide](https://pub.dev/packages/glob#syntax).

#### FAQ

I am getting an error as FormatException: Missing argument for…

This error likely indicates that you haven't correctly entered the command option along with its value. Double-check that all required information has been entered. If everything is correct and you're still encountering the error, it might be due to using an outdated version of the FlutterFlow CLI. To resolve this, you can update to the latest version by running the installation command:

```
dart pub global activate flutterflow_cli
```

This should update the CLI and fix the issue.

---

---

## FlutterFlow UI & Dashboard

### App Builder {#app-builder}

*Explore the App Builder in FlutterFlow, featuring a comprehensive interface with four main sections-Navigation Menu, Toolbar, Canvas, and Properties Panel.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/builder

On opening the project, you'll see the App Builder, which consists of four main sections: [Navigation Menu](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu), [Toolbar](https://docs.flutterflow.io/flutterflow-ui/builder#toolbar), [Canvas](https://docs.flutterflow.io/flutterflow-ui/builder#canvas-area), and [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel).

![navigation-menu.avif](https://docs.flutterflow.io/assets/images/navigation-menu-d7267cc6d7230adcd7258b08f5ceefaa.avif)

#### Navigation Menu

The Navigation Menu, located on the left side of the builder, allows you to switch between various FlutterFlow features. These include designing the UI, managing databases, setting up API, adjusting app settings, adding integrations, and more.

Here is a list of all the features accessible from the navigation menu:

1. **Dashboard**: Manage projects, access account info, and FlutterFlow resources.
2. **Widget Palette**: Access all widgets for your app.
3. **Page Selector**: Manage pages, components, and custom code files, and organize them using folders.
4. **Widget Tree**: Get an overview of all widgets on a selected page.
5. **Storyboard**: Visualize app's design and navigation.
6. **Test Mode**: [Test your app](https://docs.flutterflow.io/testing/run-your-app#test-mode) in a live debugging environment.
7. **Firestore**: Create collections and adjust Firestore-related settings.
8. **Data Types**: Create custom data types for your app.
9. **App Values**: Manage [App State variables](https://docs.flutterflow.io/resources/data-representation/app-state) and Constants.
10. **API Calls**: Define API calls.
11. **Media Assets**: Upload assets for your app and team.
12. **Cloud Functions**: Write and deploy cloud functions for Firebase.
13. **Tests**: Add automated tests.
14. **Agents**: Create, configure, and manage [AI Agents](https://docs.flutterflow.io/integrations/ai-agents) to integrate conversational AI interactions into your app.
15. **App Events**: Define and manage [App Events](https://docs.flutterflow.io/concepts/app-events) that allow different parts of your app to communicate without being directly connected.
16. **Theme settings**: Customize visual appearance.
17. **Settings and Integrations**: Access app-related settings and integrations.

#### ToolBar

From [ToolBar](https://docs.flutterflow.io/flutterflow-ui/toolbar), you can search for project resources, change canvas size, see project history, branching, optimization and enhancements, view-download code, and run your app.

#### Canvas Area

In the [Canvas Area](https://docs.flutterflow.io/flutterflow-ui/canvas), you can see a preview of a device's screen and build your app page.

#### Properties Panel

The Properties Panel lets you modify both the visual appearance and interactive behavior of UI elements on the canvas. It allows you to add [Actions](https://docs.flutterflow.io/resources/functions/action-flow-editor), set up a [Backend Query](https://docs.flutterflow.io/resources/backend-query), add [Animations](https://docs.flutterflow.io/concepts/animations) and more.

The Properties Panel will vary slightly depending on the entity you have selected. To explore the details of each Properties Panel, click on the following:

* **[Page Properties](https://docs.flutterflow.io/resources/ui/pages/properties)** (when you have selected a Page)
* **[Widget Properties](https://docs.flutterflow.io/resources/ui/widgets/properties)** (when you have selected any widget, including built-in components)

---

### Canvas {#canvas}

*Dive into the versatile Canvas in FlutterFlow, where you can effortlessly design and preview your app’s interface.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/canvas

The Canvas shows the selected device screen, such as mobile, tablet, web, or desktop. It allows you to add widgets via drag-and-drop. You can select, move, and position widgets anywhere on the Canvas.

The Canvas also includes zoom controls, light and dark previews, multi-language preview, App Bar and Nav Bar controls, text size simulation, and more.

![canvas area](https://docs.flutterflow.io/assets/images/canvas-5fb2f2b205ec872d07cffb04be6b5be8.avif)

#### Show or Hide Navigation Menu

From here, you can open or close the [Navigation Menu](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu).

#### Zoom Controls

There are zoom in (+) and zoom out (-) buttons to control the zoom level of the Canvas. While working on complex UI designs, this comes in handy when you want to zoom in on a specific area or zoom out for an overview.

#### Preview Screen

The Preview Screen is where you build the UI for the selected device. You can customize the screen by adding widgets using drag and drop from the [Widget Palette](https://docs.flutterflow.io/flutterflow-ui/widget-palette) and by applying properties from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel).

#### Set Preview Screen Size

Use the screen size controls at the top of the Canvas to preview your app at different dimensions. Select the mobile, tablet, or desktop icon to switch between device types and test how your layout responds on each screen size.

You can also set a custom preview size by clicking the current size box, entering the desired **Width (px)** and **Height (px)** values, and then clicking **Save**.

[Set Preview Screen Size](https://demo.arcade.software/DfBQoBkkkRX68CIYoWwD?embed\&show_copy_link=true)

#### Add App Bar

From here, you can add an [App Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#appbar) to your page. Clicking this button opens a popup displaying different App Bar styles for you to choose from. Select an App Bar style from the list, and it will appear in the Preview Screen.

![appbar-style.avif](https://docs.flutterflow.io/assets/images/appbar-style-69cc04345c9bf715e4889aafb113b01d.avif)

#### Designer Import/Export

Use this menu to copy screens between FlutterFlow and FlutterFlow Designer.

* **Export to Designer:** Copy pages from your FlutterFlow project into Designer, where you can explore new styles and continue refining the layouts. See [Import from FlutterFlow](https://docs.flutterflow.io/designer/import) for detailed instructions.
* **Paste from Designer:** Copy designs from Designer into your FlutterFlow project. In Designer, use **Export to FlutterFlow** to copy the frames, then select **Paste from Designer** on the Canvas. See [Export from Designer](https://docs.flutterflow.io/designer/export#export-options) for more information.

#### Dark/Light Mode

Use this toggle to switch your app preview between light and dark mode, so you can ensure your design looks great in both modes. This feature is only available if you've enabled dark mode support in your project.

#### Builder Settings

Builder Settings let you adjust how the FlutterFlow builder, Canvas, preview screen, and Property Panel behave while you design.

![builder-settings](https://docs.flutterflow.io/assets/images/builder-settings-5d1f3329679f6d47bcee8981a5e130f3.avif)

##### Platform Settings

###### Set Builder to Dark Mode

Use this option to switch the FlutterFlow builder between light and dark mode. This changes the appearance of the FlutterFlow platform, not the theme of your app.

[Set Builder to Dark Mode](https://demo.arcade.software/95jb2CKZJKfviZqPsXKt?embed\&show_copy_link=true)

##### Canvas Settings

###### Enable Snapping

Enable snapping to make widget width and height snap to multiples of the specified value while resizing. This helps keep widget sizes consistent as you adjust layouts on the Canvas.

[Enable Snapping](https://demo.arcade.software/xdE4cilXUV1P7krYEJFg?embed\&show_copy_link=true)

###### Show Resize Bars

Show resize bars to display handles on the right and bottom sides of the preview screen. You can use them to resize the preview screen to a custom size and test how your layout responds at different screen sizes.

![handle-bars](https://docs.flutterflow.io/assets/images/handle-bars-bc6d168860d8ace0c4aec71c1c127450.gif)

###### Set Canvas Color

Use this option to change the background color of the Canvas. This can be helpful when creating components or previewing widgets against a different page background. For example, if a component uses dark text, setting a lighter canvas color can make it easier to see while designing.

[Set Canvas Color](https://demo.arcade.software/XoUnydzOgh3Uc2EruRo0?embed\&show_copy_link=true)

##### Device Preview Settings

###### Show Safe Area

Enable this option to show the device safe area in the builder. Safe areas help you preview where content may be affected by device notches, rounded corners, status bars, or other screen insets.

> **Note:** If the device bezel is displayed, the safe area is always enabled in the preview.

[Show Safe Area](https://demo.arcade.software/mhjqT9pmmyxEprnF5YOY?embed\&show_copy_link=true)

###### Adjust Text Sizing

Use this option to preview your app with different text scale settings. This helps you test how your UI responds when users increase text size from their device accessibility settings.

[Adjust Text Sizing](https://demo.arcade.software/uodCNZIibPCNQIfXPSKg?embed\&show_copy_link=true)

###### Display Keyboard

Enable this option to show the keyboard on the preview screen. This is useful for checking how form fields, buttons, and bottom-aligned content appear when the keyboard is open.

[Display Keyboard](https://demo.arcade.software/xoat6tc8gNwwPPWsHG0t?embed\&show_copy_link=true)

###### Display Device Bezel

Use this option to show the device frame in the preview. This is particularly useful for checking how your screen will look with device-specific features such as the safe area or notches on iPhones and Android devices.

[Display Device Bezel](https://demo.arcade.software/pCZChdW9S252zmOfnD2t?embed\&show_copy_link=true)

###### Show Overflows

Enable this option to show overflow errors in the builder as they will appear in Test Mode. This can help you catch layout issues before running or testing your app.

[Show Overflows](https://demo.arcade.software/dXXZAlLs0wMEj1E5SBAX?embed\&show_copy_link=true)

###### Display Language

If you've enabled multi-language support for your project, you can use this to preview your app in different languages. Open **Canvas Settings** and change the **Display Language** to preview the translated text in your app.

> **Tip:** This feature is valuable for testing your app across multiple locales without needing to run your app.

[Display Language](https://demo.arcade.software/Wt1s0IIxQXNQ5cdAMIIf?embed\&show_copy_link=true)

##### Property Panel Settings

###### Keep Common Properties Collapsed

Enable this option to keep common sections in the Property Panel collapsed by default, such as **Visibility**, **Padding**, and **Alignment**. This can make the Property Panel easier to scan when you only want to open the sections you need.

[Keep Common Properties Collapsed](https://demo.arcade.software/iXj6ebaDiAZjr0WLSzkQ?embed\&show_copy_link=true)

#### Add Nav Bar

Use this button to add the [Nav Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#nav-bar) to your page. Clicking it opens a popup where you can enable the Nav Bar for your project. Once the Nav Bar is enabled, you can customize it to match your design.

![add-navbar.avif](https://docs.flutterflow.io/assets/images/add-navbar-6d11cbb07831d4afe49cd682fe1b3671.avif)

#### Video Guide

Watch this video if you prefer watching a video tutorial.

[The Canvas | FlutterFlow University](https://www.youtube.com/embed/NDrte4nOXYc)

---

### Dashboard {#dashboard}

*Explore the dashboard in FlutterFlow, a centralized location for managing projects and your account.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/dashboard

When you log in to FlutterFlow, the first page you’ll see is the **Dashboard**. It serves as a central hub for managing your projects, including creating, searching for, deleting, and duplicating projects. The Dashboard also lets you choose your preferred theme—dark or light—for a more comfortable viewing experience.

The Dashboard provides convenient access to organizational resources, facilitating seamless collaboration among team members. It also integrates with a marketplace where users can browse and download widgets, templates, and plugins.

You can also find links to various resources to help you build apps with FlutterFlow. Your account information and plan details are easily accessible from this page as well.

![dashboard](https://docs.flutterflow.io/assets/images/dashboard-6259117ba315654d5e29a9450fc01022.avif)

* **Projects**: Projects section displays all the projects you have created in FlutterFlow. Use the overflow menu to rename, duplicate, delete, leave the project, add tags, and open the project in a new browser tab.

  info

  When you duplicate a project with Firebase configured, you must delete the config files in the duplicated project and initiate a new [**Firebase setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for it.

* **Notification Center**: The Notification Center simplifies how you manage comments and invites across projects. It centralizes all your project communications. When you're ready to address a comment, select it to go directly to the relevant section of the project.

* **Dark/Light Mode**: The Dark/Light Mode option allows you to choose between a light and dark color scheme for the app builder.

* **View Options**: Switch between **List View** and **Grid View** to choose how projects are displayed on the Dashboard. Grid View displays projects as tiles for visual browsing, while List View provides a compact layout for quickly scanning your projects.

* **Search**: This option allows you to search for your projects.

* **Filter Projects**: Filter projects by privacy setting: private, shared by you, or shared with you.

* **Tag Projects**: You can create and add a tag to projects, providing a quick and organized way to classify and identify projects based on their characteristics, purpose, or status. For detailed steps, see [Creating and Managing Tags](https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects#create-and-add-tags-to-projects).

* **Create a New Project**: To create a new project, use the **+ Create New** button. Learn more about [creating a new project](https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects#how-to-create-a-project).

* From **My Teams** section, you can share custom code, assets, design systems, and APIs among team members and across projects.

* **Marketplace**: Use the [**FlutterFlow Marketplace**](https://docs.flutterflow.io/marketplace) to access prebuilt components and templates created by other users and add new functionality to your app.

* **Resources**: From the **Resources tab**, you can find various useful links that can help you build apps on FlutterFlow. [Video tutorials](https://www.youtube.com/@FlutterFlow/videos) are extremely helpful for learning about concepts visually.

* **Community**: The **Community tab** redirects you to our [Community Forum](https://community.flutterflow.io/home), a place for you to share ideas, ask questions, and troubleshoot issues with other FlutterFlow builders. The community shares a lot of amazing ideas!

Creating a Forum Account

* When you select the [**Community**](https://app.flutterflow.io/community) tab, FlutterFlow automatically creates a forum account and redirects you to the Community Forum. To add a password to your forum account, go to the forum [**settings**](https://community.flutterflow.io/settings/account) and select **Forgot Password**.
* Additionally, make sure your FlutterFlow profile includes a name. The same name will be used for the community forum profile.

- **URL Access (Only Available for Enterprise Users)**: You can view and copy URLs that need to be whitelisted for FlutterFlow to function correctly in enterprise environments with restricted internet access. See **[Whitelisting URLs](https://docs.flutterflow.io/misc/enterprise#whitelist-urls)** for more information.

  ![url-access](https://docs.flutterflow.io/assets/images/url-access-dashboard-c7344917b601031042084edb5dee953c.avif)

- **Account**: This is helpful if you want to look at your account information, upload a profile picture, reset your password, see your referrals, or delete your account.

- **Log Out**: Safely log out from your FlutterFlow account.

---

### My Teams {#my-teams}

*On the My Teams page, you can manage billing for your team, edit projects simultaneously, and share code, design systems, APIs, and assets. This makes collaboration between team members much easier and helps keep everyone on the same page. Even if you don't have team members, you can still use this page to share resources between your own projects and keep your development process organized.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/my-teams

On the My Teams page, you can manage billing for your team, edit projects simultaneously, and share code, design systems, APIs, and assets. This makes collaboration between team members much easier and helps keep everyone on the same page. Even if you don't have team members, you can still use this page to share resources between your own projects and keep your development process organized.

By sharing resources from one place, teams can build more consistently across projects.

#### Team Code

> **Warning:** **Team Code Libraries are deprecated**. Please use the new [**Libraries**](https://docs.flutterflow.io/resources/projects/libraries) to share and reuse projects across multiple projects.

#### Team Media Assets

Your team might be working on multiple projects that use the same icons, images, audio files, and other graphic resources. If each project has its own assets, the team has to upload the same resources multiple times.

However, if the team shares an asset library across projects, they can save time, increase productivity, and ensure design consistency. If an asset needs to be updated, the team can update it in one place, and the changes will reflect across all projects.

To share team media assets:

1. Go to **My Teams**, select your team, and click **Upload Media**.
2. Media assets shared with the team appear in the Media Assets tab of the Navigation Menu. You can then select and use these assets directly from the asset picker in the Properties Panel.

* Upload shareable media assets
* Access media assets

![upload-sharable-media](https://docs.flutterflow.io/assets/images/upload-sharable-media-d19e33e5d75a5a69f1d89951e3f07eb1.avif)

![access-media-assets](https://docs.flutterflow.io/assets/images/access-media-assets-178639dcb9dffac3183119af2868a154.avif)

#### Team Design Library

A company may have a website, a mobile app, and a desktop app, each with its own user interface and user experience. Instead of recreating the same design settings for each project, you can create a shared design system to speed up the work and keep designs consistent across projects.

A design system includes colors, typography, fonts, icons, app assets, a Nav Bar, and an App Bar.

> **Tip:** To store pre-designed UI components, we recommend using [**Libraries**](https://docs.flutterflow.io/resources/projects/libraries) for easy reuse across projects.

Here's how you can share the design library:

1. Navigate to **My Teams > Team Design Library** and click **+ Create New**.
2. Enter a name for the **Design System Project**.
3. A new project will open where you can configure the Theme, [Nav Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#nav-bar), [App Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#appbar), and [App Assets](https://docs.flutterflow.io/resources/projects/settings/general-settings#app-assets).

[Create Team Design Library](https://demo.arcade.software/Dammx5Es92gc1hbdU31p?embed\&show_copy_link=true)

4. To use the shared design library, open the project where you want to use the design system and navigate to **Theme Settings** (navigation menu) **> Design System**.
5. Click **No Design System Selected**.
6. A popup opens displaying the list of shared design systems. Select one to add it to your project.

[Use Team Design Library](https://demo.arcade.software/lIKiqtfucQxC9HLLKNTS?embed\&show_copy_link=true)

#### Team API Library

> **Warning:** **Team API Libraries are deprecated**. Please use the new [**Libraries**](https://docs.flutterflow.io/resources/projects/libraries) to share and reuse projects across multiple projects.

#### Add Domains

You can add custom domains and share them with all team members. This makes it simple to connect domains to the right projects and collaborate seamlessly.

To add a domain, click **Add Domains** under **My Teams**.

![Add custom domain](https://docs.flutterflow.io/assets/images/add-custom-domain-81f55cb9f2c61724d3768dd789dac99b.avif)

---

### Resource Hierarchy Overview {#resource-hierarchy-overview}

*Explore the Resource Hierarchy Overview to understand the correlation between traditional Flutter app components and their equivalents in FlutterFlow.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/resource-hierarchy

This guide aims to help you understand the structure and elements of a typical FlutterFlow project. It will walk you through some important parts of the app, from the overall project down to individual design elements, explaining their purpose and how they relate to traditional Flutter app components.

#### FlutterFlow App Parts

The diagram below illustrates how a FlutterFlow app is structured.

![FlutterFlow app part.avif](https://docs.flutterflow.io/assets/images/ff-app-part-5d677a6580a1a528a2951299d2280d84.avif)

1. **Project**: Represents the overall application you are building in FlutterFlow. It encompasses all the other elements listed below and serves as the container for your entire app development effort within FlutterFlow. Learn more about creating a project [here](https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects#how-to-create-a-project).
2. **Page**: Refers to individual screens within the FlutterFlow project. Each page represents a part of the user interface where users can interact with the app. Multiple pages collectively make up the complete user interface of your application. Learn more about pages in FlutterFlow [here](https://docs.flutterflow.io/resources/ui/pages#creating-a-page).
3. **Built-in-widgets**: These are pre-designed widgets provided by FlutterFlow that you can use to build your app’s user interface. Built-in widgets simplify the development process by offering common UI elements such as buttons, text fields, sliders, etc.
4. **Component**: A component in FlutterFlow is a reusable UI block that can be used across different pages within the project. Components are useful for maintaining consistency and reducing redundancy in the app design, as the same component (like a custom dialog box) can be inserted wherever needed. Learn more about creating a component [here](https://docs.flutterflow.io/resources/ui/components).
5. **Design System**: This refers to a set of standards for design within your FlutterFlow project. A design system in FlutterFlow includes predefined styles that ensure visual consistency throughout the app. Learn more about design system [here](https://docs.flutterflow.io/concepts/design-system).

#### Flutter to FlutterFlow

If you are coming from Flutter, it is beneficial for you to understand the Flutter to FlutterFlow mapping. The diagram below illustrates the correlation between traditional Flutter app components and their equivalents within FlutterFlow.

![Flutter to FlutterFlow app parts](https://docs.flutterflow.io/assets/images/flutter-to-flutterflow-c4f7ad3c554b0e399fdd6456dc36c176.avif)

1. **MyApp to Project**: In Flutter, `MyApp` typically represents the root of your application, where you set up routes and other global configurations. In FlutterFlow, the equivalent is the "Project," which encompasses the entire application you are building, including its configurations and settings. Learn more about creating a project [here](https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects#how-to-create-a-project).
2. **MyPage to Page**: `MyPage` in Flutter represents a specific screen in the app. Similarly, In FlutterFlow, each "Page" corresponds to a screen, where you build the layout and functionality specific to that page of the project. Learn more about pages in FlutterFlow [here](https://docs.flutterflow.io/resources/ui/pages#creating-a-page).
3. **Column, Button, Text to Built-in widgets**: In FlutterFlow, widgets are categorized under "Built-in widgets," which users can drag and drop onto their canvas to build the UI. Learn more about widgets [here](https://docs.flutterflow.io/resources/ui/overview#widgets).
4. **Custom widget to Component**: `CustomWidget` in Flutter indicates user-defined widgets that serve specific functions not covered by built-in widgets. FlutterFlow translates this into "Component" allowing you to create and use custom components within your projects. Learn more about creating a component [here](https://docs.flutterflow.io/resources/ui/components).
5. **Theme/style constants to Design System**: In Flutter, theme and style constants are used to ensure consistent styling across an app. FlutterFlow uses a "Design System" to manage and apply uniform styles and themes throughout the application. Learn more about design system [here](https://docs.flutterflow.io/concepts/design-system).

#### Resource Description

A Resource Description is a brief text note that explains the purpose, usage, or key details of a particular resource. By supplying clear, concise descriptions, you create better project documentation and a smoother development experience—both for yourself and any collaborators.

> **Info:** Here are some reasons why resource descriptions can be helpful:

* **Team Collaboration**: When multiple developers or designers work on the same project, concise descriptions help everyone understand each element’s role without guesswork.
* **Better Search**: Descriptions are indexed in the FlutterFlow search. This helps locate pages, components, and other resources quickly, especially in large projects.
* **Project Documentation**: Acts as built-in documentation of your app, which makes future updates easier.

You can add a description for each of the following resources in FlutterFlow:

* **Project**: Use the project-level description to summarize the overall goals or scope of your app. For instance, "A delivery management app for small businesses" helps keep the team aligned on the primary objective.
* **Page**: Explains a page’s main function. Example: "Displays the user’s shopping cart and checkout options."
* **Component**: Clarifies the functionality or design intention of a reusable component. Example: "Reusable card component to be used as ListTile."
* **Action Blocks**: Provide a concise description of what the set of actions does (e.g., "Sends a notification to the user’s email address upon form submission").
* **Custom Functions**: Describe the logic or purpose behind the function. Example: "Calculates shipping costs based on weight and distance."
* **Custom Actions**: Specify the custom behavior you’ve created, such as "Opens a QR scanner and returns the scanned value."
* **Custom Widgets**: Explain the widget’s purpose or structure. Example: "Carousel widget for displaying multiple images with pagination."
* **Data Type**: Summarizes the purpose of a custom data model. Example: "Represents a user’s order including items, total cost, and status."
* **Parameters**: Provide context for how a parameter is used, including expected data types or value ranges. Example: "String to store the user’s phone number—must include country code."
* **Page/Component State Variables**: Clarify what state data is being stored and why. For instance, "Tracks the currently selected tab in this component."
* **App State Variables**: Describe the global data shared across pages. Example: "Stores the user’s authentication token for all network requests".
* **Constant**: Add the intended purpose of any fixed value used throughout the app. Example: "Base API URL for all network calls".
* **Enum**: Provide a rationale for the enumerated values. Example: "Defines possible user roles—admin, editor, viewer".
* **Firestore Collection**: Explain what data the collection holds and how it relates to your app’s functionality. Example: "Stores all user profiles with fields for name, email, and profile photo URL".

In FlutterFlow, you can read descriptions as tooltips when hovering over the green note icon.

> **Tip:** In the generated code, FlutterFlow inserts descriptions as docstring-like comments near the relevant classes, methods, or properties. For instance, a data type named `OrderInfo` with a description of “Represents a user’s order, including items, total cost, and status” will have that text added above the class declaration:

```
/// Represents a user’s order, including items, total cost, and status.
class OrderInfo {
/// The total price in USD for this order.
double totalAmount;
List<String> items;
// ...
}
```

In a standard IDE (e.g., VS Code or Android Studio), if you place your mouse over a custom data type class name, the description set in FlutterFlow appears as a tooltip, helping you quickly grasp the purpose of a resource.

![resource-description.avif](https://docs.flutterflow.io/assets/images/resource-description-870afc6b99db9b5637c1beadba3677e5.avif)

---

### Storyboard {#storyboard}

*Master the Storyboard view in FlutterFlow to visualize your app’s design and user navigation. The Storyboard allows you to see screens and interactions, ensuring a seamless user experience.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/storyboard

The Storyboard view allows you to visualize the overall design and navigation of your app. On Storyboard, you can see different screens and user interactions that make up your app. This allows you to see how users will navigate through your app and ensure that the user experience is as intuitive and user-friendly as possible.

> **Info:** This feature is currently in Beta. It is optimized for projects with 30 pages or less.

![storyboard.avif](https://docs.flutterflow.io/assets/images/storyboard-9f1b0d822bd94f58e43e928cedc4279a.avif)

#### Storyboard legend

In a storyboard, a legend is a visual key or guide that explains the meaning of the different lines, icons, and colors used inside the canvas.

We use the following elements inside the storyboard:

![storyboard-legend.avif](https://docs.flutterflow.io/assets/images/storyboard-legend-d18cbc2e4f0067bf3ae2e13505ea5687.avif)

1. The solid line is used to represent the [Navigate](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) or Login action.
2. The dotted line is used to represent the Bottom Sheet action.
3. The right arrow icon represents hidden widgets. These widgets may not be visible in the current page view (e.g., they might be on another tab) but they still have a navigation action to display them.

#### Highlight routes on a page

With so many pages displayed on a Storyboard, it may be difficult to identify the route path from a specific page, especially when lines overlap each other. To highlight the pathways leading into and out of a specific page, just click on a page, and the routes will be highlighted in blue color.

![highlight-routes.avif](https://docs.flutterflow.io/assets/images/highlight-routes-0bcb55b5f6e3997421746074e0d61188.avif)

#### Move pages

You might want to adjust the default arrangements of pages on canvas and group the pages that belong to the same feature. To do so, select the page and drag it to the desired place.

#### Open a page from Storyboard

You can also open a page directly from a Storyboard. To do so, simply double-click on a page.

***

#### Video guide

Watch this video if you prefer watching a video tutorial.

[Navigating Pages & Storyboard | FlutterFlow University](https://www.youtube.com/embed/ukBii81pwm4)

***

#### FAQs

I am getting "Error: Unable to initialize Storyboard"

This error typically occurs because the initial page has not been set. To resolve this, please set the initial page in the [App Details](https://docs.flutterflow.io/resources/projects/settings/general-settings#app-details) settings of your project.

---

### Toolbar {#toolbar}

*Learn how to use the FlutterFlow Toolbar to access project management, version control, help, testing, and development tools.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/toolbar

The Toolbar, located at the top of the app builder, provides easy access to numerous tools and features. It includes options for project configuration, saving versions of your app, accessing help, reporting or debugging issues, viewing project comments, downloading your app code, and running your app directly in FlutterFlow.

![toolbar](https://docs.flutterflow.io/assets/images/toolbar-49ea1755ae529a6d00c1ac698ec45cd7.avif)

#### Project Info

Click on the project info to view the project name, branch, environment, FlutterFlow version and release date, and the Flutter version used by the project.

#### Help Menu

From here, you can access essential resource links that can help you while building your app.

1. **Search Docs**: Paid users can search the FlutterFlow documentation directly from the builder.
2. **Community Forum**: Visit the [Community Forum](https://community.flutterflow.io/) to participate in discussions, share knowledge, and collaborate with other FlutterFlow users.
3. **Feedback**: You can provide feedback and help us improve the product.
4. **Bug Report**: You can submit a bug report from here.
5. **Generate Bug Report Code**: Click this option to generate a unique code that helps the FlutterFlow team assess and troubleshoot your issue. Include this code when submitting a bug report.
6. **Tutorials**: You can start the tutorial for building your first app directly in FlutterFlow.
7. **FAQs and Docs**: While building your app, you might need to consult our official documentation frequently. This option opens the FlutterFlow documentation.
8. **What's New?**: View the latest FlutterFlow features, improvements, and product updates.
9. **Current Status/Known Issues**: View FlutterFlow's current system status and any known issues.
10. **Show/Hide Chat**: You can use this option to show or hide the chat button at the bottom right of the app builder.

#### Keyboard Shortcuts

With keyboard shortcuts, you can perform common actions related to widgets and run your project in Test Mode or Run Mode with just a few keystrokes, saving you time and effort. Select this option to see all the shortcuts.

![keyboard-shortcuts.avif](https://docs.flutterflow.io/assets/images/keyboard-shortcuts-44a1ba8b277b35d1a7164217833fbfc9.avif)

#### Command Palette

Open the Command Palette by selecting the search button or pressing **Cmd/Ctrl + K**. Search for an item, then select the right arrow to see where it is used. Select a result to open it directly.

![command-palette.avif](https://docs.flutterflow.io/assets/images/command-palette-e3cd96697f631d56997e0646a0950a4c.avif)

#### AI Generation History

The **AI Generation History** panel lets you track the status of your AI-generated items. It provides a list of all previously generated pages and components, and you can easily preview them in the panel.

#### Project Comments

Project Comments let you leave thoughts, questions, or feedback on a specific widget for your project team or client. While adding a comment, you can tag users, and they will be able to respond, creating a thread of conversation.

> **Info:** To tag users, select the **@** symbol and choose the project team member(s).

#### Project Suggestions

Project Suggestions identifies opportunities to improve your app's design and performance.

**Optimizations**: This identifies elements that may slow down your app, such as queries on columns, unused or duplicate backend queries, and widgets with unbounded sizes.

**UI Enhancements**: This provides tips for creating a more visually appealing and user-friendly design, such as increasing the size of a widget's tap target.

> **Info:** You can control which types of suggestions you receive by selecting the settings icon on the right.

![optimizations-UI-enhancements.avif](https://docs.flutterflow.io/assets/images/optimizations-UI-enhancements-c22c98b3aedf1373eac8dff13f47df86.avif)

#### Project Issues

This section displays errors and warnings that may cause build failures or app crashes. Select an issue to view its description and navigate to the relevant location in your project.

Errors vs Warnings

**Errors** prevent your app from compiling and running. These must be resolved in order to run the app. They can be due to missing actions, errors in custom code, incorrect data types, and so on.

**Warnings**, while not preventing compilation, indicate potential issues such as incorrect rule configuration or performance problems. Although it's possible to ignore warnings, addressing them can enhance the quality of your app and prevent future issues.

![warnings-errors.avif](https://docs.flutterflow.io/assets/images/warnings-errors-4f6ae376c05b81d4a4a413c2e9f9ddbc.avif)

#### Version Control

**Version Control** is a system that tracks changes to your project's files over time, allowing you to revert to previous states if needed. In FlutterFlow, you can use [Branching](https://docs.flutterflow.io/collaboration/branching) to create a separate copy of your project to build or test features without affecting the main version.

#### Developer Menu

The Developer Menu provides access to tools such as code viewing, GitHub integration, and source code download capabilities.

1. **View Code**: This option lets you view the *Dart* code for all the pages of your FlutterFlow project. You can also view the dependencies used by the app here.

2. **Connect GitHub Repo**: You can use this option to connect your project to a [GitHub](https://github.com/) repository and upload its code. See [Connect a GitHub Repository](https://docs.flutterflow.io/exporting/push-to-github#connect-a-github-repo) for step-by-step instructions.

3. **Download Code**: You can download the entire codebase of the app generated by FlutterFlow using this option.

4. **Download APK**: Use this to generate a release build of your Android app. It will automatically download the `.apk` file after the build is complete.

5. **FlutterFlow CLI**: You can also download the code using *[FlutterFlow CLI](https://pub.dev/packages/flutterflow_cli)*. See instructions [here](https://docs.flutterflow.io/flutterflow-cli/exporting).

> **Note:** *Connect GitHub Repo*, *Download Code*, and *Download APK* features require a [**paid plan**](https://flutterflow.io/pricing).

6. **Open in VSCode**: This option lets you open your entire FlutterFlow project in a VS Code environment, offering a richer development experience. You’ll have real-time autocomplete and error detection, easier access to existing Flutter and Dart tooling, and the ability to leverage the AI ecosystem.

7. **Refactor Project**: This option opens your FlutterFlow project in a YAML-based file editor, allowing you to perform bulk edits more efficiently. You can search, edit, and replace values across multiple files—useful for renaming keys, updating data types, or migrating resources to a Library. Check out the [**Refactor Project**](https://docs.flutterflow.io/resources/projects/refactor-project) documentation for more details.

#### Share Project

You can make a project public so that others can view and clone your project. Before sharing your project, make sure to remove any sensitive information.

> **Note:** * You can only share projects where you are the owner.
* The share feature can be used to create Marketplace items. See [**FlutterFlow Marketplace**](https://docs.flutterflow.io/marketplace) for more information.

#### Preview App

You can use this option to run your app in [Preview mode](https://docs.flutterflow.io/testing/run-your-app#preview-mode).

#### Test Mode

Use this menu to run your app in [Test Mode](https://docs.flutterflow.io/testing/run-your-app#test-mode) or [Run Mode](https://docs.flutterflow.io/testing/run-your-app#run-mode).

---

### Widget Palette {#widget-palette}

*Explore the Widget Palette in FlutterFlow to access a wide range of UI elements. This feature offers an intuitive interface for dragging and dropping Flutter widgets onto your canvas.*

**Source:** https://docs.flutterflow.io/flutterflow-ui/widget-palette

The Widget Palette in FlutterFlow provides access to all UI elements. These are essentially FlutterFlow widgets that can be dragged and dropped onto the canvas. You can use the search bar to quickly locate a specific widget for your application.

![widget-palette.avif](https://docs.flutterflow.io/assets/images/widget-palette-1f9d01356928e265066e46fa3bd4e443.avif)

#### 1. Widgets

From the Widgets tab, you can access all standard FlutterFlow widgets. They are organized into different categories based on their purpose, making it easier to navigate and find the appropriate widget for your app.

#### 2. Components

Components are widgets with certain functionalities that can be reused throughout your app. They are constructed from either standard or custom widgets. Once you have created a [component](https://docs.flutterflow.io/resources/ui/components/creating-components) or [custom widget](https://docs.flutterflow.io/concepts/custom-code/custom-widgets), you can access it from here.

#### 3. Templates

Templates are predefined and ready-to-use widgets. These include UI elements that are commonly used in most apps and can serve as a starting point in creating parts of the user interface. You can also create your own templates from the standard widget.

#### 4. Theme Widgets

Theme Widgets enable you to customize the visual appearance of individual widgets and reuse them consistently throughout your app. They are an integral part of the design system, allowing you to build widgets based on your theme. Once you [create a theme widget](https://docs.flutterflow.io/concepts/design-system#theme-widgets), you can access it from here.

#### 5. Floating Widget Palette

The Floating Widget Palette gives you quick access to widgets directly from the canvas. This feature is useful for swiftly adding widgets without the need to open the Widget Palette via the navigation menu.

![Floating Widget Palette](https://docs.flutterflow.io/assets/images/floating-widget-palette-907809164f7c6c702ed4986cff32b266.gif)

---

---

## Generated Code Reference

### Generated Code: Components {#generated-code-components}

*Similar to a Page, when creating a component in FlutterFlow, it automatically generates two files: a Widget class and a Model class.*

**Source:** https://docs.flutterflow.io/generated-code/component-model

Similar to a [**Page**](https://docs.flutterflow.io/generated-code/page-model), when creating a **[component](https://docs.flutterflow.io/resources/ui/components)** in FlutterFlow, it automatically generates two files: a `Widget` class and a `Model` class.

Prerequisites

This guide uses examples from the generated code of the **[EcommerceFlow demo app](https://bit.ly/ff-docs-demo-v2)**. To view the generated code directly, check out the **[Github repository](https://github.com/FlutterFlow/sample-apps/tree/main/ecommerce_flow)**.

#### ComponentModel class

`ComponentModel` classes are responsible for managing the state and behavior of individual components used within a page. These classes extend the `FlutterFlowModel` class, providing a consistent structure and shared functionality across all component models. This ensures that each component's state is isolated and reusable, making the app easier to maintain and scale.

The lifecycle of a `ComponentModel` and its associated widget class follows the same structure as a page. For more details, refer to the documentation on **[Generated Pages](https://docs.flutterflow.io/generated-code/page-model)**.

##### onComponentLoad Action: Generated Code

When you define actions for the `onComponentLoad` action trigger of a component, these actions are added inside an `addPostFrameCallback` method within the page's `initState` method. This ensures that the actions are executed only after the initial widget tree is built.

```
 @override
  void initState() {
    super.initState();
    _model = createModel(context, () => ProductListPageModel());

    // On component load action.
    SchedulerBinding.instance.addPostFrameCallback((_) async {
        await _model.updateTotalCost(context);
        safeSetState(() {});
    });
    
  }
```

---

### DataTypeStruct class {#datatypestruct-class}

*This guide uses example of the generated code of the EcommerceFlow demo app. To view the generated code directly, check out the Github repository.*

**Source:** https://docs.flutterflow.io/generated-code/custom-data-types

Prerequisites

This guide uses example of the generated code of the **[EcommerceFlow demo app](https://bit.ly/ff-docs-demo-v2)**. To view the generated code directly, check out the **[Github repository](https://github.com/FlutterFlow/sample-apps/tree/main/ecommerce_flow)**.

When you create a custom data type in the FlutterFlow editor, a corresponding class is generated in the code to act as a structured container for your data, similar to a `Struct`. This class includes simple getters and setters for each field. For example, if your data type in FlutterFlow is named "Product", the generated class will be named `ProductStruct` and can be found in the `product_struct.dart` file.

![custom-data-type-gen-class.png](https://docs.flutterflow.io/assets/images/custom-data-type-gen-class-dada69e3fce9f4e9adb7fbba271143b9.png)

---

### FFAppState {#ffappstate}

*This guide uses example of the generated code of the EcommerceFlow demo app. To view the generated code directly, check out the Github repository.*

**Source:** https://docs.flutterflow.io/generated-code/ff-app-state

Prerequisites

This guide uses example of the generated code of the **[EcommerceFlow demo app](https://bit.ly/ff-docs-demo-v2)**. To view the generated code directly, check out the **[Github repository](https://github.com/FlutterFlow/sample-apps/tree/main/ecommerce_flow)**.

The `FFAppState` class in FlutterFlow acts as a central hub for managing the application's global state. It's designed as a singleton, meaning there's only one instance of this class throughout the app's lifecycle. This class extends [**ChangeNotifier**](https://api.flutter.dev/flutter/foundation/ChangeNotifier-class.html), allowing widgets to listen and react to state changes.

It includes methods for initializing and updating the app's persisted state and also defines various state variables with corresponding **getters and setters** for manipulating these values.

Here is a basic template of the class, taken from the [**eCommerceFlow demo app**](https://bit.ly/ff-docs-demo-v2)'s generated code:

```
class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  // App State variable of primitive type with a getter and setter
  bool _enableDarkMode = false;

  bool get enableDarkMode => _enableDarkMode;

  set enableDarkMode(bool value) {
    _enableDarkMode = value;
  }
}
```

The `_enableDarkMode` is an App State variable created by developer that creates its own corresponding getter and setter.

#### Rebuild on Updating AppState

When updating an `AppState` variable from the Action Flow Editor, you will be presented with several **[update type](https://docs.flutterflow.io/resources/data-representation/app-state#update-type)** options such as **Rebuild All Pages**, **Rebuild Current Page**, and **No Rebuild** in the Action Settings. Let's see how the generated code changes when these options are selected.

##### Rebuild Current Page

When a developer chooses to update App State with the update type set to **Rebuild Current Page**, the corresponding `setter` is called. Immediately after, `setState(() {});` is invoked, which updates only the current page.

Here's an example of the generated code when we update the App State `enableDarkMode` in the `onInitialization` action trigger of the `ProductListPage`.

```
SchedulerBinding.instance.addPostFrameCallback((_) async {
  FFAppState().enableDarkMode = !(FFAppState().enableDarkMode ?? true);
  setState(() {});
});
```

##### Rebuild All Pages

In this case, the update type is set to **Rebuild All Pages**, meaning that the `setter` is called, followed by the `update()` method. This method internally calls `notifyListeners()`, which is crucial for updating any widgets that depend on this variable.

```
SchedulerBinding.instance.addPostFrameCallback((_) async {
  FFAppState().enableDarkMode = !(FFAppState().enableDarkMode ?? true);
  FFAppState().update(() {});
});
```

Updating App State from Custom Code

When updating App State variables from custom code, such as Custom Actions, it's crucial to call the update function to ensure that the changes are reflected across all pages. For example, you should use:

```
FFAppState().update(() => FFAppState().enableDarkMode = !(FFAppState().enableDarkMode ?? true));
```

##### No Rebuild

Only the setter is called with no setState or update method invoked afterward. This means that only the variable is updated, with no state changes occurring after the data update.

#### watch\<FFAppState>

When you add an [**Update App State**](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action) action via the Action Flow Editor, the corresponding pages will include this line within the build method:

```
@override
Widget build(BuildContext context) {
    context.watch<FFAppState>();
    ...
```

By using `context.watch<FFAppState>()`, the widget effectively subscribes to any changes in the `FFAppState` class. Whenever there's a change in the `FFAppState` object, this widget automatically rebuilds to reflect those changes. This ensures that your widget always displays the most current data and state of the app, maintaining an up-to-date and responsive user interface.

#### Managing AppState\<List>

When you add an App State variable of `List` type in FlutterFlow, several utility functions are automatically generated to help you manage this list. These functions include a getter, a setter, and methods for adding, removing, and updating items in the list. This setup ensures that you can easily interact with the list while keeping the app state consistent and responsive. Below is an explanation of these generated functions using the specific example of a LatLngList.

```

late LoggableList<LatLng> _LatLngList =
    LoggableList([LatLng(37.4071594, -122.0775312), LatLng(40.7358633, -73.9910835)]);

List<LatLng> get LatLngList => _LatLngList?..logger = () => debugLogAppState(this);

set LatLngList(List<LatLng> value) {
    if (value != null) {
        _LatLngList = LoggableList(value);
    }

    debugLogAppState(this);
}

void addToLatLngList(LatLng value) {
    LatLngList.add(value);
}

void removeFromLatLngList(LatLng value) {
    LatLngList.remove(value);
}

void removeAtIndexFromLatLngList(int index) {
    LatLngList.removeAt(index);
}

void updateLatLngListAtIndex(
    int index,
    LatLng Function(LatLng) updateFn,
) {
    LatLngList[index] = updateFn(_LatLngList[index]);
}

void insertAtIndexInLatLngList(int index, LatLng value) {
    LatLngList.insert(index, value);
}
```

These functions are automatically generated to provide a convenient and consistent way to manage list-type App State variables, making it easier to maintain the app's state:

* The list `LatLngList` is initialized as a private variable `_LatLngList` of type `LoggableList`, which helps in managing the list with additional logging capabilities.
* The get `LatLngList` method allows other parts of the app to access the `LatLngList`.
* The set `LatLngList` method allows you to replace the entire `LatLngList` with a new one. When a new list is assigned, it updates the private variable `_LatLngList` and logs this change using `debugLogAppState`.
* The `addToLatLngList` function appends a new `LatLng` object to the LatLngList, dynamically updating the list as the app runs.
* The `removeFromLatLngList` function removes a specific `LatLng` object from the `LatLngList`, ensuring the list remains accurate and up-to-date.
* The `removeAtIndexFromLatLngList` function removes a `LatLng` object from the list based on its index position.
* The `updateLatLngListAtIndex` function allows you to update a `LatLng` object at a specific index by applying an update function (`updateFn`) to it.
* The `insertAtIndexInLatLngList` function inserts a new `LatLng` object into the `LatLngList` at a specific index, shifting the existing items as necessary.

How to create App State variables

To learn more about creating and using App State variables in FlutterFlow's UI, check out the[ **App State**](https://docs.flutterflow.io/resources/data-representation/app-state) guide.

---

### FlutterFlow Model {#flutterflow-model}

*The FlutterFlowModel class is an abstract class used in FlutterFlow to provide a unified and extensible structure for managing state and behavior of widgets (both pages and components). It encapsulates initialization, state management, and disposal logic, making it easier to handle the lifecycle of widgets and their models.*

**Source:** https://docs.flutterflow.io/generated-code/flutterflow-model

The `FlutterFlowModel` class is an abstract class used in FlutterFlow to provide a unified and extensible structure for managing state and behavior of widgets (both pages and components). It encapsulates **initialization, state management,** and **disposal** logic, making it easier to handle the lifecycle of widgets and their models.

FlutterFlow automatically generates the `flutter_flow_model.dart` file, which contains the `FlutterFlowModel` class and utility methods like `wrapWithModel()` and `createModel()`.

The diagram below illustrates how these utility classes and methods are utilized in a widget or model class:

![page-generated.png](https://docs.flutterflow.io/assets/images/page-generated-8c049279aadda77f6233554cca01deb8.png)

When a component is added to your page (and every component you create [generates both a widget and a model class)](https://docs.flutterflow.io/generated-code/component-model), the flow below explains how the utility classes are used when there is a child component:

![page-component-generated.png](https://docs.flutterflow.io/assets/images/page-component-generated-f0a0aec0e4590657a5c9589fddf00b2f.png)

Here’s a breakdown of the lifecycle of `FlutterFlowModel` class:

#### Initialization

Ensures the model is initialized **only once** and is tied to the `BuildContext` and the widget it is associated with.

```
abstract class FlutterFlowModel<W extends Widget> {
  // Initialization methods
  bool _isInitialized = false;
  void initState(BuildContext context);
  void _init(BuildContext context) {
    if (!_isInitialized) {
      initState(context);
      _isInitialized = true;
    }
    if (context.widget is W) _widget = context.widget as W;
    _context = context;
  }
```

#### Widget & Context references

Provides references to the associated widget and its `BuildContext`.

```
  // The widget associated with this model. This is useful for accessing the
  // parameters of the widget, for example.
  W? _widget;
  W? get widget => _widget;

  // The context associated with this model.
  BuildContext? _context;
  BuildContext? get context => _context;
```

`_widget` and `_context` (private fields) store the widget and context references. `widget` and `context` (getters) are the public accessors for `_widget` and `_context`.

#### Disposal

Manages the cleanup of resources when the model or widget is disposed.

```
 bool disposeOnWidgetDisposal = true;
  void dispose();
  void maybeDispose() {
    if (disposeOnWidgetDisposal) {
      dispose();
    }
    // Remove reference to widget for garbage collection purposes.
    _widget = null;
  }
```

The `disposeOnWidgetDisposal` determines whether the model should be disposed when the widget is removed. This defaults to `true` for **pages** and `false` for **components** (as parent models typically manage their child components).

The `maybeDispose()` checks `disposeOnWidgetDisposal` before disposing. It removes the widget reference to aid garbage collection.

#### Updates and Change Notification

Allows the model to notify the associated widget or parent component/page when updates occur.

```
 // Whether to update the containing page / component on updates.
  bool updateOnChange = false;
  // Function to call when the model receives an update.
  VoidCallback _updateCallback = () {};
  void onUpdate() => updateOnChange ? _updateCallback() : () {};
  
  FlutterFlowModel setOnUpdate({
    bool updateOnChange = false,
    required VoidCallback onUpdate,
  }) =>
      this
        .._updateCallback = onUpdate
        ..updateOnChange = updateOnChange;
  
  // Update the containing page when this model received an update.
  void updatePage(VoidCallback callback) {
    callback();
    _updateCallback();
  }
```

#### wrapWithModel()

The `wrapWithModel()` method in FlutterFlow links a model to a widget and its child widgets, allowing them to access and manage state. It wraps the widget with a Provider, making the model available throughout the widget tree.

---

### Generated Code: Pages {#generated-code-pages}

*When you create a new Page in FlutterFlow, it automatically generates two files: a Widget class and a Model class. So if the name of the page you created is called ProductListPage, FlutterFlow generation backend will automatically create ProductListPageWidget class and ProductListPageModel class.*

**Source:** https://docs.flutterflow.io/generated-code/page-model

When you create a new Page in FlutterFlow, it automatically generates two files: a `Widget` class and a `Model` class. So if the name of the page you created is called **ProductListPage**, FlutterFlow generation backend will automatically create **ProductListPageWidget** class and **ProductListPageModel** class.

Prerequisites

This guide uses examples from the generated code of the **[EcommerceFlow demo app](https://bit.ly/ff-docs-demo-v2)**. To view the generated code directly, check out the **[Github repository](https://github.com/FlutterFlow/sample-apps/tree/main/ecommerce_flow)**.

#### PageModel class

The `PageModel` classes are responsible for managing the state of individual pages and initializing the components used in these Pages. These classes extend the `FlutterFlowModel` class, which provides a consistent structure and shared functionality across all page models.

The following diagram shows how FlutterFlow generates the model and widget class when you create a new Page in FlutterFlow: ![page-generation-initial.png](https://docs.flutterflow.io/assets/images/page-generation-initial-e7846168b8b4019ead1e2ca9dc71ab64.png)

FlutterFlow Model

To learn more about the utility classes and methods that FlutterFlow generates for all pages & components, see [**the FlutterFlowModel document**](https://docs.flutterflow.io/generated-code/flutterflow-model).

###### Managing Local State

A `PageModel` class typically holds local state fields specific to the page, which correspond to the **[Page State variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state)**.

For example, in the ProductListPage, user may create a Page State variable called `searchString`. Correspondingly, in the `product_list_page_model.dart` [file](https://github.com/FlutterFlow/sample-apps/blob/main/ecommerce_flow/lib/product/product_list_page/product_list_page_model.dart) (which is the `Model` file for the `ProductListPage`), the corresponding state field would be `_searchString`. This private field stores the current search string and includes a getter and setter to manage its value while logging any changes.

```
String? _searchString;
set searchString(String? value) {
  _searchString = value;
  debugLogWidgetClass(rootModel);
}
String? get searchString => _searchString;
```

Private variables in Dart

In Dart, variables that start with an underscore (`_`), such as `_searchString`, are private to the class. This means they cannot be accessed outside the class or its scope.

In addition to managing local state, the given `PageModel` class also contains fields for handling the state of widgets on the page. For instance, `_dropDownValue` is a private field that stores the current value of a dropdown widget (if it is added to the current Page). Similar to `_searchString`, it has a getter and setter that logs changes to this field.

```
String? _dropDownValue;
set dropDownValue(String? value) {
  _dropDownValue = value;
  debugLogWidgetClass(rootModel);
}
String? get dropDownValue => _dropDownValue;
```

###### Initializing child component models

The `PageModel` class is also responsible for initializing the models of components used on the page. For example, if the page includes a `CartCounter` component, the model for this component is initialized within the page's model class.

```
// Model for CartCounter component.
  late CartCounterModel cartCounterModel;

@override
void initState(BuildContext context) {
    cartCounterModel = createModel(context, () => CartCounterModel()..parentModel = this);
    
}
```

> **Info:** Only the model class of a child component is initialized inside the page or parent model class. In the case of page model classes, they are initialized within the widget’s state class itself. See the **[Widget class section](https://docs.flutterflow.io/generated-code/page-model#pagewidget-class)** for more details.

When dealing with dynamic lists of components, such as those in a `ListView`, Row, or Column widget, the `PageModel` initializes a `Map<String, FlutterFlowModel>` to manage the state of each component instance. For example, if the page includes a list of `CategoryAvatar` components, the initialization might look like this:

```
// Models for CategoryAvatar dynamic component.
  Map<String, FlutterFlowModel> categoryAvatarModels = {};
```

###### dispose()

Finally, the `dispose` function in the `ProductListPageModel` class is used to clean up resources when they are no longer needed. This is a common practice in Flutter to prevent memory leaks. In this class, the `dispose` function is overridden to dispose of the `cartCounterModel`, `searchQueryFocusNode`, and `searchQueryTextController`.

```

  @override
  void dispose() {
    cartCounterModel.dispose();
    searchQueryFocusNode?.dispose();
    searchQueryTextController?.dispose();
  }
```

#### PageWidget class

The `PageWidget` classes are responsible for creating the UI of individual pages and holding the widget tree as designed in the FlutterFlow canvas. These classes always extend Flutter's `StatefulWidget` class utilizing Flutter's built-in state management through `setState` to handle dynamic updates and interact with the app's lifecycle.

```
class ProductListPageWidget extends StatefulWidget {
    const ProductListPageWidget({super.key});

    @override
    State<ProductListPageWidget> createState() => _ProductListPageWidgetState();
}
```

###### PageModel Initialization

Within the State class, the `PageModel` object is initialized. [This class](https://docs.flutterflow.io/generated-code/page-model#pagemodel-class) serves as a centralized place to manage the page’s state, handle business logic, and interact with the data layer.

```
class _ProductListPageWidgetState extends State<ProductListPageWidget> {
    late ProductListPageModel _model;

    @override
    void initState() {
        super.initState();
        _model = createModel(context, () => ProductDetailPageModel());

    }
```

###### PageModel Dispose

Similarly, the [`dispose` method](https://docs.flutterflow.io/generated-code/page-model#dispose) of the `PageModel` class is invoked from the **overridden** `dispose` method of the widget's **State** class. This ensures that any resources managed by the `PageModel`, such as listeners or controllers, are properly released when the widget is removed from the widget tree.

```
  @override
  void dispose() {
    _model.dispose();
    super.dispose();
  }
```

###### Global Scaffold Key

Each page includes a `GlobalKey` for the `Scaffold`, which can be used to manage the scaffold's state, such as opening or closing drawers or snackbars programmatically.

```
final scaffoldKey = GlobalKey<ScaffoldState>();

return Scaffold(
    key: scaffoldKey,
    ...)
```

###### Keyboard Dismissal

Moreover, the root widget of every page is a `GestureDetector` with an `onTap` callback that unfocuses the current input field. This approach ensures that tapping anywhere outside an input field dismisses the keyboard or removes focus, creating a better user experience.

```
return GestureDetector(
    onTap: () {
    FocusScope.of(context).unfocus();
    FocusManager.instance.primaryFocus?.unfocus();
    },
...)
```

These functionalities are automatically added by FlutterFlow to ensure seamless navigation and proper keyboard handling across pages.

##### onPageLoad Action: Generated Code

When you define actions for the `onPageLoad` action trigger of a Page, these actions are added inside an `addPostFrameCallback` method within the page's `initState` method. This ensures that the **on Page Load** actions are executed after the widget is fully built and rendered. This avoids issues caused by trying to update the UI before it is ready.

```
 @override
  void initState() {
    super.initState();
    _model = createModel(context, () => ProductListPageModel());

    // On page load action.
    SchedulerBinding.instance.addPostFrameCallback((_) async {
      _model.searchString = null;
      safeSetState(() {});
      ... // more actions
    });
    
  }
```

safe Set State

The `safeSetState` method is a custom implementation built on top of Flutter's `setState` method. It ensures that `setState` is only called when the widget is currently mounted, preventing potential runtime errors.

---

### Directory Structure {#directory-structure}

*This guide uses example of the generated code of the EcommerceFlow demo app. To view the generated code directly, check out the Github repository.*

**Source:** https://docs.flutterflow.io/generated-code/project-structure

Prerequisites

This guide uses example of the generated code of the **[EcommerceFlow demo app](https://bit.ly/ff-docs-demo-v2)**. To view the generated code directly, check out the **[Github repository](https://github.com/FlutterFlow/sample-apps/tree/main/ecommerce_flow)**.

When you download the code generated by FlutterFlow, you'll notice many additional files and folders beyond what you see in FlutterFlow's Code Viewer. These files make up the complete project structure, organized according to a specific architecture. Understanding this structure is like having a detailed map, guiding you through the code and making it easier to navigate and customize your FlutterFlow project later. So, let's dive in and explore this directory structure.

#### Folder Structure

```
assets/
lib/
- actions/actions.dart
- auth/
    - firebase_auth/
    - auth_manager.dart
    - base_auth_user_provider.dart
- backend/
    - api_requests/
        - api_calls.dart
        - api_manager.dart
        - get_streamed_response.dart
    - cloud_functions/
    - firebase/
    - firebase_dynamic_links/firebase_dynamic_links.dart
    - supabase/
    - schema/
        - enums/enums.dart
        - structs/
            - address_struct.dart
            - cart_struct.dart
            - ...
        - util/
            - firestore_util.dart
            - schema_util.dart
        - carts_record.dart 
        - ...
        - index.dart
    - backend.dart
- pages/ ---// empty in this project
- cart/
    - cart_counter/
        - cart_counter_model.dart
        - cart_counter_widget.dart
    ...
- components/
    - square_leading_model.dart
    - square_leading_widget.dart
    - styled_button_model.dart
    - styled_button_widget.dart
- custom_code/
    - actions/
        - execute_search.dart
        ...
- flutter_flow/  ---//FF generated files
    - custom_functions.dart
    - flutter_flow_animations.dart
    - flutter_flow_....dart
    - nav/
- app_constants.dart
- app_state.dart
- index.dart
- main.dart
pubspec.yaml
```

##### Pages & Components

FlutterFlow follows a layer-first approach to keep your app organized as it grows. Authentication and backend methods are neatly organized into their own sections **[auth](https://docs.flutterflow.io/generated-code/project-structure#auth)** and **[backend](https://docs.flutterflow.io/generated-code/project-structure#backend)**. Each page you create in FlutterFlow will generate its own folder, containing the `widget` file and the corresponding `model` file. Shared components are placed in subfolders under `components/`.

If you've created nested folders in the FlutterFlow UI, these will directly translate into corresponding folders in the exported code. This gives you even more control to group and organize different features as you like. For instance, you could have separate folders for `products`, `user profile`, and `orders`. In the example above, `cart` is a folder explicitly created to hold all cart related pages and components.

##### assets/

The `assets/` directory is where you store static files that your app uses, such as images, fonts, and other resources. These files can be accessed in your code through asset paths and are bundled with your app when it's built.

##### lib/

The `lib/` directory contains all the Dart code that drives your Flutter app. This is where the main structure of your application resides. It's organized into several subdirectories to keep the codebase clean and manageable:

##### actions/

The actions folder contains app-level **Action Blocks**. Each Action Block is created as a separate function within this directory. For example, in the case of eCommerce demo app, the `addToWishlist` function is an app-level Action Block that is included in the `actions.dart` file.

```
Future addToWishlist(
    BuildContext context, {
        required String? productId}) async {
    // Add productId to wishlist object
    FFAppState().addToLocalWishlist(productId!);
    FFAppState().update(() {});
}
```

##### auth/

Contains files and folders related to authentication logic, including integrations with Firebase or other authentication services.

##### backend/

The `backend/` directory is responsible for handling all the backend logic and integrations for your Flutter app. This includes API requests, cloud functions, database interactions, and managing data schemas. Each subdirectory within backend/ serves a specific purpose:

* **api\_requests/**: The api\_requests/ directory handles all communication between your app and external services via APIs. It centralizes and organizes the code for making and managing HTTP requests and responses.

* **cloud\_functions/**: This directory is used to store functions that interact with cloud-based services, such as Firebase Cloud Functions. These functions are used for operations that need to be performed on the server side, such as complex calculations, data processing, or sending notifications.

* **schema/**: The schema/ directory is crucial for defining the structure of data used throughout your app. It contains the following subdirectories and files:

  * **enums/:** Stores enumeration types used across the app.
  * **structs/:** These are used to represent custom data types like `Address` or `Cart`.
  * **util/:** Contains utility functions like `firestore_util.dart` and `schema_util.dart`.

##### custom\_code/

Custom Actions and Custom Widgets created by the developer are stored in this folder, in their respective subdirectories: `custom_code/actions` and `custom_code/widgets`.

##### flutter\_flow/

This directory is generated by FlutterFlow and contains various utility files that support the app's operation, such as custom functions, generated themes, navigation and more.

##### app\_constants.dart

This class is used to store constant values that are used throughout the application.

##### app\_state.dart

This file contains the [**FFAppState**](https://docs.flutterflow.io/generated-code/ff-app-state) class, which is responsible for managing the global App States created by the developer.

##### main.dart

The `main.dart` file serves as the entry point for your Flutter application. It begins by initializing the Flutter engine with `WidgetsFlutterBinding.ensureInitialized()`. Next, it sets up the URL strategy for the web application, initializes the `FlutterFlowTheme`, and sets up the `FFAppState` to manage the global state of your app.

##### pubspec.yaml

This file is the configuration file for your Flutter project. It defines the dependencies, assets, and other project settings. It also specifies which versions of Dart and Flutter your project uses, along with any third-party packages or plugins your app relies on.

This structure makes it easier to manage and scale your app!

---

### FlutterFlow State Management {#flutterflow-state-management}

*Learn about the state management used in FlutterFlow's generated code.*

**Source:** https://docs.flutterflow.io/generated-code/state-management

Correct topic?

This document explains the generated code behind the state management approaches used in FlutterFlow. If you're looking for guidance on adding state variables in FlutterFlow, refer to the **[State Variables](https://docs.flutterflow.io/concepts/state-management)** documentation.

FlutterFlow manages state in several ways, depending on the scope.

Generally, state management is handled using the [Provider](https://pub.dev/packages/provider) package, which facilitates the provisioning of data models for components, pages, and the overall app state.

![state-management.avif](https://docs.flutterflow.io/assets/images/state-management-231f8221303479d7d7af7e747c6a57e7.avif)

#### Page & Component Models

In FlutterFlow, both component widget models and page models share a uniform structure, enhancing consistency throughout the framework. They include local state fields to store data specific to the component, such as sizes or user inputs. These models are also equipped with initialization and disposal methods: `initState` for setup when the widget initializes, and `dispose` for resource cleanup when the widget is no longer needed.

Additionally, they provide space for action blocks, which are a set of actions that performs a specific task and can be reused in different parts of the app, and helper methods for extra functionalities needed by the component. This consistent structure across models helps efficiently manage the state and interactions of various components within the app.

#### Page State

[Variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle) used exclusively within a page — such as a text field validator or the value of a checkbox — are stored in the `Model` of each page. These variables can be accessed by other component children on the same page. For instance, on a page with a form, tapping a button in one component may need to access the value of a text field in a different component.

Variables within a page are tracked through `StatefulWidget` and are encapsulated into that page’s Model.

#### Component State

Similar to page state, [**Component State variables**](https://docs.flutterflow.io/resources/ui/components/component-lifecycle) are accessible within the component where they are defined. Each component has a corresponding `Model` and `Widget` class. Variables may be passed in from their parent as parameters. Additionally, you can access component state values from its parent Page widget.

This accessibility is possible because the Model of a component is instantiated within the parent Page model. It utilizes the Provider method `context.read()`, which returns any existing model in the tree before instantiating a new one. Thus, any updates to the state in the component model will reflect in the parent’s instance of that component model.

One of the helper methods in `flutter_flow_model.dart` is `wrapWithModel()`. This method wraps the child in a Provider model to make it accessible to the child and sets a callback function, which is generally used to call `setState()` in the parent page and update any changed values. We use this wrapper around widgets that need to access the data included in the model.

For example, if a page includes a component with a text field and later on the page there is a button needing access to the text field’s value, the button would be wrapped with `wrapWithModel()`, including the text field component’s Model as a parameter.

It’s important to note that components cannot directly access variables of other components on the same page. However, you can pass a variable from ComponentA as a parameter to ComponentB in their parent Page. This ensures that ComponentB receives all updates from ComponentA as expected.

#### App State

FFAppState

The generated code behind FlutterFlow's App State class is explained in the **[FFAppState](https://docs.flutterflow.io/generated-code/ff-app-state)** documentation.

#### Variables

Variables required across multiple pages of the app, such as a username, should be added to the App State. Refer to `lib/app_state.dart`.

All defined variables within the app state are components of the `FFAppState` class, which functions as a ChangeNotifier. This means listeners can subscribe and receive notifications when any changes occur.

On each page that requires access to app state variables, the method `context.watch<AppState>()` is called to initialize a listener for that page. This `watch()` method, provided by the Provider package, facilitates access to inherited widgets and acts as an effective wrapper.

#### Persisting App State

When an app state variable is created, selecting the "Persisted" option enables FlutterFlow to save it on the device using the [**Shared Preferences**](https://pub.dev/packages/shared_preferences) package. This ensures the variable remains available even after the app is restarted, making it ideal for persisting settings such as login status or a user's choice between light and dark modes.

If the "**Secure Persisted Fields**" option is enabled in the app state settings, FlutterFlow utilizes the [**Flutter Secure Storage**](https://pub.dev/packages/flutter_secure_storage) package to encrypt the data.

Platform Differences

If the platform is **Android**, then `flutter_secure_storage` stores data in [**`encryptedSharedPreference`**](https://developer.android.com/reference/androidx/security/crypto/EncryptedSharedPreferences), which are shared preferences that encrypt keys and values. It handles [**AES Encryption**](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) to generate a secret key encrypted with [**RSA**](https://en.wikipedia.org/wiki/RSA_\(cryptosystem\)) and stored in [**KeyStore**](https://developer.android.com/reference/java/security/KeyStore).

For the **iOS** platform, it uses the [**KeyChain**](https://developer.apple.com/documentation/security/keychain_services) which is an iOS-specific secure storage used to store and access cryptographic keys only in your app.

In the case of the **Web**, it uses the [**Web Cryptography**](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) (Web Crypto) API.

#### Global State

Global state variables are pieces of information related to the device that are accessible throughout the FlutterFlow app.

These include:

* Screen size
* Platform (mobile, web, Android, iOS)
* Keyboard visibility
* Current time

These variables are found in the "Global Properties" section and are automatically added by FlutterFlow, not generated by users. Users can utilize App State variables for their own global use cases.

Global properties are retrieved through methods defined in `flutter_flow_utils.dart`. Typically, these methods utilize built-in Flutter libraries, such as `dart:io`, to gather the necessary information.

#### Constants

For values that do not change throughout the app, such as API keys or environment flags, we utilize the `FFAppConstants` class, which can be found in `lib/app_constants.dart`. This is an abstract class, meaning it cannot be directly instantiated. Instead, it serves as a namespace for static constants, allowing these values to be organized and accessed consistently across the application.

---

---

## Miscellaneous

### Additional Resources To Get Help {#additional-resources-to-get-help}

*FlutterFlow community forum*

**Source:** https://docs.flutterflow.io/misc/additional-resources

##### FlutterFlow community forum

The [FlutterFlow Community](https://community.flutterflow.io/) is a place for you to share ideas, ask questions, and troubleshoot issues with other FlutterFlow builders. The community shares a lot of amazing ideas!

To join the FlutterFlow community,

1. Go to your account at [app.flutterflow.io](https://app.flutterflow.io)
2. Next Navigate to Resources tab on the left side
3. Click on "FlutterFlow Community". This will automatically log you in to the community.

![img\_5.png](https://docs.flutterflow.io/assets/images/img_5-a0490e088034a42f5ae6b0a70eb16425.png)

Alternatively,

If you are already in your project view, you can also find the **Help Menu** and click on **Community Forum**.

![img\_6.png](https://docs.flutterflow.io/assets/images/img_6-c8f43c9d55691803e9ab86d9965f0c18.png)

##### YouTube

Our [YouTube channel](https://www.youtube.com/channel/UC5LueiosDVInA6yXE_38i9Q/featured) contains a variety of tutorials and how-to videos.

##### Flutter community

Questions about Flutter? The [Flutter Community](https://flutter.dev/community) is a great resource!

##### Flutter performance best practices

[Here are some tips](https://docs.flutter.dev/perf/rendering/best-practices) on how to write the most performant Flutter app possible.

---

### Application & Data Ownership {#application-data-ownership}

*Intellectual Property*

**Source:** https://docs.flutterflow.io/misc/application-data-ownership

#### Intellectual Property

At FlutterFlow, we champion the principle of "Own Your Code," reflecting our commitment to enabling creators to retain ownership of their work. As you develop using FlutterFlow, you own the output of your work.

FlutterFlow incorporates open-source packages which are included in the code you export. We are diligent in our selection of packages, opting for those with commercially friendly licenses, and any FlutterFlow-generated helpers or libraries will consistently adhere to permissive licenses such as MIT or BSD-3-Clause.

Please be aware that third-party Flutter packages may undergo license changes or have dependencies that are not as commercially permissive. We recommend adhering to industry-standard practices to ensure compliance with all relevant licensing requirements.

> **Info:** Please read our [**Terms of Service**](https://flutterflow.io/tos) for full details on our Intellectual Property policies.

#### Data Handling and Privacy

The mobile applications you create with FlutterFlow are designed to operate independently of FlutterFlow's services, ensuring that your end-users' data remains exclusively within your application's ecosystem and does not interact with our servers.

In instances where you utilize FlutterFlow's hosting services for web applications, either through our subdomain or your custom domain, we are responsible solely for delivering the frontend of the compiled Flutter web application to your end-users.

FlutterFlow maintains a strict policy of non-interference with your end-users' data; we do not access, store, or collect any such data through our hosting infrastructure.

> **Info:** Please read our [**Privacy Policy**](https://flutterflow.io/privacy) for full details.

---

### Customer Support Policy {#customer-support-policy}

*We love connecting with our users and supporting you as you build your application! However, there are a few things that fall outside the scope of our support team. To avoid confusion, we've created this document to outline our Customer Support Policy.*

**Source:** https://docs.flutterflow.io/misc/customer-support-policy

We love connecting with our users and supporting you as you build your application! However, there are a few things that fall outside the scope of our support team. To avoid confusion, we've created this document to outline our Customer Support Policy.

Have a request for new documentation or tutorials we should create? You can share your ideas [here](https://flutterflow.typeform.com/to/hxg5nxbo).

##### Support Hours

Our support team is available from 5 AM to 5 PM Eastern Time, Monday through Friday.

##### How To Reach Us

Depending on your plan, there are multiple ways you can get support when using FlutterFlow:

* **Account and Billing Support**: Available for all plans. You can always reach out for help with managing your account or billing-related questions.

* **Community Support**: All users have access to the FlutterFlow Community Forums, where you can ask questions, share knowledge, and connect with other builders.

* **Email Support**: Available starting from the **Basic** plan and above. Get direct help from our support team via email.

* **In-App Support**: Available starting from the **Growth** plan and above. Chat directly with support specialists from within FlutterFlow for faster assistance.

* **Dedicated Live Support**: Exclusive to the **Enterprise** plan. Gain direct access to dedicated support specialists for priority, hands-on help.

##### What We Can Help With

**We are happy to provide guidance on what is possible within FlutterFlow (e.g. can I use non-Firebase authentication), but we don't provide instructions on how to design/build/troubleshoot these features (e.g., how do I implement authentication via Microsoft).**

##### Feature Design & Implementation

We'd love to help you build your dream app, but there are some topics that are outside of the scope of our support team.

If you aren't sure how to implement something, we recommend reaching out to the [FlutterFlow Community](https://community.flutterflow.io/) or connecting with a [FlutterFlow Expert.](https://experts.flutterflow.io/)

The following topics are out of the scope of our support team:

* Feature Design & Implementation
* Data Infrastructure Design
* Integration & Troubleshooting of 3rd-party APIs
* Implementation and troubleshooting of Custom Widgets and Code

##### Additional Resources

**Tutorials & How-To Guides** Our [YouTube channel](https://www.youtube.com/channel/UC5LueiosDVInA6yXE_38i9Q/featured) contains a variety of tutorials and how-to videos. In addition to our documentation, our [blog](https://blog.flutterflow.io/) also contains a number of how-to guides.

**Troubleshooting Guides**Our documentation contains a number of [troubleshooting guides](https://docs.flutterflow.io/misc/customer-support-policy) to help you diagnose and fix common issues.

Additionally, our [Community Forum](https://community.flutterflow.io/) is a great place to get ideas and troubleshooting tips from fellow FlutterFlow builders.

Lastly, you can connect with a [FlutterFlow Expert](https://experts.flutterflow.io/) to help you troubleshoot an issue or implement a complex new feature.

##### Bug Reporting Process

We regularly release feature updates and bug releases. To make sure you are on the most recent version of FlutterFlow select Ctrl/Cmd + R.

If you think you've found a bug, please submit an [in-app bug report](https://docs.flutterflow.io/flutterflow-ui/toolbar#help-menu) or let us know via chat (Growth, Business and Enterprise users only). Please make sure to include:

* A link to your project
* The page(s) effected
* The expected behavior and the behavior you are experiencing

###### Our Approach To Fixing Bugs

To ensure we fix the most critical issues first, we assess each bug based on the severity and number of users impacted.

Our highest priority is fixing critical issues that impact a large number of users. Issues impacting a smaller number of users or that have a workaround are addressed after any critical issues are fixed.

---

### Enterprise {#enterprise}

*Learn how to use FlutterFlow for Enterprise.*

**Source:** https://docs.flutterflow.io/misc/enterprise

#### Whitelist URLs

Enterprise environments often restrict internet access to enhance security and compliance. For example, they may allow access only to approved URLs that are essential for work-related tasks. FlutterFlow won't properly work in such restrictions because it accesses multiple services—Firestore, Cloud Functions, and various APIs—these URLs must be allowed in your corporate firewall for everything to function correctly.

To find out which URLs need to be whitelisted, navigate to the URL Access page from the FlutterFlow [dashboard](https://docs.flutterflow.io/flutterflow-ui/dashboard). Any URLs marked as **Inaccessible** are currently blocked by your network, which may prevent certain features from functioning properly. You can copy these URLs individually or use the Copy All Inaccessible URLs button in the top-right corner to collect them all at once. Then, share the list with your IT team for whitelisting.

![url-access](https://docs.flutterflow.io/assets/images/url-access-9b3813d91a4ed89f5d6244f16873664b.avif)

#### Enterprise Support Policy

We understand our Enterprise customers often rely on FlutterFlow for mission critical applications. To that end, we have created a dedicated Enterprise support team to provide the highest level of service and support. This document outlines our support channels and scope for Enterprise customers.

##### Support Channels

Enterprise customers can reach our dedicated support team either through the chat widget in FlutterFlow or by emailing us. Our Enterprise support team is available 24x7, and we do our best to respond to every support request as quickly as possible. Depending on the complexity of the issue and your Enterprise support subscription, our team can assist through chat, email or video calls.

##### What We Can Help With

Our goal is for every one of our Enterprise customers to be successful building in FlutterFlow. Here are some of the areas covered by our Enterprise support team:

* Guidance on what is possible within FlutterFlow (e.g. can I use non-Firebase authentication)
* General education on FlutterFlow features and platform capabilities
* Bugs and technical issues with core FlutterFlow features
* Team and user account administration

Depending on your Enterprise support subscription, we may also provide advisory services in the following areas:

* Feature Design & Implementation
* Data Infrastructure Design
* Integration & Troubleshooting of 3rd-party APIs
* Implementation & Troubleshooting of Custom Widgets and Code

##### FlutterFlow Bug Policy

We know that bugs can be frustrating and we work to fix these on an ongoing basis. If you think you've found a bug, please [submit an bug report](https://github.com/FlutterFlow/flutterflow-issues/issues).

###### **Our Approach To Fixing Bugs**

To ensure we fix the most critical issues first, we assess each bug based on the severity and number of users impacted.

Our highest priority is fixing critical issues that impact a large number of users. Issues impacting a smaller number of users or that have a workaround are addressed after any critical issues are fixed.

We provide updates on our bug fixes in our marketing emails and in our Release Tracker.

---

### Hire FlutterFlow Developer {#hire-flutterflow-developer}

*Learn how to hire a FlutterFlow Developer.*

**Source:** https://docs.flutterflow.io/misc/hire-flutterflow-developer

You can hire a skilled FlutterFlow Developer to build your app at: <https://flutterflow.io/work-with-developers>.

**FlutterFlow Developers** include agencies and freelancers skilled in building apps using FlutterFlow. Many of them have the **FlutterFlow Expert** badge, awarded to those who demonstrate advanced technical proficiency. To earn this recognition, they must pass the FlutterFlow Expert training and submit a portfolio of their work for our evaluation.

Please Note

* FlutterFlow Developers are independent professionals, not employees, agents, or affiliates of FlutterFlow.
* Any services provided are solely the responsibility of the Developer, not FlutterFlow.
* We recommend signing a contract with the Developer before making any payments to ensure clarity on deliverables and timelines.

Visit <https://flutterflow.io/work-with-developers> to get started.

![hire-dev-page.png](https://docs.flutterflow.io/assets/images/hire-dev-page-4ce5c7a7bbc3ba59365e91a8e49d50d5.png)

There are two ways to find a Developer:

* **Get matched**: Receive recommendations based on your project requirements and preferences (*recommended*).
* **Browse Developers**: Explore available Developers, view their details, and reach out to specific ones.

In both cases, you’d need to make an account with FlutterFlow, and fill out a project proposal about your project. Make sure to clearly convey your needs, objectives, and any specific requirements. This information is crucial for the Developer to provide you with an accurate timeline and quote.

#### Get Matched With Developers

To get matched with developers based on your project requirements, follow the steps below:

1. Create or log into your FlutterFlow account.

   ![login-ff-2.png](https://docs.flutterflow.io/assets/images/login-ff-2-93ef4a99466cd0f58b909780d6aed489.png)

2. Fill out your project details, including features, budget, geo, and language preferences.

   ![project-details.png](https://docs.flutterflow.io/assets/images/project-details-77fc83a0d4b7fa6cfca1c8b169106d76.png)

3. Review your project proposal for accuracy and completeness.

   ![review-project-proposal.png](https://docs.flutterflow.io/assets/images/review-project-proposal-b1640398d5c73bce35a263adb518c0d9.png)

4. Confirm your project details to get matched with Developers based on your requirements.

   ![confirm-developers.png](https://docs.flutterflow.io/assets/images/confirm-developers-40dd0af548322cba1cd6b0acd967d264.png)

Please Note

You can send your request upto 5 Developers at a time.

Alternatively, you can browse Developers, view their profiles, and use the **Hire** button to send a personalized project proposal.

![browse-devs.png](https://docs.flutterflow.io/assets/images/browse-devs-f00bb90d36ed1738aa1290273230c11b.png)

#### FAQs

Do FlutterFlow Developers work for FlutterFlow?

No, FlutterFlow Developers are independent professionals, including designers, developers, and consultants with expertise in FlutterFlow.

How are Developers selected for my project?

Developers are matched based on your requirements, such as geo, language, budget, and project scope. Priority is given to Developers with the FlutterFlow Expert badge.

Am I obligated to work with a Developer after contacting them?

No, contacting a Developer does not obligate you to engage their services.

How are contracts and payments managed?

Contracts and payments are directly negotiated between you and the Developer. FlutterFlow does not handle contracts or payments. All terms, including scope, costs, and timelines, are agreed upon by both parties. Payments are processed through the Developer’s preferred billing system.

---

### Security {#security}

*At FlutterFlow, we consider security to be our utmost priority. We understand the importance of safeguarding your data and ensuring a secure environment for our users. Below, we provide an overview of our security measures to give you confidence in the safety of your information.*

**Source:** https://docs.flutterflow.io/misc/security

At FlutterFlow, we consider security to be our utmost priority. We understand the importance of safeguarding your data and ensuring a secure environment for our users. Below, we provide an overview of our security measures to give you confidence in the safety of your information.

#### Commitment to Security

Security is our top priority. We employ a comprehensive approach to ensure the protection of our users' data, and we continuously strive to enhance our security measures.

#### Custom Data Safety

Your custom data is in safe hands. We implement robust security protocols to prevent unauthorized access, disclosure, alteration, and destruction of your data. Our systems are designed to ensure the confidentiality and integrity of the information you trust us with.

#### SOC2 Type 1 Certification

FlutterFlow is proud to be SOC2 Type 1 certified. This certification attests to our commitment to maintaining strict security controls and measures, providing assurance to our users that their data is handled with the highest standards of security.

#### GCP Best Practices

We follow Google Cloud Platform (GCP) best practices to ensure the security of our infrastructure. By leveraging GCP's advanced security features, we aim to create a resilient and secure environment for our users.

#### Security and Monitoring Services

FlutterFlow utilizes a range of GCP security and monitoring services to enhance our overall security posture. These services include:

* **Cloud Armor:** Protects against DDoS attacks by providing defense at the edge of the GCP network.
* **Cloud IDS (Intrusion Detection Service):** Monitors and detects potential intrusions or security threats.
* **Key Management Service (KMS):** Manages cryptographic keys used for encryption and decryption.
* **Secret Manager:** Safely stores and manages sensitive information such as API keys, passwords, and certificates.
* **Cloud Monitoring:** Monitors the performance, uptime, and overall health of our systems.

These services collectively contribute to a robust security framework, ensuring that our users' data remains secure and our systems are actively monitored for any potential security incidents.

At FlutterFlow, we believe in transparency and accountability when it comes to security. Rest assured that we are dedicated to maintaining the highest standards of security to protect your valuable information.

---

### Submit Bug Reports {#submit-bug-reports}

*Learn how to submit bug report.*

**Source:** https://docs.flutterflow.io/misc/submit-bug-report

This page guides you on submitting the bug reports in the GitHub issue tracker.

We have created a [**GitHub repository**](https://github.com/FlutterFlow/flutterflow-issues/issues) specifically for tracking bug reports from our user community. This initiative fosters a more open and collaborative relationship with our users, encouraging them to report any bugs or glitches they encounter while using FlutterFlow.

This will enable us to track, triage, and resolve issues in a timely and efficient manner. So, if you encounter any bugs or issues, please don't hesitate to report them on our GitHub repository! 🐛

> **Info:** * You should use this only for reporting **FlutterFlow bugs**.
* Any new features, suggestions, and questions should be discussed in the [**community**](https://community.flutterflow.io/home) or submitted through our user feedback form.

Here is the simple flow you can refer to submit the bug report:

![Bug reporting flow](https://docs.flutterflow.io/assets/images/submit-bug-report-flow-5607bbbc75d9043356049ef34f4c03ed.avif)

Before creating a new issue, it's recommended to search the issue tracker to avoid submitting duplicate reports. If you find an existing issue, show your support by upvoting it using the *Thumbs Up* icon. If you have additional information to share or clarifications to make, add them as comments on the original issue. In case you can't find the relevant issue, you can create a new one with all the necessary details. This will help us address the issue faster and more efficiently.

Here are the step-by-step instructions:

1. Open the [issue tracker](https://github.com/FlutterFlow/flutterflow-issues/issues) and click on the **New Issue** button. Note: If you haven't already, you must [create a GitHub account](https://github.com/signup?ref_cta=Sign+up\&ref_loc=header+logged+out\&ref_page=%2F\&source=header-home).

   ![new-issue](https://docs.flutterflow.io/assets/images/new-issue-098523880b1bf4743ced662721047370.avif)

2. On the right side of the **Bug Report**, click the **Get Started** button.

   ![get-started](https://docs.flutterflow.io/assets/images/get-started-392ee263d173c89078bd128c601e3056.avif)

3. When describing your issue in the **Title** box, be as specific and concise as possible. Use descriptive words that accurately convey the problem. For example, instead of simply writing "*DatePicker issue*," provide more details such as "*Disabled future dates in the Date/Time picker action, still shows*". This will help us and others quickly understand the issue and can also help with searchability in case someone else has experienced the same problem.

   ![disabled-future](https://docs.flutterflow.io/assets/images/disabled-future-1272298d3b1583efaa5a0311fc22b0a0.avif)

4. If your issue doesn't exist and you allow us to access your project for the sole purpose of investigation, you can tick both checkboxes.

   ![issue-doesnt-exist](https://docs.flutterflow.io/assets/images/issue-doesnt-exist-acd0cd9386d92c1e28ebb9b8e8e437c0.avif)

5. In the '**Current behavior**' section, provide as much detail as possible about the behavior you are experiencing.

   ![current-behaviour](https://docs.flutterflow.io/assets/images/current-behaviour-ed947ee62061f9766d7ccc338f775ac4.avif)

6. In the '**Expected behavior**' section and enter a clear and concise description of what you expected to happen. Make sure that the expected behavior is realistic and achievable.

   ![expected-behaviour](https://docs.flutterflow.io/assets/images/expected-behaviour-3a811f4311b24626d56bb7205afe2963.avif)

7. In '**Steps to Reproduce**' section, write the step-by-step instructions to reproduce the bug. Also, mention any specific settings or configurations that might be relevant. This will help us diagnose the issue. **Note**: Issues cannot be accepted if they are too vague. For example, "project fails to build."

   ![steps-to-reproduce](https://docs.flutterflow.io/assets/images/steps-to-reproduce-19d02f4c751ffeae4968c577c7540852.avif)

8. The '**Bug Report Code**' is a unique code that helps us assess your issue. To copy it, open the **Widget Tree** > **Right Click** > select **Get Bug Report Code** and paste it here. **Note** that if an error is related to a specific widget, select the widget, right click and get the code.

9) Use the '**Context**' section to describe how it has affected you and what you are trying to accomplish.
10) In '**Additional Info**' you can provide a screenshot or recording, links, references, or anything else that will give us more context about the issue you are encountering.

> **Tip:** You can attach any media by dragging it here.

11. We must know the environment in which you experienced the issue. You can post such information under the '**Environment**' section.

    ![environment](https://docs.flutterflow.io/assets/images/environment-4d142e2107a005a0d1e7ec54f978a892.avif)

12. Click **Submit New Issue**.

    ![submit-new-issue](https://docs.flutterflow.io/assets/images/submit-new-issue-0556bf13483d804bc7c17ab64c87e51a.avif)

Once done, your issue will be listed on the issues list, and our team will assign the appropriate label.

![submitted](https://docs.flutterflow.io/assets/images/submitted-56e7c458b66c92d76bad7e06f93fc9b6.avif)

---

---

## Quickstart

### Quickstart Guide {#quickstart-guide}

*Build your first interactive FlutterFlow app by creating a layout, customizing its style, managing state, and testing the result.*

**Source:** https://docs.flutterflow.io/quickstart

Welcome to the FlutterFlow Quickstart Guide! This guide introduces the basic FlutterFlow concepts through a short, hands-on exercise. You'll build a product quantity selector that allows users to adjust the quantity of an item before adding it to their shopping cart.

Before You Begin

To complete this guide, you need:

* A [**FlutterFlow account**](https://app.flutterflow.io/).
* A web browser.
* About 15-20 minutes.

Below is a preview of what your completed app will look like:

![Quick start demo app](https://docs.flutterflow.io/assets/images/flutterflow-quick-start-app-demo-31982001a42882349b513c21db17a1e0.avif)

#### What You'll Learn

* Build a layout with widgets.
* Customize widget styles.
* Add interactivity with actions.
* Manage page state in response to user input.
* Run and test your app.

Follow these steps to build the app:

1. [Clone the starter project](https://docs.flutterflow.io/quickstart#clone-project)
2. [Build the UI](https://docs.flutterflow.io/quickstart#build-ui)
3. [Customize styles](https://docs.flutterflow.io/quickstart#customize-style)
4. [Manage state](https://docs.flutterflow.io/quickstart#manage-state)
5. [Run the app](https://docs.flutterflow.io/quickstart#run-app)

#### 1. Clone the Starter Project

This guide uses a prepared starter app so you can focus on building the interaction. Open the [FlutterFlow Quickstart project](https://app.flutterflow.io/project/f-f-quick-start-app-umu392), click **Clone**, and the project will be added to your account.

To begin with a separate project instead, see [Create a Project](https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects#how-to-create-a-project).

![clone-project.avif](https://docs.flutterflow.io/assets/images/clone-project-994b7d019a46e8a06e35911a126d24d2.avif)

After cloning the project, you’ll see a page with product images and a description. You’ll add a feature that allows users to update the product quantity.

![final-quick-start.avif](https://docs.flutterflow.io/assets/images/final-quick-start-f218dc46f227c5d088a7541ac6b6dddc.avif)

#### 2. Build the UI

Build the quantity control by combining layout and display widgets in the product page's Widget Tree.

1. Open the product page and locate the content below the product description.
2. Add a **Container** to hold the quantity control.
3. Add a **Row** inside the Container.
4. Add a **Text** widget for the "Quantity" label.
5. Add controls for decreasing the quantity, displaying its current value, and increasing it.
6. Arrange the widgets so the label appears on the left and the quantity controls appear on the right.

[Sharing a Project with a User](https://demo.arcade.software/13kkejiZuiFeo9Fj8aWz?embed\&show_copy_link=true)

> **Info:** To learn more, see [**Building Layouts**](https://docs.flutterflow.io/concepts/layouts) and the [**Widget Overview**](https://docs.flutterflow.io/resources/ui/widgets).

#### 3. Customize Styles

Next, style the quantity control to match the rest of the product page. Use the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) to adjust each selected widget.

1. Adjust the spacing and alignment of the Row.
2. Select the Container that holds the quantity control and adjust its background color, padding, size, and corner radius.
3. Style the "Quantity" label and value so they are easy to read.
4. Customize the decrease and increase controls with suitable icons, colors, and sizes.
5. Compare the result with the completed preview and make any final visual adjustments.

[Sharing a Project with a User](https://demo.arcade.software/mA0EGCPhuyJ6UUQFPDUP?embed\&show_copy_link=true)

#### 4. Manage State

Once your UI is set up, make your app interactive by adding a page state variable. A state variable stores data that can change as users interact with the page. In this exercise, it stores the current product quantity and updates the displayed value when users select the increase or decrease control.

##### 4.1 Add a State Variable

Add a [page state variable](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle) that will hold the current quantity value. Here's how to add and use the state variable:

1. Select the page's root widget in the Widget Tree.
2. Open the page's state management settings and add a new field.
3. Name the field `quantity`, set its data type to **Integer**, and give it an initial value of `1`.
4. Select the Text widget that displays the quantity.
5. Set its value from **Page State > quantity**.

> **Info:** To learn more about this workflow, see [**Creating a Page State**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state).

[Sharing a Project with a User](https://demo.arcade.software/T8dg4g238t37cct3vrD2?embed\&show_copy_link=true)

##### 4.2 Update the State Variable

Use actions to change `quantity` when a user selects the increase or decrease control:

1. Select the increase control and add an **On Tap** action.
2. Choose **Update Page State**, select `quantity`, and set it to its current value plus `1`.
3. Select the decrease control and add another **On Tap** action.
4. Update `quantity` to its current value minus `1`.
5. Confirm that both controls update the Text widget bound to `quantity`.

> **Info:** See the [**Action Flow Editor**](https://docs.flutterflow.io/resources/functions/action-flow-editor) and [**Update Page State**](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action) guides for more details.

[Sharing a Project with a User](https://demo.arcade.software/rmxuLzwsP7uGgGQUI4YO?embed\&show_copy_link=true)

#### 5. Run the App

Use [**Test Mode**](https://docs.flutterflow.io/testing/run-your-app#test-mode) to try the interaction and see changes quickly. Test Mode runs a web version of your app and can automatically sync changes from the FlutterFlow builder.

1. Select **Test Mode** from the left-side menu.
2. Wait for the test session to start.
3. Click or tap the increase and decrease controls and confirm that the displayed quantity changes.

[**Run Mode**](https://docs.flutterflow.io/testing/run-your-app#run-mode) creates a fully functional build that can include live data and be shared with project members. Because it creates a new build, it typically takes longer and does not support hot reload.

[Sharing a Project with a User](https://demo.arcade.software/hdpwwkbCYcvsjsrkygDX?embed\&show_copy_link=true)

Congratulations! You've built your first app with FlutterFlow.

#### Verify the Result

Before moving on, confirm that:

* The initial quantity is displayed correctly.
* The increase control raises the quantity.
* The decrease control lowers the quantity.
* The layout remains aligned as the value changes.
* The interaction works in Test Mode.

#### Next Steps

Continue learning with these guides:

* [Building Layouts](https://docs.flutterflow.io/concepts/layouts)
* [Widget Overview](https://docs.flutterflow.io/resources/ui/widgets)
* [Page State](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state)
* [Action Flow Editor](https://docs.flutterflow.io/resources/functions/action-flow-editor)
* [Run and Test Your App](https://docs.flutterflow.io/testing/run-your-app)

#### Need Help?

If you're experiencing any issues with the app, review the steps above and verify that each widget and action is configured as described.

For additional help, ask a question in the [Community Forum](https://community.flutterflow.io/) or contact FlutterFlow Support.

---

---

## Roadmap

### Roadmap {#roadmap}

*This roadmap guides you through the key layers of app development: the UI Layer, Logic Layer, and Data Layer. Understanding these layers is essential for creating apps that are visually appealing, functionally robust, and secure.*

**Source:** https://docs.flutterflow.io/roadmap

This roadmap guides you through the key layers of app development: the **UI Layer, Logic Layer,** and **Data Layer**. Understanding these layers is essential for creating apps that are visually appealing, functionally robust, and secure.

![layers.avif](https://docs.flutterflow.io/assets/images/layers-aea5e7fd1325b59a7152ec28570b56bc.avif)

#### UI Layer

The UI Layer is all about the visual elements and interactions in your app. It includes widgets for buttons, forms, navigation, and layouts. In FlutterFlow, this layer also covers customization options like themes and responsive design, ensuring your app looks great and is easy to use.

* **FlutterFlow Widgets:**

  * [Atomic Design](https://docs.flutterflow.io/resources/ui/overview)
  * [Pages](https://docs.flutterflow.io/resources/ui/pages), [Widget](https://docs.flutterflow.io/resources/ui/widgets) & [Components](https://docs.flutterflow.io/resources/ui/components)
  * [TextFields](https://docs.flutterflow.io/resources/forms/textfield) & [Other Form Widgets](https://docs.flutterflow.io/resources/forms)

* **Navigation Elements:**

  * [Page Transitions (Slide, Fade, etc.)](https://docs.flutterflow.io/concepts/animations/page-transition)
  * [AppBar and other Page Elements](https://docs.flutterflow.io/resources/ui/pages/scaffold)
  * [Bottom Sheets](https://docs.flutterflow.io/concepts/navigation/bottom-sheet)
  * [Webviews](https://docs.flutterflow.io/concepts/navigation/webview)

* **User Experience (UX):**

  * [Design System](https://docs.flutterflow.io/concepts/design-system)

  * [Responsiveness](https://docs.flutterflow.io/concepts/layouts/responsive)

  * Interaction Feedback * [Animations](https://docs.flutterflow.io/concepts/animations)
    * [Haptic Feedback](https://docs.flutterflow.io/concepts/alerts/haptic-feedback)

#### Logic Layer

The Logic Layer handles your app's business logic and decision-making. This includes state management, conditional actions, and navigation logic.

* **State Management:**

  * Representing Data * [Variables](https://docs.flutterflow.io/resources/data-representation/variables)
    * [Datatypes](https://docs.flutterflow.io/resources/data-representation/data-types) & [Custom Data Types](https://docs.flutterflow.io/resources/data-representation/custom-data-types)
    * [Enums](https://docs.flutterflow.io/resources/data-representation/enums)
    * [Constants](https://docs.flutterflow.io/resources/data-representation/constants)

  * [State Variables](https://docs.flutterflow.io/concepts/state-management)

  * [Managing Widget States](https://docs.flutterflow.io/concepts/state-management/widget-state)

  * Dynamic Lists [(Generating Dynamic Children)](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/generate-dynamic-children)

* **Actions & Business Logic:**

  * [Actions](https://docs.flutterflow.io/resources/functions/action-flow-editor)
  * [Conditional Actions](https://docs.flutterflow.io/resources/functions/conditional-logic)
  * [Custom Code](https://docs.flutterflow.io/concepts/custom-code)
  * [Form Validation Logic](https://docs.flutterflow.io/resources/forms/form-validation)

* **Navigation Logic:**

  * [Navigation & Routing](https://docs.flutterflow.io/concepts/navigation/overview)
  * [Deep & Dynamic Linking](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking)

* **Notification Systems**:

  * [Triggering Push Notifications](https://docs.flutterflow.io/concepts/notifications/push-notifications)
  * [Alert Dialogs](https://docs.flutterflow.io/concepts/alerts/alert-dialog)

#### Data Layer

The Data Layer manages data storage, retrieval, and integration with external sources like APIs and databases.

* **Authentication:**

  * [Auth Methods Overview](https://docs.flutterflow.io/integrations/authentication-methods)
  * [Firebase or Supabase or Custom Authentication](https://docs.flutterflow.io/integrations/authentication-types)

* **Database Integration:**

  * [Firebase](https://docs.flutterflow.io/integrations/database/cloud-firestore/getting-started) or [Supabase](https://docs.flutterflow.io/integrations/database/supabase/database-actions) integration.
  * Local Storage with [AppState](https://docs.flutterflow.io/resources/data-representation/app-state) or [SQLite DB](https://docs.flutterflow.io/integrations/database/sqlite)

* **API Integration:**

  * Working with [REST APIs](https://docs.flutterflow.io/resources/backend-logic/create-test-api)
  * [Streaming APIs](https://docs.flutterflow.io/resources/backend-logic/streaming-api)

---

