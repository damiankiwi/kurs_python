import pendulum

current_date = pendulum.now()

last_day_of_month = current_date.end_of('month')

print(f"The last day of the current month is: {last_day_of_month.to_date_string()}")