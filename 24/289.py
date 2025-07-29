from collections import OrderedDict

def remove_key_from_ordered_dict(od, key_to_remove):
    if key_to_remove in od:
        del od[key_to_remove]
        print(f"Key '{key_to_remove}' removed successfully.")
    else:
        print(f"Key '{key_to_remove}' not found in the OrderedDict.")

ordered_dict = OrderedDict([
    ('Laptop', 40),
    ('Desktop', 45),
    ('Mobile', 35),
    ('Charger', 25)
])

print("Original OrderedDict: ",ordered_dict)
print("\nKey to remove: 'Desktop'")
key_to_remove = 'Desktop'
remove_key_from_ordered_dict(ordered_dict, key_to_remove)

print("\nUpdated OrderedDict: ",ordered_dict)