def czy_oddish_evenish(liczba):
    suma_cyfr = sum(int(cyfra) for cyfra in str(liczba))
    return "Oddish" if suma_cyfr % 2 != 0 else "Evenish"

liczba1 = 120
liczba2 = 321
liczba3 = 43
liczba4 = 4433
liczba5 = 373

wynik1 = czy_oddish_evenish(liczba1)
wynik2 = czy_oddish_evenish(liczba2)
wynik3 = czy_oddish_evenish(liczba3)
wynik4 = czy_oddish_evenish(liczba4)
wynik5 = czy_oddish_evenish(liczba5)

print(f"Oryginalna liczba {liczba1}")
print(f"Sprawdź, czy suma wszystkich cyfr w tej liczbie jest nieparzysta czy parzysta!")
print(wynik1)

print(f"Oryginalna liczba {liczba2}")
print(f"Sprawdź, czy suma wszystkich cyfr w tej liczbie jest nieparzysta czy parzysta!")
print(wynik2)

print(f"Oryginalna liczba {liczba3}")
print(f"Sprawdź, czy suma wszystkich cyfr w tej liczbie jest nieparzysta czy parzysta!")
print(wynik3)

print(f"Oryginalna liczba {liczba4}")
print(f"Sprawdź, czy suma wszystkich cyfr w tej liczbie jest nieparzysta czy parzysta!")
print(wynik4)

print(f"Oryginalna liczba {liczba5}")
print(f"Sprawdź, czy suma wszystkich cyfr w tej liczbie jest nieparzysta czy parzysta!")
print(wynik5)