import os
import platform

sciezka = "/sciezka/do/pliku/nazwa_pliku.txt"

if os.path.exists(sciezka):
    rozmiar = os.path.getsize(sciezka)
    data_modyfikacji = os.path.getmtime(sciezka)
    data_modyfikacji_czytelna = str(data_modyfikacji)

    if os.path.isfile(sciezka):
        typ_pliku = "Plik"
    elif os.path.isdir(sciezka):
        typ_pliku = "Katalog"
    else:
        typ_pliku = "Inny"

    print("Ścieżka do pliku:", sciezka)
    print("Rozmiar pliku (w bajtach):", rozmiar)
    print("Data ostatniej modyfikacji:", data_modyfikacji_czytelna)
    print("Typ pliku:", typ_pliku)
else:
    print("Podana ścieżka nie istnieje.")

print("System operacyjny:", platform.system())
print("Wersja systemu operacyjnego:", platform.release())
