import itertools


def interleave_lists(*lists):
    interleaved = itertools.zip_longest(*lists, fillvalue=None)

    result = [item for sublist in interleaved for item in sublist if item is not None]

    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list3 = [100, 200]

result = interleave_lists(list1, list2, list3)

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Interleaved result:", result)