import requests
BASE = "http://localhost:5000/"

response = requests.post(BASE + "user")
print(response.json())
