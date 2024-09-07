import pendulum

current_date = pendulum.now()

is_leap_year = current_date.is_leap_year()

if is_leap_year:
    print(f"{current_date.year} is a leap year.")
else:
    print(f"{current_date.year} is not a leap year.")