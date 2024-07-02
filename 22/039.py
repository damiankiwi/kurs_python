import itertools


def index_of_first_greater_than(iterable, threshold):
    filtered = itertools.dropwhile(lambda x: x <= threshold, iterable)

    first_greater = next(filtered, None)

    if first_greater is not None:
        index = next(i for i, x in enumerate(iterable) if x == first_greater)
        return index
    else:
        return None


numbers = [2, 4, 6, 8, 10, 12, 14]
threshold = 7
index = index_of_first_greater_than(numbers, threshold)
print(f"Index of the first element greater than {threshold}: {index}")

threshold = 15
index = index_of_first_greater_than(numbers, threshold)
print(f"Index of the first element greater than {threshold}: {index}")