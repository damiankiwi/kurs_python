import itertools
import operator

def running_product(iterable):
    running_prod = itertools.accumulate(iterable, operator.mul)
    return list(running_prod)

numbers = [1, 2, 3, 4, 5]
result = running_product(numbers)

print("Original list:", numbers)
print("Running product:", result)