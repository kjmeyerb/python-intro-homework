import requests

try:
    response = requests.get("https://thisurldoesnotexist.example.com")
    if response.status_code != 200:
        print("Network Error: " & {response.status_code})
        exit()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    pass