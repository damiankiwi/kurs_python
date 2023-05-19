# #9. Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#
# ponownie wyświetl zmieniony słownik
#
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

def car_info():
    car_brand = str(input("Wpisz markę auta: "))
    car_model = str(input("Wpisz model auta: "))
    car_year = int(input("Wpisz rocznik auta: "))
    czy_oryginalny = input("Wpisz czy samochód posiada conamniej 75% oryginalnych części: tak/nie): ")

    create_dictionary(car_brand, car_model, car_year, czy_oryginalny)
    check_year_and_original(car_brand, car_year, czy_oryginalny)

def create_dictionary(car_brand, car_model, car_year, czy_oryginalny):
    car_dictionary = {}
    car_dictionary["marka"] = car_brand
    car_dictionary["model"] = car_model
    car_dictionary["rocznik"] = car_year
    car_dictionary["oryginalność"] = czy_oryginalny
    print(car_dictionary)

def check_year_and_original(car_brand,car_year,czy_oryginalny):
    current_year = 2023
    if current_year - car_year >= 25 and czy_oryginalny.lower() == 'tak':
        print(f"Gratulacje twój samochód {car_brand} może zostać zarejestorwany jako zabytek.")

    elif current_year - car_year >= 25 and czy_oryginalny.lower() == 'nie':
        print(f"Twój samochód {car_brand} ma 25 lat ale nie ma oryginalnych cześci aby zostać zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {car_brand} jest zbyt młody żeby zostać zabytkiem.")
car_info()