import os

def sprawdz_rodzaj_sciezki(sciezka):
    if os.path.isfile(sciezka):
        return "To jest ścieżka do pliku."
    elif os.path.isdir(sciezka):
        return "To jest ścieżka do katalogu."
    else:
        return "Ścieżka nie istnieje."

#podaj ścieżkę
sciezka = "ścieżka/do/twojego/pliku/lub/katalogu"

wynik = sprawdz_rodzaj_sciezki(sciezka)

print(wynik)
