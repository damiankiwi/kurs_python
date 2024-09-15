import pendulum

def get_timezone_offset():
    now = pendulum.now()

    offset_seconds = now.utcoffset().total_seconds()
    offset_hours = offset_seconds / 3600

    return offset_hours

offset = get_timezone_offset()
print(f"The timezone offset is {offset} hours.")
