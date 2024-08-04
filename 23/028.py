from datetime import datetime, timedelta

today = datetime.today()

date_30_days_before = today - timedelta(days=30)

date_30_days_after = today + timedelta(days=30)

print("Today's date:", today.strftime("%Y-%m-%d"))
print("Date 30 days before today:", date_30_days_before.strftime("%Y-%m-%d"))
print("Date 30 days after today:", date_30_days_after.strftime("%Y-%m-%d"))