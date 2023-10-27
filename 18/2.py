from itertools import permutations

znaki = ['a', 'e', 'i', 'o', 'I']

permutacje = list(permutations(znaki))

ciagi = [''.join(perm) for perm in permutacje]

for ciag in ciagi:
    print(ciag)