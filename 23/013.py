import datetime

def get_week_number(year, month, day):
    date = datetime.date(year, month, day)

    iso_calendar = date.isocalendar()

    week_number = iso_calendar[1]

    return week_number

sample_date = (2015, 6, 16)
week_number = get_week_number(*sample_date)
print(f"Week number for date {sample_date[0]}-{sample_date[1]}-{sample_date[2]}: {week_number}")