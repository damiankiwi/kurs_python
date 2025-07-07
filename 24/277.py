from collections import namedtuple

Item = namedtuple("Item", ["name", "price"])

def get_item_info(item):
    return item.name, item.price

items = [
    Item(name="Mobile", price=300.00),
    Item(name="Desktop", price=1500.00),
    Item(name="Laptop", price=1200.00)
]

for item in items:
    item_name, item_price = get_item_info(item)
    print("Item Name:", item_name)
    print("Item Price:", item_price)
    print()