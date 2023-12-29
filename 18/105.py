def sprawdz_typ_sekwencji(sekwencja):
    roznica_pierwsza = sekwencja[1] - sekwencja[0]
    roznica_druga = sekwencja[2] - sekwencja[1]
    roznica_trzecia = sekwencja[3] - sekwencja[2]

    if roznica_pierwsza == roznica_druga == roznica_trzecia:
        return "Linear Sequence"
    elif (roznica_druga - roznica_pierwsza) == (roznica_trzecia - roznica_druga):
        return "Quadratic Sequence"
    elif (roznica_trzecia - roznica_druga) == (roznica_druga - roznica_pierwsza) * 3:
        return "Cubic Sequence"
    else:
        return "Inny typ sekwencji"

sekwencja1 = [0, 2, 4, 6, 8, 10]
sekwencja2 = [1, 4, 9, 16, 25]
sekwencja3 = [0, 12, 10, 0, -12, -20]
sekwencja4 = [1, 2, 3, 4, 5]

wynik1 = sprawdz_typ_sekwencji(sekwencja1)
wynik2 = sprawdz_typ_sekwencji(sekwencja2)
wynik3 = sprawdz_typ_sekwencji(sekwencja3)
wynik4 = sprawdz_typ_sekwencji(sekwencja4)

print(f"Oryginalna sekwencja: {sekwencja1}\nSprawdź, czy ta sekwencja jest liniowa, kwadratowa czy kubiczna?\n{wynik1}\n")
print(f"Oryginalna sekwencja: {sekwencja2}\nSprawdź, czy ta sekwencja jest liniowa, kwadratowa czy kubiczna?\n{wynik2}\n")
print(f"Oryginalna sekwencja: {sekwencja3}\nSprawdź, czy ta sekwencja jest liniowa, kwadratowa czy kubiczna?\n{wynik3}\n")
print(f"Oryginalna sekwencja: {sekwencja4}\nSprawdź, czy ta sekwencja jest liniowa, kwadratowa czy kubiczna?\n{wynik4}\n")