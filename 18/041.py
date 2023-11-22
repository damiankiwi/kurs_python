first_integer = int(input("Podaj pierwszą liczbę całkowitą: "))

second_integer = int(input("Podaj drugą liczbę całkowitą: "))

sum_result = first_integer + second_integer

if len(str(sum_result)) > 80:
    print("overflow")
else:
    print(f"Suma dwóch liczb: {sum_result}")