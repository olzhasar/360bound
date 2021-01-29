from typing import List, Union, Dict, Set

Row = Dict[str, Union[int, List[int]]]


def get_weights(arr: List[Row]) -> Dict[str, int]:
    if not arr:
        return []

    mapping: Dict[int, row] = {}

    for row in arr:
        i = row["id"]
        row.pop("id")

        mapping[i] = row

    def calc_weight(row: Row):
        if not "full_weight" in row:
            row["full_weight"] = row["weight"]

            for child in row["elems"]:
                row["full_weight"] += calc_weight(mapping[child])

        return row["full_weight"]

    for row in arr:
        calc_weight(row)

    return {str(key): value["full_weight"] for key, value in mapping.items()}
