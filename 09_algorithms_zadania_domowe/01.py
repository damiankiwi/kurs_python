def euclidean_algorithm(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

number1 = 282
number2 = 78
NWD = euclidean_algorithm(number1, number2)
print("Największy wspólny dzielnik liczby", number1, "i", number2, "to:", NWD)