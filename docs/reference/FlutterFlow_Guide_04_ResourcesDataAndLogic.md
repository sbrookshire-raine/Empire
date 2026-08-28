# FlutterFlow Documentation — Complete Guide (Part 4 of 7: Resources: Data, Backend Query, Forms, Functions & Projects)

> **Note for NotebookLM:** This is one part of a multi-file Markdown export of the official FlutterFlow documentation, cleaned and reorganized for use as a NotebookLM source set to build a structured FlutterFlow learning plan. Import all parts together as separate sources in the same NotebookLM notebook.

- **Source:** https://docs.flutterflow.io (crawled via https://docs.flutterflow.io/llms-full.txt)
- **This file's page count:** 52
- **Total pages across the full guide (all 7 parts):** 369
- **Date generated:** 2026-07-18
- **Part:** 4 of 7 — Resources: Data, Backend Query, Forms, Functions & Projects
- **Other parts in this guide:**
  - Part 1: Fundamentals, Account, CLI & Builder UI (`FlutterFlow_Guide_01_Fundamentals_and_Platform.md`)
  - Part 2: Core Concepts: UI Building, Actions, Animations, Navigation, Custom Code (`FlutterFlow_Guide_02_CoreConcepts.md`)
  - Part 3: Widgets Reference (`FlutterFlow_Guide_03_WidgetsReference.md`)
  - Part 5: Integrations: Auth, Firebase, Supabase, Payments, Maps, Search, Ads (`FlutterFlow_Guide_05_Integrations.md`)
  - Part 6: Deployment, Testing, Marketplace & Exporting Code (`FlutterFlow_Guide_06_DeploymentTestingMarketplace.md`)
  - Part 7: Troubleshooting Guides (`FlutterFlow_Guide_07_Troubleshooting.md`)

## Table of Contents

**Resources (Widgets, Data, Backend Query, Functions, Projects)**

- [Create & Test API Call](#create-test-api-call)
- [API Calls](#api-calls)
- [SOAP APIs](#soap-apis)
- [Streaming APIs](#streaming-apis)
- [Backend Query](#backend-query)
- [Algolia Search Query](#algolia-search-query)
- [API Call Query](#api-call-query)
- [Document from Reference](#document-from-reference)
- [Query Collection / Table](#query-collection-table)
- [SQLite Query](#sqlite-query)
- [Control Flow Concepts](#control-flow-concepts)
- [Control Flow & Logic](#control-flow-logic)
- [Overview](#overview)
- [App State](#app-state)
- [Constants](#constants)
- [Custom Data Types](#custom-data-types)
- [Data Types](#data-types)
- [Enums](#enums)
- [Global Properties](#global-properties)
- [Variable](#variable)
- [Forms Overview](#forms-overview)
- [Checkbox](#checkbox)
- [ChoiceChips](#choicechips)
- [Dropdown](#dropdown)
- [Form Triggers](#form-triggers)
- [Form Validation](#form-validation)
- [RadioButton](#radiobutton)
- [Reset Form Field [Action]](#reset-form-field-action)
- [Set Form Field [Action]](#set-form-field-action)
- [Switch Widgets](#switch-widgets)
- [TextField](#textfield)
- [Action Blocks](#action-blocks)
- [Actions](#actions)
- [Action Triggers](#action-triggers)
- [Conditional Logic](#conditional-logic)
- [Loops](#loops)
- [Utility Functions](#utility-functions)
- [Utility Actions](#utility-actions)
- [What is a Project?](#what-is-a-project)
- [Collaborate on Projects](#collaborate-on-projects)
- [Create, Find, and Organize Projects](#create-find-and-organize-projects)
- [Run and Test Projects](#run-and-test-projects)
- [Libraries](#libraries)
- [Refactor Project](#refactor-project)
- [Pinning Projects to Stable FlutterFlow Versions](#pinning-projects-to-stable-flutterflow-versions)
- [General Settings](#general-settings)
- [Project API](#project-api)
- [Project Setup](#project-setup)
- [Naming Variables & Functions](#naming-variables-functions)
- [Periodic Action](#periodic-action)
- [Timer [Widget]](#timer-widget)
- [Wait [Action]](#wait-action)

---

## Resources (Widgets, Data, Backend Query, Functions, Projects)

### Create & Test API Call {#create-test-api-call}

*In this guide, you'll learn how to create and test API calls in FlutterFlow. Integrating API calls allows your app to interact with external services, bringing in real-time data and functionality that enhances your app's capabilities.*

**Source:** https://docs.flutterflow.io/resources/backend-logic/create-test-api

In this guide, you'll learn how to create and test API calls in FlutterFlow. Integrating API calls allows your app to interact with external services, bringing in real-time data and functionality that enhances your app's capabilities.

#### Create API Call

To use an API in your app, you first need to create the API call in FlutterFlow.

Simply select API Calls from the left navigation menu, click the **+ Add** button, and choose **Create API Call**. Enter an **API Call Name**, select the **Method Type** (GET, POST, DELETE, PUT, or PATCH), and input the API URL of the service you wish to access.

Method Types

The Method Type specifies the type of operation the API call will perform. Here’s a breakdown of common method types:

* **GET:** Retrieves data from the server.
* **POST:** Sends data to create or update a resource.
* **DELETE:** Removes a resource from the server.
* **PUT:** Updates or creates a resource with full data.
* **PATCH:** Partially updates a resource.

##### Dynamic API URLs

If you want to use a dynamic URL, for example, `<https://reqres.in/api/users/2>` where 2 is dynamic and `<https://reqres.in/api/users?page=5>` where 5 is dynamic:

1. Replace the hard-coded value with a meaningful name inside the brackets (e.g., from `https://reqres.in/api/users/2`to `https://reqres.in/api/users/[user_id]`).
2. And then, [**create a new variable**](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) with the same name you provided inside the brackets.

The further instructions are based on the **Method Type** you selected.

##### For `GET` & `DELETE` call

If you selected `GET` or `DELETE` as the method type, follow the steps below:

1. Optional: If the API call requires request headers such as an authorization token, [add a header](https://docs.flutterflow.io/resources/backend-logic/rest-api#passing-request-headers).
2. Optional: If the API call requires query parameters such as page number or user id, [add query parameters](https://docs.flutterflow.io/resources/backend-logic/rest-api#passing-query-parameters).
3. Click **Add Call** to save the API Call.

> **Warning:** After making any changes, you must save the API call.

In the above demo, a `GET` API call is defined to fetch users' data from [REQ | RES](https://reqres.in/) (which provides hosted REST API to try out HTTP requests).

A demo of using a dynamic URL in a GET request is as follows:

To add such an API call:

1. Replace the hard-coded value with a meaningful name inside the brackets (e.g., from `https://reqres.in/api/users/2`to `https://reqres.in/api/users/[user_id]`).
2. And then, [create a new variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) with the same name you provided inside the brackets.

The DELETE API Call can also be defined similarly; just make sure you select the **Method Type** as ***DELETE***.

##### For `POST`, `PUT` & `PATCH` call

If you have selected **POST request**, follow the steps below:

1. Optional: If the API call requires request headers such as an authorization token, [add a header](https://docs.flutterflow.io/resources/backend-logic/rest-api#passing-request-headers).
2. [Create a request body](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-request-body) for the API call.
3. Click **Add Call** to save the API Call.

> **Warning:** After making any changes, you must save the API call.

In this demo, a POST API call is defined with two variables, `userName` and `userJob`. The variables are used inside the JSON request body.

The PUT and PATCH API calls can be defined similarly; make sure you enter a valid API URL endpoint and select the correct Method Type.

#### Grouping API calls

You can create a group of API calls that share the same base URL. Grouping the API calls helps you add all request headers (e.g., auth token) at once, and they will be automatically added for all the API calls inside the group.

> **Warning:** For [**private APIs**](https://docs.flutterflow.io/resources/backend-logic/rest-api#private-api-calls), headers defined within the group will not be automatically included. You'll need to manually add headers for APIs marked as private.

To create the API Group:

1. Click on the **+** button (top left side) and select the **Create API Group**.
2. Enter the **API Group Name**.
3. Enter the **API Base URL**. This should be the portion that is common in all the APIs. **Note**: Do not keep the '/' in the end.
4. You can add request headers by clicking on the **+ Add Header** button. See detailed instructions on how to [add headers](https://docs.flutterflow.io/resources/backend-logic/rest-api#headers).
5. Click **Add Group**. This will display the group on the left side.
6. Open the newly created API group, and click on the **+ Add API Call**.
7. Add the API call as you would normally do. **Note**: Inside the API endpoint, enter the URL portion that starts after the base URL.

#### Import API definitions

We allow you to add multiple API call definitions by importing them directly from the [Swagger/OpenAPI](https://swagger.io/) in bulk. With just a simple click, you can add a large number of APIs, significantly reducing the time and effort needed to create them manually.

Furthermore, the ability to import Swagger/OpenAPI definitions directly into FlutterFlow eliminates the risk of errors that may occur when creating API definitions manually, ensuring that applications are reliable and efficient.

> **Info:** We also add all settings that are required to run the API, such as [headers](https://docs.flutterflow.io/resources/backend-logic/rest-api#headers), [query parameters](https://docs.flutterflow.io/resources/backend-logic/rest-api#query-parameters), [variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#variables), and body as they are defined in the Swagger file. However, you might need to replace the hard-coded values in [Body](https://docs.flutterflow.io/resources/backend-logic/rest-api#body) text with the [variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#variables).

> **Warning:** Please note that while it is possible to import APIs created with OAS 2.0 in FlutterFlow, you might face some issues, such as the body request being lost during the import process. Our import functionality is built based on the OAS 3.0 standard, so for the best experience and compatibility, it is recommended to use APIs that adhere to OAS 3.0 or above.

To import API call definitions:

1. Click the **Import OpenAPI** icon. This will open a new popup.
2. Click **Upload File**. Here you can upload your swagger file available in `.yml` or `.json` file format.
3. After the import is successful, you will see the list of all APIs created and added as a [group](https://docs.flutterflow.io/resources/backend-logic/create-test-api#grouping-api-calls).

Here's an example of importing API calls in bulk, taken from [here](https://editor.swagger.io/).

#### Testing API calls

You should always test your API call before using it inside your app. We make it easy for you to try the API call inside our builder.

To test the API call along with its response, follow the steps below:

1. Select an API call you have already created or are currently defining, and go to the **Response & Test** tab.
2. On the left side, you will see the **Variables** section, where you can enter the values for the variables defined for your API call.
3. On the right, the **Preview** section lets you check the API URL, request headers, request body, and response. In the **Test Response** tab, you can view the full API response, including both the JSON format and raw body text, as well as the response header.
4. Click **Test API Call** to trigger the API call. You'll notice that the status of the GET request is displayed, and if it's successful (status code `200`), the result returned from that request will also be displayed below.
5. Any value of the JSON result can be accessed by [defining the JSON path](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-path).

The demo below shows the testing of creating a new user using a POST request. The API Call takes two variables: `userName` and `userJob`. The successful POST request returns a status code of `201`.

> **Info:** The testing of `PUT` and `PATCH` requests would also be similar to this.

#### API Call \[Action]

Once the API calls are defined in your FlutterFlow project, you can use them wherever needed.

Open the Action Flow Editor on the widget where the API call should be triggered. After selecting the desired Action Trigger, search for "API Calls" in the Actions dropdown and select the API call you want to use.

![use-api-call.png](https://docs.flutterflow.io/assets/images/use-api-call-ee46df3313018e6348554a1c7c8fdd68.png)

> **Tip:** You can also add the API Call as a [**Backend Query**](https://docs.flutterflow.io/resources/backend-query/api-call-query) that gets triggered automatically when the page or widget is loaded on the screen.

Go to your project and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on the **+ Add Action**.

4. On the right side, search and select the **API Call** (under *Backend/Database*) action. 1. Select the **Group or Call Name** from the dropdown.
   2. Optional: If your API call requires variables (e.g., auth token, query parameters, user id, etc.), pass their value by clicking on the **+ Variable** button.
   3. The **Action Output Variable Name** helps you retrieve the response of an API call. By default, we set it to any random name. However, you can change it to a meaningful name if you wish to. (e.g., loginResponse).
   4. You can add a conditional action that checks if the API call is succeeded.
   5. If the API call is succeeded, all actions under the TRUE path will be executed. For example, [navigate](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) to the home page if the login is successful.
   6. If the API call is failed, all actions under the FALSE path will be executed. For example, [showing a snackbar](https://docs.flutterflow.io/resources/ui/pages/scaffold#snackbar) if the login is unsuccessful.

---

### API Calls {#api-calls}

*Learn the basics of making API calls in your backend logic.*

**Source:** https://docs.flutterflow.io/resources/backend-logic/rest-api

On this page, you will learn the most basic knowledge on various concepts for adding an API call to your project. They are the building blocks of adding an API call. Depending on the API's definition, you may utilize some or all of these concepts to successfully implement the API call in your project.

Here are they:

* [Headers](https://docs.flutterflow.io/resources/backend-logic/rest-api#headers)
* [Query Parameters](https://docs.flutterflow.io/resources/backend-logic/rest-api#query-parameters)
* [Variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#variables)
* [Body](https://docs.flutterflow.io/resources/backend-logic/rest-api#body)
* [API response (JSON) to/from Data Type](https://docs.flutterflow.io/resources/backend-logic/rest-api#api-response-json-tofrom-data-type)
* [JSON Path](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-path)
* [Advanced Settings](https://docs.flutterflow.io/resources/backend-logic/rest-api#advanced-settings)

#### Headers

Headers typically carry the metadata associated with an HTTP request or response of an API call. HTTP headers are mainly grouped into two categories:

* **Request headers** contain more information about the resource to be fetched or the client requesting the resource.
* **Response headers** hold additional information about the response that the server returns.

##### Passing request headers

Some of the common request headers that you might need while sending a request are:

* **Authorization**: Used for authenticating the request.
* **Content-Type**: Used while sending a POST/PUT/PATCH request containing a message body.

To pass the request header:

1. Select the **Headers** tab and click on the **+ Add Header** button.
2. Inside the input box, enter the header name followed by the colon(:) and its value (e.g., **Content-Type: application/json**).

> **Info:** The default **Content-Type** for any HTTP POST request is `application/json`, so if your data body is in JSON, you can skip defining the Content-Type.

##### Passing auth token (as request header)

You might need to add an API that is secured. That means it only gives results if you pass the authorization token (aka auth token) in the header parameter. This is usually done to prevent abuse. Let's see how you can add the auth token.

###### Passing static auth token

Some services provide you with a static auth token. Such a token never changes until you manually generate the new one.

To pass the static auth token:

1. Select the **Headers** tab and click on the **+ Add Header** button.
2. Inside the input box, enter the header name as **Authorization** followed by colon (:) and its value (e.g., **Authorization: Bearer YOUR\_TOKEN**).

###### Passing dynamic auth token

You would probably want to pass the auth token returned as a response in the login API call. Such a token changes every time when you log in. Hence, you need a way to pass the dynamic token.

How to save an authentication token?

After the login call is succeeded, ensure you save the authentication token in an app state variable (with Persisted -> True). Check the visuals below:

![api-token-variable.png](https://docs.flutterflow.io/assets/images/api-token-variable-acf56056503d2c4fb2717205d8d8c7d2.png)

Now you can pass the dynamic token:

1. Select the **Headers** tab and click on the **+ Add Header** button.
2. Inside the input box, enter the header name as **Authorization** followed by a colon (:) and then enter any variable name inside the brackets (e.g., **Authorization: Bearer \[auth\_token]**).
3. Select the **Variables** tab and [create a new variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) with the same name you provided inside the brackets. This will be used to pass the token value from the app state variable to the API call.

Now from the API call (that requires an authentication token), pass the token value from the app state variable.

##### Accessing response headers

Sometimes you might want to retrieve the values of the response headers. For example, retrieving the auth token from the response headers of the Login API call.

To access the response header:

1. Ensure you have added the [API call action](https://docs.flutterflow.io/resources/backend-logic/rest-api) and provided the **Action Output Variable Name**.
2. Now, whenever/wherever the **Value Source** is set to **From Variable**, select the **Action Outputs > \[Action Output Variable Name]** (e.g., Action Outputs > loginResponse).
3. Set the **API Response Options** to **Get Response Header**.
4. Enter the **Header Name**. Note that this must match the name of the response header from your API call.
5. Click **Confirm**.

#### Query Parameters

They are optional parameters you can pass with an API call; they help format the response data returned by the server. Usually, they are concatenated at the end of the URL with a question mark (`?`) as the delimiter and are represented as key-value pairs.

An example of an URL with query parameters looks like this ([NASA Open API](https://api.nasa.gov/)):

[https://api.nasa.gov/neo/rest/v1/feed?**start\_date=2015-09-07\&end\_date=2015-09-08\&api\_key=DEMO\_KEY**](https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07\&end_date=2015-09-08\&api_key=DEMO_KEY)

Here, `start_date`, `end_date`, and `api_key` are the query parameters passed to receive the specific data.

Here's another example, this API call `<https://www.breakingbadapi.com/api/characters?limit=20&offset=0>` has two query parameters. The `limit` parameter specifies 20 items to load per page, and the `offset` specifies the number of items to skip. This is called offset-based pagination.

##### Passing query parameters

To pass the query parameters for `GET` or `DELETE` API call:

1. Select the **Query Parameters** tab and click the **+ Add Query Parameter** button.

2. Enter the **Name** of the query parameter.

3. Set the **Value Source** to **Specific Value** or **From Variable**. 1. If you want to pass this value from your page, app state variable, or any other source (i.e. , dynamic value), choose the **From Variable,** and then from the **Select Variable** dropdown, choose the already created variable (see how to [create variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables)) or click on **+ Create New Variable**. Note: This will immediately create a new variable with the same name as of query parameter. However, you still need to open the **Variables** tab and set its **Type**.
   2. If you want to pass a static/fixed value, select the **Specific Value**, set its **Type,** and enter its **Value**.

Below is the example of passing query parameter for the URL -> `https://api.instantwebtools.net/v2/passenger?page=10&size=20`

In a rare case, you might want to pass the query parameters for the other methods of API calls. Such as POST, PUT, and PATCH. To do so:

1. In your API URL, replace the hard-coded values with a meaningful name inside the brackets (e.g., from `https://api.instantwebtools.net/v2/passenger?``**page=0**` to `https://api.instantwebtools.net/v2/passenger?``**page=[page]**`).
2. Select the **Variables** tab and [create a new variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) with the same name you provided inside the brackets.

#### Variables

Variables allow you to pass the dynamic values from any part of your app to the API calls. Here's when they come in handy:

* Sending an auth token from your app's state to an API call's request header.
* Using username and password from TextField widgets in the API call's request body.
* Including selected dates as query parameters.
* Changing the base URL with a dynamic URL.

##### Creating variables

To create variables, select the **Variables** tab, enter its **Name**, select the appropriate **Type** and provide the **Default Value** if you wish to.

![variables.png](https://docs.flutterflow.io/assets/images/variables-581babfdb6cab0e35ece92e29388cba5.png)

Now you can pass values to these variables while triggering the API call from your page. You can set its value from any widget, app state variable, or any other source.

Here's how you can use a variable to create a dynamic base URL:

![dynamic-base-url.png](https://docs.flutterflow.io/assets/images/dynamic-base-url-1b204a7de91385a3f4287fcfaf1459d4.png)

#### Body

You can send data (as a request body) while calling the API of methods POST, PUT, or PATCH by defining them inside **Body**. The most common type is JSON format which is the easiest way of passing data inside the body of the reqest.

##### Creating Request Body

Here you'll see creating a request body in the following formats:

###### JSON format

To create a request body in JSON format:

1. First, If you haven't already, [create variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) (e.g., username and password variables that will be required to pass values from a login page to the login API call).
2. Select the **Body** tab and set the Body dropdown to **JSON**.
3. Copy-paste your request body and replace the values with the variables by dragging and dropping them inside your JSON body.

###### Text format

This format is used to send textual data in the request body of an API. For example, in a SOAP API, the request body is typically in text format and contains XML data.

To create a request body in text format:

1. First, If you haven't already, [create variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables).
2. Select the **Body** tab and set the Body dropdown to **Text**.
3. Copy-paste your request body and replace the values with the variables by dragging and dropping them inside the request body.

###### x-www-urlencoded format

To create a request body in x-www-form-urlencoded format:

1. First, If you haven't already, [create variables](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) (e.g., username and password variables that will be required to pass values from a login page to the login API call).

2. Select the **Body** tab and set the Body dropdown to **x-www-form-urlencoded**.

3. Click on the **+ Add Parameter** and enter the **Name** of the parameter.

4. Set the **Value Source** to **Specific Value** or **From Variable**. 1. If you want to pass this value from your page, app state variable, or from any other source (i.e., dynamic value), choose the **From Variable,** and then from the **Select Variable** dropdown, choose the already created variable (see how to [create variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables)) or click on **+ Create New Variable**. Note: This will immediately create a new variable with the same name as of parameter. However, you still need to open the **Variables** tab and set its **Type**.
   2. If you want to pass a static/fixed value, select the **Specific Value**, set its **Type,** and enter its **Value**.

###### Multipart format

A multipart request body is a data format used in HTTP requests that enable the transfer of multiple parts of data in a single request. It is commonly used in file uploads.

To create a request body in the multipart format:

1. Select the **Body** tab and set the *Body* dropdown to **Multipart**.
2. Click on the **+ Add Parameter** and enter the **Name** of the parameter.
3. Set the **Value Source** to **From Variable,** and then from the **Select Variable** dropdown, click on **+ Create New Variable**. Note: This will immediately create a new variable with the same name as of parameter.
4. Now move to the **Variables** tab and set the **Type** to **Uploaded File**. This will allow you to pass the file stored locally on the device using an action such as **Upload/Save Media**.

#### API response (JSON) to/from Data Type

Converting between API Response (JSON) and Data Types is often referred to as JSON deserialization and serialization. It allows you to convert JSON data from an API response into a [**Custom Data Type**](https://docs.flutterflow.io/resources/data-representation/custom-data-types) when you receive it. Also, it enables you to convert your Custom Data Type back into JSON when sending data in an API request.

> **Info:** This is a more robust and maintainable way to work with JSON data in your app. It reduces complexity and potential errors (e.g., typos) compared to manually navigating [JSON paths](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-path).

##### Create Custom Data Type matching to JSON structure

First, [create a Data Type](https://docs.flutterflow.io/resources/data-representation/custom-data-types#creating-custom-data-type) with the same structure as your API response. Here's what the sample JSON response looks like after mapping it into a Custom Data Type.

![custom-data-type-json-response.png](https://docs.flutterflow.io/assets/images/custom-data-type-json-response-3a0d799722f6aaa023aa47d0142fd9a6.png)

Creating custom data type as per the JSON response

After this, you can choose to [convert to](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-to-data-type) or [from](https://docs.flutterflow.io/resources/backend-logic/rest-api#json-from-data-type) the Data Type based on your requirements.

##### JSON to Data Type

Let's see how to get the JSON into the Custom Data Type using an example that fetches the list of products from [this API](https://dummyjson.com/docs/products). Here's how it looks:

![img.png](https://docs.flutterflow.io/assets/images/img-c6ed86116aa90ef908ab4f79a0262ceb.png)

Here's how you do it:

1. First, ensure that you [create a custom data type](https://docs.flutterflow.io/resources/backend-logic/rest-api#create-custom-data-type-matching-to-json-structure) that matches your JSON structure.
2. Open your API call definition > **Response & Test tab > Response Type >** enable the **Parse as Data Type**. Select the **Data Type** that you want to convert into. For this example, it's 'AllProducts'.

![img\_1.png](https://docs.flutterflow.io/assets/images/img_1-05b380df971294e998ed9a503d802323.png)

3. On ListView, after adding the [API call backend query](https://docs.flutterflow.io/resources/backend-query/api-call-query), access the values by setting the following options.

   1. **Generate Children from Variable** by setting **API Response Options** to **As Data Type**.
   2. Set **Available Options** to **Data Structure Field** because we want to grab only a specific field, which has a list of products and not other items such as 'total' and 'skip'.
   3. **Select Field** to the field that holds the list of products, i.e., 'products' for this example.
   4. Click **Confirm** twice.

4) Now, you can bind data in UI elements as you would normally do by setting the **Available Options** to **Data Structure Field** and **Select Field** that you want to display.

##### JSON from Data Type

Sometimes you might want to dynamically create a JSON body and pass it along the API request instead of manually configuring each field in the API call editor. You can do so by adding data into a Custom Data Type and then converting it into JSON while making an API call.

Let's see an example of adding a product by sending its data in JSON format in the API request.

![add-product.png](https://docs.flutterflow.io/assets/images/add-product-ef370dfe0ed90a1a547b26a09fb59236.png)

Here's how you do it:

1. First, [create a custom data](https://docs.flutterflow.io/resources/backend-logic/rest-api#create-custom-data-type-matching-to-json-structure) type that matches the JSON format of the API request body. Here's how it looks for this example.

![img\_2.png](https://docs.flutterflow.io/assets/images/img_2-793efe2c929d07234b9fb57e4cac6d5b.png)

2. In your API call, [create a variable](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables) with type **JSON** and put it inside the **Body** section.

3) On click of **Add** button, we'll store values from UI into the page state variable of custom data type. Then, while making an API call, pass that page state variable and set the **Available Options** to **To JSON**.

#### JSON Path

**JSONPath** is a query language for JSON. Using the JSON path, you can retrieve specific data out of the whole JSON response.

> **Note:** You'll usually get a response in JSON format from an API request.

Learning a few JSON paths (or *JSONPath expressions*) will help you retrieve most of the data you need. Inside our builder, we allow you to try and add different JSON paths in real-time and suggest various options to get exactly what you are looking for.

Some examples of JSONPath expressions are as follows:

* `$.data.name`
* `$.users[0].name`
* `$.users[:].name`

The leading `$` represents the root object, dot (`.`) is used for accessing keys present inside the JSON, the value inside brackets (`[0]`) represents the array index if the key contains an array, and the (`[:]`) will select all the objects inside the list.

Let's see some real-world examples of the JSON path for the following API response:

```
{
  "page": 1,
  "per_page": 6,
  "total": 3,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    {
      "id": 2,
      "email": "janet.weaver@reqres.in",
      "first_name": "Janet",
      "last_name": "Weaver",
      "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
      "id": 3,
      "email": "emma.wong@reqres.in",
      "first_name": "Emma",
      "last_name": "Wong",
      "avatar": "https://reqres.in/img/faces/3-image.jpg"
    }
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

$.total

This will return the following data:

```
3
```

$.data

This will return the following data:

```
[
   {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
   },
   {
      "id": 2,
      "email": "janet.weaver@reqres.in",
      "first_name": "Janet",
      "last_name": "Weaver",
      "avatar": "https://reqres.in/img/faces/2-image.jpg"
   },
   {
      "id": 3,
      "email": "emma.wong@reqres.in",
      "first_name": "Emma",
      "last_name": "Wong",
      "avatar": "https://reqres.in/img/faces/3-image.jpg"
   }
]
```

$.data\[0]

This will return the object at the 0th index (i.e., the first object).

```
{
   "id": 1,
   "email": "george.bluth@reqres.in",
   "first_name": "George",
   "last_name": "Bluth",
   "avatar": "https://reqres.in/img/faces/1-image.jpg"
}
```

$.data\[0].email

This will return the email value of the object at the 0th index.

```
"george.bluth@reqres.in"
```

$.data\[:].email

This will return the email of all the objects inside the data.

```
[
  "george.bluth@reqres.in",
  "janet.weaver@reqres.in",
  "emma.wong@reqres.in"
]
```

Important

JSON keys must start with a letter, an underscore, or a dollar sign. They cannot begin with a numeric character. However, in cases where you have keys with numeric prefixes, such as `$.0_image`, you can access them using bracket notation, like this: `$.["0_image"]`.

> **Info:** Learn more about **[JSONPath](https://www.rfc-editor.org/rfc/rfc9535.html)** and how to define a proper expression.

##### Add JSON Predefined Path

You can effortlessly define and manage **JSON Paths** for your API calls in FlutterFlow to parse and extract the data you need. Once added you can [use](https://docs.flutterflow.io/resources/backend-logic/rest-api#using-json-path) them as **Predefined Path** while accessing the **JSON Body**.

First, [create and test](https://docs.flutterflow.io/resources/backend-logic/create-test-api) your API call. Inside the **JSON Paths** section, click **+ Add JSON Path**, enter your **JSON Path**, and assign it a name. If the expression is valid, a preview of the response appears under **Response Preview**. Click the **Preview** icon to see the full response. If the response contains a list of items, the **Is List** option will be enabled automatically.

Under the **Recommended** section, you'll find suggested JSON paths that might contain the data you need.

##### Using JSON Path

While accessing values from an API Call, you can either enter the custom JSON path or use the [predefined JSON path](https://docs.flutterflow.io/resources/backend-logic/rest-api#add-json-predefined-path).

To use a predefined JSON Path, first, select your API response. Then, set the **API Response Options** to **JSON Body** and the **Available Options** to **JSON Path** or **Predefined Path**. Finally, specify the JSON Path Name or select from the predefined JSON Path to map the extracted data for use in your app.

#### Advanced Settings

You can make the API call private and change the proxy settings using advanced settings.

##### Private API Calls

Making an API call private is helpful if it uses tokens or secrets you don't want to expose in your app. Enabling this setting will route this API call securely via the Firebase Cloud Functions.

![private-cloud-func.png](https://docs.flutterflow.io/assets/images/private-cloud-func-5752d692200c53e625e1907c0d726101.png)

To make an API Call Private, open the **Advanced Settings** tab, turn on the **Make Private** toggle, Click **Save,** and then **Deploy APIs**.

Optionally, you can force a user to be authenticated via the Firebase authentication to make this API call. To do so, turn on the **Require Authentication** toggle.

Private APIs are deployed as [**Cloud Functions**](https://firebase.google.com/docs/functions) within your Firebase project. While deploying, you can configure the following options:

* **Use Custom Name for Cloud Function**: When enabled, allows you to specify a custom name for the deployed Cloud Function. By default, this option is disabled and Cloud Function is named as `ffPrivateApiCall`.

* **Private API Cloud Function Instances**: You can configure the number of Cloud Function instances to optimize performance and manage costs. * **Min Instances**: Set the minimum number of active instances to reduce latency and avoid cold starts. Setting this value greater than 0 will keep instances warm but may incur additional costs.
  * **Max Instances**: Define the maximum number of instances that can be scaled up based on demand.

  **Note**: To minimize costs, you can set the **Min Instances** value to 0. For detailed pricing information, refer to the [**Cloud Functions Pricing page**](https://cloud.google.com/functions/pricing-overview).

> **Note:** * If you make the API call private, **Firebase** should be connected to your project. Follow the instructions on [**this page**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for integrating Firebase with FlutterFlow.
* If you enable the **Require Authentication** toggle, **Firebase Authentication** must be configured appropriately. Check out [**this page**](https://docs.flutterflow.io/integrations/authentication/firebase/initial-setup) for setting up authentication.

##### Process Streaming Response

When working with APIs that send data continuously, like Server Sent Events (SSE), you can enable this option. This ensures your app can handle the ongoing flow of data over a long-lasting HTTP connection to display real-time updates.

Imagine you're building a live sports score application. The API provides real-time updates on match scores. To handle this continuous stream of data, you need to enable this option.

> **Info:** You can usually determine if an API supports streaming by checking its documentation. Look for keywords like "event stream" or "processing chunks.

Learn More

Learn more about adding and using [**Streaming APIs**](https://docs.flutterflow.io/resources/backend-logic/streaming-api).

##### Change proxy settings

By default, when you test your API calls inside our builder, Run mode, and Test mode, we use a proxy to route your calls to avoid the CORS issue. However, if you want to use your proxy, you can disable these settings and provide your proxy URL.

To disable current proxy settings and provide your proxy URL:

1. Open the **Advanced Settings** tab.
2. Disable the **Use Proxy for Test** and/or **Use Proxy for Run/Test Mode**.
3. Enable the **Use** **Custom Proxy URL**.
4. Enter the **Proxy Prefix URL** (e.g., **<https://your-proxy-server.com>**).

![proxy-settings.png](https://docs.flutterflow.io/assets/images/proxy-settings-9aa01af579d7fda154ac7ff56df5de6f.png)

##### Cache API Results

You can enable this option for a specific API call. So when your app runs, multiple calls to this endpoint with the same arguments will be cached. Learn more about caching [here](https://docs.flutterflow.io/resources/backend-query#backend-query-caching).

##### Decode Responses as UTF-8

Enabling this option ensures that the data you get from a server or website is read as UTF-8, a common way of storing text. Usually, a server or website tells you how to read its data, but sometimes it doesn't. This option makes sure you read the data in UTF-8 way even if the website doesn't tell you to do so.

##### API Interceptors

An interceptor allows you to capture and modify API requests and responses before they are sent or received by your app. For example, it can be used for tasks such as adding authentication tokens, logging, and error handling.

It acts as a middleman between your app and the API server. So, when you make an API call from your app, the request goes through the interceptor first. The interceptor can then inspect the request, make changes to it (like adding headers or modifying the URL), and even cancel the request if needed. Similarly, when the server responds to your request, the response passes through the interceptor before reaching your app.

Let's see how to add an interceptor:

1. Navigate to the **Advanced Settings** tab.
2. Click on **+ Add Interceptors** and select **+ Create New Interceptor** to open the [Custom Action](https://docs.flutterflow.io/concepts/custom-code/custom-actions) editor.
3. Enter the **Action Name**.
4. In the boilerplate code, add your custom code within the `onRequest` function for request interception and modification and within the `onResponse` function for response interception and modification.

> **Tip:** You can copy the boilerplate code into ChatGPT and request the completion for the specific interceptor code. Here is an [example](https://chat.openai.com/share/9fec2562-4a17-4b4c-8bf2-88043c9dae57). However, final adjustments may be needed.

1. **Save Action** and check for any errors.
2. The newly created interceptor will be added to the **API interceptors** list.

Additonally

* You can add multiple interceptors to any API call.
* When the same interceptor is used by multiple APIs, you can create an [**API group**](https://docs.flutterflow.io/resources/backend-logic/create-test-api#grouping-api-calls) and add the interceptor under the **Advanced Group Settings**. However, you can override the interceptor for any API within the group if you wish to.

Watch a video

If you prefer watching a video tutorial, here's the one for you:

#### FAQs

Why is my Predefined Path not showing any options?

This often happens if you added the Predefined Path but forgot to save the API call in FlutterFlow. Ensure you click Save after making any changes to your API call so FlutterFlow can properly recognize and display your predefined paths.

Why am I getting a “Current variable is not valid” error?

This error typically indicates that the widget isn’t receiving the data type it expects. For example, passing a list of colors directly to a text widget will trigger the error. In such cases, convert or supply the data as a string (or another compatible type) so the widget can properly display it.

---

### SOAP APIs {#soap-apis}

*Learn how to use SOAP APIs in your backend logic with FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/backend-logic/soap-api

SOAP APIs (Simple Object Access Protocol) provide a standardized way to communicate between systems, typically using XML as the message format and operating over protocols such as HTTP, SMTP, and more.

Unlike REST APIs, which use a flexible request/response model and typically exchange data in JSON, SOAP APIs are built around a formal contract defined by WSDL. This contract ensures strict adherence to communication standards, making SOAP APIs more rigid but also more reliable and secure—ideal for enterprise applications requiring transactional integrity and guaranteed message delivery.

SOAP APIs are particularly well-suited for scenarios where robust security and detailed error handling are required, such as in financial services or telecommunications.

##### Difference between SOAP APIs and REST APIs:

**Protocol and Message Format**: SOAP is protocol-based with XML messaging, while REST is more flexible, using HTTP methods and supporting multiple data formats like JSON and XML.

**Connection Lifecycle**: SOAP operates with independent requests and responses, while REST is stateless, where each request is independent, making REST more scalable and easier to manage.

**Use Case**: SOAP is preferred in scenarios where formal contracts and high security are required, while REST is more suitable for lightweight, scalable web services.

* SOAP Example response
* REST Example response

```
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Body>
    <GetMatchScoreResponse xmlns="http://example.com/scores">
      <MatchScore>
        <Team1>Red Dragons</Team1>
        <Team2>Silver Sharks</Team2>
        <Score>2-1</Score>
      </MatchScore>
    </GetMatchScoreResponse>
  </soap:Body>
</soap:Envelope>
```

```
{
  "event": "match_score",
  "data": {
    "team1": "Red Dragons",
    "team2": "Silver Sharks",
    "score": "2-1"
  }
}
```

#### Building an App

This guide provides a step-by-step instructions on how to add and use SOAP APIs to build an example app that displays a list of countries. Upon tapping on a country name, the user is taken to a details page where the country flag is displayed. By following these instructions, you can learn how to add SOAP APIs into your app and create a basic navigation flow.

The final app looks like this:

What you'll learn

* How to create SOAP APIs.
* Creating API with dynamic data in the request body.
* Parsing XML response.
* How to navigate and pass data to a new page.

To build such an app, you will need the following pages.

1. **HomePage**: It shows a list of all countries.
2. **CountryDetails**: Shows the country flag.

Here's how you'll navigate between these pages:

![Navigation flow](https://docs.flutterflow.io/assets/images/navigation-flow-6713872bd4dceb0837937cdb61fffb33.avif)

The steps to build the app are as follows:

##### 1. Build UI

Let's start with building the UI for both pages.

###### 1.1 Home page

On this page you display the list of all countries using [**ListView**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listview-widget) and [**ListTile**](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listview-widget) widgets.

![HomePage](https://docs.flutterflow.io/assets/images/home-page-134fb34f64d264818ddd7863eef4c18a.avif)

###### 1.2 Country details page

This page shows the country flag using the [**Image**](https://docs.flutterflow.io/resources/ui/widgets/image) widget.

![CountryDetails Page](https://docs.flutterflow.io/assets/images/details-page-8c62cc0c8054409306e24291f135b027.avif)

##### 2. Create APIs

For building this example, we will use two APIs from Postman's [**Public SOAP APIs**](https://www.postman.com/cs-demo/workspace/public-soap-apis). Here are they:

1. [**getCountries**](https://www.postman.com/cs-demo/workspace/public-soap-apis/request/8854915-96a53688-6305-45be-ab8b-ca1d1c88f830)
2. [**getCountryFlag**](https://www.postman.com/cs-demo/workspace/public-soap-apis/request/8854915-4f5fae60-9ae1-4b77-8518-59e9143b8fb4)

Before you build anything related to APIs in your app, you must create and test the APIs to make sure all the APIs are working correctly. So let's [create and test](https://docs.flutterflow.io/resources/backend-logic/create-test-api) these APIs in our project.

###### 2.1 getCountries

This API retrieves a list of all countries' names and codes. You can add this API by following the instructions [here](https://docs.flutterflow.io/resources/backend-logic/create-test-api).

> **Info:** It's **important** to note that you need to include the proper *Header* in your requests, such as "**Content-Type: text/xml; charset=utf-8**", and set the request *Body* type to "**Text**".

Here's how you do it:

###### 2.2 getCountryFlag

This API gets you the country's flag based on its code. You can pass the country code dynamically into the request body by creating a variable. See how to do it [here](https://docs.flutterflow.io/resources/backend-logic/rest-api#creating-variables).

* Request body
* Header

![request-body](https://docs.flutterflow.io/assets/images/request-body-a74543aa5908052ab57a91ead422d9f9.avif)

![header](https://docs.flutterflow.io/assets/images/header-5bfd5e07131507fcd5758e077529bb49.avif)

##### 3. Create custom actions

The APIs you added in the previous step return the result in [XML](https://www.w3schools.com/xml/xml_whatis.asp) format, which needs to be parsed to extract relevant data or information. This can be accomplished using a [custom action](https://docs.flutterflow.io/concepts/custom-code/custom-actions). The custom action can utilize the '[xml](https://pub.dev/packages/xml)' package to parse the XML response and retrieve data in a format that can be easily displayed on UI widgets.

For this example, you need to create two custom actions that parse the result for two APIs. Here are they:

###### 3.1 parseListofCountries

This custom action parses the result of [getCountries](https://docs.flutterflow.io/resources/backend-logic/soap-api#21-getcountries) API and gives the list of countries in a *List* variable with a *Type* *String*.

Here's the code with an explanation in the comments:

```
// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/custom_code/actions/index.dart'; // Imports other custom actions
import '/flutter_flow/custom_functions.dart'; // Imports custom functions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'package:xml/xml.dart';

Future<List<String>> parseListofCountries(String xmlResponse) async {
  final document = XmlDocument.parse(xmlResponse);
  final countryList = <String>[]; // Create an empty list to hold the countries

  // Find all elements with tag 'm:tCountryCodeAndName'
  final countryElements = document.findAllElements('m:tCountryCodeAndName');
  // Loop through all the 'm:tCountryCodeAndName' elements found above
  for (final countryElement in countryElements) {
    // Extract the country code from the element
    final countryCode = countryElement.findElements('m:sISOCode').single.text;
    // Extract the country name from the element
    final countryName = countryElement.findElements('m:sName').single.text;
    // Add the country code and name to the country list as a single string
    countryList.add('$countryCode - $countryName');
  }

  print(countryList);
  return countryList;
}
```

Here's how it looks after adding:

![Custom action to parse list of countries](https://docs.flutterflow.io/assets/images/custom-action-af569d65f98ed6e56c1d1f4e08195a66.png)

###### 3.2 parseCountryDetails

This custom action parses the result of [**getCountryFlag**](https://docs.flutterflow.io/resources/backend-logic/soap-api#22-getcountryflag) API. It uses method chaining to navigate to the desired element and retrieve the flag URL.

Here's the code with an explanation in the comments:

```
// Automatic FlutterFlow imports
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/custom_code/actions/index.dart'; // Imports other custom actions
import '/flutter_flow/custom_functions.dart'; // Imports custom functions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'package:xml/xml.dart';

Future<String> parseCountryDetails(String xmlResponse) async {
  final document = XmlDocument.parse(xmlResponse);

  return document
      .getElement('soap:Envelope')! // Access the soap:Envelope element
      .getElement('soap:Body')! // Access the soap:Body element
      .getElement('m:CountryFlagResponse')! // Access the m:CountryFlagResponse element
      .getElement('m:CountryFlagResult')! // Access the m:CountryFlagResult element
      .text // Retrieve the text value of the element
      .trim(); // Trim any leading or trailing whitespaces
}
```

Here's how it looks after adding:

![Custom action to parse country flag response](https://docs.flutterflow.io/assets/images/parse-country-flag-response-377ed062b1c56d4a256ff0c799e20325.png)

##### 4. Showing a list of countries

You can now proceed to display the country list in *HomePage*. Here are the steps you should follow:

1. Open the HomePage.

2. Create a [page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state) variable (i.e., *countries*) to hold the list of countries. This will be used to bind data in a ListView.

   ![Page state variable](https://docs.flutterflow.io/assets/images/page-state-variable-38a6dd1d354b5ee0a2b784545b4d1481.png)

3. Select the page and add the following action chain.

   1. The API call to [getCountries](https://docs.flutterflow.io/resources/backend-logic/soap-api#21-getcountries).
   2. On success, [add a custom action](https://docs.flutterflow.io/concepts/custom-code/custom-actions) to [parseListOfCountries](https://docs.flutterflow.io/resources/backend-logic/soap-api#31-parselistofcountries). It's **important** to note that you must pass the result of a previous API call as a function argument and set the **API Response Options** to **Raw Body Text**. Also, add the *Action Output Variable Name*.
   3. Add the [update page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action) action and set the variable (i.e., *countries*) value with the output of the custom action (previously added). Ensure you keep the **Update Type** to **Rebuild Current Page**.

4. On ListView, [generate dynamic children](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/generate-dynamic-children) using the page state variable.

5. The page state variable stores the country name and code as a single string (e.g., Australia - AT). To display the name and code separately in a *ListTile*, we can use a [inline function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions). To display the country name, we can use `var1.split("-")[1].trim()`, where `var1` is the current item in the list. To display the country code, we can use the same expression and replace `[1]` with `[0]`.

##### 5. Navigate to the country details page

On tapping the country name (ListView > ListTile widget), you will navigate to the *CountryDetails* page and pass the country code. This will be used to retrieve the flag of the country in the next step.

To do so:

1. Select the **ListTile** widget and add an [action to navigate](https://docs.flutterflow.io/concepts/navigation/page-navigation#navigate-to-action) to the *CountryDetails* page.
2. Inside this action, click on the **Define** button. This will open the *CountryDetails* page, where you can define a parameter that will accept the country code.
3. After defining the parameter, open this action again and pass the country code using the code expression we used in the previous step (e.g., `var1.split("-")[0].trim()`).

* Parameter on CountryDetails page
* Passing country code while navigating to CountryDetails page

![Parameter on CountryDetails page](https://docs.flutterflow.io/assets/images/parameter-on-country-details-page-dd9b6607c8abbdae411027f142c886f0.png)

![Passing country code while navigating to CountryDetails page](https://docs.flutterflow.io/assets/images/passing-country-code-0108630a062cae5785f4316069325fed.png)

##### 6. Show country flag

Whenever this page opens, it will have the country code (as a page parameter). You can use it to make an API call and get the respective country flag.

Here are the step-by-step instructions:

1. Open the *CountryPage*.

2. Create a [page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#creating-a-page-state) variable with **Type** as **ImagePath** (i.e., *flagURL*) to hold the URL of the flag image. This will be used to display in the *Image* widget.

   ![PageState variable to hold flag URL](https://docs.flutterflow.io/assets/images/hold-flag-url-7e35a2108913fb7d71827ad82c21dfe0.png)

3. Select the page and add the following action chain.

   1. The API call to [getCountryFlag](https://docs.flutterflow.io/resources/backend-logic/soap-api#22-getcountryflag).
   2. On success, [add a custom action](https://docs.flutterflow.io/concepts/custom-code/custom-actions) to [parseCountryDetails](https://docs.flutterflow.io/resources/backend-logic/soap-api#32-parsecountrydetails). It's **important** to note that you must pass the result of a previous API call as a function argument and set the **API Response Options** to **Raw Body Text**. Also, add the *Action Output Variable Name*.
   3. Add the [update page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action) action and set the variable (i.e., *flagURL*) value with the output previously added custom action. Ensure you keep the **Update Type** to **Rebuild Current Page**.

4. Now simply use the page state variable to display the flag URL in the *Image* widget.

   ![Using page state variable to display image](https://docs.flutterflow.io/assets/images/use-page-state-to-display-04bdc5cd88b92b9be1ff101f9507e8e4.png)

#### Get the example app

Get the clonable version of this app [here](https://app.flutterflow.io/project/soap-countries-4tbmom).

---

### Streaming APIs {#streaming-apis}

*Learn how to use streaming APIs in your backend logic with FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/backend-logic/streaming-api

Streaming APIs provide a continuous flow of data over a long-lived HTTP connection, enabling real-time updates for your application.

Unlike REST APIs, which deliver data in response to specific requests, streaming APIs are designed to maintain an open connection between the client and the server, continuously sending data as it becomes available. This is particularly useful for applications that require live updates, such as live sports scores, stock market tickers, chat applications, and real-time notifications.

This reduces latency and improves the user experience by providing immediate feedback. The most common protocol used for streaming APIs is Server Sent Events (SSE), but others like WebSockets can also be used depending on the application's requirements.

##### Difference between REST APIs and Streaming APIs

The primary difference between REST APIs and Streaming APIs lies in their data delivery methods:

* **REST APIs**:

  * **Request/Response Model**: The client sends a request, and the server responds with the data.
  * **Connection Lifecycle**: Each request/response pair is independent, and the server closes the connection after sending the response.
  * **Use Case**: Suitable for applications where data doesn't change frequently and real-time updates aren't critical.
  * **Example response**:

  ```
  {  
    "event": "match_score",
    "data": {
      "team1": "Red Dragons",
      "team2": "Silver Sharks",
      "score": "2-1"
    }
  }
  ```

* **Streaming APIs (Server Sent Events)**:

  * **Continuous Data Stream**: The server maintains an open connection and continuously sends data to the client as it becomes available.
  * **Connection Lifecycle**: The connection remains open, allowing the server to push new data to the client without the client having to request it.
  * **Use Case**: Ideal for applications requiring real-time updates, such as live sports scores, real-time notifications, and live chat applications.
  * **Example response**:

  ```
  event: match_score
  data: {"team1": "Red Dragons", "team2": "Silver Sharks", "score": "2-1"}

  event: match_score
  data: {"team1": "Red Dragons", "team2": "Silver Sharks", "score": "3-1"}

  event: match_score
  data: {"team1": "Red Dragons", "team2": "Silver Sharks", "score": "3-2"}
  ```

#### Example: AI Review Summary

Let's see how you can use streaming APIs in FlutterFlow by building an example that allows users to see an AI summary of product reviews. On page load, the app displays the AI summary in real-time, letting users watch the analysis unfold as it's being generated.

The final app looks like this:

The steps to build the app are as follows:

1. [Build UI](https://docs.flutterflow.io/resources/backend-logic/streaming-api#1-build-ui)
2. [Create API](https://docs.flutterflow.io/resources/backend-logic/streaming-api#2-create-api)
3. [Create page state variable](https://docs.flutterflow.io/resources/backend-logic/streaming-api#3-create-page-state-variables)
4. [Trigger and Parse API response](https://docs.flutterflow.io/resources/backend-logic/streaming-api#4-trigger-and-extract-data-from-api-response)
5. [Extract chart data](https://docs.flutterflow.io/resources/backend-logic/streaming-api#5-extract-chart-data)

##### 1. Build UI

The user interface includes a section for the average rating, and number of reviews, followed by a detailed summary of the reviews including pros, cons, and sentiment distribution visualization. Here are key widgets to build the page:

* [**Text Widget**](https://docs.flutterflow.io/resources/ui/widgets/text): Displays the AI-generated summary of the reviews and a list of the positive and negative points mentioned in the reviews.
* [**Chart (Bar chart) Widget**](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/chart/bar-chart): Visual representation of the sentiment distribution (positive, neutral, negative) in a bar chart.

![streaming-api-example-demo.png](https://docs.flutterflow.io/assets/images/streaming-api-example-demo-76340fcccad2d986236d0ff057a0e2eb.png)

##### 2. Create API

For building this app, we will use [OpenAI's Chat Completion API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) to generate a summary based on given reviews. Before you build anything related to APIs in your app, it's essential to create and test the APIs to ensure they work correctly. So let's [create and test](https://docs.flutterflow.io/resources/backend-logic/create-test-api) the Chat Completion API in our project.

Once created, open the **Advanced Settings** and **enable** the **Process Streaming Response** toggle.

Here's how you do it:

##### 3. Create page state variables

In this example, to hold and display the result of the generated AI summary, you'll need two variables.

1. `summary`: This variable will hold the full text of the summary that includes the overall sentiment of the reviews, key points mentioned by customers, and lists of pros and cons. It is initialized as an empty string and will later be updated with the AI-generated text.
2. `sentimentValues`: This variable will store the sentiment distribution values. It is a list of *double* representing the number of positive, neutral, and negative reviews. **Note that**, these values will be used to provide the *Bar Values* in a bar chart. It is initialized with three zeros and will later be updated with the actual counts of positive, neutral, and negative reviews. ![streaming-page-state.png](https://docs.flutterflow.io/assets/images/streaming-page-state-dd31cbe47a26370ec079b4434bee871c.png)

##### 4. Trigger and extract data from API response

You can trigger the streaming API just like any other regular API. However, the method of extracting and parsing data differs from that of a standard API. Unlike non-streaming APIs, where you receive a response in an action output variable, the streaming API provides data through the following response actions:

* **onMessage:** This action is triggered every time a new piece of data is received from the streaming API. You can use this action to update your UI or perform any logic with the incoming data in real-time.
* **onError:** This action is triggered when there is an error in the streaming connection. You can use this action to handle errors gracefully, such as displaying an error message to the user or attempting to reconnect.
* **onClose:** This action is triggered when the streaming connection is closed. You can use this action to perform cleanup tasks or to notify the user that the stream has ended.

Whenever the data is received, you can access the response body via the **OnMessage > Set Variable menu > Action Parameters > OnMessageInput**. and then use the [**Response Stream Message Options**](https://docs.flutterflow.io/resources/backend-logic/streaming-api#response-stream-message-options) to extract the data.

For this specific example, we use the *Server Sent Event Stream Data JSON* option and then use this JSON path `$['choices'][0]['delta']['content']` to retrieve the story data.

Here's how exactly you do it:

##### 5. Extract chart data

The API returns a detailed summary as text, but to display counts of positive, neutral, and negative reviews on chart, you need to extract these data from the text. To achieve this, you can write a simple [custom function](https://docs.flutterflow.io/concepts/custom-code/custom-functions). Once the stream ends, pass the full text to the custom function to extract the relevant data and save the output in the `sentimentValues` page state variable we created earlier.

Here's how you do it:

> **Tip:** * After saving the`sentimentValues`, it’s a good idea to remove the same data points from the generated review text to avoid redundancy.
* Similarly, you can extract other data like 'pros' and 'cons' and display them the way you like.

#### Response Stream Message Options

When working with Server Sent Events (SSE) in FlutterFlow, it's essential to understand how to process and handle the various components of the event messages. FlutterFlow provides several options that capture different parts of the SSE. Here are they:

##### Server Sent Event Data JSON (Type: JSON)

This field captures the result of JSON parsing. For example:

```
event: chat

data: {"response": "hello", "version": 7}

id: 2
```

The Server Sent Event Data JSON would be:

```
{
  "response": "hello",
  "version": 7
}
```

**Note that** If the data is not in JSON format, it will be null:

```
event: ping

data: Server time is 2024-06-28T11:52:56+00:00

id: 2
```

The Server Sent Event Data JSON would be `null`.

##### Server Sent Event Data Text (Type: String)

This field contains just the text of the "data" field from the SSE. If there are multiple "data" entries, they are concatenated with a new line. For example, from the event:

```
event: ping

data: Server time is 2024-06-28T11:52:56+00:00

id: 2
```

The Server Sent Event Data Text would be: `Server time is 2024-06-28T11:52:56+00:00`

And from the event:

```
event: journalEntry

data: Today I went to the park.

data: For Lunch I had a sandwich.

id: 3
```

The Server Sent Event Data Text would be:

```
Today I went to the park.

For Lunch I had a sandwich.
```

##### Server Sent Event Name (Type: String)

This field contains the text of the "event" field from the SSE. For example:

```
event: ping

data: Server time is 2024-06-28T11:52:56+00:00

id: 2
```

The Server Sent Event Name would be `ping`.

##### Server Sent Event ID (Type: Integer)

This field contains the text of the "id" field from the SSE, typically used to keep track of the last sent item from the server. For example:

```
event: ping

data: Server time is 2024-06-28T11:52:56+00:00

id: 2
```

The Server Sent Event ID would be `2`.

##### Server Sent Event Retry (Type: String?)

This field contains the "retry" field from the SSE, typically used to communicate to the client when to try reconnecting to the server.

##### Message Text (Type: String)

This includes the entire Server Sent Event (SSE) message, including new lines and fields ('data', 'event', 'id', 'retry'). For example:

```
event: ping

data: Server time is 2024-06-28T11:52:56+00:00

id: 2
```

#### FAQs

Why does it show 'null'?

The "null" value appears in the Server Sent Event Data JSON field when the data is not in JSON format.

For instance, the following event data is not in JSON format:

```
event: ping
data: Server time is 2024-06-28T11:52:56+00:00
id: 2
```

The Server Sent Event Data JSON will be `null` because the data cannot be parsed as JSON.

You can fix this by using the following expression inside the [Inline Function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions) to handle the `null` case:

```
responseData ?? ''
```

This expression ensures that if `responseData` is `null`, it will return an empty string instead.

---

### Backend Query {#backend-query}

*Learn about backend queries in your FlutterFlow app, including how to set up and manage queries.*

**Source:** https://docs.flutterflow.io/resources/backend-query

**Backend Query** helps you to trigger a query automatically whenever a user navigates to the page containing the query. You can set a Backend Query on a particular widget or an entire page. The information retrieved using the Backend Query can be used in any widget present inside.

#### Types of Query

We offer you the following types of Backend Queries that you can specify on any widget or page.

* [**Query Collection or Table**](https://docs.flutterflow.io/resources/backend-query/query-collection)**:** This query type is used to fetch a single record or a list of records from a Firestore Collection or Supabase Table.
* [**Document from Reference**](https://docs.flutterflow.io/resources/backend-query/document-from-reference)**:** Used to retrieve the details from a document reference.
* [**API Call Query**](https://docs.flutterflow.io/resources/backend-query/api-call-query)**:** Used to initiate an API call.
* [**SQLite Query**](https://docs.flutterflow.io/resources/backend-query/sqlite-query): Used to execute the SQL statements.
* [**Algolia Search**](https://docs.flutterflow.io/resources/backend-query/algolia-search-query)**:** Used to trigger an Algolia search on a Firestore Collection.

#### Difference between Actions & Backend Query

| **Aspect**                | **Actions**                                                                                                                               | **Backend Queries**                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Trigger**               | Triggered by user interactions such as taps, double taps, or long presses on widgets, or they can be executed automatically on page load. | Automatically triggered when the user navigates to a page or widget containing the query.                                               |
| **Usage**                 | Can be used to navigate between pages, show messages, update variables, make API calls, and more.                                         | For apps needing instant updates like chat or live scores, Backend Queries can auto-refresh the UI with the latest database changes.    |
| **Multiplicity**          | You can specify multiple actions on the same widget.                                                                                      | Only one Backend Query can be specified on a particular widget or page.                                                                 |
| **Conditional Execution** | Can be conditional, meaning they can execute different actions on certain conditions.                                                     | -                                                                                                                                       |
| **Caching**               | -                                                                                                                                         | Can include caching mechanisms to improve app performance by reducing the number of server calls and providing offline access to data.  |
| **Handling States**       | -                                                                                                                                         | Often involve handling loading states and empty states, as the data fetching process can take time and might not always return results. |
| **Data Fetching**         | -                                                                                                                                         | Only used to fetch data from a backend.                                                                                                 |

#### Change loading indicator

While the backend query is busy retrieving results, it shows the default *Project Theme Loading Indicator* (which you can change from [**Navigation menu**](https://docs.flutterflow.io/flutterflow-ui/builder#navigation-menu) *> Theme Settings > Design System > Loading Indicator*.) However, if you want to replace this with a custom loading indicator in a specific backend query, follow the instructions below:

To change the loading indicator:

1. Ensure you have added a backend query.
2. Open the **Backend Query** section (on the right side) and scroll down to the **Backend Query Loading Widget**. Open it by clicking on the arrow icon.
3. Set the **Loading Widget Type** to **Image**. You can also choose a [**Component**](https://docs.flutterflow.io/resources/ui/components/creating-components) if you have already designed a loading component.
4. Enable the **View in UI Builder**. This allows you to see your custom loading indicator on canvas (before you actually run the app).
5. Choose the **Image Type**, [add the image](https://docs.flutterflow.io/resources/ui/widgets/image#image-type), and adjust its **Padding** and **Width**.
6. To show the indicator in the center, turn on the **Center Image** toggle.
7. Run the app, and your custom loading indicator will appear while the data is being loaded.

#### Copy Query

Sometimes, you might want to display the same list of items with a little modification. For example, showing all Todo items and completed Todo items. In such a case, you can copy-paste the entire backend query to speed up the building process. This is helpful, especially when you have a complex backend query.

To copy-paste the query:

1. Select the widget (e.g., ListView, GridView, etc.) where you have already added the backend query.
2. Select the **Backend Query** tab, and click the **Copy** button.
3. Now, select the widget (where you want to add the query), move to the **Backend Query** tab, and click **Paste Backend Query** button.
4. Click **Confirm**.

#### Move query to parent widget

You might want to utilize the same backend query on multiple widgets on a page. But if you do so, you end up making redundant server calls for the same thing. So, instead of copying it on every widget, you can move the query to any parent widget. The existing widgets will then use a generated variable derived from the parent widget's query.

To move the query up to any parent widget, simply select the up arrow button and select the parent widget you would like the query to move to.

#### Displaying empty list widget

The *Empty List* widget is a widget used to display a message when there are no items in a list. This widget helps to provide a better user experience by displaying a message instead of just an empty screen.

To display the empty list widget:

1. Ensure you have added a backend query on any scrollable widget, such as **ListView**, **GridView**, **Column**, **Row**, DataTable, and **StaggeredView**.
2. Select the scrollable widget (on which you have added the backend query), move to the properties panel, and turn on the **Show Empty List Widget**.
3. Set **Widget Type** to **Image** or **Component**. The further options are available based on what you choose.
4. Try toggling the **View in UI Builder**. This allows you to see your empty list widget on canvas (before you actually run the app).
5. You can also control the size and centering of the widget using the available options.

#### Backend Query Caching

Backend query caching refers to the process of storing the result of a backend query in a cache so that subsequent queries for the same data can be served directly from the cache rather than making a new query to the backend.

Caching a query can bring significant benefits to your app, including improved performance and reduced server load. Additionally, caching can enable your app to function offline by serving cached results when there is no internet connection available.

For example, an e-commerce app can cache product data, such as product descriptions, prices, and images, to avoid making unnecessary API calls for each page load.

> **Note:** Caching backend queries works for all [types of queries](https://docs.flutterflow.io/resources/backend-query#types-of-query).

Single time Query

For Firebase queries, enable Single Time Query if you want the query to fetch data only once. Otherwise, the query operates in real-time, updating automatically as soon as the data changes.

##### When to cache

In general, any data that is static, slowly changing, or read more often than they are updated can be cached to improve performance and reduce the load on the server. A few examples are

1. Static content such as images and videos.
2. Configuration data such as application settings or system parameters.
3. Data that is expensive to compute, such as complex reports or analytics.

##### When NOT to cache

Sometimes, it's not a good idea to cache the backend query. Here are some examples:

1. Large amounts of data can cause performance issues and may not be appropriate.
2. Sensitive or confidential data should not be cached, as it could lead to unauthorized access.
3. Frequently changing data, such as in real-time or near real-time scenarios, caching may not be appropriate as the cached data could quickly become stale or outdated.
4. Critical response time where the data needs to be up-to-date and accurate at all times.

##### Example

Let's see how to cache a backend query with an example app that shows a list of employees on the first page and employees' details on the second page. On the employee details page, the data is retrieved from a backend query and read more often than they are updated, so it's a good candidate to cache.

To improve performance, you can cache the data on the details page so that it can be quickly retrieved and displayed to users.

Here is how it looks:

> **Note:** In the visual above, see how the loading indicator appears for the first time a query is made on the page. However, subsequent queries will retrieve the result from the cache, and the loading indicator will not be displayed again.

To cache the backend query:

1. Ensure you have added a backend query. For this example, to retrieve data from a Firebase document, we add a backend query at the page level as *Single Time Query*. We use a document reference to get the employee details.

![example-bq.png](https://docs.flutterflow.io/assets/images/example-bq-2e8203dff7f01fcac18d3e7ea5c25d0a.png)

Querying employee details using document reference

2. Open **Query Cache Settings** and **Enable Query Caching**.
3. Determine the **Scope** of the cache. If you set it to **App Level** and the *exact* same query is made on any other page of the app, it will display the result from the cache. However, if you set the **Page Level**, the cached result will be used only on that page if the query is made multiple times on the same page.
4. If the current query is completely new/different, create a **Query Name**. If not, and you want to use the cached result of this query (that might be created somewhere else), select the name from the list.

5) If we leave this example here, we'll have data inaccuracy issues. That means when any employee data is cached, the same data will be used for all employees, which is not what we want. We want to cache data for all individual employees. To do so, we can set the **Unique Key**. Here the unique key can be the employee id or the document reference.

* Data inaccuracy without Unique Key
* Adding Unique Key

6. At this point, we have enabled the caching, but we still have one problem. Once the query is cached, it will be used forever, although we update the data in our backend. This is because we are not clearing or invalidating the cache at the appropriate time. To properly invalidate the cache, you can use the **Should Override Cache** property OR **Clear Query Cache** action. This helps you remove the cached data that has become stale or outdated.

   1. The *Should Override Cache* property accepts a boolean (True/False). That means we can provide a variable (e.g., an *App State* variable named *isCacheOverride)* that knows when to override the cache. So create one and set it here.
   2. Create one more *App State* variable, something like *lastCacheTime,* and set the current time as default. This will be used to save the time of results retrieved from the backend. You'll better understand how helpful it is in the logic we add in the next step.

![img\_3.png](https://docs.flutterflow.io/assets/images/img_3-2cb11f7171f5524d3bc5c77565c48d51.png)

Setting Should Override Cache to App State variable

7. Now, we must add a logic that determines whether to override the cache (every time when the page is loaded) and set the *isCacheOverride* variable accordingly. Here is how it goes:

   1. First, check if the *lastCacheTime* is set or not. If not, set the current time to it.

   2. Then the idea is to create one custom action that checks if the current time is more than 30 minutes ahead of the *lastCacheTime*. **Note** that 30 minutes is the cache expiration time, and here, it is kept minimum just for simplification purposes; It's important to carefully choose the appropriate expiration time for your cache based on the nature of your data.

   3. if **True** : 1. [Update](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action) the **lastCacheTime** with the current time and **isCacheOverride** to True. Make sure you keep the **Update Type** to **Rebuild Current Page** so that the backend query is made again, which will invalidate the cache and display updated data.
      2. You can also add an action to [Clear Query Cache](https://docs.flutterflow.io/resources/backend-query).
      3. Continuing the same action flow, [wait](https://docs.flutterflow.io/resources/time-based-logic/wait-action) for 1 sec and again update **isCacheOverride** to **False** so that the cached result won't override on page load for the next 30 min.

Note

**Note** that in this example, we use both the *Clear Query Cache* action and the *Should Override Cache* property to clear or invalidate the cache. Although both perform the same task, it's generally considered better practice to explicitly *Clear Query Cache* rather than relying on the *Should Override Cache* bool. However, in certain cases, you may want to override the cache conditionally instead of with an explicit action, so the option is there.

Here is how the custom function looks in case you want to check:

```
bool isOverrideCacheAction(DateTime cacheTime) {
  // Add your function code here!
  return DateTime.now().difference(cacheTime).inMinutes > 30;
}
```

![custom-func-cache-override.png](https://docs.flutterflow.io/assets/images/custom-func-cache-override-d3687d8170b91d2b91af9e9b031b0b1f.png)

Custom function to know if last cache time is more than 30 minutes

> **Tip:** You can have a separate *lastCacheTime* variable for all the employee records to avoid any conflict with others. Failing to do so may keep on updating the common *lastCacheTime* variable, and you might not see updated data. For example, creating a list of JSON that contains the id and *lastCacheTime* of an employee might help. Like this:

`{ "id": 1, "lastCacheTime": '2023-03-22T14:30:00+00:00', }`

##### Clear Query Cache \[Action]

This action provides a simple way to clear the query cache, which can be helpful in situations where the cached data is no longer accurate or needs to be refreshed. By executing this action, you reset the query cache, allowing the app to fetch and display the most up-to-date data.

> **Tip:** This can help improve app performance and ensure users see the most recent information available.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the [properties panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Clear Query Cache** (under *State Management*) action.
4. Determine the **Scope** of the cache, whether it lives at the **App Level** or **Page Level**.
5. Set the **Query Name** to the one you gave while adding the query cache.
6. If you have set the **Unique Key** while caching a query, you should add the same key here as well. This ensures that the cache will be removed only for specific data.

---

### Algolia Search Query {#algolia-search-query}

*Learn how to perform an Algolia search query in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/backend-query/algolia-search-query

You can set up an **Algolia Search Backend Query** to automatically trigger a search as soon as the user navigates to the page. This allows users to find documents within a Firestore Collection by simply providing a search term.

This approach is particularly useful for enhancing the user experience, such as dynamically refreshing search results in a **ListView** as the user types in a TextField, like real-time updates.

Prerequisites

Before proceeding, ensure that you have **completed the [Algolia integration](https://docs.flutterflow.io/integrations/search/algolia-search#algolia-integration)** in FlutterFlow.

To add an **Algolia Search Query**, begin by selecting the scrollable widget that will fetch the results, such as a **ListView**. In the **Properties Panel**, navigate to the **Backend Query** tab, click on **Add Query**, and set the **Query Type** to **Algolia Search**.

Next, configure the search parameters: for **Firebase Collection**, select the Firestore collection you intend to search; for **Search Term**, choose **From Variable** and select the TextField's value (e.g., **Widget State > \[Your TextField]**); and specify the optional **Max Results** to determine the number of search results.

---

### API Call Query {#api-call-query}

*Learn how to perform an API call query in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/backend-query/api-call-query

You can use the **API Call Query** to trigger an API call automatically as soon as the page or widget is loaded. This is helpful if you want to retrieve the data from an API call and display it on a page or widget. For example, showing a list of items in a ListView, showing users details on several Text widgets.

Prerequisites

Before you add this query, ensure you [create an API call](https://docs.flutterflow.io/resources/backend-logic/rest-api) in your project

#### Adding API Call query

Adding API call query comprises the following steps:

1. [Querying API call](https://docs.flutterflow.io/resources/backend-query/api-call-query#1-querying-api-call)
2. [Showing query data in UI element](https://docs.flutterflow.io/resources/backend-query/api-call-query#2-showing-query-data-in-ui-element)

##### 1. Querying API call

Go to your project page and follow the steps below to define an **API Call** backend query:

1. Select the **widget** (or page) on which to apply the query.

2. Select **Backend Query** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu).

3. Select the **Query Type** as ***API Call***.

4. Choose the API **Group or Call Name** from the dropdown. It would display all the API Calls created in your project.

5. If your API call requires variables (e.g., auth token, query parameters, user id, etc.), pass their value by clicking on the **+ Set Additional Variable** button.

6. Click **Confirm**.

##### 2. Showing query data in UI element

Once you have the API Call query defined, you can use the data retrieved from the query to display on widgets present inside. Follow the steps below:

1. Select the **widget** (e.g., `Text`) on which you want to display the data.

2. From the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel), select **Set from Variable**.

3. Select the **Source** as the **YOUR\_API\_CALL\_NAME Response**.

4. Set the **API response Options** to **JSON Body**.

5. Set the **Available Options** to **JSON Path**.

6. Set the **JSON Path Name** to either the custom JSON path or use the already created JSON path. See how to [**create a JSON path**](https://docs.flutterflow.io/resources/backend-logic/rest-api#add-json-predefined-path).

7. Click **Confirm**.

---

### Document from Reference {#document-from-reference}

*Learn how to retrieve a document from a reference in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/backend-query/document-from-reference

This backend query would help you in retrieving information from a document reference. You will require the **Document from Reference** query if you have passed a document reference to a different page of the app and want to retrieve the actual document information from the reference.

Prerequisites

In order to use this backend query, you should have:

* Completed all the steps of [**Firebase Setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) for your project.
* At least one **Firestore Collection** is defined in your project.

#### Defining the Query

Go to your project page on FlutterFlow and follow the steps below to define a **Document from Reference** backend query:

1. Select the **widget** (or page) on which to apply the query.
2. Select **Backend Query** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu).
3. Select the **Query Type** as ***Document from Reference***.
4. Choose a **Collection** from the dropdown to which the document reference belongs.
5. Select the **Source** as the record reference name.

#### Using Query Data

The document information retrieved from the backend query can now be set on the widgets present inside. Follow the steps below:

1. Select the **widget** (eg, `Text`) on which you want to set the record data.
2. From the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel), select **Set from Variable**.
3. Choose the **Source** as the record variable.
4. Under **Available Options**, select a field name.
5. You can also specify a **Default Value** (it is used if the record field is empty).
6. Click **Save**.

You can follow similar steps for using the record data on the other widgets as well.

---

### Query Collection / Table {#query-collection-table}

*Learn how to query a collection in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/backend-query/query-collection

Quering Firestore Collection or Supabase Table helps you to retrieve a record (or a list of records) automatically whenever a user navigates to the page containing the query. The information that is present in the record can be used to update any widget present inside.

Prerequisites

* To query Firestore collection, complete the [**Firebase setup**](https://docs.flutterflow.io/integrations/firebase/connect-to-firebase) and have some data in a [**Collection**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections).
* To query Supabase table, complete the [**Supabase**](https://docs.flutterflow.io/integrations/supabase/setup) Setup and have some data in a [**table**](https://docs.flutterflow.io/integrations/supabase/setup#create-tables-in-supabase).

#### Defining the Query

Go to your project page on FlutterFlow and follow the steps below to define a **Query Collection** backend query:

1. Select the **widget** (or page) on which to apply the query.

2. Select **Backend Query** from the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu).

3. Select the **Query Type** as ***Query Collection***.

4. Choose the Firestore **Collection** to use for performing the query.

5. Under **Query Type**, select either ***List of Documents*** (returns a list of document references) or ***Single Document*** (returns only one document reference).

6. If you have selected the **List of Documents**in the previous step, you can set a **Limit** to the maximum number of documents returned.

7. If you want to apply any **filter** for retrieving the documents, click **+ Filter** button. Select a **Field Name** that you want to use as the filter, choose a **Relation** ( eg, `Equal To`, `Greater Than`), and then select the **Value Source** (either as a `Specific Value` or `From Variable`) with which the relation is to be checked.

8. You can also set the **order** in which the documents should be returned, click **+ Order By** button. Select a **Field Name** to be used for ordering, and choose the **Order** to be either `Increasing` or `Decreasing`.

9. Below are some optional settings that you can configure based on your requirements: * **Single Time Query**: When this is disabled, the query results will automatically refresh whenever documents or rows are created, updated, or deleted. However, for **Supabase**, this option is enabled by default, meaning the query will run only once. To enable real-time updates, you must turn it off.
   * **Ignore Empty Filter Values**: Disabled by default, meaning the query will attempt to find documents with empty text fields if any filter value is empty. When enabled, the query will ignore fields with empty filter values instead.
   * **Filter on Null Values**: By default, if any filter value is null, the query will ignore that filter. Enabling this option will include null filters in the query.
   * **Enable Infinite Scroll**: To implement infinite scrolling, enable this option and follow the instructions here.

10. Click **Confirm**.

11. If the selected query returns a list of documents and if it's applied to any flexible widget (like `Column`, `Row`, or `ListView`) then FlutterFlow will generate the children widgets dynamically. A dialog will be displayed with a similar message, click **Confirm**.

> **Info:** The instructions to query a Supabase table are almost the same, except that for **Query Type**, you should select **Supabase Query**.

Limitations of Supabase Streaming with Filters

When using Supabase query with real-time updates enabled, you have the following limitations:

* **Only One Filter is Supported:** Supabase streaming supports only a single filter. Combining multiple filters (e.g., `isActive = true AND city = 'Los Angeles'`) is not allowed.
* **Delete Events are not Filterable:** Streaming queries do not detect deletions, even if the deleted row matches the filter condition. For example, If you are streaming rows with the filter `city = 'New York’` and a row is deleted, the query output will not reflect the deletion.
* **Updates that remove Rows from Filters are not Tracked:** Changes that make a row no longer match the filter condition (e.g., updating `isActive` from `true` to `false`) will not trigger an update in the query output.

For more details, refer to the limitations mentioned in the [**official Supabase docs**](https://supabase.com/docs/guides/realtime/postgres-changes?queryGroups=language\&language=js\&queryGroups=database-method\&database-method=dashboard#delete-events-are-not-filterable).

#### Using Query Data

The documents retrieved from the backend query can be used to set the record values to the widgets present inside. Follow the steps below to use the document record data:

1. Select the **widget** (eg, `Text`, `Image`, or `ToggleIcon`) on which you want to set the record data.
2. From the [Properties Panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel), select **Set from Variable**.
3. Choose the **Source** as the record variable (the variable gets automatically generated when you add the Collection query).
4. Under **Available Options**, select a field name from the dropdown.
5. You can also specify a **Default Value** (it is used if the record field is empty).
6. Click **Save**.

You can follow similar steps for using the record data on the other widgets as well.

* Display Data from Firestore Collection
* Display Data from Supabase Table

#### FAQs

Why aren't real-time updates working for my table in Supabase project?

First, ensure that the **Single Time Query** option is disabled in the query where you've added it. Then, verify that the real-time feature is enabled for your table in Supabase project. You can find this option in the top-right corner of the table viewer.

![enable-realtime-updates-sb-table.avif](https://docs.flutterflow.io/assets/images/enable-realtime-updates-sb-table-95fa64a0cdbd78f1e79188e5bf7b1185.avif)

Additionally, you can enable real-time updates when creating a new table.

![enable-realtime-updates-sb-table.avif](https://docs.flutterflow.io/assets/images/enable-realtime-updates-sb-table-2-7d1cd5f9ba25c093103146d03d897787.avif)

---

### SQLite Query {#sqlite-query}

*Learn how to perform SQLite queries in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/backend-query/sqlite-query

SQLite Query can be set up to automatically execute SQL statements as soon as a page or widget loads. This feature is useful for fetching data from the database to display on a page or widget, such as populating a ListView with items or showing user preferences in Text widgets.

![img\_4.png](https://docs.flutterflow.io/assets/images/img_4-47bd29266be6894e21641f3871e9798b.png)

Prerequisites

Before you add this query, ensure you configure the database and define the query. Check detailed instructions [here](https://docs.flutterflow.io/integrations/database/sqlite).

#### Adding SQLite query

Let's see how to display a list of items from the database using the SQLite query. Here are the steps:

1. [Add query](https://docs.flutterflow.io/resources/backend-query/sqlite-query#1-add-query)
2. [Showing query data in UI element](https://docs.flutterflow.io/resources/backend-query/sqlite-query#2-showing-query-data-in-ui-element)

##### 1. Add query

Go to your project page and follow the steps below to define an SQLite query:

1. Select the **widget** (or page) on which to apply the query.
2. Select **Backend Query** from the Properties Panel (the right menu).
3. Click **Add Query** and set the **Query Type** to **SQLite Query**.
4. Select the **Query Name**. (Only *Read Queries* will be displayed here.)
5. Click **Confirm**.

##### 2. Showing query data in UI element

Once you have the SQLite query defined, you can use the data retrieved from the query to display on widgets present inside. Follow the steps below:

1. Select the **widget** (e.g., `Text`) on which you want to display the data.
2. From the Properties Panel, open the **Set from Variable** menu **>** select **\[your query name] Row** **>** select the column data that you want display here.
3. Click **Confirm**.

---

### Control Flow Concepts {#control-flow-concepts}

*Understand and implement control flow in your FlutterFlow app to manage the execution of statements, instructions, and function calls under various conditions.*

**Source:** https://docs.flutterflow.io/resources/control-flow-concepts

In app development, control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated. Proper control flow ensures that your app behaves as expected under various conditions and user interactions. This involves understanding and implementing **conditionals**, managing **sequential and parallel** logic flows, handling **blocking and non-blocking** actions, and deciding when and how to execute specific actions based on certain criteria.

In this section, we will explore various control flow concepts and how they can be effectively implemented in FlutterFlow to create dynamic, responsive, and efficient applications.

#### Conditional

One of the fundamental aspects of control flow is the use of conditionals, which allow your app to make decisions and execute different blocks of code based on specific criteria. Conditional statements are expressions that evaluate to either true or false. Depending on the result of these evaluations, different logic sequences are executed.

The primary conditional statements are `if`, `if-else`, and `else`.

* **`if` Statement:** The if statement evaluates a condition and executes a block of code if the condition is true.

The if statement evaluates a condition and executes a block of code if the condition is true.

![if-condition.png](https://docs.flutterflow.io/assets/images/if-condition-46b2d18ed56b7c74168db859e37fe0ae.png)

* **`if-else` Statement:**

The if-else statement provides an alternative block of code to execute if the condition is false.

![if-else-condition.png](https://docs.flutterflow.io/assets/images/if-else-condition-8a738666792cecca224759a3cd726e51.png)

Here, if `userIsLoggedIn` is true, the app will show a welcome message. Otherwise, it will prompt the user to log in.

* **`else if` Statement:**

The `else if` statement can be used to check multiple conditions sequentially.

![if-elseif-condition.png](https://docs.flutterflow.io/assets/images/if-elseif-condition-8606606c66f1fe359dcf7d42f61183ca.png)

This example demonstrates multiple conditions. If `userIsLoggedIn` is true, it shows a welcome message. If not, it checks if `userIsGuest` is true and shows a guest message. If neither condition is met, it prompts the user to log in.

##### Implementing Conditionals

In FlutterFlow, you can implement conditional logic in two primary ways:

* **[When Setting Properties](https://docs.flutterflow.io/resources/functions/conditional-logic#setting-widget-properties-with-conditional-logic)**

  In FlutterFlow, you can set properties of widgets conditionally. For example, you might want to change the color of a button based on a variable's value. You can use conditional expressions to dynamically set these properties during runtime.

* **[Conditional Actions](https://docs.flutterflow.io/resources/functions/conditional-logic#conditional-actions)**

  You can also perform conditional actions in FlutterFlow, where certain actions are executed only if specified conditions are met. This is useful for implementing logic like navigating to different pages based on user input or showing/hiding widgets.

  Example: If the user clicks a button and a form is valid, navigate to the next screen; otherwise, show an error message.

> **Info:** Check out the [**complete guide**](https://docs.flutterflow.io/resources/functions/conditional-logic) here. Are you looking to learn about implementing conditional UI instead? Check out our **[Responsiveness 101](https://docs.flutterflow.io/concepts/layouts/responsive)** guide instead.

#### Sequential vs Parallel Logic Flow

* **Sequential Logic Flow**: Actions are executed **one after the other**. Each action waits for the previous one to complete before starting. This is useful for tasks that depend on the outcome of previous actions.

  **Example:** Submitting a form, waiting for a server response, and then showing a confirmation message.

* **Parallel Logic Flow** Multiple actions are executed at the **same time**, independently of each other. This is useful for tasks that can be done simultaneously and do not depend on each other's outcomes.

  **Example:** Loading data from multiple sources simultaneously to speed up the data fetching process. ![parallel-sequential.png](https://docs.flutterflow.io/assets/images/parallel-sequential-14310ce3eccf7c5d31ebd268d3ddffb1.png)

#### Asynchronous Functions

Asynchronous functions are operations that do not complete immediately and may finish at a future time due to network delays or long computation times.

They can be made **blocking** or **non-blocking** depending on the use case. Some examples of asynchronous operations include:

* **Network requests** (e.g., fetching data from an API)
* **Database operations** (e.g., reading or writing data)
* **Long-running computations** (e.g., complex calculations)
* **Animations** (e.g., transitions, widget animations)

##### Blocking Actions

Blocking actions are actions that halt the execution of subsequent actions until they are completed. These actions typically involve operations that take time, such as network requests or animations.

Generated Code

In the **generated code**, FlutterFlow uses the `await` keyword to pause the execution of an asynchronous function until the operation completes before proceeding to the next function. This approach is commonly used to handle asynchronous functions, ensuring that each operation finishes before the subsequent one begins.

In the following example from **generated code**, the code **awaits** on `actions.getRandomIntAfterWait()` because it is an asynchronous function that takes around 2 seconds to complete and provide a result (in this case, a random integer).

```
    _model.result = await actions.getRandomIntAfterWait();
    _model.text1Value = _model.result.toString();
```

The result of the `actions.getRandomIntAfterWait()` is stored in `model.result` variable and then the result then set to a Text widget using the Page State variable `text1Value`.

##### Non-Blocking Actions

Non-blocking actions, on the other hand, allow the program to continue executing other subsequent tasks while waiting for the initial actions to complete in the background.

Generated Code

In the **generated code**, when an asynchronous function is made **non-blocking**, FlutterFlow removes the `await` keyword. This means the subsequent function will not wait for the asynchronous action to complete and will move to the next action immediately.

The previous example will no longer work because it doesn't await the asynchronous function `actions.getRandomIntAfterWait()`. As a result, the variable `model.result` may not be ready or available when `_model.text1Value = _model.result.toString();` is executed.

```
_model.result = actions.getRandomIntAfterWait();
_model.text1Value = _model.result.toString(); // will throw errors
```

To ensure proper execution, make only those actions non-blocking whose subsequent actions do not depend on the results from these initial functions.

#### Non-Blocking vs Parallel Actions

| Non-Blocking Actions                                                                                                          | Parallel Actions                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Allows the subsequent action to run **immediately** after the current one without waiting for the current action to complete. | Allows users to run two or more actions at the **same time** independently.            |
| **Only asynchronous** functions can be made non-blocking.                                                                     | **Both asynchronous and synchronous** functions can be included in parallel actions.   |
| Ideal for tasks where the result of the action is not immediately needed by the next action.                                  | Ideal for independent tasks that can be executed simultaneously to improve efficiency. |
| Ensures the app remains responsive by not waiting for long-running tasks.                                                     | Helps in reducing overall execution time by performing multiple tasks concurrently.    |
| **Example**: Fetching data in the background while allowing user interaction.                                                 | **Example**: Loading data from two APIs simultaneously to save time.                   |

---

### Control Flow & Logic {#control-flow-logic}

*Control flow in programming refers to the order in which individual statements, instructions, or*

**Source:** https://docs.flutterflow.io/resources/control-flow-overview

Control flow in programming refers to the order in which individual statements, instructions, or function calls are executed or evaluated. Proper control flow is crucial for determining how your app responds to user inputs and events. Here are some key elements:

* **[Conditional Flows:](https://docs.flutterflow.io/resources/control-flow-concepts)** These include `if`, `else if`, and `else` flows that allow your app to make decisions based on certain conditions. For example, you might check if a user is logged in and then show different content based on their authentication status.

* **[Loops:](https://docs.flutterflow.io/resources/functions/loops)** Loops allow your app to repeat a sequence of logic multiple times. This is useful for tasks like iterating through a list of items or retrying a failed operation.

* **[Event Handling:](https://docs.flutterflow.io/resources/functions/action-flow-editor#action-triggers)** In certain cases, you will execute functions that are triggered by specific events such as user interactions (e.g., taps, swipes) or system events (e.g., page load, on focus change). Understanding how to handle such events effectively ensures that your app reacts appropriately to user interactions or events.

**Logic** or **Functions** refer to the core operations and behaviors that determine how an app responds to user actions and interacts with data. This could include:

* **Business Logic:** This is the part of the app that manages the rules and processes of the real world. For example, in an e-commerce app, it handles tasks like processing orders, calculating prices, and managing inventory.

* **User Interface Logic:** This controls how the app looks and interacts with users. It includes tasks like validating forms, navigating between screens, and updating content based on user actions.

* **Data Logic:** This manages the app's data. It includes tasks like fetching, storing, updating, and deleting data from databases or via APIs.

Let's dive into few more key concepts:

#### Functions

A function is a block of code designed to perform a specific task. Functions can be reused throughout your application to perform common tasks efficiently.

##### Triggers or Running a Function

Functions can be executed in various ways: they can be called from properties within the app, such as performing a quick calculation or number formatting before setting the final value to a variable, or concatenating strings before setting the string to a text widget. Functions can also run in response to specific events, such as a button click or a page load.

##### Types of Functions

There are different types of functions you can use in your app. Some examples in FlutterFlow are:

* **[Built-in Utility Functions](https://docs.flutterflow.io/resources/functions/utility):** Functions that perform general utility tasks, such as formatting data or performing calculations. In FlutterFlow, you can use [**Inline Function**](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions) for simple data manipulation tasks or use the **[Combine Text](https://docs.flutterflow.io/resources/functions/utility#combine-text)** built-in function to concatenate strings.

* **[Actions](https://docs.flutterflow.io/resources/functions/action-flow-editor):** Sequence of Logic performed in response to user interactions. For example:

  * **[Updating State Variables:](https://docs.flutterflow.io/concepts/state-management)** Functions that modify the current state or data of the app, page, or component.

  * **Widget-specific Functions:** Functions applicable to various widgets that need specific actions, such as scrolling to an item in a ListView, clearing text fields, or calling third-party integration functions.

  * **[Custom Actions:](https://docs.flutterflow.io/concepts/custom-code/custom-actions)** More complex actions written in **Flutter & Dart** that can be added as a node to the action flow editor.

* **[Navigation:](https://docs.flutterflow.io/concepts/navigation/overview)** Functions that handle the movement between different pages or screens within your app, including opening bottom sheets or dialogs. In FlutterFlow, such functions can either run automatically after certain related operations, such as Login/Create Account, or they can be added as individual **Actions** if the developer enables it.

* **[Backend Queries:](https://docs.flutterflow.io/resources/backend-query)** Functions that interact with your database or external services to retrieve or manipulate data.

* **[Custom Functions:](https://docs.flutterflow.io/concepts/custom-code/custom-functions)** Complex manipulation code written in **Dart**, used to set properties of a widget or an action.

##

---

### Overview {#overview}

*Explore the essentials of data representation in app development, focusing on the use of variables in FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/data-representation

Data representation is a fundamental concept in app development. It refers to the methods and structures used to store and manipulate the data. The way data is structured can greatly influence how efficiently an app performs tasks.

#### Variable

In FlutterFlow, variables are key to managing dynamic data, ensuring your app remains interactive and responsive. They enable you to capture user inputs, track changes, and share data across different parts of your app.

> **Info:** Dig deeper into **[variables and variable scopes](https://docs.flutterflow.io/resources/data-representation/variables)**.

#### Data types

Data types are used to define the kind of data that variables can store and manipulate within your app. Managing data types correctly is crucial for ensuring that your app functions as intended, particularly when handling user inputs, storing data, and interacting with databases.

> **Info:** Learn more about primitive and composite data types in this [**detailed guide**](https://docs.flutterflow.io/resources/data-representation/data-types) and then create your own **[custom data type](https://docs.flutterflow.io/resources/data-representation/custom-data-types)**.

#### Data mutability

All variables in FlutterFlow are mutable. This means you can change their values at runtime based on user interactions or other events in your app. FlutterFlow also supports immutable data, such as [**Constants**](https://docs.flutterflow.io/resources/data-representation/constants) that cannot be changed once they have been set.

#### Global Properties

Global properties in FlutterFlow are built-in variables that you can use across your app, but they cannot be created or modified by users. Learn how to leverage these [**predefined properties**](https://docs.flutterflow.io/resources/data-representation/global-properties) to simplify common tasks.

#### Encapsulation

Encapsulation is a key concept in object-oriented programming (OOP). It bundles the data (fields) and the methods (functions) to manipulate the data. It also limits direct access to some data to prevent accidental changes. This concept is essential in improving security and functionality by managing data access and modification.

##### How Encapsulation is achieved in FlutterFlow

FlutterFlow supports the principles of encapsulation through its visual development environment. Let’s understand this with some examples:

1. **Custom Widgets and Components**: In FlutterFlow, you can create custom widgets or use built-in widgets that encapsulate specific functionalities. These widgets can include both logic and UI elements that are bundled together.

   For example, if you are creating a user profile page, you can create a custom component that includes the user's photo, name, and contact button. This component can be reused wherever a user profile needs to be displayed in the app, ensuring that changes to the profile layout or functionality are centralized within this widget.

2. **Backend Actions**: FlutterFlow allows you to define backend actions that can be called from different parts of your app. These actions can encapsulate complex logic, such as processing user input, interacting with databases, or calling external APIs.

   By defining such actions, you can manage how data is processed and passed around in your applications. This helps in maintaining a clear separation between the UI and business logic, which is a core principle of encapsulation.

##### Benefits of Encapsulation in FlutterFlow

* **Reusability**: Encapsulated components are reusable across different parts of the application without requiring duplication of widgets.
* **Maintainability**: Changes to the application’s data handling or business logic can be made in a single place using action blocks rather than having to make widespread modifications across many actions.
* **Scalability**: Applications can grow more naturally and with less complexity when their components are well-encapsulated.

---

### App State {#app-state}

*Learn how to effectively utilize App State Variables in FlutterFlow to maintain and manage global application states across all pages and components.*

**Source:** https://docs.flutterflow.io/resources/data-representation/app-state

App state variables are specific variables that hold the current state of an application. They can be accessed and modified throughout the entire application across all pages and components. This type of variable can be useful for storing data that needs to be shared between different parts of the app, such as user preferences and authentication tokens.

![app-state-variables.avif](https://docs.flutterflow.io/assets/images/app-state-variables-c3be8e44314611883d9decf575ab0882.avif)

App state variables should be used in scenarios where the same data needs to be accessed and modified from multiple locations within the app. For instance, in a shopping cart app, items in a user's cart are usually accessible across different pages.

App state variables should not be used for temporary data that doesn't impact the overall state of the application. For instance, a user's temporary input in a form should not be stored in an app state variable. It would be more appropriate to use a [page state](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state) or [component state](https://docs.flutterflow.io/generated-code/state-management#component-state) variable instead.

#### App State Variables

Let’s see how you can manage the app state variable using an example of adding items to a cart in a shopping app.

##### Create App State variable

Head over to the left-side navigation menu and follow the steps below to create a variable.

[Sharing a Project with a User](https://demo.arcade.software/QjdQ0cTmGDqUeG6F1JMh?embed\&show_copy_link=true)

###### App State Properties

* **isList:** Whether this field is a list type (e.g List of String or List of Custom Data Type)
* **Persisted:** Whether this app state is saved to disk so that it can be loaded when the app is restarted. Otherwise the field will be reset on restart.

Generated Code

Curious about what happens when the **Persisted** toggle is on? Check out the [**Generated Code**](https://docs.flutterflow.io/generated-code/state-management#persisting-app-state) guide.

##### Use App State

The variable can now be accessed via set from variable menu. For example, on the cart page, you can loop through the app state variable to display each item.

![access-app-state-variable.avif](https://docs.flutterflow.io/assets/images/access-app-state-variable-32ed5e4451632f8519881db24b694184.avif)

##### Update App State \[Action]

You can update an app state from the Actions Panel anywhere in the app, whether it's on tap of a widget in a component or page, or via custom code in FlutterFlow.

When you update the app state via the Action Flow Editor, you will find the following options in the Action Settings. ![update-app-state-action.png](https://docs.flutterflow.io/assets/images/update-app-state-action-17d969477327725f5d471be230a97ee1.png)

###### Update Type

How this app state update will affect your app.

* **Rebuild All Pages:** Rebuilds all pages in the app when this app state is updated.
* **Rebuild Current Page:** Rebuilds only the current page when this app state is updated.
* **No Rebuild:** No rebuild is required.

Generated Code

Curious about how state changes are handled internally when you choose different **Update Type** options? Explore the detailed [**FFAppState**](https://docs.flutterflow.io/generated-code/ff-app-state) guide.

Here's a quick guide to updating the app state variable. We need to add an action to the 'Add to Bag' button. Within this action, we'll provide the product details and configure it to add to the current cart list.

[Sharing a Project with a User](https://demo.arcade.software/FKv2dXq4jTjjJVLy6nxu?embed\&show_copy_link=true)

> **Tip:** If you want to rebuild a page or component without updating any state variables, use the [**Rebuild**](https://docs.flutterflow.io/concepts/state-management#rebuild-action) state action.

#### FAQs

Why are some variable types not available in App State?

Certain variable types, e.g., **Firestore Documents** and **Supabase Row**, can be used in Page State or Component State, but not in App State. This is because App State variables are designed to be global, meaning they stay in memory throughout the app. When App State variables are marked as persisted, the variable’s value is saved to the device’s local storage.

Storing large or complex data types like documents in App State could lead to **performance or size issues**, especially on lower-end devices. For this reason, FlutterFlow limits App State to lightweight types, while Page/Component State allows for more flexibility since their scope is smaller and temporary.

If you need to work with such data types, it's recommended to store them in Page or Component state instead.

---

### Constants {#constants}

*Explore the importance of using Constants in FlutterFlow to define unchanging values throughout your application.*

**Source:** https://docs.flutterflow.io/resources/data-representation/constants

Constants are used to define values that remain unchanged throughout the lifetime of an application. Using constants is a good practice for values that do not need to be recalculated or reassigned.

Constants are used to define values that you believe are fixed, like API endpoints, standard mathematical values, maximum size limits set by business rules, etc.

When to use Constants vs **[App state variables](https://docs.flutterflow.io/resources/data-representation/app-state)?**

Constants don't change. Once you set its value (in builder), you can't change it from within the app. On the other hand, app state variables are dynamic. They can be updated in response to interactions in the application, such as a user clicking a button or entering data.

#### Create and use Constants

[Sharing a Project with a User](https://demo.arcade.software/Dftl0AAL3w3fw6TjaiBR?embed\&show_copy_link=true)

Naming Convention

Prefer using a lowercase `k` prefix for constants to indicate their immutability, especially for project-specific constants. This approach is more concise and aligns with Dart's common practices. To learn more, refer to the guide on **[Naming Variables & Functions](https://docs.flutterflow.io/resources/style-guide)**.

---

### Custom Data Types {#custom-data-types}

*Learn how to create and utilize custom data types in FlutterFlow to handle complex data structures that predefined types can't cover.*

**Source:** https://docs.flutterflow.io/resources/data-representation/custom-data-types

In FlutterFlow, custom data types allow you to define structured data models that enhance data management and consistency across applications. These data types serve as blueprints for organizing related data attributes.

For instance, you can define a custom data type "Book" that combines predefined data types, such as a string for the title, an integer for the year of publication, and a list of strings for the authors.

Custom data types have several key advantages:

* **Reusable**: Define once, use everywhere.
* **Easy to Update**: Change data structure in one place, and see it reflected throughout your app.
* **Consistent**: Keeps data format uniform across the application.
* **Efficient**: Simplifies complex data handling, reducing errors and redundant code.

> **Info:** * Use custom data type when predefined data types, such as *integer* and *string* may not be enough to store certain kinds of information.
* FlutterFlow also supports some [**Built-in Data Types**](https://docs.flutterflow.io/resources/data-representation/data-types#built-in-data-types).

![custom-data-types.avif](https://docs.flutterflow.io/assets/images/custom-data-types-3b137f5c280f5408c0e9683670a4059d.avif)

When you create a custom data type, it internally creates a Struct. A struct, or structure, is a composite data type that lets you combine fields of different data types to construct a data structure to suit your specific needs.

> **Info:** The class name for such data types is generated by appending "Struct" to the name of the data type. For example, if you create a custom data type called "Cart", the corresponding class would be named "CartStruct".

#### Creating Custom Data Type

To create a custom data type, specify its name and the corresponding fields. Each field can have a distinct data type. You can also specify if a field should allow multiple entries using the **Is List** toggle.

[Sharing a Project with a User](https://demo.arcade.software/fdx2RldmRxm5VeQdaHyd?embed\&show_copy_link=true)

Naming Convention

When naming custom data types, always use **UpperCamelCase**, as recommended by the Dart Style Guide. To learn more, refer to the guide on **[Naming Variables & Functions](https://docs.flutterflow.io/resources/style-guide)**.

#### Accessing Custom Data Type

After creating a custom data type, it’s treated internally as a [Dart class](https://dart.dev/language/classes). However, just defining the custom data type doesn’t hold any real data. To work with actual data, such as storing a user profile or a review, you need to create an **instance** of custom data type.

Creating an instance allows you to:

* Assign specific values to each field in your custom data type.
* Store the instance in app state, page state, or pass it between widgets.
* Access individual fields wherever needed.

To create an instance of a custom data type, first you need to [create a state variable](https://docs.flutterflow.io/concepts/state-management#creating-state-variables) (of type **Data Type**) that will hold the instance. Then, to create and add the instance to the state variable, open the **Set from Variable** dialog and select **Create Data Type Object > Project Data Type**. Choose the data type you want to use. After that, set values for each of the required fields.

##### Custom Data Type in Custom Code

Sometimes, you might want to access the custom data type in your custom code. Our custom code editor allows you to receive and pass data into a variable of a custom data type. For example, you could manipulate or analyze the data as needed, and then return the modified result in the custom data type.

![custom-data-in-custom-code.avif](https://docs.flutterflow.io/assets/images/custom-data-in-custom-code-f280a8eb9e12f1f2736693bf81d4e2f9.avif)

#### Use case: mapping JSON responses from API calls

Consider a case where you're calling an API that returns product details. You could create a custom data type 'Product' representing the JSON structure and then map the JSON values to the custom data type field.

So, if the JSON response looks like this:

```
{
  "id": "a1b2c3d4e5f678901234567",
  "name": "Jacket",
  "price": 199.99,
  "reviews": [
    {
      "id": "rev101",
      "username": "mike",
      "rating": 4,
      "comment": "This product exceeded my expectations in every way. Highly recommended!",
    },
    {
      "id": "rev102",
      "username": "kera",
      "rating": 2,
      "comment": "Great quality, but the color was not as shown in the picture.",
    }
  ],
}
```

Here’s how you map into a custom data type:

![mapping-json-to-custom-data-type.avif](https://docs.flutterflow.io/assets/images/mapping-json-to-custom-data-type-3ea9203a0888b0f13cdb3fb1eca985c7.avif)

---

### Data Types {#data-types}

*Dive into the diverse range of data types supported by FlutterFlow, from basic primitives like integers and strings to complex composite types and built-in functionalities tailored for app development.*

**Source:** https://docs.flutterflow.io/resources/data-representation/data-types

FlutterFlow supports a variety of data types to accommodate different needs in your app. These data types range from the basic, such as integers and strings, to more complex types like lists, maps, and built-in data types.

#### Primitive Data Types

Primitive data types are the most basic data types. They include **integers**, **doubles**, **booleans**, and **strings**. These are the building blocks and are essential in any kind of app development.

#### Composite Data Types

Composite data types are made up of primitive data types. They can hold multiple values and can be used to structure and organize data in a more meaningful way. Examples of composite data types include **lists** and **custom data types**.

##### Custom Data Types

You can also create your own custom data types. This can be especially useful when you need a specific structure for your data that doesn't fit into the predefined types. For example, you might create a custom data type for a user profile, which includes several pieces of data like a name, an email address, and a profile picture.

> **Info:** Learn more about creating and using [**Custom Data Types**](https://docs.flutterflow.io/resources/data-representation/custom-data-types).

#### Built-in Data Types

FlutterFlow's built-in data types are essential for effectively managing and organizing diverse information. They ensure data consistency and easy data retrieval. They handle functionalities from storing simple color values and media URLs to complex geographical data.

For instance, the **GooglePlace** data type manages location data like coordinates, place name, and address, while the **Uploaded File** type handles uploaded file data, including file name, binary data, and image dimensions. This standardization is crucial as it allows you to focus on higher-level application logic without worrying about the underlying data handling specifics. Below is a list of all supported built-in data types:

* **Color**: Stores color values.
* **Image Path**: Stores the URL of uploaded images.
* **Video Path**: Stores the URL of uploaded videos.
* **Audio Path**: Stores the URL of uploaded audio files.
* **Document Reference**: Stores references to documents, simplifying data fetching.
* **Document**: Stores actual Firestore documents.
* **Date Time**: Stores date and time values.
* **Json**: Stores JSON values, such as `{"firstName":"John", "lastName":"Doe"}`.
* **LatLng**: Stores the latitude and longitude of specific locations, aiding Google Maps integration.
* **TimestampRange**: Stores start and end date-time values.
* **GooglePlace**: Stores GooglePlace data.
* **Data Type**: Stores custom data types.
* **Supabase Row**: Stores actual row data from a Supabase table.
* **Uploaded File (Bytes)**: Stores uploaded files in Bytes.

#### Enums

Enums, or enumerated types, are a special kind of data type that consists of a set of related values. They can be used to create a type-safe way of dealing with a specific set of values. For instance, you may have an enum for user roles, such as 'admin', 'user', and 'guest'.

> **Info:** Learn more about creating and using enums [**here**](https://docs.flutterflow.io/resources/data-representation/enums).

---

### Enums {#enums}

*Learn how Enums can enhance the management of application states, product types, and process statuses by providing a robust method to handle predefined sets of values.*

**Source:** https://docs.flutterflow.io/resources/data-representation/enums

In FlutterFlow, Enums (enumerations) provide a method for defining a set of named constants. They are typically used to represent a group of related values in a more readable and safe manner.

They prevent invalid values from being assigned. For example, if you have an enum for days of the week, you can't mistakenly assign a non-existent day. In contrast, with strings or numbers, you might accidentally use an invalid or misspelled value like "Sundey" or "Sinday".

![enums](https://docs.flutterflow.io/assets/images/enums-fi-828b0b73ef99ab7ea726edd7172c6ca4.avif)

Here are some real-world examples where using Enums is beneficial:

1. **Application States**: A media player might use enums to keep track of playback states (e.g., playing, paused, stopped).
2. **Product Types, Sizes, or Categories**: A clothing store app might use enums to categorize clothing sizes (small, medium, large).
3. **Order or Process Status**: For tracking the status of orders, processes, or tasks (pending, inProgress, completed, canceled).

#### Create and use Enums

1. You can create Enums from the left side navigation menu and add values to it.

[Sharing a Project with a User](https://demo.arcade.software/U6crZTuELtgYinr4ZxQp?embed\&show_copy_link=true)

2. Access the Enum values by navigating to the **Set from Variable** menu, then selecting **Enums > \[your enum name] > Values**.

![enums.avif](https://docs.flutterflow.io/assets/images/enums-6f100f8b0496e611ff233cae9317751d.avif)

Naming Convention

When naming enums, always use **UpperCamelCase**, and for enum values, use **lowerCamelCase**, as recommended by the Dart Style Guide. To learn more, refer to the guide on **[Naming Variables & Functions](https://docs.flutterflow.io/resources/style-guide)**.

---

### Global Properties {#global-properties}

*Discover the role of Global Properties in FlutterFlow, which provide universal access across all pages of your app to facilitate common tasks and enhance functionality.*

**Source:** https://docs.flutterflow.io/resources/data-representation/global-properties

Global properties are **built-in variable**s in FlutterFlow that you can use across all pages of your app. These properties are predefined by FlutterFlow, meaning you cannot create or modify them yourself. They are designed to help you perform common tasks efficiently, no matter what type of app you’re developing.

For example, global properties can be used to redirect users to another page if they are not logged in or to enable specific functionality based on the platform your app is running on.

You can access these properties through the **Set from Variable** menu **> Global Properties**.

![global-properties.avif](https://docs.flutterflow.io/assets/images/global-properties-334541daf62a438eecee710a65a556db.avif)

> **Caution:** Global properties are built-in variables exposed by FlutterFlow. You can't create one by yourself.

#### List of Global Properties

A list of all the available global properties is as follows:

* **Is User Logged In:** Indicates whether a user is currently logged into the app. Useful for providing exclusive features to registered users or adjusting UI elements based on login status. This property is only accessible if you have enabled authentication of any type.

* **Current Time**: Fetches the current date and time. Explore [custom formatting](https://docs.flutterflow.io/resources/data-representation/global-properties#current-time) options to tailor the DateTime display to your needs.

* **Current Device Location:** Returns the user's current location, ideal for updating their position on Google Maps or storing it in a backend database. [Check out examples](https://docs.flutterflow.io/resources/data-representation/global-properties#current-device-location) on how to retrieve and save the current device location.

* **Link To Current Page:** Provides the [Deep Link](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#deep-link) of the current page.

* **Current Route Path**: Provides the route name of the currently active or visible page in your app. This property is especially helpful in scenarios where you want to adjust or block specific actions if the active page isn't the one you expect. For example, if you launch the app through a push notification, the home page might still run in the background, even if the notification directs you to a different page. Using this property, you can prevent unnecessary action triggers, such as On Page Load from the home page. See details on avoiding [this issue](https://github.com/FlutterFlow/flutterflow-issues/issues/2765#issuecomment-2598915946).

* **Current Route Stack:** Returns a list of route names representing every active page in your app’s navigation stack. It’s helpful for understanding how many pages deep the user is and what sequence of pages they’ve visited. You may need this data to manage custom back navigation, breadcrumb displays, or logging analytics. For instance, in an e-commerce app, you could examine the route stack to see if the user arrived at the checkout page from a specific page and tailor your promotional messages or apply discount accordingly.

* **Fraction of Screen Width:** Determines the proportional width of the device's screen.

* **Fraction of Screen Height:** Determines the proportional height of the device's screen.

* **Screen Width:** Provides the total width of the current device's screen in pixels.

* **Screen Height:** Provides the total height of the current device's screen in pixels.

* **Is Android:** Determines if the user is accessing the app on an Android device. See [example](https://docs.flutterflow.io/resources/data-representation/global-properties#is-androidiosweb).

* **Is iOS:** Determines if the user is accessing the app on an iOS device. See [example](https://docs.flutterflow.io/resources/data-representation/global-properties#is-androidiosweb).

* **Is Web:** Determines if the user is accessing the app through a web browser. See [example](https://docs.flutterflow.io/resources/data-representation/global-properties#is-androidiosweb).

* **Is Debug Mode:** Indicates if the app is currently running in debug mode, useful for displaying features or performing actions only during debugging.

* **Is Dark Mode:** Checks if the app's current theme mode is set to dark.

* **Is Light Mode:** Checks if the app's current theme mode is set to light.

* **Is On-Screen Keyboard Visible:** Checks if the on-screen or soft keyboard is visible. This is helpful in making UI adjustments if keyboard is visible on screen. See a [quick example](https://docs.flutterflow.io/resources/data-representation/global-properties#is-on-screen-keyboard-visible).

* **Current Environment**: Returns the current [development environment](https://docs.flutterflow.io/testing/dev-environments) value.

Generated Code

Learn more about the [**Generated Code**](https://docs.flutterflow.io/generated-code/state-management#global-state) behind Global Properties.

##### Current Time

The **Current Time** property allows you to retrieve the current date and time. This option is available when the Source is set to Global Properties.

You can use this property to display the current date and time on the screen or pass it to a FlutterFlow or custom widget for further processing.

###### Custom formatting

Sometimes, you might need to display dates and times in a format that we don't support. This is where the custom date and time formatting comes into play. *Custom Format* enables you to represent date and time data in a multitude of ways.

For example, you can enter the text like '*yyyy/MM/dd || kk :mm*', and the date time will be displayed as '2023/07/25 || 10:30'.

In the above example, '*yyyy/MM/dd || kk :mm* is the custom format. Here's what it stands for:

* `yyyy` represents a four-digit year, like "2023".
* `MM` is a two-digit month, such as "07" for July.
* `dd` indicates a two-digit day, for instance, "25".
* `kk` is for a two-digit hour in 24-hour format, like "10".
* `mm` stands for a two-digit minute, such as "30".

Here are some more format specifiers that you can use the build the custom format:

* `d`: Day of the month. E.g., "2" for February 2nd.
* `E`: Abbreviated weekday. E.g., "Mon" for Monday.
* `EEEE`: Full weekday. E.g., "Monday".
* `LLL`: Abbreviated standalone month. E.g., "Feb".
* `LLLL`: Full standalone month. E.g., "February".
* `M`: Month of year. E.g., "2" for February.
* `Md`: Month and day. E.g., "2/2".
* `MEd`: Abbreviated weekday, month, and day. E.g., "Mon, 2/2".
* `MMM`: Abbreviated month. E.g., "Feb".
* `MMMd`: Abbreviated month and day. E.g., "Feb 2".
* `MMMEd`: Abbreviated weekday, month, and day. E.g., "Mon, Feb 2".
* `MMMM`: Full month. E.g., "February".
* `MMMMd`: Full month and day. E.g., "February 2".
* `MMMMEEEEd`: Full month, weekday, day. E.g., "Monday, February 2".
* `QQQ`: Abbreviated quarter. E.g., "Q1".
* `QQQQ`: Full quarter. E.g., "1st quarter".
* `y`: Year. E.g., "2023".
* `yM`: Year and month. E.g., "2023/2".
* `yMd`: Year, month, day. E.g., "2023/2/2".
* `yMEd`: Weekday, year, month, day. E.g., "Mon, 2023/2/2".
* `yMMM`: Abbreviated month and year. E.g., "Feb 2023".
* `yMMMd`: Abbreviated month, day, year. E.g., "Feb 2, 2023".
* `yMMMEd`: Weekday, month, day, year. E.g., "Mon, Feb 2, 2023".
* `yMMMM`: Full month and year. E.g., "February 2023".
* `yMMMMd`: Full month, day, year. E.g., "February 2, 2023".
* `yMMMMEEEEd`: Weekday, full month, day, year. E.g., "Monday, February 2, 2023".
* `yQQQ`: Abbreviated quarter, year. E.g., "Q1 2023".
* `yQQQQ`: Full quarter, year. E.g., "1st quarter 2023".
* `H`: Hour in day (24-hour). E.g., "15" for 3 PM.
* `Hm`: Hour, minute (24-hour). E.g., "15:30".
* `Hms`: Hour, minute, second (24-hour). E.g., "15:30:45".
* `j`: Hour in day (12-hour). E.g., "3 PM".
* `jm`: Hour, minute (12-hour). E.g., "3:30 PM".
* `jms`: Hour, minute, second (12-hour). E.g., "3:30:45 PM".
* `m`: Minute in hour. E.g., "30".
* `ms`: Minute, second. E.g., "30:45".
* `s`: Second in minute. E.g., "45".
* `G`: Era designator. E.g., "AD" in "AD 2023".
* `L`: Standalone month. E.g., "7" for July.
* `c`: Standalone day. E.g., "2" for Tuesday.
* `h`: Hour in AM/PM (1\~12). E.g., "3" for 3 AM.
* `H`: Hour in day (0\~23). E.g., "15" for 3 PM.
* `S`: Fractional second. E.g., "123" for 123 milliseconds.
* `D`: Day in year. E.g., "50" for the 50th day of the year.
* `a`: AM/PM marker. E.g., "AM" or "PM".
* `k`: Hour in day (1\~24). E.g., "24" for midnight.
* `K`: Hour in AM/PM (0\~11). E.g., "0" for 12 AM.
* `Q`: Quarter. E.g., "4" for the fourth quarter.

> **Info:** For more detailed information, please refer to the [DateFormat class documentation](https://pub.dev/documentation/intl/latest/intl/DateFormat-class.html).

![img.png](https://docs.flutterflow.io/assets/images/img-9946195dba2959d39385e9e2bdab25fb.png)

##### Current Device Location

This property is used to get the current device location (aka geolocation). You can access this when the **Source** is set to **Global Properties**.

You can use this property to get the user's current location to update on Google Maps or store it in the backend database.

> **Warning:** At present, testing this property isn't possible in Test mode, but you can use the Run mode for this purpose. To run it on Android, iOS or desktop platforms, use [Local Run](https://docs.flutterflow.io/testing/local-run).

###### Get Current Device Location: Example

Let's see an example of getting the current device location and passing it to a widget (that supports accepting LatLong, for example, Google Maps).

Here is an example of how you can retrieve the current device location:

1. Select the **widget** (e.g., GoogleMap) from the widget tree or canvas area.
2. Move to the properties panel, find the **Initial Location** property, and click on **Set from Variable**.
3. Set the **Source** to **Global Properties**.
4. Set the **Available Options** to the **Current Device Location**.
5. Click **Confirm**.

###### Save the Current Device Location: Example

Here's how you can save the user's current location (Geolocation) in the Firestore document.

1. Create a **LatLng** field in your Firestore Schema.

2) After this, you need to set this field from a variable source and select **Current Device Location** from the **Global Properties**.

##### Is Android/iOS/Web

Use these properties when you want to tailor the user experience for specific platforms. These properties determine whether the user is accessing the app on Android, iOS, or the Web. Knowing the user's platform is essential for customizing functionality to suit each environment. For instance, certain custom widgets or actions might be exclusive to Android.

These properties allow you to implement platform-specific features and ensure your app behaves optimally across different devices. Some examples:

* **Is Android**: Enable a custom push notification feature that only works on Android devices. By checking if the platform is Android, you can conditionally display a setup screen for this feature.

* **Is iOS**: Optimize custom animations or gestures specifically for iOS. By detecting if the user is on an iOS device, you can enable these iOS-specific interactions while providing alternatives for other platforms.

* **Is Web**: Implement a file upload feature with a drag-and-drop interface optimized for desktop environments. By checking if the platform is Web, you can provide an enhanced file handling experience that suits web users.

##### Is On Screen Keyboard Visible

This property helps check if the on-screen or soft keyboard is visible on screen. You can access this when the Source is set to Global Properties.

###### Hiding bottom navigation bar when a keyboard is visible: Example

Consider an app where users can input dog details, and a custom bottom navigation bar is present. When users enter dog details, the on-screen keyboard appears, causing the bottom navigation bar to appear over the keyboard. To optimize screen space and improve the user experience, you might want to hide the bottom navigation bar in such instances.

Here's how it looks:

To build such behavior, you can add [Conditional Visibility](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#conditional) on the bottom navigation. While adding, use the "Is On-Screen Keyboard Visible" that will hide the bottom navigation bar whenever the keyboard is displayed. Using "Is On-Screen Keyboard Visible" to hide bottom navigation

---

### Variable {#variable}

*Variables*

**Source:** https://docs.flutterflow.io/resources/data-representation/variables

Variables in FlutterFlow let you store and manage dynamic data, which is essential for creating interactive and responsive applications. By using variables, you can capture user inputs, track states, and manipulate data across different parts of your app.

![variable](https://docs.flutterflow.io/assets/images/variable-c8dba55586bec76e5d8d02e8a5769538.avif)

In this section, we'll dive into the different types of variables available in FlutterFlow, including:

* **Local Variables:** Variables that are confined to a specific widget or page, used for handling data within a localized context. For example, Page State variables or Component State variables are scoped to the entity they were created in.
* **Global Variables:** Variables that can be accessed and modified throughout the entire app, allowing for consistent data management across pages. For example, App State variables can be accessed from anywhere in the app.

What are scopes?

The scope of a variable is determined by where it is created. For instance, if it's created at the app level, it can be accessed throughout the app. However, a variable created at the page level can only be accessed on that page.

#### Creating Variables

When creating variables in FlutterFlow, there are a few important considerations regarding their name, data type, nullability, and initial values. The specific *process* for creating variables differs depending on whether you are working with App State, Page State, or Component State variables, and you can find detailed instructions linked below.

##### Naming Variable

Start by giving your variable a meaningful and descriptive name that reflects its purpose. This name will be used throughout your app to reference the variable, so it's important to keep it clear and consistent with your naming conventions.

Recommended naming convention

We recommend the `lowerCamelCase` naming convention for variables. Learn more about the **[recommended naming conventions](https://docs.flutterflow.io/resources/style-guide)** used in FlutterFlow and Flutter projects.

##### Assigning a Data Type to a Variable

Next, you need to select the appropriate data type for your variable. FlutterFlow offers several data types, such as **Text, Integer, Boolean,** or **String**. Refer to the **[Data Types guide](https://docs.flutterflow.io/resources/data-representation/data-types)** to learn more about the available data types.

Choosing the correct data type is crucial, as it determines how the variable can be used and what kind of data it can store.

##### Is List Property

Enable the **Is List** toggle to indicate that this field should be of the **list** type.

Example

If the data type selected is `String` and the `Is List` toggle is enabled, FlutterFlow will create a **list of String variables**. This list can hold multiple string values, such as a list of city names.

##### Nullable & Initial Value

When creating variables in FlutterFlow, you have the option to make them **nullable** or **non-nullable**. This setting is crucial because it determines whether the variable can hold a null value (i.e., no value). Alongside this, you can also define an initial value for your variable, which ensures that it starts with a specific value as soon as it’s created.

![variables-null-initial-value.png](https://docs.flutterflow.io/assets/images/variables-null-initial-value-3b9551914e84a3be7ba26a84e5f0a070.png)

* **Nullable:** This option determines if a variable can hold a null value, meaning it can exist without any data. If the Nullable option is enabled, the variable can start as null and only receive a value when needed. If disabled, the variable must always have a value, which means you’ll need to provide an initial value when it’s created.

* **Initial Value:** If a variable is non-nullable (i.e., cannot be null), you are required to provide an initial value to ensure it always contains data. For nullable variables, setting an initial value is optional, allowing them to remain empty until a value is assigned.

What is a null value?

A null value represents the **absence of a value**. In FlutterFlow, allowing a variable to be null can be beneficial in scenarios such as:

* **User Input:** Before a user enters data, a variable can start as null and only hold a value once the user provides input.
* **Conditional Logic:** In cases where certain data might not always be applicable (e.g., an optional user setting), a null value allows you to handle the absence of data more flexibly.
* **Loading States:** When fetching data from an API, variables can be null until the data is loaded, allowing you to differentiate between "loading" and "loaded" states easily.

##### How to create variables?

For step-by-step guides on how to create App State, Page State, and Component State variables, please refer to the following links:

* [Creating App State Variables](https://docs.flutterflow.io/resources/data-representation/app-state)
* [Creating Page State Variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#page-state)
* [Creating Component State Variables](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#component-state)

#### Set Variable

The **Set from Variable** or **Set Variable** menu in FlutterFlow is a powerful feature that allows you to dynamically control the content or behavior of your widgets using **data** stored in variables. When you select a variable from this menu, you're instructing FlutterFlow to use the value of that variable to populate or modify the widget's properties, such as text, visibility, or styling.

This menu provides a variety of variable **sources**, including data that's specific to the page or component, global properties that apply across the entire app, constants, and more. By choosing the appropriate variable, you can make your app more interactive and responsive to user input, data changes, or other conditions.

![set-variable-menu3.png](https://docs.flutterflow.io/assets/images/set-variable-menu3-36c77114a93aedc24f17013a0a1293e7.png)

#### Manipulating Variables

When setting variables via the **Set Variable** menu, you have the ability to manipulate or transform the data before applying it to a widget or another variable. This manipulation allows you to tailor the data to fit specific needs or contexts, enhancing the flexibility and functionality of your app.

For instance, you can:

* **[Concatenate or Combine Strings:](https://docs.flutterflow.io/resources/functions/utility#combine-text)** Combine multiple text values into a single string. To learn how to manipulate strings before setting variables, see the [Utility Functions](https://docs.flutterflow.io/resources/functions/utility#combine-text) guide.
* **[Filter or Sort Lists](https://docs.flutterflow.io/resources/data-representation/variables#list-options):** Organize or refine data in lists to display only what’s relevant or in a specific order.
* [**Convert DateTime to UNIX:**](https://docs.flutterflow.io/resources/data-representation/global-properties#current-time) Change a DateTime object into a UNIX timestamp for compatibility or calculation purposes.
* [**Apply Conditional Logic:**](https://docs.flutterflow.io/resources/functions/conditional-logic) Use If/Then/Else statements to set different values based on specific conditions.

These manipulations enable you to create more dynamic and responsive user interfaces by ensuring that the data presented or used in your app is always in the most appropriate form.

##### List Options

While working with a list, you may need to extract specific data based on specific criteria. The List options provide a range of functionalities for efficient data extraction from these lists. Here's what it includes:

###### Map List Items

The option **Map List Items** allows you to prepare a list of specific fields from data types such as Documents, [Custom Data Types](https://docs.flutterflow.io/resources/data-representation/custom-data-types), and JSON. For instance, if you have a list of Firebase Documents containing fields like name, age, and position, you can specifically generate a list consisting only of names. This option allows you to create tailored lists from complex data structures.

Here's an example of preparing a list of only cat names from Firebase documents (that contain other fields like name, age, and breed) and displaying them on dropdown.

###### Filter List Items

The **Filter List Items** option allows you to create a list of items based on specific criteria, generating a sublist of items that match. For example, you might want to create a list of users over a certain age from a larger user database or perhaps compile a list of products within a specific price range from an extensive inventory.

###### First Few Items

The **First Few Items** option extracts the initial elements of the list up to a specified number.

![first-few-items.png](https://docs.flutterflow.io/assets/images/first-few-items-df06267d42230386f8b6313cd234832a.png)

###### Sort List Items

If your list contains "native data types" (like numbers or strings), we can automatically sort these elements. Native data types have a "natural ordering." For example, numbers can be sorted numerically (1, 2, 3, ...), and strings can be sorted alphabetically ("apple", "banana", "cherry", ...). For such a list, set the **Sort Key** to the item in the element.

Here's an example of displaying random names in alphabetical order:

Reversing a list

To reverse sort a list, first sort it using the sort option, then apply the listView's [reverse option](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#advanced-functionalities) for descending order.

For lists with [Custom Data Types](https://docs.flutterflow.io/resources/data-representation/custom-data-types), you need to tell which field to use for sorting by specifying it in the **Sort Key**, and this field should be a standard data type that has a clear, natural way to be ordered.

Here's how you can display a list of items (of the custom data type 'Product') in order, sorted by their price.

###### Unique List Items

This option helps you create a list with unique items, such as extracting distinct product categories or unique customer names from a larger dataset.

Here's an example of displaying a list of unique cat breeds:

To get a list of unique items from a list of custom data type, first map the list of items to the field from which you want to extract unique items. For example, if you have a list of a custom data type named 'Products,' map this list to a list containing all product names. Then, derive the unique list items from this mapped list.

###### Number of Items

Choose the **Number of Items** option if you want to get the count of the total elements in the list.

###### Item at Index

The **Item at Index** option allows you to access a specific item by its position in the list. For instance, you could retrieve the third item from a list of customer names, or select the fifth product in a catalog list. This is especially useful in scenarios where the order of items carries significance, such as fetching the latest entry in a time-ordered log, or simply when you need to pinpoint a specific item without filtering through the entire list.

###### Is Set and Not Empty

To determine, if any value is present in the list or if the list is not empty, choose the **Is Set And Not Empty** option. For example, it can be used to check if a search query returned any results or to verify that a data collection process has successfully captured entries.

#### Updating Variable Values

In FlutterFlow, you can update the values of variables through **[actions](https://docs.flutterflow.io/resources/functions/action-flow-editor)**. For example, when a button is clicked or when a form field is modified, you can trigger an action that updates a variable with a new value.

Refer to the following guides for detailed instructions on updating and using these variables:

* [App State Variables](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action)
* [Page State Variables](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle#update-page-state-action)
* [Component State Variables](https://docs.flutterflow.io/resources/ui/components/component-lifecycle#update-component-state-action)

---

### Forms Overview {#forms-overview}

*Learn how to work with Forms in FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms

Forms are a fundamental part of many applications, serving as the primary method for users to input and submit data. Whether you're building a simple contact form or a complex multi-step survey, FlutterFlow provides a comprehensive set of tools to create, validate, and manage forms effectively.

> **Tip:** In this section, you'll learn how to add form widgets such as [**TextField**](https://docs.flutterflow.io/resources/forms/textfield), [**Dropdown**](https://docs.flutterflow.io/resources/forms/dropdown), [**RadioButton**](https://docs.flutterflow.io/resources/forms/radiobutton), [**Checkbox Widgets**](https://docs.flutterflow.io/resources/forms/checkbox) and add [**Validations**](https://docs.flutterflow.io/resources/forms/form-validation) and [**set**](https://docs.flutterflow.io/resources/forms/set-form-field)/[**reset**](https://docs.flutterflow.io/resources/forms/reset-form-field) actions on these widgets.

---

### Checkbox {#checkbox}

*Learn how to add Checkbox, CheckboxGroup, and CheckboxListTile widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/checkbox

In FlutterFlow, a checkbox is a versatile input widget used to capture binary choices from users, such as true/false or yes/no options. It is ideal for situations where you need to present users with options that can be individually selected or deselected. FlutterFlow provides three primary variations of the checkbox widget: **Checkbox**, [**CheckboxListTile**](https://docs.flutterflow.io/resources/forms/checkbox#checkboxlisttile), and [**CheckboxGroup**](https://docs.flutterflow.io/resources/forms/checkbox#checkboxgroup). Each of these widgets offers distinct features and use cases, making it easy to tailor your app's interface to your specific needs.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Checkbox

The **Checkbox** widget is the simplest form of a checkbox. It consists of a small square that can be either checked or unchecked. This widget is typically used for individual boolean options. You can customize the appearance and behavior of the checkbox, such as its size, color, and whether it starts as checked or unchecked.

##### Adding Checkbox

Let's see how to add a checkbox widget and build an example that shows its value on a Text widget. Here's how it looks:

Here is a simple way to do it:

1. First, click on the **+ Add Widget**, drag the **Checkbox** widget from the **Base Elements** tab, or add it directly from the widget tree.
2. Below the Checkbox, add a [**Text**](https://docs.flutterflow.io/resources/ui/widgets/text) widget, move to the properties panel, click on **Set from Variable,** and choose the **Widget State > checkboxValue** (i.e., name of your checkbox).

##### Setting Initial Value

You might want to show the checkbox with a default value, either check or uncheck. For example, showing the checked checkbox for travel insurance.

To set the initial value:

1. Select the **Checkbox** widget, move to the properties panel, and see the **Checkbox Initial Value** property.
2. Use the checkbox to set this value manually, or click **Set from Variable** to set it based on the dynamic value. If you choose *Set from Variable*, ensure you pass the boolean value from the source (e.g., API response, Firestore document field).

##### Saving Checkbox Value

You may want to immediately save the checkbox’s value when it is checked or unchecked. To do this, [add an action using the trigger](https://docs.flutterflow.io/resources/forms/form-triggers#on-toggled-on--on-toggled-off) that responds to changes in the widget’s selection.

##### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

###### Changing color

To change the checkbox colors:

1. Select the **Checkbox** widget, move to the properties panel, and scroll down to the **Checkbox Properties** section.
2. To [change the color](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#change-color) of the checkbox when it is selected and unselected, use the **Checked Color** and **Unchecked Color** properties, respectively.
3. To [change the color](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#change-color) of the check icon, use the **Check Color** property.

###### Add rounded corners

To change the rounded corner for this widget:

1. Select the **Checkbox** widget, move to the properties panel, and scroll down to the **Checkbox Properties** section.
2. Find the **Border Radius** property and enter the values for TL(Top Left), TR(Top Right), BL(Bottom Left), and BR(Bottom Right). Use the Lock button to change all values at the same time. Unlocking will allow you to adjust each value separately.

###### Make it circular

If you want to make the checkbox circular in shape, select the **Checkbox** widget, move to the properties panel, find the **Circular Check** property and enable it.

![Circular checkbox](https://docs.flutterflow.io/assets/images/make-checkbox-circular-e535ab64fac473cf839c591597ac18c9.avif)

###### Disable Checkbox

You may need to disable a checkbox if certain conditions aren't met. For instance, users should only be able to use the 'Same as Shipping Address' checkbox when a shipping address is provided.

To disable a checkbox, move to the **Properties Panel** **>** turn on the **Checkbox Disable Options >** click **Unset,** and set the [**Condition**](https://docs.flutterflow.io/resources/functions/conditional-logic). Once set, you could also customize the disabled state colors using the *Disabled Check Color* property.

#### CheckboxListTile

The **CheckboxListTile** widget combines the functionality of a checkbox with a [ListTile](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listtile-widget), providing a more comprehensive option for displaying checkboxes alongside additional information. Unlike the Checkbox this widget includes a title, and an optional subtitle, all within a single, cohesive element.

CheckboxListTile is ideal for use cases where you want to provide more context or descriptive text alongside the checkbox, such as in a settings menu or a form with detailed options.

#### CheckboxGroup

The **CheckboxGroup** widget allows you to present a group of checkboxes as a single entity. This is particularly useful when you want users to select multiple options from a list. Each checkbox within the group can be checked or unchecked independently of the others.

##### Adding CheckboxGroup

Here's an example of how you can use the CheckboxGroup widget in your project:

1. First, add the **CheckboxGroup** widget from the **Form Elements** tab or add it directly from the widget tree.

2. By default, the CheckboxGroup widget adds a single option named **Option 1**. To change the name, move to the properties panel (on the right side of your screen), and scroll down to the **Define Options** section. Find the **Option 1** property and change the **name**.

3. To add more options, move to the properties panel, and scroll down to the **Define Options** section. 1. Click on the **Add Option** text.
   2. Enter the name in **Option 2 Text**.

4. To remove the option, click on the cancel icon displayed in the **Option name** property.

5. Click on the **Set from Variable** to show the options from a variable such as app state variable, API response variable, or Firestore Document.

##### Trigger Action on Change

See how to [trigger an action when a selection changes](https://docs.flutterflow.io/resources/forms/form-triggers#on-selected) on this widget.

##### Setting Initial Selection

Sometimes you might want to display the CheckboxGroup with some options already selected. For example, selecting the topping options that are already served with Pizza itself. You can do so by setting the initial selection for the CheckboxGroup.

To set initial selection manually:

1. Select the **CheckboxGroup** from the widget tree or the canvas area.
2. Move to the properties panel (on the right side of your screen) and scroll down to the **Initially Selected** section.
3. Click on the **Add Selected** and enter the option name that you would like to display as selected. **Note**: Make sure you enter the correct name and it matches with the option name added inside the define options section.
4. Similarly, you can display the other option(s) as selected.

##### Clear/Select all items \[Action]

You might want to allow users to clear or select all items in one go. You can do so by adding the following action.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Clear All/Select All** (under *Widget/UI Interactions*) action.
4. **Choose Multiselect Widget** name from the dropdown.
5. Finally, set the **Action Type** to **Clear All** or **Select All**.

##### Customization

You can use the Properties Panel to customize the appearance of your widget.

###### Set padding around the checkbox

To create empty space around the checkbox:

1. Select the **CheckboxGroup** from the widget tree or the canvas area.
2. Move to the properties panel and find the **Item Padding** property.
3. Set the padding for the L(Left), T(Top), R(Right), and B(Bottom) sides. Use the Lock button to change all values at the same time. Unlocking will allow you to modify each value separately.

###### Changing checkbox color

To change the checkbox color:

1. Select the **CheckboxGroup** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Checkbox Style** section.
3. To change the active color (i.e. color when the checkbox is selected), find the **Active Color** property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking the **Palette** and **Simple** button.
4. the Similarly you can change the check color (i.e color of the done/tickmark icon inside the checkbox).

###### Customizing checkbox border

To customize the checkbox border:

1. Select the **CheckboxGroup** from the widget tree or the canvas area.
2. Move to the properties panel and scroll down to the **Checkbox Style** section.
3. To change the checkbox border color, find the **Check Border Color** property, click on the box next to the already selected color, select the color, and then click **Use Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking the **Palette** and **Simple** button.
4. To adjust the border corner, find the **Border Radius** property and enter the values in the TL (Top left), TR (top right), BL (bottom left), and BR (bottom right) boxes. Use the Lock button to change all values at the same time. Unlocking will allow you to modify each value separately.

---

### ChoiceChips {#choicechips}

*Learn how to add ChoiceChips in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/choice-chips

The ChoiceChips widget allows users to select a single option from a group of chips. Each chip is presented with an icon and accompanying text, making it easy to represent various choices.

You could use this widget to implement a filter feature in an e-commerce app to let users select different product attributes like size, color, or price range.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding ChoiceChips widget

To add the ChoiceChips widget to your app:

1. Add the **ChoiceChips** widget from the **Form Elements** tab.

2. By default, this widget adds a single option named **Option 1**. To change the name, move to the Properties Panel, and scroll down to the **Define Options** section. Find the **Option 1** property and change the **name** and **icon**.

3. To add more options, click on the **Add Option** text and set the name and icon for new options.

4. To set any chip as selected by default, find the **Initial Option** property and enter the chip name. 1. To set this value dynamically, open the **Set from Variable** menu and set the variable.
   2. When [multiselect](https://docs.flutterflow.io/resources/forms/choice-chips#allow-multiselect) is enabled, you can also set the list of options to pre-select.

##### Trigger Action on Change

See how to [trigger an action when a selection changes](https://docs.flutterflow.io/resources/forms/form-triggers#on-selected) on this widget.

#### Select or Clear All Choices \[Action]

Users may need to swiftly deselect all chips or choose all available choice chips at once. You can do so by adding the **Clear All/Select All** action.

> **Info:** Before you add this action, ensure you [**allow multiselect**](https://docs.flutterflow.io/resources/forms/choice-chips#allow-multiselect) on this widget.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Allow Multiselect

You might want to allow users to select multiple choices to filter the result.

To allow multiselect, select the **ChoiceChips** widget, move to the properties panel, find the **Allow Multiselect** property and enable it.

##### Disable ChoiceChips

Sometimes, you may want to present the choices in a read-only mode, preventing users from making any changes.

To do so, move to the **Properties Panel** **>** turn on **Disable >** click **Unset,** and set the [**Conditions**](https://docs.flutterflow.io/resources/functions/conditional-logic). This can be the [**Single Condition**](https://docs.flutterflow.io/resources/functions/conditional-logic#single-condition) or [**Combine Conditions**](https://docs.flutterflow.io/resources/functions/conditional-logic#multiple-conditions-andor) based on your requirement. **Note:** The ChoiceChips widget will be disabled only when condition(s) is true.

##### Adding Space between Chips

To add a space between the chips, you can use the **Chip Spacing** ad **Row Spacing** property.

* **Chip Spacing**: This adds horizontal gaps between individual chips.
* **Row Spacing**: This adds vertical gaps between the chips in a row.

##### Align Chips

When you have chips in multiple rows, you can align them using the **Alignment** property. This is similar to setting main axis alignment for the Row widget.

##### Customizing Selected and Unselected Chip Style

Various properties under the **Selected Chip Style** and **Unselected Chip Style** section allow you to customize chips to match your design. Here's how you do it:

1. To change the background color, use the **Color** property.
2. To change the icon's color and size, use the **Icon Color** and **Icon Size** property.
3. To add a shadow or to create a sense of depth for the chip, you can use the **Elevation** property.
4. To customize the border, use the **Border Color**, **Border Width** (thickness), and **Border Radius** (rounded corner) properties.
5. To create some space around the label, use the **Label Padding** property.
6. To change the label text styling, use the **Selected Text Style** property.

7) Similarly, you can customize the properties under the **Unselected Chip Style**.

![Customizing unselected chip style](https://docs.flutterflow.io/assets/images/customize-unselected-choice-76daa2c539e8b24886b48619effa7c27.png)

---

### Dropdown {#dropdown}

*Learn how to add Dropdown widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/dropdown

The DropDown widget enables users to choose from a list of options. It requires a set of items to display and an initial value to indicate the current selection. When a user selects an item from the dropdown list, the value is updated to reflect the selected item.

You can use this widget in any situation where you want users to select from a set of options, such as selecting a country, choosing a language, or picking a color.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding DropDown widget

Let's see how to add a *DropDown* widget and build an example that shows the selected value on a Text widget. Here's how it looks:

1. Add the **DropDown** widget, move to the **Properties Panel > Define Options >** click **Add Options** to add items.
2. To display the default value, move to the **Initial Configuration** section and enter the value. Ensure it matches one of the options added in the previous step.
3. The selected dropdown value can be accessed via *Widget State > DropDown*. To display it on the *Text* widget, add a [**Text**](https://docs.flutterflow.io/resources/ui/widgets/text) widget, move to the properties panel, click on **Set from Variable** and choose the **Widget State > DropDown** (i.e., name of your dropdown).

##### Setting Initial Value

Setting a default or initial value for the DropDown is a common requirement for many apps. It can provide a better user experience by pre-selecting the most likely option.

To set an initial value:

1. Select the **DropDown** widget > move to the **Properties Panel** > **Initial Configuration**.

2. In **Initial Option Value**, enter the option name that you want to set as default.

3. To set this value dynamically, open the **Set from Variable** menu and select the variable. 1. For example, to set this value from Firebase, ensure you have access to Firebase document that contains the field you want to set.
   2. Open the **Set from Variable** menu > select **\[collection\_name] Document** > select the **field**.

4. If you don't set the initial value, the **Hint Text** will be displayed.

##### Saving DropDown Value on Selection Change

You might want to save the dropdown value as soon as the selection changes. This approach is useful when you want to ensure that the user's selection is immediately saved without having to wait for them to submit the form. By doing so, you can provide a better user experience and reduce the risk of data loss in case of any interruption.

You can do so by adding an action such as [update app state](https://docs.flutterflow.io/resources/data-representation/app-state#update-app-state-action), [update Firestore record](https://docs.flutterflow.io/integrations/database/cloud-firestore/firestore-actions#update-document-action) that [triggers when a selection changes](https://docs.flutterflow.io/resources/forms/form-triggers#on-selected) on this widget.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Showing Option Label

The dropdown widget allows you to show a label than the actual option value. By adding the option label, you can have a simple/short name or abbreviation (which is quite easy to compare and process in the backend) instead of a tricky name (e.g., Falkland Islands (the) \[Malvinas]).

For example, In a Country dropdown, you could have different *Option* *Values* to store in the backend and *Option Labels* to show in the dropdown list. Just like below:

| Option Values | Option Labels                      |
| ------------- | ---------------------------------- |
| US            | United States                      |
| IN            | India                              |
| FK            | Falkland Islands (the) \[Malvinas] |

To show option label:

1. Select the **DropDown** widget, move to the properties panel, and turn on the **Add Option Labels** toggle.
2. Enter the value in the **Define Option Values** and **Define Options Labels**. Click **Add Option** (below the *Define Option Values*) to add more values and labels.
3. You must also set the **Data Type** for the values. For example, if the values you are going to store are in numbers like 1,2,3, set it to *Integer*.

##### Searchable Dropdown

The *DropDown* widget is a good choice when you have a small number of options, up to around 10-20; however, If you have more options than that, consider using a searchable dropdown.

A searchable dropdown allows users to search and filter options by typing in a search bar. As the user types, the dropdown list is dynamically filtered to only show matching options. This is especially useful when dealing with long lists of options and can improve the user experience by reducing the time it takes to find and select an option.

To make the dropdown widget a searchable one:

1. Select the **DropDown** widget, move to the **Properties Panel > DropDown Search >** enable **Is Searchable** option.
2. You can also customize the **Search Hint Text** property.

![Making dropdown searchable](https://docs.flutterflow.io/assets/images/making-dd-searchable-f1de9e328ba77af1b6c50fbb028e23b0.png)

##### Disable Dropdown

You might need to disable a dropdown when certain conditions are not yet met or need to be fulfilled. For example, when the dropdown options are dependent on other fields, and those fields are not filled yet.

To disable the dropdown:

1. Select the **DropDown** widget, move to the **Properties Panel > DropDown Search >** enable **Disable Dropdown** option.
2. Click on **Unset** and select the source that returns the boolean value (i.e., True or False), such as boolean variable, [Conditions](https://docs.flutterflow.io/resources/functions/conditional-logic), [Inline Function](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions).

![Disabling dropdown](https://docs.flutterflow.io/assets/images/disabling-dropdown-05e5d82e8c412f1ae7cc909623b9e693.png)

##### Allow Multi Select

You might want to allow users to select multiple options from the dropdown list. For example, on an e-commerce app, users might want to filter products based on multiple attributes, such as t-shirts in both 'blue' and 'red' colors.

To allow multi-select, select the **Dropdown** widget, move to the properties panel, find the **Allow Multi Select** property, and enable it.

> **Info:** To clear the selection, you can use the [Reset Form Fields](https://docs.flutterflow.io/resources/forms/reset-form-field) action and choose the **Reset Dropdown Fields** option. Then, simply select the name of the dropdown widget you wish to reset.

##### Changing Dropdown Size

To change the height and width of the dropdown, select the **DropDown** widget, move to the **Properties Panel > DropDown Properties > enter the Width and Height value**.

##### Set Max Height

If needed, you can also control the dropdown height using the **Max Height** property.

##### Adding Margin

Margin adds a space between the DropDown's text and its border. To change the margin, select the **DropDown** widget, move to the **Properties Panel > DropDown Properties >** find the **Margin** property, and change the values.

##### Changing Background Color

To change the background color, move to the **Properties Panel > DropDown Style > set the Fill Color**.

![Changing background color](https://docs.flutterflow.io/assets/images/changing-background-color-2522beea0239fb73d5746b2a33cb77ac.png)

##### Changing Menu Elevation

Menu elevation adds a shadow to the dropdown, giving it a sense of depth and making it appear above the surface it is placed on.

To change the menu elevation (depth or Z-axis), move the **Properties Panel >** enter the **Menu** **Elevation** value.

> **Info:** The higher value draws the bigger size of the shadow.

##### Adding Border

See how to [add a border](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#adding-border).

##### Show/hide Underline

To show or hide the dropdown underline, move the **Properties Panel >** **DropDown Style** > use the **Hides Underline** toggle.

##### Fix Position

By default, the dropdown options are displayed over/above the dropdown button. To display beneath/below the button, move the **Properties Panel >** **DropDown Style** > switch on the **Fix Position** toggle.

![Fix position for dropdown options](https://docs.flutterflow.io/assets/images/fix-position-44942cedca06778938f5864d54a1a709.webp)

---

### Form Triggers {#form-triggers}

*Learn how to use Form Triggers in FlutterFlow to create dynamic, interactive user experiences by responding to user input on widgets like dropdowns, sliders, toggles, and text fields.*

**Source:** https://docs.flutterflow.io/resources/forms/form-triggers

**Form Triggers** in FlutterFlow allow you to respond dynamically to user input on widgets like dropdowns, sliders, toggles, and text fields. Whether it’s selecting an option, toggling a switch, or typing in a field, these triggers help you create interactive, responsive experiences by executing actions based on user interaction.

#### On Selected

The **On Selected** action trigger is used to perform actions when a user selects or changes a value from a widget that presents multiple options. This trigger is associated with form widgets where selection input is required, such as [Dropdown](https://docs.flutterflow.io/resources/forms/dropdown), [RadioButton](https://docs.flutterflow.io/resources/forms/radiobutton), [CheckboxGroup](https://docs.flutterflow.io/resources/forms/checkbox#checkboxgroup), [ChoiceChips](https://docs.flutterflow.io/resources/forms/choice-chips), and [Slider](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/slider).

Possible use cases

* **Dropdown – Shipping Method Selection:** User selects a shipping method from options like "Standard", "Express", or "Next Day". Action under the *On Selected* trigger sets the app state variable `shippingOption`, which updates pricing or estimated delivery time dynamically.
* **Slider – Show Volume Level in Snackbar:** User adjusts a Slider from 0 to 100. The *On Selected* trigger displays a Snackbar showing the current volume: Volume set to: \[sliderValue].
* **ChoiceChips – Filter Products by Category:** User taps a chip like "All", "Electronics", or "Clothing". The *On Selected* trigger might set an app state variable (e.g., `selectedCategory`) and update the product list to match the chosen category.

To use the **On Selected** trigger:

1. Start by selecting a supported widget, such as a Dropdown.
2. Open the **Actions** tab in the properties panel and click **+ Add Action**.
3. You will notice that the **Type of Action** (aka callback) is already set to **On Selected**. That means actions added under this will be called whenever the selection changes.
4. Finally, define the actions you want to perform when the user makes a selection, such as setting a variable, navigating to another page, or displaying a message.

![on-selected](https://docs.flutterflow.io/assets/images/on-selected-dc6bc4f81bd0d298bbbc71ca82d99b59.avif)

#### On Toggled On / On Toggled Off

The **On Toggled On** and **On Toggled Off** action triggers are used to perform actions when a user turns a toggleable widget on or off. These triggers are supported by widgets such as [Checkbox](https://docs.flutterflow.io/resources/forms/checkbox), [CheckboxListTile](https://docs.flutterflow.io/resources/forms/checkbox#checkboxlisttile), [Switch](https://docs.flutterflow.io/resources/forms/switch), and [SwitchListTile](https://docs.flutterflow.io/resources/forms/switch#switchlisttile), any widget that represents a binary state.

These triggers are especially useful when you want to conditionally execute different actions based on whether a user enables or disables a setting, preference, or feature.

Possible use cases

* **Switch – Enable Dark Mode:** User toggles a Switch to enable Dark Mode. Action under the *On Toggled On* trigger sets the dark mode.
* **Checkbox – Agree to Terms:** User checks a Checkbox labeled “I agree to the terms and conditions.” The *On Toggled On* trigger enables the Submit button. If the user unchecks it, the *On Toggled Off* trigger disables the button again.
* **CheckboxListTile – Select Notification Channels:** User checks or unchecks options like Email, SMS, or Push Notifications. Each toggle fires either *On Toggled O*n or *On Toggled Off* to update selected preferences in the backend.

To use the **On Toggled On** or **On Toggled Off** trigger:

1. Start by selecting a supported widget, such as a Switch.
2. Open the **Actions** tab in the properties panel and click **+ Add Action**.
3. Choose **On Toggled On** to define actions when the toggle is switched on, or **On Toggled Off** to define actions when it's switched off.
4. Add your desired actions, such as updating a variable, showing a message, enabling a button, or triggering a backend call.

![on-toggle](https://docs.flutterflow.io/assets/images/on-toggle-9bc23d1bd5b7301c0e2382945ce9fccf.avif)

#### On Change

The **On Change** action trigger is used to respond to real-time user input as they type or modify the contents of an input field. This trigger is supported by widgets such as [TextField](https://docs.flutterflow.io/resources/forms/textfield) and [Pincode](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/pincode).

It’s ideal for enabling live form validations, updating app state as the user types, or enabling/disabling UI elements based on the current input.

Possible use cases

* **TextField – Enable Button When Email Is Entered:** As the user types in an email TextField, action under the *On Change* trigger checks if the input is a valid email. If it is, it enables the Continue button.
* **Pincode – Auto Submit When Complete:** When a user finishes entering a 6-digit code in a Pincode widget, action under the *On Change* trigger checks if the full code is entered and triggers form submission or a backend call.

To use the **On Change** trigger:

1. Start by selecting a supported widget, such as a TextField.
2. Open the **Actions** tab in the properties panel and click **+ Add Action**.
3. Choose **On Change** from the list of available triggers.
4. Define the actions to trigger, such as setting a variable, showing a message, or calling an API.

![on-change](https://docs.flutterflow.io/assets/images/on-change-88fcfa03bf04b3b1a30deca3915a861e.avif)

***

#### On Focus Change

The **On Focus Change** trigger fires whenever an input field gains or loses focus, like when a user taps into or out of a [TextField](https://docs.flutterflow.io/resources/forms/textfield) and [Pincode](https://docs.flutterflow.io/resources/ui/widgets/built-in-widgets/pincode) widget. It’s useful for providing user guidance (on focus) or performing validations.

Possible use cases

* **TextField – Show Hint on Focus:** When the TextField gains focus, action under the *On Focus Change* trigger displays a helper text or tooltip with input instructions (e.g., “Enter your phone number without dashes”).
* **Pincode – Validate on Exit:** When the user finishes entering the code and the Pincode widget loses focus, action under the *On Focus Change* trigger runs validation logic to check if the input is complete or valid, and displays an error if it's not.

To use the **On Focus Change** trigger:

1. Start by selecting a supported widget, such as a TextField.
2. Open the **Actions** tab in the properties panel and click **+ Add Action**.
3. Choose **On Focus Change** from the list of available triggers.
4. Define the actions to trigger, such as showing helper text, validating input, or updating the UI based on focus.

![on-focus-change](https://docs.flutterflow.io/assets/images/on-focus-change-eb02d0ce94bb5b1e5310a75acda7f36e.avif)

---

### Form Validation {#form-validation}

*Learn how to add Form Validation widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/form-validation

You can add validations to input fields by wrapping them inside the Form widget. The Form widget enables you to validate user inputs and display appropriate messages when validation criteria are not met.

For example, you could use it to check if a user has given a valid email and password. This makes it easy to handle user input and ensure that the data is correct before it is submitted to the server or stored locally.

#### Adding Form widget

Let's see how to add a *Form* widget by building a signup example. Here's how it looks:

Building and validating a *Form* includes the following steps:

1. [Adding input fields](https://docs.flutterflow.io/resources/forms/form-validation#1-adding-input-fields)
2. [Adding validations](https://docs.flutterflow.io/resources/forms/form-validation#2-adding-validations)
3. [Adding validate action](https://docs.flutterflow.io/resources/forms/form-validation#3-adding-validate-action)

##### 1. Adding input fields

A form widget can only validate if there are any input fields. Here's an example of adding input fields for the signup form.

1. First, add the **Form** widget itself from the **Form Elements**.
2. Inside the form, add the **Column** widget from the **Layout Elements** tab.
3. Now, add two [**TextFields**](https://docs.flutterflow.io/resources/forms/textfield) (one for email and one for password).
4. Add a [**Button**](https://docs.flutterflow.io/resources/ui/widgets/button) widget and then add **Date/Time Picker** action to get the date of birth.
5. Add one more **Button** to validate and submit the form.

Here's how it looks:

![Input fields](https://docs.flutterflow.io/assets/images/fv-input-fields-217cea7794a21e90fc1475fe1cc83e15.avif)

##### 2. Adding validations

Validation refers to the process of checking user input for correctness and ensuring that it meets certain criteria or requirements. This can include checking for the presence of required fields, verifying that a value is within a certain range or format, or validating against the custom pattern.

After adding input fields, they will be available to be validated using the form widget properties. Here's how you do it:

1. Select the **Form** widget, and move to the **Properties Panel > Validate** section.

2. Identify the **TextField** on which you would like to add the validation and tick the box on the right side. 1. Inside the **Error Message** input box, provide the message that will be displayed (below the *TextField*) if a user leaves the *TextField* empty.

   2. You can also specify the **Min Required Character** and **Max Allowed Characters**. 1. **Min Required Character**: This is the minimum character required for the validation to pass. For example, If you provide a value as 9 and a user enters the value as *<a@a.com>* (which is 6 characters), \*\*then the validation fails, and an error message will be displayed. 1. Inside the **Minimum Character** **Error Text** input box, provide the message that will be displayed if a user doesn't provide the min required characters.
      2. **Max Allowed Characters**: This is the maximum number of characters allowed for the validation to pass. For example, If you provide a value of 15 and a user enters a password that exceeds 15 characters, then the validation fails, and an error message will be displayed. 1. Inside the **Max Allowed Characters** **Error Text** input box, provide the message that will be displayed if a user enters more than the maximum allowed characters.

3) You can also choose to validate the input using our predefined validators or by creating the custom one. To do so, you can set the **Text Validator** to the one you need. 1. If the required validation is not on the list, you can select **Custom Regex** and specify your own **Regex (Dart/JS)**. Here are some examples of *Custom Regex*:

      | Examples                                 | Regex (Dart/JS)                                                                   |
      | ---------------------------------------- | --------------------------------------------------------------------------------- |
      | IP address (e.g., 192.168.1.1)           | ^\d 3 .\d 3 .\d 3 .\d 3 $ |
      | Time in the 24-hour format (e.g., 13:45) | ^(\[01]?\[0-9]                                                                    |

   2. Also, provide a message in **Invalid Text Error Text**. This will be displayed If validation for the *Custom Regex* fails.

4) You can also add validation on certain actions that can be used inside the form, such as *Date/Time Picke*r and *PlacePicker*. To do so, find the action name and tick the box on the right side. 1. Now you must enable **Add Action on Error** and set the **Action Type** to the appropriate one. This will be triggered if the validation fails. For example, in this case, if a form is submitted without selecting the birth date, you can add a Show Snackbar action asking a user to select the date.

![Validating Date/Time picker](https://docs.flutterflow.io/assets/images/validating-date-time-picker-490b88db4d2332d91249ea6c37362dd6.png)

##### 3. Adding validate \[Action]

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Validate Form** (under *Widget/UI Interactions*) action.
4. Set the **Select Form to Validate** to your **Form name**.
5. You can chain the next action that will be triggered if the validation passes.

#### Auto validating

Rather than displaying an error message after the user submits the form, you can provide real-time feedback as they type in the *TextField* widget to indicate validation errors. This feature can be particularly useful for lengthy forms where it can save the user's time and effort.

To auto validate a form, select **TextField >** move to the **Properties Panel > Add validations >** and then enable the **Automatically Validate**.

![Enabling auto validate](https://docs.flutterflow.io/assets/images/enable-auto-validate-c63d86f6dc81572a21a5ebeb15bb20ab.avif)

#### Validating a Form on TextField On Submit

You can also validate a form when you are done entering a value inside the *TextField* using the *On Submit* action.

To validate a form on *TextField* *On Submit*:

1. Select the **TextField** widget and select **Actions** from the Properties panel.
2. Click **+ Add Action** button, and ensure that the **Type of Action** is set to **On Submit**.
3. Search, and select the **Validate Form** (under UI Interactions) action.
4. Set the **Select Form to Validate** to your **Form name**.

***

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### RadioButton {#radiobutton}

*Learn how to add RadioButton widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/radiobutton

The RadioButton widget is used to allow a user to select one option from multiple selections.

You can use the **RadioButton** widget for implementing a single selection such as gender selection, notification preferences, etc.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding RadioButton to Your Project

Here's an example of how you can use the RadioButton widget in your project:

1. First, drag the **Column** widget from the **Layout Elements** tab (in the Widget Panel) or add it directly from the widget tree. Set its **Cross Axis Alignment** to **Stretch**.
2. Now add the **RadioButton** widget from the **Form Elements** tab or add it directly from the widget tree.

> **Info:** The RadioButton widget adds a single option named **Option 1** by default.

##### Trigger Action on Change

See how to [trigger an action when a selection changes](https://docs.flutterflow.io/resources/forms/form-triggers#on-selected) on this widget.

##### Changing Option Name

To change the name of the option:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Define Options** section.
3. Find the **Option 1** property and change the **name**.

##### Adding or Removing Option

To add or remove an option from the RadioButton:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Define Options** section.
3. Click on the **Add Option** text.
4. Enter the name in **Option 2 Text**.
5. To remove the option, simply click on the cancel icon () displayed in the **Option name** property.

##### Setting Initial Option

When you run the app, no option is selected by default.

To set the initial option:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Initial Option** property.
3. Enter the **name** of the option. For example, entering a value as **Jupiter** will show the second option selected on running the app.

##### Styling Selected Option

To change the text style of the selected option:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Text Style** section.
3. Checkmark the **Change Selected Text Style**. (Click on it)
4. Under the **Radio Button Selected Text Style** section, change the text style.

#### Retrieving RadioButton Selection

Let's build an example of showing the selected option in a Text widget.

> **Info:** For simplification purposes, the selected option is shown in the Text widget. In a real-world scenario, you may pass the RadioButton selection to your Backend (Firestore Database/API call).

To retrieve the user's selection:

1. Add the [**Text**](https://docs.flutterflow.io/resources/ui/widgets/text) widget to your page.
2. Move to property editor and click on the **Set from Variable** text. (This will open a new panel)
3. Set the **Source** to **Widget State**.
4. Set the **Available Options** to **RadioButton**.
5. (Optional) Set the default value if you wish to.
6. Click **Save**.

#### Changing the Properties

The Properties Panel can be used to customize the appearance and behavior of your widget.

##### Changing Options Height

To change the height of all options:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Enter the desired height into the **Option Height** box.

##### Adding Space Around Option Text

To add some space around the option text:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Find the **Margin** property and enter the values.
4. Click on the Refresh icon to reset the values.

> **Info:** Use the Lock button to change the Left, Top, Right and Bottom padding all at the same time. Unlocking will allow you to modify each value separately.

##### Showing Options Horizontally

By default, all options are shown as if they were inside the Column widget. Using *Axis* property, you can change this behavior to display all options horizontally as if they are inside the Row widget.

To display all options horizontally:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Find the **Axis** property, change it to **Horizontal**.

##### Aligning Options

Changing the alignment will change how the options are distributed in the horizontal space.

To change the option alignment:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Find the **Alignment** dropdown and select from the options displayed that include Start, Center, End.
4. If the **Axis** property is set to **Horizontal**, you will see options that include Start, Center, End, Space evenly, Space between, and Space around.

##### Changing Button Position

If you want to display the button on the opposite side of the option text i.e right side, you can do so using the *Button Position* property.

To change the button position:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Find the **Button Position** property, change it to **Right**.

##### Styling Radio Button

To change the color of selected and unselected options:

1. Select **RadioButton** from the widget tree or from the canvas area.
2. Move to the Property Editor (on the right side of your screen) and scroll down to the **Radio Button Properties** section.
3. Find the **Selected Color** property, click on the box next to **Unset**, select the color, and then click **Use Selected Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple button.
4. Find the **Unselected Color** property, click on the box next to **Unset**, select the color, and then click **Use Selected Color** or click on **Unset** and enter a Hex Code directly. You can also choose the color by clicking on the Palette and Simple button.

---

### Reset Form Field [Action] {#reset-form-field-action}

*Learn how to add Reset Form Field action in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/reset-form-field

The **Reset Form Field** action allows you to reset values in form widgets. This is especially useful for clearing previously entered data and giving users a clean slate.

For example, after a form is successfully submitted, you can use this action to clear the input fields—making it easy for users to enter new information for another submission.

![reset-form-field](https://docs.flutterflow.io/assets/images/reset-form-field-9555bd87c26221abdff902bc72be91ad.avif)

> **Info:** You can also reset form fields that are inside the components. ![reset-form-field-component](https://docs.flutterflow.io/assets/images/reset-form-field-component-189c6112822c7a787500e872dedbe4d6.avif)

---

### Set Form Field [Action] {#set-form-field-action}

*Learn how to add Set Form Field action in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/set-form-field

The **Set Form Field** action allows you to programmatically populate or update the value of any input widget—like a TextField, Dropdown, or other form elements—at runtime. This is especially useful when you want to quickly fill or modify user input fields based on user preferences (e.g., saved addresses) or pre-stored information.

possible use cases

* **Use Saved Address:** If a user toggles "Use Saved Address," you might set the Full Name, Street Address, City, and ZIP Code fields to values pulled from a user profile or database.
* **Edit Existing Data:** When navigating to an "Edit Profile" page, you can auto-populate the TextFields with the current user info so they only change what’s needed.
* **Auto select Country/State Dropdown:** Automatically select the user's country and state based on location services or their account settings.

While adding the Set Form Field action, select the target widget (e.g., `TextField`) and assign a value—this could come from a variable like `fullName` in your backend, app state, or page parameters.

![set-form-field-action.avif](https://docs.flutterflow.io/assets/images/set-form-field-action-0e8ca7dc0d5864645a21baa09f70a1b7.avif)

If you need to update several widgets (such as a TextField and a Dropdown), use a separate Set Form Field action for each and specify the appropriate value.

![multiple-set-form-field.avif](https://docs.flutterflow.io/assets/images/multiple-set-form-field-bdcfae8c0444b80a9a4bdbaa571b1caa.avif)

###### Focus Field When Set

You can also set additional preferences like whether the field should be focused and how the cursor should behave using the **Focus Field When Set** option. When you enable the option, it automatically sets the focus on the field once its value is assigned.

This is helpful in scenarios such as an “Edit Full Name” switch—when turned on, the field preloads the existing name and positions the cursor for immediate editing.

When **Focus Field When Set** is enabled, you can set one of the following **Cursor Position**:

* **End**: Places the cursor at the end of the newly filled text, letting the user continue typing from the last character.
* **Start**: Positions the cursor at the beginning of the text.
* **Highlight**: Selects (highlights) the entire text, letting the user immediately overwrite it.
* **Preserve**: Maintains the cursor location as it was (if any), which is useful when the user is already typing and only part of the text has changed.

![focus-field-when-set](https://docs.flutterflow.io/assets/images/focus-field-when-set-922b79f19bfb336f337de2da9304a23c.avif)

> **Info:** You can also set form fields inside the current widget’s child component.

![set-form-field-component](data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAIDEAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAoQAAAD6AAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQEMAAAAABNjb2xybmNseAACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAIDltZGF0EgAKChhl6D+WCBAQNCAyoEBMBAK0SXfcyYvIQUhY6FkRmHvEOBJI4nkskODet+RuOS2E4enKuEYn3tV3sVb/87UojPO8Ga3ZyL4gKhYZ6fribu85bDa/R/9q4dbVHCiWIPIjZ78nVf5cW2KiUKx3Qz/1fAPYUK4Cj2W7hQE57qapBeNEoBq1OPTLXef0hOV7CoXXT3DZUPXG76rqfneQVGSD/0FU1tMoGA1YV7SL3qaGNYoa7UqjjAWCVoG0n7poeWOcDJWjEGbBoIS84gieN5PdF1XspMCP6wBGUer8BfcEq/s7SHb27k76OUnwI7N8cnfLF9HecgFXEumeIDGJCviOvcMvq7l05TXMLLto4imKO4Ninv7rsQg/kjTprLMyK7a97qLO+EVI+hUjgpA6KPcqsL8gCmjN35FNGP+iGgmOTvDrlvHGRcO2RUtRC1i8JAr/GplQX+dr5JYRfntDR/DTAO42AT4UdslBn3vd9q+4XhKxEPffvwYXC9LYCcufdgZY4Fwo5KtKAwKZESA4fWfjZ/kgMXitTsjbCe6aToDTpOFevLXQ08gVbkYpDmT6nzeC9Upp5uaXjOqKDQKbD0QOZTTA6e1gf+GAIIPSSA20dbYgwIBXSxz3irTc8cNzf/3UnsifvpFfybVL3PNgEe8W8LVs2vc/vR+LyeUYLjcLDEZ3YhHWiKFcRsz9fhg+wDazWdMIXJbVqexjlODEEDqBNxPpdXKcxTm3zz6q8FJnSwt+oD0cKVfkgu1U+GByU+Fi02rlKVfQcCMODAkMYAqV/csel4AcEuFzJdNn5mmaO/C+3aw4PIx/nURfhSxfmwB7f+aQ8p7WZh+XMPVtz5dETaOiq8C4Ib70r3gH/nUJJlChB5z31uBvkmIYviRAoz7wEZVKognEv7M6P+mrPS9dO4Pe2AbVjtW4QvoWBELsva/M+5ipCAgnGYGlzbvHRwMIFGSSlvYagFAGJkve3DhhG+1SRQaFJuIPLrfacq0zRAj0GAx5Ws3NqMgr0yWstCF7OHeIoS+buyMimbRONJ/P3KcRDskoYLYze4KsdXhJ4mVIA2yuuZV+wxSdIb2afy0X5yLgxZsYIVWtKSOytmtX/rt+a5cq2a6z5HzzNwauM+WeGtUJyUDIJ4sxyK4UgM/P4Fz+V1waHToPwJ1ecZTnGGNSc/ruOo3GtGzf30ISeHW+piJycl6ZvfMvQ+wRER0BGDAh5UZ8UhOijmQ8l4ow4Xq6bnOMyt83/Ggb+4EnWnr7HUmPWjCKdV1U0xVPzisY35iT90lY2xFhtBO3muplEGc+4pDAxbHSbx9YcGBZlp8CgXQvn2jdpUFhXloPgpK1OBiO9+6F2BeIfMaA2rWo5YRAJgBVlRvRFFiNU65s7w343koaAhZG2EpvDrOB0wImbD/rha5NDLuWBvdkcnesE3yasBrPyGAH1VQmEKC4BiTIlqdKv0rSbSO46Lwgpj+Uxotc0RVaqNKJbM45ZnIsFdOwevRFuL5r41xIbYt1Zx0xpttv+/35RJ1sFHx/EWQDPH69Jv8mfqnCBt4kV1W7LZzGIWWYuJaPjjdJZV0pv7Avyru9HO1xrmclSrYqLCejYnneNFR2aRljosqkTVsW1N169ownMLaPJ2zjUlEsZBlY532/urzPNhFIaznev7QhKn7UOS9RiAKxkwEuus4GfD+OYnRI7r+U+Je7nfyrIKWREAU8T5tNqO0Ws3kEANLHmTlqE9JFzCCvm9uKyeSRRWJdRBkzNSN93CLUHWEXAfZs1F/TzQ4cwU1gfF30Msah5wqIwT6MLdADPwndiWvwPVMRGr8wodhAWwZj9y2W9Xk20xsRB0XFQ7x2BWfGxU3ZqkiuhChOo+YogsWmpXj0pb2WmtTh8Nxi1u8rllyH43H2tf7O7VyvLzOy8y8YRSw5jq+ozCosI6d9NkkV3zHt7GKPhNK/6MuzrI455woqaL3oYkJ7MQGxexfIJ+QWM0V/MZdpNwlW9lFWAqIDJTFIyQON72OXXL/JxAKDyozKHCrKbEpYUtCX7LN58EBbqORz0QBRSIOSn6RY3WPqa6MjnBxKThy6a2OTSH+lfS9PZdMWGSVZKAwE49no8paWj44cqTLOqSknTNfWws/w5QrUWNo47E7yKXOSlbo509pyG3vRL8m6PcNiFL4UuZ+GvdesxWmpWee5WnND0mbHZKGkI+01iCUK4zg46Folvp/XtZ3y+5BLBcIySlhDtkyVWIReFoPsP9pyaeQh4K7kg3ku98pPz1jkLS0H0MrGR68j4/OeL0i/naOt+HL6nVgLq4gRe8J8lZqr6edOJW+hGdQVsyiqMjmTTEJv8wHU2rkdvl4S5D1Y/p1VekWI+aVw2hVQh399sH9qx7e9GKoptWLgnotRIOPmTpXE7Alk3jGTOCDcUMvkaeIVcTyj+WhfRpwyyoCNUsKy33mJh3S4aR4JyDVQoW/aMDRKb7QBJ22adT6Ivoxfs+A4BDb/WTx5PBWgy9Bl8kbr+L/N7FQ7belJ7p4uuP9KM9HM3Twn9MNQTdStvmQYDorrVw4XfcGWuE4R4UXyITjFxej9KxUr1mr6KvVcVjB0hNN0/yF3Xslh1hKbyKHmPOYkEQ1wVwszBLZ8eyuUE4a6XXn5fs3hNcsLoBuuccKH5HPmFgVoGReuI3t79o0ZT8jJ4spk8zFCUjyCqbPKEkyR8lxE13Oe5K1TJvHn+U74FWdkTn637Zw6WuOes1c+aMiJV52sT/fDk1qDQcErBzHjH3SyUBRRLiRiFAQXIsReTGSu3yxbACE0SpAYLKM+kmbcnWAkqe7LZoAb6Ft/PpHxOBMhlD/qf/StyRRZBcoNc9irQyZCdP407gv6o5ON56ZpLl0mfJRQFMiRYXWJXn+c7YGuCOvlNJyAtw01hlDiS6LpkJsc7FbmnPRAPteb1fU/EVatERBkGy/yMAfCKLcA5DAh1d8fb5BItPEB2X8y5baCS8IuY9uIADd7i0Vjt9LsW+locH6WTg0IQiFVEl+Wo3h6vHaLcWxZRZ0N+J1saFbTYVIu4TGZkR9He9Z/I7zB38WJ59v0x4zAc7UmszPURvpAremDzJFjfQ2m66EIAsIgc8McW61GY+/ro0P1e5mTzk+cLt9SrY4i5lrr/9SBOg5zRZ9Tkszv9GsJfhwHD4jYTMqUWl5L0/YBa6hzUOp6MckupRFkaV30JHcB80ybBVk+N2KaIuYy3RWzszFg2CyqswQsVYPO0cV3uy8/8rrhVCABms+SLl4Z2fCZ4eZd2ahgBYvRDRmEK7RLKq+FmF7A1miUzlXegblwIsTgHiXYnPSIkVhC3yuMtkPJUnD3SU0Wsp/93gSQHYKROQYNHUyfuvfyxthZv8xTnrfiPtCqPhT1BiCzjNow3jvDrHo70pR+YOgTsyyvE/UA5nB0wX5wMxVTuZxX4UW2CCOodVw4Rx1Ai8EHyWU0FTVNqzAFvkT4J8gVke0X4mXQyaznNMOvTRkJREcTzNXEOXIBaFhkvxCKa2rGyBi2qVV+b4flMLcsk3sTydoGiidEYkhhyGfOGGq6NH3y0aVrqrPYwgHPc03D7LVCZxX3lKbhrtPFqw77zl2PfyTXKLiAFXeGxhz2yWax+iMgEjCqlttCcBSyhnEOJAN5MJQrLVknqEBxs0jUDaZj7DhQPonrwVMCSS2oI40yGoDqWM3HsMtrh0+AngaFqvofJJTFuQFO0exKh8YNcD/fW84Q6pV5zfp0gNWI4WsSACPP8UV2fjamQ2Cp0az/+fTfUiUomZS+XQModvsWuY+drrz5SffKXSwRQXf9VmLp2t+pDd30XDcV55z6rPvwv6TYYbHlTRPRRnf/Jnpv8vv+C1fZMc/UaSiPv1GBuy81GBxmt67paJeHi/z4+7kHsou4NkwubnPQtnwZmfr4A1i+GR3vVcemT8YzXH5nizhxH+TJQEJsZZaT4KbposF60bLYW7vt1Ja/vB0PxXloG4+aL46n/Z1NIIZ92r2QAuqIhJXWpXX4EgTVzkV/OkH1jT8vZI0aecIVHB0+2g5VGzdqCED8TrxyWVErgBgOA6JZk5Vw1iw8FNzbOWxe3gGgHlx69bMYJ0bACjJx7OFQiKtbGMAWG38JC6On/RcamqljWhtu301N5JOfeIP//XVWOERA7xJAqeU3nE87u+YQSsMym/x5zHejVHoRHhSjts0pfCPlaAI6tmuQ3NK15drKV1wFS2Sljl1KX195+uo3UMZTsPM5OHGOA2REwNXYFU3wRuQgJjoM0XzO9IncxII5GZKc22JWXE7bBLrpq3BfQzaawo8odZzFkHhDAQQFx72F3XQ1WqgNxhJsp/TZ9iRAxPRrTyTHBHD59BHGdMVN6+mxFpBbE6lF1WvNay9aJG4VeWxSrghll+qQsfd4OJ7Wy1yyiICK8JUsPC4Nwf303CWzrnzBMBwU3Ryrkmx/pXk1SWcFoerGLSyLvPxvAmjlRlqUHKLtLtIWEmeA+xkBcAFekOSpG8/MQVbLhEh4hA5D+67FBmBLvduSRY2OE9Ryonw6sl0r90vbQO3MTMW5VYEWDqSKol8mhuCoXmvZpQEoGAV7zBKlQqksW8coCZ5m6ZaTwOqL5nNYxvrvh1oa9x64kqRHSCvwh5KbGK/b00GI7k6NU/9aPJxV4jQUODHS27zBr2/re1YlejqMOvYEj5/OXlHY2lKMisSaziN3PUdIAfwNPNANDlF8OEXS48lYTfSbX7JfLRweqwXAeGLzUgyqWLCQrEBGoRjUTcgcRQa5T2PuVHGx7ytbqNws0yv1qLI4kVQoVZeAI5np52nhwEZZGAiZCxPhhLnRmfQoP2ySytE7wWxwI8PDzDVGIgyqi2Lj2ImmRDcrayISomHJhGFl/9ey6hhNq+SCbmcDeLaWLocn00ZPmpdoii7GXnG0XKjc+7BmB1Rv9A0+xOMfHnLf9e1jqZ7xuzjJ7xtZKvixLw+1DNVij/vKGUN9yuGfIlD+9Sz6b/CeYEB+N3vBIblNbwjJvg47w/SDkLl5UXKNAj/O1roKMrOvaAGMsfwmSAoXvx2dYyqnMvv115/JWVXF3rwp4dUZNYZ12zzCs2fx31Uerx0p4mrmgvcBHppldMO2HiXiapN3nwTIULHlVFu/IBNJCiFkY7xJwhLFmpAjFS6gj6Ucqs6nP7vtD3xmE6PuNB6tcNYRx8t4ugya4wBZ0EEFP+QRlBnmtn8uFnSVdc5qDZooflxphkYFqrc5lqKMUINyDKs5k0tMWpYDRufuK5ydSrKebo7r3C9aXpeIvUz/fEuIEB5tN0SZNdl74RYl2+tiOGa1y9BaKYM9LO7Eyvf1ZLY9FFQP4XLvPCHQiF0qz5T+iiFEJwqCfv1zeHTtGbGQZhjl9TKhUeysKk6+RAErQta7GfoDrIjYxZWdp7gpDfjPHkdDR2AgyghX5CuIBAHxWMSWMn3l4KrFan3XmELIYhIQ3D+flkAhnKTXrKjQJ3FXlLvdcwk1tMnTvzrUDmd2o1g5lfUrUwnSo5J1Oa8RKbQnFhdbm0Q08kXz354owh0nKbbbhfJ9mpdz/OO4sHiAr9Zc9o4UUA963QkLBSBjFWDvJxTfNGTfP47VsvRyytMCYJ/kP+pf7MNXmdmGhfmMfRRvmzmFIHfOsHfOTo5wQBv6aiV4DvhRSqrVEo4DyQRKE5+I+g+BvoKxZlsxLNW8vKFy56/0tOwRHaj/C8dDiecCAKbQW0nl4/7O0MFXOhL7iKife4XuA9jURBSYzFjruFF/EAFCQSxwEQjvPPETVuNc/ctxQ9gB3NtvfQieXoHbXrll5Tz6vTEf0eR40iGBaYFTWOGe986R+cOstGFPN8N07HkbGAqDJpR0Ef7BltyWjPBwGrg/uo2BfWuB8bQyiba7bXKhPxCRdvEU29gz/iSQ91jrGvCDcRV+KJ8FUIkjlqcNkdD05yOyAHludB/7KWH4IyxmM1N7vIBlr9PdwjK5PyBGtSx9Hq+dwfC+UEAU7Ed5Kp7Q8Y+xLF56WY3PNU4lNvLrvK06mjlTrXepbSol0VOEZTbFWY+MKNbKgDXMJzcbNInx4G+HWLlXMESuQiRCyRlwPJvXk4b1C5Hbr3Le2AOk2ZNGD6b9/7+dK2ChFhh58H8AOkGSvwrgpzIATs7FrYUd7s/Zk79toUBSzOZHB8EaHl1h/AjS1TiiKQKsfMVnXO52RbfVwo00ksxP7UAFSRtZMxtQgUp5i6zvNTf1pXLeR2OVcEor8bVvQOXbw7Admj4oBHfYXGnGDJ8lBbHmdWt2/DQ09s8xYgZWIFhV4Eyh8NBg4Rf9jaKrMiph+iN5Xno8Ae7KvwFVI3Hz4xTLLiNCBduv1JL1kz8NKTmUOcqD39BtGw41K+hR8IeRUfA6SkCuDWC9K6LAX4X1PouXqIfRmE7twfPDkz4whzSDjvnmEctmKO86DKpuMpD75BYyIBnWWgh3nYKzB05oPW+zfo2aGnxHaAjI7H6uFU3WD/oT1xJi+Tncu4pJE/m+CT0Np6gjI2EvbC26r9+SvwNrnIGdFSg8SbdS7ZuxbFurZs40fd5HFCCP5XjxaIfAxegXa9nn1wA3+RRIVeua8ekXg6TdfUEj7st4kHPLIGEZezIYTPXBYzaw6BsVKwDUtfZatvjeMFH48+Af5S5J5nRS3Z2dUIyGElIUtpop1hC/hnTOMYIfdAGlNTV98olvtM/e9oYbNe5ZTAuCXL2MzBrThPQ44TL5UemnkKf9Z+itTr7FuJuStuHSw9/IWaY1P6kBUW3pm57yqEXJxvI69L9qGPW2Mkfhqv+4iv7Anoa1ju2a35EyE+dMemyaDKAS4w/BaDHLIcH/ga+qlxAVAOyI4uGeSz5NGzX139sO2zVPThk2lRY5nFy1Fj4i9qAO+2xgdtC/APUD8Xh0dAE2YzIDWrrlFhAxl/zNLD/sMHTQ7G6/zoQHLOmNOzm2CtPP9Ryf5/nb5mNNS9La8V2U05UzGTseHPrh3c/2sm9NiiaQimA5hr2QVN8UH0JVJ9/nker41nPJUcjR3OKgMpwnJEU1p1NmOd+QVUopOPsJaSzOA7sHxyFfeIQuL9S9ujgTWgfcvTxKFmVKWf6axOU91kVE8vpYyBt+yxfHUeGmHQhk4qV6sn7C8uQLxEXsZ6vabsLJJn+sGxNFifqHPR1vzmsaBS5yBtLTJN4hm2bpiTokT3/dS5aZEdPDZ8urApZAdMPgCGLvRfEZuOGCzdy6+lGdfAuCPKPl5Bu6VcG94d3Zow4/BfFee55vovvpzB7GuRET2WYe3DpcJ4yDuiGmeaA3zthFAL11KiGf+YMTUC7Sa43VUlPk2degyHMgWFxVGwj8XQCmHAVNw78516TXg/JuR8+4/ZtPkZDlIOAcrBKGz6vGhCo4Osxlm64FHJGAi93jg9eWXbFEWp5DvhfiuiZmNYR1jSgkOdSfjXHsTl3EQf//D9z3cHQIfGyMEFq5hyyJE1Tdscx3ujDYyhOn4NCN3K2ABE1LOPGLE4SA2EaOpKF4YLrCSX6RVPCMklaBP8dIsbiV9h04KWpJy9nH5++5QRPLHJ9ZgrNvf/fYQtauQRv9aZ+AAoQb0aMRR1bAoRkUtj/iPD8rvEDU02QH2AD4rlmdCUpoMGOEH0DS6MTwKkkJUmu9b7E01EmlkyhFgkRZLqZb8ZXhKHVOO4CxU86TGbGM6Tq+pg5v4/4L+zWGoNNmqqIlrIuU5ERjwAua9ypV5Vfy8lkEKPFtxQwxh7dbPdeeMTqTKnmEPJ6EEJFoDxE4lngFLEru8UJM8FRaBtnxchcsN6csAVGLby5G6iH3KqRJZXWnmbCZLRzJJE+AupxzjHDx6WmZvTssrUZisWOXzMMfKrR1CwJmBqBK1+Syx8iNaMKfTasoN0nU9mTWnAl6FMHq+Ts6vgzPZH9akypyPH4zjGBh0A/w/tRA1gD4GKbujoEfirhubiXOK4bECQ8yb1ODSnUcKYMapruD+J6IiWJAw4YeF5HxEuc3bgvmsy7Kc9qCr79HYEJ2STxORMnPBrkjCdp4Y/RIA4UF7TZ6tUzpfUU++l2/wKePVO3PhUA/EBbgmW7s9YmVsNxbcib+tCmUStfPy40VIaI+g18fQTJLERWgNQAPPEwQvFG96VBRjs6ZTAiuRuwy5DLVpTWfXAfG5T1shKqmTbXWqgLR5ILMHxU5uVo72XjKGShRRzICUbFTTfKZYujAGfvo/+TcRLfTMJRdj86tR4c9BhOaByLS+bBZ472DxHfGuU9rI06PhdrDwrYRphqA+aLZtBjT1VqWv9XFtNUGYYnpkwj75b9wM0FXv+ApLRZ+79NBDxXroKd3wZ4JC9rzIlB6SUPs550m7bSOgOSajSeMQtReg+HRpKSNBYLTEyNfWIXi6lFiPQo0u1LfgEjYpxVHptAaLNnlpk3nAEvUsGkPlJOs4ZvAG+6RSaKq6uXiIYkRslOrOksVL1soKB2I7hbMzGeSrQhm2exCSv2iSviIZabaZ++GvExo6S7IcLHWRRm8VG7y65SJMXn/CfFkPknfofLtzxl9BTgtVOygqtC7ZgnfioAb9RKXBXEiCAVOdYng6rKzgT2TEzx69Hs7/VV8o1ObEwpwowH7qVHFaNAbOyVMAKFKuqq0sLIbKt/zCNr9aHRjwjwg86vC2P4XWw1NVv1ESqz3dvHmGabRwNn3VWZGoUZ9pScF2LLmpZunQ4Bl2jI7iJm5nqnGUot3jmnEnaVy+3IhX+etNyeE4tocqydr0z5QF8SPqjbg5h8PEBZL9jWPGpPN1Wkx2mOWJjmjNKB94KB2JeyNlKVmC5yKFFyObmRuu6kj9t77T0iiuDaXoG/FVfUlD3ktrtfv3ffX34pnfO6slGCvUBTrRu0chEGlLpXUsHnOyZt6Ih6eHle94F5V9j83ApyPMAWbbeTeIblL6rT0Tsu1VVGft4iqVjFGFpCFicrn02uO6nsv6g6ZBu2C3UK0L/B8a0wFQ362qFwvE6YjXmjFK9VPoseVUVuf2n75GsSE18qcddECUx/Wy9Rupo5t87HglUrBeWZKQ2Cqi7uiT//IFO088GnOx1OxuuoAZjhT7iU0QYlN5P/1b9CctHJ6ch2gWFCuQUTeyH/P3Ua08HWr/0DSTU3ZDsqQpA/9AJGqBi2aOWst0tkQ6D4OXVktk5p72hRwd0SPVpDDS3CO0050lEUPwOxnp+Qf3mHCYDu7shrAXA6fM6XaxnKLOE5wV3aOo/8KJL69+dG6XM/7dK51MEoEMM/r2+n8KucuTFOrSfsbs6CzLd1QfrDlO1eH7ypvFo3Z75tth3XaHT/5d4AJEzg7UrkTosKOqlgZlniZrNrq74SrkbzHlBVN2LOqXM77LTkF/b56CIUVCeNPnZkTXwDhzXUCSniJSMbH1eo4XH7coMfeRCm7w0JUY0QlLMOY24w4BUbYLx2kcKANLDTy37tewK0YIUUeksop+V9c9gY851sj6jWWQgvcdcGl9vRGC6+omy2Rgo6LSkkIuWK/1FI84GhuH0qpCxRxjud4ju8GuYFT1KK9Nslr03lEw166ZJ/yKmkaiD2uQlz6btZDs0iyv6PrPwRo7Efit9lFTUAPibUXRyeCFBZuX5J9G+nLeDV6nyB9K77yd9KJ+ef/8IHhiwTTgDziLDK2fnJDmwEDY9Dccel5Mbor1w5cPTuhS5L3hCQU2Xk52ENqeiWJzMTgoLyQgRt1f/VRdr/aNzUb0+KPWMTRdn5EZSOI7zmwqC05D1Ga6/ePuxKlk8Gd76Fo5yNhIS0ZgWJSe7PQARklwreZ4IW4C7zkD8pulzf61Y9FIwCY4NQWTtf5B88NgrFGBXz6knVzgFDMidiid6J/6PjF5CbT0/omvxSBMayCudhKDKzj80dmHbWOnADOko4D+5ZH5TNjXthcAHdM1GSt4Vcv+E5FcXZieieQajOCX1YNKsAFKj8dzfXaRPUA7tSvovUfu6t1wR3j9xK9QOGrbPz4s1cy0dS7WUL/p1HrYflyJmlhYmwP8NviAF5a5bvvHKpt2a69x6+GZHnIJlM/QAEPA10hfd6tiQ0NwQKtrIz56Cj9WMZuXJPtsCl0i40Se0nD7y0Dbt6LvdkLxE8HFddoIHFlUsIAE1FO7TvzNGhIYabMR5pKn6EkrBAy1SAWtgle/7/jQ2/smSg69401SMRsf/JeGRZLNPzMqYdTTmddkPK8XJyMk5GKMJQ9T3a2ipkSvHH1AxDSDAFXvaOtL09k4OPAPPuEL3FjYlPMw8h8eAiRYcjxD6CPJz6Qlu5Z17sOGNmO9+PFuDmzkqUyTTjPPwh1VlhxaRELM/9MITnRfmvW4nEpSrI9zkxoxqwwpqSu0Ky5lSvcAUBCHVbHteRpAA4GdqLuzK+82x9TJ0A47AkcByPyskk2J6Mb7DoA81IjUCvcOjTmLaysCe+nIawXM9dpzy3o/t6lK4eb/S2xPC/LSjPvWwDQqN69aPAwQDRIpLmpRR/Yp05Tgdh3fS4DUpMmHvNFC8BprEhHhVOSlQRlXFuFFnqDsJFKh8qfcCsJT4jVwb0RIYDemB/bfUfWkT+dArYoF22xBwNMBrIi6vBUQL1QH9epW4YI2vn7HSzeL4YskN5iRSpL0WO9FjnSOmbRE+jAuGRN/jespg9cbEwyXRjemwIYWQ1gMH/VhLc9SaXUbrmpGKxvxwO+MENnAawpb3uRYfhA0W4NnHoWUdYkGShHgVyHs+p2I42wjMB5/2mG8r9rEWQplrVH7ZpGOD0yPfo9fVCmQbDzRqj/22CYrf6CqzpEG/KiRagIB5Ls+WML1ceCzlYHPpcnxRqNqJhVT/zbc4b5Uc+zzvn86oH6GCFGkN0SxXnObdyX16+T5IyT5ZHRlfZtBY17VojlJwQbBB7Ud4a6bifpdEXJd8IXwWYKXw1jaEm6zQc7glEvmCQm2XT5Yxdjj/EfWw54wWoA+xfD9kwTTKgmHLEaqaJh6108NZLUS7coNSlT)

---

### Switch Widgets {#switch-widgets}

*Learn how to add Switch and SwitchListTile widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/switch

In FlutterFlow, **Switch** widgets provide an intuitive way for users to toggle between two states, such as on/off or enabled/disabled. They are useful for settings, preferences, and other scenarios where a simple binary choice is required. FlutterFlow offers two primary switch widgets: [**Switch**](https://docs.flutterflow.io/resources/forms/switch#switch) and [**SwitchListTile**](https://docs.flutterflow.io/resources/forms/switch#switchlisttile). Each of these widgets provides unique features and use cases, making it easy to incorporate toggle functionality into your app's interface.

#### Switch

The **Switch** widget is a straightforward toggle switch. It consists of a sliding button that can be moved between two positions, indicating an on/off state. You can customize the appearance and behavior of the switch, such as its color, and initial state (whether it starts as on or off).

##### Adding Switch

Let's see how to add a switch widget and build an example that shows its value on a Text widget. Here's how it looks:

Here is a simple way to do it:

1. First, click on the **+ Add Widget**, drag the **Switch** widget from the **Base Elements** tab, or add it directly from the widget tree.
2. Below the Switch, add a [**Text**](https://docs.flutterflow.io/resources/ui/widgets/text) widget, move to the properties panel, click on **Set from Variable** and choose the **Widget State > switchValue** (i.e., name of your switch).

##### Setting Initial Value

You might want to show the switch with a default status, i.e., ON or OFF. For example, showing the location service setting with a default switch OFF.

To set the initial value:

1. Select the **Switch** widget, move to the properties panel, and see the **Switch Initial Value** property.
2. Use the checkbox to set this value manually, or click **Set from Variable** to set it based on the dynamic value. If you choose *Set from Variable*, ensure you pass the boolean value from the source (e.g., API response, Firestore document field).

##### Saving Switch Value

You may want to save the switch value as soon as it is toggled ON or OFF. To do this, [add an action using the trigger](https://docs.flutterflow.io/resources/forms/form-triggers#on-toggled-on--on-toggled-off) that responds to changes in the widget’s selection.

##### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

###### Changing color

To change the switch colors, select the **Switch** widget, move to the properties panel, and scroll down to the **Switch Properties** section. Here you can [change the color](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#change-color) for the following properties:

* **Active Color**: The color of the thumb (circle) when the switch is ON.
* **Active Track Color**: The color of a track (the line over which the circle slides) when the switch is ON.
* **Inactive Track Color**: The color of a track (the line over which the circle slides) when the switch is OFF.
* **Inactive Thumb Color**: The color of the thumb (circle) when the switch is OFF.

###### Disable switch

You may need to disable a switch if certain conditions aren't met. For instance, users should only be able to toggle the switch when the connected smart device is operational.

To disable a switch, move to the **Properties Panel** **>** turn on the **Switch Disable Options >** click **Unset,** and set the [**Condition**](https://docs.flutterflow.io/resources/functions/conditional-logic). Once set, you could also customize the disabled state colors using the *Disabled Active Color, Disabled Active Track Color, Disabled Inactive Track Color,* and *Disabled Inactive Thumb Color* properties.

#### SwitchListTile

The **SwitchListTile** widget combines the functionality of a switch with a **[ListTile](https://docs.flutterflow.io/resources/ui/widgets/composing-widgets/list-grid#listtile-widget)**, providing a more comprehensive option for displaying toggle switches alongside additional information. This widget includes a switch, a title, and an optional subtitle, all within a single, cohesive element.

SwitchListTile is ideal for use cases where you want to provide more context or descriptive text alongside the switch, such as in a settings menu or a form with detailed options.

##### Adding SwitchListTile

Here's an example of how you can use a SwitchListTile widget in your project:

1. Drag the **SwitchListTile** widget from the **Base Elements** tab and drop it inside the **Column**.

2. By default, the switch is enabled initially. 1. To turn it off, move to the properties panel, and **uncheck** the **Switch Initial Value** property.
   2. To set its value based on the variable (e.g. app state variable, API response), move to the properties panel, click on the **Set from Variable** and choose the **Source**.

3. To set the title, scroll down to the **Title** section and change the **Text** property.

4. Similarly, scroll down, find the **Subtitle** section, and change the **Text** to add the description.

##### Setting Platform Type

You can set the platform type to *Adaptive or Android* for this widget. Selecting the Adaptive type will display the widget in its native style. That means the widget will show iOS-style rendering when running on iOS devices and Android-style rendering when running on Android devices.

To set the platform type:

1. Select the **SwitchListTile** widget from the widget tree or the canvas area.
2. Move to the properties panel and open the **Platform** section.
3. Set the **Platform Type** among the **Adaptive** or **Android**.

##### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

###### Changing switch color

To change the switch color:

1. Select **SwitchListTile** from the widget tree or the canvas area.
2. Move to the Properties panel and scroll down to the **Switch List Tile Properties** section.
3. To change the color of the thumb (sliding circle), find the **Thumb Color** property and click on the box next to the already selected color, select the color, and then click **Use Color** or click on the already selected color and enter a Hex Code directly.
4. To change the color of the track (the line over which the circle slides), find the **Track Color** property and click on the box next to the already selected color, select the color, and then click **Use Color** or click on the already selected color and enter a Hex Code directly.

###### Showing switch at the start

To make the switch appear before the title:

1. Select **SwitchListTile** from the widget tree or the canvas area.
2. Move to the Properties panel and scroll down to the **Switch List Tile Properties** section.
3. Scroll down and checkmark the **Leading** property (click on it).

---

### TextField {#textfield}

*Learn how to add TextField widget in your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/forms/textfield

The TextField widget allows users to enter text, numbers, and symbols in your app. You can use the TextField widget to build forms, send messages, dialogs, search, etc.

Widget State

Before diving into form widgets, check out our guide on [**Widget States**](https://docs.flutterflow.io/concepts/state-management/widget-state) to efficiently manage the state and behavior of your form elements.

#### Adding TextField Widget

Let's see how to add a TextField widget and see an example of displaying its value in an Alert Dialog.

Here are the steps:

1. First, add the TextField widget, move to the properties panel and give it a name.
2. Add the [**Button**](https://docs.flutterflow.io/resources/ui/widgets/button) widget and on tap of it, add an Alert Dialog action. While adding this action, provide the Message **From Variable > Widget State > \[TextFieldName]**.

#### Customizing

You can customize the appearance and behavior of this widget using the various properties available under the properties panel.

##### Changing Width

By default, the TextField widget takes all the available space in the horizontal direction. You might want to limit its width to match your design. See how to change the width of this widget.

##### Adding Multiline/auto Expand Support

By default, a TextField is only one line. So when you type in a long text that won't fit in one line, you'll be able to see an entire message using a horizontal scrollbar. You can change this default behavior and show the full message (without a horizontal scrollbar) by making the TextField multiline/auto-expand.

To make a TextField multiline/auto-expand, move the **Properties Panel *>*** find the **Max Lines** and **Min Lines** properties.

1. To make the TextField auto-expand as long as its parent allows, remove the **Max Lines** value and set the **Min Lines** to **1**.
2. To make the TextField auto-expand up to a few lines and then show a vertical scrollbar to see the full message, set **Max Lines** to a value up to which you like to show an entire message (e.g., 3,5) and **Min Lines** to **1**.

##### Setting Prefilled Value

You might want to display a TextField with some initial value. This can be any specific value such as "*What are you looking for*", "*Input your Email*", or a value from any variable.

To set the initial value, move to the **Properties Panel > TextField Properties > Initial Value** and enter the specific value or *Set from Variable*.

![setting-prefilled-value](https://docs.flutterflow.io/assets/images/setting-prefilled-value-c47b24e1996e7de1532b8b69333d6444.avif)

##### Adding Label

Showing a label helps users understand what should be entered into the TextField. If you don't have an initial value set, the *Label Text* will appear as full size in the TextField. Once the user taps the TextField, the *Label Text* will become smaller, and the *Hint Text* will appear.

To set the label, move to the **Properties Panel > Label Properties >** enter the **Label Text**.

![adding-label](https://docs.flutterflow.io/assets/images/adding-label-902c402214265f2a53df93b3547b6c10.avif)

When the TextField is set to [Multiline](https://docs.flutterflow.io/resources/forms/textfield#adding-multilineauto-expand-support) the label appears in the center. To get it closer to the hint text, switch on the **Align Label With Hint** property.

##### Setting Hint Text

Showing a hint text helps users know what information is needed to enter into the TextField. For example, showing hint text as "Enter Your Email Here" clearly informs the user to enter their email.

To set the hint text, move to the **Properties Panel > Hint Properties > enter the Hint Text**.

![setting-hint-text](https://docs.flutterflow.io/assets/images/setting-hint-text-ea03c449e2bd46fc47082cf5b62a51b3.avif)

##### Decorating TextField

Various properties under the *Input Decoration Properties* allow you to customize the TextField to match your design.

##### Changing TextField Background Color

To change the background color, move to the **Properties Panel > Input Decoration Properties >** enable **Filled >** set the **Fill Color**.

##### Adding Border

Here's an example of how you can add a border around the TextField:

1. Select TextField widget, move to the **Properties Panel > Input Decoration Properties > select the Input Border Type**. 1. Choose **Outline** to place a border around the entire field.
   2. Choose **Underline** to place a border only on the bottom of the field.
   3. Choose **None** to completely remove the border.

2. You can also set a color to the border for various states, such as when TextField is in a *Focused* or *Error* state. To do so, use the **Border Color**, **Focused Border Color**, and **Error Border Color**.

3. To increase the border thickness, use the **Border Width** property.

4. To create the rounded border, use the **Border Radius** property. By default, any value your enter will be set for all corners, which are TL (Top left), TR (top right), BL (bottom left), and BR (bottom right). Click on the lock icon to change each corner separately. Use the refresh icon to reset the values.

##### Add Content Padding

Content Padding adds space between the test and the border of your TextField.

To add content padding, move to the **Properties Panel > Input Decoration Properties >** enter the **Content Padding** value.

##### Reducing TextField Height

To reduce TextField's height to as minimum as possible, select the TextField widget, move to the **Properties Panel >** enable the **Dense** property.

##### Changing Error Message Styling

You can also change the text styling for the error message. To do so, head over to **Properties Panel > Input Decoration Properties >** enable **Custom Error Style** and [change the text styling](https://docs.flutterflow.io/resources/ui/widgets/text#common-text-styling-properties).

![changing-error-message-styling](https://docs.flutterflow.io/assets/images/changing-error-message-styling-007121650f2b27c1d1bbe4fba7422883.avif)

##### Adding Icon

You might want to add an icon inside the TextField, either at the start or end. You can do so using the *Leading* and *Trailing* Icon property.

To add a leading or trailing icon, move to the **Properties Panel >** find the **Leading** and **Trailing Icon** property > Click on the **None** button **>** search and select the icon.

You can also [customize the icon's size and color](https://docs.flutterflow.io/resources/ui/widgets/icons#common-icon-properties).

![adding-icon](https://docs.flutterflow.io/assets/images/adding-icon-95bb6492fecbd52ce05440bc093e7a75.avif)

##### Using TextField for Passwords

To make a TextField a Password Field, move to the **Properties Panel > Additional Properties >** enable the **Password Field**.

When you enter a password, it will be obscured with the dot (•). You can see and confirm the entered password by clicking on the

**Toggle Hide Password Icon**. You can also customize its size and color.

![textfield-for-passowrd](https://docs.flutterflow.io/assets/images/textfield-for-passowrd-6b3f53f88dfc032e449d8199f664e528.avif)

##### Clear TextField

A clear field icon inside the TextField allows the users to quickly remove the entered text.

To clear a TextField, move to the **Properties Panel > Additional Properties >** enable the **Show Clear Field Icon**. You can also customize the icon's color and size.

###### Adding Clear Text Fields/Pin Codes \[Action]

This action lets you clear the values from single or multiple TextField and PinCode widgets. This comes in handy while implementing a form inside your app, and you want to let the user reset the form with one click.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., IconButton, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), click **+** **Add Action** button.
3. Search and select the **Clear Text Fields/Pin Codes** (under *Widget/UI Interactions*) action.
4. Select the *TextFields* and *PinCode* widgets you want to reset.

![adding-clear-textfield-action](https://docs.flutterflow.io/assets/images/adding-clear-textfield-action-10eaab0d9d431d61dfa1c0c8308015bc.avif)

##### Autofocusing TextField

When you autofocus a TextField, it mimics the tap event and immediately shows the keyboard. This makes TextField ready to receive input from you without having you click on TextField.

To autofocus a TextField, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** enable the **Autofocus** property.

##### Enable Interactive Selection

The **Enable Interactive Selection** toggle controls whether users can interact with the text selection features, such as long-press selection, copy/paste menus, and selection handles.

By default, this property is set to **True**, allowing users to select, copy, and paste text using the platform's built-in text selection controls. Disabling this can help prevent unintended text copying or editing, especially in sensitive fields.

![interactive-selection](https://docs.flutterflow.io/assets/images/interactive-selection-323dae6cef2a9187fe13cfa47857e9a5.avif)

##### Autocomplete a TextField

You might want to allow users to enter the text by suggesting them a list of items. The suggested items are shown if it contains the currently entered text from TextField. For example, using autocomplete to get the *Country* *name*, *Fruit* *name*, etc.

> **Info:** This helps avoid spelling mistakes and enhances the user experience as users won't have to enter the complete text.

To autocomplete a TextField, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** enable the **Autocomplete** property.

Now you can customize the autocomplete using the **Autocomplete Properties** section. Here's how you do it:

1. Inside the **Autocomplete Options**, click **Add Option** and provide item names that you would like to appear in the suggestion box.
2. You can also **Set from Variable** to show items from any variable, such as app state variable, API response, and Firestore collection.

> **Info:** If you *Set from Variable* and run the app in preview mode, you can try entering the country name. The list will be populated with matching countries.

3. You can also customize the appearance of the suggestion box using properties such as **Height**, **Elevation**, **Background Color**, and **Highlight Color** (highlighting the currently selected option in the dropdown list).
4. To style the text displayed inside the dropdown list, you can use the **Option Text Style** and **Substring Style** (can be used to highlight the matching text in an item name).

##### Auto Fill Hint

When *Auto Fill Hint* property is enabled, it uses the operating system's autofill service to suggest the relevant information to the user, such as usernames, passwords, or credit card numbers, based on the context of the text field.

For example, you have a form where the user needs to enter their credit card information. You can use this property to help the autofill service suggest the user's credit card number and expiration date.

To enable the Auto Fill Hint property:

1. Select the TextField widget, move to the **Properties Panel** **> Additional Properties >** enable the **Auto Fill Hint** property.
2. Set the **Auto Fill Hint Options** to one that you want to provide a hint about.

> **Warning:** The availability and behavior of the *Auto Fill Hint* may vary by platform and user settings, and it does not guarantee that the operating system's autofill service will suggest the correct information to the user.

##### Update Page on Change

You might have added the TextField widget inside the search page and want to refresh the search result as the value inside the TextField changes.

> **Info:** Enabling this feature will refresh the page whenever a user types into TextField after a configurable delay.

Here's an example of displaying the TextField value in a Text widget in realtime:

1. Select the TextField widget, move to the **Properties Panel** **> Additional Properties >** enable the **Update Page On Change** property.
2. Also, set the **Update Delay (ms)**, which specifies the time interval after the user stops typing before the page refreshes its UI. For example, if the *Update Delay (ms)* value is set to 2000 ms (2 seconds), the page will update 2 seconds after the user stops typing. For this example, let's set it to 0 ms.
3. Now select the **Text** widget, move to the **Properties Panel > Set from Variable > Widget State > \[TextFieldName]**. Tip: You can also set the default value to be displayed until the user has entered any text.

> **Tip:** We advise setting the delay value if you make an API call that accepts the input from TextField.

##### Read only TextField

Sometimes you might want to restrict users from entering or updating anything into TextField and only allowed it if they are in edit mode. You can accomplish this by switching the **Read Only** property.

##### Change Cursor Color

In a form with many text fields, changing the cursor color for the currently focused field can help the user understand where their input will go when they start typing.

To change the cursor color, head over to **Properties Panel** **> Additional Properties >** change the **Cursor Color**.

![change-cursor-color](https://docs.flutterflow.io/assets/images/change-cursor-color-05f5660685d861eddeefade60a07d7ab.avif)

##### Changing Keyboard Type

When the keyboard opens by default, you can type any text. You might want user input in a certain format, such as a phone number, email address, website URL, etc. In this situation, you can choose a predefined keyboard type to present the appropriate key selections.

To change the keyboard type, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Keyboard Type** to the right one.

![keyboard-types](https://docs.flutterflow.io/assets/images/keyboard-types-e4a1beb8860678317acbb152580517c6.avif)

![changing-keyboard-type](https://docs.flutterflow.io/assets/images/changing-keyboard-type-7bcaa99496b93d0ca8b3165eb5c38544.avif)

##### Masking Input

You might want to allow users to provide input in a specific format. For example, if you want a date in a format like MM/DD/YYYY, where all input must be a number, and its length should not exceed eight digits. You can do so by formatting the user input using the specific mask.

To mask the user input, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Mask** dropdown to the one you need.

If the required format is not on the list, you can select **Custom** and specify the **Custom Mask**. The '#' sign represents the number, and 'A' represents a letter. Here are some examples of *Custom Masks*:

| Input                                          | Custom Mask         |
| ---------------------------------------------- | ------------------- |
| Credit card number (e.g., 3424 4353 5453 3535) | #### #### #### #### |
| Custom date (e.g., 12-Jan-2023)                | ##-AAA-####         |; ##### Filtering Input

You might want to restrict the type of characters that can be entered into a TextField. Let's say you are building an app that requires its employees to enter their employee ID when they clock in and out for their shifts. The employee ID consists of only letters and numbers, and the app should only allow these characters to be entered. You can do so by filtering the user input

To filter the user input, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Filter** dropdown to the one you need.

##### Validating Input

You can validate the TextField value by wrapping it inside the [Form](https://docs.flutterflow.io/resources/forms/form-validation) widget and adding the validation criteria.

> **Tip:** Filtering ensures that only the allowed characters or values are entered, whereas the validation checks the entire input data against certain criteria. Both techniques can be used together or independently to ensure the correctness of user input in a TextField widget.

##### Capitalization

You might want to control the capitalization of text when the user is typing, and also when the text is displayed. The Capitalization property allows you to specify how the text entered in the TextField should be capitalized.

This property accepts one of the following values:

* **None**: This value means that no capitalization should be applied to the text. All the characters will be displayed as they are typed.
* **Words**: This value capitalizes the first letter of each word in the text.
* **Sentences**: This value capitalizes the first letter of each sentence in the text.
* **Characters**: This value capitalizes every character in the text.

To set the capitalization, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Capitalization** dropdown to the one you need.

![capitalization](https://docs.flutterflow.io/assets/images/capitalization-882a7bdbe6b787328f3798af98637803.avif)

##### Submit Type

Showing a particular action on a keyboard can be useful in guiding users on what to do next. For example, if you have a search bar, you can display a "Search" button on the keyboard. When tapped, instead of moving to a new line or closing the keyboard, you can execute a search function. This can improve user experience by providing more intuitive keyboard actions based on the context of the input.

This property accepts one of the following values:

* **Done**: This closes the keyboard.
* **Next**: This moves focus to the next field.
* **Previous**: This moves focus to the previous field.
* **Send**: This represents the Send action.
* **Search**: This represents the Search action
* **Go**: This represents the Go action.

To set the submit type, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Submit Type** dropdown to the one you need.

![submit-type](https://docs.flutterflow.io/assets/images/submit-type-7b60ba6675f9b8ad3b637f0b56c950d7.avif)

##### Set Max Character Length

Sometimes, you might want to specify the maximum number of characters users can enter into the TextField. When the user types or pastes text into the field and reaches the specified character limit, they won't be able to input more characters, or the TextField will visually indicate that the limit has been reached.

For example, When users can leave comments or post messages (similar to 'tweet'), setting a maximum character length can help prevent spam or excessively lengthy responses.

To set the max character limit, select the TextField widget, move to the **Properties Panel** **> Additional Properties >** set the **Max Length** (number of characters you want to allow), and set the **Max Length Enforcement** to one of the following values:

* **Not Enforced**: This allows users to input extra characters and displays a warning when the limit is exceeded.
* **Enforced**: This always truncates any additional character once the limit is reached.

> **Info:** You can also hide the maximum character count by enabling the **Hide Max Length Counter** option.

#### Hiding Keyboard on Tap

Hiding the keyboard when the user taps outside of a TextField is a common user experience pattern that many apps use to improve usability. When the keyboard is open, it can obscure important information on the screen and make it difficult for the user to interact with other parts of the app.

Adding this behavior in your app can make it easier for these users to interact with other parts of the app without interference from the keyboard. It can also make your app feel more polished and professional.

To hide/close the keyboard, select the page, move the **Properties Panel >** enable the **Hide Keyboard on Tap**.

![Hide keyboard on tap](https://docs.flutterflow.io/assets/images/hide-keyboard-tap-2-845a510336fc3403e93e770c5a78ad8b.avif)

#### Focus Change Event

Sometimes, you may need to know whether a TextField is being used or not. For example, you can turn other parts of the app *on* or *off* depending on if the TextField is active. Also, you can start animations when someone starts or stops typing in the TextField.

Let's see an example of controlling the visibility of a Text widget based on the TextField's Focus state.

To do so:

1. On a Text widget, add a [Conditional Visibility](https://docs.flutterflow.io/resources/ui/widgets/widget-commonalities#conditional) based on the TextField's Focus state. You can access via **Set from Variable** menu **> Widget Focus State > \[TextField name]**.
2. Now, on a TextField widget, under the [On Focus Change](https://docs.flutterflow.io/resources/forms/textfield#trigger-action--listen-callback) callback, simply add an action to refresh the page by adding the update app state variable.

#### Trigger Action / Listen Callback

The TextField widget provides you with two types of actions (aka callbacks):

1. **On Submit**: Actions under this will be triggered when you finish entering the text in the TextField widget. i.e., pressing a done button inside the soft keyboard.
2. **On Change**: Actions under this will trigger when you enter or delete a character in the TextField widget.
3. **On Focus Change**: Actions under this will trigger when the focus state changes on a TextField. This means when users click on it to type or click away from it.

> **Warning:** Be careful about adding the actions under the **On Change**. Specifically, you should avoid adding any action that will take more time.

* On Submit
* On Change
* On Focus Change

To trigger an action:

1. Select the TextField widget from the widget tree or canvas area.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Select the **Type of Action** among the **On Submit, On Change,** and **On Focus Change**.
4. Now you can add any action here.

***

#### Video guide

If you prefer watching a video tutorial, here's the one for you:

---

### Action Blocks {#action-blocks}

*Learn how to use Action Blocks in your FlutterFlow app to and create reusable actions.*

**Source:** https://docs.flutterflow.io/resources/functions/action-blocks

An Action Block is a set of actions that perform a specific task and can be reused in different parts of the app. If you find yourself repeatedly performing a particular set of operations in your app, it may be helpful to create an Action Block. This allows you to break down complex actions into smaller, more manageable units, making them easier to understand and modify in the future.

Action Blocks have different scopes, which determine their availability:

| **Action Block Type**             | **Description**                                                                                                                                                                                                                                                     | **Scope**                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **App Level Action Blocks**       | Usable across the entire app. You can create an App Level Action Block from any page or component, and it will be accessible for viewing or editing from any page or component as well.                                                                             | Internally, an App Level Action Block can only access the state variables available in its scope (e.g., app state variables). |
| **Page Level Action Blocks**      | Restricted to the page in which they were created. These can access the state variables available in their scope, such as page state variables, as well as variables above their scope, such as [App State variables](https://docs.flutterflow.io/resources/data-representation/app-state). | Page Level Action Blocks can access page state variables and App State variables.                                             |
| **Component Level Action Blocks** | Restricted to the component in which they were created. These can access the state variables available in their scope, such as component state variables, as well as variables from higher scopes, like page and App State variables.                               | Component Level Action Blocks can access component state variables, page state variables, and App State variables.            |

Unsupported Actions in Action Blocks

Some actions are not supported and cannot be used in an Action Block. By default, these actions are hidden in the Action Block Editor. For example, actions under the **Firebase Authentication** category, **Start Periodic Action**, **Upload Data**, and others.

#### Action Blocks Structure

When creating an Action Block, the process of defining the flow is similar to **[defining Actions](https://docs.flutterflow.io/resources/functions/action-flow-editor#adding-an-action-example)**. The main difference is in choosing the scope and defining the input & output values of the Action Block.

##### Choosing the Scope of Action Block

As discussed, Action Blocks can be **App Level, Page Level**, or **Component Level**. App Level Action Blocks can be created from any widget's action properties throughout the app. However, Page Level or Component Level Action Blocks are only available in the Page or Component where they were created.

Usually, you will see a dropdown to choose between App Level, Page Level, or Component Level. Choose the scope based on your Action Block's use case.

![action-blocks.png](https://docs.flutterflow.io/assets/images/action-blocks-9d20367e001bf2a5d845ba072d3b36fc.png)

##### Action Parameters

Action Blocks have access to the state variables available in the same scope as the Action Block (for e.g., Page State variables can be accessed from Page Level Action Blocks). However, there will be times when you may need to input some parameters for the Action Block to perform its logic. These are called **Action Parameters**, and they can be added from the Action Flow Editor when you create a new Action.

For example, here is a small demo where we create an Action Block with an input parameter.

In this example, we add an item to the wishlist of an e-commerce app. Let's say our local wishlist is saved in an App State variable called `localWishlist`, and we have a reusable Action Block called `addToWishlist` that takes an input parameter called productId and performs the actions to add it to the `localWishlist` object.

##### Return Values

Often, your Action Block may return a value. For example, in our Product Cart Page, we have a reusable Component Level Action Block called `getTotalCost` that returns the final cost of all the products. You can define such an Action Block that returns a value (e.g., a double for this example) or a value related to your use case. You can define the return value in the Action Flow Editor. Let's see one example.

---

### Actions {#actions}

*Learn how to use the Action Flow Editor in your FlutterFlow app to manage and streamline your backend logic.*

**Source:** https://docs.flutterflow.io/resources/functions/action-flow-editor

Effectively managing user interactions is essential for developing interactive applications. Designing interactivity involves two steps:

1. Listening for Interaction (**Action Triggers**)
2. Responding to Interaction (**Actions**)

**Action Triggers** represent a specific event, while **Actions** are functions executed in response to the triggered event. Common triggers are:

* **On Tap**: Triggered on tapping on a widget or specifically buttons.
* **On Selected:** Triggered on selecting an option from a dropdown list.
* **On Page Load:** Triggered on loading a page

Actions are tasks or operations that are performed in response to an event detected by a trigger.

#### Action Flow Editor

The Action Flow Editor is a visual, node-based editor used to configure the functions that run in response to a trigger. This editor simplifies the process of creating and managing business logic.

![Action Flow Editor](https://docs.flutterflow.io/assets/images/actions-e960c2b3fcd71f75014ba419ffa23dc8.avif)

##### Action Triggers

When you open the Action Flow Editor, no triggers are added by default. To add a trigger, simply search for and select the desired one from the available options. The Action Triggers bar, located at the left of the editor, displays all added triggers.

> **Info:** To learn more about **Action Triggers** and its types, refer [**here**](https://docs.flutterflow.io/resources/functions/action-triggers).

Exposed by FlutterFlow

Please note that Action Triggers are exposed by FlutterFlow and are not user-generated. You can only work with the ones provided in the Action Flow Editor.

Each trigger has its own separate node-editor, allowing you to create distinct logic flows for different events. When you switch between triggers, the node-editor will update to display the logic specific to the selected trigger.

[Switching Triggers](https://demo.arcade.software/IazHon14tfvS4UljRsqu?embed\&show_copy_link=true)

> **Info:** It's important to note that the logic defined in the node-editor is associated with the selected trigger. This means that the actions you set up will only be executed when that particular trigger is activated.

##### Node Editor

This central area of the editor is where you define and visualize the logic/actions that will execute in response to the selected trigger. The actions are laid out in a flowchart-like manner, making it easy to understand and modify the flow of actions.

Actions in the Node Editor are executed synchronously. This means that if an action returns a value, it will be available to subsequent actions within the flow.

Synchronous vs Asynchronous

**Synchronous actions** are executed one after another, with each action waiting for the previous one to complete. **Asynchronous actions** are executed independently and can run concurrently, allowing other following tasks to proceed without waiting for them to finish.

##### Creating Action

If there is no initial action or if there is an action,and you want to add another one and press the plus icon, the following options will be available:

1. **Add Action**: Adds a single action node to the flow. You can add multiple synchronous actions one after another.

2. **Add Conditional Action**: Adds a conditional node with an input for a boolean expression and two action branches. The actions in each branch will be executed based on the evaluation of the boolean expression.

3. **Add Loop**: Adds a loop flow that contains an input boolean expression and an action flow. The actions within the loop will be executed repeatedly as long as the expression evaluates to true ( similar to a while loop).

4. **Add Parallel**: Adds two action flow branches that will be executed in parallel.

5. **Paste Action(s)**: Allows you to paste actions previously copied to the clipboard.

After creating an action node, you need to specify the action type in the Right Panel. Creating a node is equivalent to creating an empty function, and specifying the action type is like filling out the function body with the desired logic.

[Create New Action](https://demo.arcade.software/I9valjo4KqgEs8qol2Wp?embed\&show_copy_link=true)

##### Right Panel

The Right Panel serves two main purposes:

1. **Selecting Actions**: Choose the specific actions you want to add to your action flow.
2. **Configuring Actions**: Configure the properties, parameters, and return names of the selected action.

[Arcade Flow (Fri May 10 2024)](https://demo.arcade.software/oHXsShi0Kyo5hbOIYZL5?embed\&show_copy_link=true)

##### Widget Binding

In the Action Flow Editor, the icon in the upper left corner indicates the widget to which the current action flow is bound.

![Widget Binding](https://docs.flutterflow.io/assets/images/widget-binding-5e3c31a9a5e00772c04a2fc51ad6c67a.avif)

> **Info:** If you rename your widget, the new name will automatically be updated and associated with this action flow. This makes it easier to keep track of the logic associated with each widget, ensuring clarity and better organization of your action flows.

##### Issues

The bug icon will display warnings and errors in any of the action flows bound to this widget. Note, these are neither issues in the whole project nor issues in all of the action flow but *only* issues generated from the action flows bound to *this* widget. This includes *all* the action flows on *all* the triggers and not just currently visible action flow on the selected trigger.

![Issues](https://docs.flutterflow.io/assets/images/action-errors-3bd97539688a6e9a8ae102f8e5b74cf5.avif)

##### Action Blocks

The diamond icon in the Action Flow Editor opens a menu where you can create and edit Action Blocks. **Action Blocks** are reusable action flows that can accept parameters and return values, promoting code reusability and modularity.

![action-block.avif](https://docs.flutterflow.io/assets/images/action-block-icon-7f09cb4c8a36689a1503abee4a6057db.avif)

Deep Dive on Action Blocks

Learn more about different types of **[Action Blocks](https://docs.flutterflow.io/resources/functions/action-blocks)** and their scopes.

#### Adding an Action \[Example]

Here's a quick demo of how you can add an action or multiple sequential actions to a widget:

---

### Action Triggers {#action-triggers}

*Explore the action triggers available in FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/functions/action-triggers

**Action Triggers** represent specific events that occur when a user interacts with the app, such as tapping a button, selecting an option from a dropdown, or loading a new page. When an Action Trigger is invoked by one of these interactions, it initiates a corresponding **Action**—a task or operation that responds to the event.

In essence, Action Triggers are the '*listeners*' in your app, keeping an eye out for user interactions and signaling when it's time for your app to respond. By understanding and utilizing Action Triggers, you can craft a more dynamic and user-friendly application experience.

#### Types of Action Triggers

##### Page & Component Root Level Triggers

FlutterFlow provides several action triggers that allow you to respond to a page or component being initialized, or things like a key press event.

For more information on these triggers, see the [Page Actions & Lifecycle](https://docs.flutterflow.io/resources/ui/pages/page-lifecycle) and [Components Actions & Lifecycle](https://docs.flutterflow.io/resources/ui/components/component-lifecycle) pages.

##### Basic Triggers

FlutterFlow provides several basic action triggers that can be easily added:

* **On Tap**: This trigger is activated when a user taps on a widget. For instance, you can use this trigger to display a [Snackbar message](https://docs.flutterflow.io/resources/ui/pages/scaffold#snackbar) when a [button](https://docs.flutterflow.io/resources/ui/widgets/button) is tapped.
* **On Double Tap**: This trigger is activated when a user taps a widget twice quickly. A typical example might be zooming in on an image or photo when the user double-taps on it.
* **On Long Press**: This trigger is activated when a user presses and holds down on a widget for an extended period. A common use case is to show additional options or a context menu, such as allowing a user to delete or rename a file when long-pressing on it.

Here’s an example of showing a message on button click using the **On Tap** trigger:

##### Widget Specific Triggers

Certain widgets offer specific triggers that activate based on user interactions or device events. These triggers enable developers to define custom behaviors for various situations. Below are examples of widget-specific triggers:

* **On Submit**: Triggered on the TextField widget when the user presses "submit" or "done," finalizing text entry.
* **On Page Load**: Available on the page widget, this trigger activates as soon as the page loads, useful for tasks like data fetching or content updates.
* **On Phone Shake**: Specific to the page widget, this trigger responds to physical shaking of the device, commonly used in games for actions like rolling dice.
* **On Selected**: Found on widgets like Dropdowns, CheckboxGroups, Sliders, RadioButtons, ChoiceChips, and RatingBars, this trigger activates upon any change in selection.
* **On Page Swipe**: Available on the PageView widget to trigger actions when the page is swiped.
* **On Toggle**: Available on the ToggleIcon widget, this trigger responds each time the toggle is activated.
* **On Completed, On Change**: Specific to the PinCode widget, these triggers activate when the user completes or alters a pin entry.
* **On Count Changed**: Present in the CountController widget, this trigger responds to changes in the count.

#### Gesture Detector Triggers

Gesture Detector Triggers enable you to respond to user gestures, such as taps, drags, swipes, and pinches. These triggers are invoked based on specific gestures and allow you to add actions in response to user interactions. For example, the `onDoubleTap` trigger is invoked whenever a user quickly taps twice on a widget, which can be used to toggle a 'like' state or zoom in on content.

These triggers are accesible when you add an action onto a `Container`.

##### Lifecycle stages

The lifecycle of gesture triggers involves four key stages: **Start**, **Update**, **End/Stop**, and **Cancel**. These stages dictate how gestures are detected and handled, from the initial interaction to completion or cancellation. Understanding this lifecycle is crucial for building intuitive gesture-based interactions in your app.

###### Tap Gesture Lifecycle

Tap gestures have a simpler lifecycle, focusing primarily on detecting taps and whether they complete or get canceled. Here's how the tap lifecycle works:

1. **Down**: This stage begins when the user places their finger on the screen to initiate a tap. For example: `onTapDown` is triggered when the user touches the screen to start a tap.
2. **Up**: The tap gesture is completed when the user lifts their finger from the screen. For example: `onTapUp` is triggered when the user completes the tap by lifting their finger.
3. **Tap**: After both of the above actions are successfully completed, `onTap` is triggered indicating a full tap gesture has occurred.
4. **Cancel**: If the user moves their finger too much before lifting it, the tap is canceled, preventing the completion of the action. For example: `onTapCancel` will be called, and `onTap` will not be triggered.

Here’s how the lifecycle flows for tap gestures:

![tap-gesture-lifecycle](https://docs.flutterflow.io/assets/images/tap-gesture-lifecycle-aa2aabf02f7c37fef8fb5ba2381c11e3.avif)

###### Drag Gesture Lifecycle

Drag gestures are more complex, involving continuous tracking of movement across the screen. The drag lifecycle involves the following stages:

1. **Start**: This stage occurs when the user begins dragging their finger on the screen. For example: `onHorizontalDragStart` is triggered when a horizontal drag is initiated.
2. **Update**: During the drag, the gesture’s movement is tracked, allowing you to capture real-time data like the pointer's position or delta values. For example: `onHorizontalDragUpdate` is triggered as the user drags their finger, enabling the app to track the drag’s progress.
3. **End/Stop**: The drag gesture is completed when the user lifts their finger, finalizing the interaction. For example: `onHorizontalDragEnd` is triggered when the user finishes dragging and lifts their finger off the screen.
4. **Cancel**: If the drag gesture is interrupted before it completes (for instance, by another gesture), it will be canceled. For example: `onHorizontalDragCancel` is triggered if the drag is interrupted before finishing.

Here’s how the lifecycle flows for drag gestures:

![lifecycle-stage.avif](https://docs.flutterflow.io/assets/images/lifecycle-stage-fb3686571c89efb6d780be88eb80173f.avif)

##### Drag Gesture Cancellation

For drag gestures, lifecycle doesn't always strictly follow the sequence of **Start**, **Update**, **End/Stop**. The **Cancel** stage can occur at any point, even before **End/Stop**, depending on the interaction. This is different from tap gestures because a drag can be canceled after it has started or even while it is being updated.

For example, If a horizontal drag is interrupted before the drag completes (for example, if another gesture takes precedence), `onHorizontalDragCancel` is triggered instead of `onHorizontalDragEnd`.

![lifecycle-stage-cancel.avif](https://docs.flutterflow.io/assets/images/lifecycle-stage-cancel-0fb909588adf6847ef4ca5d046e680ed.avif)

##### Available Gesture Detector Triggers

Below is a complete list of available gesture detector triggers in FlutterFlow to enhance the capabilities of gesture-based interactions.

* **onDoubleTapCancel**: Triggered when a double-tap gesture is recognized but does not complete successfully.
* **onDoubleTapDown**: Triggered when the user presses down on the screen for the first tap in a double-tap sequence.
* **onForcePressEnd**: Triggered when the user releases a press that exceeds a certain force threshold.
* **onForcePressPeak**: Triggered when the force of a press reaches its peak.
* **onForcePressStart**: Triggered when the user begins pressing with enough force to pass a defined threshold.
* **onForcePressUpdate**: Triggered when the user changes the amount of pressure applied during a press.
* **onHorizontalDragCancel**: Triggered when a horizontal drag gesture is interrupted or canceled.
* **onHorizontalDragDown**: Triggered when the user first touches the screen and initiates a horizontal drag.
* **onHorizontalDragEnd**: Triggered when the user ends a horizontal drag gesture.
* **onHorizontalDragStart**: Triggered when the user begins a horizontal drag gesture.
* **onHorizontalDragUpdate**: Triggered continuously as the user drags horizontally.
* **onLongPressCancel**: Triggered when a long press gesture is recognized but doesn't complete.
* **onLongPressDown**: Triggered when the user first presses down on the screen with the intention of a long press.
* **onLongPressEnd**: Triggered when the user releases a long press.
* **onLongPressMoveUpdate**: Triggered as the user moves their finger while holding down during a long press.
* **onLongPressStart**: Triggered when the long press gesture starts after the user holds down for the required duration.
* **onLongPressUp**: Triggered when the user releases a long press after the hold duration.
* **onPanCancel**: Triggered when a pan gesture (general dragging) is interrupted or canceled.
* **onPanDown**: Triggered when the user first touches the screen with the intention of panning.
* **onPanEnd**: Triggered when the user ends a pan gesture.
* **onPanStart**: Triggered when the user begins a pan gesture.
* **onPanUpdate**: Triggered continuously as the user drags their finger across the screen.
* **onScaleEnd**: Triggered when the user ends a scaling gesture, such as pinch-to-zoom.
* **onScaleStart**: Triggered when the user begins a scaling gesture.
* **onScaleUpdate**: Triggered continuously as the user changes the scale (e.g., zooms in or out).
* **onSecondaryLongPress**: Triggered when the user presses and holds with a secondary pointer (e.g., two-finger press).
* **onSecondaryLongPressCancel**: Triggered when a secondary long press gesture is recognized but does not complete.
* **onSecondaryLongPressDown**: Triggered when the user first touches the screen with a secondary pointer intending to long press.
* **onSecondaryLongPressEnd**: Triggered when the user releases a secondary long press.
* **onSecondaryLongPressMoveUpdate**: Triggered as the user moves a secondary pointer while holding down during a long press.
* **onSecondaryLongPressStart**: Triggered when the secondary long press gesture starts after holding down for the required duration.
* **onSecondaryLongPressUp**: Triggered when the user releases a secondary long press after the hold duration.
* **onSecondaryTap**: Triggered when the user taps with a secondary pointer (e.g., two-finger tap).
* **onSecondaryTapCancel**: Triggered when a secondary tap gesture is recognized but does not complete.
* **onSecondaryTapDown**: Triggered when the user first touches the screen with a secondary pointer intending to tap.
* **onSecondaryTapUp**: Triggered when the user releases the screen after a secondary tap.
* **onTapCancel**: Triggered when a tap gesture is recognized but does not complete successfully.
* **onTapDown**: Triggered when the user first touches the screen with the intention of tapping.
* **onTapUp**: Triggered when the user releases the screen after a tap.
* **onTertiaryLongPress**: Triggered when the user presses and holds with a tertiary pointer (e.g., three-finger press).
* **onTertiaryLongPressCancel**: Triggered when a tertiary long press gesture is recognized but does not complete.
* **onTertiaryLongPressDown**: Triggered when the user first touches the screen with a tertiary pointer intending to long press.
* **onTertiaryLongPressEnd**: Triggered when the user releases a tertiary long press.
* **onTertiaryLongPressMoveUpdate**: Triggered as the user moves a tertiary pointer while holding down during a long press.
* **onTertiaryLongPressStart**: Triggered when the tertiary long press gesture starts after holding down for the required duration.
* **onTertiaryLongPressUp**: Triggered when the user releases a tertiary long press after the hold duration.
* **onTertiaryTapCancel**: Triggered when a tertiary tap gesture is recognized but does not complete successfully.
* **onTertiaryTapDown**: Triggered when the user first touches the screen with a tertiary pointer intending to tap.
* **onTertiaryTapUp**: Triggered when the user releases the screen after a tertiary tap.
* **onVerticalDragCancel**: Triggered when a vertical drag gesture is interrupted or canceled.
* **onVerticalDragDown**: Triggered when the user first touches the screen and initiates a vertical drag.
* **onVerticalDragEnd**: Triggered when the user ends a vertical drag gesture.
* **onVerticalDragStart**: Triggered when the user begins a vertical drag gesture.
* **onVerticalDragUpdate**: Triggered continuously as the user drags vertically.

##### Accessing Gesture Detector Data

Gesture detectors not only recognize types of gestures but also provide relevant data based on the trigger. For example, the exact location (XY coordinates) where a drag event occurs.

Examples of using gesture data include:

* **Custom Slider:** Use the coordinates to update the position of the thumb of a custom slider on its track.
* **Interactive Zoom:** Used the data provided by the scale gesture to appropriately zoom in or out.
* **Dynamic Interfaces:** Create effects that react to touch, like animations that start from where the user taps the screen.

You can access the Gesture Detector data after adding the relevant gesture detector triggers. Once added, you can retrieve this data via the **Set from Variable** menu inside the **Action Flow Editor**. Depending on your specific needs, you can choose from the following options:

* **Global Position X**: The x-coordinate of the pointer relative to the left edge of the screen when the gesture was triggered.
* **Global Position Y**: The y-coordinate of the pointer relative to the top edge of the screen when the gesture was triggered.
* **Local Position X**: The x-coordinate of the pointer relative to the left edge of the widget that has the action triggers applied.
* **Local Position Y**: The y-coordinate of the pointer relative to the top edge of the widget that has the action triggers applied.
* **Delta X**: The horizontal distance the pointer moved during the gesture.
* **Delta Y**: The vertical distance the pointer moved during the gesture.

![access-xy-data](https://docs.flutterflow.io/assets/images/access-xy-data-98437951d7a2304fb0a923c07529b3a3.png)

See how to effectively use gesture detector triggers and access XY data in the following example.

##### Example: Swipe to delete cart items

Let's walk through an example that demonstrates how to implement a "Swipe to Delete" feature for cart items **entirely** using Gesture Detectors. Here's a preview of how it works:

Here’s how you do it:

1. First, we create a variable called `offsetX` to track the horizontal drag distance of the cart item. Since the cart item is displayed in a **ListView** and is built as a reusable component, we'll define `offsetX` as a **component state variable**. This ensures that each cart item independently tracks its own drag position.

   ![component-state-variable.avif](https://docs.flutterflow.io/assets/images/component-state-variable-207381e4133bc82238588f7e9d023a32.avif)

2. Now, to make the item move as the user drags it, we add a **slide animation** (under **On Action Trigger**) to the Container that holds the item's layout. While configuring the animation, set the **Duration** to 0 and the **Final Position** to the `offsetX` variable. This ensures that the item follows the user's finger as they swipe.

   info

   We'll trigger this animation every time the user swipes by listening to the `onHorizontalDragUpdate` event (see how to do it in next step).

   ![add-animation.avif](https://docs.flutterflow.io/assets/images/add-animation-8edbaddf0a8a5d669e5638cf27824b18.avif)

3. On the main Container, we add the `onHorizontalDragUpdate` action trigger. This will called continuously as the user drags the item horizontally. On this event, we update the `offsetX` variable with the new position based on the swipe movement (using **Delta X** Data) and trigger the animation. This real-time update makes the item slide on the screen.

4. Now we need to check if the swipe meets the threshold to delete the item or reset the item's position back to its original location. For that, we add the `onHorizontalDragEnd` trigger. In the `onHorizontalDragEnd` trigger, we check if the `offsetX` value exceeds 100. If it does, we send the item index back to the page or component (via execute callback action) to delete the item from the list. If not, we reverse the slide animation. Lastly, we reset the `offsetX` value to 0 to ensure it's ready for the next interaction.

---

### Conditional Logic {#conditional-logic}

*Learn how to implement conditional logic in your FlutterFlow app to control the flow of actions or generate properties based on certain conditions.*

**Source:** https://docs.flutterflow.io/resources/functions/conditional-logic

Conditional logic is a fundamental concept in programming and software development. It involves making decisions in code based on certain conditions. This is achieved using conditional statements, which evaluate expressions to determine whether they are true or false. Depending on the result, different actions or outcomes are executed.

###### How Conditional Logic Works

* **Condition:** An expression that evaluates to either true or false.
* **True Path:** The set of actions to execute if the condition is true.
* **False Path:** The set of actions to execute if the condition is false.

![true-false.png](https://docs.flutterflow.io/assets/images/true-false-326377a00a7b1d4e0d107d516594f4cc.png)

#### Conditional Flows

Conditional flows enhance basic true-false logic by handling multiple conditions and executing specific actions based on those conditions. This is achieved through more complex flows, such as single conditions, multiple conditions (using AND/OR), and conditional values with If/Then/Else logic.

##### Single Condition

This flow allows you to define a condition based on the comparison of two values, which can be set manually or derived from variables. The condition will return **True** or **False**.

**Comparison Operators:**

* Equal To
* Not Equal To
* Less Than
* Greater Than
* Less Than Or Equal To
* Greater Than Or Equal To
* Is Set
* Is Not Set

![single-condition.png](https://docs.flutterflow.io/assets/images/single-condition-fc718d2facebe1cb7c2137da8dfe8770.png)

##### Multiple Conditions (AND/OR)

This flow lets you combine multiple single conditions using logical AND or OR operators. It is useful for more complex decision-making processes.

![multiple-condition.png](https://docs.flutterflow.io/assets/images/multiple-condition-8d10635d362ca8204fda8d0de7d56a19.png)

##### Conditional Value (If/Then/Else)

Conditional Value allows you to set a dynamic variable based on different conditions. For each condition, you can specify a value that will be assigned if the condition is true. A default value can be provided if none of the conditions are met.

See the example **[below](https://docs.flutterflow.io/resources/functions/conditional-logic#setting-widget-properties-with-conditional-logic).**

#### Setting Widget Properties with Conditional Logic

FlutterFlow allows you to dynamically set the properties of widgets based on conditional logic. Depending on the expected data type of the property, you can use a combination of conditional flows to achieve your desired logic.

Here's an example where we use Conditional Logic to determine the value of a Text widget:

If the `placePicker` widget state is set, then return the placePicker address string. Else, if the `defaultAddress` component parameter is set and not empty, then return that as a string. Otherwise, return a default address value.

#### Conditional Actions

When you need to execute actions based on specific conditions, you can do so in the Action Flow Editor. By combining simple single conditions or multiple conditions, you can create complex logical flows. These conditions can be configured as learned in the Setting Properties section, allowing your action flows to follow **True/False** logic or **If-Else, If-Else If-Else** structures.

Here's a quick demo to illustrate a simple Single Condition Action flow:

You can easily convert a single condition action flow into a multiple condition action flow by enabling the Multiple Conditions toggle. Here's how:

---

### Loops {#loops}

*Learn how to implement loops in your FlutterFlow app to iterate over data and perform repeated actions.*

**Source:** https://docs.flutterflow.io/resources/functions/loops

**Loops** in FlutterFlow allow you to perform repetitive tasks without writing complex code. This is useful when working with lists of data or when you want to repeat actions a certain number of times.

There are two types of loops supported in FlutterFlow:

#### While Condition Loops

A **While Condition** loop requires a condition. The actions within the loop will continue to trigger as long as the condition holds true. When the condition becomes false, the loop terminates, and the next actions in the workflow will trigger.

For example, you can use a While Condition loop to continuously check if a user is still within a geofenced area. As long as the condition `isUserInLocation == true` holds, the app might keep checking for updates or show a live indicator.

![loop-block.png](https://docs.flutterflow.io/assets/images/loop-block-fc90ec57a9d391e64cbcebc44df2a956.png)

#### Over List

This loop type lets you iterate over a list of items to perform actions for each item in the list.

For example, if you have a list of items in a shopping cart and want to calculate the total price or apply a discount to each item, you can use Over List to go through each product and perform a calculation for each one.

You can also customize how the loop iterates:

* **Start Index**: Where the loop starts (default is `0`).
* **End Index**: Where the loop ends (default is the length of the list).
* **Step Size**: Interval between each iteration (e.g., set to `2` to loop through every second item).
* **Reverse Order**: Enables the loop to iterate from the end of the list to the beginning (e.g., showing the latest messages first).

![loop-over-list.avif](https://docs.flutterflow.io/assets/images/loop-over-list-012eca6fedc40882eb110c201b83b898.avif)

Inside a loop, you can access the current item and its index. This gives you the ability to work with each item individually, such as displaying item-specific data and making calculations.

![access-item-inside-loop.avif](https://docs.flutterflow.io/assets/images/access-item-inside-loop-e97760677c5d140e18249dacb7b27078.avif)

Nested Loops

You can also add a loop inside another loop to handle related data structures. For example, looping through orders and then looping through each order’s line items.

#### Loop Breaks

AVOID an INFINITE LOOP

Be careful with loop actions, as they can cause your app to enter an infinite loop if the condition never becomes false. Always ensure that the condition will be met at some point so the loop can exit.

If the intended operation is completed before the condition becomes false, you must add a **Loop Break** action in your workflow to exit the loop.

**Loop Breaks** are statements used to exit a loop prematurely, before the loop's normal termination condition is met. They are typically used to stop the loop when a certain condition is satisfied, preventing unnecessary iterations and allowing the program to proceed to the next section of actions.

**Key Points:**

* **Purpose:** Exit the loop immediately when a specific condition is met.
* **Implementation:** Typically implemented with the "Add Break" node in Action Flow Editor.
* **Usage:** Commonly used to avoid infinite loops or to stop looping once a desired result is achieved.

![loop-block-return.png](https://docs.flutterflow.io/assets/images/loop-block-return-fc9222466eb9481890fbb79e2f5ef4dc.png)

---

### Utility Functions {#utility-functions}

*Learn about the built-in utility functions available in FlutterFlow to enhance your app's UI logic.*

**Source:** https://docs.flutterflow.io/resources/functions/utility

Utility functions are crucial for simplifying common tasks in app development, such as performing quick calculations, formatting data, and concatenating strings.

In FlutterFlow, you can effortlessly integrate these utility functions when setting variables to value sources. This allows you to simplify processes like calculations, data formatting, and text manipulation directly within the visual builder.

FlutterFlow has the following built-in functions:

* **Combine Text:** A built-in function that lets you concatenate strings, making it easy to join multiple text elements together seamlessly.

* **Inline Function:** This feature allows you to perform simple calculations and data manipulations quickly and efficiently.

#### Combine Text

Oftentimes, you will encounter scenarios where you need to show two variables in a single String or Text widget. For example, in our [Ecommerce Demo](https://bit.ly/ff-docs-demo-v2) app, we have a price object in the following format:

```

"price": {
"currency": "$",
"amount": 25.50
}
```

However, when displaying the data in the UI, we should combine both the currency value and amount, as they make sense only together.

In such cases, we can use the **Combine Text** built-in function available in all value sources that take a `String`. You can combine any number of *dynamic* and *static* variables together, even if they are not `Strings` themselves. In the end, the final value is always a String since it is set to a widget that only accepts `String` data types.

Here is a quick demo:

Combine Text vs RichText widget

The **Combine Text** built-in function only allows you to combine multiple values (dynamic or static) together, with the same text style applied to all of them. If you need to combine multiple String values with different text styles for each, consider using the **[RichText](https://docs.flutterflow.io/resources/ui/widgets/text#richtext-widget)** widget.

#### Inline Function (Code Expressions)

> **Info:** **Code Expressions** was renamed to **Inline Functions** starting from FlutterFlow 6.0 version.

Often times, you may need to quickly format data, convert a data type from one form to another, or perform a simple calculation before setting the variable to a data source, such as a widget value source.

Inline Function is a piece of code that combines operators, variables, and/or values to produce a result. It can be used for arithmetic and logical operations, among other tasks.

To add inline function, open the Set from Variable dialog wherever it's possible to set a dynamic value and choose the values that will be part of the inline function.

For example, we may want to quickly calculate the discount amount of a product where the discount is 18% of the MRP of the product. The expression would be `cost - (cost * discount)`.

> **Tip:** Looking for more power and flexibility? Use the new [**Custom Code Expression**](https://docs.flutterflow.io/resources/functions/utility#custom-code-expression). It’s a more advanced version of Inline Functions that lets you access FlutterFlow generated resources without passing them as arguments. You also get real-time autocomplete and inline error checking for faster, more accurate logic.

**Precedence of operations**

Inline Function for math operations follow typical precedence (e.g., multiplication/division before addition/subtraction), but parentheses can change the order.

In this case, the variables we need are `cost` and `discount`.

So, we create two arguments in the **Inline Function** dialog where they hold the value of `cost` and `discount`, assign the data type for each of the arguments, and define the return type of the final value. In this case, the return type is a `double` since it holds the **subtotal** amount.

Now you can write the inline function in the **Expression** field and click on **Check Errors** to see if the expression is valid. If it is valid, you will see the generated code for the same.

The arguments in a Inline Function can take the following properties:

| DataType | Supports Nullable | Supports List |
| -------- | ----------------- | ------------- |
| String   | ✅                | ✅            |
| Integer  | ✅                | ✅            |
| Double   | ✅                | ✅            |
| Boolean  | ✅                | ✅            |
| Colors   | ✅                | ✅            |

##### Common Examples

Here are some common expressions you can use for your business logic:

| Expression                         | Description                                             | Example                    | Return Type    |
| ---------------------------------- | ------------------------------------------------------- | -------------------------- | -------------- |
| `contains()`                       | Checks if a **string** contains a particular substring. | `text1.contains(text2)`    | `bool`         |
| `split()`                          | Splits a **string** into a list of substrings.          | `text.split(",")`          | `List<String>` |
| `toLowerCase()` or `toUpperCase()` | Converts all characters in a **string** to lowercase.   | `text.toLowerCase()`       | `String`       |
| `contains()`                       | Checks if a **list** contains a particular element.     | `fruits.contains("apple")` | `bool`         |
| `max()`                            | Returns the larger of two numbers.                      | `math.max(a, b)`           | `int`          |
| `toDouble()`                       | Converts the **integer** to a **Double**.               | `intValue.toDouble()`      | `double`       |
| `int.parse(s)`                     | Convert the **String** into an **integer.**             | `int.parse(stringValue)`   | `int`          |

#### Custom Code Expression

**Custom Code Expression** lets you write short Dart code directly in widget property fields and action flows in FlutterFlow. It’s a more powerful version of [**Inline Function**](https://docs.flutterflow.io/resources/functions/utility#inline-function-code-expressions), allowing you to directly access FlutterFlow generated classes, global variables, widget properties, parameters, and more without needing to manually pass them as inputs.

Custom Code Expressions also support real-time autocomplete, making it easy to discover available fields as you type. For example, when you type `FFAppState().`, it will suggest all available app state variables along with their types.

In addition, inline validation provides immediate feedback as you write, helping you catch syntax errors or invalid property references.

> **Info:** To use Custom Code Expression, you must have an active [**FlutterFlow paid plan**](https://www.flutterflow.io/pricing).

> **Tip:** * To explore what you can access within a Custom code expression, refer to the [**Common Examples**](https://docs.flutterflow.io/concepts/custom-code/common-examples) page.
* Press `^ + Space` (or `Ctrl + Space`) while typing to see suggestions for what you can access in your Custom code expression.
* You can access values inside custom structs. For example, you can use `FFAppState().localDeviceInfo.osVersion` if that field exists in your app state.
* To use Custom code expressions better, it's helpful to understand how FlutterFlow builds your project behind the scenes. You can check the [**State Management**](https://docs.flutterflow.io/generated-code/state-management) page and other **Generated Code** sections to learn how everything is set up.

Here are a couple of examples showing how to access App State and Page State within a Custom code expression:

* **App State Access:** For example, to check if dark mode is enabled using an App State variable:

  ```
  FFAppState().enableDarkMode ? 'Dark Mode On' : 'Light Mode Off'
  ```

  This accesses the global `enableDarkMode` boolean stored in `FFAppState`, and returns a string based on its value.

* **Page and Component State Access:** For example, to access a page or component state variable like `searchText`, you start with `_model.` and then select the variable from the autocomplete suggestions.

  ```
  _model.searchText.isEmpty ? '' : 'Searching for "${_model.searchText}"'
  ```

  This expression checks if the `searchText` variable (defined as a page state) is empty, and returns an appropriate message. The `_model` object refers to the current page’s generated state model.

Here's an example of adding a Custom Code Expression:

##### Execute Custom Code \[Action]

To use a Custom Code Expression when triggering actions in FlutterFlow (i.e., inside an Action Flow), you can use the **Execute Custom Code** action. This allows you to run a Dart expression when something happens, such as tapping a button or after a page loads.

![execute-custom-code.avif](https://docs.flutterflow.io/assets/images/execute-custom-code-bd07ca89bc8f62a23382545a6573949c.avif)

The Execute Custom Code action can be really helpful in scenarios where the home page is removed early from the navigation stack and standard navigation using the local context may fail. To prevent this, you can [use the global navigator context](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking#using-global-context-to-navigate) inside a code expression.

#### Custom Functions

You can also use custom functions to handle slightly more complex calculations or to process a wider range of data types that are not supported in Inline Function.

> **Info:** Learn more about [**Custom Functions**](https://docs.flutterflow.io/concepts/custom-code/custom-functions).

#### FAQS

How is a Custom Code Expression different from an Inline Function?

Custom Code Expression is a more advanced and flexible version of Inline Function.

With Inline Functions, you had to manually pass values as arguments. In contrast, Custom Code Expressions let you directly reference FlutterFlow generated resources (such as `FFAppState()`, `_model`, context, and more) without needing to pass them in.

You can write any valid Dart expression in a Custom code expression, even multi-line logic using anonymous functions. Plus, Custom Code Expressions support real-time autocomplete and inline error validation, making it much easier to discover available variables and avoid mistakes.

---

### Utility Actions {#utility-actions}

*Learn about the built-in utility Actions available in FlutterFlow to enhance your app's UI logic.*

**Source:** https://docs.flutterflow.io/resources/functions/utility-actions

Utility Actions provide essential functionalities that enhance your app's capabilities, such as data manipulation and system interactions. These actions streamline processes and improve the overall user experience. Examples include copying text to the clipboard and selecting colors or dates.

#### Color Picker \[Action]

Using this action, you can allow users to pick their favorite color from the palette or by entering a HEX/RGB color value. You might, for instance, utilize this to give customers the option of choosing the color of a product you offer.

When this action is triggered, it opens the color picker, where users can customize the color. The color picker will close once the desired color has been selected, and the selected color will then be accessible via *Widget State > Color Picked*.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Color Picker** (under *Widget/UI Interactions*) action.
4. When the color picker is opened, by default, the primary color is selected. To change this, set the **Initially Selected Color**.
5. You can also customize the look and feel of the color picker by changing the color of the **Text**, **Background**, and **Button**.
6. By default, the color picker allows users to add opacity to the color. To allow users only select the opaque colors, disable the **Allow Opacity** toggle.
7. Recent colors help users choose any previous color they have used. Disable the **Show Recent Color** toggle if you don't want to show them.
8. The selected color is now available at **Widget State > Color Picked**. You can access it from any widget's color property or click the "**+**" button and add the following action to update the selected color in your backend or app state.

> **Info:** After the user has selected the desired color, the picker will close automatically, and the selected color can then be accessed via the **Widget State > Color Picked**.

Here's an example of adding the color picker action and updating the selected color in an app state variable.

* Adding color picker action
* Customize color picker

![customize-color-picker](https://docs.flutterflow.io/assets/images/customize-color-picker-9a6db3757512a828ae5b86369eed4027.avif)

#### DateTime Picker \[Action]

This action allows the user to select a date and time. You could use it to schedule appointments, set a reminder for a specific date, choose travel dates and times, etc.

When this action is triggered, it opens the graphical calendar and clock interface that the user can interact with to select a specific date and time.

##### Types Date/Time Picker

You can choose to open the following types of *Date/Time* picker dialog:

* **Date**: Allows you to only select a date.
* **Date+Time**: Allows you to select the date followed by the time.
* **Time**: Allows you to only select a time.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Container, Button, etc.) on which you want to add the action.
2. Select **Actions** from the properties panel (the right menu), If it's the first action, click **+ Add Action** button. Otherwise, click the "**+**" button below the previous action tile (inside *Action Flow Editor*) and select **Add Action**.
3. Search and select the **Date/Time Picker** (under *Widget/UI Interactions*) action.
4. Set the [Date/Time picker type](https://docs.flutterflow.io/resources/functions/utility-actions#types-datetime-picker).
5. By default, the picker shows the current date/time. You can change this by adjusting the **Default Date/Time**.
6. To define the range of selectable dates, use the **Minimum Date/Time** and **Maximum Date/Time** properties. Click on **Unset** to specify your dates.
7. Control whether the past and future dates/times are selectable with **Allow Past Date/Time** and **Allow Future Date/Time**. **Tip**: If you explicitly set the min or max date, this option will be disabled.
8. For an iOS-style display, activate the **Use Cupertino-style** toggle.

![cupertino-style](https://docs.flutterflow.io/assets/images/cupertino-style-6cd132faee38015163a03a82e6406a29.png) 9. For more personalized styling, turn off **Use Default Theme** and tweak the settings in the **Appearance Properties** section.

![appearance-properties](https://docs.flutterflow.io/assets/images/appearance-properties-e452f129ea064da6443fb476b9a69f92.png)

> **Info:** After the user has selected the desired date and time, the picker will close automatically, and the selected date/time can then be accessed via the ***Widget State > Date Picked**.*

Here's an example of adding the date time picker action and displaying the value in a Text widget.

#### Biometric Verification \[Action]

Most modern devices come with biometric sensors to strengthen the device's security. Using this action, you can leverage on-device authentication such as fingerprint or face recognition to protect your app's privacy.

When this action triggers, it checks for the enrolled biometric. If it finds any, it asks users to verify their identity. If the biometric authentication fails, it opens up the screen lock option (e.g., Pattern, PIN, Password, Swipe, etc.) as a fallback method to authenticate users.

A common use case of this action is to allow only the intended user to open an app that involves financial or confidential information, such as an online payment app, stock trading app, or online storage app.

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to define the action.

2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.

3. Click on the **+ Add Action**.

4. On the right side, search and select the **Biometric Verification** (under *Utilities*) action. 1. By default, if the biometric verification fails, it opens the on-device credentials such as Pattern and PIN. This helps in a case where the biometric sensor can't recognize a valid fingerprint or face. However, you can disable this behavior and only allow biometric verification. To do so, turn on the **Allow biometric only** toggle.

   2. Enter the **Biometric Reason text**. This message is displayed inside the biometric recognition UI.

   3. Provide the **Action Output Variable Name**. The status of biometric verification, True (pass) or False(fail), is stored in this variable. You can use this variable to decide the following action. For example, showing a success or failure message.

   4. To show a success or failure message, **Add Conditional** action by clicking on the + button inside the already added action. 1. Click on the **UNSET**, select **Action Output**, and select the action output variable name.
      2. Under the **TRUE** section, add an action to [show the snackbar](https://docs.flutterflow.io/resources/ui/pages/scaffold#snackbar) with a success message.
      3. Similarly, add the failure message under the **FALSE** section.

#### Copy to Clipboard \[Action]

Using this action, you can allow users to copy a particular text from your app. For example, copying a message or transaction ID and then pasting it into another application.

When this action is triggered, the data is stored temporarily in a special part of the device's memory called the clipboard. The user can then paste the copied text into another application by using the "paste" command.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **Open**. This will open an **Action Flow Editor** in a new popup window.
3. Click on the **+ Add Action**.
4. Search and select the **Copy to Clipboard** (under *Utilities*) action.
5. Most probably, this value would be dynamic; hence, you can set the **Value Source** to **From Variable** and set the **Source** accordingly.

> **Warning:** At present, testing this action isn't possible in Test mode, but you can use the Run mode for this purpose.

#### Set Dark Mode Setting \[Action]

Using this Action, you can set the app theme to Light/Dark or set it as per the system.

* As Per System
* Manually Setting Theme Mode

##### Types of Dark Mode Setting

There are three types of the mode you can set:

* **From System**: Set the Light/Dark Mode based on system preference. That means you don't need to build the Light/Dark Mode switch UI in your app. The dark mode will be set automatically if a user has set the dark mode in the Android/iOS operating system.
* **Light Mode**: Set the theme mode to Light.
* **Dark Mode**: Set the theme mode to Dark.

Go to your project page on FlutterFlow and follow the steps below to define the Set Dark Mode Setting Action to any widget.

1. Select **Actions** from the [properties panel](https://docs.flutterflow.io/flutterflow-ui/builder#properties-panel) (the right menu)
2. Click **+ Add Action** button
3. Choose a gesture from the dropdown among **On Tap**, **On Double Tap**, or **On Long Press**.
4. Select the **Action Type** as **Set Dark Mode Setting**.
5. Set the **Setting Source** to **Select Setting**.
6. Set the **Dark Mode Setting** to any amongst the **From System**, **Light Mode**, **Dark Mode**.

#### Send Email \[Action]

Using this action, you can send an Email to the specified email Id. This action does not directly send an email. Instead, it redirects you to the email app and prefills the subject and message body, and you have to press the send button to send an email finally.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Send Email** (under *Share*) action.
4. Inside the **Email Address** section, provide the valid email id. Your message will be sent to this email Id.
5. Also, provide the **Subject** and **Body** of the message to be sent.

#### Call Number \[Action]

Using this action, you can make a call to the specified number. This action does not directly call a number. Instead, it redirects you to the native Calls app and prefills the specified number; you have to press the call button to make a call.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Call Number** (under *Share*) action.
4. Inside the **Phone Number** section, provide the valid phone number. The call will be made to this number.

#### Send SMS \[Action]

Using this action, you can send an SMS to the specified number. This action does not directly send SMS. Instead, it redirects you to the native SMS app and prefills your message, and you have to press the send button to send the message finally.

Follow the steps below to add this action to any widget.

1. Select the **Widget** (e.g., Button) on which you want to add the action.
2. Select **Actions** from the Properties panel (the right menu), and click **+ Add Action**.
3. Search and select the **Send SMS** (under *Share*) action.
4. Inside the **Phone Number** section, provide the valid phone number. Your message will be sent to this number.
5. Inside the **SMS Body** section, provide the message you want to send.

---

### What is a Project? {#what-is-a-project}

*Understand what constitutes a project in FlutterFlow and how to manage them effectively.*

**Source:** https://docs.flutterflow.io/resources/projects

A **Project** in FlutterFlow represents a complete Flutter application. It contains all the generated code for a Flutter app. This means that you can export your code and your app will run as a normal Flutter app without requiring FlutterFlow.

A FlutterFlow project includes all the files and packages generated by the `flutter create` command, along with additional packages specifically added to support common functionalities. These include:

##### UI and Styling

* [**auto\_size\_text**](https://pub.dev/packages/auto_size_text): Automatically resizes text to fit within its bounds.
* [**cached\_network\_image**](https://pub.dev/packages/cached_network_image): Provides a widget that displays images from the internet, caching them for performance.
* [**flutter\_animate**](https://pub.dev/packages/flutter_animate): Facilitates adding animations to widgets.
* [**font\_awesome\_flutter**](https://pub.dev/packages/font_awesome_flutter): Offers a comprehensive set of icons provided by FontAwesome.
* [**from\_css\_color**](https://pub.dev/packages/from_css_color): Converts CSS color strings to Flutter color objects.
* [**google\_fonts**](https://pub.dev/packages/google_fonts): Enables custom fonts to be used easily from the Google Fonts catalog.
* [**page\_transition**](https://pub.dev/packages/page_transition): Adds customizable page transition effects.

##### Navigation

* [**go\_router**](https://pub.dev/packages/go_router): A declarative router based on URL patterns, simplifying navigation logic.

##### Data Management and Storage

* [**collection**](https://pub.dev/packages/collection): Provides additional collection types and utilities.
* [**json\_path**](https://pub.dev/packages/json_path): Allows querying JSON data structures with path expressions.
* [**provider**](https://pub.dev/packages/provider): A popular state management technique to propagate changes across the app.
* [**shared\_preferences**](https://pub.dev/packages/shared_preferences): Facilitates persistent storage of simple data (key-value pairs).

##### Platform Specific Integrations

* [**path\_provider**](https://pub.dev/packages/path_provider): Locates commonly used locations on the filesystem.
* [**path\_provider\_android**](https://pub.dev/packages/path_provider_android), [**path\_provider\_foundation**](https://pub.dev/packages/path_provider_foundation), [**path\_provider\_platform\_interface**](https://pub.dev/packages/path_provider_platform_interface): Platform-specific implementations and interface for `path_provider`.
* [**shared\_preferences\_android**](https://pub.dev/packages/shared_preferences_android), [**shared\_preferences\_foundation**](https://pub.dev/packages/shared_preferences_foundation), [**shared\_preferences\_platform\_interface**](https://pub.dev/packages/shared_preferences_platform_interface), [**shared\_preferences\_web**](https://pub.dev/packages/shared_preferences_web): Platform-specific implementations for `shared_preferences`.
* [**url\_launcher**](https://pub.dev/packages/url_launcher), [**url\_launcher\_android**](https://pub.dev/packages/url_launcher_android), [**url\_launcher\_ios**](https://pub.dev/packages/url_launcher_ios), [**url\_launcher\_platform\_interface**](https://pub.dev/packages/url_launcher_platform_interface): Packages that enable launching URLs on various platforms, allowing the app to open web links, emails, and more.

##### Utilities

* [**intl**](https://pub.dev/packages/intl): Provides internationalization and localization facilities, including message translation, plurals and genders, and date/number formatting.
* [**flutter\_cache\_manager**](https://pub.dev/packages/flutter_cache_manager): Manages cached files, supporting custom file retrieval strategies and cache rules.
* [**timeago**](https://pub.dev/packages/timeago): A library to format dates as a relative time (e.g., "5 minutes ago").

Any elements (e.g. pages, widgets), business logic or packages that are added to the project will be included in the generated code.

Generated Code

FlutterFlow automatically generates a complete Flutter application for you. To dive deeper into the project structure of a Flutter app generated by FlutterFlow, explore the [**Directory Structure**](https://docs.flutterflow.io/generated-code/project-structure) guide.

---

### Collaborate on Projects {#collaborate-on-projects}

*Learn how to collaborate effectively on projects in FlutterFlow, including best practices for teamwork and project management.*

**Source:** https://docs.flutterflow.io/resources/projects/collaboration

In FlutterFlow you can share projects with your entire organization (team), with individual users within your organization, or external users.

#### Sharing a Project with Team

To share a project with team members, use the **Share with team** dropdown in the **Collaboration** page of your project's settings, and select how you want the project to be shared:

![share\_with\_team.png](https://docs.flutterflow.io/assets/images/share_with_team-d9300d604efe99f80fc07d46d2912eda.png)

* **Team project:** A project associated with your team and automatically visible to all team members. When a project is a Team Project, team members are automatically added as Editors. You can specifically designate team members as Viewers, but you cannot remove them.
* **Restricted team project:** A project associated with your team but only visible to specific team members who are added directly. After selecting this option, you’ll need to manually choose the team members you want to share the project with.
* **Personal project:** A project not associated with any team, where editing capabilities depend on the type of personal plan you have.

> **Info:** * The Team owner always has edit access to the project, regardless of who created or shared it, and retains full team plan capabilities.
* The Team owner can also selectively share the project with any number of team members.
* A [**Library**](https://docs.flutterflow.io/resources/projects/libraries) project will not have the *Restricted Team Project* option.
* Sharing a project with team members is only available on the **Growth** plan and **higher**. Check out our [**pricing**](https://www.flutterflow.io/pricing) section.

#### Sharing a Project with External Collaborators

You can invite users to your project who are not part of your organization. For instance, you might want to share your work with clients, stakeholders, or team members of the client.

You can add users as Read Only users to any project regardless of your pricing plan in the **Collaborators** page of your project's settings.

> **Info:** * Users with read-only access will only be able to access that specific project and won't be able to access any shared *Teams* libraries (e.g., custom code, design system).
* You must verify your email before inviting users.
* If a user isn't already a FlutterFlow user, we will send them an invite email. Their status will be shown as Pending until they create an account.

To add an external user as a collaborator as an Editor to a project, you first need to purchase a collaborator pass.

To purchase a collaborator pass, go to the [My Teams](https://app.flutterflow.io/team) page and, under the **Collaborator Passes** section, click **Add Pass** and complete the checkout process. Once the pass is created, enter the user email and select the project (Team Project or Restricted Team Project) you’d like to grant them access to.

> **Info:** * You must be a Team Owner to purchase and assign a Collaboration Pass.
* Collaborator Passes can only be assigned to users who have a paid plan (Basic, Growth, or Business).

#### Transferring Project

> **Danger:** This step can not be undone. If you want to regain project ownership, the new project owner will need to transfer ownership back to you.

To transfer ownership to another user, navigate to **Settings & Integrations > Project Setup > Collaboration > Project-Level Access**, click on the current role and select **Owner**.

> **Info:** You can transfer a project to any FlutterFlow user (including [external collaborators](https://docs.flutterflow.io/resources/projects/collaboration#sharing-a-project-with-external-collaborators)) as long as they have an active paid plan.

![transfer-ownership.avif](https://docs.flutterflow.io/assets/images/transfer-ownership-38bf5147ec948ecaffe2d643eb6d8970.avif)

#### Real-Time Collaboration

Real-Time Collaboration is a powerful feature that allows multiple builders to work together on the same project or, rather same page and design system simultaneously. With this, all builders can see the changes being made to the page as they happen and can also make their own changes to the page without interfering with the work of others.

This increases efficiency and productivity, as multiple builders can work on various aspects of the project or together on the same page at the same time.

When multiple builders are on the same page, it looks like this:

![real-time-collaboration.gif](https://docs.flutterflow.io/assets/images/real-time-collaboration-e7b2aa92a77ba20a8d27dc59722bcbae.gif)

> **Info:** Real-Time collaboration is only available on the **Growth** plan and **higher**. Check out our [**pricing**](https://www.flutterflow.io/pricing) section.

#### Project Activity

You can see a running history of changes made while building that helps you track progress and stay up to date on project changes.

> **Info:** Project Activity is only available to **Enterprise** users. Check out our [**pricing**](https://www.flutterflow.io/pricing) section.

![project-activity](https://docs.flutterflow.io/assets/images/project-activity-3d3eee4fef07cfaf66934cc1a76937e8.avif)

---

#

#### How to Create a Project

To create a new project, go to the Dashboard and click **+ New Project** in the upper-right corner. This opens a window where you can start with a template app or a blank project.

[Create a Project](https://demo.arcade.software/s8Pwq75FDwnaLyt6pQvZ?embed\&show_copy_link=true)

#### How to Find Projects

Go to the Project Dashboard to view all your projects. You can search for specific projects using the search bar.

[Projects - FlutterFlow](https://demo.arcade.software/GonI3mWkBe7xg98MvA0J?embed\&show_copy_link=true)

Narrow your search scope with the dropdown menu next to the search bar:

* **All Projects:** Shows all projects you can access.
* **My Private Projects:** Shows projects accessible only to you.
* **My Shared Projects:** Shows projects you own and have shared with others.
* **Shared With Me:** Shows projects shared with you that you do not own.
* **Team Projects:** Shows projects that belong to your teams.
* **Library Projects:** Shows projects configured as libraries for reuse across other projects.
* **Marketplace Listings:** Shows projects connected to your Marketplace listings.
* **Archived Projects:** Shows projects you have archived.
* **Beta Projects:** Shows projects using the Beta environment.
* **Prod Projects:** Shows projects using the Production environment.

![filter-projects](https://docs.flutterflow.io/assets/images/filter-projects-665e7c456b47e85db1d936f2c1243a32.avif)

#### Organizing Projects

##### Create and Add Tags to Projects

Tags help categorize and filter your projects for easier management.

To create a tag, click **+ Tag** or open the three-dot menu on a project card and select **Create Tag**.

Add a tag to a project by opening the three-dot menu on the project card and selecting a tag. Each project can have only one tag.

[Create and Add Tags to Projects](https://demo.arcade.software/ltenHF4tRtLi4zEX0QS4?embed\&show_copy_link=true)

##### Searching and Filtering by Tags

When a tag is selected, the project list filters to show only projects associated with that tag. This filter can be combined with the search bar to refine your project search further.

[Search and Filter Projects by Tag](https://demo.arcade.software/85XUoxRUK2ZxbWgBr95M?embed\&show_copy_link=true)

##### Editing and Removing Tags

Modify or remove tags by clicking the gear icon within the orange Tag button. This lets you quickly update tag names and assignments.

![edit-tags](https://docs.flutterflow.io/assets/images/edit-tags-a332d8bd24063d78cd99b8397ca832fa.avif)

---

### Create, Find, and Organize Projects {#create-find-and-organize-projects}

*Learn how to create, find, and organize projects in FlutterFlow to streamline your app development process.*

**Source:** https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects

_[Content could not be reliably extracted from the source export for this page. Please refer to the live page at https://docs.flutterflow.io/resources/projects/how-to-create-find-organize-projects.]_

### Run and Test Projects {#run-and-test-projects}

*Learn how to run and test projects in FlutterFlow to ensure your app functions correctly and meets your requirements.*

**Source:** https://docs.flutterflow.io/resources/projects/how-to-run-test-projects

There are 4 ways to test your project in FlutterFlow.

* **[Preview](https://docs.flutterflow.io/testing/run-your-app#preview-mode)**: This mode allows for quick testing of the user interface on a virtual device without requiring a full build.
* **[Test](https://docs.flutterflow.io/testing/run-your-app#test-mode)**: This mode runs a web version of your app with Flutter's "Hot Reload" feature, enabling you to visualize changes immediately.
* **[Run](https://docs.flutterflow.io/testing/run-your-app#run-mode)**: This mode allows for testing a fully functional version of your app with live data.
* **[Local Run](https://docs.flutterflow.io/testing/local-run)**: This feature, available in the FlutterFlow Desktop App, lets you test your app on an emulator or physical mobile device.

---

### Libraries {#libraries}

*Learn how to share and reuse entire FlutterFlow projects using libraries.*

**Source:** https://docs.flutterflow.io/resources/projects/libraries

Libraries enable you to share and reuse entire FlutterFlow projects as dependencies across multiple projects. This allows teams and developers to modularize their apps by creating shared libraries that include components, API calls, custom code, and more. By using libraries, development becomes more efficient and scalable.

> **Info:** A **Dependency** refers to an external library or resource that your project relies on to function correctly. When you create a new FlutterFlow project, certain dependencies are automatically added to support the generated code. Also, when you use a [**Custom Widget**](https://docs.flutterflow.io/concepts/custom-code/custom-widgets), you are essentially adding dependencies to your project. Libraries take this concept further by allowing you to add entire FlutterFlow projects as dependencies.

Imagine you're building an e-commerce app, and different teams are working on various features. One team develops a complex payment system. By using the Libraries, they can publish the payment system as a reusable library and allow other teams to easily import and integrate it into multiple projects without duplicating development efforts.

![libraries.avif](https://docs.flutterflow.io/assets/images/libraries-4e9c4d418929a4bbff1bef0c0df29fae.avif)

##### Importance of Libraries

Previously, FlutterFlow offered several methods to share resources between projects, such as team code libraries, design systems, API libraries, and by leveraging marketplace items. However, these methods had limitations, including the inability to share custom data types or custom functions alongside components or API calls and the absence of version control.

With Libraries, you can publish the complete FlutterFlow project as a library and import it as a dependency into other projects.

possible use cases

* **Modular Development**: Build large-scale apps by separating them into smaller, independently managed projects (e.g., UI library, backend integrations, etc.).
* **Team Collaboration**: Share reusable UI components, custom functions, or API integrations across multiple apps within a team.
* **Community Sharing**: Publish libraries that can be imported and reused by the broader FlutterFlow community.

#### Publishing a Library

To make the resources in your project available for others to use, publish your project as Library.

When you publish your project as a Library, your project will become a **Library Project**, and [certain features](https://docs.flutterflow.io/resources/projects/libraries#disabled-features-in-a-library) will no longer be available.

> **Note:** When you publish your project as Library, it can not be reverted. If you want to restore your project so that it is no longer a Library, you can clone the project. However, things like your deployment and Firestore settings will be cleared. If you want to preserve the state of your project before turning it into a Library, you should clone it first and then publish.

To publish a FlutterFlow project as a library, start by creating a FlutterFlow project as you normally would, then follow these steps:

[Publishing a Library](https://demo.arcade.software/CTuBPgISjpRWy5TT6rRD?embed\&show_copy_link=true)

> **Info:** * You can only publish libraries if you have access to [**branching**](https://docs.flutterflow.io/collaboration/branching), which is available to users on **Growth** plan and above.
* Libraries can only be published from the main branch, and each published version is linked to a specific commit, ensuring robust version control.
* You must commit your changes before publishing a new version of the library.
* It's recommended to include a message that tells users what has changed in the version your are publishing.

> **Warning:** To publish a project as a library, it must meet the following requirements:

* **No Prior Store Deployment**: The project must not have been deployed to the Google Play Store or Apple App Store.
* **No Failed Deployments**: The Publish button remains disabled if a deployment process was started and failed.
* **No Errors or Warnings**: All project errors or warnings must be addressed beforehand.
* **Main Branch Only**: You can only publish from the main branch.
* [**Paid Plan**](https://www.flutterflow.io/pricing): Subscription to one of the paid plans is required to publish a project as a Library.
* **Not Cloned from Marketplace**: The project cannot be a clone of a Marketplace item.

##### Disabled Features in a Library

When a project is converted into a library, the following features are disabled to ensure compatibility and functionality limitations:

* App settings * Supabase
  * Development environments
  * Authentication
  * Push notifications
  * Mobile deployment
  * Web deployment
  * Stripe
  * Braintree
  * Razorpay
  * Google Analytics
  * OneSignal
  * Mux

#### Importing a Library

To import a library project into another FlutterFlow project, you must go **Settings and Integrations** > **Project Setup** > **Project Dependencies** . Here you can specify the library project and version you are importing.

[Importing a Library](https://demo.arcade.software/DrzjKuhTWZXOxBB5yGJn?embed\&show_copy_link=true)

> **Info:** * You can only select a library if you have at least read access on the library project.
* For a library project to show in the drop down, you must be added as a collaborator on the project and the library project must have a published version.
* You can import publicly accessible libraries by specifying the project ID in the text field when adding a library dependency.
* By default, the latest published version of the library is imported, but you can choose to depend on an earlier version if needed.
* You can also import the `current` version of the library to use the latest state of the library on the main branch - however, this is not recommended.
* When importing a library into a project or another library, the library’s version must not be set to 'current' and should be less than or equal to the FlutterFlow version of the project or library it’s being imported into. Learn more about [**managing Library’s FlutterFlow version**](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#version-management-with-libraries).

##### Dependency Conflicts

A **Dependency Conflict** occurs when two or more libraries added by a project depend on different versions of the same dependency. This creates a situation where the project cannot resolve which version to use, leading to a project error.

![dependency-conflict.avif](https://docs.flutterflow.io/assets/images/dependency-conflict-68c1edda9693988f306551e329bff394.avif)

Let's say you are building an eCommerce app that uses multiple libraries for different purposes:

* **User Auth Library** is used for handling user authentication.
* **Payment Gateway Library** is used for managing the payment gateway.

Both library projects depend on a common library called **Components Library** but imports different versions respectively:

* **User Auth Library** depends on `Components Library v1.5.0`.
* **Payment Gateway Library** depends on `Components Library v2.0.0`.

In this scenario, the eCommerce project will detect the dependency conflict because it can't add both `v1.5.0` and `v2.0.0` of the Components Library at the same time.

###### Fixing Dependency Conflicts

Follow these steps to ensure both libraries rely on the same version of Components Library:

1. **Upgrade both libraries**: If updates are available, start by upgrading both the User Auth Library and Payment Gateway Library to their latest versions. Often, newer versions of libraries are designed to use the latest version of the Components Library, which can help resolve conflicts.
2. **Modify Libraries**: If you have access to the library projects, adjust the dependencies of either User Auth Library or Payment Gateway Library (or both) to use the same version of the Components Library.
3. **Contact Library Maintainers**: If you do not own the library yourself, reach out to the maintainers of the library projects. They may provide guidance, suggest workarounds, or release a version that addresses the conflict.

#### Access Library Resources

Once the library is imported, following resources are accessible for use:

* [Components](https://docs.flutterflow.io/resources/ui/components)
* [Data Types & Enums](https://docs.flutterflow.io/resources/data-representation/custom-data-types)
* [App State Variables](https://docs.flutterflow.io/resources/data-representation/app-state)
* [Constants](https://docs.flutterflow.io/resources/data-representation/constants)
* [API Calls](https://docs.flutterflow.io/resources/backend-logic/rest-api)
* [Action Blocks](https://docs.flutterflow.io/resources/functions/action-blocks)
* [Custom Functions](https://docs.flutterflow.io/concepts/custom-code/custom-functions), [Actions](https://docs.flutterflow.io/resources/functions/action-flow-editor), and [Widgets](https://docs.flutterflow.io/resources/ui/widgets)
* [Assets](https://docs.flutterflow.io/resources/projects/settings/general-settings#app-assets) (Note: These are not versioned)
* [Code Files](https://docs.flutterflow.io/concepts/custom-code/code-file)

> **Info:** * [**Pages**](https://docs.flutterflow.io/resources/ui/pages), [**Firestore Collections**](https://docs.flutterflow.io/integrations/database/cloud-firestore/creating-collections), and [**Cloud Functions**](https://docs.flutterflow.io/concepts/custom-code/cloud-functions) are still being worked on and may come in future updates.
* Creation of [**AI Agents**](https://docs.flutterflow.io/integrations/ai-agents) is not yet supported in the Library project

It's important to note that these resources show up where they are instantiated. For example:

* **Components** appear in the widget palette.
* **API calls** appear when making API calls in the action flow editor.
* **Custom Functions** are available when setting up actions or functions within the app.
* **Code Files** (Dart files containing classes or enums) become available when [creating instances](https://docs.flutterflow.io/concepts/custom-code/code-file#create-custom-class-instance), allowing you to access their fields and methods. They also appear in the action flow editor when adding [custom class actions](https://docs.flutterflow.io/concepts/custom-code/code-file#set-field-action).

This ensures that only relevant resources are shown where they are needed, optimizing performance and discoverability.

Access Library Components in Custom Code

When your project includes a library dependency, you can use its components—such as Library App State, Library Values, Library Custom Code resources, etc.—in your custom code. Explore the **[Common Custom Code Examples](https://docs.flutterflow.io/concepts/custom-code/common-examples#access-library-components-in-custom-code)** directory for reference.

![access-library-resources.avif](https://docs.flutterflow.io/assets/images/access-library-resources-6cdcb108936bad7eb864b8412170abe6.avif)

#### Library Versioning

Library versioning allows you to manage different versions of a library project over time. Using versioning, library users can control which version of a library to use in a project, ensuring compatibility and reducing the risk of breaking changes.

Importance of Library Versioning

* **Maintain Backward Compatibility**: It ensures older versions of the library continue to work as expected while introducing new features.
* **Roll Back Changes**: In case of bugs or issues in a new version, you can easily revert to a previous stable version.
* **Control Updates**: Library users can decide when to upgrade to the latest version, rather than being forced into changes.

##### Publish New Version

When you're ready to update your library, ensure that all modifications are committed to the main branch of the library project and then publish as per instructions [here](https://docs.flutterflow.io/resources/projects/libraries#publishing-a-library).

> **Tip:** * While publishing a new version, add a description to highlight what's new or changed in this version.
* Each time a new version is published, the version number will automatically increment.

##### Import Specific Version

When importing a library into a project, you have the flexibility to choose which version of the library to use. By default, the latest version will be selected.

![import-specific-library-version.avif](https://docs.flutterflow.io/assets/images/import-specific-library-version-3c6f3149e6ac482344617db9bada7cf6.avif)

##### Update to Latest Version

You can easily upgrade to newer versions of the libraries as they become available.

> **Tip:** * If a new update causes issues with your existing implementation, you also have the option to revert to a previous version.
* Always test your app after upgrading to ensure that the new library version works well with your existing project.

![update-library](https://docs.flutterflow.io/assets/images/update-library-4edeaa44ed91b4f37ecce0b86b1bac00.avif)

#### Library Pages

When you publish a library, all the pages included in the library become available for use in the consumer project. These pages function like any regular project page in your app; they support navigation, parameters, state management, and transitions.

Library Pages offers a modular approach to development, making it ideal for large teams and complex, multi-feature apps. For example, instead of recreating common flows like onboarding and payment flows, you can build them in a library once and use them wherever needed.

Possible Use Cases

* **Super Apps** like Gojek and Uber with distinct modules such as ride booking, shopping, and payments. Each module can be developed as a separate library and imported into a single main project.
* **Enterprise Apps** with isolated user journeys for different roles, such as admin and customer. Each role-based flow can be built as its own library and integrated into the core app as needed.
* **White-labeled Apps** that share common onboarding flows can benefit from libraries. The onboarding process can be built once as a library and reused across all branded versions of the app.

When users import or update the library, they can override the default route names to prevent conflicts between the library and their project. Library pages then appear in navigation actions just like any regular page.

##### Library Pages in NavBar

Library pages can also be used in the NavBar, allowing users to add reusable flows into the app’s primary navigation structure. For example, in a Super App, you can import ride booking, food delivery, or payment pages from separate libraries and add them directly to the bottom navigation, giving users quick access to each module.

> **Tip:** Want to learn more about building modular Super Apps using libraries? Check out our [**blog post**](https://blog.flutterflow.io/scaling-super-apps-modular-architecture-with-flutterflow-libraries/).

To display a library page on the NavBar, navigate to **Project Dependencies > FlutterFlow Libraries**, then click on **Pages** for the relevant library to open its details. In the list of pages, locate the desired page and click **Nav Bar Settings**, then enable **Show on NavBar**. You can also customize additional settings, such as label and icon, as needed.

To confirm, go to the **Nav Bar & App Bar** section, where you’ll see the library page listed as part of the NavBar items.

> **Info:** NavBar settings for regular pages are available directly within the Page Settings panel in the builder. However, for Library pages, these settings are managed through the Library Details dialog.

![NavBar-settings-for-regular-and-library-page](https://docs.flutterflow.io/assets/images/NavBar-settings-for-regular-and-library-page-967f2d0fbad3c9b44fc0eaca26d923ea.avif)

#### Library Values

**Library values** are essentially variables created and used by a library author and intended to have their values set by the library user. These values allow library author to create configurable variables that are useful in different contexts, such as public or client-side API keys, global settings, or other project-specific configurations. These values allow library users to input specific data required for the library to function properly in their project.

For example, if someone builds a payment gateway library, they might define Library Values for configuration settings, such as:

* Default currency: USD
* Region: US
* Default Payment method: Card

This allows the user importing the library to provide their own payment preferences without modifying the internal code of the library.

> **Danger:** **Library Values should not be used to store private or sensitive data**, such as secret API keys or credentials. These values are not currently designed to securely store or handle sensitive information.

The use of *client-side* or *publishable* API key is generally acceptable, because the keys often have limited permissions, rate limits, or are intended for public use. For instance, if someone creates a library that connects to a public weather API, they might define a Library Value for the API key. Users of that library can then input their own API key to make it work.

> **Tip:** To avoid misuse on any type credential, make sure to apply appropriate restrictions to limit its usage. For example, see how to [**restrict a Google Maps API key**](https://docs.flutterflow.io/best-practices/secure-api-keys#add-restrictions-to-your-api-key) in the Google Cloud Console.

##### Create Library Values as Author

The library author defines the variable name, data type (e.g., string, enum), whether the variable is nullable, and an optional default value.

To create library values, navigate to **Settings and Integrations > App Settings > Publish as Library > Library Values** section and click **+ Add Value**.

###### Use Library Values

After setting Library Values, they function just like any other variable in FlutterFlow. You can bind them to components, actions, API calls, or any property that allows you to configure dynamic values across your library project. You can access Library Values via the ****Set from Variable**** menu.

> **Tip:** Library values are used only within the library project and are not available for use in the project that imports it. The library user can only set their values.

![access-library-values](https://docs.flutterflow.io/assets/images/access-library-values-f087d40c48ba05c7809df5287da630b3.avif)

##### Set Library Values as User

To set library values, navigate to **Settings and Integrations > Project Setup > Project Dependencies** page. When you import a library, you'll be prompted to set values for required Library Values. If the library has already been added, click on **View Details**, which will open a dialog and then you can enter a value.

> **Tip:** For different [**development environments**](https://docs.flutterflow.io/testing/dev-environments) (e.g., development vs. production), you can bind Library Values to [**environment values**](https://docs.flutterflow.io/testing/dev-environments#environment-values). For instance, you could have two different Library Values for an API key, such as `DEV_OPENAI_API_KEY` and `PROD_OPENAI_API_KEY`, and bind them to the development and production environments to track API usage separately.

#### Libraries with Firebase

You can create collections and enable various Firebase features in library projects without connecting a separate Firebase project.

In library projects, you won’t see an option to link to a Firebase project. Instead, the project that imports the library handles the actual Firebase connection.

Any indexes or security rules defined in the library are recognized by the importing project and deployed accordingly.

Limitations

Libraries work with Firebase but have **some limitations**. The **Firebase Auth** and **Firebase Storage** are not directly supported in library projects at this time. If you need these features in your library’s functionality, you can include an action that accomplishes this task as a [**callback**](https://docs.flutterflow.io/resources/ui/components/callbacks).

If your team has multiple projects that share a common Firebase feature, turning it into a library is a great idea. This ensures the same logic is used and connects to the same Firestore project across all apps.

Here are some examples of library projects you can build with Firebase:

* **Basic Analytics or Tracking**: A library that logs events to Firestore; useful for aggregating usage data at an application level.
* **Configuration or Settings**: A library that serves app-wide configurations (like feature flags, UI themes, or layout choices) is handled in Firebase Remote Config.

#### FAQs

What will happen to existing team libraries?

Team code and API libraries will be migrated to library Projects. These projects will be imported as a library with the latest version specified as the version. The components within team design systems will move into their own projects, while design systems will continue to exist but only containing the theme settings.

Do libraries work with Marketplace?

Yes, you can add and import a Marketplace project as a library.

How do libraries work with themes (design systems)?

By default, the design system of the parent project takes precedence over the imported library's design system. If you want to use a library's design system, you must [**select or set the library in the Design System**](https://docs.flutterflow.io/concepts/design-system#adding-design-system) page.

How are API keys shared?

We're working on Library Values, which will allow users to set specific values when they import a library. This feature will be available soon.

How does nested dependencies work?

Projects can import libraries that themselves have imported other Libraries as dependencies. However, if the project and the library share the same dependency, the version must match exactly to avoid conflicts.

Why do I get collision errors when importing a duplicated project as a library?

When you duplicate a project and publish it as a library, the unique identifiers (keys) for components and other resources are not automatically changed. If you then import this library back into the original project, it causes key collisions between the original and duplicated resources.

To help with this, FlutterFlow shows a dialog that offers to automatically delete the original resources in your base project and update all references to point to the library versions.

If you prefer to resolve this manually, you can duplicate individual components within the library after importing, this will generate new keys and avoid the collision.

---

### Refactor Project {#refactor-project}

*Learn how to refactor your project in FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/projects/refactor-project

PLANS

Refactor Project is only available on the Paid Plans. Check our [**pricing plans**](https://flutterflow.io/pricing).

**Refactor Project** is a developer‑focused mode that opens your FlutterFlow project as a set of YAML files so you can perform large-scale edits in a single, consistent operation.

For example, if you want to use a custom data type from a Library and update all references, you don’t have to manually edit each page or component. With this mode enabled, you can update all references at once using a single refactor pass.

It makes managing large projects easier and more reliable. You can make changes across hundreds of references in just seconds, saving time and effort compared to manual edits. It also lets you preview changes and dismiss anything you don’t want to update.

possible use cases

* **Type Refactoring**: Rename a custom data type (e.g., `OrderDetails` → `OrderInfo`) across all bindings, forms, and logic in a single pass.
* **String Replacement**: Find and replace hardcoded (magic) strings like `"admin"`, `"true"`, or `"completed"` to improve clarity and maintainability.
* **Library Migration**: Replace a project-based custom data type (e.g., `UserProfile`) with its Library counterpart throughout the app without manually editing each reference.
* **Key Updates**: Update outdated keys—for example, replace all instances of `old_api_key` with the new `new_api_key` value.
* **Cleanup Unused Items**: Locate and remove unused fields or stale references (e.g., `oldFieldName`) from your YAML files to keep your project clean.

> **Info:** You can refactor the project only if you're on a [**paid plan**](https://www.flutterflow.io/pricing).

To refactor a project, go to **Toolbar > Developer Menu > Refactor Project**. You’ll need to commit any unsaved changes before entering the refactor view. This opens your project in a YAML-based editor, where you can search, edit, and replace values across multiple files.

You can also use **key reference** search by toggling the **key** icon—currently supported for data types, enums, pages, and components. Changes are color-coded: added lines appear in green, and removed lines appear in red. As you make changes, FlutterFlow provides inline YAML validation to help you catch and fix issues in real time.

When you're done, click **Commit** to save the changes. After that, test your app to make sure all widgets, actions, and bindings still work as expected.

> **Tip:** You can exclude any item from the replacement by right-clicking on it and selecting **Dismiss**.

---

### Pinning Projects to Stable FlutterFlow Versions {#pinning-projects-to-stable-flutterflow-versions}

*Learn how to manage the FlutterFlow version used for your project.*

**Source:** https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management

FlutterFlow is constantly evolving to provide new features, address bugs, and keep up-to-date with Flutter and third-party packages. However, frequent updates can introduce unwanted changes that break existing projects—especially those that rely on custom code with external dependencies.

To mitigate these issues, FlutterFlow offers a **version management** system that allows you to pin your project to a particular [*stable release*](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#stable-release) of FlutterFlow. Projects pinned to a stable release will **not automatically receive the latest FlutterFlow updates**, giving you more control over your development workflow.

However, pinning to a stable release means that you will not be able to use the latest features, and there may be bugs that are not fixed until subsequent releases. **We only recommend doing this if you have a complex app with custom code dependencies.**

> **Info:** Currently, the ability to pin a FlutterFlow project to a stable version is only available to **Enterprise** users.

#### When should you pin your project to a stable version?

Pinning your project to a stable version of FlutterFlow offers the following benefits:

* **Prevents Unexpected Breakages:** FlutterFlow updates can introduce errors into your project—particularly when you have custom code. Pinning to a stable release reduces the risk of unexpected changes to your project.
* **Gives Control Over Update Timing:** FlutterFlow updates might occur at inopportune times (e.g. right before you plan to release a new version of your application). Pinning your project to a stable version allows you to choose **when** to move your project to a newer release.

#### Key Concepts

To understand FlutterFlow's version management system, it's important to understand **Semantic Versioning**.

FlutterFlow tends to release a new version of the product each week. When a new version is released, the overall version number is incremented.

The version number consists of three parts:

* **Major Version:** Incremented when introducing substantial changes that significantly alter the product.
* **Minor Version:** Incremented for changes that notably enhance or modify the FlutterFlow development experience—such as upgrading to a new Flutter version, making substantial modifications to generated code or project structure, or introducing major new features.
* **Patch Version:** Incremented with routine releases that include bug fixes and minor improvements, ensuring stability without introducing breaking changes to the generated code or project structure.

![semantic\_versioning](https://docs.flutterflow.io/assets/images/semantic-versioning-3f848e936e19cadc1ed2794d526f90a6.png)

You can see what version of FlutterFlow you are using by looking at the top left hand corner of the builder.

![version-in-builder](https://docs.flutterflow.io/assets/images/version-in-builder-71d2a435efdc7c2bf6b31f4fdb98aa4c.png)

###### Standard Release

A **Standard Release** of FlutterFlow is released approximately every week. However, this is subject to change based on user needs.

When your project is **not pinned** to a stable release (default behavior), you will automatically use the **latest standard release.**

###### Stable Release

A **Stable Release** of FlutterFlow is published monthly if any of the following conditions are met:

* Significant changes have been made to project code generation.
* The underlying Flutter version or Pubspec dependencies in generated projects have been updated.
* Updates affecting the project structure have been introduced (e.g., the addition of a new widget type).

Each stable release is assigned a unique **Major.Minor** version number. Projects that have not been edited in a FlutterFlow version with a **Major.Minor** version higher than the stable release can be pinned to that stable version.

> **Note:** Each stable release will be supported for **6 months** before you are forced to upgrade to the next stable version.

#### Pinning Your Project

To pin your project, navigate to **Settings and Integrations > General > App Details >Version Pinning** section and select the stable release you want to lock into.

![pin-version](https://docs.flutterflow.io/assets/images/pin-version-cdb7d124a32829412c61bf793850b532.avif)

##### Modifying the Pinned Version

You have several options when it comes to modifying pinned version of your project:

* **Upgrade to more recent Stable Version**: When a new stable version is released, you will see it as an option in the dropdown shown above. You can upgrade the pinned version to a more recent stable version whenever it becomes available. Newer stable versions will have higher numbers (i.e., 5.1 is newer than 5.0)
* **Set to *Latest Version* (Unpinned):** You can unpin your project by setting it to the *Latest Version* which will use the latest [standard release](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#standard-release).
* **Opt-in to the *Next Stable*:** Your project may be on a standard version that does not have a corresponding stable version (i.e., you are on 5.0.1 but the 5.0 stable will correspond to 5.0.4). In that case, you can choose to opt-in to the *Next Stable Version*. If it is already available, it will be pinned to that version immediately.

Pinning and Unpinning Cannot Be Reversed

Once you unpin a project or pin it to a later version, this action cannot be undone. If you're unsure whether a newer FlutterFlow version will be compatible with your project, we recommend creating a new branch and updating the pinned version within that branch first. This allows you to preview changes before applying them to your main project.

##### Accessing the Proper Stable Version

As mentioned above, once you update your project to a stable version, you can only edit the project using that version of FlutterFlow.

* **For Web**: You will be automatically redirected to the URL for the stable version that your project is pinned to when you open a project from the FlutterFlow dashboard (i.e., navigating to app.flutterflow\.io or enterprise-\[region].flutterflow\.io).
* **For Desktop**: You will [**install**](https://www.flutterflow.io/desktop) the dedicated desktop application for the pinned stable release. The desktop app for stable releases won’t auto-update, you will need to install a new version when you upgrade your project to a new stable version.

#### Recommended FlutterFlow Version Workflow

If you have a complex app with custom code that depends on specific versions of package dependencies, it may be helpful to pin your project to a specific version. This is the workflow we recommend for managing the version of your projects.

1. If you think your project should be pinned to a stable release, choose to [pin a currently available stable version (if any)](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#modifying-the-pinned-version).
2. When a new stable version is released, you can choose when you would like to upgrade based on your own release schedule and development process. For instance, you might wait until you're not actively developing a new feature, or you could check the release notes first to see if there are must-have features that would prompt you to upgrade sooner.
3. When you’re ready to upgrade, commit all your changes on main to save your progress. Create a new branch from the main branch, [update the pinned version](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#modifying-the-pinned-version), and test all functionalities to ensure compatibility. If any modifications are needed, make those changes in the new branch.
4. Run your app on the platforms you support—using a simulator, emulator, or physical device to ensure everything works as intended. See the [Local Run documentation](https://docs.flutterflow.io/testing/local-run/) for details.
5. If everything looks good, you can merge the new branch into the main branch. However, to merge branches successfully, ensure that both the main branch and the new branch are pinned to the same FlutterFlow version! If for some reason your app is not working as expected, you can choose to leave or close the branch until you are ready to make the modifications needed to support the latest FlutterFlow version (i.e. upgrade dependencies/custom code).

> **Tip:** See the video [**here**](https://youtu.be/8Y1uyCC_dXE) for guidance on updating [**dependencies**](https://docs.flutterflow.io/concepts/custom-code#manage-dependencies).

#### Version Management with Libraries

[Libraries](https://docs.flutterflow.io/resources/projects/libraries) have their own versions. Like projects, libraries edited in FlutterFlow can only be used in FlutterFlow versions greater than or equal to the version it was last edited in.

To ensure that new versions of libraries used in a pinned project are compatible with a pinned project, we recommend pinning all libraries used in a pinned project to the same (or lower) Flutterflow version as the pinned project.

Library projects can also be pinned to a specific version, ensuring that all library versions use that FlutterFlow release until the pinned version is changed.

> **Info:** * Pinned projects cannot add a library with the version set to 'current' or to a library version that has been edited on a later release of FlutterFlow.

* Projects cannot be pinned if they contain a library with the version set to 'current' or to a library version that has been edited on a later release of FlutterFlow.

> **Tip:** When you import a library into a project or another library, the library’s version must be lower than or equal to the version used for the project it’s being imported into; otherwise, you will encounter an error.

#### FAQs

Can I edit my project in multiple versions of FlutterFlow?

No. If your project is not pinned to a specific version, you’ll always use the latest FlutterFlow release. If your project is pinned to a specific version of FlutterFlow, you will be prompted to edit the project in that version.

How often are new stable versions released?

We aim to release new stable versions of FlutterFlow approximately once a month.

How can I see what's included in a new stable version?

We’re currently working on displaying release notes directly in the product, so you can easily review what’s been added or changed in each new stable version.

What if there are bugs in the FlutterFlow version I’m using?

If critical bugs arise, we may provide hotfixes or patches for older FlutterFlow versions. However, some fixes depend on updating the underlying Flutter framework or related dependencies, which isn’t always feasible for older versions. This is a risk of staying on an older version of FlutterFlow as opposed to always using the latest.

Can I change the pinned version to be different for various branches in my project?

Yes, you can pin different versions for different branches. We recommend first creating a new branch, updating it to a later version, making any necessary changes, and verifying that everything works as expected before merging it into your main branch.

However, to merge branches successfully, ensure that both the main branch and the new branch are pinned to the same FlutterFlow version.

What happens if there is no stable version available for me to pin my project to?

If your project was created and edited on a [standard release](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#standard-release) that does not correspond to a [stable version](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#stable-release), you may not see a stable version available. Instead, you can choose to opt-in to the [*next stable release*](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management#pinning-your-project). If set to the next stable release, a project will immediately be pinned when opened when a new stable release becomes available.

What is the recommended approach if I have multiple projects and libraries that I am working on?

If you choose to pin your project to a stable version of FlutterFlow, we recommend pinning all your projects and dependencies to the same version - and trying to upgrade all projects to the next version around the same time. This makes it easier to ensure compatibilities between projects and libraries that depend on each other. Additionally, this makes it easier to have a single FlutterFlow desktop environment that you are working within.

---

### General Settings {#general-settings}

*Learn how to configure general settings for your FlutterFlow app.*

**Source:** https://docs.flutterflow.io/resources/projects/settings/general-settings

General Settings serve as the control center for configuring essential aspects of your app.

#### App Details

Edit the metadata and app-level settings for your project.

* **Project Name**: The name of your FlutterFlow project. This is the name shown inside FlutterFlow.
* **Project Description**: Optional internal notes about the project. Use this to describe the app, its purpose, or any context that helps collaborators understand the project.

##### App Names

Use **App Names** to configure the package and display names for each environment.

* **Current Environment**: Select the environment you want to configure, such as **Production**, **Staging**, or **Development**.
* **Package Name**: The unique package or bundle identifier for your app. You can define different package names for different environments.
* **Display Name**: The name shown to users on the installed app and in stores such as the App Store and Play Store.

> **Tip:** After changing the package name, errors may appear on the toolbar due to invalidated Firebase config files. To resolve this, generate new config files by going to **Settings & Integrations > Project Setup > Firebase > Regenerate Config Files**.

##### Pinned FlutterFlow Version

Use this section to pin the project to a specific FlutterFlow version or keep it on the **Latest Version (Unpinned)**. Pinning can help protect complex projects from unexpected changes caused by platform updates.

For more details, see [Pinning Projects to Stable FlutterFlow Versions](https://docs.flutterflow.io/resources/projects/settings/flutterflow-version-management).

> **Warning:** Once pinned, upgrading the FlutterFlow version may introduce breaking changes that could cause errors in your project. If needed, you can revert to the previous version, but any changes made to the project after upgrading will be lost.

##### Initial Page

You can specify your app's **Entry Page** and **Logged In Page** from this section.

* **Entry Page**: The Entry Page is the first page users see when they open your app. When authentication is disabled, all users are directed to this page by default. If authentication is enabled, this page becomes the login, signup, or onboarding page for users who are not authenticated.
* **Logged In Page** (*available only if auth is enabled*): This page is displayed when the app starts for authenticated users. If a user successfully signs in, they are automatically redirected to the page specified here. If the user is already authenticated, this page bypasses the Entry Page.

To set the page, choose the page you want to use from the dropdown menu.

![initial-page](https://docs.flutterflow.io/assets/images/initial-page-d9f36f9a9e089c4010558d95d327adfb.avif)

##### Download Settings

* **Run "dart fix"**: Enabling this runs the `dart fix` command when downloading the code. This makes the generated code cleaner and potentially more performant.
* **Download Unused Project Assets**: Enable this option to download all assets, including those that are not currently used in the project. This is useful when you need to access and use the assets in custom code or other parts of your project.

##### Routing & Deep Linking

Configure global navigation and deep linking settings for your app.

* **Override Default Transition**: Enable this to set a default page transition that applies across the app unless a page or action overrides it.
* **Pages Require Authentication by Default**: Enable this to require authentication for pages by default. You can still configure page-level access as needed.
* **Use Firebase Dynamic Links**: Enable this if your project still relies on Firebase Dynamic Links. If you are setting up deep links for a new project, see the [Deep & Dynamic Linking](https://docs.flutterflow.io/concepts/navigation/deep-dynamic-linking) guide.
* **URL Scheme**: Defines the scheme and domain values used for deep links. Keep these values unique to your app and aligned with your configured domain.
* **Advanced Route Settings**: Opens additional routing options for configuring app navigation behavior.

##### Display Settings

The **Display Settings** section allows you to configure how text scales within your app. This is particularly helpful for accessibility, ensuring that users with visual impairments can comfortably read content.

* **Min Text Scaling Factor**: Defines the minimum allowable scale for text. This prevents text from shrinking below a certain threshold, helping maintain legibility for all users. For example, setting this to `1` ensures text is never rendered smaller than its base size, regardless of device settings or user preferences.
* **Max Text Scaling Factor**: Defines the maximum allowable scale for text. This limits how large text can appear, which is useful for preserving layout consistency on devices with accessibility text scaling enabled. For example, setting this to `10` allows text to scale up to 10× its original size.
* **Persist Text Scaling Factor**: When enabled, the current text scaling factor will be stored and applied even after the app is restarted. This ensures a consistent user experience across sessions. This setting requires both **Min** and **Max Text Scaling Factors** to be set. If either is unset, persistence will have no effect.

> **Info:** Once the text scaling factors are set, you can use the [**Update Text Scaling Factor**](https://docs.flutterflow.io/concepts/accessibility#update-text-scaling-factor-action) action to let users dynamically adjust text size.

For example, suppose the Min Text Scaling Factor is set to 1.0 and the Max Text Scaling Factor is set to 5.0. If a user's device requests a scaling factor of 2.5, FlutterFlow will accept it because it falls within the allowed range. So, if the base font size is 16.0, the final rendered size would be: `2.5 × 16.0 = 40.0`

If a device requests a scaling factor higher than 5.0 (such as 6.0), it will be capped at 5.0. Thus, for a base font size of 16.0, the final rendered size will be: `5.0 × 16.0 = 80.0`.

Similarly, if a device requests a scaling factor below 1.0 (for example, 0.5), it will be raised to 1.0 to ensure readability. The resulting font size would remain: `1.0 × 16.0 = 16.0`.

##### UI Settings

* **Show Component Preview in Palette**: Enable this to show component previews in the Widget Palette. This helps you identify reusable components visually while building.

#### App Assets

Use App Assets to upload images for your splash screen and app launcher icon.

##### Splash

Splash screens are the first thing users see when your app starts up. They give the app time to get ready while showing users your branding or loading experience. This screen typically contains the image or logo of the app.

To configure the splash screen:

1. Navigate to **Settings and Integrations** from the Navigation Menu > **General** section > **App Assets**.

2. Under the **Splash** section, click **Upload Image** and upload the image you would like to display on the splash screen.

3. You can try any of the **Image Fit** options to determine how the uploaded image should display on the splash screen.

4. To control the image dimensions manually, you can set the **width** and **height** properties.

   * To set an **exact size**, select **PX** and enter the desired values.
   * To set the dimensions as a **% of the screen size**, select **%** and enter the desired value.

5. The **Min Duration** property helps you set how long the splash screen will be visible. For reference, 1000 ms equals 1 second.

6. You can also set a **Background Color** to match the background of the image.

7. In mobile apps, you might occasionally notice a blank white screen briefly appearing (as the Flutter engine loads) before the splash screen is displayed. To change the color of this screen, use the **Pre-loading** Color property.

8. Typically, web apps don't use a splash screen, so if you prefer a more traditional web experience, you can choose to **Disable for Web**.

![splash-image](https://docs.flutterflow.io/assets/images/splash-image-a40ac0d29201d04fe452038c3b038623.avif)

##### Launcher Icon

The launcher icon, also known as the app icon, represents your application on a user's device. The image asset you upload here is used as the app launcher icon.

To add the app launcher icon:

1. Click **Settings and Integrations** from the Navigation Menu.

2. Under the **General** section, select **App Assets**.

3. Under the **Launcher Icon** section, click **Upload Image**.

4. Use the **Unset** dropdown menu to select from images already uploaded to Project Media/Assets.

5. [Download the project](https://docs.flutterflow.io/flutterflow-cli/exporting) and run the following command in your terminal to generate the launcher icon:

   `flutter pub run flutter_launcher_icons:main`

6. [Run your app](https://docs.flutterflow.io/testing/run-your-app) on a real device or emulator to see the app launcher icon.

##### Android Adaptive Icon

[Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) let app icons adapt to different device environments. Unlike traditional launcher icons, adaptive icons are designed to scale and display well across different devices. Adaptive icons consist of two layers:

1. **Foreground layer**: This layer usually contains the logo or main visual element of the icon.
2. **Background layer**: This provides a fill (color or background image) behind the foreground, which can be manipulated by the device’s software.

Here are the steps to add adaptive icons:

1. [Create an adaptive icon](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons). You can either use this [online tool](https://icon.kitchen/) or use these [resources](https://docs.flutterflow.io/resources/projects/settings/general-settings#create-adaptive-icon) to create one.

2. Return to FlutterFlow and navigate to **Settings and Integrations > General** > **App Assets > Android Adaptive Icon.**

   1. Upload the **Foreground Icon**. If you use the online tool, you'll find it inside the `IconKitchen-Output > android > res > mipmap-xxxhdpi > ic_launcher_foreground.png`.
   2. For **Background Type**, you can either set the **Color** or **Image**. Use a color that aligns with your app's branding for a cohesive look.

3. [Download the project](https://docs.flutterflow.io/flutterflow-cli/exporting) and run the following command in your terminal to generate the launcher icon:

   `flutter pub run flutter_launcher_icons:main`

4. [Run your app](https://docs.flutterflow.io/testing/run-your-app) on a real device or emulator to see the app launcher icon.

![adaptive-icons](https://docs.flutterflow.io/assets/images/adaptive-icons-12360989e7fcdd7452191243b0ad3208.avif)

###### Useful Resources

See the following resources for more information on Android adaptive icons.

###### Create Adaptive Icon

* [Create app icons in Android Studio](https://developer.android.com/studio/write/create-app-icons#create-adaptive)
* [Figma template](https://material.uplabs.com/posts/adaptive-icon-sticker-sheet) (requires login)
* [Affinity Designer template](https://cyrilmottier.com/2017/07/06/adaptive-icon-template/)
* [Bjango templates](https://github.com/bjango/Bjango-Templates) include adaptive icons
* [Adobe XD template](https://github.com/faizmalkani/adaptive-icon-template-xd)

###### Adaptive Icon Fundamentals

* [Understanding Android Adaptive Icons](https://medium.com/google-design/understanding-android-adaptive-icons-cee8a9de93e2)
* [Designing Adaptive Icons](https://medium.com/google-design/designing-adaptive-icons-515af294c783)
* [Implementing Adaptive Icons](https://medium.com/google-developers/implementing-adaptive-icons-1e4d1795470e)

#### Nav Bar and App Bar

See how to configure the [Nav Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#enable-nav-bar-in-settings) and the [App Bar](https://docs.flutterflow.io/resources/ui/pages/scaffold#appbar).

---

### Project API {#project-api}

*The FlutterFlow Project APIs allow you to programmatically read, write, and validate YAML configuration files through REST endpoints. Using these APIs, you can automate project management tasks, integrate continuous integration and delivery (CI/CD) workflows, and apply bulk configuration updates without manual interactions with the FlutterFlow user interface.*

**Source:** https://docs.flutterflow.io/resources/projects/settings/project-apis

The FlutterFlow **Project APIs** allow you to programmatically read, write, and validate YAML configuration files through REST endpoints. Using these APIs, you can automate project management tasks, integrate continuous integration and delivery (CI/CD) workflows, and apply bulk configuration updates without manual interactions with the FlutterFlow user interface.

> **Warning:** The Project API is currently in beta and may undergo changes that could affect functionality or compatibility.

Prerequisites

Before using the Project YAML API, make sure you have the following:

* **HTTP Client**: Use a tool like `curl`, [**Postman**](https://www.postman.com/), or an HTTP library in your preferred programming language (e.g., `axios`, `requests`).
* **Project Access**: You must have read access for GET/validation operations and an editor access for making updates to the project.
* **Paid Plan**: You need a paid [**FlutterFlow subscription plan**](https://www.flutterflow.io/pricing).

#### YAML Overview

##### What are FlutterFlow Project YAMLs?

YAML (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files. In FlutterFlow, **Project YAMLs represent the complete structural definition of your app,** essentially exposing the full project schema that powers your FlutterFlow app.

##### What's Included in the Project Schema?

FlutterFlow's YAML files contain a comprehensive representation of your entire project, including:

* **UI Components & Pages**: Widget trees, page layouts, component hierarchies, and styling configurations.
* **App Configuration**: Settings like app details, authentication methods, integrations (AdMob, Firebase, etc.)
* **Data Structures**: Database collections, API schemas, app state variables, and custom data types.
* **Business Logic**: Actions, functions, conditional logic, and workflow definitions.
* **Assets & Resources**: Custom code files, image references, fonts, and other project assets.
* **Project Organization**: Folder structures, component libraries, and project metadata.

##### YAML vs. FlutterFlow UI

Every change you make in the FlutterFlow visual editor — from dragging a widget onto a page to configuring a database collection, is ultimately stored as structured data in these YAML files. The FlutterFlow UI provides an intuitive visual interface for editing this underlying schema, while the Project API gives you direct programmatic access to the same data.

##### File Structure

FlutterFlow automatically partitions your project into logical YAML files for optimal performance and organization. Each file represents a specific aspect of your project (e.g., `app-state`, `ad-mob`, individual pages, collections, etc.), making it easy to target specific updates without affecting the entire project.

#### Base URL

FlutterFlow provides different API endpoints for various environments. Use the appropriate base URL below depending on your needs:

* Production
* Beta/Staging
* Enterprise

```
https://api.flutterflow.io/v2/
```

```
https://api.flutterflow.io/v2-staging/
```

**India**

```
 https://api-enterprise-india.flutterflow.io/v2/
```

**APAC**

```
https://api-enterprise-apac.flutterflow.io/v2/
```

**US Central**

```
https://api-enterprise-us-central.flutterflow.io/v2/
```

**Europe**

```
https://api-enterprise-europe.flutterflow.io/v2/
```

#### Authentication

All API endpoints require authentication using a Bearer token. You'll need to include your FlutterFlow API token in the Authorization header of each request. See [how to get the API Token](https://docs.flutterflow.io/accounts-billing/account-management#how-do-i-generate-an-api-token).

```
Authorization: Bearer YOUR_API_TOKEN_HERE
```

#### API Endpoints

Below is a list of available API endpoints with their methods and usage descriptions.

| Endpoint                    | Method | Purpose                                        |
| --------------------------- | ------ | ---------------------------------------------- |
| `/listPartitionedFileNames` | GET    | List available YAML file names for a project.  |
| `/l/listProjects`           | POST   | Retrieve metadata for all projects.            |
| `/projectYamls`             | GET    | Export/download YAML files from a project.     |
| `/validateProjectYaml`      | POST   | Validate YAML content before applying changes. |
| `/updateProjectByYaml`      | POST   | Update project configuration via YAML.         |

##### List File Names

Before you read or update project files, you need to know what YAML files are available. This endpoint returns a full list of file names associated with your FlutterFlow project.

###### Endpoint

`GET /listPartitionedFileNames`

###### Query Parameters

`projectId` (required): The ID of the FlutterFlow project

###### Response

```
{
  "success":true,
  "reason":null,
  "value":{
    "versionInfo": {
      "partitionerVersion": 6, 
      "projectSchemaFingerprint": "abc123"
    },
    "fileNames": [
      "folders",
      "app-details",
      "collections/id-yr7z6g5a",
      "page/id-Scaffold_l9g6ilb6/page-widget-tree-outline/node/id-Column_174wuhc4",
      "custom-file/id-MAIN/custom-file-code",
      ...
    ]
  }
}
```

The `fileNames` array lists out all the available YAML files. The `versionInfo` section provides metadata about the schema version and its unique fingerprint. If any part of `versionInfo` changes, it indicates that the API or the structure of the YAML responses has been updated.

###### Example Usage

```
curl -X GET \
  'https://api.flutterflow.io/v2/listPartitionedFileNames?projectId=your-project-id' \
  -H 'Authorization: Bearer YOUR_API_TOKEN'
```

##### List Projects

This endpoint retrieves a list of FlutterFlow projects associated with your account, including detailed metadata such as project name, owner email, team info, collaboration settings, and versioning data.

###### Endpoint

`POST /l/listProjects`

###### Request Body

```
{
  "project_type": "ALL",
  "deserialize_response": true
}
```

* **`project_type: "ALL"`**: Use "ALL" to include personal, team, and shared projects, or "TEAM\_RESOURCE" to include only team-associated projects.

* **`deserialize_response: true`**: Ensures the response is returned as human-readable JSON instead of a base64-encoded protobuf.

> **Tip:** It’s recommended to use the default options: `"ALL"` for `project_type` and `true` for `deserialize_response` for the most complete and readable results.

###### Response

Returns a JSON object containing an array of projects under the `entries` key. Each entry contains the project ID and rich metadata, including collaborators, app icons, sessions, and branching information.

```
{
  "success": true,
  "reason": null,
  "value": {
    "entries": [
      {
        "id": "XXXXXXXXXXXXXXX",
        "project": {
          "name": "Sample Project A",
          "ownerEmail": "user1@example.com",
          "createdAt": "2024-08-08T11:01:12.427Z",
          "updatedAt": "2024-08-08T11:01:18.669Z",
          "teamRef": {
            "path": "teams/TEAM_ID_1"
          },
          "mainBranchRef": {
            "path": "projects/sample-project-id"
          },
          "numBranches": 2,
          "otherMembers": {
            "USER_XYZ": {
              "email": "editor1@example.com",
              "accessLevel": "EDITOR"
            }
          },
          "activeSessions": {
            "SESSION_ID_1": {
              "lastSuccessfulUpdate": "2024-08-06T18:41:56.569Z"
            }
          },
          "totalNumUpdates": 2177
        }
      }
    ]
  }
}
```

###### Example Usage

```
curl 'https://api.flutterflow.io/v2/l/listProjects' \
  -H 'authorization: Bearer YOUR_API_TOKEN' \
  --data-raw '{
    "project_type": "ALL",
    "deserialize_response": true
  }'
```

##### Download Project YAML

You can download specific or all YAML configuration files from your FlutterFlow project. This helps in understanding the current structure of the file before modifying it.

###### Endpoint

`GET /projectYamls`

###### Query Parameters

* `projectId` (required): The ID of the FlutterFlow project
* `fileName` (optional): Specific file to export (without extension). If not provided, all files are exported.

###### Response

Returns a zip file encoded as a base64 string. You will need to manually decode this base64 data into a downloadable .zip file. To do so, copy the value of `projectYamlBytes` and then you can use online tools such as [base64.guru](https://base64.guru/converter/decode/file) or [b64encode.com](https://b64encode.com/tools/base64-to-zip/) to convert and download the files.

```
{
  "success":true,
  "reason":null,
  "value":{
    "versionInfo": {
      "partitionerVersion": 6,
      "projectSchemaFingerprint": "abc123"
    },
    "projectYamlBytes": "UEsDBAoAAAAAAKxV..."
  }
}
```

###### Example Usage

```

#### Export all YAML files
curl -X GET \
  'https://api.flutterflow.io/v2/projectYamls?projectId=your-project-id' \
  -H 'Authorization: Bearer YOUR_API_TOKEN'

#### Export specific file
curl -X GET \
  'https://api.flutterflow.io/v2/projectYamls?projectId=your-project-id&fileName=ad-mob' \
  -H 'Authorization: Bearer YOUR_API_TOKEN'
```

##### Validate Project YAML

You must validate the YAML content before applying changes to ensure it's properly formatted and contains valid values.

###### Endpoint

`POST /validateProjectYaml`

###### Request Body

```
{
  "projectId": "your-project-id",
  "fileKey": "ad-mob",
  "fileContent": "showTestAds: false\nappId: \"your-app-id\""
}
```

> **Info:** * In the `fileContent` object, you must provide the **entire content** of the file.

* The YAML content must be passed as a **single-line string** with correct formatting and appropriate escaping for new lines and indentation. For example, in the following `fileContent` object, you see the actual multiline YAML content, which is not allowed ❌.

  ```
  {
    "projectId": "ecommerce-flow-app-ie7nl6",
    "fileKey": "app-state",
    "fileContent": "fields:
    - parameter:
        identifier:
          name: myAppState
          key: hg7j8z0y
        dataType:
          scalarType: String
        description: "Stores the current user session state"
      persisted: false"
  }
  ```

  Now, here’s how the YAML content should be passed (i.e., as single line string ✅).

  ```
  {
    "projectId": "ecommerce-flow-app-ie7nl6",
    "fileKey": "app-state",
    "fileContent": "fields:\n  - parameter:\n      identifier:\n        name: myAppState\n        key: hg7j8z0y\n      dataType:\n        scalarType: String\n      description: \"Stores the current user session state\"\n    persisted: false"
  }
  ```

###### Response

* **Success (200):** YAML is valid - `{"success": true, "reason": null, "value": ""}`

* **Error with validation details:**

  ```
  {
    "validationErrors": [
      {
        "message": "Expected bool value",
        "fileKey": "ad-mob",
        "yamlLocation": {
          "line": 1,
          "column": 15
        }
      }
    ]
  }
  ```

###### Example Usage

```
curl -X POST \
  'https://api.flutterflow.io/v2/validateProjectYaml' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "projectId": "your-project-id",
    "fileKey": "ad-mob", 
    "fileContent": "showTestAds: false"
  }'
```

##### Update Project YAML

This endpoint allows you to overwrite existing files in your FlutterFlow project by submitting updated YAML content.

###### Endpoint

`POST /updateProjectByYaml`

###### Request Body

```
{
  "projectId": "your-project-id",
  "fileKeyToContent": {
    "ad-mob": "showTestAds: false",
  }
}
```

> **Info:** * In the `fileKeyToContent` object, you must provide the **entire content** of the file.

* The YAML content must be passed as a **single-line string** with correct formatting and appropriate escaping for newlines and indentation. For example, in the following `fileKeyToContent` object, you see the actual multiline YAML content, which is not allowed ❌.

  ```
  {
    "projectId": "ecommerce-flow-app-ie7nl6",
    "fileKeyToContent": {
      "app-state": "fields:
        - parameter:
        identifier:
          name: myAppState
          key: hg7j8z0y
        dataType:
          scalarType: String
        description: "Stores the current user session state"
      persisted: false"
    }
  }
  ```

  Now, here’s how the YAML content should be passed (i.e., as single line string ✅).

  ```
  {
    "projectId": "ecommerce-flow-app-ie7nl6",
    "fileKeyToContent": {
      "app-state": "fields:\n  - parameter:\n      identifier:\n        name: myAppState\n        key: hg7j8z0y\n      dataType:\n        scalarType: String\n      description: \"Stores the current user session state\"\n    persisted: false"
    }
  }
  ```

###### Response

* **Success (200):** `{"success": true, "reason": null, "value": ""}`
* **Error (400):** Validation errors or malformed request.
* **Error (403):** Insufficient permissions or project locked.
* **Error (404):** Project or user not found.

###### Example Usage

This example updates the `ad-mob` file and adds/updates app state variables.

```
curl -X POST \
  'https://api.flutterflow.io/v2/updateProjectByYaml' \
  -H 'Authorization: Bearer YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "projectId": "your-project-id",
    "fileKeyToContent": {
      "ad-mob": "showTestAds: false",
      "app-state": "fields:\n  - parameter:\n      identifier:\n        name: myAppState\n        key: hg7j8z0y\n      dataType:\n        scalarType: String\n      description: \"Stores the current user session state\"\n    persisted: false\n  - parameter:\n      identifier:\n        name: userPreferences\n        key: abc123xy\n      dataType:\n        scalarType: JSON\n      description: \"User settings and preferences\"\n    persisted: true"
    }
  }'
```

#### API Usage Example

Let’s walk through a practical example of updating an app state variable using the Project APIs.

> **Info:** You can download and use [**Postman Collection**](../../../../static/jsons/FlutterFlow_APIs.postman_collection.json) to quickly test all FlutterFlow Project APIs with pre-filled headers, parameters, and sample requests.

First, we use the `/listPartitionedFileNames` endpoint to check if the `app-state` file exists in the project. Once confirmed, we call the `/projectYamls` endpoint to download the YAML file. The API returns a base64-encoded string representing a zip file, which we decode and download using tools like [Base64 to ZIP](https://b64encode.com/tools/base64-to-zip/).

Next, we open the `app-state.yaml` file and update the `enableDarkMode` variable by setting its `persisted` value to `true`. We then convert the updated YAML into a properly escaped single line string and validate it using the `/validateProjectYaml` endpoint. If validation succeeds, we send the final update using the `/updateProjectByYaml` endpoint.

#### Error Handling

This section outlines how the API handles errors, including common HTTP response codes and detailed validation feedback for YAML processing issues.

##### Common Error Responses

This table outlines the most common HTTP status codes and their meanings, helping you identify and resolve API issues more effectively.

| Status Code | Description                                  | Example Response                                         |
| ----------- | -------------------------------------------- | -------------------------------------------------------- |
| 400         | Bad Request - Invalid JSON or malformed YAML | `"Failed to update project: ad-mob:Expected bool value"` |
| 403         | Forbidden - Insufficient permissions         | `"You do not have write access to this project"`         |
| 404         | Not Found - Project or user doesn't exist    | `"Project not found"`                                    |
| 500         | Internal Server Error                        | `"Unknown error"`                                        |

##### Validation Errors

When YAML validation fails, you'll receive detailed error information:

```
{
  "validationErrors": [
    {
      "message": "Unknown field name 'showTestAdsasssdaf'",
      "fileKey": "ad-mob",
      "yamlLocation": {
        "line": 1,
        "column": 1
      }
    }
  ]
}
```

#### Best Practices

* **Always Validate First**: Before updating project YAMLs, use the validation endpoint to ensure your changes are valid:

  ```
  # 1. Validate the YAML
  curl -X POST 'https://api.flutterflow.io/v2/validateProjectYaml' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{"projectId": "project-id", "fileKey": "ad-mob", "fileContent": "showTestAds: false"}'

  # 2. If validation passes, apply the changes
  curl -X POST 'https://api.flutterflow.io/v2/updateProjectByYaml' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{"projectId": "project-id", "fileKeyToContent": {"ad-mob": "showTestAds: false"}}'
  ```

* **Handle Project Locks**: Projects may be temporarily locked during other operations. If you receive a 403 error mentioning `Project is locked due to ongoing changes. Please try again later.`, wait and retry.

* **Batch Updates**: You can update multiple files in a single request by including multiple entries in `fileKeyToContent`:

  ```
  {
    "projectId": "your-project-id",
    "fileKeyToContent": {
      "ad-mob": "showTestAds: false",
      "app-settings": "appName: \"Updated Name\"",
      "authentication": "enableEmailAuth: true"
    }
  }
  ```

#### Rate Limits

Please be mindful of API rate limits. If you're making many requests, implement appropriate delays between calls to avoid being rate-limited.

---

### Project Setup {#project-setup}

*Learn how to setup your project in FlutterFlow.*

**Source:** https://docs.flutterflow.io/resources/projects/settings/project-setup

-keep class com.google.gson.** { *; }
-keepattributes *Annotation*
```

This ensures that Firebase and Gson classes are not obfuscated, preventing serialization errors.

**Example 2: Debugging ProGuard Issues**

If your app crashes in release mode but works in debug mode, ProGuard might be removing important classes. To troubleshoot, you can add logging and keep rules.

```
-assumenosideeffects class android.util.Log {
    public static *** d(...);
    public static *** v(...);
    public static *** i(...);
}
```

This removes debug logs in release builds but retains them for troubleshooting.

**Example 3: Improving Security by Removing Debug Information**

Attackers can decompile APKs and view sensitive debug logs. To remove these debug logs, add:

```
-dontwarn android.util.Log
```

**Example 4: Keeping Native Libraries (JNI) Safe**

If your app uses native C/C++ libraries (JNI), ProGuard may mistakenly remove required components. To prevent this:

```
-keep class com.example.native.** { *; }
-keepclassmembers class * {
    native <methods>;
}
```

This keeps all native methods intact.

**Example 5: Preventing Issues with Reflection-Based Code**

Some libraries rely on reflection to dynamically call methods, which ProGuard may remove.

```
-keep class * implements android.os.Parcelable { *; }
-keepclassmembers class ** {
    @android.webkit.JavascriptInterface <methods>;
}
```

This ensures reflection-based code continues working.

##### `Info.plist` (iOS)

`Info.plist` (Information Property List) is the configuration file for iOS apps. It’s a structured XML file that provides iOS with essential information about your app’s configuration and requirements.

The `Info.plist`defines things such as your app’s bundle identifier, display name, version, and most importantly, usage descriptions for permissions and other settings iOS needs at runtime. The file is required for every iOS app and is located in the project’s `/ios/Runner/` directory of your FlutterFlow apps.

Essentially, it’s the blueprint for iOS to understand your app’s capabilities and needs.

Here are some scenarios where you may need to modify the `Info.plist` file:

**Example 1: Requesting Permissions**

If your app requires location access both while in use and in the background, you must declare the appropriate permissions in `Info.plist`. **Tip:** You can also add custom permissions directly through the [**Permission Settings**](https://docs.flutterflow.io/resources/projects/settings/project-setup#adding-custom-permission) in FlutterFlow.

```
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app requires location access while in use to provide location-based services.</string>

<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app requires background location access to enable continuous location tracking.</string>
```

This ensures the app can access location services even when the user is not actively using it.

**Example 2: Enabling App Transport Security (ATS) for HTTP Requests**

By default, iOS enforces HTTPS connections for security reasons. If your app needs to communicate with **HTTP-only** servers, you must modify `Info.plist`.

```
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

This allows all HTTP requests but should be used with caution

**Example 3: Configuring Background Modes**

If your app requires background functionality (e.g., playing music, location tracking), you must enable background modes in `Info.plist`.

```
<key>UIBackgroundModes</key>
<array>
    <string>audio</string>
    <string>location</string>
</array>
```

This allows the app to play audio or track location when running in the background.

**Example 4: Adding Keys**

Many third-party packages require to add keys in the in `Info.plist` file. For example, If you’re using the Mapbox SDK, you need to provide an access token in `Info.plist` to enable map functionality.

```
<key>io.flutter.embedded_views_preview</key>
<true/>
<key>MGLMapboxAccessToken</key>
<string>YOUR_MAPBOX_ACCESS_TOKEN</string>
```

The **`MGLMapboxAccessToken`** key is required for initializing Mapbox maps in your app. Additionally, the **`io.flutter.embedded_views_preview`** key must be set to `true` to support embedding native views inside Flutter widgets.

> **Tip:** You can modify the `Info.plist` file by either [**adding a snippet**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#snippet-placement-for-ios) or [**editing it manually**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### `Entitlements.plist` (iOS)

The `Entitlements.plist` file is a property list in iOS applications that defines the app’s security-related capabilities and permissions. It grants specific privileges to an app, allowing it to access Apple services such as iCloud, Push Notifications, App Groups, Background Modes, and Keychain access. It is located in the **`/ios/Runner/`** directory of your FlutterFlow app and is named **`Runner.entitlements`**.

This file ensures that only authorized apps can use these features, maintaining security and preventing unauthorized access to sensitive system functions.

Here are some scenarios where you may need to modify the `Entitlements.plist` file:

**Example 1: Enabling iCloud Storage**

If your app integrates **iCloud services**, such as syncing user data or storing documents, you must add iCloud entitlements.

```
<key>com.apple.developer.icloud-container-identifiers</key>
<array>
    <string>iCloud.com.yourcompany.appname</string>
</array>

<key>com.apple.developer.icloud-services</key>
<array>
    <string>CloudDocuments</string>
</array>
```

This grants your app access to iCloud storage under the specified container.

**Example 2: Enabling Keychain Access**

If your app needs to store secure credentials, enabling Keychain Sharing is required.

```
<key>keychain-access-groups</key>
<array>
    <string>com.yourcompany.appname</string>
</array>
```

This allows secure storage of login credentials, API tokens, or encryption keys in the iOS Keychain.

**Example 3: Enabling App Groups for Shared Data**

If your app shares data between multiple apps or an app extension (e.g., a widget or a Siri shortcut), you must enable App Groups.

```
<key>com.apple.security.application-groups</key>
<array>
    <string>group.com.yourcompany.shared</string>
</array>
```

This allows different apps or extensions to access shared storage and user defaults.

**Example 4: Enabling Wallet (Apple Pay & Passes)**

If your app integrates with Apple Wallet, you need to add Wallet entitlements.

```
<key>com.apple.developer.pass-type-identifiers</key>
<array>
    <string>pass.com.yourcompany.appname</string>
</array>
```

This enables your app to create, manage, and present passes in Apple Wallet.

> **Tip:** You can modify the `Entitlements.plist` file by either [**adding a snippet**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#snippet-placement-for-ios) or [**editing it manually**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### `AppDelegate.swift` (iOS)

The `AppDelegate.swift` file is the entry point for your iOS application. It plays a crucial role in setting up your app’s runtime environment and handling app lifecycle events such as launching, backgrounding, and termination. This file is also where you register Flutter plugins and initialize SDKs like Firebase or Branch.

It’s located at: `ios/Runner/AppDelegate.swift`

**Example: Registering Custom iOS Plugins**

For custom native iOS plugins that aren’t auto-registered, you can manually register them inside `AppDelegate.swift`.

```
override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  let controller: FlutterViewController = window?.rootViewController as! FlutterViewController
  let myPlugin = CustomPlugin()
  myPlugin.register(with: controller)
  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```

Use this for custom iOS integrations that require manual setup.

> **Tip:** You can modify the `AppDelegate.swift` file by either [**adding a snippet**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#snippet-placement-for-ios) or [**editing it manually**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

##### `main.dart` (Flutter)

The `main.dart` file is the entry point of every FlutterFlow app. It is the first file that runs when the app starts and is responsible for initializing the application, configuring dependencies, and defining the root widget. Located in the **`lib/`** directory, `main.dart` contains the `main()` function, which is required for every FlutterFlow app.

If you need to execute any custom Dart code at startup — such as initializing third-party SDKs, setting global configurations, service locators, printing a debug log, or running certain functions once — `main.dart` is the place to do it.

> **Info:** [**Adding Snippets**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-1-add-individual-snippets) isn't available for `main.dart`. Instead, you can directly modify the file using [**Manual Edit Mode**](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-2-manual-edit-mode).

Here are some scenarios where you may need to modify the `main.dart` file:

**Example 1: Initializing Third-Party Packages**

Many packages have initialization calls. For example, if you added a custom package for analytics or error tracking (say Sentry or a logging service), you might need to call `SentryFlutter.init()` or set up an error handler at app startup. By placing that call in `main.dart` (before or right after `runApp`), you ensure it’s executed early.

```
import 'dart:async';

import 'package:flutter/widgets.dart';
import 'package:sentry_flutter/sentry_flutter.dart';

Future<void> main() async {
  runZonedGuarded(() async {
    await SentryFlutter.init(
      (options) {
        options.dsn = 'https://example@sentry.io/add-your-dsn-here';
      },
    );

    runApp(MyApp());
  }, (exception, stackTrace) async {
    await Sentry.captureException(exception, stackTrace: stackTrace);
  });
}
```

This ensures Sentry is ready before the app starts, just like Firebase initialization.

**Example 2: Customizing the Status Bar Appearance**

If you want to change the status bar color and adjust icon brightness for Android and iOS, you need to modify `main.dart` before calling `runApp()`.

```

import 'package:flutter/services.dart';

void main() {
  SystemChrome.setSystemUIOverlayStyle(
    SystemUiOverlayStyle(
      statusBarColor: Colors.redAccent, // Custom status bar color
      statusBarIconBrightness: Brightness.dark, // Dark icons for Android
      statusBarBrightness: Brightness.light, // Light icons for iOS
    ),
  );

  runApp(MyApp());
}
```

**Example 3: Locking the Screen Orientation**

Some apps require landscape-only or portrait-only modes. You can enforce screen orientation in `main.dart` before launching the app.

```
import 'package:flutter/services.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.landscapeLeft,
    DeviceOrientation.landscapeRight,
  ]);

  runApp(MyApp());
}
```

This ensures the app only runs in landscape mode.

**Example 4: Observing App Lifecycle Changes**

If your app needs to respond to lifecycle events, such as tracking when the app goes into the background or returns to the foreground, you can attach an observer.

```
import 'package:flutter/widgets.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  WidgetsBinding.instance.addObserver(AppLifecycleObserver());
  runApp(MyApp());
}

class AppLifecycleObserver with WidgetsBindingObserver {
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      print('App is in foreground');
    } else if (state == AppLifecycleState.paused) {
      print('App is in background');
    }
  }
}
```

#### Best Practices

* **Backup:** Before making native file changes, ensure you have a backup of at least the text of the original file. You could also commit your changes so you can revert if needed. This way, if things go wrong, you can manually restore.
* **One Change at a Time:** Add or modify one item at a time and then test your app. If you add multiple things and something breaks, it’s harder to pinpoint which change did it.
* **Consult Package Documentation:** When you’re making changes for third-party packages, follow their instructions exactly. Usually, package docs show a snippet – use that in FlutterFlow’s [snippet](https://docs.flutterflow.io/concepts/custom-code/configuration-files#option-1-add-individual-snippets). Double-check official docs for Android or iOS if you’re unsure about the correct keys or tags. For example, if enabling background fetch, Apple’s docs will list the exact string to use in `Info.plist` (`fetch` in `UIBackgroundModes` array).
* **Keep it Minimal:** Only add what you truly need. Don’t add a bunch of entitlements or permissions “just in case” as that can bloat and complicate your app, and even trigger store reviews for uses that your app doesn’t actually have.
* **Use Comments:** As you modify files, annotate them. If six months later you or a team member look at the manifest, a comment like `<!-- Added for Payments SDK on Feb 2025 -->` is very helpful.
* **Testing on Devices:** Especially for anything related to `Info.plist` or entitlements, always test on a real iOS device if possible. Some issues (like missing entitlements or background mode usage) won’t show up in the simulator. Similarly, test Android changes on a device or emulator with a release build – because ProGuard rules effects, for example, only show in release mode.
* **Monitoring Logs and Errors:** After making changes, monitor the Xcode console or Android logcat when running the app. If there are misconfigurations, you often get warnings.
* **Stay Updated:** FlutterFlow may improve native editing features over time. Keep an eye on FlutterFlow’s docs or community announcements. If they introduce a new easier way, prefer that to manual editing when possible, as it will be more foolproof.
* **Security Consideration:** Remember that anything in these files (especially `Info.plist`, `AndroidManifest.xml`) is essentially public in the distributed app. Don’t assume an API key in `Info.plist` is hidden – it’s not. For keys you must include (maps, etc.), consider using [private environment values](https://docs.flutterflow.io/testing/dev-environments#private-environment-values) and monitoring their usage.

#### FAQs

My app won’t install on an iOS device. What should I check?

Confirm that the entitlements in `Entitlements.plist` match your provisioning profile. If you see a “Missing entitlement” error, it means you added an entitlement not allowed by your profile. Remove it or update the profile in the Apple Developer Portal.

How do I fix “Manifest merger failed” on Android?

This error indicates a conflict in your `AndroidManifest.xml`. Common issues include **duplicate permissions** or attributes (e.g., two `<application android:label>` entries). The error message usually identifies the conflicting line. Remove the duplicate or ensure each property is set only once to resolve the conflict.

Why my app isn't running in Test Mode after editing the `main.dart` file with Supabase enabled?

There's a known limitation where editing the `main.dart` file with Supabase enabled prevents Test Mode from running. As a workaround, please use [**Local Run**](https://docs.flutterflow.io/testing/local-run) to test your app instead.

Can I modify the Configuration Files in a Library project?

Yes, you can. When a Library Project is imported, any configuration file snippets, such as those for `AndroidManifest.xml`, `Info.plist`, or `Entitlements.plist` are automatically merged into the importing project's configuration files.

Additionally, your Library Project can pass values (like API keys) into those snippets using [**Library Values**](https://docs.flutterflow.io/resources/projects/libraries#library-values), making it easy to customize.

![config-values-in-library](https://docs.flutterflow.io/assets/images/config-values-in-library-daa58dd3085d67ffaec7a37c099da6fc.avif)

This makes Libraries incredibly powerful and enables easy integration of tools like **PostHog** (analytics), **Sentry** (crash reporting), **CleverTap**, **flutter\_local\_notifications**, **flutter\_nfc\_kit**, and many more directly from the Marketplace.

---

### Naming Variables & Functions {#naming-variables-functions}

*Naming conventions for FlutterFlow, including guidelines for widgets, components, state variables, constants, and more.*

**Source:** https://docs.flutterflow.io/resources/style-guide

To make your code more maintainable, readable, and consistent, it’s essential to adopt clear naming conventions for variables, functions, and components.

Best practices for naming conventions in app development (especially for projects using Flutter), aim to improve code readability, maintainability, and consistency across the application. Here are some general guidelines tailored for different aspects of a Flutter project:

Various naming styles (as suggested by [Dart Effective Style Guide](https://dart.dev/effective-dart/style#identifiers)):

* **UpperCamelCase** (also known as PascalCase) names capitalize the first letter of each word, including the first.

* **lowerCamelCase** (also known as camelCase) names capitalize the first letter of each word, except the first which is always lowercase, even if it's an acronym.

* **lowercase\_with\_underscores** (also known as snake\_case) names use only lowercase letters, even for acronyms, and separate words with \_.

![various-naming-styles.png](https://docs.flutterflow.io/assets/images/various-naming-styles-1c972b9898f0f011be5caba60a9754a5.png)

**General Principles**

* **Be Consistent:** Whatever conventions you choose, apply them consistently across the project.
* **Be Descriptive:** Names should be self-explanatory, reducing the need for additional comments to explain what a variable, function, or class does.
* **Avoid Abbreviations:** Unless it's a well-known abbreviation, spell out words to avoid confusion.

#### Variable Naming Convention

This section outlines naming conventions for pages, components, state variables, custom data types, enums, and constants to ensure clarity and consistency throughout the project.

##### Pages & Components

Use **UpperCamelCase** for all widgets, components, pages, and screen names to maintain consistency and readability. FlutterFlow ensures clarity by automatically adding "Widget" to widget names when generating code. For components, you can suffix the name with "Component" to clearly distinguish them.

Similarly, for pages and screens, include "Page" or "Screen" in the name to indicate their purpose. This approach aligns with Dart conventions for class names and ensures a well-organized project structure.

![comp-style-guide.png](https://docs.flutterflow.io/assets/images/comp-style-guide-2ff5f0992fe7d38b846bdb92e807b6b1.png)

Do's

* **Use UpperCamelCase for Names:** Always use **UpperCamelCase** for widgets, components, pages, and screens. Examples: `CustomButton`, `UserProfilePage`, `MainViewComponent`.

* **Include "Screen" or "Page" in Page Names:** Use "Screen" or "Page" in file names to identify UI screens or pages. Examples: `LoginScreen`, `SettingsPage`.

* **Use Prefixes for Clarity When Necessary:** Add a prefix if it significantly improves clarity or prevents naming conflicts. Example: `AdminUserProfile` (to differentiate it from `CustomerUserProfile` or `UserProfile`).

* **Be Descriptive and Clear in File Names:** Ensure names are descriptive enough to convey their purpose at a glance. Examples: `OrderConfirmationScreen`, `ProductDetailsPage`.

Don'ts

* **Don’t Use Unnecessary Prefixes:** Avoid prefixes that do not add clarity or are redundant. Bad Example: `AppPrimaryButton` (if `PrimaryButton` is sufficient).

* **Don’t Add "Widget" Explicitly:** Avoid adding "Widget" to class or component names manually, as FlutterFlow already appends it during code generation. Bad Examples: `ButtonWidget`, `ProfileCardWidget`.

* **Don’t Use LowerCamelCase for Class Names:** Reserve **lowerCamelCase** for variables and methods, not for components, or pages. Bad Examples: `loginButton`, `userProfile`.

* **Don’t Mix Naming Conventions:** Maintain consistency with UpperCamelCase for all widgets, components, pages, and screens. Bad Examples: `userLogin`, `Profilecard`, `headerView`.

* **Don’t Use Generic Names Without Purpose:** Avoid overly generic names that do not clearly convey the file’s intent. Bad Examples: `Main`, `View`, `Screen1`.

Note that the style guidelines for Pages and Components also apply to **[Custom Widgets](https://docs.flutterflow.io/concepts/custom-code/custom-widgets)**, as Pages and Components created in FlutterFlow are internally generated as widgets.

##### Custom Data Types & Enums

When naming custom data types and enums, use **UpperCamelCase** for consistency and clarity. Ensure that names are descriptive, providing a clear representation of the entity or purpose.

![dt-style-guide.png](https://docs.flutterflow.io/assets/images/dt-style-guide-8a04300e5d3d1f20e1dbb7d13e96c3b2.png)

Do's

* **Use UpperCamelCase for Custom Data Types:** Name your custom data types using **UpperCamelCase**. Ensure that names are clear, concise, and descriptive, reflecting the entity they represent. Good Examples: `UserModel`, `ProductDetails`, `OrderItem`.

* **Use consistent naming for Enum Names and Values:** Use **UpperCamelCase** for the enum name such as, `Status`, `ConnectionState`, `UserRole` and **lowerCamelCase** for its values e.g., `{active, inactive, pending}`. This approach aligns with Dart's enum naming guidelines and ensures consistency.

* **Use Plural Names for Lists:** If the data type represents a List, use a plural name to clarify its purpose. Good Example: `OrderItems` (to represent multiple `OrderItem` objects).

Don'ts

* **Don’t Use All Lowercase or Mixed Case for Custom Data Types:** Avoid using all lowercase or inconsistent casing in data model class names, as it reduces readability. Bad Example: `usermodel`, `product_details`.

* **Don’t Use Vague or Non-Descriptive Names**: Avoid using generic or unclear names that do not clearly describe the data entity. Bad Example: `DataModel`, `Entity`, `Item`.

* **Don’t Mix Naming Conventions for Enums:** Maintain consistent capitalization between enum names and their values. Bad Example: `enum UserRole { Admin, EDITOR, viewer }`

For datatype fields, we use the same convention as [State variables](https://docs.flutterflow.io/resources/style-guide#variables).

##### Constants

Flutter prefers using a lowercase `k` prefix for constants to indicate their immutability, especially for project-specific constants. This approach is more concise and aligns with Dart's common practices. Use **SCREAMING\_SNAKE\_CASE** only when contributing to global or legacy projects where it is already in use.

Do's

* **Start Constants with a k Prefix:** Always use a lowercase `k` followed by **UpperCamelCase** for constants in FlutterFlow projects.
* **Use Descriptive and Contextual Names:** Clearly describe the purpose of the constant. Avoid using abbreviations unless they are widely understood. Examples: `kDefaultPadding`, `kMaxUploadSizeMb`

Don'ts

* **Don’t Omit the k Prefix for Constants:** Avoid using plain names for constants in a Flutter-specific project, as they might conflict with variables or methods. Bad Examples: `padding`, `uploadSize`.
* **Don’t Use Vague or Generic Names:** Avoid using names that fail to describe the purpose of the constant. Bad Examples: `VALUE`, `DATA`, `X`, `Y`.

##### Variables

State variable & Data Type field names follow the **lowerCamelCase** naming style to align with Dart's conventions.

Do's

* **Be Descriptive and Clear:** Use variable names that clearly describe their purpose, avoiding generic or vague terms. Examples: `isFormValid`, `errorMessage`, `availableProducts`.
* **Prefix Boolean Variables with `is`, `has`, or `should`:** For readability, use prefixes that denote the variable's purpose when naming Boolean values. Examples: `isActive`, `hasErrors`, `shouldReload`.
* **Use Consistent Prefixes to denote state:** When managing UI or asynchronous state, use prefixes like `current`, `selected`, or `pending` for better context. Examples: `currentTabIndex`, `selectedUserId`, `pendingAction`.

Don'ts

* **Don’t Use Abbreviations or Single Letters:** Avoid abbreviations or single-character names that obscure the variable's intent. Bad Examples: `usrNm`, `f`, `cnt`.
* **Don’t Use Generic Names:** Avoid using generic terms that do not convey the variable’s purpose. Bad Examples: `data`, `value`, `temp`.
* **Don’t Start Variables with Uppercase:** Follow Dart conventions by starting variable names with lowercase. Bad Examples: `UserName`, `IsLoading`.

#### Function Naming Convention

This section defines naming conventions for custom functions, actions, and action blocks to maintain consistency, readability, and ease of understanding across the codebase.

##### Custom Functions & Actions

Custom functions and custom actions created in the Custom Code tab of FlutterFlow should follow the **lowerCamelCase** naming convention. These typically reflect an action or behavior.

![func-style-guide.png](https://docs.flutterflow.io/assets/images/func-style-guide-4884145ca292af50c547ddac71846d0b.png)

Do's

* **Be descriptive and concise:** Use clear, meaningful names that describe the action or purpose of the function (e.g., `validateForm` instead of `doCheck`, or `fetchUserData` instead of `userData`).
* **Use action-oriented names:** Start with verbs to indicate behavior (e.g., `submitForm`, `processPayment`).

Dont's

* **Avoid using underscores or spaces:** Names like `fetch_user_data` do not align with **lowerCamelCase** conventions.
* **Avoid redundant prefixes or suffixes:** There’s no need to prefix with `custom` or suffix with `Func` unless absolutely necessary for clarity (e.g., `customSubmitFormFunc` is redundant).
* **Don’t use overly generic names:** Avoid vague terms like `doSomething` or `functionOne`, which don’t provide context.

Note that **[Action Blocks](https://docs.flutterflow.io/resources/functions/action-blocks)** should follow the same naming convention as custom actions, as they are both technically Dart functions internally in the generated code.

---

### Periodic Action {#periodic-action}

*Learn how to use the Periodic Action in your FlutterFlow app to perform actions at regular intervals.*

**Source:** https://docs.flutterflow.io/resources/time-based-logic/periodic-action

Periodic execution of logic refers to running a specific block of code or a set of actions at regular, defined intervals. This is useful for tasks that need to be repeated continuously or at specific time intervals.

#### Use-cases

* For tasks that need regular updates, such as fetching data from a server, monitoring system health, or updating a user interface.
* In scenarios where periodic checks or maintenance tasks are required (e.g., cleaning up temporary files, sending periodic notifications).
* Implementing polling mechanisms for checking changes in state or data.

#### Start Periodic Action

To create a periodic action workflow, add the **Start Periodic Action** action either on the **On Page Load** action trigger of your page or on any widget that should start the periodic action.

The properties of the Periodic Action look like this:

![periodic-action.png](https://docs.flutterflow.io/assets/images/periodic-action-443603587a43e6ca0016f1e208f692d4.png)

#### Stop Periodic Action

You can call the **Stop Periodic Action** action from anywhere on the page or component to stop one or multiple periodic actions.

Dont forget to stop the Periodic Actions

Stopping a periodic action is crucial to prevent unnecessary resource consumption and potential performance issues. It ensures that tasks do not continue running in the background when they are no longer needed, which can help maintain the efficiency and responsiveness of your application.

##### Periodic Action vs Timer

| Feature     | Timer Widget                                                                                                    | Periodic Action                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Purpose** | Used for single or non-repetitive timing events, often within user interfaces.                                  | Used for repetitive tasks that need to run at regular intervals.        |
| **Usage**   | To set a countdown timer, start/stop actions based on user input, or trigger actions after a specific duration. | For background tasks, monitoring, regular updates, and periodic checks. |
| **Example** | Countdown timer in a quiz application.                                                                          | Fetching new messages from a server every 5 minutes.                    |

##### Periodic Actions vs Loops

| Feature                 | Periodic Actions                                                       | Loops                                                                       |
| ----------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Purpose**             | To execute a task at regular, defined intervals.                       | To execute a task repeatedly until a condition is met.                      |
| **Execution Frequency** | Executes at specified time intervals (e.g., every 60 seconds).         | Executes continuously until the loop condition is false.                    |
| **Use Case**            | Suitable for tasks needing regular updates, such as fetching new data. | Suitable for tasks requiring iteration over collections or repeated checks. |
| **Control**             | Can be started and stopped easily, allowing for controlled execution.  | Runs until a break condition is met or the loop is explicitly stopped.      |
| **Resource Management** | Efficient, as it allows idle time between executions.                  | Can be resource-intensive if not managed properly, as it runs continuously. |
| **Examples**            | Fetching new offers from a server every 5 minutes.                     | Iterating over a list of items to process them one by one.                  |

---

### Timer [Widget] {#timer-widget}

*Learn how to use the Timer Widget in your FlutterFlow app to manage timed events and actions.*

**Source:** https://docs.flutterflow.io/resources/time-based-logic/timer-widget

**Timer \[Widget]** allows developers to create countdown or count-up timers within your page. It is particularly useful in scenarios where timing is crucial, such as quizzes, auctions, workout apps, and various time-sensitive activities.

#### Use Cases

* **Quizzes and Exams:** Enforcing time limits for answering questions.
* **Auctions:** Displaying the remaining time for bids.
* **Workouts:** Timing exercises and rest periods.
* **Events:** Counting down to the start or end of an event.
* **Productivity:** Using Pomodoro timers to manage work sessions and breaks.

#### Timer Types

* **Countdown Timer:** Counts down from a specified time to zero, often used in scenarios where a task or event needs to be completed within a set period.

* **Count-up Timer:** Counts up from zero to a specified time or indefinitely, useful for tracking the duration of an event or activity.

On adding the Timer widget to your page, you can specify the type of timer and other properties as mentioned here:

![timer-widget.png](https://docs.flutterflow.io/assets/images/timer-widget-003b5dec98bdbd979f826e8693f11640.png)

#### On Timer End \[Action Trigger]

You can also specify a flow of actions when the timer ends. You can find this Action Trigger on clicking the Action Flow Editor on the Timer widget.

![timer-widget-action.png](https://docs.flutterflow.io/assets/images/timer-widget-action-d16ca9214fae45e4005bc40e35b5dec2.png)

#### Controlling the Timer

You can control the timer from anywhere on the page. Using any widget's Action Flow Editor, you can perform the following actions:

* **Start Timer:** This starts the timer. If the timer is already started, triggering this type won't have any effect.

* **Stop Timer:** This stops the timer. This will have effect only if the timer is started.

* **Reset Timer:** This resets the timer and brings it to the initial state.

![timer-control.png](https://docs.flutterflow.io/assets/images/timer-control-61e5b36b9b03b1d9d93c08a4228b0f5d.png)

#### Periodic Action vs Timer

| Feature     | Timer Widget                                                                                                    | Periodic Action                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Purpose** | Used for single or non-repetitive timing events, often within user interfaces.                                  | Used for repetitive tasks that need to run at regular intervals.        |
| **Usage**   | To set a countdown timer, start/stop actions based on user input, or trigger actions after a specific duration. | For background tasks, monitoring, regular updates, and periodic checks. |
| **Example** | Countdown timer in a quiz application.                                                                          | Fetching new messages from a server every 5 minutes.                    |

---

### Wait [Action] {#wait-action}

*Learn how to use the Wait Action in your FlutterFlow app to pause actions for a specified duration.*

**Source:** https://docs.flutterflow.io/resources/time-based-logic/wait-action

The **Wait** action is used to pause the execution of a workflow for a specific amount of time. This is helpful when you want to delay the next step in a sequence, for example, to synchronize events, allow animations to complete, or ensure a condition is met before continuing. It’s a key concept in managing time-based logic within action flows.

Possible use cases

* **Show Splash Screen:** Delay the transition to the next page to allow the splash screen to be visible for a few seconds.
* **Step-by-Step Tutorials:** Introduce timed delays between steps to guide users through a tutorial or onboarding flow.
* **Chain Animations:** Add pauses between multiple animations for a more fluid and organized visual effect.

---

