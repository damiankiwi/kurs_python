import os

nazwa_sciezki = "nazwa_pliku.txt"

for root, dirs, files in os.walk("/"):
    if nazwa_sciezki in files or nazwa_sciezki in dirs:
        pelna_sciezka = os.path.join(root, nazwa_sciezki)
        print("Znaleziona ścieżka:", pelna_sciezka)
        break
else:
    print("Nie znaleziono ścieżki o nazwie:", nazwa_sciezki)
