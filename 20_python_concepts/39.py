import functools
import logging

def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def add(x, y):
    return x + y

@log_function
def multiply(x, y):
    return x * y

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

print(add(3, 5))
print(multiply(4, 6))