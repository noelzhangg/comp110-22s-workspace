"""Define at least 3x unit test functions for only_evens, sub, and concat."""

__author__ = "730490949"


from utils import only_evens, sub, concat


def test_only_evens_multiple_integers() -> None:
    """Testing for even numbers in a list containing multiple integers with odd and even integers - use case."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_odd_integers() -> None:
    """Testing for even numbers in a list containing only odd integers - edge case."""
    assert only_evens([1, 1, 1]) == []


def test_only_evens_all_even_integers() -> None:
    """Testing for even numbers in a list ocntaining only even integers - use case."""
    assert only_evens([2, 10, 100]) == [2, 10, 100]


def test_sub_indecies_within_len_range() -> None:
    """Listing the values within given indices that are less than the len value - use case."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_indecies_less_than_len_value() -> None:
    """Listing the values within given indices that are less than the len value - use case."""
    assert sub([30, 30, 30, 30, 30, 30], 2, 4) == [30, 30]


def test_sub_negative_indices() -> None:
    """Listing the values between a negative start index and positive index less than len value - edge case."""
    assert sub([1, 2, 3, 4], -1, 2) == [1, 2]


def test_concat_positive_integers() -> None:
    """Combining two lists that both contain only positive integers - use case."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_negative_integers() -> None:
    """Combining two lists that both contain only negative integers - use case."""
    assert concat([-1, -2, -3], [-4, -5, -6]) == [-1, -2, -3, -4, -5, -6]


def test_concat_empty_lists() -> None:
    """Combining two empty lists - edge case."""
    assert concat([], []) == []