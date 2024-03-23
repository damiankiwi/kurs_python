try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    num1 = float(num1)
    num2 = float(num2)

    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)

except ValueError:
    print("Error: Inputs must be numerical.")