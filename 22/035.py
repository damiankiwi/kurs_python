import itertools

def all_combinations(lst):
    result = []
    for r in range(1, len(lst) + 1):
        combinations = list(itertools.combinations(lst, r))
        result.extend(combinations)
    return result

lst = [1, 2, 3, 4]
combinations = all_combinations(lst)

print("Original list:", lst)
print("All possible combinations:")
for combination in combinations:
    print(combination)