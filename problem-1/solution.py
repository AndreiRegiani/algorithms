#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution by Andrei Regiani
https://regiani.xyz
"""

import sys
import doctest


def special_sort(line_input):
    """
    >>> special_sort('1')
    '1'

    >>> special_sort('car truck bus')
    'bus car truck'

    >>> special_sort('8 4 6 1 -2 9 5')
    '-2 1 4 5 6 8 9'

    >>> special_sort('car truck 8 4 bus 6 1')
    'bus car 1 4 truck 6 8'

    >>> special_sort('')
    ''
    """

    line_input = line_input.split()
    int_list = []
    str_list = []
    index_list = []  # 'str' or 'int', to save positions
    final_list = []  # sorted output

    for i in line_input:
        try:
            int(i)
            int_list.append(i)
            index_list.append('int')
        except ValueError:
            str_list.append(i)
            index_list.append('str')

    # sort individual lists
    int_list = sorted(int_list, key=int)
    str_list = sorted(str_list, key=str.lower)

    # create final list
    for i in index_list:
        if i == 'int':
            final_list.append(int_list.pop(0))
        else:  # 'str'
            final_list.append(str_list.pop(0))
    return ' '.join(final_list)


def main():
    doctest.testmod()
    while True:
        try:
            line = input('Input: ')  # space-separated values
        except KeyboardInterrupt:
            sys.exit(0)
        print('Output:', special_sort(line), '\n')


if __name__ == '__main__':
    main()
