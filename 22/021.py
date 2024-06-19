import datetime

def find_christmas_sundays(start_year, end_year):
    christmas_sundays = []
    for year in range(start_year, end_year + 1):
        if datetime.date(year, 12, 25).weekday() == 6:
            christmas_sundays.append(year)
    return christmas_sundays

start_year = 2000
end_year = 2150
christmas_sundays = find_christmas_sundays(start_year, end_year)
print("Years when 25th of December is a Sunday between {} and {}:".format(start_year, end_year))
print(christmas_sundays)