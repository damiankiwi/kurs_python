def sprawdz_warunki(lista):
    return len(lista) == 8 and lista.count(lista[4]) == 3

print(sprawdz_warunki([19, 19, 15, 5, 5, 5, 1, 2]))
print(sprawdz_warunki([19, 15, 5, 7, 5, 5, 2]))
print(sprawdz_warunki([11, 12, 14, 13, 14, 13, 15, 14]))
print(sprawdz_warunki([19, 15, 11, 7, 5, 6, 2]))