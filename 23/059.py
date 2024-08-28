import time

def convert_seconds_to_local_time(seconds):
    local_time = time.localtime(seconds)
    time_string = time.strftime("%a %b %d %H:%M:%S %Y", local_time)
    return time_string

seconds_1 = 1618311111
seconds_2 = 236674589

print(convert_seconds_to_local_time(seconds_1))
print(convert_seconds_to_local_time(seconds_2))