import pytz
from datetime import datetime

default_timezone = pytz.timezone('America/New_York')

def get_current_time():
    now_utc = datetime.utcnow()

    now_local = default_timezone.localize(now_utc)

    return now_local

print("Current time with default timezone:", get_current_time())

specific_time = datetime(2023, 8, 9, 15, 0, 0)
specific_time_local = default_timezone.localize(specific_time)

print("Specific time with default timezone:", specific_time_local)