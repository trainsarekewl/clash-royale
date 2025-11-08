from typing import Tuple

import torch
from torch.utils.data import random_split

# default ratios: 80% train, 20% val, 0% test (for now)
def split_dataset(dataset, ratios: Tuple[float, float, float] = (0.8, 0.2, 0), seed: int = 42):
    assert sum(ratios) == 1.0, "Ratios must sum to 1.0"

    total = len(dataset)
    n_train = int(total * ratios[0])
    n_val = int(total * ratios[1])
    n_test = total - n_train - n_val

    generator = torch.Generator().manual_seed(seed)
    return random_split(dataset, [n_train, n_val, n_test], generator=generator)