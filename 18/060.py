def wytnij_slowa(zdanie):
    slowa = zdanie.split()
    wynik = [slowo for slowo in slowa if 3 <= len(slowo) <= 6]
    return wynik

zdanie = input("Podaj zdanie (maksymalnie 1024 znaki): ")

wynik = wytnij_slowa(zdanie)
print("Słowa o długości od 3 do 6 znaków:")
print(" ".join(wynik))