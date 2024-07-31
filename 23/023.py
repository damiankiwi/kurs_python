from datetime import datetime
from dateutil.relativedelta import relativedelta

def add_months(date, months):
    new_date = date + relativedelta(months=months)
    return new_date

date = datetime(2024, 1, 31)
new_date = add_months(date, 1)
print(f"Original date: {date.strftime('%Y-%m-%d')}")
print(f"New date after adding 1 month: {new_date.strftime('%Y-%m-%d')}")

dates = [
    (datetime(2024, 1, 31), 1),  # Adding 1 month to January 31, 2024
    (datetime(2024, 12, 31), 1), # Adding 1 month to December 31, 2024
    (datetime(2023, 2, 28), 1),  # Adding 1 month to February 28, 2023 (non-leap year)
    (datetime(2024, 2, 29), 1)   # Adding 1 month to February 29, 2024 (leap year)
]

for date, months in dates:
    new_date = add_months(date, months)
    print(f"Original date: {date.strftime('%Y-%m-%d')}, New date after adding {months} month(s): {new_date.strftime('%Y-%m-%d')}")