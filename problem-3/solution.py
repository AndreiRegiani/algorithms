#!/usr/bin/env python3
import doctest


def reverse_message(text):
    """
    >>> reverse_message('others on depend not do salvation own your out work')
    'work out your own salvation do not depend on others'
    """

    return ' '.join(reversed(text.split()))


if not doctest.testmod().failed:
    print("Unit tests passed")
