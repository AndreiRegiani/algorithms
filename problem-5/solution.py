#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def combine(a, b):
    """
    >>> combine(['a', 'b', 'c'], ['1', '2', '3'])
    ['a', '1', 'b', '2', 'c', '3']
    """

    l = []
    while a or b:
        if a: l.append(a.pop(0))
        if b: l.append(b.pop(0))
    return l


if not doctest.testmod().failed:
    print("Unit tests passed")
