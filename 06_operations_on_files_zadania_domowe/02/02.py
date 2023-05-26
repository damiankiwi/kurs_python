import os
import time

quotes_file = "quotes.txt"

# rozmiaru pliku w bajtach:
print(f'Rozmiar pliku {quotes_file} wynosi {os.path.getsize("quotes.txt")} bajtów')

#Dodatowe:

# ścieżka dostępu:
print(os.getcwd())

# lista plików i folderów zawartych w danej lokalizacji:
l = list(os.listdir())
print(l)

# data utworzenia pliku:
print(time.ctime(os.path.getctime(quotes_file)))