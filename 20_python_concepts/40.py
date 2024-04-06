import functools

def handle_exceptions(default_response):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"An error occurred: {e}")
                return default_response
        return wrapper
    return decorator

@handle_exceptions(default_response="Error occurred, please try again later.")
def divide(x, y):
    return x / y

print(divide(10, 0))