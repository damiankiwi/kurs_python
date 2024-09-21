import pendulum

current_date = pendulum.now()

quarter_of_year = (current_date.month - 1) // 3 + 1

print(f"Quarter of the year for the current date ({current_date.format('YYYY-MM-DD')}): {quarter_of_year}")
