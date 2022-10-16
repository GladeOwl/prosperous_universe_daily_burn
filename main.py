import requests

url = "https://rest.fnar.net/auth/login"
data = {"UserName": "GladeOwl", "Password": "v*DY8k8W6zVEd22"}

response = requests.post(url=url, json=data)
print(response.text)
