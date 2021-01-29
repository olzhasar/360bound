from typing import List, Union, Dict, Set

Row = Dict[str, Union[int, List[int]]]


def get_weights(arr: List[Row]) -> Dict[str, int]:
    if not arr:
        return []

    mapping: Dict[int, Row] = {}

    for row in arr:
        i = row["id"]
        row.pop("id")

        mapping[i] = row

    def calc_weight(row: Row):
        if not "total_weight" in row:
            row["total_weight"] = row["weight"]

            for child in row["elems"]:
                row["total_weight"] += calc_weight(mapping[child])

        return row["total_weight"]

    for row in mapping.values():
        calc_weight(row)

    return {str(key): value["total_weight"] for key, value in mapping.items()}
