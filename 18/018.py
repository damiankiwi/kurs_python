def find_median(num1, num2, num3):
    if num1 >= num2:
        if num2 >= num3:
            return num2
        elif num1 <= num3:
            return num1
        else:
            return num3
    else:
        if num1 >= num3:
            return num1
        elif num2 <= num3:
            return num2
        else:
            return num3

# Przykład użycia:
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
num3 = float(input("Podaj trzecią liczbę: "))

median = find_median(num1, num2, num3)
print("Mediana spośród podanych liczb to:", median)
