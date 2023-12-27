def suma_przemnozona_przez_indeks(tablica):
    suma = 0
    for indeks, liczba in enumerate(tablica):
        suma += indeks * liczba
    return suma

input1 = [1, 2, 3, 4]
input2 = [-1, -2, -3, -4]
input3 = []

output1 = suma_przemnozona_przez_indeks(input1)
output2 = suma_przemnozona_przez_indeks(input2)
output3 = suma_przemnozona_przez_indeks(input3)

print(f"Wejściowe dane: {input1}\nSuma przemnożona przez indeks: {output1}")
print(f"Wejściowe dane: {input2}\nSuma przemnożona przez indeks: {output2}")
print(f"Wejściowe dane: {input3}\nSuma przemnożona przez indeks: {output3}")