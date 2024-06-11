import itertools

def limited_permutations(iterable, r, num_permutations):
    permutations_iterator = itertools.permutations(iterable, r)
    return itertools.islice(permutations_iterator, num_permutations)

data = [1, 2, 3]
r = 2
num_permutations = 4

permutations = limited_permutations(data, r, num_permutations)

print(f'First {num_permutations} permutations of length {r}:')
for perm in permutations:
    print(perm)