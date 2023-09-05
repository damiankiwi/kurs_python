def posortuj_trzy_liczby(a, b, c):
    liczby = [a, b, c]
    liczby.sort()
    return liczby

liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
liczba3 = int(input("Podaj trzecią liczbę całkowitą: "))

posortowane_liczby = posortuj_trzy_liczby(liczba1, liczba2, liczba3)

print("Posortowane liczby:", posortowane_liczby)
