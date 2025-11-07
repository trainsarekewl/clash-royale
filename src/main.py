import urllib.request
import json

with open("src/key.txt") as f:
    key = f.read().rstrip("\n")

base_url = "https://api.clashroyale.com/v1"

endpoint = "/cards"

request = urllib.request.Request(
    base_url + endpoint,
    None,
    headers={
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
        "User-Agent": "python-urllib"
    }
)


response = urllib.request.urlopen(request).read().decode("utf-8")
data = json.loads(response)

with open("cards.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, indent=4)

print(response)