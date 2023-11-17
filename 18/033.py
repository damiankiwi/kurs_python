def liczba_cyfr_sumy(a, b):
    suma = a + b
    liczba_cyfr = len(str(suma))
    return liczba_cyfr

wejscie = input("Podaj dwie liczby całkowite oddzielone spacją (a b): ")
a, b = map(int, wejscie.split())

wynik = liczba_cyfr_sumy(a, b)
print(f"Suma dwóch liczb {a} i {b} ma {wynik} cyfr(y).")