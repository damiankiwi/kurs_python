def laczenie_elementow_w_napis(lista):
    napis = ''.join(map(str, lista))
    return napis

dana_lista = ['Hello', ' ', 'world', '!']

wynik = laczenie_elementow_w_napis(dana_lista)
print(wynik)