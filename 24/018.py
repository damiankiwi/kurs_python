import pendulum

now = pendulum.now()

custom_format = "dddd, MMMM D, YYYY - HH:mm:ss A"

formatted_date = now.format(custom_format)

print(f"Custom formatted date and time: {formatted_date}")