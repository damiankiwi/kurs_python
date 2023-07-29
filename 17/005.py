def main():
    imie = input("Podaj swoje imię: ")
    nazwisko = input("Podaj swoje nazwisko: ")

    imie_i_nazwisko_w_odwrotnej_kolejnosci = nazwisko + " " + imie
    print("Twoje imię i nazwisko w odwrotnej kolejności: " + imie_i_nazwisko_w_odwrotnej_kolejnosci)

if __name__ == "__main__":
    main()