# IMPORTS REQUIRED LIBRARIES
import requests
from requests.auth import HTTPBasicAuth
import json
import os

# JIRA API URL SETUP
url = "https://amishasharma1921.atlassian.net/rest/api/3/project"

# SECURELY FETCH CREDENTIALS
email = os.getenv("jira_email")
API_TOKEN= os.getenv('jira_api_token')

# SET UP AUTHENTICATION
auth = HTTPBasicAuth(email, API_TOKEN)

# DEFINE HEADERS - to define response format, json here
headers = {
  "Accept": "application/json"
}

# MAKE A GET REQUEST TO JIRA API
response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# Printing the response code; if API request to JIRA API was successful (status code-200)
#print(response)           # <Response [200]>
#print(response.text)      # 
'''
[{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10000","id":"10000","key":"SCRUM","name":"GitHub-Jira-Integration","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=medium"},"projectTypeKey":"software","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"af0a1d42-f3c7-4537-a42f-ac789d29d539","uuid":"af0a1d42-f3c7-4537-a42f-ac789d29d539"},{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10001","id":"10001","key":"MDP","name":"My discovery project","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=medium"},"projectTypeKey":"product_discovery","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"ffe53d53-1dff-481f-86b2-1e0eec7d6d2d","uuid":"ffe53d53-1dff-481f-86b2-1e0eec7d6d2d"},{"expand":"description,lead,issueTypes,url,projectKeys,permissions,insight","self":"https://amishasharma1921.atlassian.net/rest/api/3/project/10002","id":"10002","key":"SDSTP","name":"Soft-Dev-Scrum-Template-PROJECT","avatarUrls":{"48x48":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417","24x24":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=small","16x16":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=xsmall","32x32":"https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=medium"},"projectTypeKey":"software","simplified":true,"style":"next-gen","isPrivate":false,"properties":{},"entityId":"ba50747b-7444-48cd-b99d-7896525ab04a","uuid":"ba50747b-7444-48cd-b99d-7896525ab04a"}]
'''


output = json.loads(response.text)    # usable response; by converting from raw json str to usable dict
#print(output)             # 
'''
[{'expand': 'description,lead,issueTypes,url,projectKeys,permissions,insight', 'self': 'https://amishasharma1921.atlassian.net/rest/api/3/project/10000', 'id': '10000', 'key': 'SCRUM', 'name': 'GitHub-Jira-Integration', 'avatarUrls': {'48x48': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400', '24x24': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=small', '16x16': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=xsmall', '32x32': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10400?size=medium'}, 'projectTypeKey': 'software', 'simplified': True, 'style': 'next-gen', 'isPrivate': False, 'properties': {}, 'entityId': 'af0a1d42-f3c7-4537-a42f-ac789d29d539', 'uuid': 'af0a1d42-f3c7-4537-a42f-ac789d29d539'}, {'expand': 'description,lead,issueTypes,url,projectKeys,permissions,insight', 'self': 'https://amishasharma1921.atlassian.net/rest/api/3/project/10001', 'id': '10001', 'key': 'MDP', 'name': 'My discovery project', 'avatarUrls': {'48x48': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404', '24x24': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=small', '16x16': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=xsmall', '32x32': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10404?size=medium'}, 'projectTypeKey': 'product_discovery', 'simplified': True, 'style': 'next-gen', 'isPrivate': False, 'properties': {}, 'entityId': 'ffe53d53-1dff-481f-86b2-1e0eec7d6d2d', 'uuid': 'ffe53d53-1dff-481f-86b2-1e0eec7d6d2d'}, {'expand': 'description,lead,issueTypes,url,projectKeys,permissions,insight', 'self': 'https://amishasharma1921.atlassian.net/rest/api/3/project/10002', 'id': '10002', 'key': 'SDSTP', 'name': 'Soft-Dev-Scrum-Template-PROJECT', 'avatarUrls': {'48x48': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417', '24x24': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=small', '16x16': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=xsmall', '32x32': 'https://amishasharma1921.atlassian.net/rest/api/3/universal_avatar/view/type/project/avatar/10417?size=medium'}, 'projectTypeKey': 'software', 'simplified': True, 'style': 'next-gen', 'isPrivate': False, 'properties': {}, 'entityId': 'ba50747b-7444-48cd-b99d-7896525ab04a', 'uuid': 'ba50747b-7444-48cd-b99d-7896525ab04a'}]
'''

'''
response.text → This contains the raw JSON response from the Jira API as a string.
json.loads(response.text) → Converts the JSON string into a Python list or dictionary (depending on the structure of the response).
output → Now holds the parsed JSON data as a Python list of dictionaries.

Before json.loads(): response.text is a string (not usable as a Python object).
After json.loads(): output becomes a list of dictionaries in Python.
'''

# printing the 1st dictionary value of key 'name' of this output list

#name = response.text[0]["name"]
#print(name)
'''
Traceback (most recent call last):
  File "/home/asharma/devops/Python/python-for-devops_AV/Day-14/Practice-Test/jira-list-all-projects-names.py", line 42, in <module>
    name = response.text[0]["name"]
TypeError: string indices must be integers
'''
# Error Because Before json.loads(): response.text is a string (not usable as a Python object).

# After json.loads(): output becomes a list of dictionaries in Python and hence usable.
#name = output[0]["name"]
# Printing the 1st project name from JIRA API response
#print(name)             # GitHub-Jira-Integration

# Display all project names in the Jira account
for list_item in output:
    print(list_item['name'])

# TO understand the traversing, print response with formatting and indentation for readability
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))