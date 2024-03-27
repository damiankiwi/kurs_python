class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return x / y

calculator = Calculator()
print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(10, 4))
print("Multiplication:", calculator.multiply(7, 2))
print("Division:", calculator.divide(20, 5))