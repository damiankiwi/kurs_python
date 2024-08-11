import datetime

def difference_in_seconds(date1, date2):
    difference = date2 - date1

    total_seconds = difference.total_seconds()

    return total_seconds

date1 = datetime.datetime(2024, 8, 9, 14, 30, 0)
date2 = datetime.datetime(2024, 8, 10, 16, 45, 30)

seconds_diff = difference_in_seconds(date1, date2)
print("Difference in seconds:", seconds_diff)