def bold(func):
    def wrapper(text):
        return f"<b>{func(text)}</b>"
    return wrapper

def italic(func):
    def wrapper(text):
        return f"<i>{func(text)}</i>"
    return wrapper

def underline(func):
    def wrapper(text):
        return f"<u>{func(text)}</u>"
    return wrapper

@bold
@italic
@underline
def format_text(text):
    return text

formatted_text = format_text("Hello, world!")
print("Formatted text:", formatted_text)