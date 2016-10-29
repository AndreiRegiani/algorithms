#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


# Quick solution
def solution_1(int_list):
    """
    >>> solution_1([2, 4, 0, 100, 4, 11, 2602, 36])
    11

    >>> solution_1([160, 3, 1719, 19, 11, 13, -21])
    160
    """

    odds = [x for x in int_list if x % 2]
    evens = set(odds) ^ set(int_list)
    if len(evens) >= len(odds): return odds.pop()
    return evens.pop()


# Much better performance, can handle any amount of data
def solution_2(int_list):
    """
    >>> solution_2([2, 4, 0, 100, 4, 11, 2602, 36])
    11

    >>> solution_2([160, 3, 1719, 19, 11, 13, -21])
    160
    """

    checks = []
    checks.append(int_list[0] % 2 == 0)
    checks.append(int_list[1] % 2 == 0)
    checks.append(int_list[2] % 2 == 0)
    if checks.count(True) >= 2:
        for i in int_list:
            if i % 2 != 0:
                return i
    else:
        for i in int_list:
            if i % 2 == 0:
                return i


if not doctest.testmod().failed:
    print("Unit tests passed")
