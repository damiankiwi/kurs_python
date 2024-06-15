import itertools

def generate_all_permutations(objects):
    return list(itertools.permutations(objects))

objects = ['A', 'B', 'C']

permutations = generate_all_permutations(objects)

print('All possible permutations:')
for perm in permutations:
    print(perm)