def split_dict_of_lists(dict_of_lists):
    length = len(next(iter(dict_of_lists.values())))

    list_of_dicts = list(map(lambda i: {key: value[i] for key, value in dict_of_lists.items()}, range(length)))

    return list_of_dicts


dict_of_lists = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

result = split_dict_of_lists(dict_of_lists)

print("List of Dictionaries:", result)