def czy_szczesliwa_liczba(liczba):
    def sumuj_kwadraty_cyfr(liczba):
        return sum(int(cyfra) ** 2 for cyfra in str(liczba))

    odwiedzone = set()
    while liczba != 1 and liczba not in odwiedzone:
        odwiedzone.add(liczba)
        liczba = sumuj_kwadraty_cyfr(liczba)

    return liczba == 1

input1 = (7,)
input2 = (932,)
input3 = (6,)

output1 = czy_szczesliwa_liczba(*input1)
output2 = czy_szczesliwa_liczba(*input2)
output3 = czy_szczesliwa_liczba(*input3)

print(output1)
print(output2)
print(output3)