import pendulum

current_date = pendulum.now()

start_of_week = current_date.start_of('week')
end_of_week = current_date.end_of('week')

print(f"Start of the current week: {start_of_week.to_date_string()}")
print(f"End of the current week: {end_of_week.to_date_string()}")