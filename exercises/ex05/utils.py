"""Where you will implement function skeletons and implementations below."""

__author__ = "730490949"


def only_evens(xs: list[int]) -> list[int]:
    """Return only even integers in a given list."""
    i: int = 0
    x: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            x.append(xs[i])
        i += 1
    return x


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Given a list of ints, and a start and end index, sub should generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    y: int = b
    z: list[int] = []
    if y < 0:
        y = 0
    if len(a) == 0 or b > len(a) or c <= 0:
        return z
    if c > len(a):
        c = len(a)
    while y < c:
        z.append(a[y])
        y += 1
    return z


def concat(d: list[int], e: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    f: int = 0
    h: int = 0
    g: list[int] = []
    while f < len(d):
        g.append(d[f])
        f += 1
    while h < len(e):
        g.append(e[h])
        h += 1
    return g
