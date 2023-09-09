def oblicz_punkt_srodkowy(x1, y1, x2, y2):
    x_srodek = (x1 + x2) / 2
    y_srodek = (y1 + y2) / 2
    return x_srodek, y_srodek

x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))

srodek_x, srodek_y = oblicz_punkt_srodkowy(x1, y1, x2, y2)

print(f"Środek odcinka znajduje się w punkcie ({srodek_x}, {srodek_y})")
