import math

def oblicz_odleglosc(x1, y1, x2, y2):
    odleglosc = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return odleglosc

x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))

wynik = oblicz_odleglosc(x1, y1, x2, y2)
print(f"Odległość między punktami: {wynik:.2f}")