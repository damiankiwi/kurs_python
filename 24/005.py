import pendulum

utc_time = pendulum.now("UTC")

new_york_time = utc_time.in_timezone("America/New_York")

print("Current date and time in UTC:", utc_time)
print("Current date and time in America/New_York:", new_york_time)