import urllib.request
import json
from urllib.error import HTTPError

from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("KEY")

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


try:
    response = urllib.request.urlopen(request).read().decode("utf-8")
except HTTPError as e:
    print(e.code, e.read().decode())
    exit()

data = json.loads(response)

with open("../../src/assets/cards.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, indent=4)