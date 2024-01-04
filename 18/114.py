def wypisz_alfabet():
    print("Alfabet od a do z:")
    print(" ".join([chr(i) for i in range(ord('a'), ord('z') + 1)]))

    print("\nAlfabet od A do Z:")
    print(" ".join([chr(i) for i in range(ord('A'), ord('Z') + 1)]))

wypisz_alfabet()