import datetime

def czy_piatek_13(miesiac, rok):
    pierwszy_dzien_miesiaca = datetime.date(rok, miesiac, 1)
    trzynasty_dzien_miesiaca = datetime.date(rok, miesiac, 13)

    return pierwszy_dzien_miesiaca.weekday() == 4 and trzynasty_dzien_miesiaca.weekday() == 0

print("Numer miesiąca: 11 Rok: 2022")
print("Czy podany miesiąc i rok zawierają piątek trzynastego?:", czy_piatek_13(11, 2022))

print("Numer miesiąca: 6 Rok: 2022")
print("Czy podany miesiąc i rok zawierają piątek trzynastego?:", czy_piatek_13(6, 2022))