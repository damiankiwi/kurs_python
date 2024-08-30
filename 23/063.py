import time

def parse_time_string(time_string, format_string):
    time_struct = time.strptime(time_string, format_string)
    return time_struct

time_strings = [
    ("22 January, 2020", "%d %B, %Y"),
    ("30 Nov 00", "%d %b %y"),
    ("04/11/15 11:55:23", "%d/%m/%y %H:%M:%S"),
    ("12-11-2019", "%d-%m-%Y"),
    ("13::55::26", "%H::%M::%S")
]

for time_str, format_str in time_strings:
    parsed_time = parse_time_string(time_str, format_str)
    print(f"String representing time: {time_str}")
    print(parsed_time)
    print()