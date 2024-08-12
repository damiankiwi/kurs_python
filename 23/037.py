import datetime

def difference_in_time(date1, date2):
    difference = date2 - date1

    days = difference.days
    seconds = difference.seconds

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return days, hours, minutes, seconds

date1 = datetime.datetime(2024, 8, 9, 14, 30, 0)
date2 = datetime.datetime(2024, 8, 10, 16, 45, 30)

days, hours, minutes, seconds = difference_in_time(date1, date2)

print(f"Difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")