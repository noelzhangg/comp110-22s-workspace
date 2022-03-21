"""Practice Questions for Quiz 2."""


def odd_and_even(x: list[int]) -> list[int]:
    resulting_dict: list[int] = []
    i: int = 0
    while i < len(x):
        if x[i] % 2 != 0 and i % 2 == 0:
            resulting_dict.append(x[i])
        i += 1
    return resulting_dict