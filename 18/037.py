from itertools import product

def liczba_kombinacji(n):
    licznik = 0

    for kombinacja in product(range(10), repeat=4):
        if sum(kombinacja) == n:
            licznik += 1

    return licznik

n = int(input("Podaj liczbę (1 <= n <= 50): "))

liczba_kombinacji = liczba_kombinacji(n)

print(f"Liczba kombinacji: {liczba_kombinacji}")