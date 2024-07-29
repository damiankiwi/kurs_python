import datetime

def get_last_tuesday():
    today = datetime.date.today()
    offset = (today.weekday() - 1) % 7
    last_tuesday = today - datetime.timedelta(days=offset)
    return last_tuesday

last_tuesday = get_last_tuesday()
print("The date of the last Tuesday was:", last_tuesday)