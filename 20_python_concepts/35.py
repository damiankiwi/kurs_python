def cache_result(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Result cached for input:", args)
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@cache_result
def add(x, y):
    print("Adding", x, "and", y)
    return x + y

@cache_result
def multiply(x, y):
    print("Multiplying", x, "and", y)
    return x * y

print(add(2, 3))
print(add(2, 3))

print(multiply(2, 3))
print(multiply(2, 3))