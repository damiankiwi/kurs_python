import os

nazwa_uzytkownika = os.environ.get("USERNAME")
sciezka_home = os.environ.get("HOME")

print(f"Nazwa użytkownika: {nazwa_uzytkownika}")
print(f"Ścieżka katalogu domowego: {sciezka_home}")
