import pendulum


def time_until_next_saturday():
    now = pendulum.now()

    next_saturday = now.next(pendulum.SATURDAY)

    time_difference = next_saturday - now

    return time_difference

time_until_saturday = time_until_next_saturday()
print(f"Time until next Saturday: {time_until_saturday}")