import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
data = response.json()
#for i in data:
for i in range(len(data)):
    print(data[i]["id"])
