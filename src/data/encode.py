import json
import numpy as np
from pathlib import Path

# create dictionary for converting card id to index from 0 to n-1
def load_card_index_dict(cards_json_path: str = "../assets/cards.json"):
    data = json.loads(Path(cards_json_path).read_text(encoding="utf-8"))
    cards = data["items"]
    index_map = {card["id"]: i for i, card in enumerate(cards)}
    return index_map, len(index_map)

# if card is present in opponent deck, set the value at the card id to 1
def one_hot_deck(card_ids: list[int], n_cards:int) -> np.ndarray:
    vec = np.zeros(n_cards, dtype=np.float32)
    for id in card_ids:
        vec[id] = 1
    return vec

def encode_opponent_deck(opponent_cards: list[int], n_cards: int) -> np.ndarray:
    return one_hot_deck(opponent_cards, n_cards)