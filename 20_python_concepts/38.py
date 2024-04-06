import time

def rate_limit(max_calls, period):
    def decorator(func):
        last_called = time.time()
        call_count = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called, call_count
            now = time.time()

            if now - last_called > period:
                call_count = 0
                last_called = now

            if call_count < max_calls:
                call_count += 1
                return func(*args, **kwargs)
            else:
                raise Exception("Rate limit exceeded. Please try again later.")
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def example_function():
    print("Example function called.")

example_function()
example_function()
example_function()
try:
    example_function()
except Exception as e:
    print(e)