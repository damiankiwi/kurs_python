from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['Laptop'] = 40
ordered_dict['Desktop'] = 45
ordered_dict['Mobile'] = 35

item = ordered_dict['Desktop']
print(f"Quantity of Desktops: {item}")

item_to_check = 'Mobile'
if item_to_check in ordered_dict:
    print(f"{item_to_check} exists in the OrderedDict")
else:
    print(f"{item_to_check} does not exist in the OrderedDict")

item_to_check = 'Charger'
if item_to_check in ordered_dict:
    print(f"{item_to_check} exists in the OrderedDict")
else:
    print(f"{item_to_check} does not exist in the OrderedDict")