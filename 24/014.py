import pendulum

current_date = pendulum.now()

if current_date.day_of_week < 5:
    print(f"{current_date.to_date_string()} is a weekday.")
else:
    print(f"{current_date.to_date_string()} is a weekend.")