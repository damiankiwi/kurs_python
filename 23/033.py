from datetime import datetime

def days_between_datetimes(dt1_str, dt2_str, dt_format="%Y-%m-%d %H:%M:%S"):
    dt1 = datetime.strptime(dt1_str, dt_format)
    dt2 = datetime.strptime(dt2_str, dt_format)

    delta = dt2 - dt1

    return delta.days

dt1 = "2023-05-20 14:30:00"
dt2 = "2024-05-25 18:45:00"
dt_format = "%Y-%m-%d %H:%M:%S"

days = days_between_datetimes(dt1, dt2, dt_format)

print(f"Number of days between {dt1} and {dt2}: {days} days")