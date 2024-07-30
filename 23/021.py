import calendar

def get_last_day(year, month):
    last_day = calendar.monthrange(year, month)[1]
    return last_day

year = 2024
month = 5
print(f"The last day of {year}-{month} is: {get_last_day(year, month)}")

dates = [
    (2024, 2),  # Leap year February
    (2024, 4),  # April
    (2024, 12)  # December
]

for year, month in dates:
    print(f"The last day of {year}-{month} is: {get_last_day(year, month)}")