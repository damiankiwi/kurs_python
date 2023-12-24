def sprawdz_parzystosc_indeksow(lista):
    for i in range(len(lista)):
        if i % 2 == 0 and lista[i] % 2 != 0:
            return False
        elif i % 2 != 0 and lista[i] % 2 == 0:
            return False
    return True

input1 = [2, 1, 4, 3, 6, 7, 6, 3]
input2 = [2, 1, 4, 3, 6, 7, 6, 4]
input3 = [2, 1, 4, 3, 6, 7, 6, 4]

output1 = sprawdz_parzystosc_indeksow(input1)
output2 = sprawdz_parzystosc_indeksow(input2)
output3 = sprawdz_parzystosc_indeksow(input3)

print(f"Original list of numbers: {input1}\nCheck whether every even index contains an even number and every odd index contains odd number of a given list:\n{output1}")
print(f"Original list of numbers: {input2}\nCheck whether every even index contains an even number and every odd index contains odd number of a given list:\n{output2}")
print(f"Original list of numbers: {input3}\nCheck whether every even index contains an even number and every odd index contains odd number of a given list:\n{output3}")