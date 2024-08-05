from datetime import datetime

def date_to_timestamp(date_string, date_format):
    dt = datetime.strptime(date_string, date_format)
    timestamp = datetime.timestamp(dt)
    return timestamp

date_string = "2024-05-26"
date_format = "%Y-%m-%d"
timestamp = date_to_timestamp(date_string, date_format)
print("Date:", date_string)
print("Timestamp:", timestamp)