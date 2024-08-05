from datetime import datetime, timezone, timedelta

gmt_time = datetime.now(timezone.utc)

local_time = datetime.now()

print("Current GMT time:", gmt_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
print("Current Local time:", local_time.strftime("%Y-%m-%d %H:%M:%S"))