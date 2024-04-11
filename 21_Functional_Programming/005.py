def factorial(n):

    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 5
factorial_of_number = factorial(number)
print("Factorial of", number, ":", factorial_of_number)