from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 17, 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 6, 2
    parts = split_integer(value, number_of_parts)
    assert parts == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 8, 1
    parts = split_integer(value, number_of_parts)
    assert parts == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 4
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 2, 4
    parts = split_integer(value, number_of_parts)
    assert parts == [0, 0, 1, 1]
