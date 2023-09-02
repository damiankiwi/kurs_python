import os
import datetime

def data_i_czas_pliku(nazwa_pliku):
    if os.path.exists(nazwa_pliku):
        czas_utworzenia = datetime.datetime.fromtimestamp(os.path.getctime(nazwa_pliku))
        czas_modyfikacji = datetime.datetime.fromtimestamp(os.path.getmtime(nazwa_pliku))
        return czas_utworzenia, czas_modyfikacji
    else:
        return None

nazwa_pliku = input("Podaj nazwę pliku (lub ścieżkę do pliku): ")

czasy = data_i_czas_pliku(nazwa_pliku)
if czasy:
    czas_utworzenia, czas_modyfikacji = czasy
    print(f"Data utworzenia pliku: {czas_utworzenia}")
    print(f"Data ostatniej modyfikacji pliku: {czas_modyfikacji}")
else:
    print("Plik nie istnieje.")
