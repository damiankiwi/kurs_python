liczba_pietr = int(input("Podaj liczbę pięter (od 4 do 10): "))

if liczba_pietr < 4 or liczba_pietr > 10:
    print("Nieprawidłowa liczba pięter.")
else:
    for i in range(1, liczba_pietr + 1):
        for j in range(i):
            print("*", end="")
        print()