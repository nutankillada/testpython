# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://prashantsukhadeve123.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("prashantsukhadeve123@gmail.com", "JIRA_TOKEN")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output = json.loads(response.text)
name = output[1]["name"]
print (name)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

