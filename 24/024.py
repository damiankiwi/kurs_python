import pendulum

def round_to_nearest_hour():
    now = pendulum.now()

    if now.minute >= 30:
        rounded_time = now.start_of('hour').add(hours=1)
    else:
        rounded_time = now.start_of('hour')

    return rounded_time

rounded_time = round_to_nearest_hour()
print(f"Rounded time to the nearest hour: {rounded_time}")