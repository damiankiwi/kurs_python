import datetime

def days_between_dates(date1, date2):
    return date2 - date1

date1 = datetime.date(2000, 2, 28)
date2 = datetime.date(2001, 2, 28)

difference = days_between_dates(date1, date2)

print("Difference:", difference)