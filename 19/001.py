def sprawdz_warunki(lista):
    return lista.count(19) == 2 and lista.count(5) >= 3

print(sprawdz_warunki([19, 19, 15, 5, 3, 5, 5, 2]))
print(sprawdz_warunki([19, 15, 15, 5, 3, 3, 5, 2]))
print(sprawdz_warunki([19, 19, 5, 5, 5, 5, 5]))