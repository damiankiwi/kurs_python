#1. Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

# circle_radius = float(input("Podaj promień koła aby obliczyć pole koła: "))
# # def circle_field(r):
# #     pi = 3.14
# #     return pi * r ** 2
# #     #Wzór: pole koła  = pi razy r do potęgi drugiej
# # print("Pole koła:", circle_field(circle_radius))


def calc_area(radius):
    pi = 3.14
    return pi * radius ** 2


r = int(input("Podaj promień -> "))
print("Pole koła = ", calc_area(r))




