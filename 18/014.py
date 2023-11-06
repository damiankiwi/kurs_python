def add_without_plus_operator(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a

num1 = int(input("Podaj pierwszą liczbę całkowitą: "))
num2 = int(input("Podaj drugą liczbę całkowitą: "))
result = add_without_plus_operator(num1, num2)
print("Wynik dodawania:", result)
