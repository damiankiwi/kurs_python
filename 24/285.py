from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['Laptop'] = 40
ordered_dict['Desktop'] = 45
ordered_dict['Mobile'] = 35
ordered_dict['Charger'] = 25

reversed_dict = OrderedDict(reversed(list(ordered_dict.items())))

print("Original OrderedDict:")
print(ordered_dict)

print("\nReversed OrderedDict:")
print(reversed_dict)