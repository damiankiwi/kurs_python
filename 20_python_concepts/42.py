import psutil
import functools
import time

def measure_memory_usage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        start_memory = process.memory_info().rss / 1024 / 1024
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        end_memory = process.memory_info().rss / 1024 / 1024
        print(f"Memory usage for {func.__name__}: {end_memory - start_memory} MB")
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@measure_memory_usage
def example_function():
    numbers = list(range(1, 1000001))
    print("Sum of numbers:", sum(numbers))

example_function()