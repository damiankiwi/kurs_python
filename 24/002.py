import pendulum

now = pendulum.now()

tomorrow = now.add(days=1)

print("Tomorrow's date and time:", tomorrow.to_datetime_string())
print("Detailed format:", tomorrow.format('dddd, MMMM D, YYYY h:mm:ss A'))