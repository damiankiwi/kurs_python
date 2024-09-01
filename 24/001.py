import pendulum

now = pendulum.now()

print("Current date and time:", now.to_datetime_string())
print("Detailed format:", now.format('dddd, MMMM D, YYYY h:mm:ss A'))
