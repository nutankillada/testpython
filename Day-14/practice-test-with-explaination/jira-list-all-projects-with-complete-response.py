'''
Your provided code performs an authenticated API request to Jira to fetch a list of projects from the Atlassian Jira REST API. Here's a step-by-step explanation of what it does:
-----------------------------------------------------------------------------
🔹 Summary-
✅ Fetches Jira projects from amishasharma1921.atlassian.net.
✅ Uses authentication (email & API token).
✅ Sends a GET request to retrieve project data.
✅ Prints the response (status code & project details).
=====================================================================================================
'''


'''
IMPORTING REQUIRED MODULES:
------------------------------
'''
# This code sample uses the 'requests' library:
# http://docs.python-requests.org - official doc for request library in python
import requests
#- **`import`** → A Python keyword that imports a library.  
#- **`requests`** → A library used for making HTTP requests (GET, POST, PUT, DELETE etc.).

from requests.auth import HTTPBasicAuth
#- **`from`** → A Python keyword used to import a specific module from a package.  
#- **`requests.auth`** → A module in the `requests` library that provides authentication functions.  
#- **`import HTTPBasicAuth`** → Imports the `HTTPBasicAuth` class, which handles HTTP Basic Authentication (username & password).

import json
#- **`import`** → Imports a library.  
#- **`json`** → A built-in Python module for working with JSON (JavaScript Object Notation) data.

import os           # to use getenv() method, to read value of environment variables
#- **`import`** → Imports a library.  
#- **`os`** → A built-in Python module that provides functions to interact with the operating system.  


'''
API URL
--------
'''
url = "https://amishasharma1921.atlassian.net/rest/api/3/project"
#- **`url`** → A variable storing the API endpoint.  
#- **`=`** → Assignment operator, assigns a value to the variable.  
#- **`"https://amishasharma1921.atlassian.net/rest/api/3/project"`** → A string representing the Jira API endpoint for fetching projects.


'''
CREDENTIALS (FETCHING FROM ENVIRONMENT VARIABLES)
--------------------------------------------------
'''
# email = "amisha#######1921@gmail.com"
# api_token = "###########################"     # never hardcode security credentials in your code

email = os.getenv("jira_email")
api_token = os.getenv("jira_api_token")

#- **`os.getenv("jira_email")`** → Fetches the value of the environment variable `jira_email`.  
#- **`os.getenv("jira_api_token")`** → Fetches the value of the environment variable `jira_api_token`.  
#**Why use `os.getenv()`?**  
#- This prevents storing sensitive credentials directly in the code.  
#- The credentials should be set as environment variables in the system.


'''
SETTING UP AUTHENTICATION
--------------------------
'''
auth = HTTPBasicAuth(email, api_token)
#- **`HTTPBasicAuth(email, api_token)`** → Uses the imported `HTTPBasicAuth` class to create authentication credentials using the email and API token.


'''
SETTING HEADERS
-----------------
'''
headers = {
  "Accept": "application/json"
}
#- **`headers`** → A dictionary storing HTTP headers for the request.  
#- **`=`** → Assigns a value.  
#- **`{}`** → Creates a dictionary.  
#- **`"Accept"`** → A key specifying what content type is acceptable in the response.  
#- **`"application/json"`** → Specifies that the API should return JSON-formatted data.


'''
MAKING AN HTTP REQUEST
------------------------
'''
response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
#- **`response`** → A variable storing the API response.  
#- **`=`** → Assigns a value.  
#- **`requests.request()`** → A method in the `requests` library to send HTTP requests.  
#- **`"GET"`** → The HTTP method used (GET request fetches data).  
#- **`url`** → The API endpoint URL (passed as a parameter).  
#- **`headers=headers`** → Passes the headers dictionary to specify JSON response format.  
#- **`auth=auth`** → Passes the authentication details.

'''
PRINTING THE API RESPONSE
---------------------------
'''
print(response)
#- **`print()`** → A function to display output.  
#- **`response`** → Prints the response object. The output might look like:
# OUTPUT:
'''
  <Response [200]>      # A sample expected output when the request is successful.
'''
#- **`Response`** → Indicates an HTTP response object.  
#- **`[200]`** → HTTP status code 200 means **Success**.


print(response.text)
#- **`print()`** → Prints the response content.  
#- **`response.text`** → Extracts the response body as a string.  
#- The output is the actual JSON data returned by the API.
# OUTPUT:
'''
[{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10000","id":"10000","key":"SCRUM","name":"GitHub-Jira-Integration","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=medium"},"projectTypeKey":"software","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"af0a1d42-f3c7-4537-a42f-ac789d29d539","uuid":"af0a1d42-f3c7-4537-a42f-ac789d29d539"},{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10001","id":"10001","key":"MDP","name":"My discovery project","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=medium"},"projectTypeKey":"product_discovery","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"ffe53d53-1dff-481f-86b2-1e0eec7d6d2d","uuid":"ffe53d53-1dff-481f-86b2-1e0eec7d6d2d"},{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10002","id":"10002","key":"SDSTP","name":"Soft-Dev-Scrum-Template-PROJECT","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=medium"},"projectTypeKey":"software","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"ba50747b-7444-48cd-b99d-7896525ab04a","uuid":"ba50747b-7444-48cd-b99d-7896525ab04a"}]
'''


'''
PARSING JSON FOR BETTER READABILITY
-------------------------------------
'''
# list all jira projects on mention jira site (amishasharma1921) with all details
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#- **`json.loads(response.text)`** → Converts the JSON response (string) into a Python dictionary.  
#- **`json.dumps(..., sort_keys=True, indent=4, separators=(",", ": "))`**  
    #- **`json.dumps()`** → Converts a Python dictionary back into a JSON string.  
    #- **`sort_keys=True`** → Sorts JSON keys alphabetically.  
    #- **`indent=4`** → Formats JSON with 4-space indentation for readability.  
    #- **`separators=(",", ": ")`** → Controls formatting of key-value pairs.  
#- **`print(...)`** → Prints the formatted JSON data.
# OUTPUT:
'''
[
    {
        "avatarUrls": {
            "16x16": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=xsmall",
            "24x24": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=small",
            "32x32": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=medium",
            "48x48": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400"
        },
        "entityId": "af0a1d42-f3c7-4537-a42f-ac789d29d539",
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "id": "10000",
        "isPrivate": false,
        "key": "SCRUM",
        "name": "GitHub-Jira-Integration",
        "projectTypeKey": "software",
        "properties": {},
        "self": "https://amishasharma1921.atlassian.net/rest/api/3/project/10000",
        "simplified": true,
        "style": "next-gen",
        "uuid": "af0a1d42-f3c7-4537-a42f-ac789d29d539"
    },
    {
        "avatarUrls": {
            "16x16": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=xsmall",
            "24x24": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=small",
            "32x32": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=medium",
            "48x48": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404"
        },
        "entityId": "ffe53d53-1dff-481f-86b2-1e0eec7d6d2d",
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "id": "10001",
        "isPrivate": false,
        "key": "MDP",
        "name": "My discovery project",
        "projectTypeKey": "product_discovery",
        "properties": {},
        "self": "https://amishasharma1921.atlassian.net/rest/api/3/project/10001",
        "simplified": true,
        "style": "next-gen",
        "uuid": "ffe53d53-1dff-481f-86b2-1e0eec7d6d2d"
    },
    {
        "avatarUrls": {
            "16x16": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=xsmall",
            "24x24": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=small",
            "32x32": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=medium",
            "48x48": "https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417"
        },
        "entityId": "ba50747b-7444-48cd-b99d-7896525ab04a",
        "expand": "description,lead,issueTypes,url,projectKeys,permissions,insight",
        "id": "10002",
        "isPrivate": false,
        "key": "SDSTP",
        "name": "Soft-Dev-Scrum-Template-PROJECT",
        "projectTypeKey": "software",
        "properties": {},
        "self": "https://amishasharma1921.atlassian.net/rest/api/3/project/10002",
        "simplified": true,
        "style": "next-gen",
        "uuid": "ba50747b-7444-48cd-b99d-7896525ab04a"
    }
]
'''
