import os

#Pobiera aktualny katalog, w którym znajduje się plik
katalog = os.path.dirname(os.path.abspath(__file__))

if os.path.isdir(katalog):
    for plik in os.listdir(katalog):
        pelna_sciezka = os.path.join(katalog, plik)
        if os.path.isfile(pelna_sciezka):
            print(f'Znaleziono plik: {plik}')
else:
    print(f'Bieżący katalog "{katalog}" nie jest prawidłowym katalogiem.')

