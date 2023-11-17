def czy_trojkat_prostokatny(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Yes"
    else:
        return "No"

wejscie = input("Podaj trzy liczby całkowite oddzielone spacjami (a b c): ")
a, b, c = map(int, wejscie.split())

wynik = czy_trojkat_prostokatny(a, b, c)
print(wynik)