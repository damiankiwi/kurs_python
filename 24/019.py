import pendulum

date1 = pendulum.datetime(2023, 9, 10, 10, 0, 0)
date2 = pendulum.datetime(2023, 9, 12, 18, 0, 0)

diff_in_hours = date2.diff(date1).in_hours()

print(f"The difference between the two dates is {diff_in_hours} hours.")