original_tuple = ('123', '456', '789', '1011', '1213')

indices_to_take = [0, 2, 4]

convert_to_integer = lambda x: int(x)

new_list = list(map(convert_to_integer, [original_tuple[i] for i in indices_to_take]))

print("Original tuple:")
print(original_tuple)
print("New list with specific elements converted to integers:")
print(new_list)