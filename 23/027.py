from datetime import datetime, timedelta

def create_fixed_dates(start_date, number_of_dates, days_difference):
    dates = [start_date + timedelta(days=i*days_difference) for i in range(number_of_dates)]
    return dates

start_date = datetime(2024, 1, 1)

number_of_dates = 12
days_difference = 20

fixed_dates = create_fixed_dates(start_date, number_of_dates, days_difference)

for date in fixed_dates:
    print(date.strftime("%Y-%m-%d"))