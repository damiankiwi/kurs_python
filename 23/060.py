from datetime import datetime


def print_time_formats():
    now = datetime.now()

    simple_format = now.strftime("%a, %d %b %Y %H:%M:%S + %f")
    print(f"Simple format of time:\n{simple_format}")

    full_format = now.strftime("%A, %m/%d/%y %B %Y %H:%M:%S + %f")
    print(f"\nFull names and the representation:\n{full_format}")

    preferred_format = now.strftime("%a %b %d %H:%M:%S %Y")
    print(f"\nPreferred date time format:\n{preferred_format}")

    example_11_format = now.strftime("%m/%d/%y, %H:%M:%S, %y, %Y")
    print(f"\nExample 11:\n{example_11_format}")

print_time_formats()