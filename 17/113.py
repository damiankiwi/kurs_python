wprowadzona_wartosc = input("Podaj liczbę: ")

try:
    liczba = float(wprowadzona_wartosc)
    print("Podano liczbę:", liczba)
except ValueError:
    print("Podana wartość nie jest liczbą.")

