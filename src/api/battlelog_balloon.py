import urllib.request
import json
from urllib.error import HTTPError
from urllib.parse import quote

from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("KEY")
player_tag = quote(os.getenv("PLAYER_TAG"))
base_url = "https://api.clashroyale.com/v1"

endpoint = f"/players/{player_tag}/battlelog"

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

battlelog_path = "../assets/battlelog_balloon.json"

# add more to battle log
if os.path.exists(battlelog_path):
    with open(battlelog_path, "r", encoding = "utf-8") as f:
        old_data = json.load(f)

else:
    old_data = []

merged = data + old_data

seen = set()
unique = []

target_deck = {"Musketeer", "Skeletons", "Giant Snowball", "Bomb Tower",
               "Balloon", "Miner", "Ice Golem", "Barbarian Barrel"}

# create battle log
for battle in merged:
    battle_id = battle.get("battleTime")
    battle_type = battle.get("type")

    battle_deck = {card["name"] for card in battle["team"][0]["cards"]}

    # make sure it is ranked, using the correct deck, and not duplicate
    if (battle_id not in seen
        and battle_type == "pathOfLegend"
        and battle_deck == target_deck):

        seen.add(battle_id)
        unique.append(battle)

with open(battlelog_path, "w", encoding = "utf-8") as f:
    json.dump(unique, f, indent=4)