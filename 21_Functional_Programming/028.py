import datetime

sample_datetime = datetime.datetime(2020, 1, 15, 9, 3, 32, 744178)

get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S.%f")

print(sample_datetime)
print(get_year(sample_datetime))
print(get_month(sample_datetime))
print(get_day(sample_datetime))
print(get_time(sample_datetime))