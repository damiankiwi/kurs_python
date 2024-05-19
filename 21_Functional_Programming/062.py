from functools import reduce

def product_of_list(lst):
    return reduce(lambda x, y: x * y, lst)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List 1:", list1)
print("Product of the said list numbers:", product_of_list(list1))

list2 = [2.2, 4.12, 6.6, 8.1, 8.3]
print("\nList 2:", list2)
print("Product of the said list numbers:", product_of_list(list2))