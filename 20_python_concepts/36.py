def validate_condition(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Function arguments do not satisfy the condition")
        return wrapper
    return decorator

@validate_condition(lambda x: x > 0)
def square(x):
    return x ** 2

try:
    print(square(-3))
except ValueError as e:
    print(e)