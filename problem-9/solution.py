#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def to_camel_case(text):
    """
    >>> to_camel_case("the_stealth_warrior")
    'theStealthWarrior'

    >>> to_camel_case("The-Stealth-Warrior")
    'TheStealthWarrior'
    """

    separators = ('-', '_')
    text = list(text)
    for index, value in enumerate(text):
        if value in separators:
            if index != 0:
                text[index+1] = text[index+1].upper()
            del text[index]

    return ''.join(text)


if not doctest.testmod().failed:
    print("Unit tests passed")
