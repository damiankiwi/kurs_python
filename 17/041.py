import os

def sprawdz_czy_plik_istnieje(nazwa_pliku):
    if os.path.exists(nazwa_pliku):
        return True
    else:
        return False

nazwa_pliku = input("Podaj nazwę pliku: ")

if sprawdz_czy_plik_istnieje(nazwa_pliku):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")