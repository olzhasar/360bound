from typing import List, Union, Dict, Set

Row = Dict[str, Union[int, List[int]]]


def get_weights(arr: List[Row]) -> Dict[str, int]:
    if not arr:
        return []

    weights: Dict[str, int] = {}

    def calc_weight(row: Row):
        key = str(row["id"])

        if key not in weights:
            weights[key] = row["weight"]

            for child in filter(lambda x: x["id"] in row["elems"], arr):
                weights[key] += calc_weight(child)

        return weights[key]

    for row in arr:
        calc_weight(row)

    return weights
