original_list = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

def sort_list_by_index(lst, index):
    sorted_list = sorted(lst, key=lambda x: x[index])
    return sorted_list

print("Sort the said list of lists by a given index (Index = 0) of the inner list:")
print(sort_list_by_index(original_list, 0))

print("\nSort the said list of lists by a given index (Index = 2) of the inner list:")
print(sort_list_by_index(original_list, 2))