from datetime import datetime

current_datetime = datetime.now()

datetime_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Date and Time as String:", datetime_string)