from functools import reduce

lista_liczb = [2, 3, 4, 5]

iloczyn = reduce(lambda x, y: x * y, lista_liczb)

print("Iloczyn wszystkich liczb w liście:", iloczyn)
