#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def forloop(number_list):
    """
    >>> forloop([2, 3, 5, 10, 80])
    100
    """

    sum = 0
    for i in number_list:
        sum += i
    return sum


def whileloop(number_list):
    """
    >>> whileloop([2, 3, 5, 10, 80])
    100
    """

    sum = 0
    while number_list:
        sum += number_list[0]
        number_list.pop(0)
    return sum


def recursion(number_list):
    """
    >>> recursion([2, 3, 5, 10, 80])
    100
    """

    if len(number_list) == 1:
        return number_list[0]
    return number_list[0] + recursion(number_list[1:])


if not doctest.testmod().failed:
    print("Unit tests passed")
