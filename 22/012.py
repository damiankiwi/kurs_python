import itertools

def compute_cartesian_product(*lists):
    return list(itertools.product(*lists))

list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['X', 'Y']

cartesian_product = compute_cartesian_product(list1, list2, list3)

print('Cartesian product of the given lists:')
for item in cartesian_product:
    print(item)