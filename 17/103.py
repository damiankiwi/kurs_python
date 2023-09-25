import os

sciezka = "/sciezka/do/pliku/nazwa_pliku.txt"

nazwa_pliku = os.path.basename(sciezka)

print("Nazwa pliku:", nazwa_pliku)
