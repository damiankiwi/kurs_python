def generuj_i_wypisz_liste():
    zakres = range(1, 10)
    lista_liczb = list(zakres)

    print(lista_liczb)

    lista_liczb_jako_str = [str(liczba) for liczba in lista_liczb]
    print(lista_liczb_jako_str)

generuj_i_wypisz_liste()