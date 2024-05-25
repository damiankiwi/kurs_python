original_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

remove_none = lambda lst: list(filter(lambda x: x is not None, lst))

filtered_list = remove_none(original_list)

print("Original list:")
print(original_list)
print("Remove None value from the said list:")
print(filtered_list)