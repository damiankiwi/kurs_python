frozen_set = frozenset([1, 2, 3, 4, 5])
regular_set = set([3, 4, 5, 6, 7])

converted_to_set = set(frozen_set)

converted_to_frozenset = frozenset(regular_set)

print("Frozen Set:", frozen_set)
print("Type of Frozen Set:", type(frozen_set))
print("\nConverted to Set:", converted_to_set)
print("Type of Converted Set:", type(converted_to_set))
print("\nRegular Set:", regular_set)
print("Type of Regular Set:", type(regular_set))
print("\nConverted to Frozen Set:", converted_to_frozenset)
print("Type of Converted Frozen Set:", type(converted_to_frozenset))