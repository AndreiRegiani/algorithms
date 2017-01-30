def cakes(recipe, available):
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
