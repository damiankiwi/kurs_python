def powtorz_n_razy(tekst, n):
    if n <= 0:
        return "Podaj liczbę od 1 do 100!"
    else:
        return tekst * n

dany_napis = "Hello, World! "
liczba_powtorzen = int(input("Podaj liczbę powtórzeń: "))

wynik = powtorz_n_razy(dany_napis, liczba_powtorzen)
print(wynik)
