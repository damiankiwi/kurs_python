def is_within_100(number):
    return abs(1000 - number) <= 100 or abs(2000 - number) <= 100

liczba = int(input("Podaj liczbę: "))

if is_within_100(liczba):
    print("Liczba jest w odległości 100 od 1000 lub 2000.")
else:
    print("Liczba nie jest w odległości 100 od 1000 lub 2000.")