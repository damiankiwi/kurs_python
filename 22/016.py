import itertools

def sorted_permutations(input_list):
    permutations = list(itertools.permutations(input_list))
    sorted_permutations = sorted(permutations)
    return sorted_permutations

input_list = ['B', 'A', 'C']

sorted_perms = sorted_permutations(input_list)

print('Sorted permutations:')
for perm in sorted_perms:
    print(perm)