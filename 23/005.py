from datetime import datetime, timedelta

current_date = datetime.now().date()

new_date = current_date - timedelta(days=5)

print(f"Current Date : {current_date}")
print(f"5 days before Current Date : {new_date}")