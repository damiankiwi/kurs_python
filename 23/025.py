import time

def print_string_with_delay(string, repetitions, delay):
    for _ in range(repetitions):
        print(string)
        time.sleep(delay)

print_string_with_delay("Hello, World!", 5, 3)