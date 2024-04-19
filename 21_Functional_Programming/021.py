import time

def square_root(x):
    return x ** 0.5

def delayed_execution(func, args, delay):
    time.sleep(delay / 1000)
    return func(*args)

print("Square root after specific miliseconds:")
print(delayed_execution(square_root, (16,), 2000))
print(delayed_execution(square_root, (100,), 5000))
print(delayed_execution(square_root, (25000,), 200))