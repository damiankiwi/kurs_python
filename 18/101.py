def najstarszy_student(studenci):
    najstarszy_imie = None
    najstarszy_wiek = float('-inf')

    for imie, wiek in studenci.items():
        if wiek > najstarszy_wiek:
            najstarszy_wiek = wiek
            najstarszy_imie = imie

    return najstarszy_imie

input1 = {"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
input2 = {"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}

output1 = najstarszy_student(input1)
output2 = najstarszy_student(input2)

print(f"Wejściowe dane: {input1}\nNajstarszy student: {output1}")
print(f"Wejściowe dane: {input2}\nNajstarszy student: {output2}")