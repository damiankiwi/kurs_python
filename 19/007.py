def sprawdz_suma_i(lista):
    suma = 0
    for i, num in enumerate(lista):
        suma += num
        if suma != i + 1:
            return False
    return True

print(sprawdz_suma_i([0, 1, 2, 3, 4, 5]))
print(sprawdz_suma_i([1, 1, 1, 1, 1, 1]))
print(sprawdz_suma_i([2, 2, 2, 2, 2]))