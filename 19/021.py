def sprawdz_izolowana_litere(napisy):
    wyniki = [napis[-1].isalpha() and (napis[-2] == ' ' or napis[-2].isdigit() or napis[-2] in ['!', '?', ',', '.']) for napis in napisy]
    return wyniki

input1 = ['cat', 'car', 'fear', 'center']
output1 = sprawdz_izolowana_litere(input1)
print(f"Wejście:\n{input1}\nWyjście:\n{output1}")

input2 = ['ca t', 'car', 'fea r', 'cente r']
output2 = sprawdz_izolowana_litere(input2)
print(f"\nWejście:\n{input2}\nWyjście:\n{output2}")