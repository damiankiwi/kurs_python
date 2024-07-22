from datetime import datetime


def convert_to_day_of_year(year, month, day):
    date = datetime(year, month, day)

    day_of_year = date.timetuple().tm_yday

    return day_of_year


year = 2024
month = 5
day = 26
day_of_year = convert_to_day_of_year(year, month, day)
print(f"The date {year}-{month}-{day} is the {day_of_year} day of the year.")