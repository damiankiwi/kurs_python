import math

def calculate_circle_parameters(x1, y1, x2, y2, x3, y3):
    mx1 = (x1 + x2) / 2
    my1 = (y1 + y2) / 2
    mx2 = (x2 + x3) / 2
    my2 = (y2 + y3) / 2

    k1 = (y2 - y1) / (x2 - x1) if x2 != x1 else math.inf
    k2 = (y3 - y2) / (x3 - x2) if x3 != x2 else math.inf

    cx = (k1 * mx1 - k2 * mx2 + my2 - my1) / (k1 - k2)
    cy = my1 - k1 * (cx - mx1)

    radius = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)

    return radius, (cx, cy)

coordinates = input("Podaj trzy współrzędne okręgu (x1 y1 x2 y2 x3 y3, oddzielone spacją): ")
x1, y1, x2, y2, x3, y3 = map(float, coordinates.split())

radius, center_coordinates = calculate_circle_parameters(x1, y1, x2, y2, x3, y3)
print(f"Promień okręgu: {radius:.3f}")
print(f"Współrzędne centralne (x, y) okręgu: {center_coordinates[0]:.3f} {center_coordinates[1]:.3f}")