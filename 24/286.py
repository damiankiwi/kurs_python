from collections import OrderedDict

ordered_dict = OrderedDict([
    ('Laptop', 40),
    ('Desktop', 45),
    ('Mobile', 35),
    ('Charger', 25)
])

print("Original OrderedDict:")
print(ordered_dict)

print("\nMove the 'Desktop' key to the end")
ordered_dict.move_to_end('Desktop')

print("\nUpdated OrderedDict:")
print(ordered_dict)