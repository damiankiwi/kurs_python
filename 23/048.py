import calendar


def display_calendar(year, month):
    cal = calendar.TextCalendar(firstweekday=0)

    month_calendar = cal.formatmonth(year, month)

    print(month_calendar)

year = 2024
month = 8
display_calendar(year, month)