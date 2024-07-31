import calendar

def get_days_in_month(year, month):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month

year = 2024
month = 2
print(f"The number of days in {year}-{month} is: {get_days_in_month(year, month)}")

dates = [
    (2024, 1),  # January
    (2024, 2),  # February (leap year)
    (2024, 4),  # April
    (2023, 2),  # February (non-leap year)
    (2024, 12)  # December
]

for year, month in dates:
    print(f"The number of days in {year}-{month} is: {get_days_in_month(year, month)}")