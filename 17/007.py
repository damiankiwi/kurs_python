import os

def main():
    try:
        nazwa_pliku = input("Podaj nazwę pliku: ")

        nazwa, rozszerzenie = os.path.splitext(nazwa_pliku)

        if rozszerzenie == '':
            raise ValueError("Nieprawidłowy format nazwy pliku. Proszę podać nazwę pliku wraz z rozszerzeniem.")

        print("Rozszerzenie pliku:", rozszerzenie[1:])

    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()