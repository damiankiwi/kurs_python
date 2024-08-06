from datetime import datetime

def string_date_to_timestamp(date_string, date_format="%Y-%m-%d %H:%M:%S"):
    dt = datetime.strptime(date_string, date_format)
    timestamp = datetime.timestamp(dt)
    return timestamp

# Example usage
date_string = "2014-07-01 14:43:00"
date_format = "%Y-%m-%d %H:%M:%S"
timestamp = string_date_to_timestamp(date_string, date_format)

print("String Date:", date_string)
print("Timestamp:", timestamp)