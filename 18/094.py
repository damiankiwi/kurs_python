def najwiekszy_iloczyn_sasiadow(lista):
    if len(lista) < 2:
        return "Lista jest zbyt krótka"

    najwiekszy_iloczyn = lista[0] * lista[1]

    for i in range(1, len(lista) - 1):
        iloczyn_sasiadow = lista[i] * lista[i + 1]
        najwiekszy_iloczyn = max(najwiekszy_iloczyn, iloczyn_sasiadow)

    return najwiekszy_iloczyn

input1 = [1, 2, 3, 4, 5, 6]
input2 = [1, 2, 3, 4, 5]
input3 = [2, 3]

output1 = najwiekszy_iloczyn_sasiadow(input1)
output2 = najwiekszy_iloczyn_sasiadow(input2)
output3 = najwiekszy_iloczyn_sasiadow(input3)

print(f"Original list: {input1}\nLargest product of the pair of adjacent elements of the said list: {output1}")
print(f"Original list: {input2}\nLargest product of the pair of adjacent elements of the said list: {output2}")
print(f"Original list: {input3}\nLargest product of the pair of adjacent elements of the said list: {output3}")