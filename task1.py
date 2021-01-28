from collections import defaultdict
from typing import List, Union, Dict


def get_weights(arr: List[Dict[str, Union[int, List[int]]]]):
    if not arr:
        return []

    weights: Dict[int, int] = {}

    without_parent = list(range(1, len(arr) + 1))

    children: Dict[int, List[int]] = {}

    for row in arr:
        weights[row["id"]] = row["weight"]

        children[row["id"]] = []

        for el in row["elems"]:
            children[row["id"]].append(el)
            without_parent.remove(el)

    root = without_parent[0]

    def calc_weight(node_id: int):
        for child in children[node_id]:
            weights[node_id] += calc_weight(child)

        return weights[node_id]

    calc_weight(root)

    return [weights[i] for i in sorted(weights.keys())]
