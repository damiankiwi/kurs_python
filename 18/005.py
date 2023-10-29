import itertools

cyfry = list(range(10))
kombinacje = list(itertools.combinations(cyfry, 3))

for kombinacja in kombinacje:
    print(kombinacja)