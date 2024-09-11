import pendulum

current_datetime = pendulum.now()

time_part = current_datetime.time()
print(f"Current time: {time_part}")