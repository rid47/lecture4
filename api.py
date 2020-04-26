import requests

url = "https://api-football-v1.p.rapidapi.com/v2/predictions/157462"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "9b353d1bc4msheb1f6e0bd8ea6ddp1c5536jsn8c1bd9bfef20"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
