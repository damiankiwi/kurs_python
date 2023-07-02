class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

    def add_product(self, product):
        self.products.append(product.lower())

    def remove_product(self, product):
        product = product.lower()
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"{product} nie istnieje w zamówieniu.")

    def get_order_details(self):
        return {'order_id': self.order_id, 'products': self.products}


def display_menu():
    print("===== Menu Sklepu =====")
    print("1. Wyświetl zamówienie")
    print("2. Dodaj produkt do zamówienia")
    print("3. Usuń produkt z zamówienia")
    print("4. Zakończ program")


# Tworzenie obiektu klasy Order
order = Order("12345", ["komputer", "klawiatura"])

while True:
    display_menu()
    choice = input("Wybierz opcję (1-4): ")

    if choice == '1':
        # Wyświetlanie zamówienia
        details = order.get_order_details()
        print("Numer zamówienia:", details['order_id'])
        print("Lista produktów:", details['products'])

    elif choice == '2':
        # Dodawanie produktu do zamówienia
        product = input("Podaj nazwę produktu: ")
        order.add_product(product)
        print("Produkt został dodany do zamówienia.")

    elif choice == '3':
        # Usuwanie produktu z zamówienia
        product = input("Podaj nazwę produktu do usunięcia: ")
        order.remove_product(product)
        print("Produkt został usunięty z zamówienia.")

    elif choice == '4':
        # Zakończenie programu
        print("Dziękujemy za skorzystanie z programu. Do widzenia!")
        break

    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 4.")