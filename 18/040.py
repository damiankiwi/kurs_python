def is_point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
    area_triangle = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    area_sub_triangle1 = abs((x1*(y2-yp) + x2*(yp-y1) + xp*(y1-y2)) / 2)
    area_sub_triangle2 = abs((xp*(y2-y3) + x2*(y3-yp) + x3*(yp-y2)) / 2)
    area_sub_triangle3 = abs((x1*(yp-y3) + xp*(y3-y1) + x3*(y1-yp)) / 2)

    sum_areas = area_sub_triangle1 + area_sub_triangle2 + area_sub_triangle3

    return abs(sum_areas - area_triangle) < 1e-6

triangle_coordinates = input("Podaj współrzędne trójkąta i punktu (x1 y1 x2 y2 x3 y3 xp yp, oddzielone spacją): ")
x1, y1, x2, y2, x3, y3, xp, yp = map(float, triangle_coordinates.split())

if is_point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp):
    print("Punkt znajduje się w trójkącie.")
else:
    print("Punkt nie znajduje się w trójkącie.")