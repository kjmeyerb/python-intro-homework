import requests

response=requests.get("https://api.agify.io/?name=michael")
print(response.status_code)
print(response.json())