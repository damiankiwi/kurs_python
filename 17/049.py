import os

def wypisz_pliki_w_katalogu(sciezka):
    if os.path.exists(sciezka) and os.path.isdir(sciezka):
        pliki = os.listdir(sciezka)
        print("Lista plików w katalogu:")
        for plik in pliki:
            if os.path.isfile(os.path.join(sciezka, plik)):
                print(plik)
    else:
        print("Podana ścieżka nie istnieje lub nie jest katalogiem.")

katalog = os.path.dirname(os.path.abspath(__file__))
wypisz_pliki_w_katalogu(katalog)
