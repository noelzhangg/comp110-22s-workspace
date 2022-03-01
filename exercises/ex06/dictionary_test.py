"""Define at least 3x unit test functions for invert, favorite_colors, and count."""

__author__ = "730490949"

from dictionary import invert, favorite_color, count

import pytest


def test_invert_letters() -> None:
    """Invert letter assigned to keys and values wtihin the dictionary - use case."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None:
    """Invert words assigned to keys and values within the dictionary - use case."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_error() -> None:
    """Invert keys and values with the same key name - edge case."""
    with pytest.raises(KeyError):
        invert({'kris': 'jordan', 'michael': 'jordan'})


def test_favorite_color() -> None:
    """Print the color that is chosen most frequently - use case."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_same_colors() -> None:
    """Print the color that is chosen most frequently when all colors are the same - use case."""
    assert favorite_color({"John": "prink", "Noel": "pink", "Rindha": "pink"}) == "pink"


def test_favorite_color_two_color_same_max() -> None:
    """If two colors have the same max frequency, print the color that appears first in the dictionary - edge case."""
    assert favorite_color({"Noel": "blue", "Julia": "green", "Anna": "blue", "Kayla": "green"}) == "blue"


def test_count_numbers() -> None:
    """Given a list of numebrs, produce a dict that displays how many times a number was shown in the list - use case."""
    assert count(["1", "2", "3", "4", "5", "3", "1"]) == {"1": 2, "2": 1, "3": 2, "4": 1, "5": 1}


def test_count_duplicate_numbers() -> None:
    """Given a list of duplicate numebrs, produce a dict that displays how many times a number was shown in the list - use case."""
    assert count(["33", "44", "55", "66", "77", "44", "33", "77", "66", "55"]) == {"33": 2, "44": 2, "55": 2, "66": 2, "77": 2}


def test_count_no_number_repeats() -> None:
    """Given an empty list of numbers, produce a empty dict - edge case."""
    assert count([]) == {}