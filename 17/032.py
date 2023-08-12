def oblicz_nww(a, b):
    nww = (a * b) // oblicz_nwd(a, b)
    return nww


def oblicz_nwd(a, b):
    while b:
        a, b = b, a % b
    return a


try:
    liczba_a = int(input("Podaj pierwszą liczbę całkowitą dodatnią: "))
    liczba_b = int(input("Podaj drugą liczbę całkowitą dodatnią: "))

    if liczba_a <= 0 or liczba_b <= 0:
        print("Podaj poprawne wartości, obie liczby muszą być dodatnie.")
    else:
        nww = oblicz_nww(liczba_a, liczba_b)
        print(f"Najmniejsza wspólna wielokrotność liczb {liczba_a} i {liczba_b} to: {nww}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj dwie liczby całkowite dodatnie.")
