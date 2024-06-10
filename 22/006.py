import itertools

def drop_until_positive(iterable):
    return itertools.dropwhile(lambda x: x <= 0, iterable)

input_list = [-1, -2, -3, 4, 5, -6, 7, 8, -9]

iterator = drop_until_positive(input_list)

remaining_elements = list(iterator)
print("Remaining elements after dropping until the first positive number:")
print(remaining_elements)