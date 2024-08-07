from datetime import datetime

def days_between_dates(date1_str, date2_str, date_format="%Y-%m-%d"):
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    delta = date2 - date1

    return delta.days


date1 = "2000-02-28"
date2 = "2001-02-28"
date_format = "%Y-%m-%d"

days = days_between_dates(date1, date2, date_format)

print(f"Number of days between {date1} and {date2}: {days} days")