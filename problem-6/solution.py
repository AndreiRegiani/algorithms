#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def largest(int_list):
    """
    >>> largest([50, 2, 1, 9])
    95021
    """

    int_list = sorted(int_list, reverse=True)
    largest = ""

    for i in reversed(range(0, 10)):  # 9...0
        for integer in int_list:
            if str(integer)[0] == str(i):
                largest += str(integer)

    return int(largest)


if not doctest.testmod().failed:
    print("Unit tests passed")
