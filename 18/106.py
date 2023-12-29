def czy_pandigital(liczba):
    liczba_str = str(liczba)
    cyfry = set(liczba_str)

    return len(cyfry) == len(liczba_str) and '0' in cyfry and len(cyfry) == 10

liczba1 = 1023456897
liczba2 = 1023456798
liczba3 = 1023457689
liczba4 = 1023456789
liczba5 = 102345679

wynik1 = czy_pandigital(liczba1)
wynik2 = czy_pandigital(liczba2)
wynik3 = czy_pandigital(liczba3)
wynik4 = czy_pandigital(liczba4)
wynik5 = czy_pandigital(liczba5)

print(f"Oryginalna liczba: {liczba1} Sprawdź, czy ta liczba jest liczbą pandigitalną czy nie? {wynik1}")
print(f"Oryginalna liczba: {liczba2} Sprawdź, czy ta liczba jest liczbą pandigitalną czy nie? {wynik2}")
print(f"Oryginalna liczba: {liczba3} Sprawdź, czy ta liczba jest liczbą pandigitalną czy nie? {wynik3}")
print(f"Oryginalna liczba: {liczba4} Sprawdź, czy ta liczba jest liczbą pandigitalną czy nie? {wynik4}")
print(f"Oryginalna liczba: {liczba5} Sprawdź, czy ta liczba jest liczbą pandigitalną czy nie? {wynik5}")