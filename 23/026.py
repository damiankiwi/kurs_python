from datetime import datetime
from dateutil.relativedelta import relativedelta

current_date = datetime.now()

six_months_later = current_date + relativedelta(months=6)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date six months later:", six_months_later.strftime("%Y-%m-%d"))