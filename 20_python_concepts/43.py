import time
import functools


def cache_with_expiry(expiration_time):
    def decorator(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < expiration_time:
                    print(f"Using cached result for {func.__name__}({args}, {kwargs})")
                    return result

            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        return wrapper

    return decorator


@cache_with_expiry(expiration_time=5)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(5))
print(factorial(3))
print(factorial(3))


time.sleep(6)

print(factorial(5))