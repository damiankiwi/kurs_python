from datetime import datetime

def convert_string_to_datetime(date_string, date_format):
    return datetime.strptime(date_string, date_format)

date_string = "Jul 1 2014 2:43PM"
date_format = "%b %d %Y %I:%M%p"

converted_datetime = convert_string_to_datetime(date_string, date_format)

print("Converted datetime:", converted_datetime)