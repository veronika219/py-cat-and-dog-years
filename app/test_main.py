from app.main import get_human_age

def test_check_if_cat_age_is_equal_0() -> None:
    assert get_human_age(0, 98) == [0, 3]

def test_if_animals_age_less_15_equal_empty_list() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_check_if_both_age_14_boundary() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_check_if_dog_age_is_equal_0() -> None:
    assert get_human_age(98, 0) == [3, 0]

def test_check_if_both_age_is_15() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_check_if_both_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_check_if_max_age_for_both() -> None:
    assert get_human_age(28,29) == [3, 3]