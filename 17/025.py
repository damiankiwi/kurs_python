def sprawdz_czy_wartosc_wystepuje(wartosc, grupa_wartosci):
    if wartosc in grupa_wartosci:
        return True
    else:
        return False

grupa_wartosci = [1, 5, 8, 3]

wartosc_1 = 3
wynik_1 = sprawdz_czy_wartosc_wystepuje(wartosc_1, grupa_wartosci)
print(f"Czy wartość: {wartosc_1} występuje w -> {grupa_wartosci} : {wynik_1}")

wartosc_2 = -1
wynik_2 = sprawdz_czy_wartosc_wystepuje(wartosc_2, grupa_wartosci)
print(f"Czy wartość: {wartosc_2} występuje w -> {grupa_wartosci} : {wynik_2}")
