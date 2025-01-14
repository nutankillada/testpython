'''
# github api url?
# get response [http respnse - json] from that url - requests module; requests.get() method
# convert json to dict (by default here) and filter required detail of PR and then user
# print it and process/count(PR by a user) if needed
'''

# requests - python library for making HTTP requests to interact with web services and APIs. It simplifies sending requests, handling responses, and managing common HTTP tasks, such as headers, form data, cookies, and more.
import requests

# google -- github api documentation -- quickstart -- home -- pull requests -- GET the URL
# Use the REST API to interact with pull requests (You can list, view, edit, create, and merge pull requests using the REST API)
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# get the response back from this url, containing all the PR details
response = requests.get(url)    #<Response [200]>

complete_PR_details = response.json()   # list of dictionary items - [ {}, {}, {}, {}, {} ]
#print(complete_PR_details)

# Displaying the latest PR details:
latest_user = complete_PR_details[0]["user"]["login"]     # user name who created latest PR
latest_PR_creation_time = complete_PR_details[0]["created_at"]     # time when latest PR was created
print("\n----------- Latest PR was created by '{}' at '{}' --------------".format(latest_user, latest_PR_creation_time))

# Displaying the users list who created PRs with creation time:
##users_list = []
PR_dict = {}
i=1
user_count_dict = {}
output_list = []
for PR in complete_PR_details:
    user = PR["user"]["login"]
    creation_time = PR["created_at"]
    ##users_list.append(user)

    sub_dict = {"user":user, "created_at":creation_time}
    ##PR_dict["user-"+str(i)] = sub_dict
    #PR_dict["creation_time"+str(i)] = creation_time
    #print(user)
    output_list.append(sub_dict)
    i += 1

    if user in user_count_dict:
        user_count_dict[user] += 1
    else:
        user_count_dict[user] = 1

##users_set = set(users_list)     # unique users/ non-repititive
#print(users_list)
##print(users_set)
##print("-------------------------------------")
##print(PR_dict)      # final output

print("\n------------ Users and creation time details of PRs -------------")
print(output_list)

#for key,value in PR_dict:
#    print(key + ": " + value)
print("\n----------- User Count for PRs created ------------")
print(user_count_dict)