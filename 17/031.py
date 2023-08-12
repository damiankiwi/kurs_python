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
        nwd = oblicz_nwd(liczba_a, liczba_b)
        print(f"Największy wspólny dzielnik liczb {liczba_a} i {liczba_b} to: {nwd}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj dwie liczby całkowite dodatnie.")
