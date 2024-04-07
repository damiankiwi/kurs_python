import functools
import inspect


def enforce_type(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_types = inspect.signature(func).parameters

        for arg_name, arg_value in zip(arg_types, args):
            if arg_name in func.__annotations__:
                if not isinstance(arg_value, func.__annotations__[arg_name]):
                    raise TypeError(
                        f"Argument '{arg_name}' should be of type {func.__annotations__[arg_name].__name__}")

        return func(*args, **kwargs)

    return wrapper

@enforce_type
def add(x: int, y: int) -> int:
    return x + y

try:
    add("1", "2")
except TypeError as e:
    print(e)