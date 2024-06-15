import itertools

def generate_permutations(values, permutation_length):
    return list(itertools.permutations(values, permutation_length))

values = ['A', 'B', 'C']
permutation_length = 2

permutations = generate_permutations(values, permutation_length)

print('Permutations:')
for perm in permutations:
    print(perm)