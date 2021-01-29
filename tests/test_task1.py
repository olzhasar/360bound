from task1 import get_weights

import pytest


@pytest.mark.parametrize(
    "arr, expected",
    [
        [
            [
                {"id": 1, "weight": 1, "elems": [2, 3]},
                {"id": 2, "weight": 2, "elems": []},
                {"id": 3, "weight": 3, "elems": [4]},
                {"id": 4, "weight": 4, "elems": []},
                {"id": 5, "weight": 5, "elems": [1]},
            ],
            [10, 2, 7, 4, 15],
        ],
        [
            [
                {"id": 1, "weight": 3, "elems": [5]},
                {"id": 2, "weight": 1, "elems": []},
                {"id": 3, "weight": 5, "elems": [4]},
                {"id": 4, "weight": 1, "elems": [7]},
                {"id": 5, "weight": 4, "elems": [2, 6]},
                {"id": 6, "weight": 2, "elems": []},
                {"id": 7, "weight": 2, "elems": []},
            ],
            [10, 1, 8, 3, 7, 2, 2],
        ],
        [
            [
                {"id": 1, "weight": 1, "elems": []},
            ],
            [1],
        ],
    ],
)
def test_get_weights(arr, expected):
    assert get_weights(arr) == expected
