def suma_cyfr_rowna(lista):
    for liczba in lista:
        if liczba < 0:
            return False
        suma_cyfr = sum(int(cyfra) for cyfra in str(liczba))
        if suma_cyfr != sum(int(cyfra) for cyfra in str(lista[0])):
            return False
    return True

print(suma_cyfr_rowna([13, 4, 22]))
print(suma_cyfr_rowna([-13, 4, 22]))
print(suma_cyfr_rowna([45, 63, 90]))