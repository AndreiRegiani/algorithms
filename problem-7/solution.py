#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def iq_test(numbers):
    """
    >>> iq_test("2 4 7 8 10")
    3

    >>> iq_test("1 2 1 1")
    2
    """

    numbers = numbers.split()
    odds, evens = [], []

    for index, i in enumerate(numbers):
        if int(i) % 2 == 0:
            evens.append(index+1)
        else:
            odds.append(index+1)

    if len(odds) < len(evens):
        return odds.pop()
    else:
        return evens.pop()


if not doctest.testmod().failed:
    print("Unit tests passed")
