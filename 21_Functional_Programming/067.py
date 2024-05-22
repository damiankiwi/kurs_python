original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

def sort_mixed_list(lst):
    numbers = sorted(filter(lambda x: isinstance(x, int), lst))
    strings = sorted(filter(lambda x: isinstance(x, str), lst))
    return numbers + strings

sorted_list = sort_mixed_list(original_list)

print("Original list:")
print(original_list)
print("Sort the said mixed list of integers and strings:")
print(sorted_list)