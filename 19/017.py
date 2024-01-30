def utworz_ciag_liczb(n):
    wynik = ' '.join(map(str, range(n + 1)))
    return wynik

input1 = 4
output1 = utworz_ciag_liczb(input1)
print(f"Wejście: {input1}\nWyjście: {output1}")

input2 = 15
output2 = utworz_ciag_liczb(input2)
print(f"\nWejście: {input2}\nWyjście: {output2}")