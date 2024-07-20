from datetime import date, datetime

sample_date = date(2015, 6, 22)

midnight_datetime = datetime.combine(sample_date, datetime.min.time())

print(midnight_datetime)