def oblicz_przyszla_wartosc(kwota_poczatkowa, stopa_procentowa, lata):
    przyszla_wartosc = kwota_poczatkowa * (1 + (stopa_procentowa / 100)) ** lata
    return przyszla_wartosc

kwota = 10000
stopa_procentowa = 3.5
lata = 7

wynik = oblicz_przyszla_wartosc(kwota, stopa_procentowa, lata)
print(f"Przyszła wartość po {lata} latach: {wynik:.2f}")
