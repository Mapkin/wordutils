from __future__ import division


def split_num(n, s):
    """
    Split n into groups of s numbers

    >>> split_num(123, 2)
    [1, 23]

    >>> split_num(12345, 3)
    [12, 345]

    >>> split_num(123, 4)
    [123]

    """
    groups = []
    div = 10 ** s
    while n:
        groups.append(n % div)
        n //= div
    groups.reverse()

    return groups
