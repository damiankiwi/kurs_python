def czy_podzielna(liczba, dzielnik):
    if liczba % dzielnik == 0:
        return f"{liczba} jest podzielna przez {dzielnik}."
    else:
        return f"{liczba} nie jest podzielna przez {dzielnik}."

liczba = int(input("Wprowadź pierwszą liczbę: "))
dzielnik = int(input("Wprowadź drugą liczbę (dzielnik): "))

wynik = czy_podzielna(liczba, dzielnik)

print(wynik)