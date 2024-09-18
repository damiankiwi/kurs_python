import pendulum


def time_until_midnight():
    now = pendulum.now()

    midnight = now.end_of('day').add(seconds=1)

    time_difference = midnight - now

    return time_difference

time_until_midnight = time_until_midnight()
print(f"Time until midnight: {time_until_midnight}")