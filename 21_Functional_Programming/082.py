def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

square = lambda x: x * x

N = 10

fibonacci_numbers = generate_fibonacci(N)

squared_fibonacci_numbers = list(map(square, fibonacci_numbers))

print("First", N, "Fibonacci numbers:")
print(fibonacci_numbers)
print("Squares of the first", N, "Fibonacci numbers:")
print(squared_fibonacci_numbers)