#8. Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.

# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
# model (str)
# rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

def car_info():
    car_brand = str(input("Wpisz markę auta: "))
    car_model = str(input("Wpisz model auta: "))
    car_year = int(input("Wpisz rocznik auta: "))

    create_dictionary(car_brand, car_model, car_year)
    check_year(car_brand, car_year)

def create_dictionary(car_brand, car_model, car_year):
    car_dictionary = {}
    car_dictionary["marka"] = car_brand
    car_dictionary["model"] = car_model
    car_dictionary["rocznik"] = car_year
    print(car_dictionary)

def check_year(car_brand,car_year):
    current_year = 2023
    if current_year - car_year >= 25:
        print(f"Gratulacje twój samochód {car_brand} może zostać zarejestorwany jako zabytek.")
    else:
        print(f"Twój samochód {car_brand} jest zbyt młody żeby zostać zabytkiem.")

car_info()