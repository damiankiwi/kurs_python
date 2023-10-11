def dodaj_wiodace_zera(tekst, ilosc_zer):
    if ilosc_zer <= 0:
        return tekst
    else:
        wiodace_zera = "0" * ilosc_zer
        return wiodace_zera + tekst

przykladowy_tekst = "12345"
ilosc_zer = 7

wynik = dodaj_wiodace_zera(przykladowy_tekst, ilosc_zer)
print("Wynik:", wynik)
