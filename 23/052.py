from datetime import datetime, timedelta

def get_first_and_last_second():
    today = datetime.now().date()

    first_second = datetime.combine(today, datetime.min.time())

    last_second = datetime.combine(today, datetime.max.time())

    return first_second, last_second

first, last = get_first_and_last_second()
print(f"First second: {first}")
print(f"Last second: {last}")