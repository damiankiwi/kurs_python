import datetime

def is_third_tuesday(year, month, day):
    date = datetime.date(year, month, day)

    if date.weekday() != 1:
        return False

    first_day_of_month = date.replace(day=1)
    first_tuesday = first_day_of_month + datetime.timedelta(days=(1 - first_day_of_month.weekday() + 7) % 7)

    third_tuesday = first_tuesday + datetime.timedelta(weeks=2)

    return date == third_tuesday


test_date = datetime.date(2024, 5, 21)
print(
    f"Is {test_date} the third Tuesday of the month? {is_third_tuesday(test_date.year, test_date.month, test_date.day)}")

test_dates = [
    datetime.date(2024, 5, 7),
    datetime.date(2024, 5, 14),
    datetime.date(2024, 5, 21),
    datetime.date(2024, 5, 28)
]

for date in test_dates:
    print(f"Is {date} the third Tuesday of the month? {is_third_tuesday(date.year, date.month, date.day)}")