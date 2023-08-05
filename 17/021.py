def sprawdz_czy_parzysta(liczba):
    if liczba % 2 == 0:
        return "Liczba jest parzysta."
    else:
        return "Liczba jest nieparzysta."

try:
    podana_liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = sprawdz_czy_parzysta(podana_liczba)
    print(wynik)
except ValueError:
    print("Wprowadzono niepoprawną liczbę. Spróbuj ponownie i podaj liczbę całkowitą.")
