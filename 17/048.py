def parsuj_na_liczbe(tekst):
    try:
        liczba = float(tekst)
        if liczba.is_integer():
            return int(liczba)
        else:
            return liczba
    except ValueError:
        return None

tekst = input("Podaj ciąg znaków do sparsowania: ")
wynik = parsuj_na_liczbe(tekst)

if wynik is None:
    print("Nie można sparsować na liczbę.")
else:
    if isinstance(wynik, int):
        print(f"Sparsowana liczba całkowita: {wynik}")
    else:
        print(f"Sparsowana liczba zmiennoprzecinkowa: {wynik}")
