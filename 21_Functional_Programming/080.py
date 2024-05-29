list_of_integers = [1, 2, 3, 4, 5]

tuple_of_integers = (6, 7, 8, 9, 10)

convert_to_string = lambda x: str(x)

list_of_strings_from_list = list(map(convert_to_string, list_of_integers))

list_of_strings_from_tuple = list(map(convert_to_string, tuple_of_integers))

combined_list_of_strings = list_of_strings_from_list + list_of_strings_from_tuple

print("Original list of integers:")
print(list_of_integers)
print("Original tuple of integers:")
print(tuple_of_integers)
print("List of strings from the given list of integers:")
print(list_of_strings_from_list)
print("List of strings from the given tuple of integers:")
print(list_of_strings_from_tuple)
print("Combined list of strings:")
print(combined_list_of_strings)