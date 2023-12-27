def bez_powtarzajacych_sie(tekst):
    nowy_tekst = tekst[0]

    for i in range(1, len(tekst)):
        if tekst[i] != tekst[i - 1]:
            nowy_tekst += tekst[i]

    return nowy_tekst

input1 = "PPYYYTTHON"
input2 = "PPyyythonnn"
input3 = "Java"
input4 = "PPPHHHPPP"

output1 = bez_powtarzajacych_sie(input1)
output2 = bez_powtarzajacych_sie(input2)
output3 = bez_powtarzajacych_sie(input3)
output4 = bez_powtarzajacych_sie(input4)

print(f"Wejściowy tekst: {input1}\nTekst bez powtórzeń: {output1}")
print(f"Wejściowy tekst: {input2}\nTekst bez powtórzeń: {output2}")
print(f"Wejściowy tekst: {input3}\nTekst bez powtórzeń: {output3}")
print(f"Wejściowy tekst: {input4}\nTekst bez powtórzeń: {output4}")