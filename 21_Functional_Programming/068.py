original_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

def sort_numerically(lst):
    return sorted(lst, key=lambda x: int(x))

sorted_list = sort_numerically(original_list)

print("Original list:")
print(original_list)
print("Sort the said list of strings(numbers) numerically:")
print(sorted_list)