# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd


def main():
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print("Krotka przed zmianą:", a)

    index = int(input("Podaj indeks od 0 do 9: "))
    value = int(input("Podaj wartość: "))

    try:
        if 0 <= index <= 9:
            new_list = list(a)
            new_list[index] = value
            a = tuple(new_list)
            print("Krotka po zmianie:", a)
        else:
            print("Podano nieprawidłowy indeks.")
    except IndexError:
        print("Podano nieprawidłowy indeks.")

if __name__ == "__main__":
    main()