import itertools

def generate_combinations(iterable, r):
    return itertools.combinations(iterable, r)

data = [1, 2, 3, 4]
r = 2

combinations = generate_combinations(data, r)

print(f'Combinations of length {r}:')
for comb in combinations:
    print(comb)