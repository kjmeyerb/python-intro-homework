import os
import requests

API_KEY = os.environ.get("REST_COUNTRIES_API_KEY")
if not API_KEY:
    print("No API key found. Set REST_COUNTRIES_API_KEY and try again.")
    exit()

url= 'https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population'
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(url, headers=headers)
countries = response.json()["data"]["objects"]
for country in countries[:10]:
    print(country["names"]["common"])
