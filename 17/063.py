import os

def bezwzgledna_sciezka_pliku(nazwa_pliku):
    sciezka_bezwzgledna = os.path.abspath(nazwa_pliku)
    return sciezka_bezwzgledna

nazwa_pliku = input("Podaj nazwę pliku (lub ścieżkę do pliku): ")

sciezka = bezwzgledna_sciezka_pliku(nazwa_pliku)
print(f"Bezwzględna ścieżka do pliku: {sciezka}")