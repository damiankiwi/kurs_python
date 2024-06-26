import itertools

def interleave_lists(*lists):
    interleaved = list(itertools.chain(*zip(*lists)))
    return interleaved

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

result = interleave_lists(list1, list2, list3)
print(f"Interleaved list: {result}")