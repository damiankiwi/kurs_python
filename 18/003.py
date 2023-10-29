def usun_co_trzecia(lista):
    licznik = 1
    while len(lista) > 0:
        if len(lista) < 3:
            print("Nie można usunąć co trzeciego elementu, ponieważ lista jest za krótka.")
            break
        element = lista.pop(2)
        print(f"Usunięto {element}")
        licznik += 1

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

usun_co_trzecia(lista_liczb)
