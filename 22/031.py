import itertools


def count_consecutive_duplicates(numbers):
    grouped = itertools.groupby(numbers)

    result = [(key, len(list(group))) for key, group in grouped]

    return result


numbers = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 7]
result = count_consecutive_duplicates(numbers)
print("Frequency of consecutive duplicate elements:")
print(result)