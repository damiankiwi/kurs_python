def suma_bez_duplikatow(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


try:
    liczba_a = int(input("Podaj pierwszą liczbę całkowitą: "))
    liczba_b = int(input("Podaj drugą liczbę całkowitą: "))
    liczba_c = int(input("Podaj trzecią liczbę całkowitą: "))

    wynik_sumy = suma_bez_duplikatow(liczba_a, liczba_b, liczba_c)
    print(f"Suma trzech liczb wynosi: {wynik_sumy}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj trzy liczby całkowite.")
