# FlutterFlow Documentation — Complete Guide (Part 7 of 7: Troubleshooting Guides)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 76
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 7 of 7 — Troubleshooting Guides
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 4: Resources: Data, Backend Query, Forms, Functions & Projects (`FlutterFlow_Guide_04_ResourcesDataAndLogic.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)

## Table of Contents

**Troubleshooting**

- [API Charset and Encoding Fix Guide](#api-charset-and-encoding-fix-guide)
- [Client-Server Errors During the API Call](#client-server-errors-during-the-api-call)
- [Securing Your API Keys in Private API Calls](#securing-your-api-keys-in-private-api-calls)
- [Custom Domain Connection Error](#custom-domain-connection-error)
- [Custom Domain Connection Issues](#custom-domain-connection-issues)
- [Web Publishing FAQs](#web-publishing-faqs)
- [Codemagic Install Pods Failure](#codemagic-install-pods-failure)
- [Codemagic Signing Certificate Limit](#codemagic-signing-certificate-limit)
- [Download dSYM File from App Store Connect](#download-dsym-file-from-app-store-connect)
- [ImageNotification Development Team Error](#imagenotification-development-team-error)
- [iOS Deployment Authentication Error](#ios-deployment-authentication-error)
- [App Starts from HomePage in Run Mode](#app-starts-from-homepage-in-run-mode)
- [Check Firebase Login Method](#check-firebase-login-method)
- [Deleting Firebase Users and Related Data](#deleting-firebase-users-and-related-data)
- [Fix Google Sign-In Issues](#fix-google-sign-in-issues)
- [Permission Denied: Code 403](#permission-denied-code-403)
- [SafetyNet Phone Sign-In Issue on Android Devices](#safetynet-phone-sign-in-issue-on-android-devices)
- [Sign in With Apple (for Web)](#sign-in-with-apple-for-web)
- [Troubleshooting Custom Authentication](#troubleshooting-custom-authentication)
- [ListView Gray Box and Red Screen Errors](#listview-gray-box-and-red-screen-errors)
- [Fix ListView Only Returning One Item](#fix-listview-only-returning-one-item)
- [Resolving Firebase Configuration Issues](#resolving-firebase-configuration-issues)
- [Update Document Action Fails During Backend Call](#update-document-action-fails-during-backend-call)
- [Fix Cloud Functions Deployment](#fix-cloud-functions-deployment)
- [Custom Actions Errors](#custom-actions-errors)
- [Testing Custom Actions using Debug Console](#testing-custom-actions-using-debug-console)
- [Codemagic Deployment Error Identification](#codemagic-deployment-error-identification)
- [CodeMagic Deployment Tips](#codemagic-deployment-tips)
- [Deployment Issues with Stripe Integration](#deployment-issues-with-stripe-integration)
- [Fixing Razorpay Deployment](#fixing-razorpay-deployment)
- [Fixing Stripe Deployment & Payment Errors](#fixing-stripe-deployment-payment-errors)
- [Resolve Errors in Downloaded Code](#resolve-errors-in-downloaded-code)
- [Run Mode: Build Failure](#run-mode-build-failure)
- [Enterprise](#enterprise)
- [Client Access to Firestore Expired](#client-access-to-firestore-expired)
- [Configuring CORS for Firebase Storage](#configuring-cors-for-firebase-storage)
- [Content Manager Firestore Error](#content-manager-firestore-error)
- [Firebase Android Config File Missing](#firebase-android-config-file-missing)
- [Firebase Storage Limits in FlutterFlow](#firebase-storage-limits-in-flutterflow)
- [Get the Sum of Firebase Document or API Values](#get-the-sum-of-firebase-document-or-api-values)
- [Missing Firebase Storage in FlutterFlow Settings](#missing-firebase-storage-in-flutterflow-settings)
- [Resolving Firestore Index Deployment Issues](#resolving-firestore-index-deployment-issues)
- [Unable to Validate Firestore Schema](#unable-to-validate-firestore-schema)
- [Updating Firestore Security Rules](#updating-firestore-security-rules)
- [Initialize GitHub Repository](#initialize-github-repository)
- [Repository Head Deployment Failure](#repository-head-deployment-failure)
- [AdMob Ads Not Displaying in Google Play Testing](#admob-ads-not-displaying-in-google-play-testing)
- [Declare Advertising ID for Android 13+ in Play Console](#declare-advertising-id-for-android-13-in-play-console)
- [Error Running Pod Install](#error-running-pod-install)
- [Fix Flutter Launcher Icons Package Error](#fix-flutter-launcher-icons-package-error)
- [Google Play Draft Release Error](#google-play-draft-release-error)
- [Google Play Failed to Upload Artefacts](#google-play-failed-to-upload-artefacts)
- [Google Play Store Debug Signing Error](#google-play-store-debug-signing-error)
- [Launcher Icon Missing After Upload](#launcher-icon-missing-after-upload)
- [Migrate to Play Integrity API From SafetyNet Attestation](#migrate-to-play-integrity-api-from-safetynet-attestation)
- [Signed in Debug Mode Error](#signed-in-debug-mode-error)
- [Version Solving Failed Due to Incompatible Package](#version-solving-failed-due-to-incompatible-package)
- [FCM Token Generation Troubleshooting](#fcm-token-generation-troubleshooting)
- [Firebase Push Notification Troubleshooting](#firebase-push-notification-troubleshooting)
- [Firebase Push Notifications on Web](#firebase-push-notifications-on-web)
- [Fix Insufficient Permissions for Push Notifications](#fix-insufficient-permissions-for-push-notifications)
- [Fix Push Notifications Sent to Zero Devices](#fix-push-notifications-sent-to-zero-devices)
- [Black Screen During Preview](#black-screen-during-preview)
- [Firestore Permission Error in Run Mode](#firestore-permission-error-in-run-mode)
- [Gray Screen in Run Mode](#gray-screen-in-run-mode)
- [Loading Spinner in Run Mode](#loading-spinner-in-run-mode)
- [Local Build ProviderInstaller Error](#local-build-providerinstaller-error)
- [Slow Loading in Test Mode](#slow-loading-in-test-mode)
- [Test API Calls](#test-api-calls)
- [Fix Google Translate Errors](#fix-google-translate-errors)
- [Custom Widget Errors](#custom-widget-errors)
- [Emoji Size on iOS Devices](#emoji-size-on-ios-devices)
- [Infinite Scroll Pagination in ListView](#infinite-scroll-pagination-in-listview)
- [Rive Animation Loading Errors](#rive-animation-loading-errors)
- [Scroll To Action on Page Load](#scroll-to-action-on-page-load)
- [Store Custom Widget Output Using App State](#store-custom-widget-output-using-app-state)

---

## Troubleshooting

### API Charset and Encoding Fix Guide {#api-charset-and-encoding-fix-guide}

*When working with API calls in FlutterFlow, you might encounter issues where the response returns with strange characters, incorrect formatting, or unreadable content. These problems are often caused by improper charset or encoding settings either in the API request or the server response.*

**Source:** https://docs.flutterflow.io/troubleshooting/api/api-charset-and-encoding-fix-guide

When working with API calls in FlutterFlow, you might encounter issues where the response returns with strange characters, incorrect formatting, or unreadable content. These problems are often caused by improper charset or encoding settings either in the API request or the server response.

This guide shows you how to resolve such issues and ensure your API outputs are correctly displayed in your FlutterFlow project.

Follow the steps below:

1. **Set Proper Request Headers**

   Make sure your API call includes the appropriate headers to instruct the server on how to format the response. Add the following headers to your API configuration:

   * `Content-Type: application/json`

   * `Charset: utf-8`​

   These headers tell the server to return the data in JSON format using UTF-8 encoding, which is compatible with FlutterFlow.

   ![Setting Content-Type and Charset headers](https://docs.flutterflow.io/assets/images/20250430121409119593-f9abb5e3b9054634e35b7478b2c4ae30.png)

2. **Enable UTF-8 Decoding in FlutterFlow**

   If the server does not specify encoding—or if you're still getting corrupted text—you can configure FlutterFlow to decode the API response as UTF-8 manually.

   To do this:

   1. Go to your API call setup in FlutterFlow.
   2. Scroll to **Advanced Settings**.
   3. Enable **Force response decoding as UTF-8**.

   This setting helps FlutterFlow correctly interpret the API response, especially from servers that don’t return standard headers.

   ![Force decode response as UTF-8](https://docs.flutterflow.io/assets/images/20250430121409391507-ffa5d343b7e960f80dc91eb8e3d9af2a.png)

Final Tips

* Always test your API calls in FlutterFlow’s API Test tab to ensure the response is properly formatted.
* Confirm that the external API supports UTF-8 and returns a valid JSON response.
* Review your server settings if you control the backend, to ensure it sends the correct headers.

> **Note:** Incorrect API call outputs due to charset or encoding can be quickly resolved by:

* Adding proper headers like `Content-Type: application/json` and `Charset: utf-8`.
* Enabling **Force response decoding as UTF-8** in FlutterFlow’s API advanced settings. These simple steps will help you get accurate and readable data from your APIs, resulting in a smoother app development experience.

If you still face challenges, don't hesitate to reach out to our support team through Live chat or by emailing <support@flutterflow.io>

---

### Client-Server Errors During the API Call {#client-server-errors-during-the-api-call}

*When calling an API in FlutterFlow, you may run into client-server errors. These typically come as status codes that indicate what went wrong, either on your end (the client) or on the server you're requesting data from.*

**Source:** https://docs.flutterflow.io/troubleshooting/api/client-server-errors-during-the-api-call

When calling an API in FlutterFlow, you may run into client-server errors. These typically come as status codes that indicate what went wrong, either on your end (the client) or on the server you're requesting data from.

This guide will help you understand the most common API error codes and how to fix them.

To learn more about APIs, check out our **[API documentation guide](https://docs.flutterflow.io/resources/backend-logic/rest-api)**.

#### Common Client-Side Status Codes

These errors are usually caused by incorrect requests from the client side.

* **400 – Bad Request**

  The 400 error is a generic response indicating that the server could not understand the request due to malformed syntax. Common causes include incorrect query parameters or missing fields in the request body. Ensure your request is correctly formatted and all required information is included.

  tip

  Check the API's own documentation to ensure you're including the correct fields and headers.

  ![400 Example](https://docs.flutterflow.io/assets/images/20250430121351345482-673e942c94c6b33263d5ed75e5c7833b.png)

* **401 – Unauthorized**

  This status code appears when authentication has not yet been provided. To resolve this, ensure you have signed up for the API and included your API key in the HTTP header of your request.

  ![401 Example](https://docs.flutterflow.io/assets/images/20250430121350799148-811fa6f6d26ee9693c3520006c344d9a.png)

* **403 – Forbidden**

  Receiving a 403 error means you're authenticated but do not have permission to access the requested resource. This could be due to using the wrong API key or attempting to access features not available in your subscription plan.

  ![403 Example](https://docs.flutterflow.io/assets/images/20250430121351077308-5530372a8a17f5b9c34c4a2cac813698.png)

* **404 – Not Found**

  The 404 error indicates that the requested URL does not exist on the server. This could be due to a typo in the URL or changes in the API endpoints. Always verify the URL and check for any recent API updates.

  tip

  Always double-check your request URL before troubleshooting further.

  ![404 Example](https://docs.flutterflow.io/assets/images/20250430121350517804-696d4bb632fe7720f7e469260ce90792.png)

* **407 – Proxy Authentication Required**

  You haven't authenticated with the proxy server. This is less common but can happen in restricted network environments.

* **422 – Unprocessable Entity**

  Your request was well-formed but couldn’t be processed. For example, passing a `latlng` without a comma.

* **429 – Too Many Requests**

  This error occurs when too many requests are sent in a short period, exceeding the API's rate limits. To avoid this, implement request throttling or review your API subscription plan to ensure it meets your needs.

  tip

  Check your API plan limits and consider throttling requests from your app.

#### Common Server-Side Status Codes

These errors occur on the API server side.

* **500 – Internal Server Error**

  A 500 error can occur for various reasons, often indicating that the API server has crashed. Check your request for accuracy and consult the API documentation for any known issues.

* **501 – Not Implemented**

  This error occurs when the HTTP method used in the request is not supported by the server. Trying a different HTTP method or checking the API documentation for supported methods can resolve this issue.

* **502 – Bad Gateway**

  This error means that the server, acting as a gateway or proxy, received an invalid response from the upstream server. It's usually a temporary issue that should be resolved by the API provider.

* **503 – Service Unavailable**

  The 503 status code indicates that the server is temporarily unable to handle the request due to overload or maintenance. Waiting before sending another request is often the best approach.

* **504 – Gateway Timeout**

  A 504 error suggests that the server, acting as a gateway, did not receive a timely response from the upstream server. This could be due to network latency or the API server processing the request too slowly.

**Troubleshooting Steps**

* **Clear Browser Cache and Cookies**

  If you're encountering a 400 Bad Request error, clearing your browser's cache and cookies can resolve issues related to expired or invalid data.

* **Verify the Requested URL**

  Ensure the URL or endpoint is correct. Remember, domain names are case-sensitive.

* **Adjust Request Parameters**

  For 400 errors, check if the file size is too large (for POST requests) or if there are any other incorrect parameters.

* **Consult API Documentation**

  Always refer to the API's official documentation for specific requirements and troubleshooting tips.

* **Contact API Support**

  If you continue to face issues, reaching out to the API's support team can provide further assistance and insights into resolving the problem.

Understanding these common API error status codes and their solutions can significantly smooth the development process, ensuring more efficient and effective communication between your application and the APIs you rely on.

Final tips

* Always check the API's own documentation, inspect your request, and look up error messages. If the issue persists, contact the API provider.
* Once you fix the issue, your calls should return a `200 OK`, which means everything is working as expected!

---

### Securing Your API Keys in Private API Calls {#securing-your-api-keys-in-private-api-calls}

*Ensuring the security of API keys is a critical aspect of building and maintaining a safe and reliable application. In the realm of private API calls, it's especially important to make sure your API keys are not exposed. This article aims to provide a best-practices guide on where to place your API keys to increase security in a FlutterFlow environment.​*

**Source:** https://docs.flutterflow.io/troubleshooting/api/securing-your-api-keys-in-private-api-calls

Ensuring the security of API keys is a critical aspect of building and maintaining a safe and reliable application. In the realm of private API calls, it's especially important to make sure your API keys are not exposed. This article aims to provide a best-practices guide on where to place your API keys to increase security in a FlutterFlow environment.​

**The Misconception: Private API Calls Secure Everything**

Many users assume that simply marking an API call as 'private' is enough to protect all associated data. However, this is not the case. Private API calls run in a Cloud Function, which means any keys or sensitive data in the body will be secure, as long as they're not passed in from the frontend. Even in private API calls, if you're loading an API key from the frontend (like from Firebase remote configs), then you're still exposing it.​

#### Secure Placement of API Keys in Your Project

The ideal way to secure an API key is to include it in a request header or directly within the API endpoint URL. This ensures that it is never passed in from the client, thereby maintaining its confidentiality.​

For example, you can hard-code the key directly into your API call header like this:​

```
{ "Authorization": "Bearer YOUR_API_KEY_HERE" }
```

Or directly within the API endpoint URL:​

```
https://api.example.com/resource?api_key=YOUR_API_KEY_HERE
```

The key should never be a variable that gets passed in from the frontend, as that would make it accessible via the client-side code, defeating the purpose of using private API calls for secure operations.

#### Verifying the Security of Your API Key

After implementing these changes, a straightforward way to verify that your key is secured is by downloading your application code and checking to make sure the API key doesn’t appear in any frontend files.​

Example: Not Secure

![](https://docs.flutterflow.io/assets/images/20250430121157297846-558fb203f7daca2d47d53c7c2ee5fd77.png)

Example: More Secure

![](https://docs.flutterflow.io/assets/images/20250430121157601185-d840701955c3ab46620abe83a9ff66df.png)

By adhering to these best practices, you can increase the safety of your API keys even while making private API calls.

> **Info:** The goal is to keep all sensitive data, including API keys, away from the client side of the application to ensure optimal security.

​

---

### Custom Domain Connection Error {#custom-domain-connection-error}

*If you encounter the error shown below after clicking Connect, follow these steps to resolve it:*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment-issues/custom-domain-connection-error

If you encounter the error shown below after clicking **Connect**, follow these steps to resolve it:

![](https://docs.flutterflow.io/assets/images/20250430121243410633-49bbbf9e371e3a93e2d327ea974c0f87.png)

Prerequisites

* Access to your domain registrar or DNS provider dashboard.
* DNS management permissions to add or modify DNS records.

**Steps to Resolve the Error:**

1. **Verify DNS Records**

   * Ensure that you have correctly configured the DNS records required for your custom domain connection.

   * Add the keys provided by FlutterFlow to your domain’s DNS settings.

     note

     For A records, if your DNS provider requires a name, you can use `"@"`. When you see an empty value, it typically refers to `"@"`.

     ![](https://docs.flutterflow.io/assets/images/20250430121243684493-7be68a61e4a14bfdd10b65c006f2def2.png)

2. **Check for Conflicting Records**

   * Review your DNS configuration to ensure there are no extra or unnecessary records that conflict with the FlutterFlow-provided keys.

   * For example, if you already have an A record using `"@"`, remove it to avoid conflicts.

     note

     Before removing any existing DNS records, take screenshots and save them for reference.

     Below are examples of correct configurations in FlutterFlow and your DNS provider:

     ![](https://docs.flutterflow.io/assets/images/20250430121243982678-b87737146da4c860ffe03a1fb4672195.png)

     ![](https://docs.flutterflow.io/assets/images/20250430121244255037-0b78e57dc8fce0a8ff528ae03e8fd28b.png)

     By following these steps, you can ensure your custom domain is connected correctly.

---

### Custom Domain Connection Issues {#custom-domain-connection-issues}

*This article provides solutions for common problems encountered when connecting custom domains.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment-issues/custom-domain-connection-issues

This article provides solutions for common problems encountered when connecting custom domains.

Prerequisites

* Access to your domain registrar or DNS provider dashboard.
* DNS management permissions to add or modify DNS records.
* Familiarity with DNS record types (A, CNAME, CAA).

**Steps to Resolve DNS Record Errors:**

1. **Verify DNS Records**

   * Use tools like **[nslookup.io](https://www.nslookup.io)** to verify that your DNS A and CNAME records match the configuration provided in FlutterFlow.
   * Ensure no conflicting A, AAAA, or CNAME records exist.

   ![](https://docs.flutterflow.io/assets/images/20250430121150651702-795c4d0a85619abadc9fcd060e3c2771.png)

2. **Allow Time for DNS Propagation**

   * DNS updates may take up to 24 hours.
   * Wait at least one hour after making changes before attempting to reconnect your domain.

3. **Retry Connection**

   * After verifying DNS settings and allowing propagation, attempt to reconnect your domain.

4. **Contact Registrar Support If Necessary**

   * If settings are correct and the issue persists after 48 hours, contact your domain registrar to confirm DNS configuration.

**Handling Difficulty Creating DNS Records:**

* Different registrars require different formats for DNS record names: * For root domains (e.g., `example.com`), some require an empty name, others `"@"`, or the full domain name.
  * For subdomains (e.g., `test.example.com`), some require just `"test"`, others `"test.example.com"`.

* Consult your registrar’s documentation for exact instructions.

**Resolving 404 Errors After Domain Connection:**

* Publish the project again after connecting the domain.
* This usually resolves most 404 errors related to domain connections.

**Fixing DNS Restrictions for SSL Certificates:**

1. **Check for CAA Records**

   * Use **[nslookup.io](https://www.nslookup.io/domains/your-site-name/dns-records/caa/)** (replace `your-site-name` with your domain) to check CAA records.

2. **Adjust CAA Records**

   * Add `"letsencrypt.org"` to your allowed certificate authorities.

   * Remove any conflicting CAA records.

     note

     Once CAA records allow `"letsencrypt.org"`, FlutterFlow will be able to generate SSL certificates and complete the domain connection.

If issues persist after following these steps, contact FlutterFlow support via Live Chat or email at <support@flutterflow.io>.

---

### Web Publishing FAQs {#web-publishing-faqs}

*This article provides answers to frequently asked questions related to web publishing.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment-issues/web-publishing-faqs

This article provides answers to frequently asked questions related to web publishing.

Prerequisites

* Basic understanding of FlutterFlow and Flutter web projects.
* Access to FlutterFlow exported web project files.
* Familiarity with web hosting concepts.

- **What certifications does FlutterFlow web hosting comply with?**

  FlutterFlow web hosting runs on Google Compute Engine. For detailed information about compliance and certifications, see **[Google Cloud Compliance](https://cloud.google.com/security/compliance)**.

- **What are the system requirements for self-hosting a FlutterFlow web project?**

  FlutterFlow exports standard Flutter code. To compile and host Flutter web apps yourself, review the **[Flutter Web Deployment Guide](https://docs.flutter.dev/deployment/web)**.

  Compiled Flutter projects produce static files that can be hosted on most web servers without backend technology like Node.js or PHP.

- **Do I need backend technologies to host my FlutterFlow web project?**

  No, compiled Flutter web projects are static content. You can host them on any server capable of serving static files with proper MIME types.

- **What should I consider when hosting on a custom domain?**

  You need to configure DNS settings correctly and ensure SSL certificates are in place for HTTPS. See domain connection guides for more information.

For further questions, contact FlutterFlow support via in-app messenger or email at <support@flutterflow.io>

---

### Codemagic Install Pods Failure {#codemagic-install-pods-failure}

*During Codemagic deployment, errors may occur at the Install Pods step due to iOS dependency conflicts, unstable code branches, or pod version mismatches. This guide outlines steps to identify and resolve these issues effectively.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment/codemagic-install-pods-failure

During Codemagic deployment, errors may occur at the **Install Pods** step due to iOS dependency conflicts, unstable code branches, or pod version mismatches. This guide outlines steps to identify and resolve these issues effectively.

Prerequisites

* You are deploying an iOS app using Codemagic.
* Your project includes custom code or third-party packages.

#### Fix Dependency Conflicts from Custom Code

Custom code or third-party packages may introduce conflicting versions of dependencies that prevent CocoaPods from resolving successfully.

**Steps to Resolve Install Pods Failure:**

* **Check for Dependency Conflicts from Custom Code**; Custom or third-party packages may cause version mismatches with FlutterFlow-supported dependencies.

  * Review documentation to ensure package compatibility.

  * Adjust versions in your `pubspec.yaml` file accordingly.

  * Run:

    ```
    flutter pub get
    ```

    ![](https://docs.flutterflow.io/assets/images/20250430121132533922-3b7325e726f04e089085f7f88e024042.png)

* **Use a Stable GitHub Branch for Deployment**; Deploying from unstable branches can introduce unexpected errors during pod installation.

  * Ensure you're using a branch that passed previous Codemagic deployments.
  * Remove untested or experimental code.
  * Revert or refactor recent commits that might break dependencies.

  ![](https://docs.flutterflow.io/assets/images/20250430121132883140-a6f00f21f57ef2ada91b0b1126ba9db3.png)

* **Fix Pod Version Compatibility Issues**; CocoaPods may fail to resolve dependencies due to incompatible versions or incorrect iOS deployment targets.

  * Update packages like `app_settings` in `pubspec.yaml` to versions compatible with your Flutter version.
  * Raise the iOS minimum deployment target in Xcode if necessary.

  ![](https://docs.flutterflow.io/assets/images/20250430121133219967-a817d6dd70abcb7fc46406c95445af11.png)

Deployment Best Practices

* Confirm dependency compatibility before pushing changes.
* Always deploy from tested GitHub branches.
* Verify your deployment target supports all pods used.

---

### Codemagic Signing Certificate Limit {#codemagic-signing-certificate-limit}

*During iOS deployment, Codemagic attempts to create distribution certificates in your Apple Developer Account. If the maximum number of certificates has already been reached, the build will fail with a certificate creation error.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment/codemagic-signing-certificate-limit

During iOS deployment, Codemagic attempts to create distribution certificates in your Apple Developer Account. If the maximum number of certificates has already been reached, the build will fail with a certificate creation error.

#### Error Message

```
Build failed :|Step 3 script `Fetch signing files` exited with status code 1
Returned 409: There is a problem with the request entity - You already have a current Distribution certificate or a pending certificate request.
```

This message indicates that Codemagic cannot proceed because no additional distribution certificates can be created.

Prerequisites

* You are deploying an iOS app using Codemagic.
* Your Apple Developer Program account is active and linked.

**Steps to Resolve Certificate Limit Error:**

1. **Access Your Apple Developer Account**; Log into your Apple Developer account to manage certificates:

   * Go to the **[Apple Developer Certificates List](https://developer.apple.com/account/resources/certificates/list)**.

2. **Navigate to the Certificates Section**; In the **Certificates, Identifiers & Profiles** section:

   * Click on **Certificates**.
   * Locate all existing **Distribution Certificates**.

3. **Remove Unused or Expired Certificates**; Review and delete any unused, expired, or redundant distribution certificates to free up space.

4. **Re-run Deployment**; After deleting the certificates, initiate the build process again in FlutterFlow. Codemagic will automatically generate a new certificate as needed.

   note

   The deleted distribution certificates will be recreated automatically by Codemagic during the next build.

---

### Download dSYM File from App Store Connect {#download-dsym-file-from-app-store-connect}

*To download the dSYM file from the App Store Connect Developer Console, follow these steps.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment/download-dsym-file-from-app-store-connect

To download the dSYM file from the App Store Connect Developer Console, follow these steps.

Prerequisites

* Access to your Apple Developer account.
* Your app has at least one build uploaded to App Store Connect.

**Steps to Download the dSYM File:**

1. **Sign in** to **[App Store Connect](https://appstoreconnect.apple.com/)** with your Apple Developer account.

2. Open your app.

3. Select a build from the **TestFlight** tab on your project page.

4. Open the **Build Metadata** tab.

5. Under **Include Symbols**, download the dSYM file.

   ![](https://docs.flutterflow.io/assets/images/20250430121257965718-1878d33e7c1b9d3378179fd47de1e14c.png)

   note

   The dSYM file is only available for builds that have been successfully uploaded to App Store Connect and are in a "processing" or "ready for submission" state.

   If the **Download dSYM file** link is not visible, it indicates that the build submission did not complete successfully. In this case:

   1. Redeploy the build to the App Store.

   2. After successful processing, return to the **Build Metadata** tab and download the dSYM file.

      ![](https://docs.flutterflow.io/assets/images/20250430121258232331-c39d5ac905c1a85d35b4487febae227c.png)

---

### ImageNotification Development Team Error {#imagenotification-development-team-error}

*This error occurs when the ImageNotification entitlement is missing in your Apple Developer account. To resolve it, create a new Identifier for ImageNotification in your Apple Developer account.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment/imagenotification-development-team-error

This error occurs when the **ImageNotification** entitlement is missing in your Apple Developer account. To resolve it, create a new Identifier for `ImageNotification` in your Apple Developer account.

Prerequisites

* Access to your **Apple Developer account**.
* Permission to manage **Certificates, Identifiers & Profiles**.

**Steps to Create the Identifier:**

1. Sign in to your **[Apple Developer account](https://developer.apple.com/)**.
2. Navigate to **Certificates, Identifiers & Profiles**.
3. Select **Identifiers**.
4. Click the **Add (+)** button.
5. Choose **App IDs** and click **Continue**.
6. Under **Type**, select **App** and click **Continue**.
7. In the **Description** field, enter `ImageNotification` (case-sensitive).
8. In the **Bundle ID** field, enter your full bundle ID followed by `.ImageNotification` (for example: `com.example.app.ImageNotification`).
9. Click **Continue** and then **Register** to complete the setup.

Once this Identifier is added, the signing process should proceed without requiring a development team selection.

---

### iOS Deployment Authentication Error {#ios-deployment-authentication-error}

*During iOS deployment using Codemagic, an authentication credentials error can occur due to misconfigured or expired API tokens for App Store deployment.*

**Source:** https://docs.flutterflow.io/troubleshooting/apple-store-deployment/ios-deployment-authentication-error

During iOS deployment using Codemagic, an authentication credentials error can occur due to misconfigured or expired API tokens for App Store deployment.

The API token used for App Store Connect may be invalid or expired.

> **Info:** For details on generating valid tokens, see the **[Apple API Token Documentation](https://developer.apple.com/go/?id=api-generating-tokens)**.

Here is the error message:

```
Failed Step: Fetch signing files
GET https://api.appstoreconnect.apple.com/v1/bundleIds?limit=100&sort=name&filter%5Bidentifier%5D=appname.com&filter%5Bplatform%5D=IOS returned 401: Authentication credentials are missing or invalid. Provide a properly configured and signed bearer token, and make sure that it has not expired. Learn more about Generating Tokens for API Requests https://developer.apple.com/go/?id=api-generating-tokens 
```

Prerequisites

* Access to your Apple Developer App Store Connect account.
* Permission to manage API keys under **Users and Access**.

**Steps to Resolve the Authentication Error:**

1. Open **App Store Connect** and navigate to **Users and Access → Keys**.

2. If prompted, click **Request Access**.

3. Select **Generate API Key** or click the **Add (+)** button.

4. In the popup, provide the following details:

   * **Name**: Enter a descriptive name for the API Key.
   * **Access**: Choose the appropriate access level for the key.

5. Click **Generate** to create the API Key.

6. Download the newly created API Key by selecting **Download API Key**.

   note

   If the download option does not appear immediately, refresh the page.

7. In **FlutterFlow**, go to **Settings & Integrations → Deployment**.

8. Under **Private Key**, click **Upload Private Key**, select the downloaded API Key file, and click **Open**.

9. Retry your iOS deployment.

   ![](https://docs.flutterflow.io/assets/images/20250430121336383410-4e20c9a876b7745e7dc870012bb098c6.gif)

> **Note:** If the error persists after completing these steps, contact FlutterFlow support via in-app messenger or email at <support@flutterflow.io>.

---

### App Starts from HomePage in Run Mode {#app-starts-from-homepage-in-run-mode}

*If your app always redirects to the HomePage in Run Mode, even after a previous login, it's likely caused by retained authentication state or cached session data in your browser.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/app-starts-from-homepage-in-run-mode

If your app always redirects to the **HomePage** in **Run Mode**, even after a previous login, it's likely caused by **retained authentication state** or **cached session data** in your browser.

#### Troubleshooting Steps

* Clear your browser cache and history.

  ![How to clear browser cache](https://docs.flutterflow.io/assets/images/20250430121300291232-3cadce68e528afe990e06d47b2558512.png)

* Try a different browser or use incognito/private browsing mode to see if the issue persists.

If the problem continues, consider checking your authentication flow and session management in your app settings.

Reset Authentication State in Run Mode

When using **Run Mode**, FlutterFlow preserves your **authentication state** across sessions. To test your app from a clean state, add a **"Log Out"** button on your HomePage that triggers the `Sign Out` action. This ensures the app starts from the login screen during your next test.

---

### Check Firebase Login Method {#check-firebase-login-method}

*Understanding which authentication method a user has used can be useful for several reasons. For example, it can be leveraged for analytics, user support, and to customize the user's experience based on their login method. This method, however, is specific to Firebase Authentication.​*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/check-firebase-login-method

Understanding which authentication method a user has used can be useful for several reasons. For example, it can be leveraged for analytics, user support, and to customize the user's experience based on their login method. This method, however, is specific to Firebase Authentication.​

In our Flutter app, we can find out which method a user used to authenticate by leveraging Firebase's `User.providerData` property. Let's take a closer look at how this works in the code:

```
import 'package:firebase_auth/firebase_auth.dart';

String getUserSignInMethod() {
  final user = FirebaseAuth.instance.currentUser;
  String signInMethod;

  for (var info in user!.providerData) {
    signInMethod = info.providerId;
  }

  return signInMethod;
}
```

Here's a breakdown of the code:

* We first import the [Firebase Auth](https://pub.dev/packages/firebase_auth) package which gives us access to Firebase's authentication methods.

* Next, we define a function `getUserSignInMethod`. This function will return a string indicating the sign-in method the user used.

* Inside the function, we obtain the current user from FirebaseAuth using `FirebaseAuth.instance.currentUser`.

* We then declare a string `signInMethod` that will store the name of the provider used for sign-in.

* `user.providerData` is an iterable that provides UserInfo for each sign-in method used by the user. We loop over this iterable using a `for` loop.

* In each iteration, we assign the `providerId` to our `signInMethod` string. The `providerId` can be 'google.com' for Google, 'facebook.com' for Facebook, and 'password' for email and password.

* After the loop is done, the function returns `signInMethod` string which indicates the sign-in method the user used.

* The function `getUserSignInMethod()` returns a String value which corresponds to the providerId of the user's sign-in method.

Here are examples of how the return value might look like:

* If the user has signed in using Google, the function will return: **`'google.com'`**

* If the user has signed in using Facebook, the function will return: **`'facebook.com'`**

* If the user has signed in using Email and Password, the function will return: **`'password'`**

  These are the identifiers used by Firebase to represent different sign-in methods. Please thoroughly test this function to ensure it fits your specific requirements

Use Sign-In Method to Drive Dynamic UI in FlutterFlow

In FlutterFlow, if you want to display or use the user's sign-in method in your UI logic (example, showing different UIs for Google vs. email login), you can create a custom function using the `providerId` approach shown in the article and **connect it to a custom action**. This allows you to make dynamic decisions inside your app based on how the user authenticated.

Remember to return the result from the custom function and store it in an App State variable for easy access throughout your app.

---

### Deleting Firebase Users and Related Data {#deleting-firebase-users-and-related-data}

*Understanding the Delete Action*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/deleting-firebase-users-and-related-data

![](https://docs.flutterflow.io/assets/images/20250430121300815719-93473f2543e01b1e4fb75bce9e5dd145.png "Screenshot showing the delete user action")

#### Understanding the Delete Action

The delete action in Firebase is designed to remove the user from the authentication table only. This means the user's document in the database will not be affected. If you want to delete the user's document from the database as well, you'll need to create a custom action with some custom code.

##### Logging Out After Deletion

After completing the delete action, it is important to log out the user. Since the user no longer exists in the authentication system, logging out ensures the app routes the user back to the login page, which is typically the initial page of your project.

#### Steps for Proper User Deletion

1. **Delete related data first:**; Before calling the delete user action, delete any related data such as Firestore documents or Storage files associated with the user. Once the user is deleted from Firebase Auth, their UID will no longer be accessible in the app session, making it difficult to reference their data afterward.

2. **Handle re-login behavior:**; Keep in mind that if the same user signs in again using the same signup method, Firebase will create a new document in the database for them. This happens because Firebase links the new login information to the old user document.

Important Tips for Deleting Users

* Always delete associated user data from Firestore or Storage **before** deleting the user from Firebase Auth. This prevents orphaned data and issues with data referencing.
* Remember that after deletion, the user will need to be logged out to avoid session errors.
* If the user signs in again with the same signup method, Firebase creates a new document for them, reconnecting the new login to the old user document.

![](https://docs.flutterflow.io/assets/images/20250430121301101693-de232395e419de0c7398095f4c145d23.png "Screenshot illustrating user deletion flow")

> **Note:** The delete user action in FlutterFlow performs the same operation as manually deleting a user from the Firebase Authentication table.

---

### Fix Google Sign-In Issues {#fix-google-sign-in-issues}

*If Google Sign-In isn’t working after exporting your FlutterFlow app, follow these steps based on how you’re deploying your app.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/fix-google-sign-in-issues

If Google Sign-In isn’t working after exporting your FlutterFlow app, follow these steps based on how you’re deploying your app.

1. **If Deployed to the Play Store via CodeMagic**

   If you published your app to the Play Store using FlutterFlow's CodeMagic integration:

   * In the **Google Play Console**, open your app from the **All apps** list.
   * Go to **Setup → App Integrity**.
   * Under the **App Signing** tab, copy the **SHA-1 certificate fingerprint**.

   ![](https://docs.flutterflow.io/assets/images/20250430121440426479-9f2c4340a46f05d29580a4763c4ba7f3.png)

   * In the **Firebase console**, open the same project, scroll to **Your Apps**, and select your Android app.
   * Click **Add fingerprint**, paste the SHA-1, then click **Save**.

   ![](https://docs.flutterflow.io/assets/images/20250430121441325585-013b7c6532c00e98fee3f90c4d1f4fbd.png)

   * In FlutterFlow, go to **Settings → Firebase** and click:
   * **Regenerate Config Files**
   * **Generate Files**

   ![](https://docs.flutterflow.io/assets/images/20250430121442125737-992a83c99d1aaac98c6db7838fa1782e.png)

   Re-test your app. Google Sign-In should now work correctly.

2. **If Not Yet Published or Using Manual Signing**

   If you’re not using Play Store App Signing:

   * Use **Keytool** or **Gradle's Signing Report** to generate your SHA-1.
   * In **Firebase**, open your project settings.
   * Under **Your Apps**, select the Android app and add the SHA-1 fingerprint.

   ![](https://docs.flutterflow.io/assets/images/20250430121442863891-013b7c6532c00e98fee3f90c4d1f4fbd.png)

   * In FlutterFlow, go to **Settings → Firebase**, then:
   * **Regenerate Config Files**
   * **Generate Files**

   ![](https://docs.flutterflow.io/assets/images/20250430121443525154-992a83c99d1aaac98c6db7838fa1782e.png)

   Test the app again to confirm Google Sign-In works.

   *Refer to the [Google Play Services documentation](https://developers.google.com/android/guides/overview) for more information.*

Add Debug SHA-1 for Local Testing

* When testing Google Sign-In in FlutterFlow before publishing, add your **debug SHA-1** in Firebase.
* Then go to `Settings → Firebase` in FlutterFlow and regenerate your config files.

---

### Permission Denied: Code 403 {#permission-denied-code-403}

*This error typically occurs when your application or service account does not have the required permissions to access a resource in Google Cloud or Firebase.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/permission-denied-code-403

This error typically occurs when your application or service account does not have the required permissions to access a resource in Google Cloud or Firebase.

#### Code 403 Error Message

You may encounter this error due to one or more of the following reasons:

* **Invalid or misconfigured service account JSON file**
* **Insufficient permissions** assigned to the service account
* **Missing or incorrect IAM roles** for the service account
* **API not enabled** in the Google Cloud project

Do the following to fix this error:

* **Check Your Service Account JSON File**

  Ensure you are using the correct `service-account.json` file and that it is not corrupted or expired.

* **Verify IAM Roles and Permissions**

  Make sure the service account has the necessary roles like `Editor`, `Owner`, or other specific roles required for your use case.

* **Enable Required APIs**

  Go to the [Google Cloud Console](https://console.cloud.google.com/apis/library) and ensure all necessary APIs are enabled for your project.

* **Regenerate the Service Account Key if Needed**

  If you suspect the key is invalid, generate a new one and update your application configuration accordingly.

Always Use Least Privilege Principle

When assigning IAM roles to your service account, follow the **principle of least privilege**—only grant the minimum permissions necessary for the task. This not only reduces the risk of misconfiguration but also enhances the overall security posture of your app.

If you continue to experience issues, consult the [Google Cloud IAM documentation](https://cloud.google.com/iam/docs/troubleshooting-access) or contact [FlutterFlow Support](mailto:support@flutterflow.io) for further assistance.

---

### SafetyNet Phone Sign-In Issue on Android Devices {#safetynet-phone-sign-in-issue-on-android-devices}

*If you're experiencing issues with Firebase Phone Authentication on Android devices, especially when using emulators or testing in release mode, this guide will help you identify and resolve common problems.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/safetynet-phone-sign-in-issue-on-android-devices

If you're experiencing issues with Firebase Phone Authentication on Android devices, especially when using emulators or testing in release mode, this guide will help you identify and resolve common problems.

Firebase uses either **SafetyNet** or **reCAPTCHA** to verify that phone number sign-in requests originate from your app. Issues typically arise when one of these verification methods is not correctly configured.

#### Troubleshooting Checklist

Ensure the following configurations are in place:

* **Firebase Setup**

  * Your project is correctly set up in the [Firebase Console](https://console.firebase.google.com/).
  * Firebase Authentication is enabled.
  * The Phone Sign-In method is activated.

* **Phone Authentication Flow**

  * Prompt the user to enter their phone number.
  * Send a verification code to the user's phone.
  * Accept and verify the code entered by the user.

* **SafetyNet / reCAPTCHA Configuration**

  * Your app includes the required Firebase and Play Services dependencies.
  * SHA-1 and SHA-256 fingerprints are added to your Firebase project settings.
  * Your API key is either unrestricted or allowlisted.

* **Testing Environment**

  * If you're using an emulator, test on a physical device instead. Emulators may bypass or fail certain integrity checks.

#### Firebase Verification Methods

Firebase uses one of the following methods to confirm the authenticity of phone sign-in requests:

1. **SafetyNet (Deprecated)**

   If the device supports Google Play Services, Firebase uses **SafetyNet Attestation** to confirm the device’s legitimacy.

   Deprecated API

   The SafetyNet Attestation API is deprecated and has been replaced by the [Play Integrity API](https://developer.android.com/google/play/integrity). After **January 31, 2023**, you can no longer enable the SafetyNet API for new projects in the Google Cloud Console.

   To use SafetyNet (if still active for your project):

   * Enable **Android Device Verification (Deprecated)** in the [Google Cloud Console](https://console.cloud.google.com/).
   * Ensure your app's **SHA-256** is added in the Firebase Console under **Project Settings > General > Your Apps**.
   * Use the default Firebase API key or request onboarding for SafetyNet if needed.
   * Monitor your quota [here](https://developer.android.com/google/play/safetynet/quotas).

   ![](https://docs.flutterflow.io/assets/images/20250430121259958091-c6869a1ed27cc114df371bef037c90f6.png)

2. **reCAPTCHA Verification**

   If SafetyNet is unavailable (e.g. device without Google Play Services or running on an emulator), Firebase falls back to **reCAPTCHA verification**.The reCAPTCHA challenge usually completes without user interaction. This flow requires:

   * A valid **SHA-1** fingerprint added to your Firebase project.
   * An **unrestricted** or **domain-allowlisted** API key (e.g. `your-project-name.firebaseapp.com`).
   * Ensure both SafetyNet and reCAPTCHA flows are working to support a wider range of Android devices.

Release Mode Configuration

When releasing your app to the Google Play Store, ensure you include the **SHA-1** and **SHA-256** keys from your **Play Console**. Here is how to do that:

* Navigate to **Play Console → Your App → Release → Setup → App Signing**
* Then copy both **SHA-1** and **SHA-256** fingerprints and add them to Firebase Console under **Project Settings > General > Your Apps**.

![](https://docs.flutterflow.io/assets/images/20250430121300291238-1e1512108bd55771c4c7bc2f003507bd.png)

Learn more

* [Firebase Phone Authentication (FlutterFire)](https://firebase.flutter.dev/docs/auth/phone/)
* [Using Firebase Auth in FlutterFlow](https://docs.flutterflow.io/authentication)
* [Play Integrity API Migration](https://developer.android.com/google/play/integrity)

Still stuck? Check Firebase logs, test on a physical device, and ensure your API keys and fingerprints are correctly added. Proper configuration of SafetyNet or reCAPTCHA is critical to ensuring phone number sign-in works reliably across devices.

---

### Sign in With Apple (for Web) {#sign-in-with-apple-for-web}

*To enable Sign in with Apple on the web, you must complete additional steps in both your Apple Developer Account and Firebase Console. These steps allow Apple to identify your website and authorize the use of Apple login on web platforms.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/sign-in-with-apple-for-web

To enable **Sign in with Apple** on the web, you must complete additional steps in both your **Apple Developer Account** and **Firebase Console**. These steps allow Apple to identify your website and authorize the use of Apple login on web platforms.

> **Warning:** The **Sign in with Apple (Web)** functionality cannot be tested in Test/Run Mode. You must **deploy** your app to a live domain before testing.

Take the following steps to set up Sign in with App (for Web):

1. **Configure Apple Developer Account**

   Follow these steps in your [Apple Developer Account](https://developer.apple.com/account/):

   1. **Register a New Identifier**

      * Select **App IDs** and fill in the required details.
      * Enable the **Sign in with Apple** capability.

   2. **Create a New Service ID**

      * Provide a name and a unique identifier.
      * This will be used as the **Service ID** in Firebase.

   3. **Configure Sign in With Apple**

      * Add your domain and return URL (from Firebase).
      * Save the configuration.

   4. **Create a New Key**

      * Enable **Sign in with Apple**.
      * Download the generated private key (`.p8` file).

2. **Set Up in Firebase Console**

   After downloading the private key, configure your Firebase app by doing the following:

   1. Go to **Authentication → Sign-in method → Apple**.

   2. Enter the following details: * **Apple Team ID**
      * **Key ID**
      * **Private Key** (from the `.p8` file)

   3. Set the **Service ID** to match the one created in the Apple Developer account.

   Once these steps are completed, your **Sign in with Apple (Web)** setup should be active.

Still Not Working?

If the sign-in process fails after completing these steps, please contact [FlutterFlow Support](mailto:support@flutterflow.io) via Chat or Email.

Helpful Resources

* [Apple Developer - Sign in with Apple](https://developer.apple.com/sign-in-with-apple/)
* [Firebase Authentication - Apple Provider](https://firebase.google.com/docs/auth/web/apple)
* [FlutterFlow Authentication Docs](https://docs.flutterflow.io/authentication)

---

### Troubleshooting Custom Authentication {#troubleshooting-custom-authentication}

*- Ensure you have a custom server with login and sign-up endpoints that return a JWT token upon success.*

**Source:** https://docs.flutterflow.io/troubleshooting/authentication/troubleshooting-authentication

Prerequisites

* Ensure you have a **custom server** with login and sign-up endpoints that return a JWT token upon success.
* **Custom authentication** must be enabled in FlutterFlow, with entry and logged-in pages correctly set.

Here's an example:

![](https://docs.flutterflow.io/assets/images/20250430121149388590-eb05f8e20642cd740ae49b917fb2a8ab.png)

#### How to Fix Custom Authentication Issues

1. **Verify Server and API Endpoints**

   * Confirm that your server correctly returns JWT tokens for login and sign-up requests. The server's response should include the **authentication token**, **refresh token**, **expiration time**, and **user ID (UID)**.
   * Double-check the API endpoint configurations in FlutterFlow to ensure they match your server’s requirements.

2. **FlutterFlow Configuration**

   * Make sure **Custom Authentication** is enabled in your project settings.
   * Verify that the **Entry Page** and **Logged In Page** are correctly set.

3. **UI Configuration**

   * Ensure your app includes the essential pages for the authentication flow: **Login**, **Sign Up**, and **Home Page** (the page shown when a user is authenticated).

4. **API Integration and Authentication Flow**

   * Test API calls from FlutterFlow to your custom server to confirm responses are working as expected.
   * Use the **Backend Call** action to trigger login/signup, then handle the **Custom Login** action using the response data.

5. **Handling Tokens and User Data**

   * Parse the API response properly to extract and store: * `auth token`
     * `refresh token`
     * `expiration time`
     * `user ID (UID)`

   * Store these values in local state or secure app storage.

![](https://docs.flutterflow.io/assets/images/20250430121149749937-2f080ea6b813107d114451f2edd8ffa4.png)

6. **Navigation**

   * If navigation does not occur automatically after login/signup: * Disable automatic navigation.
     * Use a **manual navigation** action to route users to the appropriate page.

General Tips

* Test your flow with **dummy credentials** before using real user data. This helps debug token handling, API responses, and navigation.
* Add **logging** on both the server and in FlutterFlow (example, using snack bars or alerts) to monitor each step of the flow.
* Verify the full flow—from login to protected pages—to ensure everything works as expected.

More Resources

* [FlutterFlow Custom Authentication Video](https://www.youtube.com/watch?v=hnX3CvBtGvI)
* **Sample project:** [Custom Auth Checklist](https://app.flutterflow.io/project/custom-auth-checklist-fdjkno)
* [FlutterFlow Custom Authentication Documentation](https://docs.flutterflow.io/data-and-backend/custom-authentication)

---

### ListView Gray Box and Red Screen Errors {#listview-gray-box-and-red-screen-errors}

*When loading a list of items from the database, you might encounter a gray box or red error screen. This article explains the possible causes and how to resolve them.*

**Source:** https://docs.flutterflow.io/troubleshooting/backend/listview-gray-box-and-red-screen-errors

When loading a list of items from the database, you might encounter a gray box or red error screen. This article explains the possible causes and how to resolve them.

Prerequisites

* Ensure your query is correctly connected to a Firestore collection or CMS.
* Confirm that your app builds and runs correctly in **Run** and **Test** modes.

**Understanding the Error:**

A **gray box** usually indicates that the backend query failed to return results. A **red screen** in Test mode suggests a runtime error caused by invalid data or query failure.

**Step-by-Step Troubleshooting:**

1. **Verify Query Results**

   * If the query is successful and returns items, the list will populate as expected.
   * If there are no records matching the query, you will see the **empty state** you configured.
   * If the query fails, a gray box (in Run mode) or a red error screen (in Test mode) will appear.

   ![Empty State](https://docs.flutterflow.io/assets/images/20250430121239249713-c31c0a76d2143af7fdcaeccc648d63b0.png)

   tip

   Always configure an empty state for lists. This helps distinguish between a failed query and an empty dataset.

2. **Behavior by Mode**

   * **Run mode**: Displays a gray box when the query fails.

   * **Test mode**: Shows a red screen with a specific error message.

     **Example: Working Query with No Results**; ![Working Query](https://docs.flutterflow.io/assets/images/20250430121239492027-aa83575a453036ca7dec97a5c5d07c0f.png)

     **Example: Failed Query**; ![Failed Query](https://docs.flutterflow.io/assets/images/20250430121239708989-9f07c45b1dd9e9906e2fe6f44ce93fa5.png)

3. **Check for Null Values in the Data**

   Null values in critical fields may cause queries or widgets to fail.

   Here is how to check for null values:

   1. Inspect your data in **Firebase** or **CMS** for any fields with `null` values.
   2. Pay attention to fields used in filters, formatting, or conditional visibility.
   3. For example, if `created_time` is null and you are formatting a date from this field, the query may fail.

   **Example: Null Field Causing Error**

   ![Null Field Example](https://docs.flutterflow.io/assets/images/20250430121240227391-6af12dfe0048a0ac5e35266444292525.png); ![Date Formatting Error](https://docs.flutterflow.io/assets/images/20250430121240508011-5f32e3b00fe8ffad5396024a01edb6e4.png)

   note

   Use **visibility rules** to hide widgets that depend on potentially null values.

4. **Handle Document-From-Reference Queries Safely**

   If you use document references inside a list item widget, and the reference is null or missing, it will break the query.

   ![Broken Reference Example](https://docs.flutterflow.io/assets/images/20250430121240818334-9d09c42d5d3bc820c9cbae3b3bdb69d9.png)

   note

   Always add a visibility rule to any widget performing document-from-reference queries. This ensures the widget is only visible when the reference is valid.

Summary

* A **gray box** means the backend query failed.
* A **red screen** indicates a runtime error in **Test mode**.
* **Null values** in your database are a common cause of failure.
* Always configure **empty states** and apply **visibility rules** to handle null or missing data gracefully.

---

### Fix ListView Only Returning One Item {#fix-listview-only-returning-one-item}

*If your ListView is only showing one item, this guide will walk you through the common reasons and how to resolve the issue.*

**Source:** https://docs.flutterflow.io/troubleshooting/backend/listview-returning-only-one-item

If your **ListView** is only showing one item, this guide will walk you through the common reasons and how to resolve the issue.

Prerequisites

* A working Firebase or CMS integration.
* A dynamic layout widget such as `ListView`, `GridView`, or `Column`.
* At least two documents in your Firestore collection for testing.

Follow the steps below to resolve the issue:

1. **Use a Dynamic Widget**; Make sure you're using a widget like `ListView`, `GridView`, or `Column` that supports dynamic content.

2. **Confirm the Query Type**; Ensure the query is set to return a **list of documents**, not a single document.

3. **Review Applied Filters**; If you are using filters, check that multiple records in your database satisfy those filter conditions.

4. **Check Firestore Data**; Open your Firestore collection and verify that it contains **multiple records**.

5. **Verify List Type Fields**; If querying a single field, confirm it's defined as a **List** in both Firebase and FlutterFlow.

> **Tip:** To test your setup, remove all filters temporarily and use a basic list query. This helps isolate whether the issue is with filtering or the query type.

---

### Resolving Firebase Configuration Issues {#resolving-firebase-configuration-issues}

*If you're experiencing backend errors, failed schema validation, or data sync issues, this guide will help you verify and fix your Firebase setup in FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/backend/resolving-firebase-configuration-issues

If you're experiencing backend errors, failed schema validation, or data sync issues, this guide will help you verify and fix your Firebase setup in FlutterFlow.

Prerequisites

* You must have already connected your Firebase project to FlutterFlow.
* You should have access to your Firebase console with admin rights.

Follow the steps below to fix firebase configuration:

1. **Grant Required Permissions**

   Assign the following permissions to `firebase@flutterflow.io` in your Firebase project:

   * Editor
   * Cloud Functions Admin
   * Service Account User

   Learn how to **[assign Firebase permissions](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project)**.

2. **Update Firestore Rules**

   Update your Firestore security rules to allow access for FlutterFlow.

   After making changes:

   * Remove `firebase@flutterflow.io` from your authenticated users.
   * Redeploy your Firestore rules.
   * Validate your schema again.

   ![](https://docs.flutterflow.io/assets/images/20250430121532523511-793bd6baac529fb45002bc73df1636a0.png)

3. **Match Field Types and Names**

   Check that data field types and names match between Firestore and FlutterFlow exactly. Mismatches will cause query errors.

4. **Validate Firestore Schema in FlutterFlow**

   Use the **Validate** button under **Firestore → Settings** in FlutterFlow to confirm that your collection schema matches your Firestore structure.

   ![](https://docs.flutterflow.io/assets/images/20250430121532793176-81306c33ba320ea521aa4a3b4a8d6803.png)

5. **Reset Firebase Setup (If Needed)**

   If issues persist after following the steps above:

   * Revoke the current setup.
   * Reconnect your Firebase project using the **[Firebase setup instructions](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)**.

6. **Add Authorized Domains**

   In the Firebase console, go to **Authentication → Sign-in Method → Authorized Domains** and add: `app.flutterflow.io`

7. **Refresh FlutterFlow**

   Make sure you're using the latest version of the platform:

   * Press `Ctrl`/`Cmd + Shift + R`
   * Clear your browser cache
   * Log out and back in to FlutterFlow

8. **Upgrade to Blaze Plan (If Using Cloud Functions)**

   Cloud Functions such as Push Notifications and Payments require a billing-enabled Firebase project. Make sure you’re on the **Blaze Plan**.

> **Tip:** After updating Firestore rules, always validate the schema using the **Validate** button before proceeding with other fixes.

---

### Update Document Action Fails During Backend Call {#update-document-action-fails-during-backend-call}

*When performing the Update Document action, you may encounter a situation where the loading indicator appears but then stops without completing the action. This indicates that the update was unsuccessful. If the update succeeds, the next steps in your action flow, such as displaying an alert dialog, should execute automatically.*

**Source:** https://docs.flutterflow.io/troubleshooting/backend/update-document-action-fails-during-backend-call

When performing the **Update Document** action, you may encounter a situation where the loading indicator appears but then stops without completing the action. This indicates that the update was unsuccessful. If the update succeeds, the next steps in your action flow, such as displaying an alert dialog, should execute automatically.

![](https://docs.flutterflow.io/assets/images/20250430121241690449-72728d8ac64b57f905a10b2867d628dc.gif)

![](https://docs.flutterflow.io/assets/images/20250430121241899370-d79442f878599856692251154e0ddb36.png)

> **Note:** After performing the update action, always verify that the data has been correctly updated in your database. If your document is not streamed in real-time within your app, the updated data may not immediately appear. Check the data in FlutterFlow CMS or directly in Firebase to confirm the update.

**Causes of Document Update Failures:**

When the update action fails, the action flow stops, preventing any subsequent actions from executing.

There are two common reasons why the update action may fail:

* **Permission Issue in Firestore**

  The user may not have the necessary permission to write to the document.

  ![](https://docs.flutterflow.io/assets/images/20250430121242149430-fd479a11417ff877bd79c30bd2bb66d2.png)

  **Cause:**; The Firestore security rules may not allow the current user to write (edit) documents.

  **Solution:**; Review and configure your Firestore rules to grant write permission. For example, allowing write access to authenticated users is often sufficient if your app requires user authentication.

* **Data Type Mismatch**

  The values you are attempting to write may not match the expected field types.

  For example, assigning a string value to a field that expects an integer will result in failure.

  ![](https://docs.flutterflow.io/assets/images/20250430121242530889-edd1b26adbf2601edf31c23cf3647e94.png)

  **Cause:**; Attempting to write a value of the wrong type, such as assigning text to a number field.

  **Solution:**; Verify that the values being written match the expected data types for each field. If the data comes from an API call or form input, consider using custom actions to convert the value to the appropriate type before performing the update.

  note

  If you want to save a text field value as a number, ensure that the text field input type is set to **Number**.

Additional Troubleshooting

You can check for error details in your browser's developer console (F12). For example, permission errors will typically appear in the console logs, as shown below:

![](https://docs.flutterflow.io/assets/images/20250430121242814005-79f185001a0291f523c966be512c7557.png)

---

### Fix Cloud Functions Deployment {#fix-cloud-functions-deployment}

*- You must have a Firebase project connected to FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/cloud-functions/fix-cloud-functions-deployment

Prerequisites

* You must have a Firebase project connected to FlutterFlow.
* Ensure your project is on the Blaze Plan.

Cloud Functions allow you to execute backend code in response to events triggered by Firebase features or HTTPS requests. Various situations might cause Cloud Functions to malfunction, often stemming from setup problems or coding mistakes within the Cloud Function's script.

This article guides you through common challenges with Cloud Functions in FlutterFlow and how to resolve them.

**Errors Shown in FlutterFlow Builder**

You may encounter the following errors in the FlutterFlow Builder:

* `Out of Date (Error)`
* `Not Deployed (Error)`

These errors can arise from various situations. Below are screenshots of these errors:

**Out of Date Error**

![](https://docs.flutterflow.io/assets/images/20250430121126719355-82d03fcbe771f63c6224d5397506917a.png)

**Not Deployed Error**

![](https://docs.flutterflow.io/assets/images/20250430121126936614-d515543411b3756f0ff1a0e03156dfb0.png)

#### Key Checks for Resolving Deployment Errors

1. **Verify <firebase@flutterflow.io> Has Necessary Permissions**

   To ensure FlutterFlow works smoothly with your project, ensure that `firebase@flutterflow.io` has the following permissions in your Firebase project:

   * Cloud Functions Admin
   * Editor
   * Service Account User

   Follow the steps below to add these permissions:

   * Go to the Firebase Console and log into your account.

   * Open your project and go to **Project Settings > Users and Permissions**.

   * Under **Advanced Settings Permissions**, locate `firebase@flutterflow.io`, click **Edit**, and add the required roles.

     ![](https://docs.flutterflow.io/assets/images/20250430121127218829-addc39229a055565157b00d29fa41251.png)

     ![](https://docs.flutterflow.io/assets/images/20250430121127501343-5f6dbb7491d1ddb5d008eb09a0d39245.png)

2. **Check for Function Name Mismatch**

   Ensure the function name in your code exactly matches the function name defined in FlutterFlow.

   For example, in this case, FlutterFlow expects `logoMaker`, but the code incorrectly uses `data`.

   ![](https://docs.flutterflow.io/assets/images/20250430121133833159-5303c0c6008b98cba4972c4d28150935.png)

3. **Validate Custom Code for Cloud Functions**

   Small mistakes in your custom Cloud Functions code can prevent deployment.

   * Double-check your code for errors.

   * Test locally using an IDE or Firebase CLI.

     ![](https://docs.flutterflow.io/assets/images/20250430121127844921-2a56c94139ae832cc5f01f809a6a424c.png)

4. **Verify Firebase Billing Plan (Blaze Plan Required):**

   * Ensure your Firebase project is on the **Blaze Plan**, not Spark Plan.
   * Check billing status on GCP. Even if Firebase shows Blaze, GCP billing issues may still block deployments.

5. **Check if Other Cloud Functions Are Deploying:**

   * If some Cloud Functions (like Push Notification or Stripe) are deploying successfully, it indicates your Firebase setup is mostly correct.
   * Focus on inspecting your specific function code and configuration.

6. **Ensure Region Selection Matches Firebase Project:**

   * The region set for your Cloud Function in FlutterFlow should match your Firebase project's region.

   * Do not leave the region as `[default]`.

     ![](https://docs.flutterflow.io/assets/images/20250430121128170242-7e143cda4b0438bc0763b049bb4e6ba1.png)

     ![](https://docs.flutterflow.io/assets/images/20250430121128453683-c8ce143b6022ca86729958388bf01ca9.png)

   tip

   If you previously deployed functions in the wrong region, delete them, set the correct region, and re-deploy.

7. **Protocol Conflicts: HTTP vs Callable Functions**

   If you initially deployed a function as HTTP and later try to redeploy it as Callable (or vice versa), you'll get this error:

   `[makeUserAdmin(us-central1)] Changing from an HTTPS function to a callable function is not allowed. Please delete your function and create a new one instead.`

   Follow the steps below to fix this error:

   * Delete the existing function in Firebase Console.
   * Modify the protocol type in FlutterFlow.
   * Redeploy the function.

8. **Verify `package.json` Integrity**

   * Use the generated `package.json` file as-is unless you need to add extra packages.

   * Ensure it’s not blank and doesn’t contain invalid characters.

     **Recommended structure:**

     ```
     {
     "name": "functions",
     "description": "Firebase Custom Cloud Functions",
     "engines": {
         "node": "18"
     },
     "main": "index.js",
     "dependencies": {
         "firebase-admin": "^11.8.0",
         "firebase-functions": "^4.3.1"
     },
     "private": true
     }
     ```

9. **Ensure Packages Are Included in `package.json`**

   If you are using third-party packages (e.g., `axios`), make sure they are properly added to the `dependencies` section in `package.json`:

   ![](https://docs.flutterflow.io/assets/images/20250430121128741407-9e4e60bdb55bc4f475e16ffc418576dd.png)

10. **Validate Third-Party Package Versions**

    The versions specified in your `package.json` should match available versions listed on **[npmjs.com](https://www.npmjs.com/package/axios?activeTab=versions)**.

    ![](https://docs.flutterflow.io/assets/images/20250430121129014430-550f4af2873fbfeab570f5289e3f4cc0.png)

11. **Check for Undeployed Firebase Rules and Indexes:**

    * Incomplete Firestore rules or indexes can block function deployment.
    * Make sure all rules and indexes have been deployed from FlutterFlow.

**Additional Troubleshooting and Optimization:**

* **Trigger Configuration Issues**

  If your Cloud Functions are not being triggered:

  **Review Event Triggers:**

  * For Firestore triggers: verify document paths and collection names.
  * For HTTP functions: ensure correct setup in FlutterFlow.

  **Check Permissions and Rules:**

  * Firebase security rules and project permissions must allow the Cloud Function operations.

* **Execution Timeouts**

  * Cloud Functions may fail if execution time exceeds limits.

  * Set a custom timeout duration in FlutterFlow:

    ![](https://docs.flutterflow.io/assets/images/20250430121134186956-dd7a3ea01e0cbbd3b9e85a7913ce88f4.png)

    For longer processing tasks, increase the timeout duration in your Cloud Function configuration.

    Configuring Cloud Function regions in FlutterFlow can also optimize performance:

    ![](https://docs.flutterflow.io/assets/images/20250430121134509618-5cc01a26e7e36f1760c722f41c26a33a.png)

    note

    Longer timeouts may increase Firebase costs.

* **Cold Start Delays**

  Cloud Functions may respond slower after periods of inactivity:

  * Use **Cloud Scheduler** to periodically invoke functions and keep them warm.
  * Minimize dependencies to reduce cold start delays.

Following this comprehensive troubleshooting guide should help you resolve most issues encountered when working with Cloud Functions.

---

### Custom Actions Errors {#custom-actions-errors}

*- A basic understanding of how custom actions work.*

**Source:** https://docs.flutterflow.io/troubleshooting/custom-actions/custom-actions-errors

Prerequisites

* A basic understanding of how custom actions work.
* A FlutterFlow project with a custom action already created.

Custom actions are powerful, but troubleshooting them can be tricky. This guide will help you systematically resolve common issues.

* **Read the Error Message**

  Always read the error message printed during test mode, compilation, or local build. The message often provides a clue about the potential issue.

* **Common Troubleshooting Checklist**

  * **Action Name Mismatch**

    Ensure the name in the action matches the custom action in your code.

    ![](https://docs.flutterflow.io/assets/images/20250430121138021235-b2a84894e26e51c308d8165327e7429c.png)

    tip

    Use the `Add BoilerPlate Code` option to generate code with the correct action name.

  * **Imports and Arguments**

    * Check that all required imports are present.

    * Ensure arguments are defined in both the action settings and your code.

      ![](https://docs.flutterflow.io/assets/images/20250430121138830209-e031679e2bcca11bc6ec7ce09fe26dbe.png)

      Example:

      * Argument 1: Missing definition in settings panel

      * Argument 2: Correctly imported

      * Argument 3: Nullable selected, but not specified as nullable in code

        Follow the steps below to fix this issue:

        1. Manually update arguments in both the settings panel and your code.
        2. Use the `Add BoilerPlate Code` option (on web, copy only what you need; on desktop, it may replace all code).

        ![](https://docs.flutterflow.io/assets/images/20250430121139816551-758c54ef51a14b4f6fc2012ea6588d24.gif)

  * **Name Conflicts**

    * Avoid using the same name for an action and its argument.

      ![](https://docs.flutterflow.io/assets/images/20250430121142594662-94f9b7f5c350fec098cb25851c074efc.png)

  * **Reserved Keywords**

    * Do not use Dart/Flutter reserved keywords as argument names. **Examples:** `abstract`, `else`, `import`, `show`, `as`, `enum`, `in`, `static`, `this`. *FlutterFlow usually warns you, but double-check!*

  * **Return Type Mismatch**

    * Ensure the custom action returns the correct data type as defined in the settings.

      ![](https://docs.flutterflow.io/assets/images/20250430121143268592-1f07b2e96bfa688e76f7e800463421b9.png)

      *The function should return the type specified in the settings panel.*

  * **Internal Library Imports**

    * If importing internal libraries (example, `../../flutterflow`), set **Exclude from compilation** to `true` if needed.

  * **Pubspec Dependencies**

    * Ensure your dependencies are declared in your code and are compatible with FlutterFlow.

      ![](https://docs.flutterflow.io/assets/images/20250430121143614166-de2881be9794e6225e63e65781a10a65.png)

      Check for:

      * Version conflicts (check on **[pub.dev](https://pub.dev)**)

      * Multiple versions of the same dependency

      * Conflicts with FlutterFlow's auto-imported dependencies

        ![](https://docs.flutterflow.io/assets/images/20250430121143935249-28fbc1d922eb729fa65f328f42233253.png)

        ![](https://docs.flutterflow.io/assets/images/20250430121144228150-4b655f3fe4751bc7cf795ca8a02bd9e5.png)

  * **Code Errors:**

    * **Null values:**

      Handle null values safely.

      ```
      int example = passingIntWhichMayBeNullable ?? 0;
      ```

    * **Correct data types:**

      Convert data types explicitly.

      ```
      String str = "5";
      int result = int.parse(str); // ✅
      ```

      Use `.toString()`, `.toInt()`, `.toDouble()` as needed.

    * **Single elements** vs **arrays:**

      Ensure you are not passing a single element where a list is expected, or vice versa.

  * **Exclude from Compilation**

    If this option is enabled, the code won’t be checked during build but can still run during test..

    ![](https://docs.flutterflow.io/assets/images/20250430121144509497-570186a33271937e74fe0b06fe081a55.png)

  * **Duplicate Data Types/Structs**

    Do not redefine data types or structs already defined in the data schema panel.

    ![](https://docs.flutterflow.io/assets/images/20250430121144853131-5e03acb547d4795fece1d7396bf9848c.png)

  * **Callback Data Types**

    Ensure callback actions return the correct data type.

    ![](https://docs.flutterflow.io/assets/images/20250430121145202849-bb345fa114bbdf9028e9ac06984923fc.png)

Additional Resources

* **Debugging with the Browser Console:** Use the browser debug console for logic errors.
* **FlutterFlow University Video**: [Custom Actions Video](https://www.youtube.com/watch?v=rKaD9eKuZkY).
* **Official Docs:** [Custom Actions | FlutterFlow Docs](https://docs.flutterflow.io/concepts/custom-code/custom-actions)

> **Tip:** When in doubt, regenerate the boilerplate and compare with your code. Consistency between settings and code is key!

---

### Testing Custom Actions using Debug Console {#testing-custom-actions-using-debug-console}

*Sometimes, the compiler does not show any errors in the custom action, but the custom action still won't work as expected. This might be due to the code logic or the implementation. In order to test the implementation and the flow, you can use the debug console to test the custom action in different scenarios.*

**Source:** https://docs.flutterflow.io/troubleshooting/custom-actions/testing-custom-actions-using-debug-console

Sometimes, the compiler does not show any errors in the custom action, but the custom action still won't work as expected. This might be due to the code logic or the implementation. In order to test the implementation and the flow, you can use the debug console to test the custom action in different scenarios.

Prerequisites

* You have created a custom action in FlutterFlow.
* You are familiar with using Run Mode and viewing the browser console.

The core function that you can use to test the custom actions on the console is the `debugPrint` function in Flutter. To use that in the custom actions, follow the steps below:

1. **Add `debugPrint` Statements in the Code**

   Use `debugPrint` to print some error on the debug console in case of a specific result. You can use if-else statements or try-catch statements in order to test the success of the scenario.

   ![](https://docs.flutterflow.io/assets/images/20250430121216632942-63960ad02159d34e7a6e652d1cb4c7c3.png)

   Example:

   ```
   try {
       final result = someFunction();
       debugPrint('Function result: $result');
   } catch (e) {
       debugPrint('Error occurred: $e');
   }
   ```

2. **Run the App and Open Console**

   After the correct implementation in the code, use the action inside the app. On the run mode, open the console. Now you should be able to see the errors in the console upon performing the action.

   ![](https://docs.flutterflow.io/assets/images/20250430121216962021-90ed68f4858e11cecae8b90992a7de16.png)

Still having issues?

If you continue to experience issues after testing your logic with debugPrint, please contact support at <support@flutterflow.io>.​

---

### Codemagic Deployment Error Identification {#codemagic-deployment-error-identification}

*Follow the steps below to identify your codemagic error:*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/codemagic-deployment-error-identification

Follow the steps below to identify your codemagic error:

* Press **Cmd/Ctrl + k**, type **"deployment"** and hit enter. It will take you to the deployment page.​

  ![](https://docs.flutterflow.io/assets/images/20250430121346608131-6051c8ea2ed39c336fb416c77c21edd9.png)

* Navigate to the Deployment section by clicking **Project Settings** > **Deployment** (under App Settings).​

  ![](https://docs.flutterflow.io/assets/images/20250430121346890273-bd3b94558011c64dfb0021518ec0be4a.png) ​

* Click on the **Failed (VIEW LOGS)** text to see the logs. ​

  ![](https://docs.flutterflow.io/assets/images/20250430121347217644-55dff2897e82db223506ec239460e025.png)

  In this step, you'll need to note the Failed Step that been displayed by CodeMagic error log. ​

  ![](https://docs.flutterflow.io/assets/images/20250430121347593094-8827607888b9888bcf0478b4223d6c1e.png) ​

* Now, press **Cmd/Ctrl + F** to search for the term **"error"** in the logs to find the root cause of the issue. Keep pressing **"Enter"** till you find the error ( this is usually at the bottom of the logs ).

  If you search for "error" and still don't find an error message that makes sense to you then you can also try with the following keyword: "message".

  ![](https://docs.flutterflow.io/assets/images/20250430121347925706-7968ab925bd39390fc5f6701162d0f4e.png)

* Now select and copy this error message and paste it in the Help Center search in the chat icon in the bottom-right corner to search the error. This will help you find the help article for this issue and then you can find the fix for it.

  ![](https://docs.flutterflow.io/assets/images/20250430121348293622-e59b4593b13524be85bdee95d0b752ca.gif)

---

### CodeMagic Deployment Tips {#codemagic-deployment-tips}

*Here are some tips to avoid Deployment issues:*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/codemagic-deployment-tips

Here are some tips to avoid Deployment issues:

> **Tip:** * Make sure you've followed all the steps for **[setting up deployment](https://docs.flutterflow.io/deployment/deploy-for-environments#mobile-deployment)** in your project.
* If you choose a deployment source from a GitHub Repository then please make sure that it's associated with FlutterFlow's GitHub integration.
* If you are deploying to the Play Store from a GitHub repo, make sure to modify your build.gradle file to sign in release mode.
* Setting a version number is optional but may be required for specific cases. If you are updating an existing app that has not been deployed using FlutterFlow yet, you will want to specify a version number.

---

### Deployment Issues with Stripe Integration {#deployment-issues-with-stripe-integration}

*Integrating Stripe in your FlutterFlow project can help you accept payments efficiently. However, some common deployment issues may arise. This article outlines key steps and best practices to ensure a smooth Stripe integration and deployment experience.*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/deployment-issues-with-stripe-integration

Integrating Stripe in your FlutterFlow project can help you accept payments efficiently. However, some common deployment issues may arise. This article outlines key steps and best practices to ensure a smooth Stripe integration and deployment experience.

1. **Firebase Connection**

   Stripe integration requires a connected Firebase project. Before running through this checklist, it's important to ensure your FlutterFlow project is linked to Firebase, a crucial step for successful payment processing. Detailed guidance can be found at **[FlutterFlow's Firebase Setup Guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#step-1-set-up-your-project)**.

2. **Upgrade to Firebase Blaze Plan**

   Stripe functionality requires a Firebase Blaze Plan for operational capabilities. To avoid disruptions, you will need to upgrade from the Firebase Spark plan to the Blaze plan. Learn more about **[Google's process for upgrading](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans)**.

3. **Set the Google Cloud Platform (GCP) Location**

   A defined Google Cloud Platform (GCP) location for your Firebase project ensures the correct regional operation of services. The absence of a set location can hinder the deployment process.​

   ![](https://docs.flutterflow.io/assets/images/20250430121121827511-04519b51a0219b97efed58e9cb8f6302.png)

4. **Firebase Project Permissions**

   Ensure you have the necessary permissions enabled for your Firebase project. Two critical permissions involve access management and service configuration. You can also reference the **[setup guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#step-1-set-up-your-project)** as well.​

   ![](https://docs.flutterflow.io/assets/images/20250430121122068343-0d7529a28637317e6b080a6dfde3dce7.png)

5. **Correct Merchant Code**

   Use the correct 3-letter merchant country code (e.g., "GBR" for the United Kingdom vs. "UK"). Incorrect codes can lead to failed transactions. For accurate codes, refer to **[IBAN Country Codes](https://www.iban.com/country-codes)**.​

   ![](https://docs.flutterflow.io/assets/images/20250430121122307123-ce254157c126b63ba4f6d28b18407876.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121122597517-7bd69ca688add81b57c2786e5c82167a.png)

6. **Test and Live Keys**

   For deployment, both Test and Live Stripe keys must be configured in your project settings, regardless of the development stage. This ensures Stripe's API can properly interact with your application.​

   ![](https://docs.flutterflow.io/assets/images/20250430121122925141-9d93238a034787161270b25ce87ec7b8.png)

7. **Consistent Region Settings**

   Align your Firebase project's region with that of your FlutterFlow settings to prevent deployment failures. Inconsistencies can cause function deployment issues.​

   ![](https://docs.flutterflow.io/assets/images/20250430121123230941-b344665d460afd8118a7232a42fad81a.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121123502329-e3650708a342858946ee640eb2349795.png)

If you find that this article hasn't fully addressed your concerns or if you have more questions, please don't hesitate to reach out to us at <support@flutterflow.io>

​

---

### Fixing Razorpay Deployment {#fixing-razorpay-deployment}

*Razorpay is a major payment processor in India. Integrating Razorpay can allow users to make payments using their app. This article outlines some common scenarios and troubleshooting instructions for Razorpay deployment issues.*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/fixing-razorpay-deployment

Razorpay is a major payment processor in India. Integrating **[Razorpay](https://razorpay.com/)** can allow users to make payments using their app. This article outlines some common scenarios and troubleshooting instructions for Razorpay deployment issues.

1. **Firebase Integration and Auth**

   FlutterFlow uses Firebase integration and cloud functions to facilitate Razorpay payments. Ensure you have Firebase configured in your FlutterFlow project and that Firebase Auth is enabled.

   ![](https://docs.flutterflow.io/assets/images/20250430121119193097-a438f40c7cdfcb6f5d1835d2ec6f5fc7.png) ![](https://docs.flutterflow.io/assets/images/20250430121119493481-f8b5d61a1b92ca72e37c18aab36a3c1c.png)

2. **Firebase Blaze Plan**

   Razorpay uses cloud functions behind the scenes to facilitate payments. Cloud functions are a part of Firebase's "Blaze" plan. You must upgrade from the Firebase Spark plan to the Blaze plan to avoid disruptions. Learn how to upgrade here. On the bottom left side of your Firebase console, you will see which plan you are on

   ![](https://docs.flutterflow.io/assets/images/20250430121119754142-f2fe2017ace7abe5aff8a39815eb0f66.png)

3. **Set Google Cloud Location**

   Ensuring your Firebase project is pinned to a specific Google Cloud Platform (GCP) location is key for optimal service functionality across regions. Skipping this step could result in errors.​

   ![](https://docs.flutterflow.io/assets/images/20250430121120027064-04519b51a0219b97efed58e9cb8f6302.png)

4. **Firebase Project Permissions**

   Make sure your Firebase project has the required permissions activated. Access management and service configuration are two essential permissions to focus on. For guidance on setting these up, look at the instructions in the **[FlutterFlow Project Setup](https://docs.flutterflow.io/resources/projects/settings/project-setup)**.

5. **Razorpay Keys Check**

   Make sure to copy and paste the correct Key ID and Key Secret from Razorpay for testing and production, respectively. For testing, make sure "Is Production" is turned off.

   ![](https://docs.flutterflow.io/assets/images/20250430121120324713-954f9bacfc758924edb56feaf8d03874.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121120614698-427f7e6d97ef154687e5c52d418bade7.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121120833797-47659c8138d19168b2aa7de8c2f896c3.png)

6. **Razorpay Business Name**

   Finally, ensure you have entered the proper "Business Name" in the Razorpay additional settings in FlutterFlow. Make sure this business name matches your business name in Razorpay records.

   ![](https://docs.flutterflow.io/assets/images/20250430121121100378-562380f0010a8034013ffb62e8768126.png)

Other Considerations

Razorpay currently works only on mobile (Android and iOS). This is due to a limitation from Razorpay's Flutter Package. If you are planning to collect payments on a web app - consider using Stripe.

![](https://docs.flutterflow.io/assets/images/20250430121121294657-9281e98e690de9a3fbc9f3190be20cd5.png)

If you are still facing issue with deploying Razorpay on Flutterflow, please feel free to reach out to <support@flutterflow.io>

---

### Fixing Stripe Deployment & Payment Errors {#fixing-stripe-deployment-payment-errors}

*Integrating Stripe for payment processing in FlutterFlow can significantly simplify monetization. However, developers may encounter issues during deployment or while managing transactions. This guide outlines common deployment and payment issues—and how to fix them—to help ensure a seamless Stripe integration experience in FlutterFlow apps.*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/fixing-stripe-deployment-and-payment-errors

Integrating Stripe for payment processing in FlutterFlow can significantly simplify monetization. However, developers may encounter issues during deployment or while managing transactions. This guide outlines common deployment and payment issues—and how to fix them—to help ensure a seamless Stripe integration experience in FlutterFlow apps.

#### Deployment Checklist for Stripe Integration

1. **Firebase Connection**

   Stripe integration requires a connected Firebase project. Before running through this checklist, it's important to ensure your FlutterFlow project is linked to Firebase, a crucial step for successful payment processing. Detailed guidance can be found at **[FlutterFlow's Firebase Setup Guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)**.

2. **Upgrade to Firebase Blaze Plan**

   Stripe functionality requires a Firebase Blaze Plan for operational capabilities. To avoid disruptions, you will need to upgrade from the Firebase Spark plan to the Blaze plan. Learn more about **[Google's process for upgrading](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans)**.

3. **Set the Google Cloud Platform (GCP) Location**

   A defined Google Cloud Platform (GCP) location for your Firebase project ensures the correct regional operation of services. The absence of a set location can hinder the deployment process.​

   ![](https://docs.flutterflow.io/assets/images/20250430121145711998-04519b51a0219b97efed58e9cb8f6302.png)

4. **Firebase Project Permissions**

   Ensure you have the necessary permissions enabled for your Firebase project. Two critical permissions involve access management and service configuration. You can also reference the **[setup guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)**.​

   ![](https://docs.flutterflow.io/assets/images/20250430121145949036-0d7529a28637317e6b080a6dfde3dce7.png)

5. **Correct Merchant Code**

   Use the correct 3-letter merchant country code (example., "GBR" for the United Kingdom vs. "UK"). Incorrect codes can lead to failed transactions. For accurate codes, refer to **[IBAN Country Codes](https://www.iban.com/country-codes)**.​

   ![](https://docs.flutterflow.io/assets/images/20250430121146161973-ce254157c126b63ba4f6d28b18407876.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121146400049-7bd69ca688add81b57c2786e5c82167a.png)

6. **Test and Live Keys**

   Both Test and Live Stripe keys must be configured in your project settings, regardless of the development stage. This ensures Stripe's API can properly interact with your application.​

   ![](https://docs.flutterflow.io/assets/images/20250430121146604033-9d93238a034787161270b25ce87ec7b8.png)

7. **Consistent Region Settings**

   Align your Firebase project's region with that of your FlutterFlow settings to prevent deployment failures. Inconsistencies can cause function deployment issues.​

   ![](https://docs.flutterflow.io/assets/images/20250430121146854018-b344665d460afd8118a7232a42fad81a.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121147068781-e3650708a342858946ee640eb2349795.png)

#### Addressing Payment Transaction Issues

1. **Authentication Requirement**

   Stripe payments **require an authenticated user session**. Before initiating payment processes, ensure your application logic includes user login or account creation.

2. **Payment Modal Variations**

   It's important to note that web and mobile platforms present different payment modal presentations. These UI differences are out-of-the-box for Stripe and cannot currently be customized within FlutterFlow.

3. **Price Format**

   Prices should be submitted to Stripe in **cents**, not **dollars**. Utilize a custom function to convert dollar values to cents for accurate transaction processing.​To set a price in cents to Stripe, you can simply use a custom function that takes the price in dollars and returns it as cents.​

   Here is a custom code you can use to make this calculation in a custom function:

   ```
   int dollarToCent(double amount) {
   // Convert the amount to a string
   String st = amount.toString();

   // Remove any dots or commas
   st = st.replaceAll('.', '');
   st = st.replaceAll(',', '');

   // Convert the cleaned string to an integer
   return int.parse(st);
   }
   ```

   // Input: 14.99

   // Output: 1499 cents

4. **CORS Error Resolution**

   A CORS error during payment initiation often indicates a permissions issue with your Firebase function. Verify and adjust the `allUsers` permission for your Stripe function in the Firebase console to resolve this error.​

   ![](https://docs.flutterflow.io/assets/images/20250430121147385978-51634e1a435a358149efcdd9361de1bf.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121147683388-db162fbb7e44ca3923b1521c56743149.png)

5. **Subscriptions**

   Currently, Apple and Google restrict Stripe subscriptions on mobile platforms. To expand your subscription capabilities, you can use alternative solutions like RevenueCat for mobile apps and direct API calls for web applications.​

**For further information and troubleshooting:**

* [Stripe Documentation](https://stripe.com/docs)
* [Stripe Payments](https://stripe.com/payments)
* [FlutterFlow University](https://university.flutterflow.io/)
* [Payments - Intro | FlutterFlow University](https://university.flutterflow.io/courses/flutterflow-payments)

---

### Resolve Errors in Downloaded Code {#resolve-errors-in-downloaded-code}

*When you download your project from FlutterFlow and run it locally in your IDE, you may encounter errors due to Flutter version mismatches. This guide outlines how to resolve these issues by ensuring your local Flutter version matches the version supported by FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/resolve-errors-in-downloaded-code

When you download your project from FlutterFlow and run it locally in your IDE, you may encounter errors due to Flutter version mismatches. This guide outlines how to resolve these issues by ensuring your local Flutter version matches the version supported by FlutterFlow.

1. **Check FlutterFlow’s supported Flutter version**

   To find the Flutter version currently supported by FlutterFlow:

   * Open the FlutterFlow dashboard.
   * Navigate to your project settings or export screen.
   * Locate the displayed Flutter version used for your project.

   ![](https://docs.flutterflow.io/assets/images/20250430121137152872-9f928bf5f226f815cf41220d9edc1795.png)

2. **Verify the Flutter version on your machine**

   To check the Flutter version installed locally, run the following command in your terminal:

   ```
   flutter --version
   ```

   Here's an example of how you can do that:

   ![](https://docs.flutterflow.io/assets/images/20250430121137421780-b885347a16240cdd13b780ae93f2b68a.png)​

3. **Upgrading or Downgrading to the correct Flutter version**

   If the current version on your machine is different than what is currently supported by FlutterFlow, you can downgrade or upgrade to the supported version. You can learn more about [**upgrading Flutter**](https://docs.flutterflow.io/testing/local-run#4-running-app-on-device). ​By following these steps, you can fix the errors that you face after downloading the code and run locally.

If you continue to experience issues, contact the FlutterFlow support team via live chat or email at <support@flutterflow.io>.

---

### Run Mode: Build Failure {#run-mode-build-failure}

*Encountering a "Run mode: Build failed" error can be frustrating when you're eager to see your app in action. This error typically signifies a project issue that prevents a successful build. Addressing these errors promptly ensures your app's functionality and performance.*

**Source:** https://docs.flutterflow.io/troubleshooting/deployment/run-mode-build-failure

Encountering a "Run mode: Build failed" error can be frustrating when you're eager to see your app in action. This error typically signifies a project issue that prevents a successful build. Addressing these errors promptly ensures your app's functionality and performance.

This guide provides a structured approach to troubleshooting and resolving "Run mode: Build failed" errors, ensuring a smooth development process for your projects.

* **Recognizing the Error**

  Here's what the "Run mode: Build failed" error looks like inside of FlutterFlow:

  ![](https://docs.flutterflow.io/assets/images/20250430121148301014-4d413e5fef4fbe4880435e75c2edf4ee.png)

* **Understanding Test Mode vs. Run Mode**

  Here's a little background on run mode vs. test mode in FlutterFlow. Test mode runs as a "test" to help you identify errors before deployment. These features include a debugger and display warnings. Alternatively, run mode attempts to run the app in **release mode** to better mimic what your users can expect in production. In release mode, **warnings are mostly suppressed**, meaning it's important to ensure you are acknowledging and addressing warnings in debug mode before you enter run mode.

  The "Run mode: Build failed" error can occur under various circumstances, during:

  * Run mode

  * APK download

  * Code download

  * GitHub push

  * And more

#### Common Scenarios and Solutions

* **Custom Code Failures**

  * **Issue**: Your project's custom code doesn't show errors within the editor, but errors appear when you try to run the app.

  * **Example**: A custom widget lacks web support.

  * **Solution**: Verify on pub.dev or equivalent platforms that the custom code supports the necessary platforms (example, web, iOS, Android).

  * **Best practice**: Consider running the code locally on a sample Flutter project before implementing the custom code inside FlutterFlow to identify possible errors logged.

* **Widget Failures**

  * **Issue**: A widget within your app causes the build to fail due to errors.

  * **Example**: Actions assigned to a widget are incomplete or improperly configured.

  * **Solution**: Locate the error-causing widget (usually identified in the error message)

    To correct the issue:

    * Ensure the widget tree is correctly formatted

    * Verify that widgets are named clearly for easy identification

* **Build Fails Without Error Messages**

  * **Issue**: The build process fails without displaying an error message, making it challenging to diagnose the problem.

  * **Solution**: Download and run the project code locally with a debugger to identify and resolve the issue. If downloading the code is problematic, check your browser's console for errors that might indicate the cause.

    ![](https://docs.flutterflow.io/assets/images/20250430121148811672-4c769af193fd8c00576f42eb585c2658.png)

* **Grey Screen in Run Mode**

  * **Issue**: Encountering a grey screen in run mode usually indicates an error suppressed by the release mode.

  * **Solution**: Run the app in test mode to potentially reveal the error for troubleshooting. If test mode does not display errors, use the browser's developer console for clues.

#### Checklist for Troubleshooting

* **Identify when and where the error occurs**:

  Determine if the error is specific to run mode, test mode, or other instances like APK download or code download.

* **Locate the source of the error**:

  The error message often provides clues about where the problem lies, whether in custom code, a specific widget, or elsewhere.

* **Check for platform support**:

  For issues related to custom code, ensure compatibility with your target platforms.

* **Examine widget configuration**:

  Verify that all actions and configurations associated with widgets are complete and correct.

* **Utilize local debugging**:

  If the error is elusive, running the debugger locally on your downloaded code can help identify the issue.

* **Leverage browser tools**:

  The browser's console and developer tools can offer insights, especially when dealing with errors that don't manifest in traditional debug outputs.

Additional Resources

[Basic Troubleshooting Guide – FlutterFlow Documentation](https://docs.flutterflow.io/troubleshooting/basic-troubleshooting-guide)

---

### Enterprise {#enterprise}

*A guide to troubleshoot FlutterFlow enterprise projects.*

**Source:** https://docs.flutterflow.io/troubleshooting/enterprise

#### Unable to access FlutterFlow

Few enterprise customers might have restrictions in accessing the internet. For example, allowing only safe URLs that are related to their work. If you have such restrictions, you might not be able to access FlutterFlow. To use FlutterFlow and get the best experience, you need to allow all the URLs FlutterFlow uses to operate.

Allowlist of URLs:

* [app.flutterflow.io](http://app.flutterflow.io/)
* [flutterflow-io-6f20.firebaseapp.com](http://flutterflow-io-6f20.firebaseapp.com/)
* [https://flutterflow-io-6f20.firebaseio.com](https://flutterflow-io-6f20.firebaseio.com/)
* [flutterflow-io-6f20.appspot.com](http://flutterflow-io-6f20.appspot.com/)
* [https://storage.googleapis.com](https://storage.googleapis.com/)
* <https://firestore.googleapis.com/>
* <https://us-central1-flutterflow-io-6f20.cloudfunctions.net/>
* <https://www.google-analytics.com/>
* <https://fonts.gstatic.com/>
* <https://cdn.jsdelivr.net/>
* <https://r.wdfl.co/>
* [https://maps.googleapis.com](https://maps.googleapis.com/)
* <https://www.googletagmanager.com/>
* <https://www.gstatic.com/>
* <https://docs.flutterflow.io/>

---

### Client Access to Firestore Expired {#client-access-to-firestore-expired}

*You may receive an email from Firebase with the subject:*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/client-access-to-firestore-expired

You may receive an email from Firebase with the subject:

**"Client access to your Cloud Firestore database expired"**

This message typically appears when your Firestore database is in **Test Mode** and the access duration has expired.

You are seeing this error message because of the following:

When setting up Firestore for the first time, Firebase offers two rule options:

1. **Test Mode** – Temporarily allows open access (expires after 30 days).
2. **Production Mode** – Starts off restricted and requires secure rules.

![](https://docs.flutterflow.io/assets/images/20250430121224235710-89e69fcdc91e04a8e895f061065d4b91.png)

If you selected **Test Mode** during setup, Firestore access will automatically expire after the preset period. To continue using Firestore, you'll need to update the rules using one of the following options:

* **Option 1: Manage Firestore Rules From FlutterFlow**

  You can **[manage and deploy Firestore rules](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules)** directly from FlutterFlow.

* **Option 2: Manually Update Firestore Rules in Firebase Console**

  Follow these steps to manually update the rules:

  1. Go to the **[Firebase Console](https://console.firebase.google.com/)**.
  2. Open your project and navigate to **Firestore Database**.
  3. Select the **Rules** tab.

  From here, you have two options:

  * **Option A: Extend Test Mode**

    Update the expiration timestamp to a future date if you're still in development.

    ![](https://docs.flutterflow.io/assets/images/20250430121224547832-a2a051061854b7c100d8a54f3f166710.png)

  * **Option B: Secure Your Rules for Production**

    Update your rules to enforce proper authentication and access controls.

    ![](https://docs.flutterflow.io/assets/images/20250430121224874215-be277d57d8c10ead3f30dd39c3cd5b43.png)

If the issue persists, contact us at <support@flutterflow.io> for further assistance.

---

### Configuring CORS for Firebase Storage {#configuring-cors-for-firebase-storage}

*When you deploy your web app to a custom domain, the domain and the Firebase Storage bucket are hosted on different servers. This means that the browser will block requests to the Firebase Storage bucket from your web app, because the origins (the domains and ports) of the two servers are different.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/configuring-cors-for-firebase-storage

When you deploy your web app to a custom domain, the domain and the Firebase Storage bucket are hosted on different servers. This means that the browser will block requests to the Firebase Storage bucket from your web app, because the origins (the domains and ports) of the two servers are different.

**What is CORS?**

CORS stands for **Cross-Origin Resource Sharing**. It allows you to specify which origins are allowed to access your resources. By configuring CORS, you can tell the browser that your web app is allowed to make requests to the Firebase Storage bucket, even though the two servers are hosted on different domains.

Follow these steps to configure CORS for your Firebase Storage bucket:

1. Open **[Google Cloud Console](https://console.cloud.google.com)**.

2. **Launch the Cloud Shell**:

   Click the **Activate Cloud Shell** icon in the top-right corner.

   ![](https://docs.flutterflow.io/assets/images/20250430121203371000-ae959dd8cb3f0d459ec1a3c85478fac5.png)

   Wait for the terminal to load.

   ![](https://docs.flutterflow.io/assets/images/20250430121203911156-0d82267ed36a199657a864eeb231151d.png) ​

3. **Run the following Command:**

   ```
   gcloud config set project your-firebase-project-id;
   ```

4. **Define and upload your cors.json file:**

   The `cors.json` file contains a list of origins that are allowed to access your resources. Each origin is a string that identifies a domain or port. For example, the following origin allows access from the domain `www.example.com`:

   ```
   "origins": ["https://www.example.com"]
   ```

   You can also specify a list of allowed headers. The following example allows access to the `Content-Type` and `Authorization` headers:

   ```
   "origins": ["https://www.example.com"], "allowedHeaders": ["Content-Type", "Authorization"]
   ```

   To allow any origin to access your resource, you can use `*`. The `cors.json` file below allows any origin to access, but not modify your resources.

   ```
   [
       {
           "origin": ["*"],
           "method": ["GET"],
           "maxAgeSeconds": 3600
       }
   ]
   ```

   Once you have defined your `cors.json` file, upload it to Google Cloud Console.

   ![](https://docs.flutterflow.io/assets/images/uploadToGCC-97604280ce723bb14f8c458427ed74c4.png)

   To confirm that you have uploaded it correctly, you can run `ls` in your console and you should see your `cors.json` file listed.

5. **Run the `cors` Command to Configure CORS:**

   ```
   gcloud storage buckets update gs://your-google-storage-bucket-name --cors-file=cors.json
   ```

6. **(Optional) Confirm success by viewing the CORS of your bucket**

   Run the following command to confirm that the rules from your `cors.json` file were applied.

   ```
   gcloud storage buckets describe gs://your-google-storage-bucket-name --format="default(cors_config)"
   ```

   You should see the same allowed origins and any other info defined in your `cors.json` file.

For more information on configuring CORS in Firebase Storage, please see the **[official documentation](https://firebase.google.com/docs/storage/web/download-files#cors_configuration)**.

---

### Content Manager Firestore Error {#content-manager-firestore-error}

*You may see the following error message when accessing the FlutterFlow Content Management System (CMS):*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/content-manager-firestore-error

You may see the following error message when accessing the **FlutterFlow Content Management System (CMS)**:

![](https://docs.flutterflow.io/assets/images/20250430121517855306-24e97004e33cce6167bdd47037e1263a.png)

This error typically occurs when Firebase permissions or authentication settings are not properly configured. Follow the steps below to resolve it.

1. **Enable Email/Password Sign-In**

   1. Open the **[Firebase Console](https://console.firebase.google.com/)**.
   2. Select your project.
   3. From the left-hand menu, click **Authentication**.
   4. Click **Get started** (if not already started).
   5. Go to the **Sign-in method** tab.
   6. Ensure **Email/Password** is listed and marked as **Enabled** ✅.

   ![](https://docs.flutterflow.io/assets/images/20250430121518159572-c74b9cb5cb2f2eb2ebac07205fcbe1c4.png)

   note

   If Email/Password is not enabled, turn it on by clicking the pencil icon and toggling the setting.

2. **Add Required Firebase Project Permissions**

   FlutterFlow requires the following roles to be granted to `firebase@flutterflow.io` for proper functionality:

   * Editor
   * Cloud Functions Admin
   * Service Account Admin

   To add these permissions:

   1. In the **[Firebase Console](https://console.firebase.google.com/)**, open your project.
   2. Navigate to **Project Settings** > **Users & Permissions**.
   3. Check if `firebase@flutterflow.io` has the roles listed above.

   ![](https://docs.flutterflow.io/assets/images/20250430121518370897-f0e035f033238446b162c7eacbb6af13.png)

   info

   If these roles are missing, the integration is incomplete. Make sure to add all three roles.

3. **Update Firestore Rules in FlutterFlow**

   1. In your FlutterFlow project, go to **Firestore** > **Settings**.
   2. Scroll down to the **Firestore Rules** section.
   3. Click **Deploy/Redeploy** to apply your latest rules.

   ![](https://docs.flutterflow.io/assets/images/20250430121518594245-1fa5ba0cf70fb84c236da5b1a6e8d77d.png)

4. **Define Your Firebase Schema**

   Make sure your Firebase schema is fully defined. The Content Manager only displays fields that are already defined in your Firebase schema.

5. **Ensure You're Using the Latest FlutterFlow Version**

   Press `Ctrl + R` (on Windows) or `Cmd + R` (on macOS) to refresh and ensure you’re on the latest version of FlutterFlow.

6. **Clear Cache and Re-Login**

   After completing the above steps:

   * Clear your browser cache.
   * Log out and log back into FlutterFlow.

Still not working?

Try reconfiguring permissions from scratch.

If none of the steps resolve the issue:

1. Remove existing Firebase permissions.
2. Re-add all necessary roles from scratch.
3. Follow the full setup instructions in the **[official FlutterFlow Firebase integration guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)**.

By following the steps above, you should be able to resolve the error and continue using FlutterFlow CMS without interruptions.

---

### Firebase Android Config File Missing {#firebase-android-config-file-missing}

*You may see the following warning in FlutterFlow, as shown in the image below:*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/firebase-android-config-file-missing

You may see the following warning in FlutterFlow, as shown in the image below:

![](https://docs.flutterflow.io/assets/images/20250430121357585709-174b3b73ac2cca43e887898b6590d2d3.png)

This typically means that the Firebase Android configuration file (`google-services.json`) has not been generated or uploaded to your FlutterFlow project.

Follow the steps below to fix the issue:

1. **Verify your Firebase Setup**

   Make sure that Firebase has been fully configured for your project. Follow the **[Firebase setup guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase)** to ensure all required steps have been completed.

2. **Open Project Settings in FlutterFlow**

   * Navigate to your FlutterFlow project.
   * From the left menu, select **Settings > Firebase**.

   ![](https://docs.flutterflow.io/assets/images/20250430121357870887-9a8bd8979530cdb39ac0650f847d866f.png)

3. **Regenerate your Firebase Configuration Files**

   * In the Firebase Settings screen, click **Regenerate Firebase Files** to create new configuration files and upload them automatically.

4. **Contact Support if Needed**

   If you continue to experience issues, reach out to [FlutterFlow Support](mailto:support@flutterflow.io) for further assistance.

> **Note:** The configuration file is required for successful builds and deployment on Android. Make sure it remains up-to-date if you make changes in your Firebase project.

---

### Firebase Storage Limits in FlutterFlow {#firebase-storage-limits-in-flutterflow}

*Managing Firebase Storage properly is essential for controlling your app's file storage and associated costs in FlutterFlow. This article summarizes the current limits and best practices following Firebase’s September 2024 changes.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/firebase-storage-limits-in-flutterflow

Managing Firebase Storage properly is essential for controlling your app's file storage and associated costs in FlutterFlow. This article summarizes the current limits and best practices following Firebase’s September 2024 changes.

#### Firebase Storage Plans and Limits

* **Blaze Plan (Pay-as-you-go)**

  * Firebase Storage (Cloud Storage for Firebase) is only available on the Blaze plan for new Firebase projects.
  * Storage charges are based on usage volume.
  * The price per GB/TB decreases as your usage increases.
  * Refer to the **[Firebase Pricing page](https://firebase.google.com/pricing)** for current rates.

* **Spark Plan (Free Tier)**

  * For projects created after September 2024, Cloud Storage for Firebase is **no longer available** on the Spark plan.
  * To use file storage (uploads, images, videos, etc.) with Firebase Storage, you must upgrade to the Blaze plan.

> **Info:** If your Firebase project was created before the September 2024 policy change, you may still have limited access to Firebase Storage under legacy conditions. However, new projects must follow the updated Blaze-only policy.

#### Firebase Storage Operations Limits

* Firebase imposes limits on the number of operations (uploads, downloads, deletes) based on your plan.
* With Blaze, these limits are generally higher but still subject to quotas depending on your usage volume.
* Monitor your app’s usage patterns to avoid unexpected failures or costs.

#### Best Practices for Managing Firebase Storage

* Regularly delete unused or unnecessary files.
* Compress large files (especially images and videos) before uploading.
* Actively monitor storage usage in the Firebase Console.
* Set up automated cleanup processes for apps with large or growing data volumes.

> **Tip:** Proactive storage management helps control costs and maintain app performance.

Additional Resources

* [Firebase Pricing](https://firebase.google.com/pricing)
* [Firebase Storage FAQ (September 2024 Changes)](https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024)
* [Firebase Storage Documentation](https://firebase.google.com/docs/storage)
* [FlutterFlow Docs: Storage](https://docs.flutterflow.io/integrations/firebase-storage/storage-rules)

Always review your Firebase plan details to ensure you're aligned with the most current pricing model and storage policies.

---

### Get the Sum of Firebase Document or API Values {#get-the-sum-of-firebase-document-or-api-values}

*Sometimes you need to display a total, such as a subtotal or count based on data fetched from Firebase or an API. This guide walks you through the steps to calculate and display that sum in FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/get-the-sum-of-firebase-document-or-api-values

Sometimes you need to display a total, such as a subtotal or count based on data fetched from Firebase or an API. This guide walks you through the steps to calculate and display that sum in FlutterFlow.

Prerequisites

* A working Firebase collection or API that returns numeric values.
* A FlutterFlow UI component (example, **Text**) where the sum will be displayed.

**Steps to Calculate the Sum of Firebase Document or API Values**

1. **Identify where to Display the Total**

   Decide where in your app the total will appear. For example, insert a **Text** widget that will show the computed sum.

   ![](https://docs.flutterflow.io/assets/images/20250430121219360101-421db570635b0004a33c0e3c102580ba.png)

2. **Prepare your Data Type**

   Next, you need to specify what kind of data you're adding up. For example, if you're working with numbers with decimal points, you'll classify your data as double. Make sure to indicate that you're dealing with a list of these values.

   ![](https://docs.flutterflow.io/assets/images/20250430121219606895-00021a4fa8e3ae17e474ff9060a63370.png)

3. **Retrieve and Map your Data**

   When fetching data from Firebase or an API, extract the values you want to sum. Use the `map()` function to create a list of those values.

   ![](https://docs.flutterflow.io/assets/images/20250430121219871237-fcb0c28690750863a8af6ed74f10c3a4.png)

4. **Calculate the Sum**

   With your list of values ready, store them in a variable (let's call it `var1`). Then, decide on the format you want for your result. Use the `reduce` function to add up all the values in your list, `var1`, to get your total sum.

   ![](https://docs.flutterflow.io/assets/images/20250430121220084430-5a459b5c85db423fa188d82a944de37f.png)

5. **Checking Your Results**

   After completing these steps, you should have the total sum displayed where you need it. If it looks right, you've successfully calculated the sum!

   [](https://docs.flutterflow.io/assets/files/20250430121220338400-87ae823e6fb5f5d9c92b2651efbe48b6.png)

Trobleshooting

* Use `.isNotEmpty` to prevent errors when the list is empty.
* Format the output using `.toStringAsFixed(2)` to show 2 decimal places if needed.
* Optional: Store the sum in a global variable for use across multiple pages.

---

### Missing Firebase Storage in FlutterFlow Settings {#missing-firebase-storage-in-flutterflow-settings}

*When setting up Firebase Storage in your FlutterFlow project, you may notice that the Firebase Storage option is missing from the Firebase Settings tab.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/missing-firebase-storage-in-flutterflow-settings

When setting up Firebase Storage in your FlutterFlow project, you may notice that the **Firebase Storage** option is missing from the **Firebase Settings** tab.

![](https://docs.flutterflow.io/assets/images/20250430121309740417-bf1c5b27e75fe10c002115df6be9b0b0.png)

This usually happens when Firebase Storage has not been enabled for your project in the Firebase Console. Until it’s enabled there, the option won’t appear in FlutterFlow.

Follow these steps to enable Firebase Storage and make it available in your FlutterFlow settings:

1. In your FlutterFlow project, click **Firebase** from the left menu, then click **Open Firebase Console**.

   ![](https://docs.flutterflow.io/assets/images/20250430121310019673-e0ccc993e764abdf269d95415452c112.png)

2. In the Firebase Console, go to the **Build** menu and select **Storage**.

   ![](https://docs.flutterflow.io/assets/images/20250430121310317285-985cd6624de61ad14b28b6394eb4db6b.png)

3. Click **Get started** and complete the setup process.

   ![](https://docs.flutterflow.io/assets/images/20250430121310619096-a543a7ff241ac8ddb0501a78ef2ba3b3.png)

4. After successfully creating the storage bucket, return to FlutterFlow. You should now see the **Rules** option under **Firebase Settings**.

   ![](https://docs.flutterflow.io/assets/images/20250430121310959552-a17de5817984012a100fce3db8ec70bd.png)

> **Note:** After setting up Firebase Storage, it may take up to one hour for the changes to appear in FlutterFlow.

---

### Resolving Firestore Index Deployment Issues {#resolving-firestore-index-deployment-issues}

*If your Firestore indexes are not being deployed as expected, follow these troubleshooting steps to resolve the issue and ensure your app performs correctly.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/resolving-firestore-index-deployment-issues

If your Firestore indexes are not being deployed as expected, follow these troubleshooting steps to resolve the issue and ensure your app performs correctly.

![](https://docs.flutterflow.io/assets/images/20250430121118024255-a20f447be6780a9a23eba9e9c53d3240.png)

1. **Enable Email Sign-In**

   * Open your Firebase project.
   * Go to **Authentication** > **Sign-in method**.
   * Enable **Email/Password** sign-in.

2. **Grant Proper Permissions**

   * In your Firebase project, open **Project Settings** > **Users and permissions**.

   * Add <firebase@flutterflow.io> as a member.

   * Assign the following roles: * **Editor**
     * **Cloud Functions Admin**
     * **Service Account User**

   ![](https://docs.flutterflow.io/assets/images/20250430121118320891-4875e5f70a7f07f81cffd302e3f013bb.png)

3. **Update Firestore Rules**

   * Update your Firestore rules in both Firebase Console and FlutterFlow.
   * Ensure they match your app’s data access requirements.
   * Follow the detailed steps in the **[Firestore Rules documentation](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-rules)** to correctly configure your rules.

   ![](https://docs.flutterflow.io/assets/images/20250430121118592064-f6712af4376f88d2e1ef9f00fbd75b82.png)

4. **Verify Index Deployment**

   * In the Firebase Console, go to **Firestore Database** > **Indexes**.

   * Check that your indexes have been deployed.

     note

     Deployment may take a few minutes. Refresh the page if you don’t see updates immediately.

Additional Tips

* Make sure you completed all the steps above before retrying deployment.
* For advanced troubleshooting, check Firebase logs and permissions in Google Cloud Console.

Following these steps should help resolve Firestore index deployment issues in FlutterFlow.

---

### Unable to Validate Firestore Schema {#unable-to-validate-firestore-schema}

*When trying to validate your Firestore Schema, you may encounter the error as seen in the image below:*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/unable-to-validate-firestore-schema

When trying to validate your Firestore Schema, you may encounter the error as seen in the image below:

![](https://docs.flutterflow.io/assets/images/20250430121304770472-d33d51d68090bdbed7a8eb1502d7ef8d.png)

**Troubleshooting Steps:**

1. **Verify that you have Created a Firestore database**

   Ensure that you have already created a Firestore database in your Firebase project.

   ![](https://docs.flutterflow.io/assets/images/20250430121305056379-894e3e17d43df54fe13ad23cf585188a.png)

2. **Check the Database Mode**

   A database in Test Mode may not work properly for FlutterFlow integration.

   note

   After creating the database in Test Mode, there is no direct visual option to switch to Production Mode. You need to update the Firebase security rules manually. However, if you deploy the rules from FlutterFlow, this step is handled automatically.

   **Steps to Update your Database Rules**:

   1. Go to your Firebase project.
   2. Select **Cloud Firestore**.
   3. Navigate to **Rules**.

   You will see something like this:

   ![](https://docs.flutterflow.io/assets/images/20250430121305295728-e7dc52922d82931db1e441a76c95ebb7.png)

   Update the rules as needed.

   note

   Ensure that you specify the correct `rules_version` and verify your configuration.

   ![](https://docs.flutterflow.io/assets/images/20250430121305526883-dbdfc8d387727dfdb162fbcbae39ce53.png)

   4. Click **Publish** to apply the changes.

3. Assign the necessary permissions to `firebase@flutterflow.io`

   You must grant the required cloud permissions to `firebase@flutterflow.io`:

   * **Editor**
   * **Cloud Functions Admin**
   * **Service Account**

   In the Firebase Console:

   1. Open your project.
   2. Go to **Project Settings** > **Users & Permissions**.
   3. Confirm that the required roles are assigned to `firebase@flutterflow.io`.

   If you don't see these roles assigned, you need to complete this step:

   ![](https://docs.flutterflow.io/assets/images/20250430121305771267-b4c1e1d6d592a4e892881d4779c781fc.png)

4. Ensure you have at least one collection created in FlutterFlow

   In FlutterFlow, select the **Firestore** tab from the left menu. If no collections are listed, create at least one collection.

   ![](https://docs.flutterflow.io/assets/images/20250430121306066982-32b6ddf68c8679c186f91bb82de66a84.png)

5. **Confirm that your collections have documents**

   Use FlutterFlow's CMS to verify that your collections contain at least one document:

   * Select **Manage Content**.
   * Check each collection to confirm that data exists.

   If no documents exist, add at least one:

   ![](https://docs.flutterflow.io/assets/images/20250430121306294908-0e97d67ca6ccfbd57582ecd175bad8f7.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121306553330-f80c6041d593bc2e43f17bbfd8783d9f.png)

6. **Deploy Firestore rules from FlutterFlow**

   In your FlutterFlow project:

   1. Select **Firestore** > **Settings**.
   2. Scroll down to **Firestore Rules**.
   3. Select **Deploy** (or **Redeploy** if needed).

   ![](https://docs.flutterflow.io/assets/images/20250430121306835223-e3de6e45ed89ba05cbd17d52431f83cd.png)

---

### Updating Firestore Security Rules {#updating-firestore-security-rules}

*Most backend issues are generated by the misconfiguration of the Firestore Security Rules. These backend issues may include Grey Screen errors, Infinite Loading screen, Firestore record creating error, Data mismatch errors, etc.*

**Source:** https://docs.flutterflow.io/troubleshooting/firebase/updating-firestore-security-rules

Most backend issues are generated by the misconfiguration of the Firestore Security Rules. These backend issues may include Grey Screen errors, Infinite Loading screen, Firestore record creating error, Data mismatch errors, etc.

To solve these issues, the Firestore rules have to be updated, for which you can follow the given series of steps:

* **Update Your Firestore Rules**

  From within your FlutterFlow project, select **Firestore** > **Settings** > Scroll down to **Firestore Rules** > select **Deploy**/**Redploy**.

  ![](https://docs.flutterflow.io/assets/images/20250430121507937548-1fa5ba0cf70fb84c236da5b1a6e8d77d.png)

* **Update Firestore Indexes**

  The next step is to see if the Firestore Rules and Indexes are **Out of Date** or **Not Deployed** (as shown in the image below). If yes, click on the blue **Deploy** button to push the latest rules.

  ![](https://docs.flutterflow.io/assets/images/20250430121508288240-4b57b60ef6edf955155ef962a6136c99.png)

  After clicking on the **Deploy** button, a confirmation dialog would be shown, highlighting the changes in the rules that are being made from the deployment.

  This compares the existing rules in Firestore and highlights what changes are being made in the Firestore rules. These changes are required when a new collection is created or is been edited or if the rules are Out of Date.

  ![](https://docs.flutterflow.io/assets/images/20250430121508604665-43762681cfc53b60ebe21a52469d8b49.png)

  You can review the changes, and then you can click on the **Deploy Now** button. An orange loading indicator would be shown, which means that the rules are getting deployed (This step usually finishes within less than a minute, and the loading indicator is replaced with a Green Checkbox button).

* **Validate the Firestore Schema**

  After completing the steps above, validate the Firestore schema by clicking on the blue **Validate** button. This ensures that everything is configured correctly and the Firestore collection schema matches with the Collection schema configured in FlutterFlow.

  ![](https://docs.flutterflow.io/assets/images/20250430121508962664-81306c33ba320ea521aa4a3b4a8d6803.png)

---

### Initialize GitHub Repository {#initialize-github-repository}

*When pushing code to GitHub, the following error may occur:*

**Source:** https://docs.flutterflow.io/troubleshooting/github/initialize-github-repository

When pushing code to GitHub, the following error may occur:

```
Error pushing repository. Make sure your repository is initialized
```

This typically happens if the GitHub repository was not initialized correctly or if the project exceeds GitHub’s file size limits.

Prerequisites

* Access to your GitHub account.
* A FlutterFlow project with GitHub integration enabled.

Follow the steps below to initialize a GitHub repository:

1. **Create a New Repository**

   * Go to **[GitHub](https://github.com/)** and click **New** to create a repository.
   * Enable the option **Add a README file** during creation.

2. **Connect Repository to FlutterFlow**

   * Open your FlutterFlow project.

   * Navigate to **GitHub Integration** and follow the instructions to connect the new repository.

     ![](https://docs.flutterflow.io/assets/images/20250430121522561282-0a96b3cf65667cd8570589b9b0ca700a.gif)

3. **Download and Inspect Your Project**

   * Download the full source code from FlutterFlow.

   * Navigate to the `assets` folder.

   * Identify any files larger than **25MB**.

     Check Your Asset Size

     GitHub does not allow individual files larger than 25MB. Large image or video files may cause push failures.

     Tips to Reduce Project Size

     * Use **network assets** instead of uploading large media files directly to FlutterFlow.
     * Optimize images using tools like TinyPNG or ImageOptim before uploading.

Additional Resources

* **[Connect a GitHub Repo](https://docs.flutterflow.io/exporting/push-to-github#connect-a-github-repo)**
* **[State Management](https://docs.flutterflow.io/concepts/state-management)**

---

### Repository Head Deployment Failure {#repository-head-deployment-failure}

*This error may occur when deploying your FlutterFlow app to GitHub using Codemagic. The message Failed to set the repository head indicates a problem with repository access, configuration, or connectivity.*

**Source:** https://docs.flutterflow.io/troubleshooting/github/repository-head-deployment-failure

This error may occur when deploying your FlutterFlow app to GitHub using Codemagic. The message `Failed to set the repository head` indicates a problem with repository access, configuration, or connectivity.

Prerequisites

* A connected GitHub repository with appropriate access permissions.
* GitHub deployment enabled within FlutterFlow.

**The Error Message**

```
Failed to set the repository head
```

This message typically appears in the build log during deployment.

Below are the possible causes of this error:

* The GitHub repository does not exist or was deleted.
* The branch specified in build settings does not exist.
* Insufficient permissions to push or write to the branch.
* GitHub API or network connectivity issues.
* Local build errors in the codebase.

**Steps to Fix the Deployment Error:**

1. **Confirm the Repository Name**

   Ensure the repository name in your FlutterFlow deployment settings exactly matches the name in GitHub.

2. **Verify the Branch**

   Check that the branch exists in the repository and is correctly specified in your build settings. Avoid typos or casing mismatches.

3. **Review Repository Permissions**

   Confirm that your GitHub account or connected GitHub App has push/write access to the repository and branch.

4. **Check Network Access**

   Make sure your environment is not blocking GitHub via VPN, firewall, or DNS restrictions.

5. **Validate the Codebase Locally**

   Run the downloaded Flutter project locally to confirm that it builds without errors.

Additional Resources

* **[GitHub Deployment Overview](https://docs.flutterflow.io/deployment/deploy-from-github#steps-to-deploy)**
* **[Codemagic Deployment Error Identification](https://docs.flutterflow.io/troubleshooting/deployment/codemagic-deployment-error-identification)**

---

### AdMob Ads Not Displaying in Google Play Testing {#admob-ads-not-displaying-in-google-play-testing}

*If your AdMob ads are not showing during Open Testing via the Google Play Store, the issue is often tied to AdMob configuration, app permissions, or settings in the Google Play Console. Follow the steps below to ensure ads display correctly.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/admob-ads-not-displaying-in-google-play-testing

If your AdMob ads are not showing during **Open Testing** via the Google Play Store, the issue is often tied to AdMob configuration, app permissions, or settings in the Google Play Console. Follow the steps below to ensure ads display correctly.

Prerequisites

* An active **AdMob** account is set up.
* Your FlutterFlow project is linked to **AdMob**.
* The app is uploaded to **Google Play Console** under an Open Testing track.

- **Use Test Ads During Development**

  Always use test ads during development to avoid policy violations or ad-serving issues:

  * Refer to the **[Google AdMob Test Ads](https://developers.google.com/admob/android/test-ads)** guide for appropriate test ad unit IDs.
  * Live ads should be used only after your app is published to production and approved.

- **Verify AdMob Account Setup**

  1. Go to the **AdMob Console**.

  2. Confirm that your app is registered and linked to your Google Play listing.

  3. Ensure the app’s release status in AdMob matches its status in the **Google Play Console**.

     note

     If your app is listed as `not released` in AdMob, live ads may not load during testing.

- **Declare Use of Advertising ID**

  Apps targeting **Android 13 (API 33)** or above must declare use of the **Advertising ID**:

  1. Open the **Google Play Console**.

  2. Go to **Policy > App Content**.

  3. Select **Advertising ID** and complete the required form.

     warning

     Failing to declare the Advertising ID may result in ads not showing during testing or after release.

- **Confirm Ad Unit Configuration in FlutterFlow**

  1. Open your project in **FlutterFlow**.
  2. Navigate to **Settings > AdMob Integration**.
  3. Confirm that the correct **Ad Unit IDs** are used.
  4. Ensure Ad widgets are connected to the appropriate ad units.

- **Test in the Correct Environment**

  * Use a physical device instead of an emulator when possible.
  * Ensure the device has a strong internet connection.
  * Avoid using VPNs or battery optimization tools that may interfere with ad delivery.

- **Add app-ads.txt (Optional)**

  Setting up an `app-ads.txt` file is optional but recommended for better ad quality:

  * Follow the **[official guide](https://support.google.com/admob/answer/9363762?hl=en\&ref_topic=9675856\&sjid=8136071085841576181-EU)** to set it up.

- **Wait for Ad Approval**

  Even after the app is released:

  * Live ads may take several days to appear due to the review process and inventory matching.
  * This delay is expected.

If ads still aren’t appearing, contact FlutterFlow Support at <support@flutterflow.io>

---

### Declare Advertising ID for Android 13+ in Play Console {#declare-advertising-id-for-android-13-in-play-console}

*If your app targets Android 13 (API 33) or higher, Google Play requires that you declare whether your app uses the Advertising ID. Failing to do so will result in an upload error when submitting artifacts to the Play Console.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/declare-advertising-id-android-13-play-console

If your app targets Android 13 (API 33) or higher, Google Play requires that you declare whether your app uses the **Advertising ID**. Failing to do so will result in an upload error when submitting artifacts to the Play Console.

Prerequisites

* Your app targets Android 13 (API 33) or above.
* The app is being submitted via the **Google Play Console**.

When uploading your app to Google Play, you may encounter this error:

```
{
"error": {
    "code": 400,
    "message": "Your app targets Android 13 (API 33) or above. You must declare the use of advertising ID in Play Console.",
    "status": "INVALID_ARGUMENT"
}
}
```

This error occurs when the required declaration for the Advertising ID is missing, incomplete, or inconsistent with your app configuration.

Google Play now requires developers targeting Android 13 (API 33) or above to explicitly declare if their app uses the **Advertising ID**.

You may see this error if:

* You didn't complete the advertising ID declaration in the Play Console.
* Your app configuration suggests ad usage but you have not declared it.
* Your declaration is incomplete or missing required details.

Follow the steps below to fix this error:

1. **Open App Content Section in Play Console:**

   * Log into your **Google Play Console**.

   * Navigate to your app's **App Content** section.

     ![](https://docs.flutterflow.io/assets/images/20250430121230522324-4cc8e39aca512a60d499496ffd4f5c83.png)

2. **Declare Advertising ID Usage**

   * If your app **does not contain ads**, select **No** under the "Advertising ID" section.

   ![](https://docs.flutterflow.io/assets/images/20250430121230823138-2950ce06ec96a32cb831f17acdf336b1.png)

   * If your app **contains ads**, select **Yes** and provide the necessary details about how ads are used.

     This Declaration is important because Google Play uses this information to:

     * Inform users about your app’s data collection practices.
     * Ensure compliance with privacy policies.
     * Prevent build upload failures.

If the issue persists after following these steps, please contact FlutterFlow Support via Chat or email at <support@flutterflow.io>.

---

### Error Running Pod Install {#error-running-pod-install}

*This article addresses the common Error Running Pod Install issue, which typically occurs due to misconfiguration of Flutter or CocoaPods on macOS devices.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/error-running-pod-install

This article addresses the common **Error Running Pod Install** issue, which typically occurs due to misconfiguration of Flutter or CocoaPods on macOS devices.

Prerequisites

* Flutter is installed on your development machine.
* You are working on a macOS device.
* Basic familiarity with terminal commands.

#### Steps to Fix Error Running Pod Install:

1. Verify Flutter is set up correctly by following the official guide: **[Flutter - Get Started: Install on macOS](https://docs.flutter.dev/get-started/install/macos)**.

2. For troubleshooting specific to macOS, consult this guide: **[Troubleshooting Flutter on macOS](https://docs.flutter.dev/get-started/install/macos/mobile-ios#install-cocoapods)**.

3. Run `flutter doctor` in the terminal to check for missing dependencies or configuration issues.

4. Ensure CocoaPods is installed and up to date by running the following commands:

   ```
   sudo gem install cocoapods
   pod repo update
   ```

5. If the problem persists, try deleting the CocoaPods cache and reinstalling:

```
flutter clean
```

```
flutter pub get
```

```
cd ios
```

```
pod install
```

Deleting the `ios/Pods` directory and `ios/Podfile.lock` file before running `pod install` can help resolve lingering CocoaPods issues.

---

### Fix Flutter Launcher Icons Package Error {#fix-flutter-launcher-icons-package-error}

*This article describes how to resolve the flutter_launcher_icons package error that may occur during app build or deployment.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/fix-launcher-icons-package-error

This article describes how to resolve the **[flutter\_launcher\_icons package](https://pub.dev/packages/flutter_launcher_icons)** error that may occur during app build or deployment.

Prerequisites

* Access to your FlutterFlow project.
* Ability to open and edit the `pubspec.yaml` file.
* Familiarity with your build environment (FlutterFlow, GitHub, or IDE).

**Understanding the Error:**

During the build process, you might see the following error message:

```
Codemagic Deploy Output Failed Step: Generate Launch Icon Could not find package "flutter_launcher_icons". Did you forget to add a dependency? pub finished with exit code 65. Build failed: Step 5 script 'Generate Launch Icon' exited with status code 65.
```

This error indicates that the **flutter\_launcher\_icons** package is missing or not configured correctly.

Follow the steps below to fix the error:

1. **Clear and Reset App Assets in FlutterFlow:**

   * Navigate to **Settings and Integrations** > **App Assets** inside FlutterFlow.

   * If the **Splash Screen** and **Launcher Icon** are set:

     * Clear both assets.
     * Re-upload the launcher icons.

     ![](https://docs.flutterflow.io/assets/images/20250430121327988277-fb0bf90a2c5c2fb0d4b1dddccbfe14ad.gif)

2. **`Add flutter_launcher_icons` Package in GitHub Deployment** If you are deploying via GitHub and encounter this error, add the package to your `pubspec.yaml` file:

   * Open your `pubspec.yaml` file.

   * Add the following under `dev_dependencies`:

     ```
     dev_dependencies:
     flutter_launcher_icons: "^0.10.0"

     flutter_icons:
     android: true
     ios: true
     image_path_ios: "assets/images/launcher/ios.png"
     image_path_android: "assets/images/launcher/android.png"
     ```

     * \**flutter\_launcher\_icons*: "^0.10.0" specifies the package version.
     * `image_path_ios` and `image_path_android` specify the paths to your launcher icon images.
     * Ensure the image files exist at the specified paths.

3. **Run the following commands in your terminal or IDE:**

   ```
   flutter pub get
   ```

   ```
   flutter pub run flutter_launcher_icons:main
   ```

   ```
   flutter run
   ```

   `flutter pub get` fetches packages.

   `flutter pub run flutter_launcher_icons:main` generates launcher icons.

   `flutter run` builds and runs the app.

If the issue persists after following these steps, contact FlutterFlow Support at <support@flutterflow.io>.

---

### Google Play Draft Release Error {#google-play-draft-release-error}

*When uploading an app to Google Play, you may encounter the following error:*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/google-play-draft-release-error

When uploading an app to Google Play, you may encounter the following error:

```
{
  "error": {
    "code": 400,
    "message": "Only releases with status draft may be created on draft app.",
    "status": "INVALID_ARGUMENT"
  }
}
```

This error occurs because Google Play only allows creating a Draft Release if your app is still marked as a draft in the Google Play Console. Typically, this means some required app information in the Play Console has not been completed, preventing full release submission.

Prerequisites

* Your app is registered in the Google Play Console.
* Basic app details such as store listing and setup information are ready to be filled.

This error indicates that Google Play only allows you to create a **Draft Release** when your app is still marked as a draft in your Google Play Console. You likely have missing or incomplete app information in Google Play preventing full release submission.

Follow these steps to fix the issue:

1. Complete All Required Information in Google Play Console

   * Log in to your **Google Play Console**.

   * Complete all mandatory sections under:

     * **App Content**
     * **Store Listing**
     * **Pricing & Distribution**
     * **Target Audience & Content Rating**

     Google Play requires all required information to be filled out before allowing full production releases.

2. **Enable "Submit As Draft" in FlutterFlow**

   After completing your app information, proceed as follows:

   * **Open Settings and Integrations**: From your FlutterFlow project dashboard, navigate to **Settings > Integrations**.

     ![](https://docs.flutterflow.io/assets/images/20250430121320431269-11151722194c41cf6f4b090e04863662.png)

   * **Navigate to Mobile Deployment**: Select **Mobile Deployment**.

     ![](https://docs.flutterflow.io/assets/images/20250430121320759595-d43561d2552198d967e63415a52a152c.png)

   * **Enable Submit As Draft**: Under **Google Play Store Deployment**, toggle on **Submit as Draft**.

     ![](https://docs.flutterflow.io/assets/images/20250430121321051936-e566e7f0a931aff1babd68a214530c68.png)

     This allows you to submit your release as a draft until all Google Play requirements are fully satisfied.

If you’ve followed all steps and still encounter the issue, contact **FlutterFlow Support** via Chat or email at <support@flutterflow.io> for additional assistance.

---

### Google Play Failed to Upload Artefacts {#google-play-failed-to-upload-artefacts}

*- Ensure your app’s Package Name in FlutterFlow matches the package name in Google Play Console.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/google-play-failed-to-upload-artefacts-package

Prerequisites

* Ensure your app’s `Package Name` in FlutterFlow matches the package name in Google Play Console.
* Firebase is configured in your project settings.
* Your Google Play Console account is active and accessible.

When uploading your app to Google Play, you may encounter the following error:

```
Google Play failed to upload artefacts. Package not found: com.flutterflow.appname.: {
  "error": {
    "code": 404,
    "message": "Package not found: com.flutterflow.appname.",
    "status": "NOT_FOUND"
  }
}
```

This error usually occurs in two scenarios:

* Deploying the app to Google Play for the first time.
* Changing the app’s `Package Name` in FlutterFlow without regenerating the Firebase configuration files.

**First Time Deployment to Google Play**

Follow these steps to upload your app for the first time:

1. Generate your build in FlutterFlow and click the `AAB` button to download the build artifact.

2. Log in to your **[Google Play Console](https://play.google.com/console)**.

3. Navigate to your app project and upload the **AAB** file as a new release in the appropriate track (Internal, Closed, Open, or Production).

4. After this initial upload, future deployments should proceed without this error.

   ![](https://docs.flutterflow.io/assets/images/20250430121330484821-3b5795c533eecbd6fce52a72506ed56e.png)

**Updating Package Name and Regenerating Config Files**

If you have updated your app’s `Package Name` in FlutterFlow, follow these steps:

1. Open your project in FlutterFlow.

2. Navigate to **Settings** > **Firebase**.

3. Click **Regenerate Config Files**.

   ![](https://docs.flutterflow.io/assets/images/20250430121330727549-7e216628b1bef45cd6867c86b6fd659e.png)

4. Enter the new `Package Name` and click Generate File to download the updated configuration files.

   ![](https://docs.flutterflow.io/assets/images/20250430121331069027-992a83c99d1aaac98c6db7838fa1782e.png)

5. Rebuild and redeploy your app to confirm the error is resolved.

If the error persists after completing these steps:

* Verify the `Package Name` matches exactly between FlutterFlow and Google Play Console.
* Confirm that Firebase configuration files have been updated correctly.
* Contact FlutterFlow Support via Chat or email at <support@flutterflow.io>.

---

### Google Play Store Debug Signing Error {#google-play-store-debug-signing-error}

*When uploading your Android App Bundle (AAB) or APK to Google Play, you might encounter this error:*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/google-play-store-debug-signing-error

When uploading your Android App Bundle (AAB) or APK to Google Play, you might encounter this error:

```
You uploaded an APK or Android App Bundle that was signed in debug mode. You need to sign your APK or Android App Bundle in release mode
```

This error indicates the app must be signed with a release key before uploading.

Prerequisites

* Access to the Android project files.
* Familiarity with editing Gradle build files.

**Steps to Fix Debug Signing Error:**

1. Open the `android/app/build.gradle` file in your project folder.

2. Locate the `buildTypes` section and find the configuration labeled `debug`.

3. Replace the `debug` keyword with `release` in the relevant signing configuration.

   ![](https://docs.flutterflow.io/assets/images/20250430121513060363-77131e391e5a3c171d3df0f670cec56f.png)

4. Save the file.

   ![](https://docs.flutterflow.io/assets/images/20250430121513225263-f3ae36bad62799f7c0ecbd08ee31e724.png)

   note

   Make sure that you fill out all the information in the play store including the store listing information and the setup information.

​

---

### Launcher Icon Missing After Upload {#launcher-icon-missing-after-upload}

*Custom app launcher icons may fail to appear after being added in the project settings due to missing icon generation steps.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/launcher-icon-missing-after-upload

Custom app launcher icons may fail to appear after being added in the project settings due to missing icon generation steps.

Prerequisites

* Flutter is installed on your development machine.
* The project code has been downloaded or exported.
* Basic familiarity with running terminal commands.

**Steps to Resolve Missing Launcher Icon:**

1. Run the launcher icon generation command in the terminal at your project root:

   ```
   flutter pub run flutter_launcher_icons:main
   ```

   This generates the necessary launcher icon assets for your app.

2. Ensure your Flutter environment is properly set up. If needed, follow the official **[Flutter installation guide](https://docs.flutter.dev/get-started/install)**.

   * Verify your icon files are named correctly and placed in the appropriate directory.
   * Check that your `pubspec.yaml` includes the correct `flutter_launcher_icons` configuration.
   * Run `flutter clean` in your project directory before rerunning the icon generation command to clear caches.

---

### Migrate to Play Integrity API From SafetyNet Attestation {#migrate-to-play-integrity-api-from-safetynet-attestation}

*Google is deprecating the SafetyNet Attestation API, replacing it with the Play Integrity API. This article explains the migration steps needed to maintain app security and compliance with Google Play requirements.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/migrate-to-play-integrity-api-from-safetynet-attestation

Google is deprecating the **SafetyNet Attestation API**, replacing it with the **Play Integrity API**. This article explains the migration steps needed to maintain app security and compliance with Google Play requirements.

Prerequisites

* The **SafetyNet Attestation API** is currently used in your Android app.
* Preparation for app deployment or maintenance on Google Play is underway.

**Migration Steps:**

1. **Begin the Migration Process**; Visit the official migration guide: **[SafetyNet Deprecation & Play Integrity Migration Guide](https://developer.android.com/google/play/integrity/migrate)**

2. **Update Your Backend Implementation**

   * Replace calls to the **SafetyNet Attestation API** with the **Play Integrity API** in your app code.
   * Modify your backend to validate responses from the Play Integrity API.

3. **Test Your Migration Thoroughly**; Verify that the Play Integrity API integration works correctly on multiple devices before publishing updates.

> **Tip:** Migrating is critical to:

* Comply with the latest security standards.
* Maintain access to Google's integrity services.
* Benefit from improved error handling and security signals.; Failure to migrate may cause degraded app functionality and user experience.

If issues arise during migration, contact FlutterFlow Support at <support@flutterflow.io>.

---

### Signed in Debug Mode Error {#signed-in-debug-mode-error}

*- Generated an APK or Android App Bundle via FlutterFlow → Build → Android.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/signed-in-debug-mode-error

Prerequisites

* Generated an APK or Android App Bundle via **FlutterFlow → Build → Android**.
* Access to the exported project folder.
* Ability to edit the `android/app/build.gradle` file.

When uploading an Android APK or App Bundle to the Play Store or a production environment, the following error may occur:

```
You uploaded an APK or Android App Bundle that was signed in debug mode. You need to sign your APK or Android App Bundle in release mode
```

This error indicates that the build was signed with a debug configuration, which is only for internal testing and not valid for production release.

To fix this, update the `build.gradle` file to use the release signing configuration.

**Steps to Update Build Configuration:**

1. Open the `android/app/build.gradle` file in your project folder.
2. Locate the `debug` keyword under `buildTypes`.
3. Replace the `debug` keyword with `release` and save the file.

If the issue persists, contact FlutterFlow Support at <support@flutterflow.io>.

---

### Version Solving Failed Due to Incompatible Package {#version-solving-failed-due-to-incompatible-package}

*A version solving failed error may occur when running flutter pub get if package versions in the project conflict with FlutterFlow's supported Flutter version.*

**Source:** https://docs.flutterflow.io/troubleshooting/google-play-store-deployment/version-solving-failed-due-to-incompatible-package

A **version solving failed** error may occur when running `flutter pub get` if package versions in the project conflict with FlutterFlow's supported Flutter version.

```
Running "flutter pub get" in flutter_tools... 3.4s
Resolving dependencies...
Because every version of flutter_test from sdk depends on collection 1.15.0
and horse_care_new depends on collection 1.16.0,
flutter_test from sdk is forbidden.
So, because horse_care_new depends on flutter_test from sdk,
version solving failed.
pub finished with exit code 1
```

Prerequisites

* Custom actions or widgets are used in the project.
* Access to the project's `pubspec.yaml` file.

**Steps to Resolve the Error:**

* Verify that all packages used in custom actions or widgets are compatible with FlutterFlow's Flutter version.

* Before adding a new dependency in your custom widget or action, check if the package already exists in `pubspec.yaml`. If it does, only import the package in your code without adding it again as a dependency.

* If no custom widgets or actions are used and the error persists, contact FlutterFlow Support at <support@flutterflow.io> for assistance.

---

### FCM Token Generation Troubleshooting {#fcm-token-generation-troubleshooting}

*When a user does not have an fcmtoken sub-collection in their Firestore document, push notifications cannot be delivered to their device. This guide outlines the possible causes and solutions for resolving missing fcmtoken sub-collections in FlutterFlow apps.*

**Source:** https://docs.flutterflow.io/troubleshooting/notifications/fcm-token-generation-troubleshooting

When a user does not have an `fcm_token` sub-collection in their Firestore document, push notifications cannot be delivered to their device. This guide outlines the possible causes and solutions for resolving missing `fcm_token` sub-collections in FlutterFlow apps.

**Understanding the Issue**

Push notifications require a valid Firebase Cloud Messaging (FCM) token, which is generated when a user logs in or signs up on a physical device. This token is typically stored in the `fcm_token` sub-collection of the user document in Firestore. If this sub-collection is missing, the device cannot receive push notifications.

Possible causes for missing tokens include:

* Failures during FCM token generation.
* Incomplete authentication flows.
* Permission issues preventing token creation.
* Invalid input data passed to Cloud Functions.

Here are the steps to verify user eligibility for push notifications:

1. Check Firestore for `fcm_token` Sub-Collection

   1. Open the **Firebase Console**.
   2. Navigate to **Firestore Database**.
   3. Locate the user document.
   4. Verify that the `fcm_token` sub-collection exists.

   If present, the user is eligible to receive push notifications.

   ![](https://docs.flutterflow.io/assets/images/20250430121302960895-54aed4f3798bc79637d975fd9c18488a.png)

##### Troubleshooting Missing FCM Token Generation

1. **Verify Cloud Function Execution**

   The `addFcmToken` Cloud Function is responsible for generating and storing FCM tokens. If token generation fails, review its logs:

   1. Open the **Firebase Console**.
   2. Navigate to **Functions**.
   3. Locate the `addFcmToken` function.
   4. Open its **Logs** to review errors or warnings.

   ![](https://docs.flutterflow.io/assets/images/20250430121303270464-01b82a1aec0dec61adb6565fa42ee0ee.png)

2. **Resolve Permission Errors**

   Proper permissions are required to allow the Cloud Function to write FCM tokens to Firestore.

   **Verify Firebase Security Rules**

   * Ensure your Firebase security rules permit writing to the `users` collection and its sub-collections.

   **Verify FlutterFlow Service Account Permissions**

   The `firebase@flutterflow.io` service account must have the following roles:

   * `Editor`
   * `Cloud Functions Admin`
   * `Service Account User`

   **How to Assign Roles**:

   1. Open the **Firebase Console**.
   2. Go to **Project Settings > Users & Permissions**.
   3. Locate the `firebase@flutterflow.io` service account.
   4. Assign any missing roles.

   Refer to **[this guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#connect-an-existing-firebase-project-manually)** for full instructions.

3. **Validate Input Data Passed to Cloud Function**

   If a Cloud Function fails with status code `400`, it may be receiving invalid input data.

   * Verify that your authentication flow correctly retrieves the user ID before calling the function.
   * Ensure the user ID is not `null`, empty, or malformed.
   * Implement conditional validation before invoking the function.
   * Add logging to your authentication code and Cloud Functions to trace failures.

   This is especially important if you are using custom authentication logic. If you are using FlutterFlow's built-in authentication, this issue is unlikely.

4. **Check for FCM Server Errors**

   Additional reasons FCM token generation may fail include:

   * FCM server downtime or temporary outages.
   * Incorrect or malformed requests sent from the Cloud Function to the FCM server.
   * Insufficient API access permissions.
   * Invalid or missing input data (e.g. device token).

   If server issues persist, consider contacting Firebase support for assistance.

By following this complete troubleshooting process, you can ensure your users successfully receive push notifications.

***

---

### Firebase Push Notification Troubleshooting {#firebase-push-notification-troubleshooting}

*Push notifications are essential for keeping users informed through timely alerts and updates. However, several common configuration issues can prevent push notifications from working as expected in FlutterFlow projects. This guide outlines potential causes and solutions.*

**Source:** https://docs.flutterflow.io/troubleshooting/notifications/firebase-push-notification-troubleshooting

Push notifications are essential for keeping users informed through timely alerts and updates. However, several common configuration issues can prevent push notifications from working as expected in FlutterFlow projects. This guide outlines potential causes and solutions.

Prerequisites

Before troubleshooting, ensure the following:

* The FlutterFlow app is connected to Firebase.
* The app is installed on a physical device (push notifications do not work on simulators).
* The user is logged in to the app.
* The app is not currently open when testing notifications.

1. **Verify Firebase Blaze Plan Subscription**

   * Navigate to **Firebase Console > Project Settings > Usage & Billing > Details & Settings**.
   * Confirm that the subscription is on the **Blaze Plan**.
   * If the current plan is **Spark**, upgrade by selecting **Modify Plan**.

   ![](https://docs.flutterflow.io/assets/images/20250430121514497717-35f747df9e6f0c6dc8a48f2d4df1db3e.png)

2. Verify Apple Push Notification (APN) Key Configuration

   * **Create an APN Key:**

     * Navigate to the Apple Developer Console.
     * Go to **Certificates, Identifiers & Profiles > Keys**.
     * Create a new key for push notifications if one does not exist.

     ![](https://docs.flutterflow.io/assets/images/20250430121514756330-9d82a66a1e7e3b46bdd41497816f5079.png)

     Instructions for **[adding a push notification key](https://developer.apple.com/account/resources/authkeys/list)**

   * **Upload the APN Key to Firebase**

     * Navigate to **Firebase Console > Project Settings > Cloud Messaging > iOS section**.
     * Upload the APNs Authentication Key.

     ![](https://docs.flutterflow.io/assets/images/20250430121515088626-084ba92102053aa15ae7a97621159519.png)

     Instructions for **[uploading APN key to Firebase](https://firebase.google.com/docs/cloud-messaging/ios/certs)**.

3. **Create Push Notification Identifier for Apple**

   * Go to the Apple Developer Console.
   * Navigate to **Certificates, Identifiers & Profiles > Identifiers**.
   * Create or verify an identifier for push notifications.

   ![](https://docs.flutterflow.io/assets/images/20250430121515418578-7f61320f7d4fe81294cf8228e2df56fd.png)

   Instructions for **[creating a push notification identifier](https://developer.apple.com/account/resources/identifiers/list)**.

4. **Verify Cloud Permissions for FlutterFlow Service Account**

   * Go to **Firebase Console > Project Settings > Users & Permissions**.

   * Locate the **<firebase@flutterflow.io>** service account.

   * Ensure the following roles are assigned:

     * Editor
     * Cloud Functions Admin
     * Service Account User

   ![](https://docs.flutterflow.io/assets/images/20250430121515666267-f0e035f033238446b162c7eacbb6af13.png)

   Instructions to **[add required cloud permissions](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project)**.

5. **Confirm Cloud Function Region Consistency**

   * In **FlutterFlow > Settings > Firebase > Advanced Settings**, verify the Cloud Functions Region matches the region configured in **Firebase > Project Settings > Cloud Functions Location**.

   ![](https://docs.flutterflow.io/assets/images/20250430121515990341-cb8dfe481eb7782d65eedc674d617f20.png)

   ![](https://docs.flutterflow.io/assets/images/20250430121516228961-e32ba97b88a386f77aa588720976f146.png)

6. **Update FlutterFlow to Latest Version**

   **Refresh FlutterFlow:**

   * On Windows: Press `Ctrl + R`.
   * On Mac: Press `Cmd + R`.

   **Clear Browser Cache:** Clear the browser cache to ensure the latest version loads properly.

7. **Resolve FlutterFlow Insufficient Permissions Error**

   If an insufficient permissions error occurs:

   1. Open **Firebase Console > Project Settings > Users & Permissions**.

   2. Verify the **<firebase@flutterflow.io>** account exists.

   3. Assign the following permissions:

   * Editor
   * Cloud Functions Admin
   * Service Account User

   ![](https://docs.flutterflow.io/assets/images/20250430121516955662-6322dcfe8d6656e3d837fdc3e1bd3928.png)

   4. Save changes and retry the operation in FlutterFlow.

   ![](https://docs.flutterflow.io/assets/images/20250430121517242675-be5188a887ac9adbfdd77e1f2148702a.png)

---

### Firebase Push Notifications on Web {#firebase-push-notifications-on-web}

*FlutterFlow currently does not support sending Firebase push notifications on web apps natively. However, Firebase itself supports this capability. This guide outlines alternative approaches to enable Firebase push notifications on web projects built with FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/notifications/firebase-push-notifications-on-web

FlutterFlow currently does not support sending Firebase push notifications on web apps natively. However, Firebase itself supports this capability. This guide outlines alternative approaches to enable Firebase push notifications on web projects built with FlutterFlow.

#### Workarounds for Implementing Web Push Notifications

There are two primary methods to implement Firebase web push notifications in FlutterFlow projects:

* **Use Custom Actions:**

  * Create custom actions in FlutterFlow that utilize Firebase Cloud Messaging (FCM) to send push notifications.
  * This method requires writing custom code to handle notification logic and integrate it into FlutterFlow.
  * Custom actions offer flexibility for handling different types of notifications based on the app’s needs.
  * The Firebase Web SDK can be used alongside your FlutterFlow project to achieve this.

  Refer to official Firebase documentation for detailed steps on **[setting up web push notifications](https://firebase.google.com/docs/cloud-messaging/js/client)**.

* **Use Back-End Functions:**

  * Implement server-side code using Firebase Functions or any other backend service.
  * Backend functions handle sending notifications independently of the FlutterFlow frontend.
  * This approach allows using the Firebase Admin SDK to programmatically send push notifications to targeted web clients.
  * Backend solutions also offer better scalability, error handling, and control over notification delivery.

> **Note:** * Web push notification support requires properly configured Firebase Cloud Messaging, service workers, and valid VAPID keys.
* FlutterFlow may add native support for web push notifications in future updates as the platform evolves.

---

### Fix Insufficient Permissions for Push Notifications {#fix-insufficient-permissions-for-push-notifications}

*If you encounter an "Insufficient Permissions" error when deploying push notifications from FlutterFlow to Firebase, it usually means the firebase@flutterflow.io service account does not have the necessary permissions in your Firebase project. This guide will walk you through how to resolve this issue.*

**Source:** https://docs.flutterflow.io/troubleshooting/notifications/fix-insufficient-permissions-push-notifications

If you encounter an **"Insufficient Permissions"** error when deploying push notifications from FlutterFlow to Firebase, it usually means the `firebase@flutterflow.io` service account does not have the necessary permissions in your Firebase project. This guide will walk you through how to resolve this issue.

Prerequisites

Before proceeding, ensure you have:

* Connected your Firebase project to FlutterFlow.
* Completed the steps in **[Connect to Firebase](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project)**.

**Steps to Resolve the Insufficient Permissions Error:**

1. **Open Firebase Console**

   * Go to the **[Firebase Console](https://console.firebase.google.com/)**.
   * Click on your project tile to open your FlutterFlow project.

2. **Navigate to Users & Permissions:**

   * In the Firebase project dashboard, click on the gear icon (⚙️) to open **Project Settings**.

   * From the left sidebar, select **Users & Permissions**.

     ![](https://docs.flutterflow.io/assets/images/20250430121228826304-9171280a069d17c7274a0b43294ac183.png)

3. **Locate the `firebase@flutterflow.io` Account**

   * In the **Users** tab, search for `firebase@flutterflow.io`.
   * If this account is missing, click **Add User**, enter `firebase@flutterflow.io` as the email address, and continue.

4. **Assign the Required Permissions**

   * Click on `firebase@flutterflow.io` to open the user details.

   * Ensure the following roles are assigned:

     * **Editor**

     * **Cloud Functions Admin**

     * **Service Account User**

       ![](https://docs.flutterflow.io/assets/images/20250430121229163844-6322dcfe8d6656e3d837fdc3e1bd3928.png)

     * If any permissions are missing, click **Add Permissions** and select the missing roles.

5. **Save Changes:**

   * After assigning all necessary roles, click **Save** to apply changes.
   * Verify that all permissions have been successfully added and saved.

6. **Retry the Operation in FlutterFlow:**

   * Return to your FlutterFlow project.
   * Retry the action that previously failed due to insufficient permissions.

   The error should now be resolved. If you continue to experience issues, please contact the FlutterFlow Support team.

> **Note:** Granting the correct permissions to `firebase@flutterflow.io` is essential for FlutterFlow to deploy push notifications and access Firebase resources correctly.

![](https://docs.flutterflow.io/assets/images/20250430121229476348-be5188a887ac9adbfdd77e1f2148702a.png)

Additional Resources

* [Connect FlutterFlow to Firebase](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#allow-flutterflow-to-access-your-project)
* [Firebase Roles and Permissions](https://firebase.google.com/docs/projects/iam/roles)

---

### Fix Push Notifications Sent to Zero Devices {#fix-push-notifications-sent-to-zero-devices}

*Push notifications allow apps to send updates, alerts, and messages directly to users. In some cases, after triggering a push notification, FlutterFlow displays the following message:*

**Source:** https://docs.flutterflow.io/troubleshooting/notifications/fix-push-notifications-sent-to-zero-devices

Push notifications allow apps to send updates, alerts, and messages directly to users. In some cases, after triggering a push notification, FlutterFlow displays the following message:

```
Push Notification sent to 0 devices
```

This means that the notification was attempted, but no eligible devices received it.

Here are the causes:

* No registered devices have generated FCM tokens.
* Target devices were offline at the time of sending.
* Misconfiguration in Firebase or FlutterFlow settings.
* Missing permissions or API configuration.
* Recipient devices have blocked push notifications.

The following steps below outline how to troubleshoot and resolve this issue:

1. **Verify Firebase Functions Are Enabled**

   * Ensure that Firebase Functions are enabled in the Firebase Console.
   * Confirm that your project is on the Blaze Plan.

   ![](https://docs.flutterflow.io/assets/images/20250430121213011292-1babf61949379581747118828e03c164.png)

2. **Delete and Redeploy Firebase Cloud Functions**

   * Manually delete the Cloud Functions related to push notifications from Firebase.

     ![](https://docs.flutterflow.io/assets/images/20250430121213284704-3afcc81ff3752e6b58e4d2e156ee73c5.png)

   * After deletion, redeploy Push Notifications from FlutterFlow:

     ![](https://docs.flutterflow.io/assets/images/20250430121213612267-3689521eba4ddac2ee7b5144c76dfcf6.png)

3. **Verify Server Region Configuration**

   * Ensure that the Firebase server region matches the configuration in FlutterFlow.

   * For example, if the server region is `us-central1`, it must match in both Firebase and FlutterFlow.

     In FlutterFlow: Navigate to **Settings > Firebase > Advanced Settings** and set the correct region.

     ![](https://docs.flutterflow.io/assets/images/20250430121214190877-0f8fa7167e3863fd0e98d1b7932ee2ac.png)

     In Firebase: Verify that Cloud Functions are deployed to the same region.

     ![](https://docs.flutterflow.io/assets/images/20250430121214486513-73b41f5de85f618a905f3d41ab672a67.png)

4. **Check FCM API Settings in Google Cloud Console**

   * Open the **[Google Cloud Console](https://console.cloud.google.com/)**.

   * Search for `FCM API` and ensure it is enabled.

     ![](https://docs.flutterflow.io/assets/images/20250430121214790195-9418483016c92cf5d1f7acfaa3b1b71c.png)

   * Make sure that a valid server key is available in Firebase Console. If missing, create one through Google Cloud Console.

5. **Verify Cloud Permissions for flutterflow\.io Service Account**

   To ensure proper communication between FlutterFlow and Firebase:

   * Step 1: Open Firebase Console

     * Go to [Firebase Console](https://console.firebase.google.com/).
     * Select your project.

   * Step 2: Navigate to Users & Permissions

     * Open **Project Settings** via the gear icon (⚙️).

     * Select **Users & Permissions**.

       ![](https://docs.flutterflow.io/assets/images/20250430121215127010-9171280a069d17c7274a0b43294ac183.png)

   * Step 3: Verify Existing Permissions

     * Locate the `firebase@flutterflow.io` service account.

     * Verify the following roles are assigned:

       * `Editor`
       * `Cloud Functions Admin`
       * `Service Account User`

       ![](https://docs.flutterflow.io/assets/images/20250430121215442199-6322dcfe8d6656e3d837fdc3e1bd3928.png)

   * Step 4: Add Missing Permissions

     * If any roles are missing: * Click **Add Member**.

       * Enter `firebase@flutterflow.io`.

       * Select missing roles from the dropdown: * `Editor`
         * `Cloud Functions Admin`
         * `Service Account User`

     ![](https://docs.flutterflow.io/assets/images/20250430121215729191-be5188a887ac9adbfdd77e1f2148702a.png)

   * Step 5: Verify All Permissions Are Applied

     * Confirm that all required roles now appear next to the service account.

Following these steps should resolve most push notification delivery issues.

---

### Black Screen During Preview {#black-screen-during-preview}

*If your app screen appears blank during Run Mode, follow these steps to resolve the issue:*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/black-screen-during-run-mode

If your app screen appears blank during Run Mode, follow these steps to resolve the issue:

Prerequisites

* You have already built and deployed at least one screen in your project.
* You are running the app in **Run Mode** within the editor.

1. **Reload the Frame**

   Right-click on the preview screen and select **Reload Frame**.

2. **Change the Device**

   Use the device selector on the left panel to switch to a different preview device.

3. **Refresh the Page**

   Press `Ctrl + R` (Windows) or `Cmd + R` (Mac) to refresh the browser.

4. **Update FlutterFlow and Clear Cache**

   * Ensure you are using the latest version.
   * Clear your browser cache.
   * Log out and back in to your FlutterFlow account.

5. **Submit a Bug Report**

   If none of the steps work, submit a bug report using the **Send Feedback** button in FlutterFlow.

   ![](https://docs.flutterflow.io/assets/images/20250430121528287666-5ce70b2435c1ba565426093b5f908131.png)

> **Tip:** Blank screens are often temporary. Try switching devices or reloading before making major changes to your project.

---

### Firestore Permission Error in Run Mode {#firestore-permission-error-in-run-mode}

*When previewing your app in Run Mode, you may encounter the following error message:*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/firestore-permission-error-run-mode

When previewing your app in Run Mode, you may encounter the following error message:

**Firestore Security Rules: Missing or insufficient permissions**

This occurs when your Firestore rules conflict with the permissions required for a query in your app.

Prerequisites

* You are using Firebase Firestore in your FlutterFlow project.
* Your project has one or more Firestore queries configured.

This error is typically triggered when:

* Firestore rules prevent any user from reading the database.
* A page attempts to run a query before a user is authenticated (e.g., querying user-specific data on the login page).

Example:

* If Firestore rules are configured as:

```
  rules_version = '2';
  service cloud.firestore {
    match /databases/{database}/documents {
      match /{document=**} {
        allow read, write: if false;
      }
    }
  }
```

Any Firestore query will fail because no read or write access is allowed.

* If rules allow only authenticated access:

  ```
    allow read, write: if request.auth != null;
  ```

  And a query is placed on a page before the user signs in (e.g., on the login screen), it will trigger this error.

  Descriptive widget names can help you quickly identify which query or widget is triggering the permission issue. In the example above, the error message references a widget named Container. Renaming it to something like UserQueryContainer can make debugging easier.

Take the steps below to fix this error:

* **Review Firestore Rules**

  Go to Firestore → Settings → Rules and verify that your access rules align with how and when your app queries the database.

* **Adjust Query Placement**

  Ensure that queries requiring authentication are not used on screens accessible to unauthenticated users.

* **Use Conditional Visibility**

  If a query must exist on a pre-login screen, wrap it in conditional logic to only execute when the user is signed in.

> **Tip:** Test queries using the Run Mode Console and check the browser logs for more specific errors. Use Firestore Schema Validation in FlutterFlow to ensure your rules are properly deployed.

---

### Gray Screen in Run Mode {#gray-screen-in-run-mode}

*Seeing a gray screen in Run Mode usually points to a configuration issue in your Firebase or project settings. Follow these steps to diagnose and resolve the issue.*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/gray-screen-run-mode

Seeing a gray screen in Run Mode usually points to a configuration issue in your Firebase or project settings. Follow these steps to diagnose and resolve the issue.

Prerequisites

* You have integrated Firebase with your FlutterFlow project.
* You have access to your Firebase Console.

1. **Check Firebase Permissions**

   Ensure that <firebase@flutterflow.io> has the following roles:

   * **Editor**
   * **Cloud Functions Admin**
   * **Service Account User**

   To verify:

   1. Go to the **Firebase Console**.

   2. Select your project → **Project Overview**.

   3. Navigate to **Users and permissions** → **Advanced permissions**.

   4. Locate <firebase@flutterflow.io> and ensure it has the roles listed above.

      ![](https://docs.flutterflow.io/assets/images/20250430121529462395-fdde1719fe77b55aa50ec3df4e3744b0.png)

   If missing, click the pencil icon and assign the roles.

2. **Regenerate Firebase Configuration Files**

   1. In FlutterFlow, go to **Settings & Integrations** → **Firebase**.

   2. Click **Regenerate Config Files**.

   3. In the popup, click **Generate Files**.

      ![](https://docs.flutterflow.io/assets/images/20250430121530070855-7e8912c83c1c2afb165d4762e7e4d84d.png)

      tip

      You must regenerate config files if you change your project name in FlutterFlow or Firebase.

3. **Update Firebase Rules**

   1. In FlutterFlow, go to **Firestore** → **Settings**.
   2. Scroll to **Firestore Rules** and click **Deploy**.
   3. Confirm by selecting **Deploy Now** in the popup.

   ![](https://docs.flutterflow.io/assets/images/20250430121530401837-7055a97d7146894eafc1a13985ef7065.jpg)

   A green checkmark indicates success.

4. **Validate Firebase Schema**

   1. In **Firestore** → **Settings**, scroll to **Firebase Schema Validation**.

   2. Click **Validate**.

      ![](https://docs.flutterflow.io/assets/images/20250430121530999303-6bf58af56d0c6b82d655917f4b89ce88.jpg)

      If the schema is valid, you’ll see a success message. If not, review the identified issues.

      ![](https://docs.flutterflow.io/assets/images/20250430121531448037-98813d12cfb2a8261c32e01bb494151c.png)

5. **Ensure Collections Have Data**

   An empty Firestore collection can result in a gray screen. Visit the Firebase Console → **Firestore Database** to confirm your collections contain documents.

   ![](https://docs.flutterflow.io/assets/images/20250430121531723554-2d6543b11bba69cadfb4f34b0f265649.png)

6. **Verify Custom Widget Compatibility**

   If your app uses a custom widget, make sure its package supports web. On **[pub.dev](https://pub.dev)**, check that **WEB** is listed under platforms.

   ![](https://docs.flutterflow.io/assets/images/20250430121531973906-ddd21c7e53708e9079602d171afa3222.png)

   If not, choose an alternative package.

7. **Refresh FlutterFlow Environment**

   * Press Ctrl + R (Windows) or Cmd + R (Mac) to refresh FlutterFlow.

   * Clear your browser cache.

   * Log out and back in.

     tip

     Refreshing your session can fix slow or buggy behavior in the UI Builder.

8. **Retest the Project**

   After completing the above steps, create a new Run Mode session to test if the gray screen issue is resolved.

9. **Test Locally**

   If the issue persists, download your FlutterFlow code and run the project locally to diagnose further.

Additional Resources

* **[Run Flutter App Locally](https://docs.flutterflow.io/testing/local-run)**
* **[FlutterFlow Firebase Integration Guide](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase#step-1-set-up-your-project)**

---

### Loading Spinner in Run Mode {#loading-spinner-in-run-mode}

*A persistent loading spinner in FlutterFlow's Run Mode usually indicates an issue with your Firestore rules configuration. Updating your rules can resolve this issue.*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/loading-spinner-run-mode

A persistent loading spinner in FlutterFlow's Run Mode usually indicates an issue with your Firestore rules configuration. Updating your rules can resolve this issue.

Prerequisites

* You have already connected your FlutterFlow project to Firebase.
* You have access to your Firebase Console.

Here are the steps to fix this error:

1. **Copy Firestore Rules from FlutterFlow**

   1. Open your project.
   2. Navigate to **Firestore** → **Settings**.
   3. Click the **Copy** icon to copy the default Firestore rules.

   ![](https://docs.flutterflow.io/assets/images/20250430121355282620-97cec6fdabc1b155638a88186ec7cd62.gif)

2. **Paste the Rules in Firebase Console**

   1. Open the **[Firebase Console](https://console.firebase.google.com/)**.
   2. Select your project and go to **Firestore Database**.
   3. Open the **Rules** tab.
   4. Paste the copied rules into the editor and click **Publish**.

   ![](https://docs.flutterflow.io/assets/images/20250430121355575413-0179d33777cb89357eecedad825c3070.gif)

3. **Retest Your Project in FlutterFlow**

   Return to FlutterFlow and run your project again in **Run Mode**. The loading spinner should no longer appear if the Firestore rules were configured correctly.

> **Tip:** Always keep your Firestore rules up to date after making structural changes to your database in FlutterFlow.

---

### Local Build ProviderInstaller Error {#local-build-providerinstaller-error}

*This error commonly occurs when building Flutter apps on Android emulators. It is related to the ProviderInstaller service and can typically be resolved through basic cleanup and Flutter version upgrades.*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/local-build-providerinstaller-error

This error commonly occurs when building Flutter apps on Android emulators. It is related to the `ProviderInstaller` service and can typically be resolved through basic cleanup and Flutter version upgrades.

Prerequisites

* You are testing or running your Flutter project on an Android emulator.
* You have Flutter and Android Studio installed and configured.

1. **Uninstall the App from the Emulator**

   Before rebuilding your app, ensure the old installation is removed:

   1. Open the Android Emulator.

   2. Locate your app icon and uninstall it.

   3. Alternatively, run the following command from your terminal:

      ```
      adb uninstall com.yourcompany.yourapp
      ```

      Replace com.yourcompany.yourapp with your actual app ID.

2. **Rebuild the App**

   After uninstalling:

   Run the following command in your project directory:

   ```
    flutter clean
   ```

   ```
   flutter pub get
   ```

   ```
   flutter run
   ```

   This will remove cached data and reinstall the app on the emulator.

3. **Upgrade Flutter (If Problem Persists)**

   If the issue continues, upgrading Flutter may help. Run the command below to upgrade:

   ```
   flutter upgrade
   ```

   Ensure your Flutter SDK is up to date. You can verify the version with:

   ```
   flutter --version
   ```

   note

   This error is often related to Google Play Services not being properly initialized on the emulator. If you're still encountering issues, consider creating a new emulator using a system image that includes the Play Store.

Additional Resources

* Read the official **[Flutter Build Documentation](https://docs.flutter.dev/testing/build-modes)**.
* Check **[Android Emulator System Images](https://developer.android.com/studio/run/managing-avds#system-images)**.

---

### Slow Loading in Test Mode {#slow-loading-in-test-mode}

*If Test Mode takes several minutes to load or fails entirely, the issue may stem from your browser, network, or project configuration. This guide walks you through the most common causes and how to resolve them.*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/slow-test-mode-load

If Test Mode takes several minutes to load or fails entirely, the issue may stem from your browser, network, or project configuration. This guide walks you through the most common causes and how to resolve them.

Prerequisites

* You are using FlutterFlow's Test Mode feature.
* You have already deployed or previewed a version of your app.

**Steps to Resolve Slow Loading:**

* **Check Your Internet Connection**

  A weak or unstable connection may delay the loading of compiled apps. Make sure you have a stable network before launching Test Mode.

* **Sync Your System Clock**

  Ensure your device’s time and date settings are accurate. An incorrect clock can cause authentication issues and impact performance.

* **Clear Browser Cache**

  Browsers store temporary files that may interfere with page loading. Clearing your cache can resolve stale resource conflicts and improve speed.

* **Try a Different Browser**

  Some browsers may conflict with specific web assets or settings. If one browser is slow, switch to another (e.g., from Chrome to Firefox).

* **Disable Browser Extensions**

  Extensions like ad blockers or privacy tools can interfere with FlutterFlow’s platform. Temporarily disable them to check for improvement.

Optimize Your Project

Projects with many pages, assets, or custom code may take longer to compile. Follow these steps to optimize your project:

* Remove unused images, fonts, or icons.
* Consolidate or simplify custom code.
* Limit the number of pages in a single testing session.

Additional Resources

If the issue persists after following the steps above, check the **[official support](https://intercom.help/flutterflow/en/articles/7052737-test-mode-is-not-loading-or-is-very-slow-it-takes-a-long-time-to-load-the-app)** article.

Following these steps should resolve most Test Mode performance issues and reduce load times for future previews.

---

### Test API Calls {#test-api-calls}

*Verifying an API response before integrating it into your app helps prevent runtime issues and ensures your data is structured correctly. This guide walks you through testing an API directly within FlutterFlow.*

**Source:** https://docs.flutterflow.io/troubleshooting/test-mode/test-api-calls

Verifying an API response before integrating it into your app helps prevent runtime issues and ensures your data is structured correctly. This guide walks you through testing an API directly within FlutterFlow.

Prerequisites

* A project is open in FlutterFlow.
* An API key or endpoint is available if required by the API.

**Steps to Test API Calls:**

1. **Open the `API Calls` Panel**

   From the left sidebar, go to the `API Calls` section.

   ![](https://docs.flutterflow.io/assets/images/20250430121444122926-bf78dbe544e70f93a7407dd066ab6d49.png)

2. **Select or Create an API Call**

   Choose an existing `API Call` or click `+ Add API Call` to create a new one.

   ![](https://docs.flutterflow.io/assets/images/20250430121444364083-3d7576af0612eb40005483e67956bfe9.png)

3. **Enter the API Endpoint**

   Add the endpoint and necessary parameters, headers, or authentication.

   ![](https://docs.flutterflow.io/assets/images/20250430121444571412-40417a9e3bacd13a6bdadb8d0ec44022.png)

4. **Click the `Response & Test` Tab**

   Navigate to the `Response & Test` tab to preview the response structure.

   ![](https://docs.flutterflow.io/assets/images/20250430121444783602-6c0e9c6851a4645a4cbfc0120c06e445.png)

5. **Run the API Test**

   Click the `Test API Call` button to trigger the request. If successful, the API response displays in JSON format.

   ![](https://docs.flutterflow.io/assets/images/20250430121445020637-d8c0b6a4a88e89945efcb6487f901642.png)

   A valid API response displays a structured output like the example below::

   ![](https://docs.flutterflow.io/assets/images/20250430121445238952-ca370fce28cc37d1d114d4da9b593eb7.png)

> **Tip:** Use **[JSONPath](https://jsonpath.com/)** to validate and extract values from the returned JSON structure during testing.

---

### Fix Google Translate Errors {#fix-google-translate-errors}

*FlutterFlow integrates with Google Translate to help localize your app automatically. This guide outlines how to identify and resolve common issues with the translation integration.*

**Source:** https://docs.flutterflow.io/troubleshooting/translations/fix-google-translate-errors

FlutterFlow integrates with Google Translate to help localize your app automatically. This guide outlines how to identify and resolve common issues with the translation integration.

Prerequisites

* Google Translate integration must be enabled for the project.
* At least one supported language must be added in **App Settings > Localization**.
* Review the [Google Translate Integration](https://docs.flutterflow.io/concepts/localization#add-multi-language-support) guide for setup instructions.

#### Common Translation Issues and Fixes

* **Long Text Forms**; **Problem:** Attempting to translate long blocks of text in forms or widgets can lead to API timeouts or failures.; **Solution:** Remove long text elements and translate them outside of FlutterFlow using external tools like Google Translate. Once translated, manually paste the content back into your project. Ensure the input field is empty before retrying automatic translation.

* **Special Characters**; **Problem:** Some special characters—such as emojis, accented symbols, or non-Latin characters—may not be supported by the Google Translate API and can cause translation to fail.; **Solution:** Review the text and replace or remove any unsupported special characters. Then attempt the translation again.

* **Exceeding Language Limit**; **Problem:** Adding more than 10 language options in your project may result in translation failure.; **Solution:** Limit your project to a maximum of 10 supported languages for translation to work reliably with Google Translate.

#### Steps to Troubleshoot Translation Failures

1. **Locate the Problem Area**; Identify the specific widget, page, or field where translation fails. Focusing on the problematic component will make resolution faster.

2. **Use the Translate All Button**; In **App Settings > Localization**, click the **Translate All** button. The process will stop at the first failure, indicating the field or element causing the issue.

3. **Check Chrome Developer Console**; Open the Chrome DevTools console and monitor for any error logs related to translation requests. This can help identify issues such as invalid characters, request failures, or unsupported content.

4. **Remove and Isolate Problematic Text**; Temporarily delete the suspected text and retry the translation. If the translation proceeds successfully, that text is likely causing the failure. Manually translate and reinsert it.

   note

   Using shorter, plain-text strings without special characters improves success rates with the Google Translate API.

Additional Help

If the issue persists after troubleshooting, reach out to <support@flutterflow.io> with the following:

* Screenshot or screen recording of the failure

* Console error logs (if available)

* A description of where the failure occurs (page/widget/text field)

  This will help the support team resolve the issue faster.

---

### Custom Widget Errors {#custom-widget-errors}

*This article demonstrates common errors and issues that may occur when creating a Custom Widget in FlutterFlow, along with steps to resolve them. In this example, an Animated Text Widget is used.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/custom-widget-errors

This article demonstrates common errors and issues that may occur when creating a `Custom Widget` in FlutterFlow, along with steps to resolve them. In this example, an `Animated Text Widget` is used.

![](https://docs.flutterflow.io/assets/images/20250430121322843622-c050cb0de4edcae7c8f0b355c0d1cbc0.gif)

**Project URL:** [Animated Kit Widget Project](https://app.flutterflow.io/project/animated-kit-widget-fyqw6j)

**Run Mode URL:** [Animated Kit Widget Run Mode](https://app.flutterflow.io/run/QP62FwanUTRs7O3HJzdo)

Prerequisites

* A custom widget has been added to your project.
* Necessary packages have been added to **Custom Code > Packages**.

Best Practices Before Creating a Custom Widget

* Set a unique name for the custom widget in the left panel `Side Widget` field.
* Start with the boilerplate code template provided by FlutterFlow. Copy it and modify your code from there.

![](https://docs.flutterflow.io/assets/images/20250430121323364253-2ec75fa5a0a999b940f42df1e62600fc.gif)

**Common Errors and Solutions:**

* **Widget Name Conflicts with Package Name**

  A common issue is using a widget name that conflicts with the name of an imported package.

  Avoid generic or conflicting names like `main` or `widget`. Use unique widget names that do not overlap with package names.

  ![](https://docs.flutterflow.io/assets/images/20250430121324152439-03c0a9f6e48a39760356762c6f92d182.png)

  ![](https://docs.flutterflow.io/assets/images/20250430121324382074-cce6c4b49b75d0c7cf167c99bb384323.png)

  Avoid using generic or conflicting names like `main` or `widget`. Always use unique widget names that do not overlap with any package names.

* **Missing Package Imports in Code**

  After adding an external package as a dependency, you must import it at the top of your custom widget code. Failure to do so results in errors such as:

  ```
  The method 'AnimatedText' isn't defined...
  ```

  ![](https://docs.flutterflow.io/assets/images/20250430121324695186-b868bac41d84f6149620fb5cf28bc38c.png)

  Here is how to fix this issue:

  * Visit the package page on **[pub.dev](https://pub.dev/)** and locate the import line in the package details section.

  * Copy and paste the correct import statement into your custom widget code.

    ![](https://docs.flutterflow.io/assets/images/20250430121324981835-de0769611f3ddebf627bd5848965516b.png); ![](https://docs.flutterflow.io/assets/images/20250430121325311155-ffc69bca85d2e981b3bfe20e27edac57.png)

* **Missing Indirect Dependencies**

  Some packages may rely on additional external packages. Ensure that all required dependencies are also imported in your code.

  ![](https://docs.flutterflow.io/assets/images/20250430121325659677-fd2659d65e96a310697c8f95f506ed47.png)

  In this example, the package depends on another package named `silver_tools`, which must also be imported. Always review the dependency chain for any external packages you add.

  ![](https://docs.flutterflow.io/assets/images/20250430121325972589-5ae05af75dca1a7c9f5a46e73b724a4b.png)

* **Widget Name Mismatch Between UI and Code**

  A mismatch between the widget name in FlutterFlow and the class name in your code will cause compilation errors.

  Incorrect example:

  ![](https://docs.flutterflow.io/assets/images/20250430121326300880-a8bb8140772717c439f71c0c31bc0b9e.png)

  Corrected version with matching names:

  ![](https://docs.flutterflow.io/assets/images/20250430121326628836-42a2cc3c3d2e93715a5cbb6beabf95e5.png)

  Ensure that the widget name matches exactly in both places.

By following these best practices and carefully reviewing package imports, dependencies, and widget names, most common issues with `Custom Widgets` in FlutterFlow can be avoided.

---

### Emoji Size on iOS Devices {#emoji-size-on-ios-devices}

*On iOS devices, emojis can appear oversized when rendered inside text widgets, disrupting the intended design and layout. This guide explains how to maintain consistent emoji sizing across all devices using container constraints and auto-sizing configuration.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/emoji-size-on-ios-devices

On iOS devices, emojis can appear oversized when rendered inside text widgets, disrupting the intended design and layout. This guide explains how to maintain consistent emoji sizing across all devices using container constraints and auto-sizing configuration.

Prerequisites

* You are using a `Text` widget that includes emojis.
* You are targeting iOS devices as part of your app deployment.

#### Steps to Maintain Consistent Emoji Size

1. **Wrap the Text Widget in a Container**; Create a `Container` with fixed width and height (example `32x32 pixels`) to restrict the emoji size.

2. **Place the Emoji Inside a Text Widget**; Add a `Text` widget containing the emoji and place it inside the container.

3. **Set a Font Size**; Apply a specific font size to the `Text` widget (example, `16`, `24`, etc.).

4. **Enable Auto-Size**; Turn on **Auto-Size** in the `Text` widget to allow responsive resizing within the fixed container.

   ![](https://docs.flutterflow.io/assets/images/20250430121253238523-5b0095421ea62c6cfa11ca4b39e2eb9d.png)

   This ensures that the emoji will resize according to the container's constraints and not exceed the intended bounds.

   tip

   Auto-Size works best when combined with fixed container dimensions. This approach prevents oversized emojis and supports responsive layouts.

---

### Infinite Scroll Pagination in ListView {#infinite-scroll-pagination-in-listview}

*If a ListView with Infinite Scroll enabled loads all items at once instead of paginating, the issue is typically related to layout configuration. This guide outlines how to correctly structure the widget for proper pagination behavior.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/infinite-scroll-pagination-in-listview

If a `ListView` with **Infinite Scroll** enabled loads all items at once instead of paginating, the issue is typically related to layout configuration. This guide outlines how to correctly structure the widget for proper pagination behavior.

Prerequisites

* Infinite Scroll is enabled in the `ListView`.
* The widget is placed inside a layout that allows height constraints to be respected.

Follow the steps below to configure ListView for pagination:

1. **Ensure ListView Has a Defined Height**; A `ListView` must have a height constraint to determine the viewport size and paginate correctly. Without a defined height, it will attempt to load all items.

2. **Let ListView Handle Its Own Scrolling**

   * Disable scrolling in any parent `Column` or scrollable container.

   * Enable the **Primary** option, and wrap `ListView` in an `Expanded` widget.

   * This allows `ListView` to control scroll behavior and calculate items to load per page.

     ![](https://docs.flutterflow.io/assets/images/20250430121248035007-63bc015cf137d22fc50337da21f3a90e.png)

3. **Wrap ListView Inside a Fixed-Height Container (if nested)**; If `ListView` is inside a scrollable parent (like `Column` or `ListView`), wrap it in a `Container` with a defined height (e.g., `500px`). This ensures it doesn't expand indefinitely.

   ![](https://docs.flutterflow.io/assets/images/20250430121248379992-14e1ef9e72be0c45c03a56f55f8b68b1.png)

4. **Avoid Missing Height Constraints**; Without constraints, `ListView` will not know the visible size and will load all data at once, bypassing pagination.

   warning

   Placing `ListView` directly inside a scrollable parent without a defined height will break Infinite Scroll behavior.

5. **Use Layout Structure That Supports Scroll Isolation**; Allow `ListView` to scroll independently before the parent scroll takes over. Combine this with defined height and `Expanded` usage for best results.

   ![](https://docs.flutterflow.io/assets/images/20250430121249048672-6671c857c81494bec61769372aae4a77.gif)

> **Tip:** To optimize pagination, define consistent item heights and test using varying screen sizes.

Additional Resources

* **[ListView Scroll Example Project](https://app.flutterflow.io/project/list-view-scroll-example-wdv076)** – View a working configuration example.

---

### Rive Animation Loading Errors {#rive-animation-loading-errors}

*Rive animations may fail to render when the source file is incorrectly linked. This guide outlines how to provide a valid .riv file URL for successful animation loading.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/rive-animation-loading-errors

Rive animations may fail to render when the source file is incorrectly linked. This guide outlines how to provide a valid `.riv` file URL for successful animation loading.

Prerequisites

* A valid Rive animation is hosted online with a `.riv` extension.
* The animation is added to a FlutterFlow widget that supports Rive.

#### Steps to Fix Rive Animation Not Loading

1. **Verify the Rive File URL**; Ensure the file URL ends with `.riv` and points directly to a hosted Rive file.

   ```
   https://public.rive.app/community/runtime-files/1199-2317-jack-olantern.riv
   ```

   If the URL points to a webpage or lacks the `.riv` extension, the animation will not load in FlutterFlow.

2. **Copy the Correct Link from Rive Community:**

   * Go to the animation page on the **[Rive Community](https://rive.app/community/)**.

   * Right-click the **Download** button.

   * Select Copy Link Address.

     The copied link must end with `.riv`. Any URL that redirects to a webpage or file viewer will fail to render.

---

### Scroll To Action on Page Load {#scroll-to-action-on-page-load}

*When a Scroll To Action fails to trigger during a page load, it is often because the scrollable widget has not fully rendered at the time the action executes. This guide outlines how to ensure the scroll action works reliably during page load.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/scroll-to-action-on-page-load

When a `Scroll To Action` fails to trigger during a page load, it is often because the scrollable widget has not fully rendered at the time the action executes. This guide outlines how to ensure the scroll action works reliably during page load.

Prerequisites

* The `Scroll To Action` is configured inside an `On Page Load` action flow.
* The target widget is inside a scrollable view such as `ListView` or `Column`.

#### Steps to Ensure Reliable Scroll Behavior:

1. **Add a Delay Before the Scroll Action**; Insert a `Delay Action` before the `Scroll To Action` to allow the widget tree to complete rendering. Recommended delay duration is 500 to 700 ms.

   ![](https://docs.flutterflow.io/assets/images/20250430121250453056-db9b60be4173ea5f88d908ab4673546a.png)

2. **Use Load Animations for Scrollable Widgets**; Applying an animation ensures the widget is fully visible before scrolling.

   * Add a load animation (e.g., `Fade`) to the scrollable widget.
   * Set the animation duration to approximately `1200 ms`.
   * Add a `Delay Action` before the scroll action (e.g., `700 ms`).

   ![](https://docs.flutterflow.io/assets/images/20250430121250214649-b4e5617b809194b82b868f3a40d38d17.png)

   tip

   Combining a delay with animation prevents the scroll action from executing before the widget appears, creating a smoother transition.

---

### Store Custom Widget Output Using App State {#store-custom-widget-output-using-app-state}

*To use the output from a custom widget elsewhere in your project, you can store its value in an app state variable. FlutterFlow does not directly support retrieving data from custom widgets, so this method provides an effective workaround.*

**Source:** https://docs.flutterflow.io/troubleshooting/widget/store-custom-widget-output-using-app-state

To use the output from a custom widget elsewhere in your project, you can store its value in an app state variable. FlutterFlow does not directly support retrieving data from custom widgets, so this method provides an effective workaround.

Prerequisites

* You have created a custom widget in your project.
* You are familiar with the **[App State management](https://docs.flutterflow.io/resources/data-representation/app-state)** system in FlutterFlow.

#### Steps to Store Output from a Custom Widget

1. **Create an App State Variable**; Go to **App State**, then create a new app state variable that will hold the value returned by your custom widget.

   ![](https://docs.flutterflow.io/assets/images/20250430121220879251-67b746b90666bc17fb112c6558d78583.png)

2. **Update the App State Variable from the Custom Widget**; In your custom widget code, use `FFAppState()` to set the value of the app state variable.

   ![](https://docs.flutterflow.io/assets/images/20250430121221066642-eafa9c31015ec78d924fb47ad3774de8.png)

   ```
   FFAppState().update(() {
     FFAppState().localvalue = 'setvalue';
   });
   ```

   App state variables can be accessed anywhere in your FlutterFlow project, making them useful for sharing data between custom widgets and other parts of the app.

---

