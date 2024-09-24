import pendulum

current_datetime = pendulum.now()

desired_day_of_week = 3

days_to_desired_day = (desired_day_of_week - current_datetime.day_of_week) % 7

new_datetime = current_datetime.add(days=days_to_desired_day)

print(f"Original datetime: {current_datetime}")
print(f"Datetime with the day changed to {desired_day_of_week}: {new_datetime}")