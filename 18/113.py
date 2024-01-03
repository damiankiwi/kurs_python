def odwroc_nieparzyste_dlugosci_slow(zdanie):
    slowa = zdanie.split()
    odwrocone_zdanie = ""

    for slowo in slowa:
        if len(slowo) % 2 == 1:
            slowo = slowo[::-1]
        odwrocone_zdanie += slowo + " "

    return odwrocone_zdanie.strip()

zdanie1 = "The quick brown fox jumps over the lazy dog"
wynik1 = odwroc_nieparzyste_dlugosci_slow(zdanie1)
print(wynik1)

zdanie2 = "Python Exercises"
wynik2 = odwroc_nieparzyste_dlugosci_slow(zdanie2)
print(wynik2)