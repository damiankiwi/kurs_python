def calculate_polygon_area(n, vertices):
    area = 0.0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    area = abs(area) / 2.0
    return area

n = int(input("Podaj liczbę boków: "))
vertices = []

for i in range(n):
    print(f"Bok: {i+1}")
    x = float(input("Podaj współrzędną x: "))
    y = float(input("Podaj współrzędną y: "))
    vertices.append((x, y))

result = calculate_polygon_area(n, vertices)
print(f"Pole wielokąta: {result}")