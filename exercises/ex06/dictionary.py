"""Invert, favorite_color, and count function definitions."""

__author__ = "730490949"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values. The keys of the input list becomes the values of the output list and vise versa."""
    reverse_dictionary: dict[str, str] = {}
    for key in a:
        original_value = a[key]
        if original_value in reverse_dictionary:
            raise KeyError("KeyError")
        reverse_dictionary[original_value] = key
    return reverse_dictionary


def favorite_color(b: dict[str, str]) -> str:
    """Given names and facorite colors, return the color that appears most fequently."""
    color_tracker: dict[str, int] = {}
    for key in b:
        color_value = b[key]
        if color_value in color_tracker:
            color_tracker[color_value] += 1
        else:
            color_tracker[color_value] = 1
    color_max: str = ""
    max: int = 0
    for color, count in color_tracker.items():
        if count > max:
            max = count
            color_max = color
    return color_max


def count(c: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    resulting_dictionary: dict[str, int] = {}
    for key in c:
        if key in resulting_dictionary:
            resulting_dictionary[key] += 1
        else:
            resulting_dictionary[key] = 1
    return resulting_dictionary