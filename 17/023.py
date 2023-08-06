def kopie_pierwszych_dwoch_znakow(napis, n):
    pierwsze_dwa_znaki = napis[:2]
    if len(napis) < 2:
        wynik = napis * n
    else:
        wynik = pierwsze_dwa_znaki * n
    return wynik

dany_napis = input("Podaj napis: ")
liczba_kopii = int(input("Podaj liczbę kopii: "))

wynik = kopie_pierwszych_dwoch_znakow(dany_napis, liczba_kopii)
print(wynik)
