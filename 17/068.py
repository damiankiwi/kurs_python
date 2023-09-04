def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra
        liczba //= 10
    return suma

liczba = int(input("Podaj liczbę całkowitą: "))

wynik = suma_cyfr(liczba)
print(f"Suma cyfr liczby {liczba} wynosi: {wynik}")