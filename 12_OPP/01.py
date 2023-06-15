def uppercase_decorator(func):
    def uppercase_text():
        return func().upper()
    return uppercase_text

@uppercase_decorator
def text():
    return 'Przykładowy tekst'

print(text())