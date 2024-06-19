import itertools
import operator

def factorial(n):
    numbers = range(1, n + 1)

    factorials = itertools.accumulate(numbers, operator.mul)

    return list(factorials)[-1]

print(factorial(5))
print(factorial(10))