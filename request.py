import requests
BASE = "http://localhost:5000/"
f = open("data.txt", "r")
text = f.read()
response = requests.post(BASE, {"text": text})
print(response.json())
