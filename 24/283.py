from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['Laptop'] = 40
ordered_dict['Desktop'] = 45
ordered_dict['Mobile'] = 35

print("OrderedDict contents:")
for item, quantity in ordered_dict.items():
    print(f"Itemt: {item}, Quantity: {quantity}")

sorted_by_keys = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[0]))

sorted_by_values = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[1]))

print("\nSorted by keys:")
for item, quantity in sorted_by_keys.items():
    print(f"Item: {item}, Quantity: {quantity}")

print("\nSorted by values:")
for item, quantity in sorted_by_values.items():
    print(f"Item: {item}, Quantity: {quantity}")