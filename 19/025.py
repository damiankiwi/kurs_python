def xor_binarnych_napisow(napis1, napis2):
    liczba1 = int(napis1, 2)
    liczba2 = int(napis2, 2)
    wynik = liczba1 ^ liczba2
    return bin(wynik)

input1 = ['0001', '1011']
output1 = xor_binarnych_napisow(*input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = ['100011101100001', '100101100101110']
output2 = xor_binarnych_napisow(*input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")