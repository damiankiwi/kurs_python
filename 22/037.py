import itertools


def add_lists_from_left(list1, list2):
    paired_elements = itertools.zip_longest(list1, list2, fillvalue=0)

    result = [sum(pair) for pair in paired_elements]

    return result


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9, 10]

result = add_lists_from_left(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Result:", result)