def sprawdz_ciągi(tekst):
    zeros = 0
    ones = 0

    for znak in tekst:
        if znak == '0':
            zeros += 1
        elif znak == '1':
            ones += 1

    return zeros == ones

ciąg1 = "01010101"
ciąg2 = "00"
ciąg3 = "000111000111"
ciąg4 = "00011100011"

wynik1 = sprawdz_ciągi(ciąg1)
wynik2 = sprawdz_ciągi(ciąg2)
wynik3 = sprawdz_ciągi(ciąg3)
wynik4 = sprawdz_ciągi(ciąg4)

print("Wynik 1:", wynik1)
print("Wynik 2:", wynik2)
print("Wynik 3:", wynik3)
print("Wynik 4:", wynik4)
