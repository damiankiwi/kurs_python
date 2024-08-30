import time

def tuple_to_string_time(time_tuple):
    time_string = time.asctime(time_tuple)
    return time_string

time_tuple_1 = (2020, 1, 22, 2, 34, 6, 2, 22, -1)
time_tuple_2 = (1982, 11, 12, 2, 54, 8, 2, 316, -1)

print(f"Result: {tuple_to_string_time(time_tuple_1)}")
print(f"Result: {tuple_to_string_time(time_tuple_2)}")