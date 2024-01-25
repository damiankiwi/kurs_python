def sprawdz_distinct(lista):
    for i in range(3, len(lista)):
        if lista[i] == lista[i-2] == lista[i-4] == lista[i-6] and lista[i-1] == lista[i-3] == lista[i-5] == lista[i-7]:
            return True
    return False

print(sprawdz_distinct([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
print(sprawdz_distinct([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]))
print(sprawdz_distinct([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))
