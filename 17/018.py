def calculate_sum_and_check_equal(a, b, c):
    suma = a + b + c

    if a == b == c:
        return 3 * suma
    else:
        return suma

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

suma_wynik = calculate_sum_and_check_equal(liczba1, liczba2, liczba3)

print("Suma podanych liczb to:", suma_wynik)