import calendar

def print_year_calendar(year):
    cal = calendar.TextCalendar(firstweekday=0)

    cal.pryear(year, w=2, l=1, c=6, m=3)


year = 2024

print_year_calendar(year)