import math

def find_third_side(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

side1 = float(input("Podaj długość pierwszego boku: "))
side2 = float(input("Podaj długość drugiego boku: "))

third_side = find_third_side(side1, side2)
print("Długość trzeciego boku (przeciwnego do kąta prostego) wynosi:", third_side)
