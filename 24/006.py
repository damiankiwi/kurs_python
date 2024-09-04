import pendulum

date1 = pendulum.date(2024, 8, 9)
date2 = pendulum.date(2025, 2, 25)

difference = date2.diff(date1).in_days()

print(f"The difference between {date1} and {date2} is {difference} days.")