def sprawdz_kod_pracownika(kod):
    if len(kod) == 8 or len(kod) == 12:
        return True
    else:
        return False

input1 = '12345678'
output1 = sprawdz_kod_pracownika(input1)
print(f"Kod pracownika: {input1}\nCzy to jest poprawny kod: {output1}")

input2 = '1234567j'
output2 = sprawdz_kod_pracownika(input2)
print(f"Kod pracownika: {input2}\nCzy to jest poprawny kod: {output2}")

input3 = '12345678j'
output3 = sprawdz_kod_pracownika(input3)
print(f"Kod pracownika: {input3}\nCzy to jest poprawny kod: {output3}")

input4 = '123456789123'
output4 = sprawdz_kod_pracownika(input4)
print(f"Kod pracownika: {input4}\nCzy to jest poprawny kod: {output4}")

input5 = '123456abcdef'
output5 = sprawdz_kod_pracownika(input5)
print(f"Kod pracownika: {input5}\nCzy to jest poprawny kod: {output5}")