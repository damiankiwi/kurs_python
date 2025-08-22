var1 = ...

def print_arguments(*args):
    for i, arg in enumerate(args):
        print(f"Argument {i + 1}: {arg}")

    if not args:
        print(f"\nUnspecified arguments: {var1}")

print_arguments(1, 2, 3, "Python")
print_arguments(50, [1, 2, 3], "Derya Nidia", "Mitul Calixta")
print_arguments()