# This code sample uses the 'requests' library: http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://amishasharma1921.atlassian.net/rest/api/3/issue"

    email = os.getenv("jira_email")
    API_TOKEN=os.getenv("jira_api_token")

    auth = HTTPBasicAuth(email, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {

        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Testing issue creation through github webhood sending payload to python flask app at even trigger of issue comment, then this python flask app will make API call to Jira to create an issue in Jira.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "SCRUM"
        },
        "issuetype": {
            "id": "10003"
        },
        "summary": "Issue creation through github webhook trigger make API call to python flask app, which then make API call to Jira to create an issue; Day-15",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

#app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)