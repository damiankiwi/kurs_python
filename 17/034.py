def suma_z_ograniczeniem(a, b):
    suma = a + b
    if 15 <= suma <= 20:
        return 20
    else:
        return suma


try:
    liczba_a = int(input("Podaj pierwszą liczbę całkowitą: "))
    liczba_b = int(input("Podaj drugą liczbę całkowitą: "))

    wynik_sumy = suma_z_ograniczeniem(liczba_a, liczba_b)
    print(f"Wynik sumy wynosi: {wynik_sumy}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj dwie liczby całkowite.")
