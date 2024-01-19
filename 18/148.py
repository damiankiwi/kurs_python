def policz_wieksze_od_poprzedniego(lista):
    licznik = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            licznik += 1
    return licznik

print(policz_wieksze_od_poprzedniego([1, 4, 7, 9, 11, 5]))
print(policz_wieksze_od_poprzedniego([1, 3, 3, 2, 2]))
print(policz_wieksze_od_poprzedniego([4, 3, 2, 1]))