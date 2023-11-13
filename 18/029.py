def znajdz_wspolne_dzielniki(liczba1, liczba2):
    wspolne_dzielniki = []

    for i in range(1, min(liczba1, liczba2) + 1):
        if liczba1 % i == 0 and liczba2 % i == 0:
            wspolne_dzielniki.append(i)

    return wspolne_dzielniki

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

wynik_wspolnych_dzielnikow = znajdz_wspolne_dzielniki(liczba1, liczba2)

if wynik_wspolnych_dzielnikow:
    print(f"Wspólne dzielniki między {liczba1} a {liczba2}: {wynik_wspolnych_dzielnikow}")
else:
    print("Brak wspólnych dzielników między podanymi liczbami.")
