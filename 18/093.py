def srodkowy_znak(ciag_znakow):
    dlugosc = len(ciag_znakow)
    srodkowy_indeks = dlugosc // 2

    if dlugosc % 2 == 0:
        return ciag_znakow[srodkowy_indeks - 1:srodkowy_indeks + 1]
    else:
        return ciag_znakow[srodkowy_indeks]

input1 = "Python"
input2 = "PHP"
input3 = "Java"

output1 = srodkowy_znak(input1)
output2 = srodkowy_znak(input2)
output3 = srodkowy_znak(input3)

print(f"Original string: {input1}\nMiddle character(s) of the said string: {output1}")
print(f"Original string: {input2}\nMiddle character(s) of the said string: {output2}")
print(f"Original string: {input3}\nMiddle character(s) of the said string: {output3}")