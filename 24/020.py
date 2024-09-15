import pendulum

arbitrary_date = pendulum.datetime(2023, 9, 12, 18, 0, 0)

now = pendulum.now()

relative_time = arbitrary_date.diff_for_humans(now)

print(f"The relative time for the given date is: {relative_time}")