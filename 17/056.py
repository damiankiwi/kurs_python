import shutil

def rozmiary_okna_konsoli():
    szerokosc, wysokosc = shutil.get_terminal_size()
    return szerokosc, wysokosc

# Przykład użycia:
szerokosc, wysokosc = rozmiary_okna_konsoli()
print(f"Wysokość okna konsoli: {wysokosc}")
print(f"Szerokość okna konsoli: {szerokosc}")
