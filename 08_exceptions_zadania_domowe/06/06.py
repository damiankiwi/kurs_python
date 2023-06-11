def main():
    try:
        with open("nofile.txt", "r", encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Plik nie istnieje.")

    try:
        with open("file.txt", "w", encoding='utf-8') as file:
            file.write("Przykładowa zawartość pliku.")

        with open("file.txt", "r", encoding='utf-8') as file:
            contents = file.read()
            print(contents)

    except IOError:
        print("Wystąpił błąd odczytu/zapisu pliku.")

    try:
        with open("file.txt", "x", encoding='utf-8') as file:
            file.write("Nowa zawartość pliku.")
    except FileExistsError:
        print("Plik już istnieje.")


if __name__ == "__main__":
    main()