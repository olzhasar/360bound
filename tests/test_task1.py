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
                {"id": 1, "weight": 1, "elems": []},
            ],
            [1],
        ],
    ],
)
def test_get_weights(arr, expected):
    assert get_weights(arr) == expected
