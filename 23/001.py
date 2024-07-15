import datetime

now = datetime.datetime.now()

current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_date_time}")

current_year = now.year
print(f"Current year: {current_year}")

month_of_year = now.strftime("%B")
print(f"Month of year: {month_of_year}")

week_number_of_year = now.strftime("%U")
print(f"Week number of the year: {week_number_of_year}")

weekday_of_week = now.strftime("%A")
print(f"Weekday of the week: {weekday_of_week}")

day_of_year = now.strftime("%j")
print(f"Day of year: {day_of_year}")

day_of_month = now.strftime("%d")
print(f"Day of the month: {day_of_month}")

day_of_week = now.strftime("%w")
print(f"Day of week: {day_of_week}")