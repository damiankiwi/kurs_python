class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item_price):
        if item_name in self.items:
            print(f"{item_name} is already in the cart.")
        else:
            self.items[item_name] = item_price
            print(f"{item_name} added to the cart.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from the cart.")
        else:
            print(f"{item_name} is not in the cart.")

    def calculate_total(self):
        total_price = sum(self.items.values())
        return total_price

cart = ShoppingCart()

cart.add_item("Apple", 2.5)
cart.add_item("Banana", 1.8)
cart.add_item("Orange", 3.0)

cart.remove_item("Banana")

total_price = cart.calculate_total()
print(f"\nTotal price of items in the cart: ${total_price:.2f}")