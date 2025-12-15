import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0,0], id="check empty list"),
        pytest.param(0, 98, [0, 3], id ="check if only cat age is equal 0"),
        pytest.param(98, 0, [3, 0], id="check if only dog age is equal 0"),
        pytest.param(14, 14, [0, 0], id="check if both age 14 boundary"),
        pytest.param(15, 15, [1, 1], id="check if both age is 15"),
        pytest.param(24, 24, [2, 2], id="check if both age is 24"),
        pytest.param(28, 29, [3, 3], id="check unic-max age for both")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
