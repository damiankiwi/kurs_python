import itertools


def non_repeated_combinations(numbers):
    cartesian_product = itertools.product(numbers, repeat=4)

    non_repeated = [combo for combo in cartesian_product if len(set(combo)) == len(combo)]

    return non_repeated


numbers = [1, 2, 3, 4]
result = non_repeated_combinations(numbers)
print("Non-repeated combinations of the Cartesian product:")
for combo in result:
    print(combo)