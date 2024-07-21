from datetime import datetime, timedelta

current_time = datetime.now()

print("Current time:", current_time)

new_time = current_time + timedelta(seconds=5)

print("Time after adding 5 seconds:", new_time)