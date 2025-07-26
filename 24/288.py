from collections import OrderedDict

def merge_ordered_dicts(dict1, dict2):
    merged_dict = OrderedDict()

    for key, value in dict1.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict

ordered_dict1 = OrderedDict([
    ('Laptop', 40),
    ('Desktop', 45),
    ('Mobile', 35)
])
print("\nOrderedDict-1:",ordered_dict1)

ordered_dict2 = OrderedDict([
    ('Laptop', 40),
    ('Charger', 25)
])
print("\nOrderedDict-2:",ordered_dict2)
merged_ordered_dict = merge_ordered_dicts(ordered_dict1, ordered_dict2)
print("\nMerged Dictionary: ",merged_ordered_dict)