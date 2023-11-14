def count_carry_operations(num1, num2):
    num1_digits = [int(digit) for digit in str(num1)][::-1]
    num2_digits = [int(digit) for digit in str(num2)][::-1]

    max_length = max(len(num1_digits), len(num2_digits))
    num1_digits += [0] * (max_length - len(num1_digits))
    num2_digits += [0] * (max_length - len(num2_digits))

    carry = 0
    carry_count = 0

    for digit1, digit2 in zip(num1_digits, num2_digits):
        current_sum = digit1 + digit2 + carry

        if current_sum >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

    return carry_count

number1 = int(input("Podaj pierwszą liczbę: "))
number2 = int(input("Podaj drugą liczbę: "))

result = count_carry_operations(number1, number2)
print(f"Liczba operacji przenoszenia: {result}")