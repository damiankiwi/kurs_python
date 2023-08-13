def sprawdz_warunki(a, b):
    if a == b or abs(a - b) == 5 or a + b == 5:
        return True
    else:
        return False


try:
    liczba_a = int(input("Podaj pierwszą liczbę całkowitą: "))
    liczba_b = int(input("Podaj drugą liczbę całkowitą: "))

    wynik = sprawdz_warunki(liczba_a, liczba_b)
    print(f"Sprawdzam czy liczby są takie same4: {wynik}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj dwie liczby całkowite.")
