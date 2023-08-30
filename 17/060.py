import math

def oblicz_hipotenuse(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa

a = float(input("Podaj długość pierwszej przyprostokątnej: "))
b = float(input("Podaj długość drugiej przyprostokątnej: "))

hipotenusa = oblicz_hipotenuse(a, b)
print(f"Długość przeciwprostokątnej: {hipotenusa:.2f}")
