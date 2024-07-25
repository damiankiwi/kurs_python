import datetime

def get_sundays(year):
    date = datetime.date(year, 1, 1)
    sundays = []

    while date.year == year:
        if date.weekday() == 6:
            sundays.append(date)
        date += datetime.timedelta(days=1)

    return sundays

sample_year = 2024
sundays = get_sundays(sample_year)
for sunday in sundays:
    print(sunday.strftime('%Y-%m-%d'))

print([sunday.strftime('%Y-%m-%d') for sunday in sundays])