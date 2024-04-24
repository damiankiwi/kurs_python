fibonacci = lambda n: [] if n == 0 else [0] if n == 1 else [0, 1] if n == 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]

test_cases = [2, 5, 6, 9]

for n in test_cases:
    print(f"Fibonacci series upto {n}:")
    print(fibonacci(n))