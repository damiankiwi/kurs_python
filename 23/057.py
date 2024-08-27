import time
from datetime import datetime
import pytz


def display_time_info(tz_name):
    tz = pytz.timezone(tz_name)
    now_naive = datetime.now()  # Naive datetime (bez strefy czasowej)
    now = tz.localize(now_naive)  # Przypisanie strefy czasowej
    is_dst = bool(now.dst())

    print(f"\n{tz_name} :")
    print(f"TZ : {tz_name}")
    print(f"Timezone abbreviations: {tz._tzname}")
    print(f"Timezone : {now.utcoffset().total_seconds()} ({now.utcoffset().total_seconds() / 3600.0})")
    print(f"DST timezone : {1 if is_dst else 0}")
    print(f"Time : {now.strftime('%H:%M:%S %m/%d/%y %Z')}")


# Default Zone
print("Default Zone:")
print(f"TZ : {time.tzname}")
print(f"Timezone abbreviations: {time.tzname}")
print(f"Timezone : {-time.timezone} ({-time.timezone / 3600.0})")
print(f"DST timezone : {time.daylight}")
print(f"Time : {time.strftime('%H:%M:%S %m/%d/%y %Z', time.localtime())}")

# Different timezones
display_time_info('Pacific/Auckland')
display_time_info('Europe/Berlin')
display_time_info('America/Detroit')
display_time_info('Singapore')