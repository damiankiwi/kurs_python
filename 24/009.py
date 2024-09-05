import pendulum

date1 = pendulum.datetime(2024, 9, 1)
date2 = pendulum.datetime(2023, 8, 15)

difference = date1.diff_for_humans(date2)

print(f"Difference: {difference}")