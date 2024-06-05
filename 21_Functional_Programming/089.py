def tuples_to_strings(list_of_tuples):
    list_of_strings = list(map(lambda t: ''.join(map(str, t)), list_of_tuples))
    return list_of_strings

list_of_tuples = [(1, 2), (3, 4), (5, 6), ('a', 'b')]

result = tuples_to_strings(list_of_tuples)
print("List of Strings:", result)