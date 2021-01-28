from collections import defaultdict
from typing import List, Union, Dict


def get_weights(arr: List[Dict[str, Union[int, List[int]]]]):
    if not arr:
        return []

    l = len(arr)

    weights: List[int] = [0] * l

    without_parent: List[int] = list(range(1, l + 1))

    children_mapping: Dict[int, List[int]] = {}

    for row in arr:
        i = row["id"]

        weights[i - 1] = row["weight"]
        children_mapping[i] = []

        for el in row["elems"]:
            children_mapping[i].append(el)
            without_parent.remove(el)

    root_id = without_parent[0]

    def calc_weight(node_id: int):
        for child in children_mapping[node_id]:
            weights[node_id - 1] += calc_weight(child)

        return weights[node_id - 1]

    calc_weight(root_id)

    return weights
