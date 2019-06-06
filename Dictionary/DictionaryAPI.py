import requests
import json
app_id = "60edc74a"
app_key = "6b8466506d884d62a86f1e2d283f2286"
language = "en-gb"
word_id = "example"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print(r.text)