import requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en/hello"
response = requests.get(url)
if response.status_code == 200:
   data = response.json()
   print(data[0]["phonetics"])
else:
    print(f"Request failed with status code {response.status_code}")
    