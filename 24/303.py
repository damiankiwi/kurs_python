def call_function(func, *args, **kwargs):

    return func(*args, **kwargs)

def add(x, y):
    return x + y

result = call_function(add, 10, 22)
print(result)

def message(name, text="Good Evening"):
    return f"{name}, {text}!"

result = call_function(message, "Erich", text=...)
print(result)