def suma_elementow_kontenera(kontener):
    suma = 0

    if isinstance(kontener, (tuple, list, set)):
        for element in kontener:
            suma += element
    elif isinstance(kontener, dict):
        for key, value in kontener.items():
            suma += value

    return suma


tuple_przyklad = (1, 2, 3, 4, 5)
list_przyklad = [6, 7, 8, 9, 10]
set_przyklad = {11, 12, 13, 14, 15}
dict_przyklad = {"a": 16, "b": 17, "c": 18, "d": 19, "e": 20}

suma_tuple = suma_elementow_kontenera(tuple_przyklad)
suma_list = suma_elementow_kontenera(list_przyklad)
suma_set = suma_elementow_kontenera(set_przyklad)
suma_dict = suma_elementow_kontenera(dict_przyklad)

print("Suma elementów tuple: ", suma_tuple)
print("Suma elementów list: ", suma_list)
print("Suma elementów set: ", suma_set)
print("Suma elementów dict: ", suma_dict)
