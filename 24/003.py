import pendulum

now = pendulum.now()

formatted_time = now.format("YYYY-MM-DD HH:mm:ss")

print("Formatted date and time:", formatted_time)