# This code sample uses the 'requests' library: http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://amishasharma1921.atlassian.net/rest/api/3/issue"

email = os.getenv("jira_email")
api_token = os.getenv("jira_api_token")

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# data to be sent while making POST HTTP request to create JIRA issue with the given fields
payload = json.dumps( {
  "fields": {

    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Testing 1st ticket creation through python scripy, by calling Jira API Post HTTP request",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },

    "issuetype": {
      "id": "10001"     # 10001 to create 'Task' 
      # To view issue type IDs; top right side '...' -> configure board -> issue type -> see url for id
    },
    "project": {
      "id": "10000"
    },

    "summary": "Issue creation through python script: jira-create-issue.py from Day-14",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))