from datetime import date, timedelta

today = date.today()

print("Today's date:", today)
print("Next 5 days:")

for i in range(1, 6):
    next_day = today + timedelta(days=i)
    print(next_day)