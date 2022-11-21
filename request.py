import requests
BASE = "http://localhost:5000/"

response = requests.post(BASE, {"text": "hellow"})
print(response.json())
