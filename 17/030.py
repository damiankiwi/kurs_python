def oblicz_pole_trapezu(podstawa, wysokosc):
    pole = 0.5 * podstawa * wysokosc
    return pole


try:
    podstawa = float(input("Podaj długość podstawy trójkąta: "))
    wysokosc = float(input("Podaj wysokość trójkąta: "))

    pole_trapezu = oblicz_pole_trapezu(podstawa, wysokosc)
    print(f"Pole trójkąta wynosi: {pole_trapezu}")
except ValueError:
    print("Wprowadzono niepoprawne wartości. Podaj liczby.")
