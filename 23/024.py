from datetime import datetime

def count_mondays_on_first(start_year, end_year):
    monday_count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if datetime(year, month, 1).weekday() == 0:
                monday_count += 1
    return monday_count

start_year = 2015
end_year = 2016
monday_count = count_mondays_on_first(start_year, end_year)
print(f"Number of Mondays on the 1st day of the month from {start_year} to {end_year}: {monday_count}")