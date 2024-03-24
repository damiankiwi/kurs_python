try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    result = dividend / divisor
    print("Result of division:", result)

except ArithmeticError:
    print("Error: Arithmetic operation failed.")
except ValueError:
    print("Error: Please enter valid integer values for dividend and divisor.")