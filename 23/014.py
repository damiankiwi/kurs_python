import datetime

def get_first_monday(year, week):
    fourth_jan = datetime.date(year, 1, 4)

    delta = datetime.timedelta(days=fourth_jan.weekday())  # Monday is 0
    first_monday = fourth_jan - delta

    target_date = first_monday + datetime.timedelta(weeks=week - 1)

    return target_date

sample_year = 2015
sample_week = 50
first_monday = get_first_monday(sample_year, sample_week)
print(f"First Monday of week {sample_week} in {sample_year}: {first_monday.strftime('%a %b %d %H:%M:%S %Y')}")