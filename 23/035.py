import datetime
import time

def date_to_unix_timestamp(year, month, day, hour=0, minute=0, second=0):
    dt = datetime.datetime(year, month, day, hour, minute, second)

    unix_timestamp = int(time.mktime(dt.timetuple()))

    return unix_timestamp

date = date_to_unix_timestamp(2024, 8, 9)
print("Unix Timestamp:", date)