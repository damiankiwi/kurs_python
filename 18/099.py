def pozycja_drugiego_wystapienia(ciag, szukany):
    pierwsze_wystapienie = ciag.find(szukany)
    if pierwsze_wystapienie == -1:
        return -1

    drugie_wystapienie = ciag.find(szukany, pierwsze_wystapienie + 1)
    return drugie_wystapienie

input1 = ("The quick brown fox jumps over the lazy dog", "the")
input2 = ("the quick brown fox jumps over the lazy dog", "the")

output1 = pozycja_drugiego_wystapienia(*input1)
output2 = pozycja_drugiego_wystapienia(*input2)

print(f"Wejściowe dane: {input1}\nPozycja drugiego wystąpienia: {output1}")
print(f"Wejściowe dane: {input2}\nPozycja drugiego wystąpienia: {output2}")