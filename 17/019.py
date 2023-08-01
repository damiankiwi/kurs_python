def dodaj_is_na_poczatek(tekst):
    if tekst.startswith("Is"):
        return tekst
    else:
        nowy_tekst = "Is" + tekst
        return nowy_tekst

wejsciowy_tekst = input("Podaj łańcuch znaków: ")
wynik = dodaj_is_na_poczatek(wejsciowy_tekst)
print("Wynik:", wynik)