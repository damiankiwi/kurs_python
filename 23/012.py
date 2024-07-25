import time

def get_current_time_in_milliseconds():
    current_time_seconds = time.time()

    current_time_milliseconds = int(current_time_seconds * 1000)

    return current_time_milliseconds


current_time_ms = get_current_time_in_milliseconds()
print(f"Current time in milliseconds: {current_time_ms}")