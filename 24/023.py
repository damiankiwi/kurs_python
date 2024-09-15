import pendulum

def get_days_in_month(year, month):
    date = pendulum.datetime(year, month, 1)

    days_in_month = date.days_in_month

    return days_in_month

year = 2024
month = 2
days = get_days_in_month(year, month)
print(f"The number of days in {month}/{year} is {days} days.")