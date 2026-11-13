import requests

response=requests.get("https://api.agify.io", {'name':"michael"})
name_data = response.json()

print(f"Name: {name_data['name']}")
print(f"Predicted age: {name_data['age']}")
print(f"Birthday: {name_data['birthday'] if name_data.get('birthday') else "Not Given"}")