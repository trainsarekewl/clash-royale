import json
import torch
from torch.utils.data import Dataset
from pathlib import Path
from encode import encode_opponent_deck

class BattlelogDataset(Dataset):
    def __init__(self, battlelog_path: str, card_index: dict, n_cards: int):
        data = json.loads(Path(battlelog_path).read_text(encoding="utf-8"))
        self.datapoints = []

        # iterate through all battles
        for battles in data:
            # create array of opponent cards ids
            opponent_cards = [card["id"] for card in battles["opponents"][0]["cards"]]

            # turn into one hot vector
            x = encode_opponent_deck([card_index[cid] for cid in opponent_cards], n_cards)

            my_crowns = battles["team"][0]["crowns"]
            opp_crowns = battles["opponents"][0]["crowns"]

            y = 1.0 if my_crowns > opp_crowns else 0.0

            self.datapoints.append((x, y))

    def __len__(self):
        return len(self.datapoints)

    def __getitem__(self, indx):
        x, y = self.datapoints[indx]
        return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)
