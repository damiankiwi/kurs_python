def suma_ascii_wielkich_liter(napis):
    return sum(ord(znak) for znak in napis if znak.isupper())

input1 = "PytHon ExerciSEs"
output1 = suma_ascii_wielkich_liter(input1)
print(f"Wejście: {input1}\nWyjście: {output1}")

input2 = "JavaScript"
output2 = suma_ascii_wielkich_liter(input2)
print(f"\nWejście: {input2}\nWyjście: {output2}")