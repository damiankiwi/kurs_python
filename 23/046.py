import calendar

def create_html_calendar(year, month):
    html_cal = calendar.HTMLCalendar(calendar.SUNDAY)

    html_calendar = html_cal.formatmonth(year, month)

    return html_calendar

year = 2024
month = 8

html_calendar = create_html_calendar(year, month)

print(html_calendar)