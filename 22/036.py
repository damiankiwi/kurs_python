import itertools


def add_lists_from_right(list1, list2):
    reversed_list1 = list1[::-1]
    reversed_list2 = list2[::-1]

    paired_elements = itertools.zip_longest(reversed_list1, reversed_list2, fillvalue=0)

    result = [sum(pair) for pair in paired_elements][::-1]

    return result


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9, 10]

result = add_lists_from_right(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Result:", result)