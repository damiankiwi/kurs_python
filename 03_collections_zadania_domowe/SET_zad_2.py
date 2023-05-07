# 2. Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
#
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]  # LIST
T_test = (1, 2, 3, 4)  # TUPLE
S_test = {1, 2, 3, 4}  # SET

# L_test.append(4)
# print(L_test)
# L_test.insert(2,4)
# print(L_test)
# print(L_test.pop(1))
# print(L_test)
# L_test.pop(2)
# print(L_test)
# L_test.sort()
# print(L_test)
# L_test.reverse()
# print(L_test)
# print(L_test.count(4))
# print(L_test.index(4))
# L_test.remove(4)
# print(L_test)
# del L_test[0]
# print(L_test)

L_test.append(4)
print(L_test)
print(L_test.pop(1))
print(L_test)

print('W Tuple oraz SET nie zadzaiła metoda APPEND ani POP')