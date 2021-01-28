from typing import List, Union, Dict, Set


def get_weights(arr: List[Dict[str, Union[int, List[int]]]]):
    if not arr:
        return []

    weights: List[int] = [0] * len(arr)

    top_nodes: Set[int] = set(range(1, len(arr) + 1))

    children_mapping: Dict[int, List[int]] = {}

    for row in arr:
        i = row["id"]

        weights[i - 1] = row["weight"]
        children_mapping[i] = []

        for el in row["elems"]:
            children_mapping[i].append(el)
            top_nodes.remove(el)

    def calc_weight(node_id: int):
        for child in children_mapping[node_id]:
            weights[node_id - 1] += calc_weight(child)

        return weights[node_id - 1]

    for node_id in top_nodes:
        calc_weight(node_id)

    return weights
