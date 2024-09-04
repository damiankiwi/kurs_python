import pendulum

now = pendulum.now()

new_time = now.add(hours=3, minutes=30)

final_time = new_time.subtract(days=1)

print(f"Current date and time: {now}")
print(f"Date and time after adding 3 hours and 30 minutes: {new_time}")
print(f"Final date and time after subtracting 1 day: {final_time}")