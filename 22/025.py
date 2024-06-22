import itertools

def find_pair_with_sum(lst, target_sum):
    for pair in itertools.combinations(lst, 2):
        if sum(pair) == target_sum:
            return pair
    return None

lst = [10, 20, 10, 40, 50, 60, 70]
target_sum = 50
result = find_pair_with_sum(lst, target_sum)

if result:
    print(f"The first pair of elements whose sum is {target_sum} is: {result}")
else:
    print(f"No pair of elements found whose sum is {target_sum}")