def czy_wszystkie_wieksze(lista, liczba):
    for element in lista:
        if element <= liczba:
            return False
    return True

lista_liczb = [10, 20, 30, 40, 50]
liczba_porownawcza = 15

wynik = czy_wszystkie_wieksze(lista_liczb, liczba_porownawcza)

if wynik:
    print("Wszystkie liczby w liście są większe od", liczba_porownawcza)
else:
    print("Nie wszystkie liczby w liście są większe od", liczba_porownawcza)
