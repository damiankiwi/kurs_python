def generuj_decimal(start, end, step):
    wynik = []
    aktualna = start
    while aktualna <= end:
        wynik.append(round(aktualna, 1))
        aktualna += step
    return wynik

print(generuj_decimal(2, 5.5, 0.5))