#!/usr/bin/env python3
""" Solution by Andrei Regiani - https://regiani.xyz """

import doctest


def cakes(recipe, available):
    """
    cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
    2

    cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})
    0
    """

    baked = 0  # total count
    while available:
        # how many ingredients is left to finish this recipe
        remaining_ingredients = len(recipe)
        for k, v in available.items():
            if k in recipe:
                if v >= recipe[k]:
                    available[k] -= recipe[k]
                    remaining_ingredients -= 1
                else:
                    del available[k]
            else:
                del available[k]
        if remaining_ingredients == 0:
                baked += 1

    return baked


if not doctest.testmod().failed:
    print("Unit tests passed")
