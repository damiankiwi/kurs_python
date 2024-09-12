import pendulum

now = pendulum.now()

unix_timestamp = now.int_timestamp

print(f"Current Unix timestamp: {unix_timestamp}")