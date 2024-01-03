def usuń_zduplikowane(lista):
    unikalne = list(set(lista))
    return unikalne

lista1 = [1, 2, 3, 2, 3, 4, 5]
print("Oryginalna lista liczb:", lista1)
print("Po usunięciu zduplikowanych liczb:")
print(usuń_zduplikowane(lista1))

lista2 = [1, 2, 3, 2, 4, 5]
print("\nOryginalna lista liczb:", lista2)
print("Po usunięciu zduplikowanych liczb:")
print(usuń_zduplikowane(lista2))

lista3 = [1, 2, 3, 4, 5]
print("\nOryginalna lista liczb:", lista3)
print("Po usunięciu zduplikowanych liczb:")
print(usuń_zduplikowane(lista3))