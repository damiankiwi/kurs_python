import pendulum

current_date = pendulum.now()

first_day_of_month = current_date.start_of('month')

print(f"The first day of the current month is: {first_day_of_month.to_date_string()}")