def zastap_gwiazdkami(oryginalny_ciag):
    if len(oryginalny_ciag) <= 5:
        return oryginalny_ciag
    else:
        gwiazdki = '*' * (len(oryginalny_ciag) - 5)
        nowy_ciag = gwiazdki + oryginalny_ciag[-5:]
        return nowy_ciag

input1 = "kdi39323swe"
output1 = zastap_gwiazdkami(input1)
print(f"Oryginalny ciąg: {input1}\nNowy ciąg: {output1}")

input2 = "12345abcdef"
output2 = zastap_gwiazdkami(input2)
print(f"Oryginalny ciąg: {input2}\nNowy ciąg: {output2}")

input3 = "12345"
output3 = zastap_gwiazdkami(input3)
print(f"Oryginalny ciąg: {input3}\nNowy ciąg: {output3}")