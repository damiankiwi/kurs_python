def find_max(a, b, c):
    """
    Find the maximum of three numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The maximum of the three numbers.
    """
    return max(a, b, c)

num1 = 10
num2 = 20
num3 = 15
print("Maximum number:", find_max(num1, num2, num3))