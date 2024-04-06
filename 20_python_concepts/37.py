import time

def retry(times, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Failed to execute {func.__name__}. Retrying...")
                    time.sleep(delay)
            raise e
        return wrapper
    return decorator

@retry(times=3, delay=1)
def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except Exception as e:
    print(f"Error: {e}")