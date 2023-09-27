import os

sciezka = "/sciezka/do/pliku/nazwa_pliku.txt"

nazwa_pliku, rozszerzenie = os.path.splitext(sciezka)

print("Nazwa pliku:", nazwa_pliku)
print("Rozszerzenie:", rozszerzenie)