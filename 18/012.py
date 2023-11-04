from itertools import permutations

collection = [1, 2, 3]

permutation_list = list(permutations(collection))

print("Wszystkie możliwe permutacje z kolekcji:", collection)
for perm in permutation_list:
    print(perm)