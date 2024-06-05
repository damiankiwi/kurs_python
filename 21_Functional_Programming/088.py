def convert_strings_to_lists(list_of_strings):
    list_of_lists = list(map(list, list_of_strings))
    return list_of_lists

list_of_strings = ['Red', 'Green', 'Blue', 'White', 'Black']

result = convert_strings_to_lists(list_of_strings)

print("List of Lists:", result)