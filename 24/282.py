from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict['Laptop'] = 15
ordered_dict['Desktop'] = 40
ordered_dict['Mobile'] = 50

for item, quantity in ordered_dict.items():
    print(f"Itemt: {item}, Quantity: {quantity}")