#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def namelist(names):
    """
    >>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Andrei'}])
    'Bart, Lisa, Maggie & Andrei'

    >>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
    'Bart, Lisa & Maggie'

    >>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}])
    'Bart & Lisa'

    >>> namelist([{'name': 'Bart'}])
    'Bart'

    >>> namelist([])
    ''
    """

    # get just the name values from dict [{'name': 'Bart'}, ...]
    names = [i['name'] for i in names]

    # no names
    if len(names) == 0:
        return ''

    # one name
    if len(names) == 1:
        return names[0]

    # two names
    if len(names) == 2:
        return "{} & {}".format(names[0], names[1])

    # multiple names
    else:
        last_name = names.pop()
        buffer = ', '.join(names)
        buffer += ' & {}'.format(last_name)
        return buffer


if not doctest.testmod().failed:
    print("Unit tests passed")
