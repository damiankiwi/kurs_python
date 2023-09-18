import os

def rozmiar_pliku(nazwa_pliku):
    try:
        rozmiar = os.path.getsize(nazwa_pliku)

        if rozmiar < 1024:
            return f"{rozmiar} bajtów"
        elif 1024 <= rozmiar < 1024**2:
            return f"{rozmiar / 1024:.2f} KB"
        elif 1024**2 <= rozmiar < 1024**3:
            return f"{rozmiar / (1024**2):.2f} MB"
        elif 1024**3 <= rozmiar < 1024**4:
            return f"{rozmiar / (1024**3):.2f} GB"
        else:
            return f"{rozmiar / (1024**4):.2f} TB"
    except FileNotFoundError:
        return "Plik nie istnieje"
    except Exception as e:
        return f"Wystąpił błąd: {str(e)}"


nazwa_pliku = os.path.basename(__file__)

rozmiar = rozmiar_pliku(nazwa_pliku)

print(f"Rozmiar pliku '{nazwa_pliku}' wynosi: {rozmiar}")
