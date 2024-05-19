from functools import reduce

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

list1 = [4, 3, 2, 2, -1, 18]
print("Original list:")
print(list1)
print("Multiply all the numbers of the said list:")
print(multiply_list(list1))

list2 = [2, 4, 8, 8, 3, 2, 9]
print("\nOriginal list:")
print(list2)
print("Multiply all the numbers of the said list:")
print(multiply_list(list2))