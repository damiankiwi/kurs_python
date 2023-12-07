def czy_suma_rowna_k(lista, k):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == k:
                return True
    return False

input1 = ([12, 5, 0, 5], 10)
input2 = ([20, 20, 4, 5], 40)
input3 = ([1, -1], 0)
input4 = ([1, 1, 0], 0)

output1 = czy_suma_rowna_k(*input1)
output2 = czy_suma_rowna_k(*input2)
output3 = czy_suma_rowna_k(*input3)
output4 = czy_suma_rowna_k(*input4)

print(output1)
print(output2)
print(output3)
print(output4)