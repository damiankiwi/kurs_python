import calendar

cal = calendar.TextCalendar(firstweekday=6)

year = 2024
month = 8
formatted_month = cal.formatmonth(year, month)

print(formatted_month)