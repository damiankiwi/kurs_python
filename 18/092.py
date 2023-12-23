def skumulowana_suma(lista):
    suma_skumulowana = 0
    skumulowana_lista = []

    for liczba in lista:
        suma_skumulowana += liczba
        skumulowana_lista.append(suma_skumulowana)

    return skumulowana_lista

input1 = [10, 20, 30, 40, 50, 60, 7]
input2 = [1, 2, 3, 4, 5]
input3 = [0, 1, 2, 3, 4, 5]

output1 = skumulowana_suma(input1)
output2 = skumulowana_suma(input2)
output3 = skumulowana_suma(input3)

print(output1)
print(output2)
print(output3)